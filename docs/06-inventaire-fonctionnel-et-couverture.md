# Inventaire fonctionnel et qualification du profil indépendant

Date de recherche : 26 octobre 2026. Nature du livrable : cahier des exigences de la future solution, avec références documentaires et méthode de certification. Aucun compilateur, importeur ou adaptateur de compatibilité n'est implémenté dans ce dossier.

## Contrainte normative : aucun logiciel PC SOFT dans la chaîne

L’instruction explicite de l’utilisateur est : **« Aucune utilisation de dll ou d’outil pc soft »**. Elle s’applique à tous les maillons : acquisition/import des sources, construction, CI, tests, installation, exécution et services distants. Aucune DLL, aucun SDK, outil, runtime, pilote ODBC/OLE DB, connecteur natif, moteur ou serveur PC SOFT ne peut être utilisé, même temporairement, chez un tiers ou pour produire une référence de test. Il n’existe pas de variante hybride autorisée dans ce profil.

La documentation publique de PC SOFT demeure une source passive sur les comportements à étudier. Les fichiers sources, exports, résultats, captures et traces **déjà fournis** peuvent être analysés par des lecteurs indépendants. Le plan ne demande ni ouverture/conversion sous WINDEV ni nouvelle extraction par un outil PC SOFT. Un format opaque reste inventorié et bloquant tant qu’un lecteur indépendant n’est pas établi ; l’absence de fichier exploitable ne justifie pas un détour par l’outillage exclu.

Les noms WLangage et les familles `H*`, `Table*`, `UI*`, états et FAA sont conservés comme contrats de référence. Ils peuvent être réimplémentés indépendamment en gardant le code source lorsque leurs règles sont établies. Les API H retenues ciblent un runtime propre et PostgreSQL, sans serveur ni pilote HFSQL. Les DLL et outils .NET ou tiers **non-PC SOFT** restent des choix techniques possibles, sous contrôle de provenance et de dépendances transitives. Cela ne prouve aucune équivalence de la nouvelle implémentation avec les comportements historiques.

F-0519 est une exigence **P0 bloquante du profil** : contrôler paquets, SBOM, modules, processus, pilotes et services utilisés, y compris les dépendances transitives et les services distants. Toute présence active de PC SOFT bloque la chaîne et la release. Ce contrôle est spécifié, non implémenté dans ce dossier.

## 1. Ce que contient l'inventaire

Le fichier [fonctionnalites.csv](../data/fonctionnalites.csv) décrit **519 exigences**, réparties en **17 domaines**. Chaque ligne possède un identifiant stable, un périmètre, une priorité, une stratégie et un critère d'acceptation. Il organise les exigences selon la chaîne de migration : reprise du projet, compréhension du code, génération, conservation du comportement, qualification, installation et exploitation. Ce classement ne démontre pas la couverture de chaque API de ces étapes. Seize exigences P0 disposent désormais de références ciblées avec limites explicites ; leur précision documentaire ne prouve aucune conformité d’exécution. Le registre [sources-inventaire.json](../data/sources-inventaire.json) distingue les références thématiques des observations ponctuelles et précise le mode d'accès réellement obtenu.

Cette matrice est un cahier d’exigences destiné à devenir le backlog de référence ; son nombre de lignes ne mesure pas la couverture du langage. **Elle ne constitue pas une liste certifiée de toutes les fonctions WLangage, surcharges, constantes, propriétés et cibles de toutes les versions PC SOFT.** Les signatures API ne se déduisent pas d'une liste de familles. L'exhaustivité demandée devient une obligation de fermeture du périmètre et de traçabilité, décrite ci-dessous, avant toute promesse de compatibilité complète.

Cette distinction change le produit à construire : le futur IDE doit pouvoir expliquer, pour chaque objet d'un projet, s'il est importé depuis un fichier fourni, compilé, émulé indépendamment ou bloquant. Un pourcentage global sans dénominateur explicite masquerait les incompatibilités les plus coûteuses.

