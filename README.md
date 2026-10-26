# Plateforme compatible WLangage : recherche et conception

**Étude en français — 26 octobre 2026.** Objectif : reprendre les sources PC SOFT/WINDEV, conserver le WLangage comme langage de travail, générer des applications au comportement comparable et offrir un atelier familier aux développeurs.

**Recommandation :** développer un compilateur indépendant, un runtime de compatibilité, un importeur versionné et un atelier RAD. Commencer par Windows et un profil précisément qualifié ; conserver HFSQL lorsque l'interface et les droits conviennent, puis élargir les cibles et les moteurs de données séparément.

Ce dépôt contient la **recherche et le cahier de conception**, sans compilateur ou migration déjà réalisés. Les choix techniques sont des propositions à éprouver. Aucun projet client, environnement WINDEV ou oracle d'exécution n'a été fourni.

**Contenu : 12 chapitres, 517 exigences fonctionnelles dans 17 domaines, 15 améliorations proposées et 6 prototypes de décision à réaliser.**

## Lire le dossier

- [Rapport complet dans un seul fichier](RAPPORT_COMPLET.md).
- [Matrice des exigences fonctionnelles](data/fonctionnalites.csv) : identifiants, domaines, priorités, stratégies, critères d'acceptation et références.
- [Index des URL citées](data/bibliographie.json), avec les chapitres concernés. Il indexe les références ; il ne prétend pas certifier l'accessibilité ou l'actualité de chaque page.

| Chapitre | Contenu |
| --- | --- |
| [00 — Synthèse et décisions](docs/00-synthese-et-decisions.md) | Faisabilité, recommandations, promesses distinctes et inconnues |
| [01 — Options et solutions existantes](docs/01-options-et-solutions-existantes.md) | Compatibilité indépendante, transpilation, réécriture et outils publics |
| [02 — Langage et import](docs/02-langage-et-import.md) | Formats, options de compilation, sémantique, frontend et conservation des sources |
| [03 — Expérience de développement](docs/03-experience-developpement-et-interface.md) | Atelier, raccourcis, concepteurs, champs, événements, FAA et parcours de transition |
| [04 — Données, intégrations et cibles](docs/04-donnees-integrations-et-cibles.md) | HFSQL, adaptateurs H*, SQL, impressions, interop et plateformes |
| [05 — Architecture cible](docs/05-architecture-cible.md) | IR, .NET/runtime, renderers, LSP/DAP, extensions et dix décisions d'architecture |
| [06 — Inventaire et couverture](docs/06-inventaire-fonctionnel-et-couverture.md) | Référentiel fonctionnel et méthode pour fermer l'exhaustivité API/version/cible |
| [07 — Plan de réalisation et risques](docs/07-plan-realisation-et-risques.md) | Jalons, scénarios d'effort et coût, corpus, qualification et registre de risques |
| [08 — Améliorations produit](docs/08-ameliorations-produit.md) | Quinze améliorations avec bénéfices, dépendances, preuves et limites |
| [09 — Propriété intellectuelle et licences](docs/09-propriete-intellectuelle-et-licences.md) | Droit UE/France, implémentation indépendante, contrats et redistribution |
| [10 — Pilote et recette](docs/10-protocole-pilote-et-recette.md) | Paquet d'entrée, oracle, tests différentiels, mesures, bascule et retour arrière |
| [11 — Prototypes de décision](docs/11-cahier-des-charges-des-spikes.md) | Six essais concrets, livrables, charges indicatives et critères go/no-go |

## Ce que signifie « même code source »

Les procédures et traitements restent maintenus et débogués en WLangage. Le C# généré proposé par l'architecture serait un artefact interne reconstruisible. L'import des fenêtres, états, requêtes et de l'analyse est un chantier distinct de la reconnaissance de la syntaxe.

La fidélité doit aussi préserver les options du projet, les types, les effets de bord, les événements, les automatismes des champs, les parcours HFSQL et les documents imprimés. Le réexport vers les formats natifs PC SOFT constitue un objectif séparé, sans garantie générale dans cette étude.

## Exigence d'exhaustivité

L'inventaire couvre largement les capacités de l'AGL et de son écosystème, y compris les fonctions historiques et les outils d'exploitation. **Il ne constitue pas un catalogue certifié de chaque API, surcharge, propriété, constante, erreur et variante historique.** Les références thématiques du CSV ne prouvent pas à elles seules une disponibilité exacte sur toutes les cibles.

Le chapitre 06 décrit comment atteindre une exhaustivité démontrable sur un périmètre fermé : versions/builds/options/cibles, catalogue daté, matrice des signatures et preuves d'exécution. Les inconnus restent visibles et les fonctions rares restent dans le dénominateur. Tous les statuts d'implémentation de cette étude sont **non implémenté**.

Le référentiel examine des sources historiques et l'édition 2026 vérifiée. La date de recherche n'est pas une certification que toutes les publications, mises à jour ou éditions disponibles ce jour ont été recensées. La collecte complète du catalogue et sa réconciliation avec les installations choisies font partie du premier jalon.

## Modèles à réutiliser

- [Profil de migration](examples/profil-migration.exemple.json) : version/build/options, dépendances et blocages.
- [Cas de comparaison différentielle](examples/cas-differentiel.exemple.json) : préconditions, actions, observations et preuve.
- [Structure d'un registre API](examples/registre-api.exemple.csv) : signature, cible et statut de qualification.

Ces modèles sont synthétiques et à compléter ; ils ne réalisent aucune migration. Les paramètres inconnus restent `null` et bloqueraient la génération dans le produit proposé.

## Vérifier et régénérer la documentation

Python **3.9 ou ultérieur**, sans dépendance supplémentaire :

```bash
python3 tools/build_bibliography.py
python3 tools/assemble_report.py
python3 tools/check_repository.py
```

Le contrôle vérifie les liens locaux, la structure CSV, les identifiants, les statuts et le JSON. Il ne vérifie pas le comportement de WINDEV et n'attribue aucun taux de compatibilité au futur produit.

Pour contribuer, suivre [CONTRIBUTING.md](CONTRIBUTING.md). Les notes de revue datées sont dans `data/revue-*.md` ; elles conservent aussi les constats ensuite corrigés. Les droits et la nature du dossier sont précisés dans [NOTICE.md](NOTICE.md).
