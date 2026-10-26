# Protocole d'audit, pilote et recette

Ce protocole opérationnalise la conception ; **il n'a pas été exécuté sur des projets WINDEV dans cette étude**. Les fichiers du dossier `examples/` sont des modèles de travail à compléter, sans relation normative avec les formats PC SOFT.

## 1. Définir un périmètre fermé

Avant toute mesure, signer techniquement le périmètre : produit, version, build, configuration, options, cibles d'origine et de génération, dépendances et fonctionnalités métier. Un « projet WINDEV » sans ces informations n'est pas un cas de compatibilité reproductible.

Le dossier d'un pilote contient trois ensembles distincts : projet original conservé, exports complémentaires avec provenance, résultats d'exécution. Les données réelles sensibles et secrets restent dans l'environnement autorisé de l'équipe ; les dépôts de preuves contiennent des jeux synthétiques ou anonymisés et des références de secrets.

Le pilote doit concentrer des difficultés représentatives, pas simplement le plus petit écran. Proposition de sélection : un écran de saisie maître/détail avec validation et transaction ; une recherche et un parcours indexé avec filtre ; un état paginé avec rupture ; une opération asynchrone ; une intégration native effectivement utilisée. Si le patrimoine n'utilise pas l'une de ces familles, consigner sa non-applicabilité et choisir un autre risque réel.

## 2. Paquet à recueillir

| Ensemble | Contenu demandé | Contrôle avant utilisation |
| --- | --- | --- |
| Sources | Copie complète, éléments inclus/exclus, branches et composants internes | Empreintes et inventaire indépendants ; copie originale immuable |
| Environnement | IDE/build, mode de licence, runtime installé, OS/architecture | Reconstruction ou exécution de référence reproductible sous droits appropriés |
| Options | Compilation, encodages, langues, fuseaux et configurations | Captures ou exports des réglages effectifs et surcharges locales |
| Interface | Fenêtres/pages, modèles, champs, propriétés, plans, styles, événements | Nombre d'objets et références croisés avec l'IDE et l'application |
| Données | Analyse, SQL, contraintes, clés, triggers, procédures, connexions | Schéma recensé ; comptes de test séparés ; secrets référencés |
| États | Sources, polices, modèles, imprimantes, exports de référence | Droits de reproduction des ressources et paramètres d'impression relevés |
| Interop | DLL, COM, ActiveX, assemblages, pilotes, périphériques | Version, architecture, contrat, disponibilité du matériel et licence |
| Déploiement | Installateur, service, mise à jour, signature, paramètres | Installation et désinstallation documentées sur poste propre |
| Exploitation | Volumes, incidents représentatifs, latences et pics | Mesures datées avec matériel et méthode, sans extrapolation |
| Recette | Scénarios, jeux d'entrée, sorties, erreurs attendues | Responsable métier et classification de criticité |

Un composant compilé sans source reste une dépendance externe, même si l'import du reste réussit. Un fichier de propriété opaque reste inventorié, avec sa taille et son empreinte, jusqu'à résolution.

## 3. Registre d'éléments et de pertes

Chaque objet importé possède un identifiant stable et une provenance : chemin, conteneur, élément, événement, intervalle source, empreinte, version d'extraction. Les dépendances forment un graphe typé : appelle, lit/écrit, affiche, contient, hérite, imprime et référence une ressource.

Pour chaque propriété : `reconnue`, `préservée opaque`, `convertie avec règle`, `reconstituée par preuve`, `manquante` ou `non applicable justifiée`. Ces statuts ne sont pas des niveaux de compatibilité d'exécution. Un objet peut être parfaitement importé et mal exécuté ; il peut aussi être opaque mais utilisé via un pont explicitement déclaré.

Le rapport d'import doit pouvoir répondre : combien de traitements sont présents dans l'original et la cible ; lesquels ne sont pas attribués à un événement ; quelles propriétés ne sont pas interprétées ; quelles sources sont absentes ; quels chemins de compilation et usages dynamiques restent indéterminés. La génération finale est bloquée lorsqu'une absence peut affecter une fonctionnalité exigée.

## 4. Une tranche verticale de référence

Exemple synthétique : « enregistrer une commande et produire son document ». Il sert à montrer la méthode, sans supposer la structure du patrimoine du client.