### Répartition

| Domaine | Exigences | Exemple de frontière à qualifier |
|---|---:|---|
| Import et projet | 31 | Version, format hybride, sections opaques, .MCU, constantes et événements |
| Langage | 41 | Options de compilation, conversions, portées, POO, indirection |
| Bibliothèque standard | 38 | Encodage, fichiers, sérialisation, cryptographie, scripts, dates |
| IDE | 30 | Complétion, navigation, débogage du source original, extensions |
| Designer | 23 | Ancrages, héritage, styles, traduction, accessibilité |
| Champs | 73 | Champs simples, tables, TCD, documents, hôtes natifs, chat IA |
| Événements et FAA | 20 | Ordre de traitement, focus, modalité, menus et préférences |
| Données | 72 | Analyse, API H, moteurs SQL, administration SaaS, TCD |
| États et documents | 22 | Blocs, pagination, imprimantes, exports et signatures |
| Intégrations | 40 | Protocoles, .NET, DLL, COM, matériel, services cloud, legacy |
| Web | 23 | Séparation client/serveur, sessions, AWP, AJAX, droits, déploiement |
| Mobile | 23 | Cycle de vie, permissions, hors ligne, matériel, stores |
| Construction et déploiement | 18 | Build reproductible, installation, mise à jour, signature |
| Qualité | 24 | Références fournies, indépendance, erreurs, performances, périphériques |
| Sécurité et gouvernance | 16 | Groupware, secrets, isolation, données sensibles, licences |
| Collaboration | 10 | Git/GDS, fusion visuelle, exigences, documentation, CI |
| Exploitation et support | 15 | Watchdog, reprise, support, modes hors ligne et réversibilité |
| **Total** | **519** | **Aucun de ces points n'est marqué compatible par anticipation** |

Les ajouts de revue couvrent notamment UML, MCD Merise, full-text, HBase/HDFS, aide contextuelle, anciennes API SQL, vues matérialisées et intégrité inaltérable. Les hôtes ActiveX, OLE, XAML, Java et Flash sont distingués ; les cibles sont restreintes ou signalées comme nécessitant un remplacement. COM/TAPI/TWAIN ne deviennent pas disponibles sur Linux ou mobile par une simple recompilation. Réplication universelle et serveur spare ont deux contrats séparés.

Les domaines se recoupent volontairement aux frontières : « champ TCD » concerne l'objet visuel ; ses caches et recalculs concernent le moteur de données ; son export concerne la restitution. Il ne faut pas additionner ces lignes pour annoncer un nombre de fonctions PC SOFT reproduites.

### Lecture des colonnes du CSV

| Colonne | Sens et règle de lecture |
|---|---|
| `id` | Identifiant d'exigence `F-0001` à `F-0519` ; ne pas renuméroter après publication |
| `domaine`, `sous_domaine` | Classement de navigation, sans déduire les dépendances techniques |
| `fonctionnalite` | Capacité à traiter ; certaines familles exigent ensuite plusieurs contrats API |
| `produits_reference` | Famille produit dans laquelle rechercher les usages ; ne signifie pas que chaque fonction existe dans chaque édition citée |
| `cibles_proposees` | Ambition de la future solution ; ce champ ne décrit pas les disponibilités officielles PC SOFT |
| `priorite` | Ordre proposé du programme, à recalibrer par les applications pilotes |
| `strategie` | Voie de réalisation envisagée, sans garantie de faisabilité acquise |
| `statut_preuve` | Exigence proposée ; référence thématique ou ciblée sur un contrat partiel |
| `critere_acceptation` | Résultat observable à vérifier, puis à transformer en scénarios versionnés |
| `source_url` | Contexte documentaire historique uniquement ; ne constitue ni une autorisation de dépendance logicielle ni une preuve de compatibilité |
| `statut_implementation` | Toutes les lignes : `non implémenté` |
| `portee_source` | Rappelle la contrainte utilisateur et les limites de la source ; aucune URL documentaire ne remplace la décision de périmètre |
| `nb_fonctions_couvertes` | `INCONNU` sur toutes les lignes : aucun rattachement complet exigence→fonctions/surcharges n’est établi ; ce champ n’est ni zéro ni un compteur de fonctions implémentées |
| `statut_rattachement_api` | `non établi` sur toutes les lignes : le registre des contrats API n’est pas constitué |
| `decision_perimetre` | Décision opérationnelle par exigence : réimplémenter indépendamment, importer les fichiers fournis, intégrer un tiers non-PC SOFT, ou détecter une capacité PC SOFT exclue et bloquer/remplacer |

