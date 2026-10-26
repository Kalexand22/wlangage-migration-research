# Reprendre les sources et exécuter le WLangage

Date de recherche : 26 octobre 2026. Ce chapitre décrit une architecture à développer, pas un compilateur déjà opérationnel. Aucun projet client, fichier natif, export Git ou exécutable de référence n'a été fourni. Les compatibilités et taux de reprise doivent donc être mesurés pendant les prototypes.

## 1. Le contrat de migration à viser

Le produit doit accepter le WLangage d'origine comme langage de développement permanent. Un développeur doit retrouver ses procédures, noms de champs, traitements et points d'arrêt, même si le moteur génère ensuite du C#, du JavaScript ou du code machine. Les fichiers générés sont des artefacts reconstruisibles. Ils ne deviennent pas les sources que l'équipe doit maintenir.

Il faut contractualiser séparément cinq propriétés :

| Propriété | Signification mesurable | Preuve attendue |
|---|---|---|
| Conservation textuelle | Les blocs WLangage importés gardent leurs octets ou une transformation d'encodage explicitement déclarée | Empreintes avant/après, diff consultable |
| Acceptation syntaxique | Toutes les constructions rencontrées sont reconnues dans le profil choisi | Rapport par fichier, traitement et construction |
| Compatibilité sémantique | Calculs, mutations, conversions et erreurs produisent les résultats attendus | Tests différentiels sur moteur de référence |
| Compatibilité de plateforme | Les services UI, données, système et intégrations existent pour la cible | Matrice API × signature × cible × version |
| Compatibilité observable | Le parcours utilisateur et ses effets métier restent équivalents | Scénarios, événements, données, documents et captures comparés |

La compilation sans erreur établit seulement la deuxième propriété. Une fonction remplacée par une coquille vide ne constitue jamais une compatibilité. Un résultat partiel doit rester explicite : « importé », « analysé », « exécutable avec adaptateur », « vérifié », « bloquant ».

PC SOFT distingue lui-même l'exécution du langage et les fonctionnalités du framework dans une explication historique du fonctionnement de son moteur. Cela confirme la nécessité de traiter ces deux chantiers séparément ; cette description de 2010 ne constitue pas une spécification du runtime actuel. [Source : PC SOFT, compilation, framework et JITc](https://blogs.pcsoft.fr/fr/compilation-wlangage-framework-jitc/7/read.awp).

## 2. Les sources disponibles et leurs limites

Les brochures officielles des versions 25 et 2024 indiquent que les projets peuvent être enregistrés pour Git avec du code texte et des éléments structurés dans un format hybride présenté comme du YAML. Elles mentionnent notamment projets, fenêtres, pages, états, classes et collections de procédures. Cette possibilité est un point d'entrée crédible pour un importeur ; elle ne démontre ni que tout le contenu est transparent, ni que le schéma est ouvert et stable. [Sources : brochure WINDEV 25](https://www.pcsoft-windev-webdev.com/brochureWD25.pdf), [brochure WINDEV 2024](https://www.pcsoft-windev-webdev.com/brochureWD2024.pdf).

| Élément à récupérer | Contenu nécessaire | Traitement de migration proposé |
|---|---|---|
| Projet et configurations | Éléments inclus, cibles, options de compilation, initialisation, langues | Import du manifeste, résolution des références, profil de compatibilité |
| Procédures globales et locales | Signatures, attributs, code, commentaires, ordre de déclaration | Analyse WLangage avec contexte de déclaration |
| Classes et structures | Membres, méthodes, propriétés, héritage, constantes | Graphe de types et règles d'affectation |
| Fenêtres et fenêtres internes | Arbre de champs, noms, dimensions, styles, événements | Modèle UI indépendant du moteur de rendu |
| Pages et modèles WEBDEV | Contrôles, zones, code serveur/navigateur, AJAX, ressources | Deux contextes d'exécution distincts et liaisons contrôlées |
| États et modèles d'états | Blocs, ruptures, ancrages, calculs, événements, polices | Modèle documentaire dédié ; aucune assimilation à une simple page HTML |
| Analyse de données | Tables, rubriques, clés, contraintes, liaisons, paramètres HFSQL | Import complet ou extraction contrôlée avec validation croisée |
| Requêtes | SQL, paramètres, métadonnées, relations avec les champs | AST SQL et description de résultat ; conserver le dialecte d'origine |
| Composants internes | Sources et métadonnées, dépendances et visibilité | Import récursif, espace de noms explicite |
| Composants externes binaires | Contrat public et droits d'utilisation | Source demandée au détenteur, remplacement ou pont isolé ; ne pas annoncer leur recompilation |
| Ressources | Images, icônes, traductions, modèles, sons, styles, fichiers embarqués | Copie déterministe avec empreinte, provenance et licence |
| Interopérations natives | DLL, COM, .NET, Java/Kotlin, Objective-C/Swift, scripts | Inventaire ABI et architecture, puis adaptateur spécifique |
| Tests et scénarios | Jeux de données, assertions et parcours utilisateur | Import lorsque le format le permet ; sinon reconstruction validée |
| Paramètres de génération | Manifestes, permissions, signature, installation, services | Traduction vers la chaîne de fabrication choisie |

