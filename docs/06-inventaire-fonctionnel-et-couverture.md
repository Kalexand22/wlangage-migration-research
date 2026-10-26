# Inventaire fonctionnel et démonstration de couverture

Date de recherche : 26 octobre 2026. Nature du livrable : cahier des exigences de la future solution, avec références documentaires et méthode de certification. Aucun compilateur, importeur ou adaptateur de compatibilité n'est implémenté dans ce dossier.

## 1. Ce que contient l'inventaire

Le fichier [fonctionnalites.csv](../data/fonctionnalites.csv) décrit **517 exigences**, réparties en **17 domaines**. Chaque ligne possède un identifiant stable, un périmètre, une priorité, une stratégie et un critère d'acceptation. Il couvre la chaîne complète : reprendre un projet, comprendre son code, générer l'application, conserver les comportements utiles, la qualifier, l'installer et l'exploiter. Quinze exigences P0 disposent désormais de références ciblées avec limites explicites ; leur précision documentaire ne prouve aucune conformité d’exécution. Le registre [sources-inventaire.json](../data/sources-inventaire.json) distingue les références thématiques des observations ponctuelles et précise le mode d'accès réellement obtenu.

Cette matrice est une base fonctionnelle étendue, destinée à devenir le backlog de référence. **Elle ne constitue pas une liste certifiée de toutes les fonctions WLangage, surcharges, constantes, propriétés et cibles de toutes les versions PC SOFT.** Les signatures API ne se déduisent pas d'une liste de familles. L'exhaustivité demandée devient une obligation de fermeture du périmètre et de traçabilité, décrite ci-dessous, avant toute promesse de compatibilité complète.

Cette distinction change le produit à construire : le futur IDE doit pouvoir expliquer, pour chaque objet d'un projet, s'il est importé, compilé, émulé, exécuté par un pont ou bloquant. Un pourcentage global sans dénominateur explicite masquerait les incompatibilités les plus coûteuses.

### Répartition

| Domaine | Exigences | Exemple de frontière à qualifier |
|---|---:|---|
| Import et projet | 31 | Version, format hybride, sections opaques, .MCU, constantes et événements |
| Langage | 40 | Options de compilation, conversions, portées, POO, indirection |
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
| Qualité | 23 | Oracle, erreurs, concurrence, performances, périphériques réels |
| Sécurité et gouvernance | 16 | Groupware, secrets, isolation, données sensibles, licences |
| Collaboration | 10 | Git/GDS, fusion visuelle, exigences, documentation, CI |
| Exploitation et support | 15 | Watchdog, reprise, support, modes hors ligne et réversibilité |
| **Total** | **517** | **Aucun de ces points n'est marqué compatible par anticipation** |

Les ajouts de revue couvrent notamment UML, MCD Merise, full-text, HBase/HDFS, aide contextuelle, anciennes API SQL, vues matérialisées et intégrité inaltérable. Les hôtes ActiveX, OLE, XAML, Java et Flash sont distingués ; les cibles sont restreintes ou signalées comme nécessitant un remplacement. COM/TAPI/TWAIN ne deviennent pas disponibles sur Linux ou mobile par une simple recompilation. Réplication universelle et serveur spare ont deux contrats séparés.

Les domaines se recoupent volontairement aux frontières : « champ TCD » concerne l'objet visuel ; ses caches et recalculs concernent le moteur de données ; son export concerne la restitution. Il ne faut pas additionner ces lignes pour annoncer un nombre de fonctions PC SOFT reproduites.

### Lecture des colonnes du CSV

| Colonne | Sens et règle de lecture |
|---|---|
| `id` | Identifiant d'exigence `F-0001` à `F-0517` ; ne pas renuméroter après publication |
| `domaine`, `sous_domaine` | Classement de navigation, sans déduire les dépendances techniques |
| `fonctionnalite` | Capacité à traiter ; certaines familles exigent ensuite plusieurs contrats API |
| `produits_reference` | Famille produit dans laquelle rechercher les usages ; ne signifie pas que chaque fonction existe dans chaque édition citée |
| `cibles_proposees` | Ambition de la future solution ; ce champ ne décrit pas les disponibilités officielles PC SOFT |
| `priorite` | Ordre proposé du programme, à recalibrer par les applications pilotes |
| `strategie` | Voie de réalisation envisagée, sans garantie de faisabilité acquise |
| `statut_preuve` | Exigence proposée ; référence thématique ou ciblée sur un contrat partiel |
| `critere_acceptation` | Résultat observable à vérifier, puis à transformer en scénarios versionnés |
| `source_url` | Point de départ documentaire ; son contenu ne prouve pas toutes les combinaisons de cette ligne |
| `statut_implementation` | Toutes les lignes : `non implémenté` |
| `portee_source` | Disponibilité exacte par cible et version à qualifier |