1. Ouvrir la fenêtre, vérifier ses valeurs initiales et le focus.
2. Saisir un client et une ligne ; vérifier masques, entrée/sortie et recalcul.
3. Provoquer une erreur métier puis corriger sans perdre les données.
4. Sauver, faire échouer un contrôle concurrent puis rejouer une transaction valide.
5. Fermer et rouvrir ; vérifier les clés, montants, relations et valeurs NULL.
6. Produire le document, contrôler son contenu, sa pagination et les exports.
7. Simuler un incident réseau ou une fermeture pendant une étape pertinente.

Les mêmes entrées sont appliquées à deux environnements isolés possédant un état initial équivalent. Les opérations externes sont capturées ou simulées : le scénario de comparaison ne doit pas envoyer deux paiements, deux courriels ou deux commandes réelles. L'application de référence produit les observations attendues, puis la nouvelle implémentation les reproduit.

## 5. Oracle et capture des observations

L'oracle est la version effectivement retenue de l'application d'origine, avec son profil. Il n'est pas une interprétation d'un modèle de langage. La documentation décrit les contrats, les tests les mesurent, et le responsable métier arbitre les comportements volontairement modifiés.

Toutes les observations ne sont pas instrumentables de la même façon. Distinguer capture boîte noire par l'interface et la base, journalisation ajoutée dans une copie de recette lorsque permise, et tests unitaires de procédures isolées. Une instrumentation qui change la concurrence ou les temps peut elle-même perturber le comportement ; conserver son niveau d'intrusion dans la preuve.

| Observation | Comparaison proposée | Précaution |
| --- | --- | --- |
| Valeurs et calculs | Type, valeur, échelle, précision et erreurs | Aucun arrondi global ajouté pour masquer les écarts |
| Interface | Focus, sélection, navigation, ordre d'événements accessibles | Déclarer ce qui est observé indirectement |
| Données | Valeurs canoniques, clés, relations et effets de transaction | Comparer NULL/vide et types, pas uniquement des chaînes affichées |
| Documents | Texte, positions, nombre de pages, ruptures et rendu | Ne pas comparer seulement les octets PDF avec horodatages variables |
| Fichiers et réseau | Chemins, encodages, contenu, requêtes/réponses et reprises | Retirer secrets et identifiants personnels des journaux |
| Erreurs | Catégorie, moment, état final et récupération | La formulation peut être différente si le contrat l'autorise explicitement |
| Concurrence | Invariants, interblocages, accès perdus et terminaison | Plusieurs ordonnancements ; pas un ordre exact artificiel entre threads |
| Temps et mémoire | Médiane, p95, pic, nombre d'itérations | Machines, chauffe, volumes et variabilité documentés |

Le temps, l'aléatoire, les GUID, les chemins temporaires et les réponses réseau peuvent nécessiter une normalisation. Chaque normalisation possède une justification et un test qui prouve qu'elle ne neutralise pas une différence métier. Un total monétaire incorrect ne devient jamais acceptable parce que l'interface est proche.

## 6. Batteries de tests à construire

**Langage :** limites numériques et dépassements, conversions implicites, précision monétaire, dates invalides ou vides, changement d'heure, ANSI/Unicode, indices et bornes, copie/référence, portées, paramètres facultatifs et par référence, POO, exceptions, indirections et compilation dynamique. Ajouter une combinaison de réglages différente lorsque l'option change le sens d'un cas.

**Interface :** initialisation, entrée/sortie, saisie invalide, tabulation, raccourcis, Enter/Escape, fenêtres modales, réentrance, multi-fenêtres, redimensionnement, DPI, thèmes, traductions, lecteurs d'écran et FAA réellement utilisés. Les tests pilotent les commandes accessibles autant que possible et réservent la reconnaissance visuelle aux besoins qui la justifient.

**Données :** recherche exacte/générique, doublons, filtres, parcours courant après insertion, suppression logique, verrou occupé, transaction annulée, erreur de connexion, tri/accents/casse, clés composées, mémos, import/export et changement de schéma. Les tests de concurrence utilisent au moins deux sessions isolées quand le comportement l'exige.

**États et intégrations :** début/fin de blocs, ruptures, polices manquantes, nombres localisés, pages limites, imprimantes, PDF, fichiers Office, courrier, API, matériels et fonctionnement hors ligne. Les périphériques réels sont qualifiés en complément des doubles de test.

