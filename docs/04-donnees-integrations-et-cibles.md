# Données, intégrations, impressions et plateformes

Date de recherche : **26 octobre 2026**. Ce chapitre distingue les comportements documentés de PC SOFT, les décisions proposées pour le nouveau produit et les points à vérifier sur de véritables projets. Aucun accès à une installation WINDEV, à un serveur HFSQL, à un projet client ou à une imprimante n'a été fourni : les architectures et critères ci-dessous sont des spécifications, pas des compatibilités déjà démontrées.

## 1. Contrainte ferme : aucune DLL ni aucun outil PC SOFT

**La chaîne entière doit être indépendante de PC SOFT : import, construction, exécution, tests, exploitation et support.** Sont exclus les DLL/frameworks PC SOFT, HFSQL comme moteur ou serveur, les pilotes HFSQL ODBC/OLE DB, les connecteurs PC SOFT, les ponts compilés WINDEV/WEBDEV, WDSQL, les convertisseurs et les exécutables de référence PC SOFT. Les faire exécuter chez le client ou derrière une API dans notre protocole ne respecte pas cette contrainte.

**La cible demandée est multi-moteurs sur base C# : PostgreSQL et SQLite au premier gate réel**, puis SQL Server ; MariaDB, MySQL, Oracle et les autres besoins sont qualifiés séparément. Pilotes et runtime sont indépendants, soumis à admission par version/acte. Les développements PostgreSQL ci-dessous restent un cas principal, et ne suffisent pas à prouver SQLite ou un autre fournisseur. Le [plan détaillé](16-plan-detaille-de-realisation.md) et l’[architecture multi-BDD](18-architecture-csharp-multi-bdd-et-reemploi.md) définissent les extensions. Les appels `H*` des sources métier sont interprétés ou compilés par notre implémentation originale et exécutés par notre adaptateur. Ce ne sont pas des appels à HFSQL cachés derrière une façade SQL.

Le code métier peut rester du WLangage. Cette continuité du langage ne prouve pas la fidélité de tous ses comportements. Les sources lisibles, métadonnées, données et schémas déjà fournis constituent les entrées ; les formats opaques sans lecteur indépendant qualifié constituent des blocages. Le protocole ne demande pas une extraction ou une conversion avec un outil PC SOFT, même par un tiers. Le [protocole de recette](10-protocole-pilote-et-recette.md) précise les preuves acceptables.

### 1.1. Chemins retenus et alternatives exclues

| Chemin | Statut | Conditions et limites |
|---|---|---|
| WLangage métier conservé, compilateur/runtime originaux, PostgreSQL | Prioritaire à développer | Import lisible, contrat `H*` caractérisé, bibliothèque indépendante et résultats qualifiés |
| Autre stockage SQL indépendant | Possible selon le projet | Adaptateur distinct, mêmes contrôles et aucune dépendance PC SOFT transitive |
| Modernisation explicite des accès métier | Possible avec adaptations déclarées | Réécriture identifiée et acceptée ; la mesurer séparément de la conservation des sources |
| HFSQL, pilote PC SOFT, pont WINDEV ou API exigeant un moteur PC SOFT | Exclu | Comparatif historique uniquement, jamais étape temporaire de notre plan |
| Exécution d'un oracle WINDEV, même côté client | Exclu | Comparaison limitée aux résultats déjà fournis et licites ou à une spécification indépendante |

