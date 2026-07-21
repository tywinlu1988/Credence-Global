#!/usr/bin/env node
/* Credence installer bootstrapper (npx).
 *
 * Downloads the current release package from GitHub Releases, verifies its SHA-256
 * checksum, and unpacks it into a ready-to-open project directory:
 *
 *   npx github:tywinlu1988/credence-global [target-dir] [--tag vX.Y.Z]
 *
 * - target-dir defaults to ./credence
 * - tag defaults to the latest GitHub Release; pin it with --tag or CREDENCE_TAG
 * - CREDENCE_RELEASES_BASE overrides the download base URL (mirror or offline mirror)
 *
 * The release zip is produced by `python scripts/build_dist.py --zip` and attached to
 * the GitHub Release as `<tag>-release.zip` with a `<tag>-release.zip.sha256` sidecar.
 * The zip unpacks to a single top-level `credence/` directory.
 */
const fs = require('fs');
const path = require('path');
const os = require('os');
const http = require('http');
const https = require('https');
const crypto = require('crypto');
const { execFileSync } = require('child_process');

const REPO = 'tywinlu1988/Credence-Global';
const RELEASES_PAGE = `https://github.com/${REPO}/releases`;
const LATEST_API = `https://api.github.com/repos/${REPO}/releases/latest`;
const TAG_RE = /^v\d+\.\d+\.\d+(?:-[A-Za-z0-9-]+)?$/;

function fail(message, hint) {
  console.error(`x ${message}`);
  if (hint) console.error(`  ${hint}`);
  process.exit(1);
}

function parseArgs(argv) {
  let dest = null;
  let tag = process.env.CREDENCE_TAG || null;
  for (let i = 0; i < argv.length; i += 1) {
    if (argv[i] === '--tag') {
      tag = argv[i + 1] || null;
      i += 1;
    } else if (!argv[i].startsWith('--') && dest === null) {
      dest = argv[i];
    }
  }
  return { dest: dest || 'credence', tag };
}

function httpGet(url, redirectsLeft = 5) {
  return new Promise((resolve, reject) => {
    const transport = url.startsWith('http:') ? http : https; // http allowed for local mirrors
    const req = transport.get(url, { headers: { 'User-Agent': 'credence-installer' } }, (res) => {
      if ([301, 302, 303, 307, 308].includes(res.statusCode)) {
        res.resume();
        if (redirectsLeft === 0) return reject(new Error(`too many redirects for ${url}`));
        return resolve(httpGet(new URL(res.headers.location, url).href, redirectsLeft - 1));
      }
      if (res.statusCode !== 200) {
        res.resume();
        const err = new Error(`HTTP ${res.statusCode} for ${url}`);
        err.statusCode = res.statusCode;
        return reject(err);
      }
      const chunks = [];
      res.on('data', (c) => chunks.push(c));
      res.on('end', () => resolve(Buffer.concat(chunks)));
      res.on('error', reject);
    });
    req.setTimeout(60000, () => req.destroy(new Error(`timeout fetching ${url}`)));
    req.on('error', reject);
  });
}

async function resolveTag(tag) {
  if (tag) return tag;
  try {
    const body = await httpGet(LATEST_API);
    const parsed = JSON.parse(body.toString('utf8'));
    if (parsed && typeof parsed.tag_name === 'string') return parsed.tag_name;
  } catch (err) {
    fail(`could not resolve the latest release tag (${err.message}).`,
      `Check ${RELEASES_PAGE} and retry with --tag vX.Y.Z .`);
  }
  fail('latest release lookup returned no tag_name.', `Retry with --tag vX.Y.Z .`);
}

function sha256Hex(buf) {
  return crypto.createHash('sha256').update(buf).digest('hex');
}

