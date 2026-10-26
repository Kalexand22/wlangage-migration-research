# Revue complémentaire de couverture fonctionnelle

**Note historique : cette revue décrit un état antérieur. La contrainte finale du propriétaire exclut tout logiciel, DLL, outil, pilote, serveur et oracle PC SOFT, même via un tiers dans notre chaîne. Les anciennes options de maintien HFSQL ou d’observation exécutée ne sont plus des voies actives. Voir le [périmètre retenu](../docs/15-perimetre-independant-et-preuve-de-faisabilite.md).**

Revue du 26 octobre 2026. Documents relus : `docs/02-langage-et-import.md`, `docs/03-experience-developpement-et-interface.md`, `docs/04-donnees-integrations-et-cibles.md`, `docs/08-ameliorations-produit.md`. Première passe sur documents, puis relecture du CSV de 500 lignes : les premiers compléments ont été intégrés à cette matrice. Le chapitre 06 n'était pas encore disponible lors de cette revue. Cette note identifie des familles ou contrats distincts, pas un nouvel inventaire concurrent. Les URL du CSV ont une portée thématique et les lignes sont des exigences proposées ; elles ne constituent pas chacune l'attestation d'une capacité PC SOFT sur une cible donnée.

## Compléments prioritaires à vérifier dans la matrice

P0 signifie « omission pouvant invalider une migration du patrimoine concerné » ; P1 signifie « fonction distincte à auditer et planifier selon usage » ; P2 signifie « patrimoine ancien/spécialisé à détecter, même si l'implémentation est différée ». Les priorités ne signifient pas que tous les clients utilisent ces fonctions.

