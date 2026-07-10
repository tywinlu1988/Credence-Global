import re

files = {
    'dev/reports/medicaldevice-mindray-credit-report.html': [
        ('card-green', 'signal-green', '信用利差', '利差稳定·AAA评级·现金储备充裕'),
        ('card-green', 'signal-green', '波动率', '股价波动率处于历史中低位·北向持仓稳定'),
        ('card-green', 'signal-green', '资金流向', '北向资金持仓稳定·海外收入占比53%对冲风险'),
        ('card-green', 'signal-green', '评级事件', '主体评级维持AAA·无负面展望'),
    ],
    'dev/reports/medicaldevice-lepu-credit-report.html': [
        ('card-amber', 'signal-amber', '信用利差', '集采承压·利差小幅走阔·转型不确定性溢价'),
        ('card-amber', 'signal-amber', '波动率', '股价波动率略高于同业·集采政策不确定性持续'),
        ('card-green', 'signal-green', '资金流向', '北向持仓比例稳定·机构投资者未明显减持'),
        ('card-amber', 'signal-amber', '评级事件', '评级维持BBB+·展望稳定'),
    ],
}

for fname, signals in files.items():
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    new_cards = '  <div class="grid-2">\n'
    for card_class, sig_class, title, desc in signals:
        new_cards += f'    <div class="card {card_class}"><h3><span class="signal {sig_class}"></span>{title}</h3><p>{desc}</p></div>\n'
    new_cards += '  </div>'

    html = re.sub(r'\.signal-card\s*\{[^}]*\}\s*', '', html)
    html = re.sub(r'\.signal-card\s+\.signal-[a-z]+\s*\{[^}]*\}\s*', '', html)

    html = re.sub(
        r'(<h2 class="section-title">市场定价信号 · 轨道B</h2>.*?)<div class="grid-2">.*?</div>\s*</div>\s*\n\s*<div class="section">',
        r'\1' + new_cards + '\n</div>\n\n<div class="section">',
        html, flags=re.DOTALL
    )

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'{fname}: done')
