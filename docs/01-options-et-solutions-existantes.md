# Options et solutions existantes

Recherche arrêtée au 26 octobre 2026. Cette comparaison sépare les déclarations des auteurs et les conclusions de conception. Aucun des produits ou dépôts mentionnés n'a subi ici une campagne d'essais sur une application client. L'absence de preuve publique de compatibilité n'est pas une preuve d'impossibilité.

**Périmètre retenu après instruction du propriétaire : aucun logiciel, DLL, pilote, serveur ou oracle PC SOFT exécuté dans notre chaîne, même par un tiers. Les solutions utilisant ces éléments sont comparées historiquement, mais exclues de la cible ; les promesses des fournisseurs ne prouvent pas leur conformité à cette contrainte.** [Règle de périmètre](15-perimetre-independant-et-preuve-de-faisabilite.md).

## 1. Choisir la bonne catégorie de solution

| Approche | Le développeur maintient le même WLangage | Reprise de l'IHM | Indépendance envers l'environnement PC SOFT | Usage approprié |
| --- | --- | --- | --- | --- |
| Continuer dans PC SOFT, extraire progressivement des services | Oui pour l'existant | Conservée dans le produit d'origine | Partielle | Réduire immédiatement le risque et isoler les dépendances |
| Nouveau compilateur et runtime compatibles | Objectif central | Importeur et renderer à construire | Forte si implémentation indépendante et dépendances maîtrisées | Construire le produit demandé |
| Transpileur de migration vers C# ou autre langage | Généralement non après bascule de maintenance | Variable et souvent chantier séparé | Possible | Sortie du langage d'origine acceptée |
| Réécriture assistée par IA | Non, sauf usage d'un compilateur compatible en aval | Recréée à partir des preuves | Possible | Refondre aussi l'architecture et les usages |
| Nouvel AGL avec un autre langage | Non sans couche additionnelle | Recréée ou import partiel démontré | Dépend du nouvel éditeur | Priorité à un RAD existant plutôt qu'au même code |
| Exécuter l'ancien runtime derrière un nouveau shell | Oui mais toujours exécuté par PC SOFT | Peut rester ancienne | Faible | Pont transitoire déclaré, selon licences et interfaces |
| Émuler l'exécutable compilé | Ne réutilise pas les sources au sens demandé | Ancienne application exécutée | Ne démontre pas l'indépendance | Compatibilité d'exploitation spécifique, hors architecture centrale |

**Recommandation :** retenir une implémentation compatible indépendante pour la plateforme, en gardant un pont transitoire explicite lorsqu'une capacité ne peut pas être reprise immédiatement. Pour un client qui accepte de changer de langage, proposer une autre offre de migration, avec ses propres critères. Mélanger ces promesses rendrait la couverture impossible à interpréter.

## 2. Ce qui existe publiquement et ce que cela démontre

### 2.1 Le format texte et les outils PC SOFT

