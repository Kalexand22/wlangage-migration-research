# Plan détaillé de réalisation : C#, multi-BDD et agents IA

**Plan proposé le 26 octobre 2026, non exécuté.** La base d’implémentation demandée est **C#**. Les applications continuent à être maintenues en WLangage ; le C# généré reste un artefact interne. Le premier résultat à obtenir est une preuve autonome bornée, puis une application Windows de gestion. Les autres cibles et la longue traîne sont des programmes d’extension qualifiés séparément.

Le plan et ses fiches sont dans l’[index des blocs](../plan/README.md). Le [JSON de référence](../data/plan-realisation.json) décrit les tâches, dépendances, livrables, critères, budgets et gates. Le [CSV des tâches](../data/taches-agents.csv) permet leur import dans un outil de suivi. **Aucun ticket n’a été exécuté, aucune gate produit n’a été passée et aucun composant n’est admis par la rédaction de ce plan.**

## 1. Décisions de départ

| Sujet | Décision de réalisation | Limite explicite |
| --- | --- | --- |
| Implémentation | C# pour import, frontend, IR, runtime, données, CLI, services de langage et atelier | Aucun besoin de réécrire le code métier maintenu en C# |
| Toolchain | Famille .NET LTS supportée ; .NET 10 est le candidat initial à dater de cette étude | Version corrective, SDK, runtime, workloads et dépendances à épingler et admettre avant usage |
| Données | Abstractions multi-moteurs dès le départ ; premiers tests réels sur PostgreSQL **et** SQLite | Plusieurs bases PostgreSQL ne prouvent pas le multi-moteur |
| Moteurs suivants | SQL Server, puis MariaDB, MySQL et Oracle suivant besoin et admission | Un dossier, un pilote, des versions et un gate propre à chaque moteur |
| Interface initiale | Windows, renderer original sur un framework admis ; WinForms est le premier candidat | Le noyau C# multiplateforme ne rend pas l’interface Windows portable automatiquement |
| Indépendance | Aucun outil, DLL, SDK, pilote, serveur, service ou pont PC SOFT, dans aucune étape | Aucun oracle exécuté ni export demandé chez un tiers pour contourner la contrainte |
| Entrées | Sources, exports, schémas, données et références passives déjà disponibles avec droits et provenance | Une portion opaque indispensable reste un blocage ; aucune reconstruction fidèle supposée |
| Réemploi | Liakern est examiné comme inspiration et source potentielle à qualifier | Lecture, accès GitHub, inspiration, copie, modification et diffusion sont des actes distincts |
| Publication | Décision de licence de notre code toujours différée | Le partage temporaire du dossier ne donne pas de droits sur les composants de tiers |

La [politique officielle .NET](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core) consultée pour cette étude classe .NET 10 en LTS. Le choix de famille évite une préversion comme base du prototype ; il ne vaut ni admission juridique ni autorisation de réutiliser tout composant de l’écosystème.