| ID de revue | Priorité | Couverture actuelle | Complément distinct à inscrire si absent | Preuve et recette proposées |
|---|---|---|---|---|
| COV-01 | P0 | Le langage dynamique est traité ; la personnalisation utilisateur est surtout présentée via états/FAA | **Macro Code Utilisateur (MCU)** : macros ajoutées après déploiement, fichiers `.MCU`, restrictions d'API, attachement aux événements et remontée/import dans le projet | Inventorier les macros sur postes et partages, pas seulement Git ; comparer une macro autorisée et un appel interdit. [Concepts WINDEV 25, chapitre MCU](https://www.pcsoft-windev-webdev.com/conceptsWD25.pdf) |
| COV-02 | P0 | Groupware, identités et hébergement sont couverts | **SaaS applicatif WEBDEV** : sociétés/tenants, abonnements/licences, utilisateurs, quotas de connexions, plages/durée d'accès, rattachement à une base et administration par API | Ne pas confondre ces objets métier avec l'abonnement à l'IDE WINDEV Suite SaaS ; tester cloisonnement de deux sociétés et expiration d'un droit. [Brochure officielle WEBDEV 25, administrateur SaaS](https://www.pcsoft-windev-webdev.com/brochureWB25-simple.pdf), [nouveautés WLangage 2025 et SaaSAdminListeLicence](https://help.windev.com/en-US/?9000001=) |
| COV-03 | P1 | Modèles, composants et styles sont traités | **Dictionnaires de réutilisation `.DIC`**, abonnement à un élément et propagation des modifications | Le dictionnaire est une source réutilisable distincte d'un composant compilé ; reprendre identité, lien d'abonnement et surcharge. Recette : modifier l'élément maître et comparer les objets abonnés. [Manipuler les champs d'une page](https://doc.windev.com/fr-FR/?1014006=), [Manipuler les champs d'un état](https://doc.windev.com/fr-FR/?1013015=) |
| COV-04 | P1 | Télémétrie, traces et exploitation sont couvertes globalement | **Robot de surveillance/watchdog**, moniteur, contre-robot, calendrier des sondes, notifications et tests WLangage personnalisés | Reprendre les configurations hors dépôt et démontrer l'alerte sur panne puis la détection d'une panne du robot lui-même. Ce n'est ni l'automate de tests, ni la Fabrique logicielle. [Installation du contrôleur du robot](https://doc.windev.com/en-GEN/?3541102=), [concepts officiels et schéma robot/contre-robot/moniteur](https://www.pcsoft-windev-webdev.com/conceptsWD20.pdf) |
| COV-05 | P1 | i18n à l'exécution est couverte | **Chaîne de traduction WDMSG/WDTRAD** : extraction, dictionnaire de traduction, terminologie, contrôle des messages modifiés et réintégration ; traductions des messages système/menus/installer | Préserver identifiants de ressources, variantes et paramètres ; faire un aller-retour traduction sans perdre les chaînes non modifiées. Ne pas confondre ce dictionnaire linguistique avec `.DIC`. [Concepts WEBDEV 2025, multilingue](https://fr.pcsoft-windev-webdev.com/conceptsWB2025.pdf), [Propriétés du dictionnaire WDTRAD](https://doc.windev.com/en-US/?3518022=), [Langues supplémentaires de WDSetup](https://doc.windev.com/en-US/?2028037=&name=wdsetup_gestion_idiomas_adicionales) |
| COV-06 | P1 | TCD nommé comme champ ; reporting traité séparément | **Moteur du TCD** : axes/dimensions, agrégats, filtrage avant calcul, recalcul total/incrémental, navigation détaillée, comparaison de périodes, sauvegarde/chargement du résultat | Un composant visuellement similaire n'assure pas le même calcul. Recette : même résultat après calcul total, mise à jour partielle et restauration ; profil par cible/version. [Filtrer un TCD](https://doc.windev.com/en-US/?1000029005=&lf=fr&name=Filtering_the_headers), [TCDCharge](https://doc.windev.com/fr-fr/?1000020507=&name=tcdcharge_fonction&product=ER) |
| COV-07 | P1 | Réplication, sauvegarde et hors ligne sont mentionnés | **Réplication universelle** et transportable : réplica maître/abonné, filtres de réplication, paquets échangés, conflits et reprise | À distinguer de réplication de serveurs HFSQL et de réplication logique PostgreSQL ; conserver les identités de réplicas et tester doubles modifications et paquets répétés. [HCréeRéplicaTransportable](https://doc.pcsoft.fr/fr-FR/?3044209=&verdisp=210) |
| COV-08 | P1 | Web sessions/AWP, déploiement et URL sont évoqués | **Référencement et continuité des URL** : métadonnées de page, génération/adressage des pages, URL rewriting, routes historiques et redirections après migration | Tester la résolution des URL publiques existantes et leurs paramètres ; auditer métadonnées et pages devant rester non indexées. Ne pas reprendre les promesses historiques relatives aux mots-clés comme garanties SEO actuelles. [Concepts WEBDEV 2024, référencement](https://fr.pcsoft-windev-webdev.com/conceptsWB2024.pdf), [Support officiel URL rewriting](https://www.pcsoft-windev-webdev.com/tdftech/2014/SupportDeCours.pdf) |
| COV-09 | P2 | API Win32, COM/OLE et ActiveX couverts | **DDE**, ses conversations, événements et liens chauds/tièdes, distincts de COM | Détection des appels et dépendances ; pont Windows ou remplacement contractualisé. La présence historique n'est pas une raison pour implémenter avant d'avoir un cas client. [Référence historique officielle WLangage 18, DDE](https://www.pcsoft-windev-webdev.com/wlangage.pdf) |
| COV-10 | P2 | FTP/SFTP/SSH standard couverts | **FTP/RPC propre à WINDEV** : protocole hérité `Net*`, services distants et contraintes 32 bits | Détecter le protocole exact ; conserver un pont limité ou remplacer le contrat. Un client FTP standard n'est pas automatiquement substituable. [Documentation officielle FTP/RPC WINDEV](https://doc.pcsoft.fr/fr-FR/?3056012=) |
| COV-11 | P2 | IoT/capteurs et industrie couverts de manière générique | **Domotique X10 `Domo*` et UPnP** : deux contrats distincts, découverte, adressage, commandes et état | Identifier interfaces et matériels réels ; simulateur pour les tests du protocole et recette sur matériel avant déclaration de parité. Le catalogue historique prouve les familles, pas leur support 2026 sur chaque cible. [Catalogue officiel version 26, Communication](https://fr.pcsoft-windev-webdev.com/liste-exhaustive-des-fonctionnalites-de-windev.pdf) |
| COV-12 | P2 | Téléphonie mobile couverte | **Téléphonie Windows/TAPI** : appels entrants, numéro appelant, modem/voix et événements, distincte du dialer Android/iOS | Vérifier les dépendances de l'application existante, le fournisseur TAPI et l'architecture ; reprise par pont ou nouveau fournisseur qualifié. [Concepts WINDEV 21, téléphonie](https://www.pcsoft-windev-webdev.com/conceptsWD21.pdf) |
| COV-13 | P1 | Audio/vidéo et accessibilité couverts | **Synthèse et reconnaissance vocales** : choix des voix, interruption/file de lecture, commandes et callbacks, disponibilité de service | Les distinguer de lecture audio et d'appel IA ; tester voix/langues installées, annulation et refus d'accès au micro. [Concepts WINDEV Mobile 2025](https://fr.pcsoft-windev-webdev.com/conceptsWM2025.pdf), [Référence historique WLangage, reconnaissance vocale](https://www.pcsoft-windev-webdev.com/wlangage.pdf) |
| COV-14 | P1 | Fabrique logicielle citée comme CI/génération | **Import des plans d'action de Fabrique logicielle** : coordinateur, automates, déclencheurs, variables, secrets et droits | Distinguer équivalent CI moderne et reprise des configurations existantes. Recette : porter un plan représentatif avec ses dépendances et erreurs. [Options de l'administrateur de Fabrique logicielle](https://doc.windev.com/en-US/?1000019583=) |

Les descriptions dans ce tableau sont des recommandations de couverture. Les sources établissent la présence d'un mécanisme dans l'écosystème, parfois historique ; elles ne démontrent pas un format d'import public ni une possibilité de redistribution.


## Rapprochement effectué avec le CSV à 500 lignes

Les compléments COV-01 à COV-14 ne sont plus des omissions de famille après rapprochement. Les numéros ci-dessous permettent de les retrouver ; les détails de recette du tableau restent utiles.

| Revue | Ligne(s) de matrice | État de la revue |
|---|---|---|
| COV-01 MCU | F-0479 | Famille explicite ; auditer les macros hors dépôt |
| COV-02 SaaS applicatif | F-0352, F-0493 | Famille explicite ; distinguer abonnement IDE et administration de l'application |
| COV-03 dictionnaire | F-0231 | Présent ; préciser champs/pages/états et abonnement, au-delà du seul modèle de données |
| COV-04 watchdog | F-0494 | Présent ; ajouter contre-robot et configurations dans le corpus |
| COV-05 traduction | F-0495, F-0496 | Présent ; conserver terminologie, identifiants et messages de l'installer |
| COV-06 TCD | F-0178, F-0490 à F-0492 | Présent ; parité du calcul à qualifier par cible |
| COV-07 réplication universelle | F-0261 | Présent ; distinguer contrat universel/transportable du serveur spare |
| COV-08 URL et référencement | F-0356 | Présent ; conserver les routes/paramètres et tester les redirections |
| COV-09 DDE | F-0497 | Présent, lot spécialisé |
| COV-10 RPC WINDEV | F-0498 | Présent, lot historique |
| COV-11 X10 et UPnP | F-0499, F-0500 | Présents ; conserver deux contrats distincts |
| COV-12 TAPI | F-0327 | Présent ; distinguer SMS/appel mobile du fournisseur Windows |
| COV-13 voix | F-0330 | Présent ; pas seulement lecture audio |
| COV-14 Fabrique logicielle | F-0443 | Présent ; inventorier les plans existants et leurs déclencheurs |

### Familles supplémentaires encore absentes à ce point de lecture

Ces six lignes sont des suggestions finales au rédacteur du catalogue. Elles peuvent être ajoutées avec de nouveaux IDs ou intégrées explicitement à un critère existant ; il faut éviter qu'un simple mot générique serve de preuve de couverture.

| Revue | Priorité | Famille distincte | Ce qui manque au contrat | Source primaire |
|---|---|---|---|---|
| COV-15 | P1 | Éditeur/import de modèles **UML** | Modèles, diagrammes, liens vers classes, génération éventuelle et navigation ; pas équivalent aux seuls dessins d'organigramme dans une application | [Concepts WINDEV 25, éditeur UML](https://www.pcsoft-windev-webdev.com/conceptsWD25.pdf) |
| COV-16 | P1 | **MCD Merise** et passage au modèle logique | Entités, associations, cardinalités, règles et correspondance de génération MCD→analyse ; F-0221 tables/rubriques et F-0016 import analyse ne suffisent pas à conserver le modèle conceptuel | [Concepts WEBDEV 2024, analyse et génération à partir d'un MCD](https://fr.pcsoft-windev-webdev.com/conceptsWB2024.pdf) |
| COV-17 | P0 si utilisé | **Recherche HFSQL full-text** | Index textuels, tokenisation, mots vides/synonymes, documents RTF/HTML et ordre de pertinence ; distincte des données vectorielles et recherche sémantique F-0236 | [Brochure technique HFSQL, recherche full-text](https://www.pcsoft-windev-webdev.com/hfsql.pdf) |
| COV-18 | P1/P2 selon patrimoine | **HBase et HDFS** | Contrats `hb*` pour les tables/cellules et `hdfs*` pour le système de fichiers distribué ; distincts de MongoDB/Redis et d'un stockage objet générique | [Catalogue officiel version 26, sections 6.7 et 6.8](https://fr.pcsoft-windev-webdev.com/liste-exhaustive-des-fonctionnalites-de-windev.pdf) |
| COV-19 | P1 | **Éditeur/génération d'aide utilisateur** | Pages, structure, identifiants contextuels, rattachement aux fenêtres/états, liens et langues ; F-0118 concerne l'aide IDE et F-0441 la documentation technique | [Création d'aide automatique](https://doc.pcsoft.fr/en-US/?2010030=&name=Automatic_help) |
| COV-20 | P0 si utilisé | Ancienne famille **SQL*** et **SQLConnecteWS** | Connexions, curseurs, tableaux de résultats, erreurs, transactions et exécution via webservice ; un adaptateur H* ne couvre pas ces appels et SQLConnecteWS a ses propres limitations | [Accès à une base par webservice et fonctions SQL](https://doc.windev.com/fr-FR/?1000021063=&product=WB) |

Les F-0326 « OPC UA et automates » et F-0348 « PWA hors ligne » sont acceptables comme exigences proposées ; la source thématique ne doit pas les transformer en affirmation de support natif PC SOFT. Ce principe vaut pour l'ensemble des lignes de la matrice.

## Fonctions présentes à préciser sans créer une fausse nouvelle famille

- **TWAIN/scanner** : déjà explicitement couvert dans le tableau Capture de `docs/04`. Ajouter plutôt les cas recto-verso, acquisition multipage, résolution, annulation, interface du pilote et bridge 32/64 bits à la recette. [Acquisition TWAIN](https://help.windev.com/en-US/?3078007=&lf=fr).
- **Bitmap/dessin** : image/dessin et formats figurent déjà dans `docs/03` et `docs/04`. Dans la matrice détaillée, distinguer fonctions de dessin et données de pixels de l'affichage d'un champ Image ; préciser transparence, alpha, métriques de texte, conversions, coordonnées et ressources natives. Ce sont des contrats supplémentaires, pas une nouvelle plateforme.
- **États & Requêtes créés chez le client** : déjà couvert dans `docs/04`, y compris répertoires personnel/partagé. Ne pas ajouter une seconde ligne intitulée « reporting utilisateur » sans différence de contrat.
- **Groupware et variantes de login** : `docs/03` couvre classique/serveur, droits et personnalisation. Si la matrice dispose déjà de ces dimensions, compléter seulement le modèle de droits et les profils ; éviter des lignes « auth » identiques.
- **Centre de Gestion de Projets** : tâches/exigences/incidents sont dans `docs/03`. L'enjeu distinct est l'import des liens, règles métier et historiques de temps/décisions, pas nécessairement la reconstruction d'un gestionnaire complet. [Concepts WINDEV 2024, gestion de projets](https://fr.pcsoft-windev-webdev.com/conceptsWD2024.pdf).
- **Télémétrie** : présente dans `docs/03` et A09. Ajouter au besoin l'inventaire/migration des capteurs, catégories et configurations existantes ; ne pas remplacer implicitement l'historique par un nouveau tableau vide. [Support officiel, télémétrie](https://www.pcsoft-windev-webdev.com/tdftech/2017/SupportDeCours.pdf).
- **Aide utilisateur** : aide intégrée et génération sont mentionnées. Les sujets, identifiants de contexte, liens depuis les fenêtres et langues doivent être conservés si la matrice ne les précise pas. [Création d'aide automatique](https://doc.pcsoft.fr/en-US/?2010030=&name=Automatic_help).
- **Mises à jour utilisateur** : la génération/diffusion existe dans le périmètre. Qualifier administration multiutilisateur, versions disponibles et historique de mise à jour, si présents dans le patrimoine. [Famille officielle Live Update](https://help.windev.com/fr-FR/search2.awp?cat=fonctions-mises-jour-applications%2C257&origin=browse).

## Points de vocabulaire à ne pas transformer en faits non vérifiés

**RPA.** Cette recherche n'a pas établi une famille PC SOFT moderne dédiée à la RPA au sens pilotage générique d'applications par reconnaissance d'interface. L'automation COM, les tests automatiques, le robot watchdog et la Fabrique logicielle sont documentés, mais différents. Les fichiers de réplication transportable peuvent également faire apparaître ce sigle dans des recherches ; ne pas en déduire une fonction RPA. Une nouvelle fonction d'automatisation UI peut être proposée comme amélioration, clairement identifiée comme telle.

**Généalogie de projets.** Aucune fonction actuelle nommée exactement ainsi n'a été vérifiée. Le graphe historique du projet et ses enchaînements sont décrits dans les anciens concepts ; l'historique des sources, l'héritage des modèles et les dépendances ne sont pas le même objet. Employer des termes précis dans la matrice et distinguer conservation du patrimoine historique et expérience actuelle. [Concepts WINDEV 20, graphe du projet](https://www.pcsoft-windev-webdev.com/conceptsWD20.pdf).

**Domotique et industriel.** Les sources établissent notamment X10/UPnP. Elles ne justifient pas d'annoncer par défaut un connecteur WLangage natif Modbus, OPC UA, KNX, Zigbee ou Z-Wave. Relever les bibliothèques externes rencontrées, puis les qualifier une par une.

## Intégration dans le catalogue final

Pour chaque COV retenu, rattacher un identifiant stable de la matrice, un profil version/cible, une stratégie (réimplémenter/pont/remplacer/différer) et un test. Une fonction spécialisée non demandée peut rester « détectée, hors lot », mais elle doit apparaître au rapport d'import. L'exhaustivité du périmètre d'audit ne suppose pas une implémentation immédiate de chaque technologie ancienne.


## Clôture de la revue de livraison

La matrice finale comporte 517 exigences. Les familles supplémentaires signalées dans cette revue ont été intégrées et les contraintes des cibles natives ont été précisées. Les contrats détaillés et preuves d'exécution restent à construire suivant le chapitre 06. Le profil JSON inclut désormais des rubriques numériques et de données, laissées inconnues. Cette note conserve le constat historique de la revue, sans revendiquer une certification d'exhaustivité.