Les familles de référence ne sont pas supprimées parce que leur réalisation d’origine est PC SOFT. La matrice distingue leur contrat applicatif de leur outil ou moteur historique : H* et les champs peuvent être émulés ; le moteur HFSQL, ses pilotes, la Fabrique logicielle, GDS, WDMSG/WDTRAD, Robot et États & Requêtes PC SOFT sont exclus. Les anciens services RPC WINDEV ou SQLConnecteWS ne peuvent être appelés par un adaptateur distant ; un service de remplacement doit être indépendant et son contrat qualifié. Les fonctions d’import exploitent seulement les fichiers préexistants fournis. Une exclusion d’outil ne vaut donc ni exclusion automatique de sa famille fonctionnelle ni compatibilité automatique de son remplacement.

Les références thématiques sont marquées ainsi pour empêcher qu'une URL générale soit prise pour une validation ligne par ligne. Les noms d'API historiques dans les exigences sont des sujets d'investigation et de qualification, pas une déclaration universelle de disponibilité ou de droit de redistribution.

### Priorités proposées

- **P0 : 269 exigences** liées au diagnostic fiable, au noyau de compatibilité, aux premières applications Windows, aux données, aux états et à la démonstration de non-régression. P0 signifie « nécessaire avant de déclarer réussi le périmètre qui l'utilise », pas « à livrer entièrement dans le premier prototype ».
- **P1 : 230 exigences** de parité produit, intégrations et extension aux cibles Web/mobile, dont l'ordre dépendra de la fréquence réelle dans les pilotes.
- **P2 : 20 exigences** de spécialisations ou de legacy à isoler derrière un contrat précis. P2 ne signifie jamais ignorable lorsqu'une application en dépend.

Une application industrielle utilisant DDE, un automate ou une imprimante particulière peut rendre sa dépendance P2 prioritaire pour son pilote. L'ordre global du backlog n'autorise pas une perte fonctionnelle silencieuse.

## 2. Pourquoi l'exhaustivité API exige un autre registre

### Une exigence n’est pas une fonction WLangage

Les **519 exigences** désignent des objectifs de produit à des niveaux différents : une règle de sémantique, un import d’objet, un champ, une famille de protocoles, un déploiement ou une mesure de qualité. Une exigence peut concerner plusieurs dizaines de fonctions et de surcharges ; plusieurs exigences peuvent aussi concerner la même fonction. Les compter ne donne donc ni le nombre de fonctions WLangage inventoriées ni le nombre de fonctions prises en charge.