L’[architecture C# et multi-BDD](18-architecture-csharp-multi-bdd-et-reemploi.md) définit les modules et les contrats. Les règles d’[orchestration et de preuve](17-orchestration-agents-et-gates.md) définissent l’exécution. Ces trois chapitres se lisent ensemble.

## 2. Ce que le découpage couvre réellement

Le backlog explicite contient un **socle borné**, sa preuve, un premier pilote et les mécanismes d’extension. Il ne prétend pas implémenter en quelques tâches toutes les fonctions WLangage, tous les champs ou toutes les variantes historiques. Le nombre de fonctions n’est toujours pas fermé dans le dossier.

Les **519 exigences** de la matrice sont rattachées une fois chacune à un bloc principal dans la [cartographie des exigences](../data/exigences-blocs.csv). Cette cartographie distingue :

- **269 socles partiels** : des tickets préparent ou réalisent une partie du contrat ; l’exigence entière n’est pas déclarée atomique ni couverte.
- **237 extensions à décomposer** : chaque famille doit produire des tickets par signature, comportement, propriété, cible et profil avant attribution.
- **13 technologies PC SOFT exclues, avec comportement à réimplémenter** : le besoin observable reste recensé, la technologie d’origine n’entre jamais dans la solution.

Chaque ligne reste un **parent non ordonnançable**, avec ses limites dans `notes`. « Rattaché » n’est ni « implémenté », ni « compatible », ni « décomposé jusqu’à chaque surcharge ». Le gate d’une extension exige sa propre décomposition et ses preuves avant toute déclaration de couverture.

L’[agenda des extensions](../data/extensions-a-decomposer.csv) instancie un identifiant `E-F-xxxx` pour chacun des 519 parents, avec priorité, bloc propriétaire et critère d’acceptation d’origine. Il inclut aussi le périmètre résiduel des socles partiels. Tous restent `a_decomposer`, non ordonnançables, avec contrats restants à inventorier ; ce fichier ne fabrique pas de tâches de quelques heures à partir de familles encore ouvertes. Un agenda/planning/Gantt, une intégration héritée ou une collaboration avancée conserve donc sa propre ligne, même si son détail attend les premières mesures.

Chaque ticket possède aussi un identifiant de contrat planifié `K-Bxx-nn`, ses liens `requirement_ids` et la nature du lien : préparation ou support partiel, **jamais clôture**. Ces liens concernent **199 parents distincts** ; **320 parents restent sans ticket de support explicite** dans ce premier backlog et restent visibles dans l’agenda. Quatorze tickets sont des prérequis techniques hors matrice fonctionnelle ; six attendent un choix fonctionnel précis avant rattachement et attribution. Aucun parent n’est ajouté arbitrairement pour faire monter le nombre de liens. Même les 199 parents liés conservent un périmètre résiduel à inventorier.

Ainsi, un ticket `HAjoute V0` porte sur une surcharge, un tampon et un profil choisis. Il ne clôt pas à lui seul l’exigence générale de manipulation des enregistrements. Un ticket « fermer le catalogue » produit un inventaire et ses inconnus ; il n’implémente pas cet inventaire.

Les exigences historiques de double exécution ou de coexistence restent bornées par la contrainte actuelle : comparaison à des références préexistantes ou entre nos moteurs indépendants ; aucun routage vers une application, un serveur ou un outil PC SOFT.

## 3. Taille acceptable d’une mission d’agent

La cible est **2 à 6 heures de travail effectif d’agent par ticket**, comme budget de travail révisable après les premières mesures. Elle ne prédit ni le temps calendaire, ni le coût d’une fonctionnalité complète. L’attente, la CI, la revue et la réparation doivent être mesurées séparément. Un agent rapide peut terminer avant ; un agent qui atteint le budget ne peut pas clôturer sans résultat.

Une mission doit avoir un résultat observable, un périmètre d’écriture limité et un critère qui pourrait échouer sur une mauvaise implémentation. Cinq fichiers ou 600 lignes modifiées sont des signaux de redécoupage, pas des objectifs ni des plafonds justifiant un contournement. Ne pas ajouter des tests qui recopient l’implémentation ; viser les invariants et risques réels.

**Redécouper avant attribution** lorsque le ticket contient plusieurs décisions ouvertes, dépend d’un outil encore non qualifié, modifie plusieurs contrats indépendants, ou demande une famille entière. Si la difficulté apparaît pendant l’exécution : conserver le diff et les observations, marquer le blocage, créer des enfants avec identifiants nouveaux, puis réviser les liens de dépendance. Les critères du parent ne disparaissent pas.

Exemple de décomposition d’une nouvelle recherche sur clé composée :

| Enfant | Résultat borné | Acceptation |
| --- | --- | --- |
| Spécification | Une signature, un profil, comparaison et ordre documentés | Attendus et inconnus identifiés ; pas de réponse inventée |
| Sémantique | Construction de la clé et état du tampon sur un seul cas | Absent, doublon et erreur différenciés |
| PostgreSQL | Traduction paramétrée du contrat déjà fixé | Ordre et valeurs vérifiés sur le moteur réel |
| SQLite | Adaptation du même contrat ou refus justifié | Écart de collation/capacité visible ; pas de faux support |
| Intégration | Cas WLangage inchangé et résultat observable | Source conservée, erreur localisée, preuves sur la révision finale |

Ces enfants sont à instancier avec identifiants, versions et références réelles. Leurs tests nécessaires font partie de leurs livraisons ; une tâche supplémentaire de tests n’est ajoutée que lorsqu’elle vérifie une intégration ou un risque distinct.

## 4. Ordre des blocs et gates de sortie

Les fiches indiquent tous les tickets et leurs critères. Les dépendances exactes sont dans le JSON et dans le diagramme de l’index ; ce tableau donne les résultats attendus.

| Bloc | Résultat à obtenir | Gate de fin |
| --- | --- | --- |
| [B00](../plan/blocs/B00.md) — admissions | Petite chaîne d’outils et entrées initiales qualifiées, actes distingués | `G-B00` : tout acte initial autorisé et documenté ; doute non résolu bloquant ; aucun PC SOFT |
| [B01](../plan/blocs/B01.md) — socle | Solution C#, dépendances verrouillées, contrat agent, états, DAG, baux et CI | `G-B01` : build propre et mini-cycle auteur/relecteur/intégration reproductible |
| [B02](../plan/blocs/B02.md) — import | Corpus synthétique, inventaire, profil et extraction sans perte | `G-B02` : tous éléments ont un état, octets conservés, inconnus requis bloquants |
| [B03](../plan/blocs/B03.md) — syntaxe | Lexer/CST/parseur sur grammaire V0 déclarée | `G-B03` : sous-ensemble analysé, erreurs récupérées, texte et positions conservés |
| [B04](../plan/blocs/B04.md) — types | Valeurs, conversions et options sémantiques explicites | `G-B04` : cas limites vérifiés, aucun défaut implicite C# ou de profil inconnu |
| [B05](../plan/blocs/B05.md) — runtime | Cellules, procédures, alias, erreurs et interprète original | `G-B05` : effets et passage des paramètres éprouvés sur règles identifiées |
| [B06](../plan/blocs/B06.md) — compilation | Génération C#, CLI, source maps et démonstration console | `G-B06` : mêmes sources V0 inchangées exécutées sur machine propre, limites publiées |
| [B07](../plan/blocs/B07.md) — contrats données | Modèle logique, sessions, capacités, types et transactions | `G-B07` : aucune dépendance fournisseur dans les contrats, différence des moteurs représentable |
| [B08](../plan/blocs/B08.md) — deux moteurs | Providers PostgreSQL et SQLite réels, valeurs exactes et transactions | `G-B08` : mêmes contrats exécutés sur les deux, écarts visibles, aucun faux moteur de substitution |
| [B09](../plan/blocs/B09.md) — H* | Sous-ensemble original tampon/recherche/parcours/écriture/transaction | `G-B09` : mini-parcours WLangage sur les deux moteurs, erreurs et ordre vérifiés |
| [B10](../plan/blocs/B10.md) — migration | Entrées logiques, mapping, chargement, reprise et réconciliation | `G-B10` : clés, comptes, montants, null et blobs préservés ; restauration répétée |
| [B11](../plan/blocs/B11.md) — UI runtime | Fenêtre, saisie, bouton, grille, événements et modalité bornés | `G-B11` : parcours clavier/validation/DPI/accessibilité et ordre tracés |
| [B12](../plan/blocs/B12.md) — atelier | Explorateur, édition WLangage, diagnostics et GO | `G-B12` : trois parcours développeur utilisables avec sources conservées |
| [B13](../plan/blocs/B13.md) — designer | Modèle ouvert, canvas, propriétés, événements, undo et aperçu | `G-B13` : édition/reprise sans perte, diff lisible, propriétés opaques bloquantes |
| [B14](../plan/blocs/B14.md) — langage/debug | LSP, source maps, arrêt/pas-à-pas/pile/variables V0 | `G-B14` : débogage des sources WLangage sur le chemin compilé prouvé ou blocage déclaré |
| [B15](../plan/blocs/B15.md) — documents | État métier simple, pagination, aperçu et PDF | `G-B15` : valeurs exactes et comparaison structurée puis visuelle, ressources admises |
| [B16](../plan/blocs/B16.md) — APIs/intégrations | Registre et petites signatures fichiers/chaînes/dates/JSON/HTTP | `G-B16` : contrat par signature, erreurs/annulation, aucune réussite d’un stub vide |
| [B17](../plan/blocs/B17.md) — transversal | Secrets, droits, isolation, logs, audit et support | `G-B17` : contrôles négatifs d’accès et d’isolation, secrets absents des preuves |
| [B18](../plan/blocs/B18.md) — moteurs suivants | Troisième moteur réel et dossiers optionnels distincts | `G-B18` : mêmes contrats sur la version admise, aucun support déduit d’une simple connexion |
| [B19](../plan/blocs/B19.md) — pilote Windows | Parcours métier, sources conservées, paquet et repli autonome | `G-B19` : recette bornée, machine propre, indépendance et décision de faisabilité |
| [B20](../plan/blocs/B20.md) — web | Première page, séparation client/serveur, sessions et données | `G-B20` : parcours E2E sécurisé sur un profil web distinct |
| [B21](../plan/blocs/B21.md) — mobile | Android, hors ligne et sync ; iOS ensuite avec admission propre | `G-B21` : preuves appareil/cycle système/conflits propres à chaque plateforme annoncée |
| [B22](../plan/blocs/B22.md) — longue traîne | Catalogue, champs, FAA, langage et formats supplémentaires | `G-B22` : extensions décomposées et profils de compatibilité datés ; aucun taux artificiel |
| [B23](../plan/blocs/B23.md) — maintenance | Support, collaboration, plugins, mises à jour et nouvelles cibles | `G-B23` : régression historique reproduite/corrigée et évolution requalifiée |

### Jalons décisionnels utiles

1. **M0 — exécution maîtrisée :** B00 puis B01. On sait autoriser un acte, attribuer une mission et refuser une fausse preuve. Ce n’est pas une preuve de compatibilité du langage.
2. **M1 — faisabilité du code :** B02 à B06. On compile un vrai sous-ensemble WLangage original inchangé. Un échec sémantique entraîne correction ou réduction explicite avant financement de l’atelier complet.
3. **M2 — faisabilité multi-BDD :** B07 à B09, puis réconciliation B10. On éprouve le même code et les mêmes contrats sur PostgreSQL et SQLite. On mesure les capacités impossibles à émuler plutôt que les cacher.
4. **M3 — expérience développeur :** B11 à B14. Ouvrir, éditer, concevoir, GO et déboguer deviennent des parcours vérifiables. Le runtime seul ne prouve pas l’ergonomie RAD.
5. **M4 — pilote Windows :** B15 à B17 et B19, avec les blocs précédents. Le périmètre métier est fixé avant recette ; aucune fonction manquante n’est découverte puis retirée du dénominateur pour passer.
6. **M5 — élargissement :** B18, B20 à B23 suivant les besoins. SQL Server, web, Android, iOS, catalogue avancé et autres OS ont chacun leurs propres critères ; leur présence dans le programme ne promet pas leur disponibilité.

B18 n’est pas un prérequis systématique au pilote Windows : le gate multi-moteur de départ repose déjà sur PostgreSQL et SQLite. Un pilote qui exige SQL Server doit ajouter explicitement `G-B18` à ses préconditions. Les cibles web et mobile ne sont pas nécessaires à la première preuve de faisabilité.

## 5. Contenu obligatoire d’une gate

Le passage d’un bloc ne se résume pas à « tous les tickets sont fermés ». Pour chaque gate :

1. Identifier la révision intégrée finale, l’arbre, les versions des outils, le profil et les données de test.
2. Rejouer les contrôles pertinents sur cette révision, avec commandes, codes de sortie, cas découverts et résultats. Un test absent, ignoré, interrompu ou bloqué reste non acquis.
3. Vérifier les critères spécifiques du bloc et les cas négatifs nécessaires : mauvais profil, capacité inconnue, entrée hostile, erreur, annulation, etc.
4. Contrôler les admissions pour **les actes effectivement nécessaires à ce stade**, les obligations et les dépendances transitives. B00 ne donne pas d’autorisation générale aux futures extensions.
5. Vérifier l’exclusion PC SOFT dans les outils, processus, modules, services distants et paquets du périmètre testé.
6. Faire relire diff, preuves et limites par un autre agent. Une correction ultérieure invalide les preuves et avis affectés.
7. Enregistrer `pass_verified`, `fail`, `blocked`, `stale` ou `non_execute`, la raison et la suite. Seul `pass_verified` valable ouvre les dépendants.

Le [modèle de preuve](../examples/preuve-gate.exemple.json) est vierge et non exécuté. Ses valeurs nulles ne sont pas des observations. Le statut n’est pas déduit d’un résumé d’agent ou d’un délai écoulé.

Le refus des droits non établis, l’exclusion PC SOFT et l’absence de perte de données ou de sources sont des contraintes fermes. Une réduction de périmètre se décide et se documente ; elle ne transforme pas un échec antérieur en réussite. Les autres blocs indépendants continuent si leurs propres préconditions sont satisfaites.

## 6. Multi-BDD : critères qui doivent rester séparés

Le contrat fournisseur repose sur ADO.NET, avec types, requêtes paramétrées, erreurs, sessions et transactions explicites. Le [socle ADO.NET](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/ado-net-overview) fournit les mécanismes d’accès ; il n’uniformise pas la syntaxe SQL, l’isolation, les collations ou les contrats H*.

| Dimension | Vérification exigée |
| --- | --- |
| Moteur et version | Instance réelle, options/collation/édition capturées ; admission du moteur, du driver et des composants natifs |
| Types | Entiers, précision/échelle, null/vide, dates, encodages et blobs sans pertes silencieuses |
| SQL | Paramètres pour les valeurs, validation/citation des identifiants, dialecte isolé ; SQL arbitraire fournisseur non réputé portable |
| H* | Tampon courant, ordre, recherche, filtre, états de fin/erreur et mutation visibles selon contrat |
| Transactions | Atomicité de plusieurs tables sur une connexion ; aucun commit par module si le contrat source porte plus loin |
| Concurrence | Verrouillage, timeouts, conflits, annulation, commit d’issue incertaine et politique de rejeu ; capacité non équivalente refusée |
| Reprise | Sauvegarde restaurée, migration additive et retour à une release autonome précédente ; pas de repli PC SOFT |
| Multi-tenant | Contexte, cache, erreurs, tampon, droits et connexion isolés ; gate distinct de la portabilité entre moteurs |

Sur SQLite, le monétaire exact doit avoir une représentation explicitement choisie et éprouvée ; aucun flottant implicite. Une absence de verrou de ligne équivalent ne devient pas « conforme » parce qu’un CRUD simple réussit. Pour MariaDB et MySQL, des dossiers séparés évitent de supposer leur identité à partir d’un protocole commun. La compatibilité d’un fournisseur EF Core avec une version du framework est elle aussi à vérifier si EF est retenu pour un module auxiliaire ; [Microsoft demande d’évaluer qualité, licence, support et compatibilité de chaque provider](https://learn.microsoft.com/en-us/ef/core/providers/). L’ORM ne remplace pas la couche de sémantique de compatibilité.

## 7. Liakern et modèles d’orchestration : comment en tirer parti

La consultation des dépôts indiqués par le propriétaire sert à identifier des approches et des éléments candidats. **Aucune récupération de code, exécution d’un outil de ces dépôts ni admission d’un composant n’est effectuée dans ce livrable.** Les observations détaillées de dépôts privés restent dans des notes séparées du dépôt partagé ; aucune source ni extrait interne n’est transféré ici.

La procédure de réemploi suit quatre étapes :

1. Identifier un besoin de notre plateforme et une frontière précise : contrats d’infrastructure, isolation de contexte, configuration, tests d’architecture ou principe d’orchestration.
2. Comparer le contrat attendu au candidat, avec ses dépendances et hypothèses. Un élément multi-tenant n’est pas automatiquement un adaptateur multi-moteurs ; une transaction par module ne doit pas casser une transaction source plus large.
3. Établir les droits sur l’élément exact, les contributions, les dépendances et les actes prévus. Le statut privé, le droit d’accès ou la titularité supposée ne valent pas une autorisation automatique de copie ou de diffusion.
4. Choisir une réalisation originale, un composant indépendant admis, une récupération admise et isolée, ou un refus. Faire une petite preuve d’adaptation avant toute généralisation.

Pour l’orchestration, les propriétés utiles à retenir sont : plan séparé de l’état des tentatives, dépendances explicites, état absent non assimilé à terminé, baux/heartbeats, preuve de la révision finale, revue indépendante, gate intégrée et reprise sans double effet. Le chapitre 17 les spécifie de manière originale, sans recopier de workflow privé ni présumer que les modèles consultés sont des produits à reprendre tels quels.

## 8. Organisation des agents et pilotage de l’effort

Commencer avec **trois fonctions**, cumulables selon la capacité réelle : intégrateur/planificateur, agent d’implémentation, agent de revue. Quand plusieurs tickets indépendants existent, ouvrir des pistes langage, données et transversal ; l’atelier démarre après stabilisation des contrats qu’il consomme. Plus d’agents ne raccourcit pas une chaîne de dépendances et peut augmenter les conflits.

Le DAG est volontairement conservateur au sein d’un bloc. Les tâches y sont ordonnées pour éviter que deux agents modifient simultanément la même grammaire ou le même contrat. Certaines tâches d’intégration exigent en plus des gates ciblées dans `requires_block_gates` : binding UI après données, RAD CRUD après données et renderer, isolation de connexion après runtime données. Le validateur inclut ces liens dans la recherche de cycles ; ils ne figurent pas tous dans le diagramme simplifié des prérequis de blocs. On peut ensuite paralléliser des enfants sur périmètres réellement séparés, après révision des dépendances. Le coordinateur ne doit pas ignorer ces liens pour occuper tous les agents.

Mesurer dès les dix premières tâches : durée active, délai d’attente, coût agent, CI, temps de revue, nombre de retours, défauts d’intégration et taux de redécoupage. Réestimer après M1 puis M2. La somme des budgets de tickets n’est ni le calendrier du produit ni le devis d’une compatibilité complète. Les anciennes hypothèses budgétaires du chapitre 07 restent un scénario historique de plateforme étendue, pas une conversion de ce backlog en mois garantis.

Une nouvelle API ou un nouveau champ doit être chiffré avec sa spécification, son implémentation, ses tests pertinents, la revue, les défauts et la maintenance du profil. Ne pas extrapoler le débit d’une fonction pure à un driver, un débogueur ou un moteur d’états.

## 9. Livrables et contrôles du plan

| Fichier | Rôle |
| --- | --- |
| [Plan JSON](../data/plan-realisation.json) | Source éditable des blocs, tâches et gates |
| [Exigences vers blocs](../data/exigences-blocs.csv) | Source éditable des 519 parents et de leurs limites |
| [Agenda des extensions](../data/extensions-a-decomposer.csv) | Export des 519 parents nommés et priorisés, tous à décomposer avant exécution |
| [Index et fiches](../plan/README.md) | Lecture humaine des missions, prérequis et critères |
| [Backlog CSV](../data/taches-agents.csv) | Export généré pour suivi/import, sans exécution |
| [Preuve de gate](../examples/preuve-gate.exemple.json) | Modèle de preuve à remplir lors d’une vraie réalisation |
| [Générateur](../tools/build_execution_plan.py) | Régénère les fiches et le CSV depuis les sources |
| [Contrôle du plan](../tools/check_execution_plan.py) | Vérifie références, DAG tâches/gates, budgets déclarés, rattachements et fraîcheur |

Commandes documentaires :

```bash
python3 tools/build_execution_plan.py
python3 tools/build_bibliography.py
python3 tools/assemble_report.py
python3 tools/update_metrics.py
python3 tools/check_execution_plan.py
python3 tools/check_repository.py
```

Le contrôle détecte notamment un cycle passant par une gate, un prérequis inconnu, une tâche omise par sa gate, une exigence perdue et un fichier généré périmé. **Il ne mesure pas la taille réelle d’une implémentation, ne vérifie pas l’interprétation d’une licence et ne passe aucune gate produit.** L’ordonnanceur et les contrôles runtime seront réalisés et éprouvés dans B01 ; les scripts du dossier ne lancent pas d’agents, de compilateur ou de base de données.

La prochaine action de réalisation concrète est B00 sur la petite chaîne nécessaire à B01, puis la première tranche syntaxe/types/compilation. Les choix d’extension sont arrêtés sur les mesures de ces preuves, sans attendre que tout le catalogue soit implémenté.
