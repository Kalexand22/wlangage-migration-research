# Reprendre les sources et exécuter le WLangage

Date de recherche : 26 octobre 2026. Ce chapitre décrit une architecture à développer, pas un compilateur déjà opérationnel. Aucun projet client, fichier natif, export Git ou exécutable de référence n'a été fourni. Les compatibilités et taux de reprise doivent donc être mesurés pendant les prototypes.

**Contrainte active : aucune utilisation d'outil ou de composant PC SOFT dans la chaîne proposée.** L'import, la génération, le débogage, les tests, la migration des données et l'exploitation doivent fonctionner sans IDE, GDS, utilitaire, compilateur, DLL, SDK, pilote, runtime ni serveur HFSQL de PC SOFT. Un pont distant ou une exécution demandée au client ne contourne pas cette règle : aucun oracle WINDEV ne sera lancé dans ce workflow. Les documents publics, fichiers source, exports, profils, fixtures et traces **déjà disponibles**, avec leur provenance, restent des matériaux d'étude statiques. Les dépendances tierces et leurs dépendances transitives doivent également être contrôlées.

Le maintien du WLangage par une implémentation entièrement indépendante reste une hypothèse technique et juridique à qualifier. Les limites de lecture des formats et l'absence d'observations d'exécution réduisent la portée des affirmations possibles ; elles n'empêchent pas de développer un prototype indépendant sur les règles documentées.

## 1. Le contrat de migration à viser

Le produit doit accepter le WLangage d'origine comme langage de développement permanent. Un développeur doit retrouver ses procédures, noms de champs, traitements et points d'arrêt, même si le moteur génère ensuite du C#, du JavaScript ou du code machine. Les fichiers générés sont des artefacts reconstruisibles. Ils ne deviennent pas les sources que l'équipe doit maintenir.

Il faut contractualiser séparément cinq propriétés :

| Propriété | Signification mesurable | Preuve attendue |
|---|---|---|
| Conservation textuelle | Les blocs WLangage importés gardent leurs octets ou une transformation d'encodage explicitement déclarée | Empreintes avant/après, diff consultable |
| Acceptation syntaxique | Toutes les constructions rencontrées sont reconnues dans le profil choisi | Rapport par fichier, traitement et construction |
| Compatibilité sémantique | Calculs, mutations, conversions et erreurs satisfont les contrats établis pour le périmètre retenu | Tests indépendants sur règles documentées et comparaison avec fixtures/traces déjà disponibles ; règles non établies laissées inconnues |
| Compatibilité de plateforme | Les services UI, données, système et intégrations existent pour la cible | Matrice API × signature × cible × version |
| Compatibilité observable | Le parcours utilisateur et ses effets métier restent équivalents | Scénarios, événements, données, documents et captures comparés |

La compilation sans erreur établit seulement la deuxième propriété. Une fonction remplacée par une coquille vide ne constitue jamais une compatibilité. Un résultat partiel doit rester explicite : « importé », « analysé », « exécutable avec adaptateur », « vérifié », « bloquant ».

PC SOFT distingue lui-même l'exécution du langage et les fonctionnalités du framework dans une explication historique du fonctionnement de son moteur. Cela confirme la nécessité de traiter ces deux chantiers séparément ; cette description de 2010 ne constitue pas une spécification du runtime actuel. [Source : PC SOFT, compilation, framework et JITc](https://blogs.pcsoft.fr/fr/compilation-wlangage-framework-jitc/7/read.awp).

## 2. Les sources disponibles et leurs limites

Les brochures officielles des versions 25 et 2024 indiquent que les projets peuvent être enregistrés pour Git avec du code texte et des éléments structurés dans un format hybride présenté comme du YAML. Elles mentionnent notamment projets, fenêtres, pages, états, classes et collections de procédures. Cette possibilité est un point d'entrée crédible pour un importeur ; elle ne démontre ni que tout le contenu est transparent, ni que le schéma est ouvert et stable. [Sources : brochure WINDEV 25](https://www.pcsoft-windev-webdev.com/brochureWD25.pdf), [brochure WINDEV 2024](https://www.pcsoft-windev-webdev.com/brochureWD2024.pdf).

