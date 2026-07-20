# Credence · Moteur d'Analyse de Crédit Obligataire

> **Un moteur d'analyse de crédit axé sur la méthodologie pour les marchés obligataires mondiaux** — livré sous forme de **Agent Skills** (`SKILL.md`), installable dans Claude Code, Codex, Cursor, Gemini et OpenCode. Conçu pour les professionnels du crédit qui ont besoin d'une analyse de crédit rigoureuse, reproductible et transparente au-dela des mesures financières traditionnelles.

<p align="center">
  <strong>Version <code>v0.0.2</code></strong> ·
  <strong>Licence</strong> Source visible · Non commercial ·
  <strong>Tests</strong> suite de regression pytest + portes de coherence · CI Python 3.11 &amp; 3.12 ·
  <strong>27 documents méthodologiques</strong>
</p>

<p align="center">
  🌐 <a href="README.md">English</a> ·
  <a href="README.zh.md">中文</a> ·
  <a href="README.ja.md">日本語</a> ·
  <a href="README.ko.md">한국어</a> ·
  <a href="#"><strong>Français</strong></a>
</p>

> 📝 *This is a community translation. The canonical version is the [English README](README.md).*

---

## Table des matieres

- [Qu'est-ce que Credence](#quest-ce-que-credence)
- [Architecture du moteur](#architecture-du-moteur)
  - [Couche 1 : Moteur Mosaique](#couche-1--moteur-mosaique)
  - [Couche 2 : Moteur Double Voie](#couche-2--moteur-double-voie)
  - [Couche 3 : Moteur Multi-Parties Prenantes](#couche-3--moteur-multi-parties-prenantes)
  - [Couche 4 : Couche d'Intelligence Systemique](#couche-4--couche-dintelligence-systemique)
- [Le Pipeline en Quatre Etapes](#le-pipeline-en-quatre-etapes)
- [Paradigmes Internationaux et Chemins de Travail](#paradigmes-internationaux-et-chemins-de-travail)
- [Demarrage Rapide](#demarrage-rapide)
- [Compatibilite des CLI Agent](#compatibilite-des-cli-agent)
- [Plan du Depot](#plan-du-depot)
- [FAQ](#faq)
- [Licence et Avertissement](#licence-et-avertissement)

---

## Qu'est-ce que Credence

Credence transforme la methodologie d'un analyste de credit obligataire experimente en une forme qu'un agent IA peut charger et executer directement. Ce n'est **ni un framework d'agents ni une application autonome** — c'est un **pack de competences methodologiques domaine** concu pour l'analyse de credit de qualite institutionnelle sur les marches obligataires internationaux.

### Principe Fondamental

L'analyse financiere traditionnelle repose sur une hypothese implicite — que le risque de credit d'une entreprise peut etre lu dans ses etats financiers. Cette hypothese echoue systematiquement dans trois archetypes industriels :

| Type d'Industrie | Pourquoi l'Analyse Financiere Echoue | Emplacement du Facteur le Plus Lourd |
|---|---|---|
| **Pilotee par les Politiques** (Solaire, Semi-conducteurs) | Les cycles politiques determinent les plafonds de demande ; des changements brusques peuvent devaster une industrie en semaines | Politique industrielle / Geopolitique (hors bilan) |
| **A Barriere Technologique** (Equipements avances, Biopharmacie) | Les actifs cores (PI, pipeline, certifications) sont hors bilan ; de nombreuses firmes sans revenus ne peuvent etre evaluees par PER/VCP | Feuille de route technologique / PI core (hors bilan) |
| **A Actifs en Location** (Centres de donnees, REITs d'infrastructure) | Profil type REIT ; les indicateurs cles sont le NOI/DSCR plutot que les indicateurs financiers traditionnels | Qualite des baux clients (hors bilan) |

**Les facteurs de credit les plus lourds ne figurent jamais au bilan.** Les notations de credit externes sont en retard de 17 mois ou plus sur la deterioration reelle du credit (Enron, Lehman Brothers, Wirecard, Grece souveraine — tous notes « investment grade » quelques mois avant le defaut).

### Deux Fondements Theoriques

| Theorie | Implication | Implementation dans le Moteur |
|---|---|---|
| **Theorie de la Mosaique** | Les fragments de donnees publiques individuels sont denues de sens isolement ; assembles, ils forment une image complete | Agrégation multi-source, empilement de signaux, pondération par confiance |
| **Theorie de la Completude de l'Information** | Les lacunes de donnees ne sont pas des defauts — ce sont des signaux de risque. "Nous n'avons pas ces donnees" indique en soi qu'une dimension comporte une incertitude | Chaque conclusion d'analyse est accompagnee d'un score de completude et d'une liste de lacunes |

### Architecture d'Ensemble

```
Couche d'Intelligence Systemique (Couche 4)
  Carte de Contagion x Tableau de Bord de Concentration x Indice de Risque Systemique (SRI)
                        |
                  Resultats d'un emetteur unique
                        |
              ┌─────────┴─────────┐
              │  Moteur Mosaique  │   Extraction + assemblage + completude
              │   (Couche 1)      │
              └─────────┬─────────┘
                        |
           ┌────────────┼────────────┐
           │            │            │
      Voie A         Voie B       Voie C+: Multi-Parties Prenantes
    Analyse         Prix du        6 roles buy-side
   Fondamentale     Marché
           │            │
           └──────┬─────┘
                  ▼
      Matrice de Validation Croisee
    Consensus -> Renforcement mutuel
    Divergence -> Apercu le plus precieux
                  │
                  ▼
          Sortie Integree
    Notation + Signaux + Rapport de Completude
```

---

## Architecture du Moteur

### Couche 1 : Moteur Mosaique

**Extraction de signaux a partir de donnees publiques fragmentees.**

Le moteur mosaique fonctionne comme la couche d'entree de donnees de l'ensemble du pipeline d'analyse. Il ingere des donnees publiques non structurees multi-sources et les transforme en signaux structures ponderes par confiance, prets pour l'analyse double voie en aval.

#### Extraction de Signaux

Le moteur collecte des donnees aupres de sept categories de sources publiques — politique macro, donnees sectorielles, prix de la chaine d'approvisionnement, documents d'entreprise, dossiers contentieux/reglementaires, donnees du marche obligataire et indicateurs macroeconomiques — le tout via des canaux publics gratuits (WebSearch, SEC EDGAR, portails des banques centrales, FRED, TRACE, etc.).

#### Assemblage en Mosaique

Les points de donnees individuels sont assembles en une mosaique alignee sur la pyramide sectorielle a l'aide d'un moteur de regles. Le processus d'assemblage empile les signaux par fiabilite de la source, actualite temporelle et corroboration multi-source, produisant une carte de signaux structuree pour chaque emetteur.

#### Evaluation de la Completude

Chaque conclusion d'analyse comprend un **score de completude** quantitatif (0-100) et une liste explicite des lacunes. Le moteur distingue :

- **Les connus connus** — points de donnees confirmes par plusieurs sources
- **Les connus inconnus** — lacunes de donnees identifiees et signalees comme risques
- **Les inconnus inconnus** — angles morts structurels documentes comme limitations methodologiques

#### Indicateurs Cles

| Indicateur | Description |
|---|---|
| Score de Completude | 0-100 par dimension d'analyse |
| Confiance du Signal | Confiance ponderee par la source pour chaque signal extrait |
| Impact des Lacunes | Evaluation qualitative de l'impact de chaque lacune sur la fiabilite de la notation |

---

### Couche 2 : Moteur Double Voie

**Validation croisee entre l'analyse fondamentale (Voie A) et les signaux de prix de marche (Voie B).**

Le moteur double voie execute deux pistes d'analyse independantes en parallele, puis valide croise leurs sorties. La divergence entre les pistes genere les apercus les plus precieux du moteur.

#### Voie A : Analyse Fondamentale

Applique le cadre de la pyramide sectorielle — un systeme de notation a dix dimensions (D1-D10) qui evalue :

| Dimension | Point de Mire |
|---|---|
| D1-D3 | Position sectorielle structurelle, environnement politique, fosse competitif |
| D4-D6 | Resilience du modele d'affaires, stabilite des revenus, structure des couts |
| D7-D8 | Politique financiere, structure du capital, liquidite |
| D9-D10 | Gouvernance, antecedents de la direction, soutien externe |

La notation suit une progression stricte couche par couche : la couche 1 (facteurs structurels les plus lourds) doit etre passee avant que l'analyse de la couche 2 ait un sens ; les couches ne peuvent pas etre sautees. La couche financiere (L4) sert de couche de validation pour les jugements des couches superieures.

#### Voie B : Signaux de Prix de Marche

Analyse quatre niveaux de signaux implicites du marche :

| Niveau de Signal | Indicateurs |
|---|---|
| Spreads de Credit | Z-spread, swap d'actifs, prime CDS |
| Volatilite | Volatilite des prix, skew de volatilite implicite |
| Flux de Fonds | Demande primaire, rotation secondaire, composition des investisseurs |
| Migration de Notation | Tendances des notations externes, changements de perspective, listes de surveillance |

#### Matrice de Validation Croisee

| Voie A / Voie B | Signaux Positifs | Signaux Negatifs |
|---|---|---|
| **Positifs** | **Renforcement Mutuel** — haute confiance | **Voie B Pionniere** — le marche precede les fondamentaux |
| **Negatifs** | **Voie A Pionniere** — les fondamentaux se degradent avant les prix | **Confirmation Mutuelle** — certitude elevee de difficulte |

En cas de conflit, **la Voie A (faits financiers publics auditables) a priorite** sur les notations externes.

#### Correspondance des Notations

Le score composite interne de 0 a 10 est aligne sur les trois grandes agences internationales selon une echelle de 18 crans -- **un score plus eleve signifie une meilleure notation** (9.5-10.0 = AAA en haut, 0-0.9 = D en bas) ; un veto en une voix plafonne la notation composite a CCC. L'alignement cran par cran avec S&P / Moody's / Fitch a pour source unique `dev/engine/dual-track-methodology.md` §6 et n'est pas duplique ici.

**Cadre financier** : Les normes IFRS (International Financial Reporting Standards) et US GAAP (Generally Accepted Accounting Principles) sont toutes deux supportees, avec detection automatique du referentiel a partir des depots de l'emetteur et ajustement pour les differences cles (capitalisation des credits-bails, capitalisation de la R&D, reconnaissance des impots differes).

---

### Couche 3 : Moteur Multi-Parties Prenantes

**Six roles buy-side avec matrice d'analyse inter-roles.**

Les differents acteurs du marche regardent le meme credit a travers des lentilles differentes. Le moteur multi-parties prenantes execute des evaluations paralleles sur six roles buy-side, puis construit une matrice de comparaison croisee qui met en evidence les consensus et les divergences.

#### Les Six Roles

| # | Role | Decision Centrale | Horizon | Besoins de Donnees Cles |
|---|---|---|---|---|
| 1 | **Selectionneur de Credit** | "Ce credit a-t-il sa place dans le portefeuille ?" — notation emetteur unique, probabilite de defaut | 12-36 mois | Pyramide sectorielle, analyse financiere approfondie, LGD/recouvrement, soutien externe |
| 2 | **Gestionnaire de Portefeuille** | "Est-ce le meilleur risque/rendement ?" — valeur relative, allocation sectorielle | 6-24 mois | Metriques de valeur relative, analyse comparative, positionnement de courbe |
| 3 | **Responsable des Risques** | "Ou sont les points chauds de concentration/contagion ?" — surveillance des risques de portefeuille | Continu (SRI mensuel + evenementiel) | Tableau de bord de concentration, matrice de contagion, SRI, tests de resistance |
| 4 | **Trader** | "Est-ce le jour d'agir ?" — execution, timing de marche | Intra-journalier a 2 semaines | Carte de signaux L0, spreads en temps reel, conditions de liquidite |
| 5 | **Conseiller** | "Que devrait faire mon client ?" — conseil d'allocation, adequation | 3-12 mois | Superposition du profil de risque client, apercu L1, vues thematiques |
| 6 | **Investisseur Individuel** | "Devrais-je posseder cette obligation ?" — decision d'investissement personnel | 6-36 mois | L0/L1 simplifies, signal achat/conservation/vente, resume de risque en langage clair |

#### Matrice Inter-Roles

Lorsque plusieurs parties prenantes analysent le meme emetteur, le moteur construit une matrice consensus/divergence :

| Aspect | Scenario de Consensus | Scenario de Divergence |
|---|---|---|
| Qualite de Credit | Tous les roles s'accordent sur la direction de la notation | Selectionneur haussier, Responsable des risques baissier -> enquete approfondie |
| Appetit pour le Risque | GP et Responsable des risques s'alignent sur la concentration | Trader voit une opportunite court terme, Responsable des risques avertit du risque de queue |
| Horizon Temporel | Les signaux de tous les roles pointent vers la meme fenetre de declenchement | Des horizons temporels divergents exposent un risque de decalage d'echeance |

Cette matrice inter-roles a ete demontree dans l'etude de cas Brilliance Auto, ou les perspectives de differents roles ont revele des faiblesses structurelles que l'analyse a role unique avait manquees.

---

### Couche 4 : Couche d'Intelligence Systemique

**Perception du risque systemique inter-emetteurs — contagion, concentration et alerte precoce.**

La couche d'intelligence systemique (SIL) est la couche d'agregation la plus elevee, chargee de detecter les schemas de risque systemique qu'aucune analyse d'emetteur unique ne peut reveler. Elle comprend trois modules integres et un quatrieme moteur de surveillance code.

#### Matrice de Contagion (19 Industries Internationales)

Une matrice complete d'intensite de contagion inter-industrielle 19x19 basee sur la norme GICS (Global Industry Classification Standard), couvrant tous les grands secteurs economiques internationaux :

| # | Industrie | Paradigme Principal | Role de Contagion |
|---|---|---|---|
| 1 | Energie (Petrole & Gaz) | P1 : Pilote par les Politiques | Super-propagateur (forte contagion sortante) |
| 2 | Chimie | P1 : Pilote par les Politiques | Transmetteur modere |
| 3 | Metaux & Mines | P3 : Jeu a Somme Nulle | Amplificateur cyclique |
| 4 | Materiaux de Construction | P4 : Location d'Actifs | Transmetteur lie aux infrastructures |
| 5 | Biens d'Equipement | P2 : Barriere Technologique | Hub de contagion manufacturiere |
| 6 | Services Commerciaux | P6 : Reseau + Trafic | Faible lien systemique |
| 7 | Transport | P4 : Location d'Actifs | Vecteur de transmission logistique |
| 8 | Automobiles | P3 : Jeu a Somme Nulle | Pont consommation-industrie |
| 9 | Biens de Consommation Durables | P5 : Marque + Canal | Recepteur cyclique de la demande |
| 10 | Biens de Consommation de Base | P5 : Marque + Canal | Defensif, faible contagion |
| 11 | Commerce de Detail | P6 : Reseau + Trafic | Recepteur de transmission de la demande finale |
| 12 | Materiel Technologique (Semi-conducteurs) | P2 : Barriere Technologique | Super-propagateur de contagion geopolitique |
| 13 | Logiciels & Services | P2 : Barriere Technologique | Faible contagion directe, fort effet de recit |
| 14 | Biotechnologie & Pharmacie | P2 : Barriere Technologique | Recepteur de choc reglementaire |
| 15 | Equipement Medical | P2 : Barriere Technologique | Faible contagion cyclique |
| 16 | Services Publics (Reglementes) | P4 : Location d'Actifs | Defensif, faible contagion |
| 17 | Telecommunications | P4 : Location d'Actifs | Recepteur de contagion d'infrastructure |
| 18 | Finance (Banques/Assurance) | P1 : Pilote par les Politiques | **Super-propagateur systemique** (plus forte contagion sortante) |
| 19 | Souverains & ESE | P1 : Pilote par les Politiques | Facteur de risque fondamental |

Les mesures derivees cles incluent le Coefficient de Contagion Directe (CFC), le Coefficient de Vulnerabilite a la Contagion (CVC) et le Ratio d'Exposition Nette a la Contagion (CNER), ainsi que des tables d'escalade de stress pour les sauts d'intensite specifiques aux facteurs.

#### Tableau de Bord de Concentration Cinq Dimensions

Evalue le risque de concentration du portefeuille sur cinq dimensions independantes :

| Dimension | Evaluation |
|---|---|
| Concentration Sectorielle | CR3 / CR5 / HHI / MAX1 par secteur GICS |
| Concentration Regionale | Part d'un seul pays/region + part des regions fragiles |
| Concentration de Notation | Part des AAA externes + part des pseudo-hautes notations |
| Concentration d'Echeance | Part des echeances a 12 mois + pic sur un mois |
| Concentration des Canaux de Financement | Part du premier canal + statut de contraction |

Les seuils, les bandes de feux tricolores et l'impact en crans de chaque dimension ont pour source unique `dev/engine/concentration-framework.md` et ne sont pas dupliques ici.

#### Indice de Risque Systemique (SRI) avec Thermometre a Quatre Niveaux

Le SRI agrege des signaux multi-sources en une seule lecture de risque systemique, visualisee sous forme de thermometre a quatre niveaux :

| Niveau du Thermometre | Plage SRI (echelle 0-3+) | Signification |
|---|---|---|
| 🟢 Normal | inferieure a 0.5 | Risque systemique dans les limites normales |
| 🟡 Veille | 0.5 - 1.0 | Risque eleve dans certains secteurs |
| 🟠 Alerte | 1.0 - 1.8 | Accumulation generalisee du risque |
| 🔴 Danger | 1.8 et plus | Stress systemique imminent |

Le SRI utilise une echelle continue de 0 a 3+ -- jamais un systeme en pourcentage. Les definitions des niveaux et les actions prescrites ont pour source unique `dev/engine/systemic-warning-framework.md` §3. Le moteur de calcul du SRI (`src/sri_calculator.py`) implemente l'algorithme d'agregation ; le niveau du thermometre alimente la carte de signaux L0 et declenche l'escalade dans l'ensemble du pipeline en quatre etapes.

#### Moteur de Surveillance des Perspectives

Le quatrieme moteur code (`src/outlook_engine.py`) fournit :

- **Evaluation des perspectives de notation sur 12-24 mois** avec probabilite directionnelle
- **Liste de surveillance a 90 jours** avec conditions de declenchement automatiques
- **Matrice de migration des notations** avec probabilites de transition historiques
- **Declencheurs de surveillance continue** qui se propagent via le registre des chemins de travail

---

## Le Pipeline en Quatre Etapes

Chaque analyse de credit transite par un pipeline chaine en quatre etapes, avec `path_id` comme cle de jointure entre les etapes :

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ ① Admission│ -> │ ② Analyse│ -> │ ③ Rapport│ -> │ ④ AQ    │
│ (Routeur) │    │ (Moteur) │    │ (Constructeur)│ │ (Verificateur)│
└──────────┘    └──────────┘    └──────────┘    └──────────┘
```

| Etape | Nom | Livrable | Competence Hote | Statut |
|---|---|---|---|---|
| S1 | **Admission** | Fiche de Chemin de Travail | `credit-analysis-router` | ✅ Livre |
| S2 | **Analyse** | Sortie d'Analyse | `fixed-income-credit-analysis` | ✅ Livre |
| S3 | **Rapport** | Ordre de Livraison | `credit-report-builder` | ✅ Livre |
| S4 | **AQ** | Decision AQ | `credit-qa-verifier` | ✅ Livre |

**S1 — Admission (Routeur)** : La competence `credit-analysis-router` utilise un mecanisme de routage a quatre questions pour classer les demandes vagues des utilisateurs en une **Fiche de Chemin de Travail** concrete. La fiche porte un `path_id`, un ordre de lecture du moteur, une selection de template et des specifications de portes qualite — le tout derive de la source unique de verite dans `dev/engine/work-path-registry.md`.

**S2 — Analyse** : La competence `fixed-income-credit-analysis` execute l'analyse selon l'ordre de lecture du moteur de la fiche de chemin. Pour quatre chemins cables, l'orchestrateur (`src/pipeline.py`) invoque directement le moteur code correspondant :
- **WP-RO-01** -> `src/concentration_scorer.py` (concentration cinq dimensions)
- **WP-RO-02** -> `src/contagion_engine.py` (matrice de contagion)
- **WP-RO-03** -> `src/sri_calculator.py` (indice de risque systemique)
- **WP-X-05** -> `src/outlook_engine.py` (surveillance des perspectives)

Tous les chemins non cables sont orchestres par LLM selon la documentation du moteur.

**S3 — Rapport** : La competence `credit-report-builder` assemble l'analyse completee en un rapport HTML livrable. La selection du template (Type 1-18) suit les specifications de la fiche de chemin et correspond au systeme de sortie a trois niveaux L0/L1/L2 :
- **L0** (Carte de Signaux) — Resume en 5 secondes : notation, perspectives, signaux cles du jour
- **L1** (Apercu) — Tableau de bord d'une page avec graphiques radar et liste d'anomalies cles
- **L2** (Analyse Approfondie) — Rapport d'analyse complet avec pyramide hierarchique et validation croisee

**S4 — AQ** : La competence `credit-qa-verifier` effectue un examen de porte qualite avant livraison, appliquant les regles de densite des signaux, la conformite au plafond de veto unique, les garde-fous du Mode B et l'integrite de la source unique de verite. C'est l'etape terminale de la chaine en quatre etapes — aucun rapport n'est livre sans avoir passe l'AQ.

**Orchestrateur Executable** : `src/pipeline.py` pilote l'ensemble de la chaine en quatre etapes dans le code. Il lit les definitions d'etape depuis `dev/engine/pipeline-contract.md` (ne code jamais en dur les noms d'etape), valide les fiches de chemin via `src/path_sheet.py`, et invoque les moteurs codes uniquement pour les chemins explicitement cables. La source unique de verite pour les quatre artefacts (fiche de chemin, artefact d'analyse, fiche de livraison, decision AQ) et leurs aretes de chainage est `dev/engine/pipeline-contract.md`.

---

## Paradigmes Internationaux et Chemins de Travail

### Six Paradigmes Internationaux (P1-P6)

Le moteur classe toutes les industries en six paradigmes analytiques, chacun avec des modeles de ponderation, des priorites de notation et des accents factoriels distincts :

| Paradigme | Code | Industries Cles | Facteur Differentiateur Cles |
|---|---|---|---|
| **Cyclique** | P1 | Energie (Petrole & Gaz), Chimie, Finance, Souverains & ESE | Les cycles politiques et de matieres premieres determinent les plafonds de demande |
| **Defensif** | P2 | Biens d'Equipement, Materiel Technologique, Logiciels, Biotech & Pharma, Equipement Medical | L'intensite de R&D et la PI creent des fosses durables |
| **Croissance** | P3 | Metaux & Mines, Automobiles | Dynamique competitive a somme nulle ; la concurrence par les prix erode les marges |
| **Service Public Reglemente** | P4 | Materiaux de Construction, Transport, Services Publics, Telecommunications | Profil de location d'actifs ; le NOI/DSCR sont les mesures cles |
| **Financier** | P5 | Biens de Consommation Durables, Biens de Consommation de Base | La valeur de la marque et les reseaux de distribution generent de la valeur |
| **Lie au Souverain** | P6 | Services Commerciaux, Commerce de Detail | Effets de reseau et economie de plateforme |

### 16 Chemins de Travail

Le moteur definit **16 chemins de travail** mappes aux roles buy-side internationaux, chacun specifiant une sequence de moteur, un template de rapport et des exigences de porte qualite.

#### Par Role

**Selectionneur de Credit (2 chemins)**
| ID | Chemin | Statut | Sortie |
|---|---|---|---|
| WP-CS-01 | Notation d'Emetteur Unique | ✅ Actif | Notation + Signaux + Rapport de Completude |
| WP-CS-02 | Module Complementaire LGD + Soutien Externe | 🟡 Partiel | Niveau LGD + Taux de Recouvrement + Ajustement de Soutien |

**Gestionnaire de Portefeuille (2 chemins)**
| ID | Chemin | Statut | Sortie |
|---|---|---|---|
| WP-PM-01 | Tableau de Bord d'Investissement | ✅ Actif | Score Quatre Dimensions + Recommandation d'Investissement |
| WP-PM-02 | Analyse Comparative | 🟡 Partiel | Score de Comparaison + Conclusion de Differentiation |

**Responsable des Risques (4 chemins)**
| ID | Chemin | Statut | Sortie |
|---|---|---|---|
| WP-RO-01 | Evaluation de la Concentration | ✅ Actif | Score de Concentration Cinq Dimensions + Recommandations d'Ajustement |
| WP-RO-02 | Contagion Inter-Industrielle | ✅ Actif | Carte des Chemins de Contagion + Recommandations d'Ajustement |
| WP-RO-03 | Lecture du Risque Systemique | ✅ Actif | Lecture SRI + Niveau du Thermometre |
| WP-RO-04 | Test de Resistance du Portefeuille | 🟡 Partiel | Pertes de Scenario de Stress + Resultats de Saut de Seuil |

**Trader (1 chemin)**
| ID | Chemin | Statut | Sortie |
|---|---|---|---|
| WP-TR-01 | Carte de Signaux de Surveillance du Marche | 🟡 Partiel | Carte de Signaux L0 + Lecture du Thermometre |

**Conseiller (1 chemin)**
| ID | Chemin | Statut | Sortie |
|---|---|---|---|
| WP-AD-01 | Evaluation d'Origination | 🔴 Planifie | Faisabilite de Souscription + Fourchette de Prix |

**Investisseur Individuel (1 chemin)**
| ID | Chemin | Statut | Sortie |
|---|---|---|---|
| WP-II-01 | Soutien a la Decision | 🔴 Planifie | Comparaison des Canaux de Financement + Recommandation de Calendrier |

**Meta / Usage Special (5 chemins)**
| ID | Chemin | Statut | Sortie |
|---|---|---|---|
| WP-X-01 | Validation par Backtest Cygne Noir | ✅ Actif | Conclusion de Validation + Ameliorations du Cadre |
| WP-X-02 | Evaluation Parallele Multi-Roles | ✅ Actif | Matrice de Scores Multi-Roles + Rapport Consensus/Divergence |
| WP-X-03 | Constructeur de Cadre Sectoriel | ✅ Actif | Pyramide Sectorielle + Scores D1-D10 |
| WP-X-04 | Analyse des Risques ESG/Gouvernance | 🟡 Partiel | Analyse des Risques ESG + Liste de Drapeaux Rouges de Gouvernance |
| WP-X-05 | Perspectives et Surveillance Continue | ✅ Actif | Perspectives de Notation + Liste de Surveillance |

**Resume des statuts** : 8 actifs, 6 partiels, 2 planifies.

### Templates de Rapport (Type 1-18)

Chaque chemin de travail correspond a un ou plusieurs templates de rapport HTML :

| Template | Type | Utilise Par |
|---|---|---|
| Type 1 | Analyse Approfondie d'Emetteur Unique | WP-CS-01 |
| Type 2 | Analyse Comparative | WP-PM-02 |
| Type 3 | Validation par Backtest | WP-X-01 |
| Type 4 | Matrice Multi-Roles | WP-X-02 |
| Type 5 | Tableau de Bord GP | WP-PM-01 |
| Type 6 | Carte Resume de Notation | WP-CS-01 |
| Type 7 | Cadre Sectoriel | WP-X-03 |
| Type 8 | Evaluation LGD | WP-CS-02 |
| Type 9 | Soutien Externe | WP-CS-02 |
| Type 10 | Analyse ESG/Gouvernance | WP-X-04 |
| Type 11 | Test de Resistance | WP-RO-04 |
| Type 12 | *Reserve* | — |
| Type 13 | Carte de Contagion | WP-RO-02 |
| Type 14 | Tableau de Bord de Concentration | WP-RO-01 |
| Type 15 | Thermometre SRI | WP-RO-03 |
| Type 16 | *Planifie (Origination)* | WP-AD-01 |
| Type 17 | *Planifie (Conseil)* | WP-II-01 |
| Type 18 | Surveillance des Perspectives | WP-X-05 |

---

## Demarrage Rapide

**Premisse cle** : les competences NE sont PAS autonomes — a l'execution, elles lisent `engine/` et `templates/` depuis la **racine du package** (source unique de verite, jamais copiee). L'unite d'installation est la racine entiere du package ; **ouvrez la racine du package comme votre projet** et tout se resout sans copie.

### A. npx (Recommande)

```bash
npx github:tywinlu1988/credence-global
```

Telecharge la derniere archive zip depuis GitHub Releases, verifie sa somme de controle SHA-256, puis la decompresse dans `./credence/` ; ouvrez ce dossier avec votre CLI agent. Epinglez une version precise avec `--tag vX.Y.Z`.

### B. GitHub Release

Telechargez le dernier `vX.Y.Z-release.zip` depuis la [page Releases](https://github.com/tywinlu1988/Credence-Global/releases), verifiez-le avec le fichier `vX.Y.Z-release.zip.sha256` joint, dezippez, et ouvrez la racine du package comme projet.

### C. Cloner la Source

```bash
git clone git@github.com:tywinlu1988/Credence-Global.git
cd credence-global
pip install -e .
```

### D. Execution des Tests

```bash
python -m pytest tests/ -q          # suite de regression complete
python scripts/consistency_check.py  # Validation de coherence inter-documents
```

### Premieres Etapes

1. Ouvrez la racine du package dans votre CLI agent
2. Commencez une conversation : *"Analysez l'entreprise XYZ dans le secteur des semi-conducteurs"*
3. La competence `credit-analysis-router` achemine votre demande vers un chemin de travail
4. L'execution suit le pipeline en quatre etapes : admission -> analyse -> rapport -> AQ
5. Un rapport HTML d'analyse approfondie Type-1 ou un resume de notation Type-6 est produit

Pour la documentation detaillee du moteur, voir `dev/engine/engine-overview.md`.

---

## Compatibilite des CLI Agent

Credence livre sa methodologie sous forme de Agent Skills (`SKILL.md`) que tout agent IA de codage peut charger. La compatibilite varie selon le client :

| CLI Agent | Mecanisme de Decouverte | Complexite d'Installation | Notes |
|---|---|---|---|
| **Claude Code** | Decouverte automatique de `dev/.claude/skills/` | Aucune | Support complet ; chargement automatique des competences |
| **Codex** | Lecture de `AGENTS.md` + chargement manuel de `SKILL.md` | Faible | Voir `docs/adapters/codex.md` pour l'installation detaillee |
| **Cursor** | Lecture de `AGENTS.md` + chargement manuel de `SKILL.md` | Faible | Invocation manuelle des competences |
| **Gemini** | Lecture de `AGENTS.md` + chargement manuel de `SKILL.md` | Moyenne | Peut necessiter du prompt engineering |
| **OpenCode** | Lecture de `AGENTS.md` + chargement manuel de `SKILL.md` | Faible | Compatible avec les workflows d'agents standard |

**Posture universelle** : lisez `AGENTS.md` d'abord, puis chargez le `SKILL.md` pertinent pour la tache a accomplir. Le fichier `AGENTS.md` a la racine du depot sert de point d'entree inter-CLI.

---

## Plan du Depot

```
credence-global/
|
|-- dev/                                # Source de la methodologie et des competences
|   |-- engine/                         # 27 documents methodologiques fondamentaux
|   |   |-- engine-overview.md          # Apercu de l'architecture et navigation
|   |   |-- industry-framework.md       # Classification sectorielle, scoring 10 dimensions, 6 paradigmes
|   |   |-- mosaic-engine.md            # Extraction de signaux, assemblage, completude
|   |   |-- dual-track-methodology.md   # Validation croisee Voie A+B, correspondance des notations
|   |   |-- multi-stakeholder.md        # 6 roles buy-side, matrice inter-roles
|   |   |-- quantitative-analysis.md    # Spreads, volatilite, modeles multi-facteurs
|   |   |-- qualitative-analysis.md     # Classement des sources, politique, assemblage mosaique
|   |   |-- financial-deep-dive.md      # Liaison 3 etats, fonds de roulement, FCF
|   |   |-- lgd-recovery-framework.md   # LGD 5 niveaux, evaluation des garanties, voie de recouvrement
|   |   |-- external-support-framework.md    # Soutien gouvernemental/groupe/strategique
|   |   |-- outlook-monitoring-framework.md # Perspectives 12-24m, liste de surveillance, matrice de migration
|   |   |-- governance-fraud-risk.md    # 20+ signaux de fraude, detection de defaut evade
|   |   |-- esg-framework.md            # ESG + detection gouvernance/fraude
|   |   |-- financial-bond-framework.md # Analyse des obligations financieres
|   |   |-- holding-company-framework.md # Analyse de credit des societes holding
|   |   |-- non-credit-risk-overlay.md  # Marche/operationnel/reputation/strategique/liquidite
|   |   |-- output-layered-framework.md # Carte de signaux L0, apercu L1, analyse approfondie L2
|   |   |-- contagion-theory.md         # 4 types de contagion, 7 voies de transmission
|   |   |-- contagion-matrix.md         # Matrice de contagion 19x19
|   |   |-- concentration-framework.md  # Analyse de concentration 5 dimensions
|   |   |-- systemic-warning-framework.md    # Agregation SRI, thermometre 4 niveaux
|   |   |-- validation-methodology.md   # Backtest cygne noir, validation a deux points
|   |   |-- paradigm-brand-channel.md   # Paradigme Defensif (P2)
|   |   |-- paradigm-network-traffic.md # Paradigme Reseau (P4)
|   |   |-- dimension-registry.md       # Index adressable des 6 paradigmes + roles M0-M5
|   |   |-- work-path-registry.md       # 16 chemins de travail, routage, integration pipeline
|   |   |-- pipeline-contract.md        # Contrats I/O du pipeline 4 etapes, aretes de chainage
|   |
|   |-- templates/                      # Source unique de verite des templates de rapport (16 fichiers HTML)
|   |   |-- template-base.css           # Base de style partagee
|   |   |-- template-type{1..15}.html   # Templates de rapport Type 1-15
|   |   |-- template-type18.html        # Template de surveillance des perspectives Type 18
|   |
|   |-- design/                         # Systeme de design des rapports
|   |-- data/                           # Architecture des donnees et specifications du pipeline
|   |-- product/                        # Vision produit, modele commercial, strategie GTM
|   |-- .claude/skills/                 # Chaine de competences en 4 etapes
|       |-- credit-analysis-router/     # Admission : routage 4 questions -> Fiche de Chemin
|       |-- fixed-income-credit-analysis/ # Analyse : execution par chemin
|       |-- credit-report-builder/      # Rapport : assemblage HTML a partir des templates
|       |-- credit-qa-verifier/         # AQ : porte qualite avant livraison
|
|-- src/                                # Orchestrateur executable et moteurs codes
|   |-- pipeline.py                     # Orchestrateur de la chaine en 4 etapes
|   |-- path_sheet.py                   # Validation des fiches de chemin et analyse du registre
|   |-- sri_calculator.py               # Moteur de calcul de l'Indice de Risque Systemique
|   |-- concentration_scorer.py         # Moteur de scoring de concentration 5 dimensions
|   |-- contagion_engine.py             # Moteur de matrice de contagion et d'escalade
|   |-- outlook_engine.py              # Moteur d'evaluation des perspectives et de surveillance
|
|-- tests/                              # Suite de tests de regression (pytest)
|-- scripts/                            # Outils de construction et de validation
|   |-- build_dist.py                   # Assembleur de package de release dev/ ->
|   |-- consistency_check.py            # Validation de coherence inter-documents
|   |-- promote.py                      # Utilitaire de promotion de version
|
|-- docs/                               # Adaptateurs inter-CLI et gestion de versions
|-- validation/                         # Preuves de capacite (2 rapports methodologiques publics de reference)
|-- version/                            # Archives zip de release construites localement (ignorees par git ; distribuees via GitHub Releases)
|-- AGENTS.md                           # Point d'entree universel inter-CLI
|-- DEVELOPMENT.md                      # Guide de developpement
|-- LICENSE                             # Licence source visible, non commerciale
|-- pyproject.toml                      # Configuration du projet Python
|-- package.json                        # Metadonnees du registre npm
```

---

## FAQ

### Q1 : Qu'est-ce qui rend Credence different de l'analyse de credit traditionnelle ?

Credence corrige trois echecs systematiques de l'analyse financiere traditionnelle : (1) les facteurs de credit les plus lourds (politique, PI, qualite des baux) ne figurent jamais au bilan, (2) les notations externes sont en retard de 17 mois ou plus sur la deterioration reelle, et (3) l'analyse a perspective unique manque les faiblesses structurelles. Credence utilise un cadre pyramidal hierarchise, une validation croisee double voie, un assemblage de donnees en mosaique et une perspective multi-parties prenantes pour reveler ce que l'analyse traditionnelle manque.

### Q2 : Ai-je besoin d'un abonnement payant ou d'une cle API ?

Non. Credence fonctionne sur des sources de donnees publiques gratuites — SEC EDGAR, FRED, portails des banques centrales, TRACE, rapports d'associations industrielles et recherche web. La phase POC est intentionnellement contrainte en sources de donnees pour prouver qu'une analyse de credit efficace est possible avec les seules donnees publiques.

### Q3 : A quelles agences de notation le moteur s'aligne-t-il ?

L'echelle de notation interne du moteur correspond a S&P (AAA a D), Moody's (Aaa a C) et Fitch (AAA a D). Voir le tableau de correspondance dans `dev/engine/dual-track-methodology.md` pour l'alignement complet.

### Q4 : Credence peut-il etre utilise avec n'importe quel CLI agent IA ?

Oui. Credence est independant du CLI. Il fonctionne avec Claude Code (decouverte automatique complete), Codex, Cursor, Gemini et OpenCode. Le fichier `AGENTS.md` a la racine du depot sert de point d'entree universel.

### Q5 : Comment les 16 chemins de travail sont-ils organises ?

Les chemins sont organises par role buy-side : Selectionneur de Credit (2), Gestionnaire de Portefeuille (2), Responsable des Risques (4), Trader (1), Conseiller (1), Investisseur Individuel (1) et Meta/Usage Special (5). Chaque chemin specifie une sequence de moteur, un template de rapport et des portes qualite. 8 chemins sont completement actifs, 6 sont partiellement implementes et 2 sont planifies.

### Q6 : Quels sont les 6 paradigmes internationaux ?

Cyclique (P1), Defensif (P2), Croissance (P3), Service Public Reglemente (P4), Financier (P5) et Lie au Souverain (P6). Chaque paradigme determine le modele de ponderation et les priorites de notation pour l'analyse sectorielle.

### Q7 : Que signifie "Couche d'Intelligence Systemique" ?

C'est la couche d'agregation la plus elevee qui va au-dela de l'analyse d'un emetteur unique pour detecter des schemas systemiques : contagion inter-sectorielle (matrice 19x19), concentration de portefeuille (5 dimensions) et Indice de Risque Systemique (SRI) avec un thermometre a quatre niveaux. Ensemble, ces modules repondent a "que se passe-t-il dans l'ensemble du portefeuille/marche" plutot qu'a "cet emetteur unique est-il risqué."

### Q8 : Quelle est la configuration des tests et de la CI ?

La suite de regression pytest couvre les moteurs codes, l'orchestrateur de pipeline, les registres de documents, le verificateur de coherence et le constructeur du package de release. La CI s'execute sur Python 3.11 et 3.12 via GitHub Actions. Execution locale avec `python -m pytest tests/ -q`. La coherence inter-documents est validee separement avec `python scripts/consistency_check.py`.

### Q9 : Quelles normes d'information financiere sont supportees ?

Les normes IFRS (International Financial Reporting Standards) et US GAAP (Generally Accepted Accounting Principles). Le moteur detecte automatiquement le referentiel a partir des depots de l'emetteur et ajuste les differences cles.

### Q10 : Comment commencer avec la chaine de quatre competences ?

Ouvrez la racine du package dans votre CLI, puis dites "analysez l'entreprise [X] dans le secteur [Y]." La competence `credit-analysis-router` gere le routage. Pour une utilisation directe des competences, chargez le `SKILL.md` pertinent selon les instructions du `AGENTS.md`.

### Q11 : Quelle est la difference entre les moteurs codes et les chemins orchestres par LLM ?

Quatre chemins de travail ont des implementations Python dediees (moteurs codes) : scoring de concentration, matrice de contagion, calcul du SRI et surveillance des perspectives. Ceux-ci sont invoques directement par l'orchestrateur (`src/pipeline.py`) lorsque l'ID du chemin correspond. Tous les autres chemins sont orchestres par le LLM en utilisant la documentation du moteur comme reference — aucun code Python ne duplique la methodologie.

### Q12 : Puis-je utiliser Credence a des fins commerciales ?

L'utilisation commerciale necessite une autorisation ecrite prealable du titulaire du droit d'auteur. Voir le fichier [LICENSE](LICENSE) pour les conditions completes. Le moteur est fourni en source visible pour evaluation non commerciale, recherche et evaluation interne.

---

## Licence et Avertissement

Ce depot est fourni sous **Licence Non Commerciale Source Visible Credence**. Vous pouvez consulter, apprendre et utiliser l'œuvre a des fins d'evaluation non commerciale / interne. **Toute utilisation commerciale necessite une autorisation ecrite prealable** du titulaire du droit d'auteur.

**Conditions cles** :
- L'utilisation non commerciale (recherche, enseignement, evaluation interne) est gratuite et autorisee
- L'utilisation commerciale (SaaS, conseil payant, systemes de production, redistribution) necessite une licence commerciale separee
- La sortie du moteur est une demonstration methodologique et un artefact de recherche — **ce n'est pas un conseil en investissement**
- Aucune garantie n'est fournie ; le logiciel est offert "en l'etat"

Voir le fichier [LICENSE](LICENSE) pour les conditions completes.

**Validation methodologique** : La methodologie du moteur a ete eprouvee sur cinq cas historiques documentes de defaut/detresse -- Lehman Brothers, Wirecard, Valeant, Credit Suisse et la restructuration souveraine grecque (voir `dev/engine/validation-methodology.md` §6). Deux rapports methodologiques publics de reference sont fournis dans le repertoire `validation/` ; l'archive complete des tests est maintenue en prive et disponible sur demande.

---

<p align="center">
  <strong>Credence</strong> · Moteur d'Analyse de Credit Obligataire · v0.0.2<br>
  Construit pour une analyse de credit rigoureuse, transparente et reproductible.
</p>
