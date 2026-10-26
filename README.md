# Faisabilité d’une plateforme indépendante compatible WLangage

**Recherche en français — 26 octobre 2026.** L’objectif est de conserver les sources WLangage comme code maintenu et de migrer la chaîne de développement et d’exécution vers une implémentation indépendante, avec une expérience RAD familière. La réécriture vers un autre langage est une trajectoire distincte, comparée dans le dossier.

**Contrainte ferme : aucune DLL, aucun outil, SDK, pilote, serveur ou runtime PC SOFT dans la chaîne de développement, import, compilation, exécution ou test.** Aucun oracle WINDEV ni export PC SOFT n’est exécuté, y compris par un tiers pour notre protocole. [Périmètre indépendant](docs/15-perimetre-independant-et-preuve-de-faisabilite.md).

**Règle d’admission des outils : droits d’usage et obligations réglementaires établis pour la version et l’acte envisagés avant utilisation. Un droit manquant, ambigu ou incompatible bloque cet acte ou impose un remplacement.** Les outils indépendants cités sont des candidats, pas des admissions automatiques. [Politique et registre](docs/15-perimetre-independant-et-preuve-de-faisabilite.md).

**Phase actuelle : évaluation de faisabilité.** Aucun compilateur compatible, importeur qualifié ou oracle d’exécution n’a été réalisé dans cette étude. Le choix d’une licence de publication et les décisions de commercialisation sont différés, conformément à la demande du propriétaire.

## La décision technique à préparer

Trois preuves viennent en premier : reprendre un projet sans perte silencieuse, conserver sa sémantique effective, puis exécuter une tranche métier avec données et impression. Le WLangage doit rester la source de travail et de débogage ; un éventuel C# généré serait un artefact interne.

La base d’implémentation choisie est **C#**, avec IR sémantique et runtime original. Le premier scénario est Windows ; .NET LTS et WinForms sont à sélectionner et admettre pour leurs versions et usages. La couche données est **multi-moteurs dès la conception : PostgreSQL et SQLite d’abord, SQL Server ensuite**, puis extensions qualifiées séparément. Les appels H* ont une implémentation originale ; serveur et pilotes HFSQL sont exclus. Sources, schémas et références doivent être déjà exploitables indépendamment ; un format opaque non qualifié reste bloquant. [Architecture C# et multi-BDD](docs/18-architecture-csharp-multi-bdd-et-reemploi.md).

## Plan détaillé de réalisation

**[24 blocs, 255 tâches d’agents et 24 gates](plan/README.md)** : livrables, dépendances, critères de passage, budgets cibles de 2–6 h et revue indépendante. [Guide de réalisation](docs/16-plan-detaille-de-realisation.md), [backlog CSV](data/taches-agents.csv) et [plan JSON](data/plan-realisation.json).

Les **519 exigences** sont [rattachées aux blocs](data/exigences-blocs.csv) comme parents avec limites explicites. Les familles supplémentaires doivent être décomposées avant attribution ; aucun catalogue WLangage complet n’est prétendu réalisé par ces tickets. Le [protocole d’orchestration](docs/17-orchestration-agents-et-gates.md) exige des preuves sur la révision finale et ferme les gates en cas d’échec, de blocage ou de contrôle non exécuté. Liakern et les modèles d’orchestration sont étudiés comme inspirations ; aucun code tiers n’est récupéré ou admis automatiquement.

## Points à qualifier

- **Sources et formats :** le parcours officiel de partage Git impose des prérequis ; des propriétés avancées restent binaires. Millésime, update, build et options effectives sont distincts. Un élément opaque reste conservé, signalé et peut bloquer la génération concernée.
- **Sémantique et couverture :** les réglages de projet, dont le mode de passage des paramètres 2026, peuvent modifier le comportement. Le catalogue API n’est pas fermé et aucune compatibilité exécutée n’est mesurée.
- **Méthode de réalisation :** les licences WINDEV et Framework limitent leur utilisation pour construire certains outils de développement. Cela ne démontre pas l’interdiction d’un compilateur original n’utilisant pas ces produits. Observation autorisée, réemploi de composants et redistribution sont à distinguer ; les exceptions légales ont leurs conditions. L’étude et le code autonome ne sont pas soumis ici à un avis d’avocat préalable général. [Analyse juridique et sources](docs/09-propriete-intellectuelle-et-licences.md).

Le contexte commercial de 2026 peut motiver une migration, mais ne décide pas de sa faisabilité. Qui finance, quels composants doivent être quittés et à quel coût restent des questions à instruire avant industrialisation, avec les contrats applicables. [Contexte et scénarios de décision](docs/14-contexte-commercial-et-decision.md).

## Lire le dossier

**19 chapitres, 519 exigences dans 17 domaines, 15 améliorations proposées, 11 décisions d’architecture et 6 prototypes à réaliser.**

- [Rapport complet](RAPPORT_COMPLET.md) et [réponse point par point à la relecture](docs/13-reponse-a-la-relecture-critique.md).
- [Matrice fonctionnelle](data/fonctionnalites.csv) : priorités, stratégies, critères, sources et limites.
- [Premier lot](docs/12-ameliorations-immediates.md) : dix tâches de préparation, dépendances et seuils à arrêter avant essai.
- [Bibliographie](data/bibliographie.json) et [métriques documentaires](data/metriques-dossier.json).

