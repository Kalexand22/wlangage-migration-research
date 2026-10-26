# Données, intégrations, impressions et plateformes

Date de recherche : **26 octobre 2026**. Ce chapitre distingue les comportements documentés de PC SOFT, les décisions proposées pour le nouveau produit et les points à vérifier sur de véritables projets. Aucun accès à une installation WINDEV, à un serveur HFSQL, à un projet client ou à une imprimante n'a été fourni : les architectures et critères ci-dessous sont des spécifications, pas des compatibilités déjà démontrées.

## 1. Décision structurante : séparer trois migrations

**Recommandation : permettre de migrer le langage, l'interface et la base à des moments différents.** Changer simultanément les trois rend les écarts difficiles à attribuer. Le premier chemin doit pouvoir conserver HFSQL, reprendre les procédures WLangage et reconstruire seulement un périmètre d'interface contrôlé. Un second chemin permet de conserver l'application existante pour certaines fonctions pendant que les nouveaux modules appellent une API. La migration vers PostgreSQL constitue un chantier indépendant, activé après validation fonctionnelle.

Il faut distinguer les accès **depuis** WLangage vers une base tierce, les accès **depuis** un langage tiers vers HFSQL et la réimplémentation de l'API HFSQL. PC SOFT documente des connecteurs natifs utilisables par WLangage et, séparément, un pilote ODBC permettant à des logiciels externes de lire et écrire dans HFSQL. Cela n'établit ni une API C publique équivalente à toutes les fonctions `H*`, ni le droit de redistribuer n'importe quelle bibliothèque du framework. [Connecteurs dans HOuvreConnexion](https://help.windev.com/en-US/?3044107=), [pilote ODBC HFSQL](https://doc.pcsoft.fr/fr-FR/?3044179=).

| Parcours proposé | Ce qui change | Ce qui reste à qualifier | Usage conseillé |
|---|---|---|---|
| A. Nouveau runtime, HFSQL conservé | Compilateur et interface | Connexion externe, transactions, erreurs, curseurs, performances | Première migration d'un logiciel de gestion |
| B. Application hybride par API | Certains écrans et services | Contrats, identité, sessions, transaction métier | Gros patrimoine ou intégrations Windows |
| C. PostgreSQL sous API `H*` compatible | Moteur de données | Sémantique des parcours, clés, verrous et SQL | Après validation du noyau de compatibilité |
| D. Modernisation explicite | Architecture et parfois appels applicatifs | Travail de transformation du code assumé | Modules nouveaux ou exigences incompatibles |

La présence d'un connecteur PostgreSQL dans l'offre PC SOFT crée une autre possibilité d'expérimentation : tester d'abord le changement de base dans l'environnement d'origine, puis comparer le résultat au nouveau runtime. Cela aide à séparer les écarts provenant de PostgreSQL de ceux du compilateur ; l'accès natif, ses limites et ses conditions doivent néanmoins être qualifiés pour la version possédée. [HOuvreConnexion](https://help.windev.com/en-US/?3044107=).

## 2. Reprendre correctement une analyse et les fichiers HFSQL

### 2.1. L'inventaire initial

Une reprise ne doit pas considérer les fichiers de données comme le modèle complet. Il faut rapprocher l'analyse de développement, la description réellement déployée et les décisions prises dynamiquement par l'application. Le modèle interne proposé conserve : noms logiques et physiques, alias, chemins, connexion, type et taille de chaque rubrique, précision et échelle numériques, encodage, valeurs par défaut, nullabilité, clés simples et composées, règles de tri, unicité, intégrité, index spécialisés et métadonnées de génération.