**Exploitation :** installation sans IDE, compte non administrateur, mise à jour interrompue, retour de version, sauvegarde/restauration, secrets, certificats expirés, perte réseau, manque d'espace et crash. L'absence d'un service distant attendu doit produire un diagnostic exploitable.

## 7. Mesurer sans fabriquer un « 100 % »

Définir avant calcul des ensembles de référence versionnés. Chaque mesure inclut le dénominateur et l'identifiant du corpus.

- **Intégrité d'inventaire** : éléments source identifiés avec provenance / éléments dénombrés par la procédure de référence. Les éléments non lisibles restent inclus.
- **Conservation textuelle** : blocs dont les octets sont identiques / blocs extraits. Publier séparément les conversions d'encodage déclarées ; ne pas confondre transformation technique et réécriture métier.
- **Absence de réécriture manuelle** : traitements utilisés sans modification manuelle / traitements dans le périmètre retenu. Le nombre de lignes modifiées complète cette mesure.
- **Couverture de qualification** : cas possédant résultat comparé et preuve valide / cas exigés. Un test ignoré ou non exécuté n'est pas une réussite.
- **Conformité observée** : cas conformes / tous les cas exigés, en publiant échecs, non exécutés et dérogations. Les comportements non applicables sont justifiés dans le périmètre avant calcul.
- **Complétude API** : symboles/signatures/cibles avec statut documenté / catalogue de référence. C'est une mesure de documentation de couverture ; seule une preuve d'exécution justifie le statut conforme.

Publier également les effectifs bruts et les blocages critiques. Une moyenne pondérée peut aider à planifier ; elle ne remplace pas la liste des exigences non satisfaites. La couverture d'un corpus n'est jamais extrapolée à toutes les applications possibles.

## 8. Critères proposés pour le premier pilote

Les seuils suivants sont des critères de décision à convenir, pas des résultats atteints : aucun élément obligatoire perdu silencieusement ; tous les traitements de la tranche attribués à leur événement ; aucun écart métier critique ouvert ; tous les appels utilisés classés et toute dépendance externe déclarée ; conservation sans réécriture manuelle des traitements revendiqués compatibles ; aucune modification directe du code généré ; reconstruction sur un poste vierge ; procédure de retour arrière répétée.

Pour les performances, définir le budget par parcours à partir de la référence et de l'usage. Un seuil universel « pas plus de 10 % de ralentissement » serait arbitraire sans volumes ni matériel. Certains parcours exigent une latence absolue ; d'autres nécessitent un débit ou une limite de mémoire. Déclarer les deux si nécessaire.

Les défauts anciens détectés sont consignés. La correction volontaire d'un bug métier doit apparaître comme un changement approuvé de spécification ; elle ne doit pas être comptée comme une reproduction identique.

## 9. Bascule et retour arrière

Garder un seul propriétaire d'écriture par domaine pendant la transition. Une copie de comparaison peut être alimentée pour l'observation ; elle ne devient pas un second écrivain métier. Toute synchronisation possède un ordre, une idempotence et un point de reprise explicites.

Une bascule de données fige ou séquence les écritures, prend un point de restauration vérifié, applique les derniers changements, compare les effectifs et contrôles métier, puis change le routage. Les écritures effectuées après bascule doivent avoir une stratégie de retour : journal rejouable, reconversion prouvée ou point d'arrêt assumé. Restaurer simplement l'ancienne sauvegarde ferait perdre ces écritures.

Le dossier de passage en production contient : version de la plateforme, profil, manifeste, résultats, écarts acceptés, dépendances/licences, procédure d'installation, sauvegarde vérifiée, responsabilités et procédure d'incident. Le retour arrière de l'application et le retour arrière des données sont deux opérations distinctes à tester.

## 10. Dossier de preuve à livrer

Une livraison qualifiée comporte `manifest.json`, inventaire des sources, liste des pertes, références API utilisées, décisions d'adaptation, cas et sorties de référence, résultats comparés, contrôles de données, empreintes des artefacts, documentation d'exploitation et écarts résiduels. Les chemins suivent une convention stable ; les preuves indiquent qui, quoi, quand et sur quelle configuration.

Le registre fonctionne pour un pilote, une version de runtime et chaque nouvelle cible. Une mise à jour de compilateur qui change les résultats remet les preuves concernées en statut à requalifier. Les modèles fournis dans `examples/` montrent les champs minimums ; ils ne réalisent ni import, ni analyse WLangage, ni test différentiel.