Les références thématiques sont marquées ainsi pour empêcher qu'une URL générale soit prise pour une validation ligne par ligne. Les noms d'API historiques dans les exigences sont des sujets d'investigation et de qualification, pas une déclaration universelle de disponibilité ou de droit de redistribution.

### Priorités proposées

- **P0 : 267 exigences** liées au diagnostic fiable, au noyau de compatibilité, aux premières applications Windows, aux données, aux états et à la démonstration de non-régression. P0 signifie « nécessaire avant de déclarer réussi le périmètre qui l'utilise », pas « à livrer entièrement dans le premier prototype ».
- **P1 : 230 exigences** de parité produit, intégrations et extension aux cibles Web/mobile, dont l'ordre dépendra de la fréquence réelle dans les pilotes.
- **P2 : 20 exigences** de spécialisations ou de legacy à isoler derrière un contrat précis. P2 ne signifie jamais ignorable lorsqu'une application en dépend.

Une application industrielle utilisant DDE, un automate ou une imprimante particulière peut rendre sa dépendance P2 prioritaire pour son pilote. L'ordre global du backlog n'autorise pas une perte fonctionnelle silencieuse.

## 2. Pourquoi l'exhaustivité API exige un autre registre

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

Il faut aussi conserver les options du projet : une option de court-circuit ET/OU ou de copie des tableaux peut changer le résultat sans modifier une seule ligne de code. L'importeur doit exporter cette configuration avec la source. [Description du projet, compilation](https://doc.pcsoft.fr/?9500218=).

## 3. Procédure de fermeture du catalogue

### 3.1 Fixer la baseline

Choisir des versions et builds précis, documenter les licences et l'accès à leur documentation, sélectionner les cibles réellement promises. La première baseline recommandée est étroite : une famille de projets Windows et quelques applications métier représentatives. Les éditions 2025 et les annonces 2026 alimentent la recherche ; aucune disponibilité 2026, encore moins une version ultérieure, ne doit être inférée sans sa fiche et son build.

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

Prévoir une revue humaine pour les appels dynamiques non résolus. Une instrumentation de l'application originale peut enrichir les usages observés si elle est autorisée, mais une trace sans appel observé ne prouve pas qu'un chemin est inutile. Les plugins, DLL, ActiveX et composants externes sans sources restent des dépendances séparées du catalogue WLangage.

### 3.5 Croiser documentation, import et exécution

Établir trois ensembles indépendants : éléments documentés du profil, éléments présents dans les sources et éléments effectivement exécutés durant les scénarios. Produire les différences : symbole non reconnu, objet opaque, API documentée absente du runtime, comportement exercé sans preuve, objet déclaré mais non exercé.

La fermeture du catalogue documentaire exige une vérification de toutes les pages de pagination et des branches du profil. La fermeture d'un pilote exige que chacun de ses usages dispose d'une stratégie et d'un état de preuve. Ce sont deux obligations différentes ; une migration peut être complètement qualifiée sur un périmètre limité sans avoir réimplémenté toute la plateforme.

## 4. Ce qu'une preuve doit contenir

Une exigence du CSV devient un ou plusieurs scénarios avec entrées, préconditions, profil exact, données isolées et résultat attendu. La preuve lie l'identifiant d'exigence à la signature utilisée, au test, à l'exécution et aux artefacts observés.