Les fichiers usuels comprennent `.fic` pour les données, `.ndx` pour les index et `.mmo` pour les mémos ; ils apparaissent explicitement dans les instructions officielles de déploiement Android. Il faut aussi inventorier les journaux, fichiers temporaires, transactions, sauvegardes et index spécialisés réellement présents, sans supposer que ces trois extensions suffisent à toute installation. Le fichier `.wdd` intervient notamment dans la configuration du pilote ODBC pour décrire le schéma. [Déploiement Android](https://doc.pcsoft.fr/en-us/?1410087576=&name=deploying_android_application), [configuration ODBC](https://doc.pcsoft.fr/fr-FR/?3044179=).

**Procédure proposée :**

1. Faire une copie cohérente et restaurable avec l'outil ou le mécanisme de sauvegarde approprié ; une copie de fichiers ouverts n'est pas un protocole universel de sauvegarde.
2. Relever les versions du serveur, des clients, du pilote et de la description déployée ; garder l'architecture 32/64 bits et le système.
3. Exporter le schéma par les moyens autorisés disponibles. L'éditeur d'analyse sait générer un script SQL avec des options d'index et d'intégrité ; utiliser cet export comme entrée contrôlable, puis rapprocher les métadonnées non représentées par SQL. [Génération de scripts SQL](https://doc.windev.com/en-US/?2011027=&name=Generer_Scripts_SQL).
4. Parcourir le code pour trouver les créations dynamiques, alias, changements de connexion, de nom et de répertoire ; calculer un graphe des accès.
5. Construire un manifeste versionné et une table de correspondance entre chaque rubrique source et sa représentation cible.
6. Vérifier sur échantillons puis sur la totalité des données ; ne jamais conclure à l'équivalence sur le seul succès d'un export CSV.

L'analyse reste visible dans le nouvel IDE sous des concepts familiers : fichiers/tables, rubriques, clés, liaisons et connexions. Le moteur de stockage peut être différent sans imposer au développeur de réécrire toute sa représentation mentale. Les écarts de capacités doivent être signalés à la génération du schéma.

### 2.2. HFSQL Classic et Client/Serveur ne sont pas le même adaptateur

**Classic :** qualifier chemins locaux et réseau, partage de fichiers, droits du système, accès concurrents, interruptions réseau, antivirus, reconnexions, nettoyage et gestion de l'espace disque. Un exécutable qui manipulait directement des fichiers ne devient pas automatiquement un service centralisé.

**Client/Serveur :** qualifier authentification, noms de bases, connexions, droits de serveur/base/table, administration, tâches planifiées, traitements stockés et flux réseau. Le Centre de Contrôle expose notamment connexions, blocages et transactions ; ces fonctions d'exploitation font partie de la reprise. [Gestion des fichiers HFSQL C/S](https://doc.pcsoft.fr/?35400016=).

**Proposition de produit :** deux profils distincts dans le manifeste, chacun avec version et capacités prouvées. Les opérations d'administration passent par une interface séparée de l'accès métier ; le runtime normal n'obtient pas de droits de réparation ou de suppression de bases.

## 3. Pourquoi traduire `H*` en SQL demande un moteur de compatibilité

Les fonctions `H*` manipulent à la fois des données et un état d'exécution. Une fonction qui renvoie le bon enregistrement peut encore être incompatible si elle change le tampon courant, le parcours, une erreur ou un verrou différemment.

Deux exemples documentés illustrent ce risque. `HAjoute` distingue l'effet de l'ajout sur le parcours avec `hAffecteParcours` et `hEcritureDéfaut`. `HNbEnr` peut compter différentes catégories d'enregistrements, ignore le filtre courant et comporte des particularités selon le connecteur. Les ramener à un `INSERT` et à un `COUNT(*)` génériques perd des comportements observables. [HAjoute](https://doc.pcsoft.fr/?3044147=), [HNbEnr](https://doc.pcsoft.fr/fr-FR/?3044006=).

### 3.1. Contrat d'état proposé

Chaque contexte de données doit porter au minimum :

```text
DataContext
  identity: projet, thread/tâche, connexion, transaction
  descriptors: analyse et déclarations dynamiques
  sourceStates[sourceId]:
    currentRecordBuffer, previousValues, changedItems
    browseKey, browseDirection, bookmark, searchCriterion
    filterDefinition, found, outOfBounds, deletedOrCrossedState
    lastError, duplicateError, integrityError, lockError
    heldLocks, pendingWrites, queryResources
```

Il s'agit d'un modèle conceptuel, pas d'une déclaration de l'implémentation interne PC SOFT. Sa portée exacte doit être mesurée : un contexte global, partagé entre tous les threads et toutes les sessions web, provoquerait des contaminations entre traitements.

L'interface d'adaptation proposée expose des opérations sémantiques : `seek`, `readFirst`, `readNext`, `readAtBookmark`, `insert`, `updateCurrent`, `deleteCurrent`, `lock`, `unlock`, `begin`, `commit`, `rollback`, `executeQuery`, `describeSource`. Elle doit accepter les options WLangage déjà normalisées par le compilateur et retourner un résultat structuré. Le rendu des erreurs WLangage reste dans le runtime ; les codes natifs sont conservés pour le diagnostic.

### 3.2. Matrice de conformité de données

| Domaine | Points à reproduire ou à déclarer incompatibles | Preuve nécessaire |
|---|---|---|
| Positionnement | Première/dernière ligne, suivant/précédent, absence de résultat, reprise après ajout/modification | Traces de parcours avec identités de lignes |
| Recherche | Exacte/générique, bornes, doublons, clé composée, direction, arrêt du parcours | Corpus de clés limites et résultats dans le même ordre |
| Tampon courant | Valeurs conservées après recherche infructueuse, remise à zéro, copie d'enregistrement, alias | Valeurs avant/après chaque opération |
| Indicateurs | `HTrouve`, `HEnDehors`, erreurs et remise à zéro | Table de transitions des indicateurs |
| Filtres | Empilement éventuel, activation, compatibilité clé/filtre, effet sur recherches et comptages | Parcours filtrés et non filtrés identiques au référentiel |
| Identité | Identifiants automatiques, identifiants forcés, séquences après import, doublons | Insertion concurrente et reprise après rollback |
| Suppression | Actif/rayé/supprimé, possibilité de réutilisation, renumérotation physique | Scénarios utilisant ces états explicitement |
| Types | Numérique exact, réel, monnaie, date vide/invalide, heure, durée, chaîne et binaire | Valeurs extrêmes et comparaison sans conversions implicites |
| Nullabilité | `NULL`, chaîne vide, valeur par défaut et affectation partielle | Table vérité en lecture/écriture/recherche/SQL |
| Tri | Casse, accents, ponctuation, espaces, Unicode et ordre des doublons | Jeux multilingues et clés composées |
| Verrous | Lecture, écriture, lecture-écriture, attente, timeout, libération et déconnexion | Deux processus concurrents instrumentés |
| Transactions | Connexion concernée, isolation, erreurs intermédiaires, annulation, redémarrage | Pannes injectées avec contrôle après reprise |
| SQL | Paramètres, préparation, résultats modifiables, fonctions embarquées, requêtes sur requêtes | Plans fonctionnels et valeurs de résultat |
| Schéma | Création, contrôle de structure, mise à jour, liaisons, génération | Reconstruction en base vide et mise à niveau depuis N−1 |
| Ressources | Fermeture de requête, destruction de contexte, reconnexion, mémoire | Exécution longue avec mesures de ressources |

La documentation `HLitRecherche` indique que certaines options et gestions de blocage diffèrent entre HFSQL, ODBC, connecteurs et JDBC. Le nouveau produit doit conserver ces distinctions dans une table de capacités plutôt que les masquer. [HLitRecherche](https://doc.pcsoft.fr/fr-FR/?3044050=).

### 3.3. Verrous et transactions : un blocage majeur possible

**Fait utile :** le modèle de verrous PostgreSQL ne transforme pas automatiquement un verrou d'écriture de ligne en interdiction de toute lecture ordinaire. Sa documentation distingue les verrous de table et de ligne, leurs conflits et les lectures MVCC. Un comportement historique bloquant les lectures peut donc demander une couche coopérative supplémentaire, ou conserver HFSQL. [Verrouillage explicite PostgreSQL](https://www.postgresql.org/docs/18/explicit-locking.html).

**Recommandation :** sélectionner un profil parmi `native-compatible`, `emulated-compatible` et `unsupported`. Un verrou coopératif n'est valide que si tous les clients passent par le même protocole ; un outil SQL externe peut contourner cette convention. Le rapport doit le signaler. Pour les conflits, définir l'ordre d'acquisition, les délais, la politique d'annulation et le nombre maximal de reprises. Ne jamais réessayer automatiquement un bloc métier ayant déjà envoyé un email ou appelé un paiement.

Chaque transaction doit avoir un propriétaire, une connexion et un identifiant de corrélation. L'IDE doit montrer les écritures incluses, les effets externes exclus et les risques de transaction longue pendant une interaction utilisateur. Les sauvegardes de transactions interrompues et la restitution des messages métier doivent être testées en arrêtant volontairement client, serveur et réseau dans un environnement jetable.

### 3.4. Schéma, SQL, triggers et exploitation

`HModifieStructure` fournit une modification automatique de la structure HFSQL, avec certaines possibilités à chaud en C/S ; sa documentation précise que les liaisons ne sont pas mises à jour par cette fonction. La nouvelle solution doit donc modéliser séparément colonnes, index et liaisons. [HModifieStructure](https://doc.windev.com/en-US/?1000019439=).

**Proposition :** générer une migration de schéma lisible, annoncer son verrouillage prévu et sa réversibilité, puis l'exécuter avec sauvegarde et journal. Une suppression de colonne ne doit pas être automatiquement présentée comme réversible ; conserver temporairement les anciennes données ou créer une migration de compensation. Comparer le schéma attendu au schéma observé avant chaque déploiement.

Il faut inventorier les requêtes définies dans l'éditeur et celles construites dynamiquement. Les requêtes HFSQL peuvent inclure des fonctions WLangage : une réécriture SQL vers PostgreSQL doit soit évaluer une fonction déterministe dans une stratégie explicitement définie, soit la traduire avec preuve, soit refuser la construction. Aspirer toute la table dans le client pour appliquer une fonction est une dégradation à diagnostiquer. [ExécuteRequêteSQL](https://doc.pcsoft.fr/fr-fr/?1000024948=).

Pour chaque trigger et procédure stockée, relever : moteur d'exécution, événement, ordre, paramètres, droits effectifs, dépendances, erreurs et transaction. Les triggers applicatifs exécutés par le client ne doivent pas être confondus avec des triggers serveur. Les vues SQL constituent encore un autre objet : dans HFSQL, la documentation décrit notamment des droits liés au créateur de la vue. Une reprise doit empêcher qu'une vue change silencieusement de niveau de privilège. [Vues SQL HFSQL](https://doc.pcsoft.fr/fr-FR/?9000157=).

L'exploitation couvre réindexation, contrôle des mémos, statistiques, surveillance des connexions, tâches planifiées, sauvegarde complète/incrémentale selon le moteur, restauration, réplication, bascule et réparation. Le type `hPlanification` documente des planifications pour optimisation, sauvegarde et réplication ; leur existence doit être recherchée dans les projets et dans la configuration serveur, pas seulement dans le code. [hPlanification](https://doc.pcsoft.fr/fr-FR/?1000018853=).

## 4. Garder HFSQL : voies d'intégration réalistes

| Voie | Avantage | Limite et travail requis |
|---|---|---|
| ODBC officiel depuis le runtime | Interface externe documentée, lecture/écriture, intégration avec de nombreux langages | SQL et pilote à qualifier ; recréer l'état des fonctions `H*` ; architecture et distribution à vérifier |
| OLE DB officiel sous Windows | Autre interface externe documentée | Dépendance Windows et fournisseur ; ne constitue pas une API universelle multiplateforme |
| Pont métier compilé avec l'environnement d'origine | Peut conserver des traitements et comportements difficiles à réimplémenter | Dépendance PC SOFT maintenue ; contrat de service, packaging, licences et disponibilité |
| API applicative existante REST/SOAP | Sépare proprement les modules lorsque cette API existe déjà | Ne fournit que les opérations exposées ; latence, erreurs et transactions distribuées |
| Lecture des fichiers avec un moteur réécrit | Indépendance potentielle à long terme | Risque élevé de corruption, format non garanti, coût de qualification et examen juridique |

Le fournisseur OLE DB HFSQL est documenté en lecture et écriture depuis un logiciel externe. Cette possibilité ne prouve pas que chaque fonction WLangage peut être remplacée par une requête OLE DB équivalente. La page consultée est historique et renvoie vers une édition ultérieure : vérifier le package disponible avant de choisir cette voie. [Provider OLE DB HFSQL](https://doc.pcsoft.fr/?9000059=&name=provider_ole_pour_hfsql&verdisp=180).

**Choix proposé pour le premier prototype :** ODBC officiel pour un sous-ensemble précisément défini ; pont applicatif pour les transactions métier ou primitives sans équivalence qualifiée. Les appels ne doivent pas être cachés derrière une façade prétendant tout supporter. Une capacité manquante produit un diagnostic au build si elle est statiquement détectable, puis une erreur explicite à l'exécution si elle résulte d'un appel dynamique.

Pour le pont, préférer des opérations métier transactionnelles telles que `valider_commande` à une succession de milliers d'appels réseau `HLitSuivant`. Si une API bas niveau de compatibilité reste nécessaire, introduire des lots et des contextes bornés avec expiration, annulation, contrôle d'identité et fermeture explicite. Un contexte serveur ne doit pas porter une transaction ouverte indéfiniment. Versionner les messages et conserver des identifiants d'idempotence pour les opérations qui peuvent être rejouées.

Les composants redistribuables, versions de pilotes, plateformes Linux et modalités d'installation doivent être vérifiés sur les packages réellement disponibles. La documentation Windows renvoie à un pilote Linux ; cette recherche n'a pas établi une matrice binaire complète, par architecture et version, pour tous les environnements. Il reste nécessaire de tester le téléchargement, l'installation et les clauses de redistribution applicables. [Pilote ODBC HFSQL](https://doc.pcsoft.fr/fr-FR/?3044179=).

## 5. Migrer HFSQL vers PostgreSQL sans perte silencieuse

### 5.1. Conversion et preuve

**Protocole proposé :**

La cible est l'absence de **perte supplémentaire par rapport au type et au profil source**, pas l'exactitude mathématique illimitée. Préserver aussi les arrondis, troncatures, débordements et conversions observables du programme d'origine. Un `numeric(p,s)` ou le `decimal` d'un backend ne peut être choisi qu'après qualification de sa capacité et de ses opérations ; la valeur stockée et le résultat d'un calcul sont deux contrats distincts.

1. Décrire les règles de correspondance : `numeric(p,s)` pour les valeurs exactes ; texte avec longueur validée si elle est significative ; `bytea` ou stockage externe contrôlé pour les mémos ; politique explicite pour les dates sans valeur et les dates invalides.
2. Créer le schéma et les contraintes cibles. Conserver une clé source durable ; ne pas utiliser un numéro physique d'enregistrement comme clé métier sans vérifier sa stabilité.
3. Charger une photographie cohérente. Pour chaque lot, journaliser identifiant, bornes, nombre attendu, nombre chargé, somme de contrôle et état. Rendre la reprise idempotente.
4. Comparer l'ensemble des données : nombre de lignes par table et état, clés distinctes, doublons, orphelins, valeurs `NULL`, extrêmes, sommes monétaires exactes, longueurs et empreintes binaires des mémos.
5. Comparer les résultats métier : encours client, stocks, taxes, arrondis par ligne et total, ancienneté des créances, factures et clôtures.
6. Rejouer les parcours WLangage et requêtes réelles sur les deux moteurs en observant ordre, erreurs et effets. Une différence de tri suffit à changer la sélection d'un premier résultat.
7. Approuver les écarts documentés, puis réaliser une répétition complète de la bascule avec les mêmes volumes et contraintes que la production.

Les collations PostgreSQL peuvent dépendre d'un fournisseur et de paramètres de langue ; il ne suffit pas de choisir « français » pour garantir les règles de comparaison HFSQL. Enregistrer les versions de collation et conserver un corpus d'accents, espaces, ligatures et normalisations Unicode. [Collations PostgreSQL](https://www.postgresql.org/docs/18/collation.html).

Une preuve chiffrée doit exprimer des résultats, par exemple « 2 400 000 lignes attendues, 2 400 000 chargées, 0 clé absente, 0 mémo d'empreinte différente ». Ces nombres sont un **exemple de format**, pas des mesures réalisées. Les données de validation peuvent être anonymisées, mais leurs distributions, contraintes et cas extrêmes doivent rester représentatifs.

### 5.2. Synchronisation, autorité des écritures et retour arrière

La stratégie la plus simple à prouver est une fenêtre de gel : arrêter les écritures, terminer le transfert final, vérifier, puis changer l'autorité. Pour une disponibilité accrue, étudier un journal de changements fiable ou une outbox transactionnelle implantée dans le système source avec les garanties réellement disponibles. Ne pas annoncer une capture universelle du journal HFSQL sans interface et format validés.

**Interdiction de conception proposée :** deux écritures indépendantes `HFSQL` puis `PostgreSQL` ne constituent pas une transaction atomique. Une panne entre les deux crée une divergence. Choisir un seul système autoritaire à chaque instant, et un protocole de propagation idempotent avec ordre, détection de retard et file d'erreurs. Les événements externes doivent porter une clé de déduplication.

La réplication logique PostgreSQL est une fonctionnalité PostgreSQL et ne transforme pas HFSQL en publication PostgreSQL. De plus, sa documentation mentionne des restrictions telles que l'absence de réplication du schéma et des séquences. Le plan doit traiter ces objets séparément. [Réplication logique PostgreSQL](https://www.postgresql.org/docs/18/logical-replication.html), [restrictions](https://www.postgresql.org/docs/18/logical-replication-restrictions.html).

**Retour arrière proposé :** avant la première écriture métier autoritative sur la cible après bascule, et en l'absence d'effet externe à compenser, revenir vers la source peut consister à rétablir l'ancien routage après contrôle de son état et de son schéma. Le chargement initial de la cible n'est pas une écriture métier autoritative. Après des écritures métier sur PostgreSQL, il faut soit une réplication inverse déjà testée, soit exporter et réconcilier ces changements, soit restaurer et accepter une perte explicitement décidée. Une simple restauration d'HFSQL ferait perdre les opérations créées depuis la bascule. Fixer avant la mise en production les objectifs de perte maximale de données et de délai de reprise, puis les mesurer lors d'un exercice.

## 6. Plateformes : compatibilité déclarée par profil

Le tableau suivant présente une **politique de produit recommandée**, et non une promesse que PC SOFT ou le futur runtime possède toutes les capacités de chaque ligne. Chaque capacité doit être identifiée par `version-source × runtime × OS × architecture × type-d'exécution`.

| Cible | Fait documenté utile | Politique proposée et qualification |
|---|---|---|
| Windows bureau | L'écosystème expose des applications Windows et des intégrations Windows | Première cible de fidélité des applications de gestion ; DPI, clavier, dialogues, COM et impression |
| Linux bureau/service | Des cibles Linux apparaissent dans la documentation et certaines capacités évoluent par version | Profil séparé ; distributions, bibliothèques, affichage, polices, impression et démon |
| JVM/Java | WINDEV peut générer des fenêtres et fonctions WLangage en Java, avec restrictions | Ne pas choisir Java comme preuve automatique de fidélité complète |
| macOS | Le catalogue distingue notamment Java et Mac Catalyst selon les fonctions | Inventorier l'origine réelle ; ne pas assimiler Catalyst à toute application Windows |
| Web serveur | WEBDEV documente modes Session et AWP, et déploiement de sites/services | Runtime serveur propre, isolation des sessions, identité, stockage et montée en charge |
| Web navigateur | Code navigateur distinct du code serveur | Backend JavaScript ciblé ; messages asynchrones, sécurité DOM, limites du navigateur |
| PHP | Cible explicitement distinguée dans le catalogue WEBDEV | Maintien seulement si requis par un patrimoine réel et après audit de ses limites |
| Android | Génération et déploiement WINDEV Mobile documentés | Backend mobile qualifié, versions SDK, cycle de vie, permissions et packaging |
| iOS/iPadOS | Déploiement Apple avec certificats/profils et compilation Xcode documenté | Chaîne Mac/Xcode nécessaire à qualifier, signature, sandbox et publication |
| Widgets/montres/Catalyst | Entrées de cible visibles sur certaines fonctions | Lots spécifiques selon demande et corpus ; aucun support implicite |
| Batch/service/conteneur | Des traitements sans interface existent, notamment WDScript | Runtime headless et CLI ; pas de dépendance à une session graphique |

Les différences ne sont pas théoriques : la documentation Java mentionne des fonctionnalités non disponibles, dont les états, certaines formes d'indirection et la compilation dynamique. Les impressions directes WLangage disponibles ne remplacent pas l'éditeur et le moteur d'états. [Fonctionnalités et limites Java](https://doc.windev.com/en-US/?9000056=). La documentation distingue aussi des comportements de génération et d'exécution par cible ; l'ancien mécanisme de code conditionnel a été remplacé à partir de la version 25 par d'autres constructions. L'importeur doit donc respecter les variantes réelles du code source. [Code conditionnel par cible](https://doc.windev.com/en-US/?9000033=).

### 6.1. Web : reprendre le cycle d'exécution

Un code serveur qui remplit une table avant rendu et un clic navigateur ne partagent pas nécessairement le même état ni la même transaction. Pour chaque événement importé, conserver sa localisation serveur/navigateur, ses paramètres, l'usage d'AJAX, les règles de validation et l'ordre d'initialisation. Définir les comportements du bouton retour, des URL, du rafraîchissement, des onglets multiples et de la session expirée.

Le mode AWP possède sa propre gestion du contexte. `DéclareContexteAWP` décrit une persistance des variables entre affichages avec des modes configurables. Une conversion systématique en session serveur changerait les propriétés de montée en charge, de confidentialité et de partage entre onglets. [DéclareContexteAWP](https://doc.pcsoft.fr/?3058028=).

Le déploiement WEBDEV documenté repose sur un serveur web, un serveur d'application et un compte de déploiement, avec des étapes de synchronisation des données. Un nouveau moteur peut proposer son propre hébergement, mais il doit fournir l'équivalent opérationnel : configuration des secrets, uploads, fichiers persistants, tâches, logs, sauvegarde, cluster et reprise. [Déploiement WEBDEV](https://doc.pcsoft.fr/?2028019=). WDDeploy offre déjà des packages et un mode de commande ; l'amélioration proposée doit porter sur des garanties concrètes supplémentaires plutôt que prétendre inventer le déploiement automatisé. [WDDeploy](https://doc.pcsoft.fr/?3533002=).

### 6.2. Mobile : l'équivalence inclut le système et le hors ligne

Un plugin mobile doit fournir : capteurs, permission, état autorisé/refusé/révoqué, arrivée en arrière-plan, suspension, reprise et indisponibilité matérielle. Il doit permettre aux tests de simuler ces états. Sur Android, les permissions sensibles se demandent à l'exécution et peuvent être refusées ; un ancien code qui supposait l'accès permanent nécessite un traitement explicite. [Permissions Android](https://developer.android.com/training/permissions/requesting).

Pour le hors ligne, fixer le schéma local, chiffrement, quotas, synchronisation des suppressions, identité des opérations, résolution des conflits, reprise des pièces jointes et protection des identifiants. La présence de HFSQL ou SQLite sur le terminal ne résout pas les conflits métier. Prévoir des cas de double modification, changement d'heure, plusieurs jours sans réseau, réinstallation, restauration d'une sauvegarde et appareil perdu.

Les versions de SDK et règles de publication changent ; elles doivent être épinglées et contrôlées dans la chaîne de build. L'historique PC SOFT montre des adaptations du niveau API Android selon les versions de WINDEV Mobile. [Spécificités Android](https://doc.pcsoft.fr/en-US/?9000108=). Pour iOS, la génération doit prévoir les étapes de certificats, profils et Xcode, sans confondre simulateur et distribution. [Déploiement In-House PC SOFT](https://doc.windev.com/en-US/?1000019926=).

## 7. Inventaire des intégrations à intégrer au plan de compatibilité

Les lignes suivantes sont un **périmètre d'audit et de conception**. Elles ne déclarent pas chaque API existante disponible sur chaque cible. Pour chaque appel réellement rencontré : nom et surcharges, constantes, type retourné, erreurs, cible, version, dépendance, licence, mode synchrone/asynchrone et test de référence doivent être consignés.

| Famille | Couverture à rechercher | Stratégie et point de vigilance |
|---|---|---|
| Bases SQL | PostgreSQL, SQL Server/Azure SQL, Oracle, MySQL/MariaDB, DB2, Informix, AS/400, Progress, Sybase, SQLite | Adaptateurs distincts, dialecte et types ; pas de connecteur unique miraculeux |
| Bases et formats historiques | xBase, Access, Excel source de données, XML, fichiers délimités, sources ODBC/OLE DB/JDBC | Encodages, verrous, types inférés et identifiants |
| Données non relationnelles | Documents JSON/XML, MongoDB ou autres moteurs réellement utilisés | Inventorier les extensions ; pas de traduction implicite vers SQL |
| HTTP et API | HTTP/HTTPS, REST, verbes, en-têtes, cookies, streaming, multipart, upload/download, proxy | Timeout, annulation, certificats, redirection et taille maximale |
| SOAP | WSDL, types XML, tableaux, erreurs SOAP, authentification, pièces jointes | Générateur de clients et services, compatibilité sérialisation |
| GraphQL | Schéma, requêtes, variables, mutations, pagination et erreurs | Qualifier la version source et le contrat ; préserver réponses partielles |
| Temps réel | Sockets TCP/UDP, WebSocket, serveur et client, TLS | Encadrement des messages, reconnexion et concurrence |
| Réseau métier | MQTT, messageries ou middleware effectivement présents | QoS, ordre, réémission et déduplication |
| Fichiers et transfert | FTP/FTPS/SFTP, SSH/SCP, partages réseau, disque, archives ZIP | Permissions, chemins Windows/Linux, flux binaires et reprise |
| Email | SMTP, POP, IMAP, MIME, pièces jointes, OAuth, calendriers | Encodage, jetons, limites du fournisseur et déduplication |
| Identité | OAuth 2, OpenID Connect, annuaires/LDAP, SSO, certificats client | Règles de session et renouvellement ; séparer authentification et autorisation |
| Cloud et drives | Stockage objet, Dropbox, Google Drive, OneDrive, API d'entreprise utilisées | Adaptateurs versionnés et scopes minimaux, coûts et quotas visibles |
| Cryptographie | Hash, signature, chiffrement, certificats, coffre-fort, carte à puce | Choix explicite d'algorithme et format, compatibilité des octets et rotation |
| Windows natif | DLL, API Win32, COM/OLE, ActiveX, WPF/.NET, registre, services, planificateur | Plugin Windows isolé ; passage 32/64 bits et ABI |
| .NET et Java | Assemblies, composants externes, JVM, bibliothèques natives, callbacks | Cycle de vie, exceptions, types, threading et packaging |
| Langages embarqués | JavaScript, Python, Java/C selon les appels présents | Exécution isolée et dépendances déclarées ; ne pas assimiler code texte à support automatique |
| Office | Automatisation Word/Excel/Outlook, lecture/écriture de documents et tableurs | Distinguer formats ouverts et automatisation nécessitant Office installé |
| PDF/documents | Création, lecture, fusion, extraction, formulaires, pièces jointes, signatures, PDF/A | Polices, précision de rendu, validation et dépendances sous licence |
| Données métier documentaires | Factur-X/UBL, XML/EDI, codes fiscaux ou santé réellement utilisés | Valider schémas, signatures et versions normatives ; pas de conformité implicite |
| Impression | Pilotes système, PDF, étiquettes, tickets, PCL/ESC/POS, recto-verso, bacs | Périphériques réels et paramètres persistants |
| Capture | Scanner/TWAIN/WIA, caméra, OCR, lecture code-barres et QR | Qualité, permissions, SDK fabricants, matériels de test |
| Image/audio/vidéo | Chargement, dessin, EXIF, formats, codecs, capture, lecture et enregistrement | Licences de codecs, orientation, accélération et mémoire |
| Cartes/localisation | GPS, géocodage, itinéraires, cartes et tuiles, zones | Clés fournisseur, réseau, cache hors ligne et conditions d'utilisation |
| Mobile téléphonie | Appels, SMS, contacts, agenda, partage, liens profonds | Capacités fortement conditionnées par OS et permissions |
| Mobile notification | Notifications locales/push, APNs/FCM, badges, actions | Gestion des jetons, consentement et réinstallation |
| Bluetooth/NFC | Bluetooth classique, BLE/GATT, beacons, tags NFC | Matériel et OS précis ; services, MTU, reconnexion et arrière-plan |
| Industrie et périphériques | Ports série, USB/HID, balances, lecteurs, imprimantes, terminaux spécifiques | ABI, pilotes fabricant, chronologie et indisponibilité |
| IoT et capteurs | Accéléromètre, gyroscope, orientation, capteurs embarqués, appareils connectés | Fréquence, unité, batterie et simulation |
| Paiement et signature | Terminal, passerelle, tokenisation, signature électronique | Ne pas rejouer automatiquement ; journal métier et conformité du prestataire |
| IA | Appels de modèles, streaming, embeddings, outils, traitement local éventuel | Choix du fournisseur, confidentialité, coûts et tests reproductibles |
| Administration | Exécution de processus, shell, SSH, logs, supervision, tâches | Droits, isolation, annulation et audit |

L'existence de capacités BLE dans l'écosystème est documentée, avec différences par plateforme ; cela illustre le besoin d'une matrice par cible au lieu d'une simple case « Bluetooth ». [Gestion Bluetooth LE](https://doc.windev.com/en-US/?1000022226=).

## 8. États, impressions et personnalisation utilisateur

### 8.1. Traiter le reporting comme un moteur distinct

**Proposition :** construire un modèle d'état indépendant du moteur d'interface, comprenant source de données, tri, ruptures, en-têtes/pieds, corps, blocs conditionnels, itérations, sous-états, calculs, champs, images et événements. L'état doit produire une représentation intermédiaire de pages avant export et impression. Les retours des procédures appelées pendant la génération doivent être observables dans les tests.

Le périmètre de fidélité inclut : marges, unités, mesure du texte, polices embarquées ou substituées, sauts de page, rupture en fin de page, répétition d'en-têtes, veuves/orphelines, numérotation, total en pied, impression en plusieurs passes, recto-verso, étiquettes, codes-barres et documents multilingues. Les blocs d'itération sont une construction documentée de l'éditeur d'états et doivent apparaître dans l'importeur. [Bloc Itération](https://doc.pcsoft.fr/?1011039=).

**Tests proposés :** comparer d'abord texte, montants, ordre, nombre de pages et positions des zones métier ; comparer ensuite les images avec seuils maîtrisés pour l'anticrénelage. Une comparaison d'image seule ne démontre ni le bon contenu caché, ni la validité d'une signature, ni la conformité PDF/A. Qualifier des impressions réelles sur plusieurs pilotes et formats, notamment ticket et étiquette. Les bacs, l'agrafage et le recto-verso ne sont pas reproduits par un simple export HTML.

L'aperçu doit conserver recherche, zoom, navigation, export, impression partielle et actions autorisées. Les états et requêtes créés par les utilisateurs finaux constituent des données applicatives : ils doivent être inventoriés, migrés et protégés avec leurs droits, pas remplacés silencieusement par les seuls états du projet.

### 8.2. États & Requêtes, FAA et documents produits par les utilisateurs

PC SOFT permet d'intégrer le logiciel États & Requêtes à une installation et distingue des répertoires personnels et partagés. Cela établit que la personnalisation continue après le déploiement et qu'un inventaire uniquement Git peut être incomplet. [Modules complémentaires d'installation](https://doc.pcsoft.fr/?2028045=).

**Recommandation :** importer ces variantes dans un espace utilisateur versionné, avec aperçu des changements, validation et retour à une version précédente. Pour les FAA liées à l'impression ou aux tables, reprendre les actions utilisées : export de table, copie, recherche, tri, filtres, choix des colonnes et mémorisation. Tester leurs restrictions : une colonne masquée par commodité ne doit pas devenir une colonne accessible malgré une interdiction métier.

Séparer l'export fidèle d'un état et l'export structuré des données : le premier privilégie la mise en page ; le second des types et cellules exploitables. Conserver les droits sur les fichiers générés, la purge des temporaires, le téléchargement authentifié et les noms de fichiers sûrs. Les fichiers de production ne doivent pas aboutir dans un répertoire public pour simplifier l'aperçu web.

## 9. Conditions de sortie et inconnues à lever

| Lot | Condition de sortie proposée |
|---|---|
| HFSQL conservé | Installation reproductible du connecteur et licence validée ; transactions, parcours et erreurs du corpus conformes |
| PostgreSQL | 100 % des contrôles de données approuvés ; écarts sémantiques connus et acceptés ; bascule et retour arrière exercés |
| Web | Tests de sessions, onglets, AJAX, expirations, droits et isolation réussis ; restauration de déploiement démontrée |
| Mobile | Appareils et versions OS représentatifs ; permissions refusées/révoquées et hors ligne testés ; package signé installable |
| Reporting | Documents métier approuvés, totaux exacts, pagination acceptée et imprimantes critiques testées |
| Intégrations | Propriétaire, contrat, version, secret, dépendance et scénario de panne pour chaque intégration du projet |

Les inconnues bloquantes sont : disponibilité exacte des sources et analyses, version PC SOFT et options, fichiers réellement ouverts, fonctions dynamiques, formats d'états exportables, composants externes sans source, pilotes et droits de distribution, capacité de capture des modifications HFSQL, exigences de verrouillage, plateformes souhaitées et parc d'imprimantes. Il faut obtenir ces réponses par un audit d'un échantillon représentatif. Cette recherche établit les voies possibles et les protocoles de décision ; elle ne peut garantir une migration sans modification pour tous les patrimoines.

## Sources primaires consultées

Les liens proches du texte constituent les références précises. Plusieurs pages sont indexées sur des éditions antérieures ; leur présence ne prouve pas une disponibilité uniforme en 2026. Les faits utilisés sont limités aux éléments décrits, et toute recommandation d'architecture reste une proposition de cette étude.

1. [Pilote ODBC HFSQL Windows](https://doc.pcsoft.fr/fr-FR/?3044179=).
2. [Provider OLE DB HFSQL, page historique](https://doc.pcsoft.fr/?9000059=&name=provider_ole_pour_hfsql&verdisp=180).
3. [HOuvreConnexion et connecteurs](https://help.windev.com/en-US/?3044107=).
4. [Déploiement d'application Android, fichiers HFSQL](https://doc.pcsoft.fr/en-us/?1410087576=&name=deploying_android_application).
5. [Génération des scripts SQL depuis une analyse](https://doc.windev.com/en-US/?2011027=&name=Generer_Scripts_SQL).
6. [Gestion des fichiers HFSQL C/S](https://doc.pcsoft.fr/?35400016=).
7. [HAjoute](https://doc.pcsoft.fr/?3044147=).
8. [HNbEnr](https://doc.pcsoft.fr/fr-FR/?3044006=).
9. [HLitRecherche](https://doc.pcsoft.fr/fr-FR/?3044050=).
10. [HModifieStructure](https://doc.windev.com/en-US/?1000019439=).
11. [ExécuteRequêteSQL](https://doc.pcsoft.fr/fr-fr/?1000024948=).
12. [Vues SQL HFSQL](https://doc.pcsoft.fr/fr-FR/?9000157=).
13. [hPlanification](https://doc.pcsoft.fr/fr-FR/?1000018853=).
14. [Fonctionnalités et limites Java](https://doc.windev.com/en-US/?9000056=).
15. [Code conditionnel par cible](https://doc.windev.com/en-US/?9000033=).
16. [DéclareContexteAWP](https://doc.pcsoft.fr/?3058028=).
17. [Déploiement WEBDEV](https://doc.pcsoft.fr/?2028019=).
18. [WDDeploy et packages de déploiement](https://doc.pcsoft.fr/?3533002=).
19. [Spécificités Android](https://doc.pcsoft.fr/en-US/?9000108=).
20. [Déploiement In-House iOS](https://doc.windev.com/en-US/?1000019926=).
21. [Bluetooth LE](https://doc.windev.com/en-US/?1000022226=).
22. [Bloc d'itération d'un état](https://doc.pcsoft.fr/?1011039=).
23. [Modules complémentaires et États & Requêtes](https://doc.pcsoft.fr/?2028045=).
24. [Verrous PostgreSQL 18](https://www.postgresql.org/docs/18/explicit-locking.html).
25. [Collations PostgreSQL 18](https://www.postgresql.org/docs/18/collation.html).
26. [Réplication logique PostgreSQL 18](https://www.postgresql.org/docs/18/logical-replication.html).
27. [Restrictions de réplication logique](https://www.postgresql.org/docs/18/logical-replication-restrictions.html).
28. [Permissions à l'exécution Android](https://developer.android.com/training/permissions/requesting).