Cette liste est un contrat d'inventaire. Elle ne prétend pas que chaque catégorie possède un export textuel intégral.

### Sources anciennes ou natives

Commencer par une copie immuable du projet complet, de ses dépendances et de la version exacte de l'IDE. Ne jamais faire convertir l'unique exemplaire d'un projet : une montée de version peut rendre le retour dans l'ancienne version difficile ou impossible.

Le chemin privilégié est d'ouvrir une copie dans une installation autorisée de la version source, puis, lorsque nécessaire, dans une version permettant l'enregistrement texte. Produire un export contrôlé et reconstruire l'application avec l'outil d'origine pour vérifier que l'opération d'export n'a pas modifié son comportement. Les anciennes versions, les dépendances manquantes et les formats non exportables deviennent des cas de diagnostic séparés.

Un export de code seul ne suffit pas à reconstruire les fenêtres, l'analyse et les états. L'importeur doit refuser une migration déclarée complète si ces éléments restent absents. Il ne faut pas déduire un format de fichier uniquement de son extension : le contenu, la version et le mode de sauvegarde déterminent le parseur. La lecture de formats binaires propriétaires, si elle est envisagée, nécessite une étude technique et juridique distincte ; ce chapitre n'en suppose pas la faisabilité.

### Parcours d'import recommandé

1. **Inventorier sans exécuter** : fichiers, tailles, empreintes, type détecté, encodage, liens et références. Contrôler les chemins sortant du projet et les archives anormalement volumineuses.
2. **Identifier le contexte** : produit, version/build, options effectives du projet et surcharges locales, cible, architecture 32/64 bits, langues, alphabet, fuseau et dépendances.
3. **Constituer un paquet d'évidence** : copie du projet, export texte, description de l'analyse, liste des ressources, dépendances, exécutable et jeux de référence si disponibles. Les secrets sont des références externes, jamais des valeurs publiées.
4. **Analyser les conteneurs** : lire chaque élément via un adaptateur de format versionné. Préserver les propriétés inconnues et les portions opaques ; ne pas les supprimer au prochain enregistrement.
5. **Extraire les blocs WLangage** : pour chacun, conserver fichier, objet, événement, position dans le conteneur, encodage et empreinte.
6. **Résoudre le graphe** : dépendances entre classes, procédures, champs, requêtes, tables, composants et ressources. Toute référence manquante reçoit un diagnostic localisé.
7. **Produire un bilan** : couverture par catégories, API utilisées, constructions dynamiques, incompatibilités de cible, interventions estimées et blocages.
8. **Créer un espace de travail séparé** : sources originales en lecture seule, représentation normalisée, paramètres de migration et artefacts générés dans des répertoires distincts.
9. **Compiler puis comparer** : la génération est interdite pour les configurations comportant un blocage non résolu. Un mode de démonstration peut afficher les écrans partiels, avec mention visible de son périmètre.

L'interface d'import doit proposer une explication actionnable par problème : « le composant X n'est disponible qu'en binaire ; fournir ses sources, utiliser le pont Windows ou sélectionner un remplacement ». Elle doit conserver la décision dans un fichier versionné, avec son auteur et les éléments concernés.

## 3. Un profil de compatibilité réellement reproductible