Pour chaque surcharge réellement utilisée, prévoir les cas nominal, limites et erreur ; ajouter NULL, paramètres omis, conversions, locale et interaction de contexte lorsque pertinents. Les erreurs demandent code, catégorie et état des données ; comparer seulement une chaîne de message traduite serait fragile. La documentation distingue erreurs d'exécution et erreurs de programmation : les tests doivent donc couvrir leurs circuits respectifs. [Gestion des erreurs en exécution](https://doc.pcsoft.fr/fr-FR/?3034016=).

L'oracle de référence est une exécution de l'application ou d'un cas minimal sous la version PC SOFT autorisée, sur une copie du corpus. Elle doit être enregistrée avec son build, son OS et ses dépendances. L'exécution cible utilise exactement les mêmes entrées. Horloge, hasard, réseau et ordre des threads doivent être contrôlés ou assortis d'un contrat de tolérance explicite. Les effets externes sont simulés ou confinés : on ne rejoue pas deux paiements réels pour comparer deux moteurs.

| Surface | Observation nécessaire | Exemple de divergence bloquante |
|---|---|---|
| Langage | Valeur, type, effets de bord, erreur | Second opérande ET exécuté dans le mauvais profil |
| Événements | Séquence, paramètres, focus, modalité | Validation contournée lors d'une fermeture |
| HFSQL | Buffer, curseur, état global, verrou, transaction | H implicite opère sur le mauvais fichier |
| SQL | Multiensemble de lignes, types, ordre contractuel | NULL transformé en chaîne vide |
| UI | État sémantique, accessibilité, capture sous conditions fixes | Ligne masquée exportée malgré une restriction |
| États | Texte, pages, positions, polices, réglage imprimante | Facture repartie sur une page de plus |
| Mobile | Cycle de vie, permissions, reprise hors ligne | Écriture locale perdue après arrêt du processus |
| Déploiement | Paquet, installation, signature, mise à jour, rollback | Version installée incapable de lire le schéma migré |

Les tests automatiques PC SOFT existants doivent être inventoriés et repris quand leurs API sont supportées. L'éditeur documente des scénarios en WLangage pour fenêtres, procédures et classes ; cela constitue un actif de migration, sans supposer que ces scénarios couvrent tous les traitements métier. [Tests unitaires](https://doc.pcsoft.fr/?1410086932=).

## 5. Calculs de couverture sans fausse précision

Toutes les mesures ci-dessous sont **à calculer dans la future solution**. Pour ce dépôt de recherche : aucune compatibilité exécutée n'est mesurée, et les 517 exigences sont non implémentées.

Définir `D_p` comme l'ensemble des contrats API applicables au profil `p` ; `U_a,p` comme les contrats utilisés par l'application `a` ; `Q_p` comme ceux qualifiés par un test dont l'oracle et la provenance sont disponibles. Un contrat inclut sa surcharge et son profil.

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

Un pilote est prêt à basculer lorsque tous ses éléments inventoriés ont une stratégie explicite, tous les usages statiques et dynamiques pertinents sont résolus, les scénarios métier obligatoires passent, les différences de données et documents sont expliquées, et l'installation ainsi que le retour arrière ont été exercés. Aucun composant natif manquant, champ supprimé, événement ignoré ou conversion avec perte ne peut être masqué par une génération réussie.

La liste du CSV n'accorde pas le droit d'omettre une capacité découverte après l'audit. Ajouter l'exigence avec un nouvel identifiant, son propriétaire, son origine et ses dépendances ; conserver l'historique. Pour chaque release, publier le profil certifié, le périmètre des pilotes, les limites et les preuves correspondantes.

Les surfaces à surveiller particulièrement sont les .MCU et autres codes post-déploiement, dictionnaires .DIC abonnés, états personnalisables, chaînes traduites réintégrées, composants sans source, options du projet, intégrations DDE/RPC/X10/UPnP, TCD et caches, administration SaaS, robots de surveillance, et règles implicites des fonctions H. Elles doivent être cherchées activement dans l'audit, même lorsqu'elles ne sont pas visibles dans les principaux écrans du projet.

Cette procédure permet une affirmation vérifiable : « cette application, dans ces profils et ces scénarios, garde son code et ses comportements qualifiés ». La promesse « tout projet de toute version fonctionne sans changement » resterait dépourvue de preuve tant que le catalogue documentaire, les composants externes et les comportements dynamiques ne sont pas fermés.