Le chiffre **3 480** mentionné dans la critique ne peut pas servir de dénominateur normatif. Le 26 octobre 2026, l’ancienne URL `https://windev.com/wlanguage.htm` et l’ancien chemin de liste ont redirigé en HTTP vers l’accueil anglais, sans ce compteur. Une page régionale [liste des commandes WLanguage](https://www.windev.la/wlanguage/list-of-wlanguage-programming-commands.htm) conserve un extrait indexé annonçant 3 480 fonctions, mais sa version n’est pas qualifiée et son accès HTTP direct a répondu 503 pendant cette vérification. La [page WLangage actuelle de PC SOFT](https://pcsoft.fr/wlangage.htm), liée par l’accueil officiel et lue en HTTP 200, annonce **plus de 4 500 fonctions**. Ces nombres éditoriaux ne définissent ni les surcharges comptées, ni les versions, cibles, propriétés ou constantes applicables à un projet.

Aucun ratio entre 519 exigences et l’un de ces compteurs n’est calculé : les unités et les périmètres sont différents. Les colonnes `nb_fonctions_couvertes=INCONNU` et `statut_rattachement_api=non établi` rendent cette absence de correspondance explicite dans le CSV. **La couverture API qualifiée mesurée est `N/A`**, car il n’existe ici ni registre API fermé ni campagne de tests de conformité exécutée. Tous les statuts d’implémentation restent « non implémenté ». La présence de critères d’acceptation documentés et de contrôles de structure des fichiers ne constitue pas une exécution de ces critères.


L'index officiel des fonctions WLangage ouvre cinq branches : champs/pages/fenêtres, communication, fonctions Web, fonctions Mobile et fonctions standard. Les catégories sont paginées. Les rubriques de syntaxe, les propriétés et HFSQL possèdent aussi leurs points d'entrée. Lire cette seule première page ne donne donc pas un dénominateur complet. [Index officiel des fonctions WLangage](https://doc.pcsoft.fr/fr-FR/search2.awp?cat=fonctions-wlangage%2C489&origin=browse), [accueil de la documentation](https://doc.pcsoft.fr/fr-FR/).

Un appel peut également avoir une syntaxe classique et une syntaxe préfixée ; l'existence des deux formes n'implique pas deux comportements métier différents. Les regrouper demande une correspondance explicite, tout en conservant chaque signature dans le registre. [Présentation du WLangage](https://doc.pcsoft.fr/fr-FR/?1410087578=).

Les icônes et remarques de disponibilité doivent être lues au niveau de chaque fonction et de ses paramètres. Par exemple, la documentation de `HNumEnr` expose une dépendance au moteur HFSQL ; la documentation de `ExécuteRequêteSQL` décrit des différences selon connexion et cible. Un accès SQL réussi n'établit pas l'équivalence des fonctions H. [HNumEnr](https://doc.pcsoft.fr/?3044063=), [ExécuteRequêteSQL](https://doc.pcsoft.fr/fr-fr/?1000024948=).

Le périmètre de certification est un tuple, et non un simple numéro d'année :

```text
profil = produit + version complète/build + édition/mode + cible/architecture
       + langue/vocabulaire + options de compilation + connecteur/moteur
       + OS/locale + dépendances natives utilisées
```

L'édition et le mode SaaS doivent être enregistrés. Les mises à jour officielles distinguent des fonctionnalités accessibles selon ce mode et décrivent aussi des changements de vocabulaire et de types. La version affichée en tête d'une page Web peut différer du profil effectivement choisi par le projet. [Mises à jour WINDEV 2025](https://doc.pcsoft.fr/fr-GEN/?9000050=&verdisp=300).

Il faut aussi conserver les options du projet : une option de court-circuit ET/OU ou de copie des tableaux peut changer le résultat sans modifier une seule ligne de code. L'importeur doit relever et conserver cette configuration depuis les fichiers ou preuves déjà fournis, sans ouvrir un IDE PC SOFT. [Description du projet, compilation](https://doc.pcsoft.fr/?9500218=).

La configuration du passage des paramètres est elle aussi sémantique. La brochure officielle 2026 décrit le maintien du mode historique par référence, un choix projet par valeur et des mots-clés explicites de passage ; elle ne suffit pas à établir la disponibilité de toutes les surcharges par élément ni la priorité appelant/appelé. F-0046 couvre les variantes de comportement, F-0518 impose la résolution et la provenance du mode effectif pour chaque appel. Toute règle inconnue reste à caractériser avant génération. [Brochure officielle 2026, page PDF15, nouveautés133–135](https://fr.pcsoft-windev-webdev.com/brochure-WX2026.pdf).

## 3. Procédure de fermeture du catalogue

### 3.1 Fixer la baseline

Choisir les versions et builds de référence depuis les métadonnées et preuves déjà fournies, documenter l’accès à leur documentation et sélectionner les cibles indépendantes réellement promises. La première baseline recommandée est étroite : une famille de projets Windows et quelques applications métier représentatives. Les éditions 2025 et les annonces 2026 alimentent la recherche ; aucune disponibilité 2026, encore moins une version ultérieure, ne doit être inférée sans sa fiche et son build.

Enregistrer ce qui reste hors périmètre, avec justification, dépendances et condition d'entrée. Un objet hors périmètre présent dans un projet produit un blocage ou une décision de migration explicite ; il n'est pas ignoré par le générateur.

### 3.2 Récolter les métadonnées autorisées

Parcourir les index officiels et leurs paginations, puis leurs entrées pertinentes : syntaxe, fonctions, variantes préfixées, types, propriétés, constantes, événements, erreurs, connecteurs, objets projet et formats d'échange. Respecter les conditions d'accès, limiter la charge, conserver la provenance et les échecs. La documentation reste la propriété de son éditeur ; le registre contient principalement des identifiants, noms, liens et qualifications originales.

Pour chaque collecte, consigner : URL initiale, URL normalisée, langue, version sélectionnée, date/heure, mécanisme d'accès, statut HTTP, hash du contenu d'observation conservé dans l'environnement autorisé, nombre d'entrées et pagination attendue/observée. Une erreur 403 ou une pagination manquante devient un manque de preuve. L'index de cette étude a été accessible en HTTP public, tandis que certaines ouvertures du moteur Web ont échoué ; aucun contournement d'accès privé n'est nécessaire à ce livrable.

Les dépôts tiers de documentation ou de pseudo-transpilateurs peuvent révéler des pistes. Leur compteur n'est ni un oracle sémantique ni une autorisation de recopier leur corpus. Leur version et leur licence doivent être qualifiées séparément.

### 3.3 Normaliser sans fusion abusive

Utiliser un identifiant canonique interne indépendant du nom traduit, conserver l'identifiant documentaire officiel lorsqu'il existe. Enregistrer les alias FR historique, FR générique et anglais ; ne pas fusionner les surcharges sur la seule base du nom. Les constantes identiques en apparence peuvent avoir des disponibilités différentes selon le type d'objet.

Le niveau de détail proposé pour un futur registre `api-contracts` est le suivant :

```text
symbol_id, official_doc_id, kind, canonical_name, aliases[]
receiver_type, overload_id, parameters[], defaults, return_type
side_effects, implicit_context, errors[], constants_used[]
product, source_build, edition_mode, compiler_options, target, connector
availability, documentation_observation, implementation_status
test_ids[], evidence_runs[], known_divergences[], owner
```

`kind` distingue au minimum instruction, fonction, surcharge, type, propriété, constante, événement et code d'erreur. `availability` distingue documenté disponible, documenté absent, ambigu et non investigué. `implementation_status` distingue non commencé, partiel, réalisé non qualifié et qualifié pour un profil précis.

### 3.4 Découvrir les usages effectifs

Analyser chaque application pilote : appels directs et préfixés, propriétés, événements, liaisons de données, requêtes, états, ressources et composants. Résoudre les références statiques ; journaliser les noms calculés, l'indirection, la compilation dynamique, les procédures injectées et les .MCU comme surfaces à observer.

Prévoir une revue humaine pour les appels dynamiques non résolus. Exploiter les traces et captures préexistantes fournies sans lancer ni instrumenter une application utilisant PC SOFT. Une trace sans appel observé ne prouve pas qu’un chemin est inutile. Les plugins, DLL, ActiveX et composants externes sans sources restent inventoriés séparément : un composant PC SOFT est exclu ; un composant tiers doit prouver sa provenance et l’absence de dépendance transitive PC SOFT.

### 3.5 Croiser documentation, import et exécution

Établir trois ensembles distincts : éléments documentés du profil historique, éléments présents dans les fichiers fournis et éléments exercés dans le runtime indépendant ou attestés par des résultats préexistants. Consigner séparément le type et la force de chaque preuve ; ne pas assimiler une fixture documentaire à une mesure différentielle contre l’ancien moteur. Produire les différences : symbole non reconnu, objet opaque, API documentée absente du runtime, comportement exercé sans preuve, objet déclaré mais non exercé.

La fermeture du catalogue documentaire exige une vérification de toutes les pages de pagination et des branches du profil. La fermeture d'un pilote exige que chacun de ses usages dispose d'une stratégie et d'un état de preuve. Ce sont deux obligations différentes ; une migration peut être complètement qualifiée sur un périmètre limité sans avoir réimplémenté toute la plateforme.

## 4. Ce qu'une preuve doit contenir

Une exigence du CSV devient un ou plusieurs scénarios avec entrées, préconditions, profil exact, données isolées et résultat attendu. La preuve lie l'identifiant d'exigence à la signature utilisée, au test, à l'exécution et aux artefacts observés.

Pour chaque surcharge réellement utilisée, prévoir les cas nominal, limites et erreur ; ajouter NULL, paramètres omis, conversions, locale et interaction de contexte lorsque pertinents. Les erreurs demandent code, catégorie et état des données ; comparer seulement une chaîne de message traduite serait fragile. La documentation distingue erreurs d'exécution et erreurs de programmation : les tests doivent donc couvrir leurs circuits respectifs. [Gestion des erreurs en exécution](https://doc.pcsoft.fr/fr-FR/?3034016=).

Les références admissibles sont les résultats, captures, fichiers et traces déjà fournis, avec leur provenance lorsqu’elle est connue, ainsi que les fixtures construites à partir de contrats documentés ou d’exigences métier explicites. F-0403 exclut toute nouvelle exécution PC SOFT, même sur le poste d’un client. Les tests s’exécutent uniquement dans l’implémentation indépendante. Horloge, hasard, réseau et ordre des threads y sont contrôlés ou assortis d’un contrat de tolérance explicite ; les effets externes sont simulés ou confinés. Une référence absente n’empêche pas de prototyper, mais interdit de présenter le comportement correspondant comme une équivalence historique démontrée. Une trace historique isolée ne prouve pas tous les cas limites.

| Surface | Observation nécessaire | Exemple de divergence bloquante |
|---|---|---|
| Langage | Valeur, type, effets de bord, erreur | Second opérande ET exécuté dans le mauvais profil |
| Événements | Séquence, paramètres, focus, modalité | Validation contournée lors d'une fermeture |
| API H* indépendantes sur PostgreSQL | Buffer et curseur émulés, état, verrou, transaction | H implicite vise la mauvaise source ; aucune référence disponible pour conclure |
| SQL | Multiensemble de lignes, types, ordre contractuel | NULL transformé en chaîne vide |
| UI | État sémantique, accessibilité, capture sous conditions fixes | Ligne masquée exportée malgré une restriction |
| États | Texte, pages, positions, polices, réglage imprimante | Facture repartie sur une page de plus |
| Mobile | Cycle de vie, permissions, reprise hors ligne | Écriture locale perdue après arrêt du processus |
| Déploiement | Paquet, installation, signature, mise à jour, rollback | Version installée incapable de lire le schéma migré |

Les fichiers de scénarios WLangage déjà fournis peuvent être inventoriés et interprétés par un moteur de tests indépendant lorsque leur syntaxe et leurs API sont prises en charge ; l’éditeur de tests et les runtimes PC SOFT ne sont jamais lancés. La documentation décrit les scénarios historiques pour fenêtres, procédures et classes : elle aide à définir le lecteur indépendant, sans prouver l’existence d’un format public complet ni une couverture métier complète. [Tests unitaires, contexte documentaire](https://doc.pcsoft.fr/?1410086932=).

## 5. Calculs de couverture sans fausse précision

Toutes les mesures ci-dessous sont **à calculer dans la future solution**. Pour ce dépôt de recherche : aucune compatibilité exécutée n'est mesurée, et les 519 exigences sont non implémentées. Le rattachement des exigences aux contrats API n’est pas établi : nombre de fonctions couvertes `INCONNU`, couverture qualifiée mesurée `N/A`, aucune campagne de conformité exécutée. Ne pas remplacer ces valeurs par un pourcentage nul ou un quotient exigences/fonctions.

Définir `D_p` comme l'ensemble des contrats API applicables au profil `p` ; `U_a,p` comme les contrats utilisés par l'application `a` ; `Q_p` comme ceux qualifiés par un test indépendant assorti d’un résultat attendu admissible et d’une provenance explicite. Un contrat inclut sa surcharge et son profil.

```text
Couverture catalogue(p) = |Q_p ∩ D_p| / |D_p|
Couverture usages(a,p)  = |Q_p ∩ U_a,p| / |U_a,p|
Couverture import(a)   = objets compris sans perte / objets inventoriés
Couverture scénarios  = scénarios métier acceptés / scénarios métier requis
```

Un dénominateur incomplet rend la mesure non calculable ; afficher « inconnu » et le manque à résoudre. Un symbole opaque ou un appel dynamique non résolu interdit d'annoncer la couverture complète des usages. Les exclusions restent visibles et ne sont pas retirées après coup pour améliorer un score.

Une mesure pondérée par fréquence d'appel peut guider la priorité, mais ne remplace pas la couverture brute : une seule fonction peu fréquente peut valider une clôture comptable ou signer une facture. Publier aussi les blocages, divergences connues, chemins dynamiques et scénarios non exercés.

La ligne d'exigence elle-même n'est pas une unité suffisante de certification. Une ligne « REST » peut engendrer des dizaines de contrats ; une ligne « champ Table » ne devient pas validée parce qu'une table vide s'affiche. La granularité de preuve doit suivre le comportement réel.

## 6. Conditions d'acceptation d'une migration

Un pilote est prêt à basculer lorsque le contrôle F-0519 confirme l’absence de dépendance PC SOFT, que tous ses éléments inventoriés ont une décision de périmètre et une stratégie indépendantes explicites, que les usages statiques et dynamiques pertinents sont résolus, que les scénarios métier obligatoires passent, que les différences de données et documents sont expliquées, et que l’installation ainsi que le retour arrière ont été exercés. Aucun composant natif manquant, champ supprimé, événement ignoré ou conversion avec perte ne peut être masqué par une génération réussie.

La liste du CSV n'accorde pas le droit d'omettre une capacité découverte après l'audit. Ajouter l'exigence avec un nouvel identifiant, son propriétaire, son origine et ses dépendances ; conserver l'historique. Pour chaque release, publier le profil indépendant qualifié, le rapport F-0519, le périmètre des pilotes, les limites et les preuves correspondantes. La qualification des tests indépendants ne devient une affirmation d’équivalence historique que dans les limites des références préexistantes réellement disponibles.

Les surfaces à surveiller particulièrement sont les .MCU et autres codes post-déploiement, dictionnaires .DIC abonnés, états personnalisables, chaînes traduites réintégrées, composants sans source, options du projet, intégrations DDE/RPC/X10/UPnP, TCD et caches, administration SaaS, robots de surveillance, et règles implicites des fonctions H. Elles doivent être cherchées activement dans l'audit, même lorsqu'elles ne sont pas visibles dans les principaux écrans du projet.

Cette procédure permet une affirmation vérifiable : « cette application, dans ces profils et ces scénarios, garde son code et ses comportements qualifiés ». La promesse « tout projet de toute version fonctionne sans changement » resterait dépourvue de preuve tant que le catalogue documentaire, les composants externes et les comportements dynamiques ne sont pas fermés.