| Chapitre | Objet |
| --- | --- |
| [00 — Synthèse et décisions](docs/00-synthese-et-decisions.md) | Objectif, deux trajectoires et hypothèses de faisabilité |
| [01 — Options et solutions existantes](docs/01-options-et-solutions-existantes.md) | Compatibilité, transpilation, réécriture et offres publiques |
| [02 — Langage et import](docs/02-langage-et-import.md) | Formats, builds, options et sémantique |
| [03 — Expérience de développement](docs/03-experience-developpement-et-interface.md) | Atelier, champs, événements, FAA et transition |
| [04 — Données, intégrations et cibles](docs/04-donnees-integrations-et-cibles.md) | HFSQL, H*, SQL, états, interop et plateformes |
| [05 — Architecture cible](docs/05-architecture-cible.md) | IR, runtime, renderers, débogage et onze ADR |
| [06 — Inventaire et couverture](docs/06-inventaire-fonctionnel-et-couverture.md) | Exigences, catalogue API et méthode de fermeture |
| [07 — Réalisation et risques](docs/07-plan-realisation-et-risques.md) | Jalons, scénarios d’effort, corpus et qualification |
| [08 — Améliorations produit](docs/08-ameliorations-produit.md) | Quinze propositions et leurs critères |
| [09 — Droit et licences](docs/09-propriete-intellectuelle-et-licences.md) | Développement original, observation, composants et diffusion |
| [10 — Pilote et recette](docs/10-protocole-pilote-et-recette.md) | Références passives, comparaisons, mesures et retour arrière |
| [11 — Prototypes de décision](docs/11-cahier-des-charges-des-spikes.md) | Six essais avec critères de poursuite ou d’arrêt |
| [12 — Améliorations immédiates](docs/12-ameliorations-immediates.md) | Premier lot et traçabilité |
| [13 — Réconciliation de la critique](docs/13-reponse-a-la-relecture-critique.md) | Points confirmés, corrections et conclusions à nuancer |
| [14 — Contexte 2026](docs/14-contexte-commercial-et-decision.md) | Sources commerciales, scénarios et coûts à renseigner |
| [15 — Périmètre indépendant](docs/15-perimetre-independant-et-preuve-de-faisabilite.md) | Contrainte sans PC SOFT, entrées admises et limites de preuve |
| [16 — Réalisation détaillée](docs/16-plan-detaille-de-realisation.md) | 24 blocs, missions d’agents, dépendances et critères de passage |
| [17 — Orchestration et gates](docs/17-orchestration-agents-et-gates.md) | Tentatives, baux, worktrees, preuves finales et revue indépendante |
| [18 — C# et multi-BDD](docs/18-architecture-csharp-multi-bdd-et-reemploi.md) | Modules, SPI fournisseurs, capacités et réemploi à qualifier |

## Exhaustivité : ce qui est mesuré

La matrice **structure 519 exigences**. Leur rattachement à un catalogue API versionné n’est pas établi : `nb_fonctions_couvertes=INCONNU` et `statut_rattachement_api=non établi`. Ce nombre n’est pas comparable au nombre de fonctions annoncé par PC SOFT. **Le taux de couverture API est non calculable.**

Le chapitre 06 définit les dénominateurs requis : fonctions et surcharges, types, propriétés, événements, constantes, erreurs, cibles, builds et options. Les inconnus restent visibles ; aucun statut n’est augmenté sur la seule base d’une référence documentaire. Toutes les exigences restent **non implémentées**.

## Modèles et contrôles

Les [profils](examples/profil-migration.exemple.json), [cas différentiels](examples/cas-differentiel.exemple.json) et [registre API](examples/registre-api.exemple.csv) sont des modèles synthétiques à compléter. Ils ne constituent ni une migration ni un résultat WINDEV.

Python 3.9 ou ultérieur, sans dépendance supplémentaire pour les scripts du dossier :

```bash
python3 tools/build_execution_plan.py
python3 tools/build_bibliography.py
python3 tools/assemble_report.py
python3 tools/update_metrics.py
python3 tools/check_execution_plan.py
python3 tools/check_repository.py
python3 -m unittest discover -s tests -v
```

Le workflow documentaire répète ces commandes et vérifie l’absence de différence des fichiers générés. Les tests du validateur vérifient notamment le refus des cycles tâches/gates et des faux statuts d’exécution ; ils ne passent aucune gate produit. Le contrôle externe des liens est distinct, hebdomadaire et informatif : un HTTP 403 ne prouve pas qu’une source a disparu. Aucun de ces contrôles ne certifie le WLangage.

Voir [CONTRIBUTING.md](CONTRIBUTING.md), [CHANGELOG.md](CHANGELOG.md) et [NOTICE.md](NOTICE.md). Aucune licence ouverte de publication n’est choisie à ce stade de faisabilité. Les textes et logiciels de tiers conservent leurs propres droits.