La documentation technique du partage Git indique une version minimale **25** et exige que le projet ne soit pas dans le **GDS/SCM** pour suivre ce parcours. Elle précise que le changement de format ne change pas les extensions : le code et les principales caractéristiques des fenêtres/champs sont textuels, tandis que des propriétés avancées restent binaires. Le format de sauvegarde peut aussi être vérifié par élément. Cette précondition concerne le partage Git documenté ; elle ne prouve pas que tout usage d'un format texte serait impossible dans le GDS. [Source : PC SOFT, Share your projects via Git, prérequis et préparation](https://doc.windev.com/en-US/?9500230=).

Ces indications expliquent la provenance possible de fichiers déjà fournis. Elles ne définissent aucune étape de conversion, d'export ou de vérification dans un outil PC SOFT pour notre solution. Si les éléments nécessaires ne sont pas déjà disponibles dans un format lisible indépendamment, l'import signale ce manque ; il ne déclenche pas l'ancien IDE et ne délègue pas cette opération au client.

Conséquence de conception : l'import doit relever, pour chaque élément, son mode de sauvegarde effectif, la part lisible et les segments binaires résiduels. Un fichier exporté en mode texte n'est pas déclaré entièrement interprété sur ce seul critère. Les originaux et segments opaques restent conservés ; leur impact est rapporté, puis la génération du périmètre affecté est bloquée tant que l'équivalence nécessaire n'est pas établie.

| Élément à récupérer | Contenu nécessaire | Traitement de migration proposé |
|---|---|---|
| Projet et configurations | Éléments inclus, cibles, options de compilation, initialisation, langues | Import du manifeste, résolution des références, profil de compatibilité |
| Procédures globales et locales | Signatures, attributs, code, commentaires, ordre de déclaration | Analyse WLangage avec contexte de déclaration |
| Classes et structures | Membres, méthodes, propriétés, héritage, constantes | Graphe de types et règles d'affectation |
| Fenêtres et fenêtres internes | Arbre de champs, noms, dimensions, styles, événements | Modèle UI indépendant du moteur de rendu |
| Pages et modèles WEBDEV | Contrôles, zones, code serveur/navigateur, AJAX, ressources | Deux contextes d'exécution distincts et liaisons contrôlées |
| États et modèles d'états | Blocs, ruptures, ancrages, calculs, événements, polices | Modèle documentaire dédié ; aucune assimilation à une simple page HTML |
| Analyse de données | Tables, rubriques, clés, contraintes, liaisons, paramètres HFSQL documentés | Lecture indépendante des fichiers/descriptions déjà fournis ; conversion vers modèle PostgreSQL ; inconnu conservé et bloquant |
| Requêtes | SQL, paramètres, métadonnées, relations avec les champs | AST SQL et description de résultat ; conserver le dialecte d'origine |
| Composants internes | Sources et métadonnées, dépendances et visibilité | Import récursif, espace de noms explicite |
| Composants externes binaires | Contrat fourni, provenance et dépendances | Sources déjà disponibles ou remplacement indépendant ; aucun binaire compilé nécessitant un composant PC SOFT n'est chargé |
| Ressources | Images, icônes, traductions, modèles, sons, styles, fichiers embarqués | Copie déterministe avec empreinte, provenance et licence |
| Interopérations natives | DLL tierces, COM, .NET, Java/Kotlin, Objective-C/Swift, scripts | Inventaire ABI et architecture ; adaptateur indépendant après exclusion de toute dépendance PC SOFT directe ou transitive |
| Tests et scénarios | Jeux de données, assertions et parcours utilisateur | Import lorsque le format le permet ; sinon reconstruction validée |
| Paramètres de génération | Manifestes, permissions, signature, installation, services | Traduction vers la chaîne de fabrication choisie |

Cette liste est un contrat d'inventaire. Elle ne prétend pas que chaque catégorie possède un export textuel intégral.

### Sources anciennes ou natives

Commencer par une copie immuable des fichiers déjà fournis et de leurs métadonnées de provenance. Aucune installation, ouverture, conversion ou recompilation avec un outil PC SOFT n'entre dans le parcours. Les fichiers originaux restent inchangés, même lorsqu'une lecture indépendante du contenu ne peut pas encore être réalisée.