Deux projets de même version peuvent ne pas interpréter le même texte de la même façon. La documentation de l'onglet Compilation décrit des réglages portant notamment sur la portée des variables, la copie des tableaux, les types nullables, les sources de données et l'évaluation des booléens. Les réglages peuvent aussi être surchargés sur certains éléments. Les enregistrer est une condition de migration. [Source : description du projet, onglet Compilation](https://doc.pcsoft.fr/?9500218=).

Le manifeste suivant est **une proposition de format**, avec des valeurs d'exemple à résoudre à l'import ; ce n'est pas un fichier PC SOFT ni une configuration déjà testée :

```yaml
compatibility:
  product: WINDEV
  version: "a-renseigner"
  build: "a-renseigner"
  source_target: windows-x64
  generation_target: windows-x64
  language_vocabulary: [fr, en]
  boolean_evaluation: preserve-imported-setting
  local_scope: preserve-imported-setting
  array_assignment: preserve-imported-setting
  nullable_types: preserve-imported-setting
  datasource_naming: preserve-imported-setting
  string_encoding: preserve-imported-setting
  locale: fr-FR
  time_zone: Europe/Paris
  unresolved_settings_are_errors: true
```

Conserver la provenance de chaque réglage : « lu », « déduit d'un export identifié », « confirmé par le développeur » ou « encore inconnu ». Une valeur moderne par défaut ne remplace jamais silencieusement une valeur historique inconnue. Les écarts entre cible source et cible demandée deviennent des modifications de comportement à accepter dans le dossier de migration.

Il faut séparer le **mode compatibilité**, qui reproduit les résultats convenus, et les options de modernisation sélectionnables. L'IDE peut recommander une nouvelle pratique, mais son activation produit un diff, un plan de tests et une modification versionnée du profil.

## 4. Frontend WLangage : couverture à implémenter

Il faut une grammaire construite à partir de la documentation, des exemples autorisés et de corpus de projets. Une table de remplacement de mots-clés ou de noms de fonctions est insuffisante. Le parseur doit accepter les syntaxes historiques rencontrées, diagnostiquer les ambiguïtés et tolérer un fichier temporairement incomplet dans l'éditeur.

| Groupe | Couverture attendue du frontend |
|---|---|
| Lexique | Vocabulaires français et anglais, accents des mots-clés, identificateurs, constantes et commentaires |
| Mise en forme | Retours à la ligne significatifs, continuations, indentation, chaînes multilignes et délimiteurs |
| Expressions | Priorités, associativité, appels, accès membres/propriétés, opérateurs unaires et binaires |
| Affectations | Affectation de valeur, référence, opérations composées, incrémentations et affectations multiples si rencontrées |
| Déclarations | Typage explicite, inférence, constantes, types composés et déclarations externes |
| Contrôle | SI, SELON, boucles, POUR TOUT, sorties, retours et instructions conditionnelles |
| Procédures | Locales/globales/internes, paramètres optionnels, par référence/par valeur, résultat, surcharge et attributs |
| POO | Classes, structures, héritage, constructeurs, destructeurs, visibilité, méthodes et propriétés |
| Collections | Tableaux simples/multidimensionnels/associatifs, listes, piles, files, parcours et mutation |
| Dynamique | Variant, indirection, introspection, appels par nom et code construit à l'exécution |
| Erreurs | Gestion automatique configurée, blocs d'exception, propagation et informations d'erreur |
| Compilation | Conditions de compilation, configurations, directives et attributs dépendant de la cible |
| Données | Références à l'analyse, fichiers/rubriques, sources de données et paramètres de requêtes |
| UI | Noms de fenêtres/champs, propriétés, traitements implicites et variables de contexte |
| Concurrence | Threads, tâches, temporisations, callbacks et procédures asynchrones/réactives rencontrées |
| Langages embarqués | Blocs natifs et code SQL, XML/JSON/HTML ; parsers distincts selon le contexte |

Les équivalents français/anglais convergent vers le même identifiant sémantique interne, tout en conservant le lexème d'origine. Traduire automatiquement les identificateurs ou le texte d'un code construit dynamiquement altérerait les appels par nom. Pour la syntaxe classique et préfixée, la résolution doit partager la même définition de fonction lorsque les contrats sont effectivement équivalents ; elle doit aussi reconnaître les divergences de signatures et de disponibilité.

### Arbre concret conservant le texte, AST et IR

Construire trois représentations complémentaires :

- Un **arbre concret conservant le texte** garde commentaires, espaces, encodage, lexèmes et zones inconnues. Sans modification, sa réémission doit rendre le même contenu.
- Un **AST sémantique** relie symboles, types, traitements, signatures, effets et profils. Les références aux éléments visuels y sont explicites.
- Une **représentation intermédiaire (IR)** décrit les opérations exécutables indépendamment du backend : conversion WLangage, référence vers une cellule, chargement de propriété UI, appel de fonction de compatibilité et branchement.

Le runtime reçoit des opérations WLangage précises, pas des comportements implicites du langage hôte. Une conversion, une égalité de chaînes ou un accès de tableau est un contrat à implémenter. Un backend peut ensuite optimiser une opération si une preuve et les tests établissent l'équivalence.

Ne pas imposer la normalisation du fichier d'origine dès son import. Une première version peut traiter les exports comme une source externe en lecture, avec fichiers de décisions adjacents. Une modification visuelle ultérieure peut écrire un format interne ouvert. Le réexport complet vers WINDEV est un objectif distinct : il exige une preuve de réouverture et de fonctionnement pour chaque type d'élément et chaque version.

## 5. Les règles sémantiques qui déterminent la fidélité

Les points ci-dessous sont des **exigences de conception et de caractérisation**. Lorsque le contrat exact n'est pas établi par la documentation ou le corpus, on crée un test de référence avant de choisir le comportement.

### 5.1 Nombres, conversions et valeurs absentes

Définir des types WLangage pour les entiers avec taille et signe, les réels, les monétaires et les numériques décimaux. Documenter dépassement, troncature, arrondi, division, modulo et conversion en chaîne. L'exigence est l'absence de perte supplémentaire par rapport au type, aux arrondis et au profil de référence ; préserver aussi les limites et troncatures du programme d'origine. Choisir automatiquement le `double` du backend serait une erreur d'architecture.

Tester les conversions implicites à l'affectation, à l'appel et au retour. Une expression évaluée en variant peut suivre un autre chemin qu'une variable statiquement typée. Distinguer valeur par défaut, chaîne vide, date vide, objet non affecté, variable non initialisée et NULL. Tester leur comportement dans les comparaisons, les conditions, les paramètres optionnels et les champs liés à une base.

### 5.2 Chaînes, encodages et comparaisons

La documentation distingue plusieurs formes de chaînes et des fonctions de conversion ANSI/OEM/Unicode. Elle indique aussi qu'un type de chaîne Unicode à taille fixée peut être remplacé par une chaîne ordinaire sur certaines cibles. La compatibilité doit donc porter sur une cible précise. [Sources : manipulation des chaînes](https://doc.pcsoft.fr/?3024020=), [Chaîne Unicode sur](https://doc.pcsoft.fr/?1000024447=).

Le runtime doit conserver les informations d'encodage nécessaires, distinguer texte et buffer et caractériser taille en octets/caractères, caractères composés, caractères hors du plan de base, zéros embarqués, espaces de remplissage et fins de ligne. Les tris et comparaisons dépendent aussi des options linguistiques. Une normalisation Unicode automatique peut modifier des clés ou empreintes ; elle doit être explicite.

### 5.3 Dates, heures et durées

Séparer date civile, heure civile, date-heure, durée et instant UTC. Caractériser formats compacts, dates vides, validation, changement de mois, années bissextiles, précision et conversions. Une fonction comme PremierJourDuMois accepte des chaînes compactes et des types Date/DateHeure : ce contrat exige des surcharges de compatibilité. [Source : PremierJourDuMois](https://doc.pcsoft.fr/fr-FR/?1000019417=&product=WB).

Les tests doivent fixer l'horloge, la langue et le fuseau. Pour les applications distribuées, conserver les comportements historiques nécessaires puis proposer une modernisation explicite des fuseaux et de la sérialisation.

### 5.4 Booléens et ordre d'évaluation

Les opérateurs logiques possèdent des variantes optimisées, et une option peut rendre ce mode actif pour les formes usuelles depuis la version 2024. La documentation précise également une priorité identique de ET et OU dans le langage, différente du contexte SQL. Reprendre la grammaire et la configuration exactes évite d'importer involontairement les règles du backend. [Source : opérateurs logiques](https://doc.pcsoft.fr/?1512003=).

```text
// Cas de caractérisation conceptuel, à exécuter dans le projet de référence.
SI ConditionA() ET ConditionB() ALORS
    Traiter()
FIN
```

Le test enregistre les appels et effets de `ConditionA` et `ConditionB`, y compris si la première condition est fausse. La valeur finale seule ne détecte pas une différence d'évaluation.

### 5.5 Tableaux, collections et références

Les exemples officiels d'ajout et de suppression utilisent des indices commençant à 1 et décrivent des effets sur la taille et les erreurs d'indice. Ne pas propager les indices 0 du langage cible. [Sources : TableauAjouteTrié](https://doc.pcsoft.fr/fr-FR/?1000017013=), [Tableau.Supprime](https://doc.pcsoft.fr/fr-FR/?1000024314=).

Caractériser copies et références, tableaux fixes/dynamiques, dimensions, indices invalides, ordre de parcours, suppression de l'élément courant, doublons des tableaux associatifs et invalidation d'un élément passé par référence. Pour chaque collection, définir son interaction avec les threads, la sérialisation et les membres de classes.

### 5.6 Paramètres, portée et durée de vie

Le tutoriel officiel décrit le passage par référence comme comportement usuel et le mot-clé LOCAL pour obtenir une copie. Il faut préserver cette distinction. Caractériser séparément variables affectables, éléments de tableaux, propriétés, constantes et expressions : création éventuelle d'un temporaire, conversions et possibilités de propagation des mutations. [Source : procédures, paramètres et références](https://aide.pcsoft.fr/?1410087236=&name=annexe_7_les_procedures).

Le moteur doit représenter une référence par une cellule ou un accès lecture/écriture, avec durée de vie contrôlée. Distinguer variables de projet, de collection, de fenêtre/page/état, locales, de classe et contexte de champ. Les captures de procédures internes et le moment de destruction des objets demandent des tests séparés. La documentation confirme que la visibilité dépend du lieu de déclaration. [Source : portée des variables](https://doc.pcsoft.fr/fr-FR/?1514088=).

### 5.7 Classes, objets, propriétés et champs

Établir les règles d'héritage, résolution de surcharge, construction/destruction, affectation, identité, conversion, méthode virtuelle et visibilité. Les objets exposés par un composant externe peuvent demander un adaptateur plutôt qu'une instanciation directe.

Un champ n'est pas une variable ordinaire. La documentation distingue l'opérateur de référence `<-` et l'affectation `=`, cette dernière transférant une valeur. Le runtime doit préserver cette différence et les effets sur les événements. [Source : type Champ](https://doc.pcsoft.fr/fr-FR/?1000020967=).

Une propriété doit avoir un contrat : type, cibles, lecture/écriture, valeur par défaut, effet immédiat/différé, invalidation du rendu et événements induits. Une table générique de propriétés sans ces règles ne suffit pas à reproduire l'application.

### 5.8 Événements et contexte implicite

Le compilateur associe un bloc de code à un type de traitement et un contexte : projet, fenêtre, champ, page ou état. Le runtime doit établir les variables de contexte, l'ordre d'initialisation, les événements imbriqués, les retours annulant une action et la durée de vie des fenêtres.

Créer un ordonnanceur d'événements journalisable. Une affectation programmée peut avoir un effet différent d'une saisie utilisateur ; un callback réseau peut revenir après la fermeture d'une fenêtre. Les scénarios doivent tester ces cas. Pour WEBDEV, séparer serveur et navigateur : aucun accès direct au disque serveur ni secret ne doit être déplacé dans le navigateur par simple traduction.

### 5.9 HFSQL dans la sémantique du langage

Les symboles provenant de l'analyse constituent une partie du contexte de compilation. Une expression `Client.Nom` peut désigner une rubrique, avec un buffer courant et un état de lecture associés. Les fonctions H* modifient potentiellement curseur, filtre, erreur et transaction ; les convertir en requêtes SQL isolées détruirait ces relations.

Le compilateur doit typer les fichiers, rubriques, clés, requêtes et sources de données. Le runtime délègue ensuite à un fournisseur de données compatible. Les requêtes peuvent avoir des limitations propres à une cible, notamment lorsque leur SQL contient du WLangage. [Source : Source.ExécuteRequêteSQL](https://doc.pcsoft.fr/fr-fr/?1000024948=).

### 5.10 Erreurs et exceptions

La documentation présente des mécanismes d'exception automatiques, généraux et spécifiques. Le comportement peut donc provenir du code et des paramètres de l'élément. [Source : gestion des erreurs de programmation](https://doc.pcsoft.fr/?3034004=).

Maintenir l'état d'erreur compatible au niveau correct : procédure, thread, connexion ou opération suivant le contrat. Préserver codes, message utile, emplacement source, reprise et effets transactionnels. Une exception du langage hôte doit être traduite à la frontière ; elle ne doit pas traverser arbitrairement le code WLangage. La nouvelle plateforme peut ajouter un identifiant de diagnostic stable, sans changer les valeurs sur lesquelles le programme existant branche.

### 5.11 Indirection, introspection et compilation dynamique

Les appels par nom et la construction de code à l'exécution imposent de conserver une table de symboles runtime et des métadonnées. L'analyse statique ne peut pas prouver qu'aucun autre nom sera construit. Elle doit signaler les zones dynamiques et enrichir l'inventaire avec des traces de scénarios, en précisant que ces traces ne prouvent pas une couverture complète.

L'éditeur de code intégrable de PC SOFT possède des paramètres de fonctions autorisées/interdites, ce qui fournit un exemple concret de contrôle de la surface d'exécution dynamique. Notre proposition est d'utiliser le même frontend pour compilation normale et dynamique, avec budget de temps/mémoire et capacités configurables. [Source : manipulation du champ Éditeur de code](https://doc.pcsoft.fr/?1410087305=).

Ne pas annoncer la compilation dynamique sur une cible qui l'interdit ou ne la permet pas avec les mêmes propriétés. Sur les cibles AOT, prévoir une liste de modules précompilés lorsque le besoin s'y prête ou déclarer le blocage. Un interpréteur embarqué est une option technique à étudier avec les contraintes du système et de distribution.

### 5.12 Threads, tâches et interopération

Spécifier les partages de variables, contextes de données, sections critiques, annulation, temporisations et retour sur le thread UI. Pour les opérations asynchrones, conserver ordre observable, propagation d'erreur et durée de vie des captures. Les threads ou processus du backend sont des moyens d'implémentation : ils ne définissent pas automatiquement le contrat WLangage.

L'interopération exige des contrats séparés pour tailles numériques, encodage, propriété de mémoire, callbacks, exceptions et architecture. Les docs d'intégration Java et .NET montrent des conversions et limites propres à ces passerelles ; elles ne permettent pas de promettre qu'un code natif sera portable sans adaptation. [Sources : saisir du code Java](https://doc.pcsoft.fr/fr-FR/?9000011=), [utiliser des assemblages .NET](https://doc.pcsoft.fr/fr-FR/?2012002=).

## 6. Exécution, diagnostics et expérience de débogage

La recommandation est un frontend commun et une couche de compatibilité explicitement versionnée. Un interpréteur d'AST ou une petite VM facilite d'abord les tests de sémantique et le débogage. Un backend compilé peut être développé ensuite pour les cibles et chemins validés. Le backend retenu par l'architecture générale devra passer exactement la même suite de conformité.

Chaque instruction générée garde un identifiant stable relié au fichier source, objet et traitement. La table de correspondance doit couvrir une génération un-vers-plusieurs et une macro/directive, avec positions en octets et conversion vers les unités du protocole d'éditeur. L'utilisateur pose un point d'arrêt dans « Clic de BTN_Valider », inspecte les variables WLangage et voit une pile WLangage, même si le moteur exécute du code généré.

Utiliser un serveur de langage commun via LSP et un adaptateur de débogage via DAP permet de mutualiser navigation, complétion, diagnostics et débogage entre l'IDE principal et d'autres éditeurs. Ces protocoles standardisent les échanges ; ils ne fournissent ni analyseur WLangage ni runtime. [Sources : Language Server Protocol](https://microsoft.github.io/language-server-protocol/), [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/).

Diagnostics proposés :

| Code de conception | Situation | Résolution attendue |
|---|---|---|
| IMP001 | Format/segment inconnu | Préserver le segment ; demander un export identifié |
| IMP002 | Ressource ou composant absent | Afficher les références et chemins recherchés |
| SEM001 | Réglage sémantique indéterminé | Résoudre via export, projet source ou confirmation documentée |
| API001 | Signature absente sur la cible | Proposer adaptateur, cible compatible ou remplacement |
| DYN001 | Nom construit dynamiquement | Afficher l'incertitude et les scénarios d'instrumentation |
| UI001 | Propriété visuelle sans équivalent | Afficher une différence localisée, jamais la supprimer |
| DB001 | Sémantique de curseur non assurée | Exiger un fournisseur ou un scénario de validation |
| GEN001 | Backend incapable d'une opération | Bloquer l'artefact concerné et proposer une autre stratégie |

## 7. Protocole de conformité et critères de sortie

Construire un harnais qui exécute le même petit programme dans une installation de référence autorisée et dans le nouveau moteur. Les programmes de caractérisation sont écrits pour l'étude ; on ne copie pas le code propriétaire du moteur. Conserver version, profil, résultats, erreurs et traces d'effets. Les cas non déterministes utilisent une horloge et des données fixées, ou des assertions d'ordre/intervalle explicitement convenues.

| Famille de tests | Cas minimaux nécessaires |
|---|---|
| Lexique | FR/EN, accents, commentaires, littéraux, fichier tronqué, erreurs localisées |
| Opérateurs | Priorité, associativité, courts-circuits, effets secondaires, null |
| Nombres | Limites, débordements, arrondis, divisions, conversions chaîne/nombre |
| Chaînes | ANSI/Unicode, taille, découpe, accents, zéros, caractères composés |
| Dates | Vide, invalide, bissextile, fins de mois, durée, changement d'heure |
| Paramètres | Référence/LOCAL, expression, constante, tableau, alias partagé |
| Collections | Indices, dimensions, doublons, copies, mutation pendant parcours |
| POO | Constructeurs, héritage, propriétés, identité, affectation, destruction |
| Portées | Projet/fenêtre/champ, masquage, capture, réentrée, fermeture |
| Dynamique | Nom construit, symbole absent, introspection, code valide/invalide |
| Erreurs | Retour faux, exception, gestion automatique, reprise, état d'erreur |
| Concurrence | Donnée partagée, thread UI, annulation, callback après destruction |
| Données | Buffer courant, filtre, recherche, transaction, clés, null, verrou |
| Événements | Initialisation, focus, saisie, validation, fermeture, événements imbriqués |
| Interopération | Conversion, encodage, callback, architecture, mémoire, exception |
| Génération | Profil/cible/version, build reproductible, artefacts et symboles |

Ajouter des tests génératifs pour les expressions et des tests de mutation pour vérifier que la suite détecte un changement de priorité, d'indice ou de règle de copie. Les programmes générés doivent rester dans un sous-ensemble défini dont on connaît le sens ; des programmes aléatoires invalides ne donnent pas une mesure de conformité utile.

Mesurer séparément : blocs de code importés, constructions syntaxiques rencontrées, signatures appelées, propriétés utilisées, scénarios passés et profils vérifiés. Ne pas publier un pourcentage global mêlant ces unités. Publier les dénominateurs : « 173 signatures vérifiées sur les 221 rencontrées dans trois applications », plutôt que « compatible à 78 % avec WINDEV ».

Trois portes de sortie sont recommandées :

1. **Import fidèle** : aucun élément perdu, inconnus conservés et signalés, provenance et empreintes disponibles, projet source inchangé.
2. **Noyau exécutable** : frontend, types, références, erreurs, événements et API du pilote passent les tests différentiels ; toutes les incompatibilités restantes sont visibles.
3. **Application migrée** : parcours métier, données, documents, périphériques et performances du périmètre accepté passent leur recette sur chaque cible. Une nouvelle version du runtime rejoue ces preuves.

## 8. Sources et réserves de recherche

Les liens de ce chapitre sont des sources primaires PC SOFT ou Microsoft. Plusieurs ouvertures directes du domaine de documentation ont renvoyé HTTP 403 pendant la recherche ; les passages utilisés ont alors été consultés via leur indexation web. Une URL disponible et un extrait indexé ne prouvent pas que la page décrit le build exact d'un futur projet client. Le pilote devra figer la documentation de la version effectivement migrée et consulter son aide locale autorisée.

Les sources documentaires établissent l'existence des comportements cités. Les structures de manifeste, algorithmes d'import, AST/IR, diagnostics, profils, stratégies runtime et critères de conformité sont des recommandations originales de cette étude. Aucune affirmation de compatibilité avec des fichiers binaires, de réexport natif intégral ou de couverture de tout le WLangage ne peut être déduite de ce document seul.