function extractZip(zipPath, destDir) {
  // bsdtar (Windows/macOS `tar`) handles zip; GNU tar (Linux) does not — unzip is
  // the Linux fallback; PowerShell Expand-Archive is the Windows last resort.
  const attempts = [];
  const tryCmd = (cmd, args) => {
    try {
      execFileSync(cmd, args, { stdio: 'pipe' });
      return true;
    } catch (err) {
      attempts.push(`${cmd} failed`);
      return false;
    }
  };
  if (tryCmd('unzip', ['-q', zipPath, '-d', destDir])) return;
  if (tryCmd('tar', ['-xf', zipPath, '-C', destDir])) return;
  if (process.platform === 'win32') {
    execFileSync('powershell', [
      '-NoProfile', '-Command',
      `Expand-Archive -LiteralPath ${JSON.stringify(zipPath)} -DestinationPath ${JSON.stringify(destDir)}`,
    ], { stdio: 'pipe' });
    return;
  }
  throw new Error(`no working unzip tool found (${attempts.join(', ')})`);
}

async function main() {
  const { dest, tag: tagArg } = parseArgs(process.argv.slice(2));
  const tag = await resolveTag(tagArg);
  if (!TAG_RE.test(tag)) {
    fail(`refusing suspicious release tag: ${tag}`, 'Expected something like v0.0.1 or v0.0.1-alpha.');
  }

  const destPath = path.join(process.cwd(), dest);
  if (fs.existsSync(destPath)) {
    fail(`target directory already exists: ${destPath}`, 'Pick another name or remove it first.');
  }

  const base = (process.env.CREDENCE_RELEASES_BASE || `https://github.com/${REPO}/releases/download`).replace(/\/+$/, '');
  const asset = `${tag}-release.zip`;
  const zipUrl = `${base}/${tag}/${asset}`;
  const shaUrl = `${zipUrl}.sha256`;

  console.log(`> Credence ${tag}`);
  console.log(`> downloading ${zipUrl}`);
  let zipBuf;
  try {
    zipBuf = await httpGet(zipUrl);
  } catch (err) {
    fail(`download failed: ${err.message}`, `Get ${asset} manually from ${RELEASES_PAGE}`);
  }

  // SHA-256 verification: a mismatch is fatal; a missing sidecar only warns (early releases
  // may predate the sidecar, but once published it must match).
  try {
    const shaBody = (await httpGet(shaUrl)).toString('utf8').trim().split(/\s+/)[0];
    const actual = sha256Hex(zipBuf);
    if (shaBody.toLowerCase() !== actual) {
      fail(`checksum mismatch for ${asset}: expected ${shaBody}, got ${actual}.`,
        'The download is corrupted or tampered with — aborting.');
    }
    console.log('> checksum verified (sha256)');
  } catch (err) {
    if (err.statusCode === 404) {
      console.warn('! no .sha256 sidecar attached to this release — skipping checksum verification');
    } else {
      fail(`could not verify checksum: ${err.message}`, 'Retry, or download manually from ' + RELEASES_PAGE);
    }
  }

  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'credence-install-'));
  try {
    const zipPath = path.join(tmp, asset);
    fs.writeFileSync(zipPath, zipBuf);
    const unpackDir = path.join(tmp, 'unpacked');
    fs.mkdirSync(unpackDir);
    extractZip(zipPath, unpackDir);

    // Expect a single top-level directory (credence/) inside the zip.
    const entries = fs.readdirSync(unpackDir, { withFileTypes: true }).filter((e) => e.isDirectory());
    if (entries.length !== 1) {
      fail(`unexpected zip layout: expected a single top-level directory, found ${entries.length}.`,
        'The release zip may be malformed — report this at ' + RELEASES_PAGE);
    }
    fs.cpSync(path.join(unpackDir, entries[0].name), destPath, { recursive: true });
  } finally {
    fs.rmSync(tmp, { recursive: true, force: true });
  }

  console.log(`v Credence ${tag} installed to ${destPath}`);
  console.log('');
  console.log('Next: open that folder as a project in your agent CLI and ask in plain language,');
  console.log('e.g. "analyze this company" or "check this portfolio". See INSTALL.md / AGENTS.md inside.');
}

main().catch((err) => fail(err.message));