PC SOFT documente le partage via Git et la sauvegarde textuelle des éléments. Cela fournit une voie d'acquisition préférable à une hypothèse de décompilation universelle. Le guide détaillé d'import doit cependant considérer le binaire résiduel et les éléments non convertibles. [Blog officiel PC SOFT sur les projets Git](https://blogs.pcsoft.fr/fr/obtenir-access-token-operations-pull-commit-push-projet-partage-git-heberge-chez-github/281474976710987/read.awp).

Cette voie peut servir aussi à constituer un patrimoine documentaire et des tests sans attendre le nouveau moteur. Elle ne transforme pas l'environnement PC SOFT en compilateur ouvert et ne donne pas automatiquement le droit de redistribuer ses composants.

### 2.2 `wl2net`

Le dépôt public de son auteur présente un transpileur WLangage vers C# et annonce des conversions de structures de contrôle et d'appels courants. Le README décrit explicitement des limites sur l'interface, HFSQL et l'analyse sémantique. Il est donc une piste pour étudier des transformations ou des contre-exemples, pas une preuve de compatibilité complète. [Dépôt de l'auteur et limites](https://github.com/lukimperinetti/wl2net).

Vérification complémentaire par l'API GitHub le 26 octobre 2026 : aucune licence reconnue détectée par GitHub (`license: null`), branche `main`, dépôt non archivé. Au commit `7fd8a11402e71ce38b713b06e556669c45f33942`, aucun fichier de licence ni déclaration dans le README n'a été identifié dans les éléments examinés. Une publication lisible ne suffit pas à autoriser une exploitation et redistribution générales du code. [GitHub, licences des dépôts](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository). Les pourcentages de gain annoncés dans une présentation ne sont pas repris comme mesures de cette étude. Avant réemploi : licence explicite, audit du parseur, essais des conversions numériques et contrôle des appels non reconnus. En particulier, traduire directement `ET` en court-circuit peut changer le résultat d'un projet dont l'option de compilation est différente. Le comportement doit suivre le réglage importé, car le court-circuit existe aussi dans WLangage. [PC SOFT, opérateurs logiques](https://doc.pcsoft.fr/?1512003=).

### 2.3 WXCode

L'éditeur décrit une chaîne d'import, graphe de dépendances, extraction de règles et conversion vers une nouvelle pile. Sa procédure publique mentionne les sources, le DDL et des compléments permettant de documenter les propriétés des contrôles. Cela éclaire l'intérêt d'un inventaire structuré avant conversion. Ce n'est pas, dans les pages examinées, une démonstration d'un runtime maintenant le WLangage inchangé. [Procédure de l'éditeur](https://wxcode.ai/windev-migration-guide/kb-import).

La présence d'un outil commercial d'import ou d'une démonstration ne suffit pas à conclure à une équivalence d'exécution. Une évaluation devra demander un échantillon anonymisé, les limitations par version/cible, le contrat sur les sources, le fonctionnement hors service et les résultats des tests d'origine. Aucune affirmation de réduction des coûts ou de couverture provenant du fournisseur n'est considérée ici comme vérifiée indépendamment.

### 2.4 Xojo et autres AGL

Xojo a organisé un webinaire spécifiquement destiné aux utilisateurs de WINDEV. Cette initiative est une preuve d'une offre d'accompagnement et d'une expérience RAD présentée à ce public ; elle ne démontre pas l'exécution du WLangage original. [Annonce officielle Xojo](https://forum.xojo.com/t/new-webinar-intro-to-xojo-for-windev-users/88740).

Delphi/RAD Studio et d'autres AGL peuvent constituer une cible de réécriture. Les mécanismes de modernisation décrits par Embarcadero concernent notamment les sources Delphi/C++Builder ; on ne doit pas extrapoler cette conservation des sources au WLangage. [Centre de migration Embarcadero](https://upgrade-center.embarcadero.com/).

Pour chaque AGL envisagé, demander la démonstration d'un import WLangage sur le corpus et distinguer la familiarité visuelle de la compatibilité source. Une interface de concepteur similaire peut aider la formation sans préserver un seul traitement métier.

### 2.5 Dépôts de mots-clés et documentation communautaire

Des dépôts publics recensent des mots-clés ou des pages de référence. Le fichier d'autocomplétion WLangage de la collection Notepad++ indique lui-même que ses métadonnées sont générées et demandent un travail expert. Cela peut aider à repérer des noms ; cela ne fournit ni grammaire normative, ni signatures garanties, ni disponibilité par cible. [Fichier source Notepad++](https://github.com/notepad-plus-plus/userDefinedLanguages/blob/master/autoCompletion/Wlangage.xml).

Des projets appelés `WLang` ou `WLanguage Compiler` peuvent concerner un langage totalement différent. Le nom ne permet pas de les compter comme implémentations compatibles PC SOFT. Toute veille devra vérifier l'origine, les exemples et la licence avant de retenir une solution.

### 2.6 Cartographie élargie des offres et méthodes visibles en 2026

**Vérification documentaire complémentaire au 26 octobre 2026.** Le tableau rassemble des outils, des prestations et une méthode publique. Une page publiée par un fournisseur est une source primaire pour **ce qu'il propose ou déclare**, sans constituer une validation indépendante de sa qualité. « Reprise du métier », « iso-fonctionnel », « conversion » et « sans repartir de zéro » n'impliquent pas que le développeur continuera à maintenir exactement son WLangage. Aucun achat, échange commercial ni essai de ces offres n'a été réalisé dans cette étude.

Pour les prestations, les pages examinées ne publient généralement pas de version d'outil, de grammaire ou de matrice de conformité versionnée. La date de consultation est donc le repère de cette comparaison ; les déclarations sont à confirmer sur un POC et dans le contrat. Les trois premières lignes récapitulent les pistes déjà examinées ci-dessus ; les suivantes élargissent la veille.

| Solution / auteur | Origine et repère de version | Offre ou mécanisme déclaré | Même WLangage maintenu après migration ? / preuve manquante |
|---|---|---|---|
| **wl2net** | [Dépôt de l'auteur](https://github.com/lukimperinetti/wl2net), commit examiné `7fd8a11402e71ce38b713b06e556669c45f33942` | Transpilation vers C# avec périmètre et limites annoncés ; licence à clarifier comme indiqué en §2.2 | La cible est C# ; pas de démonstration ici d'un IDE/runtime maintenant le projet WLangage intégralement inchangé. Ne pas confondre existence de transformations et conformité complète. |
| **WXCode** | [Guide propre à l'éditeur](https://wxcode.ai/windev-migration-guide/kb-import), page consultée le 26/10/2026 ; version produit non précisée dans la preuve retenue | Import et analyse du patrimoine avant transformation vers une nouvelle pile | Réemploi comme matière de migration ; continuité de maintenance WLangage non établie. POC à demander sur propriétés, événements et données. |
| **Xojo** | [Webinaire de l'éditeur pour utilisateurs WINDEV](https://forum.xojo.com/t/new-webinar-intro-to-xojo-for-windev-users/88740), annonce de l'événement | Présentation d'un autre environnement RAD et accompagnement de transition | Le webinaire n'atteste pas d'un compilateur WLangage compatible ; qualifier la réécriture, l'import et les composants nécessaires. |
| **Synelia** | [Page propre de l'offre](https://www.synelia.fr/migration-windev), consultée le 26/10/2026 ; version d'outil non publiée | Migration WINDEV/WEBDEV vers .NET, rétro-documentation puis réimplémentation assistée par IA et pilotée par développeurs ; objectif d'interface iso-fonctionnelle ; export texte à partir d'un projet ouvrable en version 25 ou ultérieure demandé | Réimplémentation dans le langage cible, explicitement décrite par le fournisseur. La fidélité annoncée et la reprise des données restent à mesurer sur le corpus client. |
| **Winfall** | [Site de l'offre](https://winfall.fr/), consulté le 26/10/2026 ; pas de version publique de l'analyseur dans la page | WINDEV/WEBDEV vers C#/.NET/Blazor ; HFSQL vers SQL Server ou PostgreSQL ; cartographie, correspondances, IA et revue humaine ; comparaison déclarée avec l'application d'origine | Maintenance en C# après bascule. Les illustrations de rapports et les gains annoncés sont des éléments de présentation du fournisseur, pas des résultats reproduits par cette étude. |
| **WinExit** | [Annonce du compte de l'entreprise](https://fr.linkedin.com/posts/winexit_windev-migration-react-activity-7518264443785416704-ogyR), complétée par [sa description de méthode](https://fr.linkedin.com/posts/winexit_architecturelogicielle-windev-refactoring-activity-7519284386350043137--4sw), consultées le 26/10/2026 ; version non précisée | Service annoncé de migration accélérée par IA, analyse de l'export, séparation du métier et de l'interface, restructuration vers une architecture web ou .NET, revue humaine et POC sur des vues critiques | Déclaration primaire de l'auteur sur réseau social. Le site `winexit.fr` indiqué par l'annonce n'a pas pu être consulté avec l'outil web ; aucun compilateur ni résultat de migration n'a été vérifié ici. |
| **Smartshift** | [Dossier propre de l'offre](https://smartshift.fr/migration-pcsoft), daté par le site du **24/07/2026** | Audit, scénarios de maintien/gel/migration de base/refonte, migration progressive, maintien de l'existant et assistance IA à la cartographie/transposition | Prestation de trajectoire et de réimplémentation, pas preuve d'un moteur compatible. Ses recommandations générales restent à confronter au besoin ; ses cas anonymisés ne constituent pas un benchmark indépendant. |
| **Dev-Booster** | [Page propre migration WINDEV](https://dev-booster.com/prestations/migration-windev), consultée le 26/10/2026 ; version des outils non précisée | Reconstruction .NET/C# ou web Symfony/React ; export automatisé HFSQL vers MySQL/MariaDB/PostgreSQL ; retour d'expérience publié sur son propre logiciel NomadBiz | Le code cible change. L'automatisation revendiquée de l'export des données ne prouve pas une conversion complète des traitements, écrans et états. Chantier propre déclaré, non audité ici. |
| **EloNeva** | [Page de prestation](https://eloneva.com/services/migration-windev-webdev/) et [méthode détaillée](https://eloneva.com/migration-windev/), consultées le 26/10/2026 ; version non précisée | C#/.NET ou React/Vue, audit, spécifications assistées par IA, lots et recette parallèle ; le site décrit aussi une transition web avec backend WINDEV conservé temporairement | La voie C# est une réécriture technique ; une interface web peut coexister avec PC SOFT. Faire préciser la trajectoire, les dépendances restantes et le langage de maintenance dans l'offre. |
| **Lexode** | [Site propre de l'offre](https://lexode.ch/), consulté le 26/10/2026 ; version produit non précisée | Portage des traitements vers un backend standard, interfaces React/Vue, mobile React Native, HFSQL vers PostgreSQL, POC puis déploiement et transfert | Réexpression du métier dans de nouveaux langages. L'exemple avant/après et les promesses de reprise intégrale ne constituent pas une preuve de compatibilité de toutes les API. |
| **Playbook migration-windev/windev-vers-dotnet** | [README à version figée](https://github.com/migration-windev/windev-vers-dotnet/blob/2f3e04c808070bb5631299a10f287d47dffd2874/README.md), commit **`2f3e04c808070bb5631299a10f287d47dffd2874` du 09/06/2026** ; [licence MIT](https://github.com/migration-windev/windev-vers-dotnet/blob/2f3e04c808070bb5631299a10f287d47dffd2874/LICENSE) | Méthode et modèles pour une migration .NET avec Cowork/Claude Code, sources texte, schéma SQL, données et captures, décisions et boucle de revue humaine | C'est un cadre documentaire réutilisable, pas un compilateur. L'inspection du dépôt ne prouve ni sa réussite sur un projet donné ni la justesse de chaque conseil technique. |

**Ce que cette veille change dans la décision.** Il existe des prestations et des outils de transformation à examiner avant de financer une plateforme complète. Une réécriture assistée peut être le meilleur choix pour une application dont l'équipe accepte un changement de langage. Elle ne satisfait cependant pas automatiquement l'objectif plus strict de ce dépôt : continuer à modifier et compiler le WLangage d'origine dans une expérience familière. Pour comparer honnêtement, faire deux évaluations séparées : coût/risque d'une migration vers une nouvelle pile et faisabilité/coût d'un runtime compatible. Les promesses de gain de coût ou de délai, l'expérience déclarée et les simulateurs tarifaires n'ont pas été utilisés ici comme mesures acquises.

### 2.7 Le playbook et la commande `/init_projet` : niveau de preuve

Le README du playbook affirme qu'un Companion IA de WINDEV 2026 propose `/init_projet` pour produire un contexte décrivant le projet. Cette affirmation est bien présente dans la source tierce consultée ; **elle n'est pas confirmée ici par une documentation PC SOFT décrivant précisément cette commande, son build, son format de sortie et ses limites**. La recherche officielle n'en a pas apporté la preuve ; cela ne démontre pas son inexistence. La mention reste une piste à vérifier sur une installation autorisée. [README figé, étape de préparation](https://github.com/migration-windev/windev-vers-dotnet/blob/2f3e04c808070bb5631299a10f287d47dffd2874/README.md).

Si l'export existe dans la version du client, l'intégrer comme **indice documentaire supplémentaire**, conserver sa provenance et le confronter au code, aux propriétés UI, au schéma et aux scénarios. Un contexte produit par IA peut omettre une règle, résumer incorrectement un événement ou ignorer une configuration. Il n'est donc ni une spécification normative du langage, ni un inventaire exhaustif, ni un substitut aux tests différentiels. La présence d'une IA intégrée en 2026, déjà documentée ailleurs dans cette étude, ne suffit pas à confirmer cette commande particulière.

**Conclusion limitée aux preuves collectées :** aucune des sources examinées dans ce chapitre n'établit une compatibilité intégrale, reproductible et indépendante avec tous les projets PC SOFT. Cette formulation ne signifie ni qu'aucun convertisseur n'existe, ni qu'aucun acteur ne peut atteindre une bonne fidélité sur un périmètre donné. Un nouvel outil, une version ou un résultat de POC peut modifier cette conclusion ; sa preuve doit être ajoutée avec date, version, corpus et limites.

## 3. Grille d'évaluation à appliquer à un fournisseur ou un prototype

La même procédure s'applique à la plateforme proposée dans ce dépôt.

| Test | Éléments à fournir | Refus ou restriction de la promesse si… |
| --- | --- | --- |
| Sources inchangées | Original, empreintes, différences, correspondance des événements | Du code généré remplace discrètement les traitements maintenus |
| Propriétés visuelles | Fenêtre dense, masques, ancrages, plans, tabulation, styles, valeurs | Des propriétés sont ignorées sans diagnostic |
| Options de compilation | Projet avec variantes de court-circuit, portées et conversions | La version du langage est la seule information capturée |
| Données | Parcours indexés, filtres, NULL, doublons, verrous et transactions | Le fournisseur montre seulement une requête SQL simple |
| État | Pagination stable, ruptures, polices, imprimante et export | La preuve est une capture d'écran d'aperçu |
| Interop | DLL/COM/Office/matériel réellement utilisé | La cible est annoncée sans architecture et pilotes compatibles |
| Débogage | Pas à pas dans le traitement d'origine, pile et variables WLangage | Le développeur doit comprendre le code généré pour corriger un incident |
| Sortie de la plateforme | Projet et dépendances exportés, build sur poste vierge | Un service distant secret reste nécessaire sans l'avoir annoncé |
| Maintenance | Mise à jour du compilateur et retour à une version antérieure | Un changement d'outil modifie silencieusement le comportement |
| Licence | Code réutilisé, composants redistribués, coûts et droits par cible | La publication du code est confondue avec une autorisation de réemploi |

## 4. Fabriquer, assembler ou acheter

**À fabriquer comme cœur du produit :** modèle de compatibilité, import versionné, analyse sémantique WLangage, IR, runtime des conventions spécifiques, moteur d'événements, adaptateur `H*`, correspondance source/débogueur et registre de preuves. Ce sont les éléments qui déterminent directement la promesse faite à l'utilisateur.

**À assembler si leur comportement et licence conviennent :** moteur de rendu natif, éditeur de texte, protocoles LSP/DAP, gestion Git, pilote SQL, bibliothèques réseau et chiffrement, outils de packaging et de tests. Chaque dépendance reste derrière une interface remplaçable et des contrats testés.

**À acheter éventuellement :** composants complexes tels que tableur, traitement de texte, reporting ou connecteurs métier, après preuve de leurs exigences. Leur présence au catalogue ne dispense pas du travail pour préserver les propriétés, événements et sorties attendus par le code existant.

Un plugin tiers ne doit pas faire disparaître une exigence du backlog. Il change sa stratégie de réalisation en « composant externe », ajoute les versions et licences au manifeste et conserve les critères d'acceptation.

## 5. Recherche restante avant une sélection irréversible

La veille de cette étude n'est pas un recensement contractuel de tous les fournisseurs du marché. Pour lancer une réalisation : ouvrir un dossier d'évaluation par solution, relever une version ou un commit précis, obtenir une licence, importer le même corpus et publier les résultats bruts reproductibles. Un outil peut être utile sans satisfaire l'ensemble de l'objectif ; sa portée doit rester visible.

La solution recommandée est donc une architecture et une méthode de preuve, pas une affirmation qu'aucune alternative ne pourra jamais exister. L'évaluation devra être réactualisée avant tout achat ou choix technique majeur.