Il faut distinguer le **millésime commercial**, l'**update** et le **build observé**. Le changelog officiel 2026 donne un cas concret historique : des fenêtres ouvertes avec « 2026 Update 2 » ne peuvent plus être ouvertes avec une version 2026 antérieure. Le même millésime ne garantit donc pas une identité de format. Cette source situe l'update dans la famille `312xxx` ; elle ne fournit pas le build exact d'un patrimoine non examiné. Relever celui-ci uniquement dans les métadonnées ou preuves déjà disponibles ; sinon conserver la valeur inconnue. [Source : mise à jour WINDEV 2026, rubrique Update 2](https://doc.pcsoft.fr/fr-FR/?9000050=&name=windev_2026_update).

Le chemin retenu est un lecteur indépendant des fichiers source ou exports existants, sélectionné par leur contenu et leur provenance. Sa faisabilité est à démontrer sur des échantillons autorisés déjà disponibles. Un ancien format non compris reste un cas de diagnostic bloquant ; une reconstruction indépendante peut être spécifiée à partir de données lisibles et d'exigences vérifiées, mais elle ne devient pas du code équivalent par hypothèse. Aucun outil ou composant PC SOFT ne sert de solution de secours.

Un export de code seul ne suffit pas à reconstruire les fenêtres, l'analyse et les états. L'importeur doit refuser une migration déclarée complète si ces éléments restent absents. Il ne faut pas déduire un format de fichier uniquement de son extension : le contenu, la version et le mode de sauvegarde déterminent le parseur. La lecture de formats binaires propriétaires, si elle est envisagée, nécessite une étude technique et juridique distincte ; ce chapitre n'en suppose pas la faisabilité.

### Parcours d'import recommandé

1. **Inventorier sans exécuter** : fichiers, tailles, empreintes, type détecté, encodage, liens et références. Contrôler les chemins sortant du projet et les archives anormalement volumineuses.
2. **Identifier le contexte** : produit, version/build, options effectives du projet et surcharges locales, cible, architecture 32/64 bits, langues, alphabet, fuseau et dépendances.
3. **Constituer un paquet d'évidence existante** : fichiers source et exports déjà fournis, descriptions de données, ressources, dépendances, profils, fixtures et traces disponibles avec leur date, auteur, contexte et intégrité. Les secrets sont des références externes, jamais des valeurs publiées. Aucun nouvel export ni relevé d'exécution dans PC SOFT n'est requis.
4. **Analyser les conteneurs** : lire chaque élément via un adaptateur de format versionné. Préserver les propriétés inconnues et les portions opaques ; ne pas les supprimer au prochain enregistrement.
5. **Extraire les blocs WLangage** : pour chacun, conserver fichier, objet, événement, position dans le conteneur, encodage et empreinte.
6. **Résoudre le graphe** : dépendances entre classes, procédures, champs, requêtes, tables, composants et ressources. Toute référence manquante reçoit un diagnostic localisé.
7. **Produire un bilan** : couverture par catégories, API utilisées, constructions dynamiques, incompatibilités de cible, interventions estimées et blocages.
8. **Créer un espace de travail séparé** : sources originales en lecture seule, représentation normalisée, paramètres de migration et artefacts générés dans des répertoires distincts.
9. **Contrôler les dépendances, compiler puis vérifier** : la génération du périmètre de production est interdite si un blocage sémantique subsiste ou si la chaîne requiert un outil/composant PC SOFT, même distant ou transitif. Les prototypes indépendants peuvent avancer sans oracle, en affichant le périmètre effectivement testé et ses inconnues.

L'interface d'import doit proposer une explication actionnable par problème : « le composant X nécessite un runtime PC SOFT interdit ; seules des sources déjà disponibles et une réimplémentation indépendante ou un remplacement peuvent lever ce blocage ». Elle conserve la décision dans un fichier versionné, avec son auteur et les éléments concernés ; elle ne propose aucun pont PC SOFT.

## 3. Un profil de compatibilité réellement reproductible