Les documentations décrivent des accès tiers à HFSQL et des connecteurs PostgreSQL PC SOFT ; ces faits historiques ne sont pas des solutions retenues. Leurs possibilités et licences ne créent aucune exception à la contrainte. [HOuvreConnexion](https://help.windev.com/en-US/?3044107=), [pilote ODBC HFSQL](https://doc.pcsoft.fr/fr-FR/?3044179=).

La page officielle des sessions associe notamment application, machine, compte système et type de base, avec activation renouvelée ; PostgreSQL accompagné du runtime PC SOFT ne suffirait donc pas à démontrer une sortie de dépendance. Cette configuration est ici exclue et aucun prix n'est déduit de cette page. [Définition des sessions](https://windev.com/fr/sessions).

### 1.2. Matrice de fermeture des dépendances

| Dimension | Exigence de la cible | Preuve attendue |
|---|---|---|
| Code métier et actifs | Sources et ressources déjà fournies, provenance établie | Inventaire, droits, empreintes ; composants opaques bloquants |
| Langage et compilation | Compilateur indépendant et format ouvert ; aucun compilateur PC SOFT | Build sur poste vierge et nomenclature des outils |
| Runtime distribué | Aucun framework/DLL PC SOFT direct ou transitif | Inventaire des binaires, bibliothèques chargées et appels externes |
| Serveur de données | PostgreSQL et SQLite initiaux, autres moteurs indépendants par qualification | Services et connexions recensés ; absence de serveur HFSQL |
| Pilote et connexion | Pilote non PC SOFT qualifié | Provenance, licence et dépendances transitives |
| Sessions applicatives | État géré par le runtime cible | Scénarios sans serveur WEBDEV ni pont PC SOFT |
| Import et qualification | Lecteurs indépendants et références déjà fournies | Journal des outils utilisés ; aucune exécution d'oracle propriétaire |
| Contrats et facturation | Obligations des composants réellement choisis recensées | Revue des licences et actifs ; pas de promesse générale d'absence de risque |

Les SDK tiers non PC SOFT restent possibles : bibliothèque PostgreSQL, SDK système, moteur PDF ou pilote matériel, sous réserve de provenance, licence et qualification. L'indépendance technique ne décide pas à elle seule des droits attachés aux sources, ressources et contrats antérieurs ; voir le [dossier juridique](09-propriete-intellectuelle-et-licences.md).

### 1.3. Jalons de décision

1. Vérifier que le paquet déjà fourni permet l'import indépendant ; bloquer les éléments manquants ou opaques.
2. Décrire le profil sémantique par documentation et preuves disponibles, en conservant les inconnues.
3. Qualifier l'adaptateur PostgreSQL et le runtime sur fixtures licites et spécifications indépendantes.
4. Construire, installer, tester et mettre à jour sur une machine dépourvue de composants PC SOFT.
5. Répéter l'import des données et la reprise de la cible indépendante ; ne pas promettre un retour à l'ancien produit.

## 2. Contrat d'entrée : sources, données et schéma déjà disponibles

### 2.1. Paquet accepté par l'importeur indépendant

Une reprise rapproche les descriptions lisibles déjà fournies, le code métier et les données disponibles. Le modèle interne conserve noms logiques et physiques, alias, types et tailles, précision/échelle, encodage, valeurs par défaut, nullabilité, clés simples/composées, règles de tri, unicité, intégrité et index spécialisés. La provenance de chaque propriété doit rester visible.

| Entrée déjà fournie | Traitement indépendant | Limite |
|---|---|---|
| Sources WLangage textuelles et fichiers de projet lisibles | Parseur original, inventaire et préservation des sections inconnues | Le texte hybride ne garantit pas que toutes les propriétés sont exposées |
| Schéma SQL, JSON ou description textuelle documentée | Normalisation, validation et correspondance vers PostgreSQL | Identifier les types et contraintes manquants sans les inventer |
| Données CSV/JSON/SQL ou autre format ouvert décrit | Lecteur indépendant, conversion contrôlée et chargement idempotent | Conserver types, `NULL`, encodage, précision et intégrité des mémos |
| Documents, captures, traces et résultats préexistants licites | Références datées et immuables pour cas comparables | Preuve partielle, sans exécution nouvelle du produit d'origine |
| Fichiers natifs opaques | Inventaire statique, taille, empreinte et dépendances | Aucune ouverture par DLL/outillage PC SOFT ; lecture bloquée sans lecteur indépendant qualifié |

Les fichiers usuels HFSQL comprennent `.fic`, `.ndx` et `.mmo` ; le schéma peut dépendre d'autres métadonnées. La présence de ces fichiers ne constitue donc pas un export logique exploitable. **Si seuls ces fichiers opaques sont disponibles, la migration des données est bloquée** jusqu'à disponibilité d'une entrée déjà fournie exploitable ou qualification d'un lecteur entièrement indépendant. Aucun lecteur de ce type n'est livré ni démontré par cette étude. [Extensions présentées dans le déploiement Android](https://doc.pcsoft.fr/en-us/?1410087576=&name=deploying_android_application).

### 2.2. Procédure indépendante proposée

1. Conserver les originaux reçus et leurs empreintes ; ne charger aucun exécutable, DLL ou pilote accompagnant le paquet.
2. Recenser les versions et options à partir des métadonnées déjà fournies ; maintenir tout réglage inconnu comme bloquant pour le comportement concerné.
3. Importer le schéma lisible et vérifier sa cohérence avec les données et les accès du code ; aucune génération via l'éditeur d'analyse n'est prévue.
4. Chercher dans le texte les créations dynamiques, alias, changements de connexion, de nom et de répertoire ; construire le graphe des accès.
5. Définir la correspondance de chaque rubrique et clé avec la cible indépendante, y compris les règles de conversion et les valeurs non représentables.
6. Comparer échantillons puis ensemble reçu : clés, effectifs, contraintes, agrégats et empreintes des mémos. L'intégrité du paquet reçu ne démontre pas qu'il couvre la totalité d'une base historique inaccessible.

L'analyse reste visible dans le nouvel IDE avec fichiers/tables, rubriques, clés, liaisons et connexions, selon ce qui a effectivement été importé. Les propriétés non récupérées restent affichées comme inconnues. La documentation indique qu'un ancien éditeur peut produire du SQL ; c'est une information historique, pas une étape autorisée de ce workflow. [Génération de scripts SQL, contexte historique](https://doc.windev.com/en-US/?2011027=&name=Generer_Scripts_SQL).

### 2.3. Classic et Client/Serveur : deux patrimoines à comprendre, aucun à exécuter

Les anciens projets Classic peuvent dépendre de chemins, fichiers partagés, verrous et accès concurrents. Les projets Client/Serveur peuvent dépendre de droits, traitements stockés, tâches et connexions. Ces informations sont relevées dans le code et les descriptions déjà reçus ; le protocole ne se connecte pas à HFSQL et ne lance pas son Centre de Contrôle. [Fonctions historiques d'administration](https://doc.pcsoft.fr/?35400016=).

Le manifeste décrit ces dépendances comme comportements à réimplémenter ou blocages, jamais comme des adaptateurs HFSQL à activer. Le runtime cible sépare l'accès métier de son administration PostgreSQL et fonctionne sans droits de réparation ou de suppression de bases.

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

**Fait utile :** le modèle de verrous PostgreSQL ne transforme pas automatiquement un verrou d'écriture de ligne en interdiction de toute lecture ordinaire. Sa documentation distingue les verrous de table et de ligne, leurs conflits et les lectures MVCC. Un comportement historique bloquant les lectures peut donc demander une couche coopérative supplémentaire ; sans équivalence qualifiée, le comportement reste bloquant ou fait l'objet d'une adaptation explicitement acceptée. [Verrouillage explicite PostgreSQL](https://www.postgresql.org/docs/18/explicit-locking.html).

**Recommandation :** sélectionner un profil parmi `native-compatible`, `emulated-compatible` et `unsupported`. Un verrou coopératif n'est valide que si tous les clients passent par le même protocole ; un outil SQL externe peut contourner cette convention. Le rapport doit le signaler. Pour les conflits, définir l'ordre d'acquisition, les délais, la politique d'annulation et le nombre maximal de reprises. Ne jamais réessayer automatiquement un bloc métier ayant déjà envoyé un email ou appelé un paiement.

Chaque transaction doit avoir un propriétaire, une connexion et un identifiant de corrélation. L'IDE doit montrer les écritures incluses, les effets externes exclus et les risques de transaction longue pendant une interaction utilisateur. Les sauvegardes de transactions interrompues et la restitution des messages métier doivent être testées en arrêtant volontairement client, serveur et réseau dans un environnement jetable.

### 3.4. Schéma, SQL, triggers et exploitation

`HModifieStructure` fournit une modification automatique de la structure HFSQL, avec certaines possibilités à chaud en C/S ; sa documentation précise que les liaisons ne sont pas mises à jour par cette fonction. La nouvelle solution doit donc modéliser séparément colonnes, index et liaisons. [HModifieStructure](https://doc.windev.com/en-US/?1000019439=).

**Proposition :** générer une migration de schéma lisible, annoncer son verrouillage prévu et sa réversibilité, puis l'exécuter avec sauvegarde et journal. Une suppression de colonne ne doit pas être automatiquement présentée comme réversible ; conserver temporairement les anciennes données ou créer une migration de compensation. Comparer le schéma attendu au schéma observé avant chaque déploiement.

Il faut inventorier les requêtes textuelles déjà fournies et celles construites dynamiquement par le code reçu. Les requêtes HFSQL peuvent inclure des fonctions WLangage : une réécriture SQL vers PostgreSQL doit soit évaluer une fonction déterministe dans une stratégie explicitement définie, soit la traduire avec preuve, soit refuser la construction. Aspirer toute la table dans le client pour appliquer une fonction est une dégradation à diagnostiquer. [ExécuteRequêteSQL](https://doc.pcsoft.fr/fr-fr/?1000024948=).

Pour chaque trigger et procédure stockée, relever : moteur d'exécution, événement, ordre, paramètres, droits effectifs, dépendances, erreurs et transaction. Les triggers applicatifs exécutés par le client ne doivent pas être confondus avec des triggers serveur. Les vues SQL constituent encore un autre objet : dans HFSQL, la documentation décrit notamment des droits liés au créateur de la vue. Une reprise doit empêcher qu'une vue change silencieusement de niveau de privilège. [Vues SQL HFSQL](https://doc.pcsoft.fr/fr-FR/?9000157=).

L'exploitation couvre réindexation, contrôle des mémos, statistiques, surveillance des connexions, tâches planifiées, sauvegarde complète/incrémentale selon le moteur, restauration, réplication, bascule et réparation. Le type `hPlanification` documente des planifications pour optimisation, sauvegarde et réplication ; leur existence doit être recherchée dans les descriptions de projets et de configuration déjà fournies, sans connexion ni outil HFSQL. [hPlanification](https://doc.pcsoft.fr/fr-FR/?1000018853=).

### 3.5. PostgreSQL simplifie le stockage, pas automatiquement le contrat `H*`

Utiliser un moteur SQL existant évite de construire son stockage, son indexation et sa récupération transactionnelle. Cela peut réduire une partie de l'effort, mais préserver les sources `H*` exige encore tampon courant, parcours ordonné, positions sauvegardées, indicateurs, filtres, règles de verrouillage et erreurs. Même sans moteur ISAM physique dédié, l'adaptateur émule les comportements ISAM observables utilisés par le projet. Le coût doit être mesuré, pas considéré comme supprimé.

Une pagination par clé stable peut servir certains parcours ; elle ne prouve pas l'équivalence d'un numéro physique d'enregistrement ou d'un verrou empêchant toute lecture. Pour chaque primitive sans correspondance, choisir une émulation qualifiée, une adaptation du code acceptée ou un blocage explicite. Une nouvelle API orientée SQL peut simplifier les modules nouveaux ; elle constitue une modernisation du contrat applicatif et doit être distinguée de l'exécution inchangée des sources anciennes.

## 4. Alternatives historiques exclues et stratégie indépendante retenue

Les licences WINDEV et du framework comportent des clauses pertinentes pour des outils de développement ; leur analyse reste dans le [chapitre juridique](09-propriete-intellectuelle-et-licences.md). La présente décision est plus stricte : aucune utilisation de ces composants dans la chaîne, même si un usage particulier pouvait être autorisé. [Licence WINDEV](https://doc.pcsoft.fr/?4510001), [licence du framework](https://doc.pcsoft.fr/?1000019581).

| Alternative étudiée historiquement | Décision ferme |
|---|---|
| Pilote HFSQL ODBC ou fournisseur OLE DB PC SOFT | Exclu de l'import, des tests et de l'exécution |
| Serveur ou moteur HFSQL conservé derrière SQL | Exclu ; PostgreSQL doit réellement stocker et traiter les données cibles |
| Pont compilé WINDEV/WEBDEV ou service exposant ces moteurs | Exclu, y compris distant ou exécuté chez le client pour notre workflow |
| WDSQL, convertisseur ou exporteur PC SOFT lancé pour la migration | Exclu ; aucune demande d'exécution à un tiers |
| Oracle WINDEV instrumenté ou application d'origine relancée pour comparaison | Exclu ; seules références préexistantes licites acceptées |
| Lecteur indépendant d'un format natif | Recherche envisageable ; aucune capacité démontrée aujourd'hui, qualification et droits nécessaires |

Le fait qu'ODBC ou OLE DB soient des interfaces documentées ne les rend pas admissibles lorsqu'ils chargent un composant PC SOFT. Une bibliothèque tierce peut être utilisée uniquement si sa chaîne de dépendances respecte aussi l'exclusion. [ODBC HFSQL, comparaison historique](https://doc.pcsoft.fr/fr-FR/?3044179=), [OLE DB HFSQL, comparaison historique](https://doc.pcsoft.fr/?9000059=&name=provider_ole_pour_hfsql&verdisp=180).

**Prototype retenu :** importer un paquet textuel et des données ouvertes déjà fournis, analyser les appels `H*`, exécuter leur implémentation originale sur PostgreSQL et comparer les sorties aux fixtures disponibles. Une capacité sans contrat ou sans référence suffisante reste inconnue ; elle ne déclenche aucun repli vers un moteur PC SOFT. Les erreurs statiquement détectables bloquent la génération concernée et les appels dynamiques inconnus produisent un diagnostic explicite.

## 5. Charger les données reçues dans PostgreSQL sans perte silencieuse

### 5.1. Conversion et preuve

**Protocole proposé :**

La cible est l'absence de **perte supplémentaire par rapport au type et au profil source**, pas l'exactitude mathématique illimitée. Préserver aussi les arrondis, troncatures, débordements et conversions observables du programme d'origine. Un `numeric(p,s)` ou le `decimal` d'un backend ne peut être choisi qu'après qualification de sa capacité et de ses opérations ; la valeur stockée et le résultat d'un calcul sont deux contrats distincts.

1. Décrire les règles de correspondance : `numeric(p,s)` pour les valeurs exactes ; texte avec longueur validée si elle est significative ; `bytea` ou stockage externe contrôlé pour les mémos ; politique explicite pour les dates sans valeur et les dates invalides.
2. Créer le schéma et les contraintes cibles. Conserver une clé source durable ; ne pas utiliser un numéro physique d'enregistrement comme clé métier sans vérifier sa stabilité.
3. Charger une photographie cohérente. Pour chaque lot, journaliser identifiant, bornes, nombre attendu, nombre chargé, somme de contrôle et état. Rendre la reprise idempotente.
4. Comparer l'ensemble des données : nombre de lignes par table et état, clés distinctes, doublons, orphelins, valeurs `NULL`, extrêmes, sommes monétaires exactes, longueurs et empreintes binaires des mémos.
5. Comparer les résultats métier : encours client, stocks, taxes, arrondis par ligne et total, ancienneté des créances, factures et clôtures.
6. Exécuter les parcours WLangage et requêtes importées sur le moteur indépendant et comparer aux résultats déjà fournis, si le profil et les entrées correspondent. Les cas sans référence ne constituent pas une preuve de parité ; une différence de tri peut changer la sélection d'un premier résultat.
7. Approuver les écarts documentés, puis réaliser une répétition complète de la bascule avec les mêmes volumes et contraintes que la production.

Les collations PostgreSQL peuvent dépendre d'un fournisseur et de paramètres de langue ; il ne suffit pas de choisir « français » pour garantir les règles de comparaison HFSQL. Enregistrer les versions de collation et conserver un corpus d'accents, espaces, ligatures et normalisations Unicode. [Collations PostgreSQL](https://www.postgresql.org/docs/18/collation.html).

Une preuve chiffrée doit exprimer des résultats, par exemple « 2 400 000 lignes attendues, 2 400 000 chargées, 0 clé absente, 0 mémo d'empreinte différente ». Ces nombres sont un **exemple de format**, pas des mesures réalisées. Les données de validation peuvent être anonymisées, mais leurs distributions, contraintes et cas extrêmes doivent rester représentatifs.

### 5.2. Fraîcheur du paquet, autorité des écritures et reprise indépendante

Le paquet déjà fourni doit définir une photographie cohérente, sa date, son périmètre et ses éventuels changements incrémentaux dans un format exploitable indépendamment. La présence de fichiers seuls ne prouve ni cohérence transactionnelle ni exhaustivité. Si une migration à chaud exige un journal HFSQL ou une extraction PC SOFT, ce mode est exclu et le passage en production reste bloqué faute de voie indépendante qualifiée. Il n'est pas remplacé par une demande d'exécution côté client.

La cible conserve un seul propriétaire d'écriture par domaine. Une comparaison en lecture ou un import technique ne crée pas de second écrivain métier. Les lots ouverts et mises à jour indépendantes utilisent ordre, identifiant d'idempotence, point de reprise et file d'erreurs. Deux écritures sur deux systèmes indépendants ne deviennent pas atomiques du fait de leur proximité dans le code.

La réplication logique PostgreSQL sert entre systèmes compatibles et ne transforme pas les fichiers HFSQL opaques en source accessible. Sa documentation mentionne aussi des limites, notamment pour schémas et séquences ; les traiter séparément. [Réplication logique PostgreSQL](https://www.postgresql.org/docs/18/logical-replication.html), [restrictions](https://www.postgresql.org/docs/18/logical-replication-restrictions.html).

**Reprise prévue :** restaurer un état ou une version de la cible indépendante, ou réimporter un paquet neutre vérifié. Avant toute écriture métier autoritative et tout effet externe, un chargement peut être annulé sans réconciliation métier. Après des écritures, conserver et rejouer les changements, réaliser une compensation qualifiée ou accepter une perte explicitement décidée ; restaurer une ancienne sauvegarde seule ferait perdre ces opérations. Le chargement initial n'est pas une écriture métier autoritative.

Aucun retour vers WINDEV, HFSQL ou un outil PC SOFT n'est prévu par cette procédure. Un export neutre de sauvegarde n'est pas une preuve qu'une ancienne application saurait le reprendre. Fixer les objectifs de perte maximale et délai de reprise pour la cible indépendante puis les mesurer par restauration et rejeu.

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

Le déploiement WEBDEV documenté repose sur un serveur web, un serveur d'application et un compte de déploiement, avec des étapes de synchronisation des données. Le nouveau moteur doit utiliser son propre hébergement indépendant et fournir l'équivalent opérationnel : configuration des secrets, uploads, fichiers persistants, tâches, logs, sauvegarde, cluster et reprise. [Déploiement WEBDEV](https://doc.pcsoft.fr/?2028019=). WDDeploy décrit des fonctions historiques de packaging ; son utilisation est exclue du nouveau workflow. [WDDeploy](https://doc.pcsoft.fr/?3533002=).

### 6.2. Mobile : l'équivalence inclut le système et le hors ligne

Un plugin mobile doit fournir : capteurs, permission, état autorisé/refusé/révoqué, arrivée en arrière-plan, suspension, reprise et indisponibilité matérielle. Il doit permettre aux tests de simuler ces états. Sur Android, les permissions sensibles se demandent à l'exécution et peuvent être refusées ; un ancien code qui supposait l'accès permanent nécessite un traitement explicite. [Permissions Android](https://developer.android.com/training/permissions/requesting).

Pour le hors ligne, fixer le schéma local, chiffrement, quotas, synchronisation des suppressions, identité des opérations, résolution des conflits, reprise des pièces jointes et protection des identifiants. Le stockage local proposé doit être indépendant, par exemple SQLite qualifié ; il ne résout pas à lui seul les conflits métier et HFSQL reste exclu. Prévoir des cas de double modification, changement d'heure, plusieurs jours sans réseau, réinstallation, restauration d'une sauvegarde et appareil perdu.

Les versions de SDK et règles de publication changent ; elles doivent être épinglées et contrôlées dans la chaîne de build. L'historique PC SOFT montre des adaptations du niveau API Android selon les versions de WINDEV Mobile. [Spécificités Android](https://doc.pcsoft.fr/en-US/?9000108=). Pour iOS, la génération doit prévoir les étapes de certificats, profils et Xcode, sans confondre simulateur et distribution. [Déploiement In-House PC SOFT](https://doc.windev.com/en-US/?1000019926=).

## 7. Inventaire des intégrations à intégrer au plan de compatibilité

Les lignes suivantes sont un **périmètre d'audit et de conception** ; les SDK, DLL, services et pilotes tiers ne sont admissibles que sans composant PC SOFT direct ou transitif. Elles ne déclarent pas chaque API existante disponible sur chaque cible. Pour chaque appel réellement rencontré : nom et surcharges, constantes, type retourné, erreurs, cible, version, dépendance, licence, mode synchrone/asynchrone et test de référence doivent être consignés.

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

Historiquement, PC SOFT permet d'intégrer le logiciel États & Requêtes à une installation et distingue des répertoires personnels et partagés ; ce logiciel ne sera ni installé ni exécuté dans notre solution. Cela établit que la personnalisation continue après le déploiement et qu'un inventaire uniquement Git peut être incomplet. [Modules complémentaires d'installation](https://doc.pcsoft.fr/?2028045=).

**Recommandation :** importer les variantes déjà fournies dans un format lisible indépendamment, ou signaler leur format opaque comme bloquant, dans un espace utilisateur versionné, avec aperçu des changements, validation et retour à une version précédente. Pour les FAA liées à l'impression ou aux tables, reprendre les actions utilisées : export de table, copie, recherche, tri, filtres, choix des colonnes et mémorisation. Tester leurs restrictions : une colonne masquée par commodité ne doit pas devenir une colonne accessible malgré une interdiction métier.

Séparer l'export fidèle d'un état et l'export structuré des données : le premier privilégie la mise en page ; le second des types et cellules exploitables. Conserver les droits sur les fichiers générés, la purge des temporaires, le téléchargement authentifié et les noms de fichiers sûrs. Les fichiers de production ne doivent pas aboutir dans un répertoire public pour simplifier l'aperçu web.

## 9. Conditions de sortie et inconnues à lever

| Lot | Condition de sortie proposée |
|---|---|
| Absence de composants PC SOFT | Import, build, tests, installation et exploitation réussis sans DLL, outil, service, pilote, pont ou oracle PC SOFT |
| PostgreSQL | Contrôles du paquet reçu approuvés ; limites des références publiées ; reprise de la cible indépendante exercée, sans prétendre une parité globale |
| Web | Tests de sessions, onglets, AJAX, expirations, droits et isolation réussis ; restauration de déploiement démontrée |
| Mobile | Appareils et versions OS représentatifs ; permissions refusées/révoquées et hors ligne testés ; package signé installable |
| Reporting | Documents métier approuvés, totaux exacts, pagination acceptée et imprimantes critiques testées |
| Intégrations | Propriétaire, contrat, version, secret, dépendance et scénario de panne pour chaque intégration du projet |

Les inconnues bloquantes sont : disponibilité exacte des sources et analyses, version PC SOFT et options, fichiers réellement ouverts, fonctions dynamiques, formats d'états exportables, composants externes sans source, pilotes et droits de distribution, fraîcheur et cohérence des données déjà fournies, exigences de verrouillage, plateformes souhaitées et parc d'imprimantes. Il faut rechercher ces réponses dans un échantillon déjà disponible et exploitable indépendamment ; les absences restent bloquantes, sans recours à un outil PC SOFT. Cette recherche établit les voies possibles et les protocoles de décision ; elle ne peut garantir une migration sans modification pour tous les patrimoines.

## Sources primaires consultées

Les liens proches du texte constituent les références précises. Plusieurs pages sont indexées sur des éditions antérieures ; leur présence ne prouve pas une disponibilité uniforme en 2026. Les faits utilisés sont limités aux éléments décrits, et toute recommandation d'architecture reste une proposition de cette étude. Les références aux outils PC SOFT documentent le patrimoine ou les alternatives exclues ; elles ne prévoient aucune exécution de ces outils.

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
29. [Licence WINDEV, clauses à rapprocher du contrat applicable](https://doc.pcsoft.fr/?4510001).
30. [Licence du framework, clauses à rapprocher du contrat applicable](https://doc.pcsoft.fr/?1000019581).