Deux projets de même version peuvent ne pas interpréter le même texte de la même façon. La documentation de l'onglet Compilation décrit des réglages portant notamment sur la portée des variables, la copie des tableaux, les types nullables, les sources de données et l'évaluation des booléens. Elle mentionne des surcharges sur certains éléments pour les options de norme de programmation ; cela ne permet pas de généraliser une surcharge à toutes les options sémantiques. Chaque possibilité de surcharge doit être vérifiée pour le réglage et le build concernés. [Source : description du projet, onglet Compilation](https://doc.pcsoft.fr/?9500218=).

Le profil doit aussi relever le **mode de passage des paramètres**. La brochure 2026 décrit un choix de mode au niveau du projet et la possibilité d'utiliser ponctuellement l'autre mode ; le mode historique par référence reste annoncé comme défaut en création de projet. Cela ne donne pas la valeur effective d'un projet importé. La disponibilité de surcharges par élément et la règle qui départage contexte appelant, élément appelé et syntaxe explicite doivent être recherchées dans les preuves existantes et la documentation, puis caractérisées dans le moteur indépendant. Elles restent inconnues si ces éléments ne suffisent pas ; aucun build PC SOFT n'est exécuté pour les lever. [Source : brochure 2026, nouveautés 133–135, page PDF 15, pages imprimées 28–29](https://fr.pcsoft-windev-webdev.com/brochure-WX2026.pdf#page=15).

Le manifeste suivant est **une proposition de format**, avec des valeurs d'exemple à résoudre à l'import ; ce n'est pas un fichier PC SOFT ni une configuration déjà testée :

```yaml
compatibility:
  product: WINDEV
  version: "a-renseigner"
  update_name: "a-renseigner"
  build: "a-renseigner"
  source_target: windows-x64
  generation_target: windows-x64
  language_vocabulary: [fr, en]
  boolean_evaluation: preserve-imported-setting
  local_scope: preserve-imported-setting
  array_assignment: preserve-imported-setting
  nullable_types: preserve-imported-setting
  datasource_naming: preserve-imported-setting
  parameter_passing:
    project_default: null
    element_overrides: []
    effective_by_context: []
    resolution_precedence: to-characterize
    provenance_status: not-observed
  string_encoding: preserve-imported-setting
  locale: fr-FR
  time_zone: Europe/Paris
  unresolved_settings_are_errors: true
```

Conserver la provenance de chaque réglage : « lu », « déduit d'un export identifié », « confirmé par le développeur » ou « encore inconnu ». Une valeur moderne par défaut ne remplace jamais silencieusement une valeur historique inconnue. Les écarts entre cible source et cible demandée deviennent des modifications de comportement à accepter dans le dossier de migration.

Pour le passage de paramètres, chaque relevé doit identifier configuration, élément, procédure, éventuel site d'appel, valeur déclarée, mode effectif, origine du réglage et preuve liée au build lorsqu'elle existe déjà. Enregistrer les surcharges présentes dans les pièces fournies, sans en inventer ni ouvrir l'IDE pour les chercher. Si leur support ou leur priorité reste inconnu, le bilan le conserve et bloque la génération concernée. L'[exemple JSON de profil](../examples/profil-migration.exemple.json) propose des emplacements distincts pour réglage projet, surcharges, contextes effectifs et provenance ; ses valeurs nulles ne constituent pas des observations.

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

Ne pas imposer la normalisation du fichier d'origine dès son import. Une première version peut traiter les exports existants comme une source externe en lecture, avec fichiers de décisions adjacents. Une modification visuelle ultérieure peut écrire un format interne ouvert. Le réexport vers WINDEV et sa vérification par réouverture sont hors du parcours retenu, puisqu'ils introduiraient un outil PC SOFT. La sortie de la nouvelle plateforme doit être indépendante et documentée.

## 5. Les règles sémantiques qui déterminent la fidélité

Les points ci-dessous sont des **exigences de conception et de caractérisation**. Chaque résultat attendu doit découler d'une règle documentaire identifiée, d'une fixture ou d'une trace déjà disponible et contextualisée. Lorsque le contrat n'est pas établi, on conserve l'inconnu et on peut tester une hypothèse de conception séparément, sans la présenter comme le comportement PC SOFT.

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
// Cas conceptuel pour le moteur indépendant ; attendu lié au profil documenté.
SI ConditionA() ET ConditionB() ALORS
    Traiter()
FIN
```

Le test enregistre les appels et effets de `ConditionA` et `ConditionB`, y compris si la première condition est fausse. La valeur finale seule ne détecte pas une différence d'évaluation.

### 5.5 Tableaux, collections et références

Les exemples officiels d'ajout et de suppression utilisent des indices commençant à 1 et décrivent des effets sur la taille et les erreurs d'indice. Ne pas propager les indices 0 du langage cible. [Sources : TableauAjouteTrié](https://doc.pcsoft.fr/fr-FR/?1000017013=), [Tableau.Supprime](https://doc.pcsoft.fr/fr-FR/?1000024314=).

Caractériser copies et références, tableaux fixes/dynamiques, dimensions, indices invalides, ordre de parcours, suppression de l'élément courant, doublons des tableaux associatifs et invalidation d'un élément passé par référence. Pour chaque collection, définir son interaction avec les threads, la sérialisation et les membres de classes.

### 5.6 Paramètres, portée et durée de vie

La page technique décrit le comportement historique par référence et les moyens de demander un passage par valeur, dont LOCAL dans la déclaration et les doubles parenthèses à l'appel. Cette présentation ne doit pas devenir un défaut universel du nouvel outil. La brochure 2026 documente également un mode par valeur choisi dans le projet, avec les mots-clés « par valeur » et « par référence » pour une sélection ponctuelle. Les pages HTML consultées n'explicitent pas toute la résolution de ce mode 2026 : sa combinaison avec les syntaxes historiques et les réglages d'élément reste à établir à partir de documents et preuves déjà disponibles. L'absence de preuve sur un build ne sera pas comblée par son exécution. [Sources : passage de paramètres](https://doc.pcsoft.fr/fr-FR/?1514077=), [brochure 2026, nouveautés 133–135](https://fr.pcsoft-windev-webdev.com/brochure-WX2026.pdf#page=15).

Caractériser séparément variables affectables, éléments de tableaux, propriétés, constantes, expressions et références d'objets : création éventuelle d'un temporaire, conversions, copie de l'objet ou de sa référence, réaffectation et propagation des mutations. Ne pas confondre le mode général de passage des paramètres avec l'option distincte relative aux instances de classe passées par référence. Les choix de l'implémentation hôte ne remplacent aucun de ces contrats.

Le harnais indépendant conserve le même fragment WLangage et change un seul réglage à la fois. Il vérifie les règles établies et peut comparer les sorties aux traces préexistantes lorsque leur contexte correspond exactement. Les écarts entre variantes de notre moteur servent aussi à isoler une règle ; ils ne prouvent pas à eux seuls une équivalence avec PC SOFT. Aucun résultat des cas ci-dessous n'a été mesuré dans cette étude :

| Cas à exécuter uniquement dans le moteur indépendant | Contrat documentaire ou preuve préexistante à rattacher ; inconnues à conserver |
|---|---|
| Même procédure et même variable, mode projet référence puis valeur lorsque disponible | Valeur avant/après appel, mutation à l'intérieur et mode effectif relevé |
| Appel dans le même élément puis entre deux éléments, dont une surcharge attestée par une pièce existante | Disponibilité de la surcharge, origine du réglage retenu, contexte appelant/appelé et règle de priorité |
| Paramètre sans indication, LOCAL, doubles parenthèses, puis syntaxes explicites 2026 suffisamment documentées | Acceptation syntaxique et mutations du moteur indépendant ; priorité laissée inconnue si aucune preuve ne l'établit |
| Scalaire, tableau, objet et référence d'objet ; paramètres typés et non typés | Copie de valeur, partage d'objet, changement de référence et éventuels effets différents selon type |
| Procédure interne, callback et événement après retour de l'appelant | Règle appliquée au contexte indirect, captures et durée de vie |
| Réglage ou contexte de résolution non relevé | Diagnostic localisé ; aucune génération prétendue équivalente tant que le mode effectif reste inconnu |

Le moteur doit représenter une référence par une cellule ou un accès lecture/écriture, avec durée de vie contrôlée. Distinguer variables de projet, de collection, de fenêtre/page/état, locales, de classe et contexte de champ. Les captures de procédures internes et le moment de destruction des objets demandent des tests séparés. La documentation confirme que la visibilité dépend du lieu de déclaration. [Source : portée des variables](https://doc.pcsoft.fr/fr-FR/?1514088=).

### 5.7 Classes, objets, propriétés et champs

Établir les règles d'héritage, résolution de surcharge, construction/destruction, affectation, identité, conversion, méthode virtuelle et visibilité. Les objets exposés par un composant externe peuvent demander un adaptateur plutôt qu'une instanciation directe.

Un champ n'est pas une variable ordinaire. La documentation distingue l'opérateur de référence `<-` et l'affectation `=`, cette dernière transférant une valeur. Le runtime doit préserver cette différence et les effets sur les événements. [Source : type Champ](https://doc.pcsoft.fr/fr-FR/?1000020967=).

Une propriété doit avoir un contrat : type, cibles, lecture/écriture, valeur par défaut, effet immédiat/différé, invalidation du rendu et événements induits. Une table générique de propriétés sans ces règles ne suffit pas à reproduire l'application.

### 5.8 Événements et contexte implicite

Le compilateur associe un bloc de code à un type de traitement et un contexte : projet, fenêtre, champ, page ou état. Le runtime doit établir les variables de contexte, l'ordre d'initialisation, les événements imbriqués, les retours annulant une action et la durée de vie des fenêtres.

Créer un ordonnanceur d'événements journalisable. Une affectation programmée peut avoir un effet différent d'une saisie utilisateur ; un callback réseau peut revenir après la fermeture d'une fenêtre. Les scénarios doivent tester ces cas. Pour WEBDEV, séparer serveur et navigateur : aucun accès direct au disque serveur ni secret ne doit être déplacé dans le navigateur par simple traduction.

### 5.9 Sémantique des accès aux données sans moteur PC SOFT

Les symboles provenant de l'analyse constituent une partie du contexte de compilation. Une expression `Client.Nom` peut désigner une rubrique, avec un buffer courant et un état de lecture associés. Les fonctions H* modifient potentiellement curseur, filtre, erreur et transaction ; les convertir en requêtes SQL isolées détruirait ces relations.

Le compilateur doit typer les fichiers, rubriques, clés, requêtes et sources de données. Le runtime délègue à un **adaptateur PostgreSQL entièrement indépendant**, qui devra implémenter les contrats retenus des fonctions H* ; aucun pilote, provider, runtime ni serveur HFSQL de PC SOFT n'est utilisé. Les descriptions et données sont lues dans les exports déjà disponibles ou via un lecteur indépendant dont le support du format est démontré. Un format natif opaque conserve son blocage ; le nom d'une API ne suffit pas à rendre sa sémantique portable. Les limitations documentées des requêtes contenant du WLangage font partie des règles à étudier, sans réutiliser leur implémentation PC SOFT. [Source documentaire : Source.ExécuteRequêteSQL](https://doc.pcsoft.fr/fr-fr/?1000024948=).

### 5.10 Erreurs et exceptions

La documentation présente des mécanismes d'exception automatiques, généraux et spécifiques. Le comportement peut donc provenir du code et des paramètres de l'élément. [Source : gestion des erreurs de programmation](https://doc.pcsoft.fr/?3034004=).

Maintenir l'état d'erreur compatible au niveau correct : procédure, thread, connexion ou opération suivant le contrat. Préserver codes, message utile, emplacement source, reprise et effets transactionnels. Une exception du langage hôte doit être traduite à la frontière ; elle ne doit pas traverser arbitrairement le code WLangage. La nouvelle plateforme peut ajouter un identifiant de diagnostic stable, sans changer les valeurs sur lesquelles le programme existant branche.

### 5.11 Indirection, introspection et compilation dynamique

Les appels par nom et la construction de code à l'exécution imposent de conserver une table de symboles runtime et des métadonnées. L'analyse statique ne peut pas prouver qu'aucun autre nom sera construit. Elle doit signaler les zones dynamiques et enrichir l'inventaire avec des traces de scénarios, en précisant que ces traces ne prouvent pas une couverture complète.

La documentation du champ Éditeur de code PC SOFT décrit des paramètres de fonctions autorisées/interdites. C'est une référence documentaire de comportement, pas un composant à intégrer. Notre frontend, compilateur dynamique et runtime sont développés indépendamment, sans appeler les implémentations PC SOFT de Compile ou d'ExécuteCode ni aucune bibliothèque PC SOFT ; ils partagent un budget de temps/mémoire et des capacités configurables. Une API de mêmes noms devra être une implémentation indépendante dont le contrat et les limites sont documentés. [Source documentaire : manipulation du champ Éditeur de code](https://doc.pcsoft.fr/?1410087305=).

Ne pas annoncer la compilation dynamique sur une cible qui l'interdit ou ne la permet pas avec les mêmes propriétés. Sur les cibles AOT, prévoir une liste de modules précompilés lorsque le besoin s'y prête ou déclarer le blocage. Un interpréteur embarqué est une option technique à étudier avec les contraintes du système et de distribution.

### 5.12 Threads, tâches et interopération

Spécifier les partages de variables, contextes de données, sections critiques, annulation, temporisations et retour sur le thread UI. Pour les opérations asynchrones, conserver ordre observable, propagation d'erreur et durée de vie des captures. Les threads ou processus du backend sont des moyens d'implémentation : ils ne définissent pas automatiquement le contrat WLangage.

L'interopération exige des contrats séparés pour tailles numériques, encodage, propriété de mémoire, callbacks, exceptions et architecture. Les docs d'intégration Java et .NET montrent des conversions et limites propres à ces passerelles ; elles ne permettent pas de promettre qu'un code natif sera portable sans adaptation. [Sources : saisir du code Java](https://doc.pcsoft.fr/fr-FR/?9000011=), [utiliser des assemblages .NET](https://doc.pcsoft.fr/fr-FR/?2012002=).

Toute interopération retenue doit exclure les passerelles et bibliothèques PC SOFT, y compris celles cachées dans un assemblage, un package, un service ou un composant tiers. Une API indépendante peut être construite à partir d'un contrat établi ; un contrat inconnu ou une dépendance interdite est un blocage, jamais une permission d'utiliser l'ancien runtime à distance.

## 6. Exécution, diagnostics et expérience de débogage

La recommandation est un frontend commun et une couche de compatibilité explicitement versionnée. Un interpréteur d'AST ou une petite VM facilite d'abord les tests de sémantique et le débogage. Un backend compilé peut être développé ensuite pour les cibles et chemins validés. Le backend retenu par l'architecture générale devra passer exactement la même suite de conformité.

Chaque instruction générée garde un identifiant stable relié au fichier source, objet et traitement. La table de correspondance doit couvrir une génération un-vers-plusieurs et une macro/directive, avec positions en octets et conversion vers les unités du protocole d'éditeur. L'utilisateur pose un point d'arrêt dans « Clic de BTN_Valider », inspecte les variables WLangage et voit une pile WLangage, même si le moteur exécute du code généré.

Utiliser un serveur de langage commun via LSP et un adaptateur de débogage via DAP permet de mutualiser navigation, complétion, diagnostics et débogage entre l'IDE principal et d'autres éditeurs. Ces protocoles standardisent les échanges ; ils ne fournissent ni analyseur WLangage ni runtime. [Sources : Language Server Protocol](https://microsoft.github.io/language-server-protocol/), [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/).

Diagnostics proposés :

| Code de conception | Situation | Résolution attendue |
|---|---|---|
| IMP001 | Format/segment inconnu | Préserver et rapporter ; chercher une pièce déjà disponible ou spécifier une lecture indépendante ; bloquer le périmètre affecté |
| IMP002 | Ressource ou composant absent | Afficher les références et chemins recherchés |
| SEM001 | Réglage sémantique indéterminé | Résoudre via sources/exports/profils déjà disponibles et preuves documentaires ; sinon conserver l'inconnu |
| API001 | Signature absente sur la cible | Proposer adaptateur, cible compatible ou remplacement |
| DYN001 | Nom construit dynamiquement | Afficher l'incertitude et les scénarios d'instrumentation |
| UI001 | Propriété visuelle sans équivalent | Afficher une différence localisée, jamais la supprimer |
| DB001 | Sémantique de curseur non assurée | Exiger un fournisseur ou un scénario de validation |
| GEN001 | Backend incapable d'une opération | Bloquer l'artefact concerné et proposer une autre stratégie |
| DEP001 | Outil/composant PC SOFT direct, transitif ou distant | Refuser la chaîne et l'artefact ; remplacement indépendant obligatoire avant génération de production |

## 7. Protocole de conformité et critères de sortie

Construire un harnais qui n'exécute que le nouveau moteur et ses dépendances indépendantes. Les programmes de test sont écrits pour l'étude. Leurs résultats attendus proviennent soit de règles publiques identifiées, soit de fixtures ou traces déjà disponibles avec provenance, version/build lorsqu'ils sont connus, profil, contexte et empreinte. Une trace sans contexte suffisant reste indicative ; elle ne tranche pas un comportement ambigu. Les cas non déterministes utilisent une horloge et des données fixées, ou des assertions d'ordre/intervalle dont la justification est enregistrée.

Distinguer dans le registre **règle documentée testée**, **trace préexistante comparée**, **contrat de conception propre testé** et **inconnu**. Il est interdit de fabriquer un attendu puis de présenter le test comme preuve du comportement PC SOFT. Sans oracle exécutable, on peut prototyper, tester la cohérence interne et démontrer les règles documentées du périmètre ; on ne peut pas revendiquer une conformité globale ni avoir observé les comportements manquants. Aucun oracle PC SOFT n'est requis ou exécuté, même chez le client.

| Famille de tests | Cas minimaux nécessaires |
|---|---|
| Lexique | FR/EN, accents, commentaires, littéraux, fichier tronqué, erreurs localisées |
| Opérateurs | Priorité, associativité, courts-circuits, effets secondaires, null |
| Nombres | Limites, débordements, arrondis, divisions, conversions chaîne/nombre |
| Chaînes | ANSI/Unicode, taille, découpe, accents, zéros, caractères composés |
| Dates | Vide, invalide, bissextile, fins de mois, durée, changement d'heure |
| Paramètres | Modes projet, surcharges observées, contexte appelant/appelé, référence/LOCAL, doubles parenthèses, syntaxes 2026 acceptées, expression, constante, tableau, alias partagé |
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

Ajouter des tests génératifs pour les expressions et des tests de mutation pour vérifier que la suite détecte un changement de priorité, d'indice ou de règle de copie. Les programmes générés doivent rester dans un sous-ensemble dont les règles et attendus sont justifiés. Ces tests vérifient notre implémentation et la sensibilité de notre suite ; ils ne découvrent pas par eux-mêmes un comportement PC SOFT absent des preuves.

Mesurer séparément : blocs de code importés, constructions syntaxiques rencontrées, signatures appelées, propriétés utilisées, scénarios passés et profils vérifiés. Ne pas publier un pourcentage global mêlant ces unités. Publier les dénominateurs : « 173 signatures vérifiées sur les 221 rencontrées dans trois applications », plutôt que « compatible à 78 % avec WINDEV ».

Trois portes de sortie sont recommandées :

1. **Import fidèle** : aucun élément perdu, inconnus conservés et signalés, provenance et empreintes disponibles, projet source inchangé.
2. **Noyau exécutable indépendant** : frontend, types, références, erreurs, événements et API du pilote passent les tests dont les attendus sont justifiés ; règles propres, preuves de compatibilité et inconnues restent distinctes. Le prototype ne dépend d'aucun oracle.
3. **Application migrée** : parcours métier, données PostgreSQL, documents, périphériques et performances du périmètre accepté passent leur recette sur chaque cible ; un contrôle des dépendances et commandes exclut tout maillon PC SOFT de l'import à l'exploitation. Une nouvelle version du runtime indépendant rejoue ces preuves.

## 8. Sources et réserves de recherche

Les liens de ce chapitre sont des sources primaires PC SOFT ou Microsoft. Plusieurs ouvertures directes du domaine de documentation ont renvoyé HTTP 403 pendant la recherche ; les passages utilisés ont alors été consultés via leur indexation web. Une URL disponible et un extrait indexé ne prouvent pas que la page décrit le build exact d'un futur projet client. Le pilote devra figer les documents publics pertinents ou les copies de documentation déjà fournies, sans lancer d'outil PC SOFT pour les consulter.

Lors de la révision sur les formats Git et le passage de paramètres, les pages `9500230`, `9000050` et `1514077`, ainsi que la brochure 2026, ont pu être lues intégralement par HTTP direct malgré les erreurs de l'outil de navigation. Les variantes française historique/générique et anglaise de `1514077`, dont la variante `verdisp=310`, n'exposaient pas le réglage de projet 2026 ni sa surcharge par élément dans leur texte lu. Le choix du mode projet est attesté par la brochure ; la disponibilité de surcharges par élément, leur priorité et le build exact du projet demeurent non vérifiés. Les commentaires d'utilisateurs présents sous une page d'aide ne sont pas traités comme spécification normative.

Les sources documentaires établissent l'existence des comportements cités. Les structures de manifeste, algorithmes d'import, AST/IR, diagnostics, profils, stratégies runtime et critères de conformité sont des recommandations originales de cette étude. Aucune affirmation de compatibilité avec des fichiers binaires, de réexport natif intégral ou de couverture de tout le WLangage ne peut être déduite de ce document seul.
