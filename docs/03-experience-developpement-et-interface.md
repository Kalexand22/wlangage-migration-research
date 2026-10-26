# Expérience de développement et fidélité des interfaces

Recherche arrêtée au 26 octobre 2026. Ce document décrit l'expérience **à construire**, les éléments officiels vérifiés servant de référence et les conditions pour déclarer une reprise satisfaisante. Les tableaux de périmètre constituent des exigences du futur produit ; ils ne signifient pas que toutes les fonctions existent déjà dans un prototype.

## 1. Principe directeur : préserver les gestes, expliciter les écarts

Une solution compatible doit permettre au développeur de retrouver son projet, son analyse de données, ses fenêtres, ses champs et leurs événements. Lui demander de comprendre d'abord une arborescence React, un ORM et trois outils de compilation déplacerait le coût de migration vers la formation. Le futur atelier doit donc présenter ces concepts familiers directement, tout en utilisant un stockage ouvert et une architecture moderne en dessous.

Il faut distinguer trois engagements :

- **Continuité du travail** : mêmes noms d'objets, recherche, passage conception/code, procédures, test d'une fenêtre et test du projet.
- **Continuité fonctionnelle** : mêmes calculs, données, contrôles, impressions, droits et séquences d'événements observables.
- **Continuité visuelle** : géométrie, police, densité, couleurs, menus et interactions suffisamment proches pour les tâches métier retenues.

Ces engagements se mesurent séparément. Une capture identique ne valide pas un ordre d'événements, et un calcul juste ne valide pas une saisie clavier. L'importeur doit préserver les originaux et produire un rapport des informations reconnues, opaques, perdues ou converties. Toute modernisation susceptible de changer le comportement doit faire l'objet d'une modification visible dans le dépôt du client.

**Référence vérifiée.** PC SOFT organise déjà son environnement autour d'éditeurs de code, fenêtres/pages, états et données. La description du projet regroupe notamment langues, styles/ambiance, GDS/Git, compilation et télémétrie. Le projet doit donc être repris comme un ensemble de métadonnées, pas seulement comme du texte WLangage. [Documentation générale](https://help.windev.com/fr-FR/), [Description du projet : compilation et autres onglets](https://doc.pcsoft.fr/?9500218=).

## 2. Deux espaces de travail, un seul projet

**Proposition.** Fournir au premier lancement un profil « Repères WINDEV » puis un profil « Atelier moderne ». Les deux manipulent le même modèle de projet. Le choix ne doit modifier ni le code ni la sémantique. Le premier place l'explorateur à gauche, les éditeurs au centre, le modifieur de propriétés à droite et les erreurs/traces en bas. Il emploie les mots fenêtre, champ, analyse, rubrique, requête, état, procédure, composant et configuration. Le second peut privilégier une palette de commandes, une vue fichiers et une disposition adaptée aux autres IDE.

Le ruban du profil de transition regroupe Projet, Création, Description, Alignement, Code, Tests et Génération. Les panneaux peuvent se détacher, se réancrer et être restaurés par un profil versionné localement. La densité d'affichage, les tailles de police, le contraste, le thème et la langue de l'IDE restent indépendants du thème de l'application. Le produit doit être utilisable entièrement au clavier ; chaque commande du ruban doit avoir un nom accessible et être disponible dans la palette.

L'écran d'accueil présente les projets récents, l'ouverture d'un projet importé, la création d'un projet et les opérations en cours. Un projet importé arrive directement sur ses objets et sur la liste des écarts ; le développeur n'est pas forcé de lire un assistant complet pour accéder à son code. Le résultat technique d'import reste accessible à tout moment depuis un onglet « Compatibilité ».

### Correspondances à conserver

| Repère connu | Comportement attendu dans le futur atelier | Vérification utile |
|---|---|---|
| Explorateur de projet | Fenêtres, pages, états, analyse, requêtes, classes, procédures, ressources, tests, configurations | Retrouver un objet par son nom d'origine en quelques secondes |
| Description du projet | Métadonnées lisibles et formulaire organisé par thèmes familiers | Aller d'une option au fichier qui la porte |
| Description d'un champ | Dialogue par catégories et panneau de propriétés synchronisés | Modifier le libellé sans modifier une autre langue |
| Conception → code | Ouvrir directement l'événement de la sélection | Le curseur arrive sur le bon traitement |
| Test d'un élément | Exécuter l'objet avec son contexte et ses paramètres | Les dépendances sont préparées ou signalées |
| Test du projet | Démarrer la configuration choisie et sa première fenêtre | Même ordre de démarrage que le profil de référence |
| Modèles et styles | Héritage, variantes locales et propagation explicites | Une surcharge locale survit à la mise à jour du modèle |
| Analyse | Schéma visuel, rubriques, clés, liaisons et contraintes | Les noms métier restent stables dans le code |
| États et requêtes | Éditeurs intégrés reliés aux mêmes objets de données | Une modification de schéma localise ses impacts |
| GDS/Git | Historique, comparaison, branches et conflits depuis l'atelier | Une fusion ne perd pas un événement de champ |

**Références vérifiées.** La première fenêtre peut être définie depuis l'explorateur, la configuration ou le test ; les outils d'alignement regroupent position, taille et répartition. Ces parcours justifient des correspondances directes. [Première fenêtre du projet](https://doc.pcsoft.fr/?9000177=), [Options d'alignement](https://doc.pcsoft.fr/?2022004=).

### Raccourcis et contexte

Les raccourcis suivants sont publiés par PC SOFT ; l'atelier peut proposer un profil de correspondance configurable. Il faut conserver leur **contexte**, car une même touche peut servir à des actions différentes selon l'éditeur. [Référence officielle WINDEV/WINDEV Mobile](https://www.pcsoft-windev-webdev.com/Raccourcis_WD_WM.pdf), [Référence officielle WEBDEV](https://www.pcsoft-windev-webdev.com/Raccourcis_WB.pdf).

| Geste | Action de transition proposée |
|---|---|
| F9 | Tester l'élément actif |
| Ctrl + F9 | Tester le projet |
| Alt + F9 | Tracer le projet |
| Ctrl + Maj + F9 | Paramétrer le mode test |
| Maj + F5 | Arrêter le test |
| F2 | Accéder au code de la sélection |
| Maj + F2 | Code de la fenêtre ou références, selon contexte |
| Ctrl + F2 | Revenir au traitement précédent |
| Alt + F2 | Revenir à l'objet visuel associé |
| Ctrl + B | Ajouter/enlever un point d'arrêt dans le code |
| F4 / Maj + F4 | Nouvelle procédure locale/globale dans le code |
| Ctrl + R | Réindenter le code dans l'éditeur de code |
| Ctrl + D | Dupliquer la sélection selon l'éditeur |
| F12 | Erreur suivante dans le code |

Le moteur de commandes doit résoudre les conflits, gérer claviers AZERTY/QWERTY et permettre un export du profil. Les raccourcis spécifiques macOS/Linux sont une décision à valider si ces hôtes IDE sont retenus ; ne pas remplacer silencieusement les touches familières.

## 3. Périmètre fonctionnel de l'atelier

Les éléments ci-dessous forment un cahier des charges de parité à décliner en tickets et tests. La disponibilité historique dépend de WINDEV, WEBDEV, WINDEV Mobile, de l'édition et de la cible. Le [catalogue officiel historique des fonctionnalités](https://fr.pcsoft-windev-webdev.com/liste-exhaustive-des-fonctionnalites-de-windev.pdf) fournit un point de départ, mais son intitulé correspond à la version 26 : il ne suffit pas pour certifier un périmètre 2026.

### Projet, code, équipe et productivité

| Famille | Fonctions à prévoir et à qualifier |
|---|---|
| Cycle de vie du projet | Création, ouverture, copie, import, sauvegarde, archivage, réparation, version d'origine, mises à niveau réversibles, dépendances, dossiers virtuels et physiques |
| Configurations | Exécutables, bibliothèques, services, webservices, sites, applications mobiles, architectures CPU, variantes client, ressources et code conditionnels, profils de compilation |
| Navigation | Recherche de symbole, références croisées, usages, appels entrants/sortants, historique de navigation, favoris, marques, tâches, navigation entre objet/propriété/événement |
| Édition | Français/anglais du langage, commentaires, indentation, complétion, signatures, aide contextuelle, snippets, glossaire, blocs, multicurseur, pliage, différences, Unicode, encodages historiques |
| Refactorisation | Renommage sémantique projet/champ/rubrique, extraction de procédure, déplacement, conversion explicite de syntaxe, prévisualisation de tous les changements |
| Qualité | Erreurs syntaxiques et sémantiques, avertissements de cible, erreurs UI, audit statique, dépendances obsolètes, analyse des secrets, règles de projet, suppressions motivées |
| Documentation | Dossier technique, diagrammes, documentation des procédures, aide intégrée, guides utilisateur, liens des exigences vers tests et éléments |
| Travail en équipe | Git, historique par ligne, comparaison texte et visuelle, revue, branches, fusion structurelle, verrouillage optionnel des ressources non fusionnables, résolution des partages |
| Réutilisation | Classes, collections de procédures, composants internes, composants externes avec sources, contrats de composants sans sources, modèles de fenêtres/pages/champs/états |
| Ressources | Images/icônes, polices, SVG, traductions, modèles de document, médias, licences des ressources, références stables et résolution de chemins |
| Industrialisation | Compilation CLI, génération reproductible, dépendances verrouillées, cache, CI, rapports machine, signatures, installateurs, publication, mises à jour et retour arrière |
| Pilotage | Tâches, exigences, incidents et liens Git ; intégration aux outils déjà utilisés ; métriques explicites sans surveillance individuelle imposée |

Chaque fonction de refactorisation doit respecter les références indirectes. Quand un nom d'objet est construit par concaténation ou par données externes, le moteur indique l'incertitude et demande une revue du changement proposé. Une recherche textuelle ne doit pas être présentée comme un renommage sûr.

### Éditeurs visuels et données

L'éditeur de fenêtres doit gérer sélection multiple, groupe, alignement, grille, guides, aimantation, règles, zoom, ordre de superposition, verrouillage, duplication et annulation/restauration. Les propriétés comprennent géométrie, ancrages, plans, visibilité, activation, focus, navigation, contenu, masque, liaison de données, styles, langues, bulles et événements. Les modèles doivent conserver l'identité des objets, les liens d'héritage et les surcharges ; un simple copier/coller du rendu ne suffit pas.

L'analyse et les requêtes nécessitent schéma visuel, tables/fichiers, rubriques, clés simples/composées, liaisons, contraintes, types, nullabilité, valeurs initiales, paramètres et génération SQL. Le développeur doit pouvoir suivre une liaison d'un champ jusqu'à la rubrique et revenir. Les données de démonstration sont isolées des connexions de production ; l'aperçu est désactivable et les valeurs sensibles masquées. Les changements de schéma présentent les effets sur requêtes, fenêtres, états et migrations de données.

Le concepteur d'états doit prévoir blocs, ruptures, regroupements, tris, calculs, sous-états, états imbriqués, étiquettes, codes-barres, images, graphes, marges, recto-verso, orientation, papier, pagination, polices, textes extensibles, aperçu, PDF et impressions physiques. Le moteur doit comparer aussi les numéros de page, les sauts, les totaux et les zones répétées. Un rendu HTML approximatif ne remplace pas une compatibilité d'impression certifiée.

### Débogage, tests et exploitation

Prévoir points d'arrêt simples/conditionnels, compteurs de passages, activation/désactivation, arrêt sur exception, exécution pas à pas, entrée/sortie, pause, pile des appels, inspection et modification de variables, expressions surveillées, objets, collections, données images/HTML, threads, tâches asynchrones et contexte de données. Le débogueur travaille sur les lignes WLangage d'origine grâce aux correspondances de sources ; une pile exclusivement dans le langage généré ferait perdre le bénéfice de migration.

La référence PC SOFT propose déjà test du projet, attachement à un exécutable et lancement du débogueur pendant l'exécution. Il faut reprendre ces parcours et décider explicitement, cible par cible, ce qui reste disponible. [Tester et déboguer un projet](https://doc.pcsoft.fr/fr-fr/?2019017=).

La future suite doit couvrir tests unitaires de procédures/classes, tests de fenêtres, scénarios enregistrés, assertions métier, données de test, exécution CLI, rapports et reprise des scénarios existants quand leur format est compris. PC SOFT dispose déjà d'un outil de tests sur exécutable et de scénarios enregistrables ; un nouveau produit doit proposer une continuité ou déclarer les scénarios à réenregistrer. [Tests automatiques sur exécutable](https://doc.windev.com/en-US/?2019029=).

Pour l'exploitation : traces structurées, journal d'erreurs, dump de débogage, profilage CPU/mémoire, requêtes lentes, métriques, télémétrie optionnelle, anonymisation, diagnostic à distance et export du contexte autorisé. Les audits et le profiler sont des fonctions historiques ; leur seule présence ne différencie pas un concurrent. [Livre officiel historique des fonctionnalités, chapitres performances et audits](https://fr.pcsoft-windev-webdev.com/Fonctionnalites_WinDev.pdf).

## 4. Périmètre des interfaces produites

### Familles de champs

Ce tableau indique les familles à inventorier pour chaque cible. Pour chacune, le contrat inclut **propriétés + événements + méthodes/fonctions + liaisons + FAA + rendu + clavier/accessibilité**. Une case « champ pris en charge » sans ces dimensions est insuffisante.

| Groupe | Familles à prévoir dans la matrice de compatibilité |
|---|---|
| Texte et saisie | Libellé, saisie simple/multiligne, mot de passe, numérique/monétaire, date/heure/durée, masque, texte riche, jetons, validation et saisie assistée |
| Actions et choix | Bouton, interrupteur, sélecteur, combo, liste, liste image, lien, menu, menu contextuel, ruban, barre d'outils, boutons segmentés |
| Données tabulaires | Table mémoire/fichier/requête, table hiérarchique, colonnes typées, ruptures, zone répétée, TCD, sélection et édition multiples, virtualisation |
| Conteneurs et navigation | Onglet, fenêtre/page interne, plans, dispositions, groupe, panneau, séparateur, volet, tiroir, fenêtre fille/sœur/modale, MDI et panneaux ancrables |
| Visualisation métier | Arbre, graphe, jauge, potentiomètre, tableau de bord, agenda, planning, diagramme de Gantt, Kanban, organigramme, diagramme |
| Documents | Lecteur PDF, traitement de texte, tableur, éditeur d'images, éditeur HTML, éditeur de code et visualiseur de documents |
| Médias et web | Image, dessin, vidéo, son, caméra, navigateur HTML, carte, contenu externe, WebView, notifications et dialogues système |
| Mobile et appareils | Gestes, orientation, zone de sécurité, clavier virtuel, caméra/scan, GPS, notifications, permissions, capteurs, authentification biométrique selon cible |
| Extensions récentes | Champs liés à l'IA et autres nouveautés : inventaire par version, dépendances externes et mode dégradé explicites |

**Faits vérifiés ciblés.** Le type `Champ` permet de référencer des champs existants ou créés dynamiquement, avec des limitations propres aux cibles. Le champ Arbre possède des options visuelles et des fonctions automatiques. Les propriétés d'un champ Disposition incluent notamment ancrage, géométrie et accessibilité. Ces cas montrent pourquoi il faut tester un objet dans sa cible réelle. [Type Champ](https://doc.pcsoft.fr/fr-FR/?1000020967=), [Champ Arbre](https://doc.pcsoft.fr/fr-FR/?1013037=), [Propriétés du champ Disposition](https://doc.pcsoft.fr/?1410087048=).

### Fonctions automatiques attendues par les utilisateurs

Les FAA font partie du comportement métier perçu : les utilisateurs peuvent s'appuyer sur un filtre, une exportation ou une personnalisation sans que ce besoin soit visible dans le code de l'application. Le catalogue officiel comprend des commandes de filtrage/recherche, zoom, export, manipulation de planning, personnalisation et contrôle de disponibilité. Le futur moteur doit implémenter les commandes nécessaires ou signaler leur absence lors de l'audit. [Constantes officielles des FAA](https://doc.windev.com/en-US/?3013073=&lf=fr&name=AAF_constants).

**Exigences proposées :** conserver tri simple/multiple, filtres et mémorisation, recherche/loupe, choix/ordre/largeur des colonnes, calculs/totaux, copie, export autorisé, impression, zoom, sélection, cocher tout, menus contextuels, saisie/calendrier/calculatrice, annuler/refaire dans les éditeurs concernés et personnalisation des fenêtres. Chaque action doit déclencher les événements attendus et respecter les droits. Il faut inventorier également les commandes programmatiques activant, désactivant ou renommant ces fonctions. Les préférences utilisateur doivent être exportables et liées à des identifiants stables de champs.

Les exports et impressions doivent appliquer les autorisations côté données/service, pas uniquement masquer une option du menu. Quand une ancienne application autorisait une action dangereuse, le mode migration conserve le comportement seulement si la politique du client le permet ; la différence devient une décision documentée, pas une surprise après livraison.

### Droits, langues, accessibilité et fidélité

La reprise du groupware doit couvrir utilisateurs, groupes, configuration de droits, premier écran, authentification, propagation des restrictions et personnalisation des fenêtres d'identification. Le groupware PC SOFT peut être classique ou utiliser un serveur d'authentification ; il ne faut pas réduire son import à un simple formulaire de login. [Options du groupware](https://doc.windev.com/en-US/?1000021153=&lf=fr&name=GPU_Options), [Personnalisation](https://doc.windev.com/en-US/?1000021170=).

**Proposition de recette :** matrice rôle × action × objet × périmètre de données ; contrôle des refus et des accès indirects ; migration des identités par processus explicite, sans présumer que les mots de passe existants sont portables. Les droits UI et les autorisations serveur doivent rester cohérents, même si un appel est fait sans interface.

Pour les langues, importer messages, libellés, bulles, masques et ressources ; conserver la langue de secours, formats nombres/dates, devises, tri/casse, pluriels et sens d'écriture. Pour l'accessibilité, prévoir navigation clavier, ordre de tabulation, focus visible, lecteur d'écran, nom/rôle/état accessibles, contraste et zoom texte. La tabulation et l'action Entrée font déjà partie du paramétrage des champs de saisie PC SOFT. [Champ de saisie](https://help.windev.com/en-US/?1013145=). La conformité au niveau WCAG 2.2 AA sur le web est une cible proposée qui exige une recette, pas une propriété acquise par choix d'un framework. [WCAG 2.2, W3C](https://www.w3.org/TR/WCAG22/).

Le web et le mobile ont des contraintes différentes du bureau : navigation HTTP, session, historique, permissions, reprise après suspension, latence et absence de réseau. Conserver le même code métier n'implique pas automatiquement les mêmes fenêtres. La conversion d'un écran dense peut demander une disposition dédiée ; l'atelier doit indiquer quels éléments sont partagés et quelles variantes sont spécifiques.

## 5. Quatre parcours prioritaires

### A. Ouvrir un projet historique et retrouver sa fenêtre

Le développeur choisit une copie exportée du projet et indique version, cible et profil. L'atelier analyse les fichiers, conserve les originaux et affiche les objets reconnus. La première fenêtre s'ouvre sur son plan initial ; un panneau montre les écarts bloquants. F2 sur un bouton ouvre le code d'origine et non une traduction. F9 exécute la fenêtre avec des paramètres contrôlés. Le critère de recette est la réalisation d'une modification de libellé puis d'un test sans modifier manuellement les fichiers générés.

### B. Corriger une régression métier après import

Depuis un scénario qui échoue, le développeur ouvre le résultat original et le résultat du nouveau moteur. Le rapport montre le premier événement divergent, les entrées et la valeur attendue. Il place un point d'arrêt dans le WLangage, inspecte la rubrique et le champ, puis corrige soit une règle de compatibilité du moteur, soit une adaptation explicitement acceptée du projet. La distinction est essentielle pour ne pas accumuler des corrections inutiles dans le code client.

### C. Faire évoluer analyse, formulaire et impression ensemble

Le développeur ajoute une rubrique dans l'analyse, demande les impacts, met à jour le formulaire et l'état associé, puis génère une migration de données révisable. L'atelier propose de prolonger la liaison de données plutôt que d'insérer un SQL ad hoc invisible. La recette compare stockage, affichage, validation, export et impression avec des données témoins incluant vide, NULL et valeurs limites.

### D. Moderniser progressivement sans perdre la référence

Le développeur duplique une disposition visuelle et active un nouveau thème sur un lot d'écrans ; le modèle métier et les procédures restent partagés. La comparaison montre la variante classique et la variante modernisée à plusieurs DPI/langues. Les nouvelles interactions sont testées avec des utilisateurs. Un déploiement pilote active la variante par population, puis permet le retour au thème classique sans restauration de la base de données.

## 6. Maquette textuelle du profil de transition

```text
Projet : Gestion commerciale             Profil : Référence WD / Windows
[Projet] [Création] [Description] [Alignement] [Code] [Tests] [Génération]
[Ouvrir] [Sauver] [GO Élément F9] [GO Projet Ctrl+F9] [Configuration ▾]
┌ Explorateur ─────────┬ FEN_Client : Conception | Code | Comparaison ┬ Propriétés ┐
│ Analyse             │ [Nom             ] [Code client         ] │ Général    │
│ Fenêtres            │ [Adresse                                 ] │ UI         │
│  FEN_Client         │ [Table contacts                          ] │ Liaison    │
│ Requêtes            │                                            │ Événements │
│ États               │ [Valider] [Annuler]                        │ Style      │
│ Classes / Procédures│ Plan 1 | Plan 2       Zoom 100 % DPI 125 %  │ Langues    │
├─────────────────────┴────────────────────────────────────────────┴────────────┤
│ Erreurs | Compatibilité | Tests | Traces | Données | Références                │
│ 1 blocage : fonction externe indisponible — localisation — options documentées│
└───────────────────────────────────────────────────────────────────────────────┘
```

Cette maquette représente une organisation proposée, sans reprendre les graphismes ni les ressources de PC SOFT. Un clic sur un écart doit ouvrir l'objet, sa localisation et les solutions possibles ; aucun écran ne doit afficher un taux global rassurant tout en cachant un blocage.

## 7. Validation et critères d'acceptation

La recette doit employer des projets représentatifs autorisés et plusieurs développeurs habitués à WINDEV, pas uniquement l'équipe qui construit l'atelier. Mesurer ouverture d'un projet, localisation d'un événement, ajout d'un champ lié, débogage d'une erreur, évolution d'un état et préparation d'une génération. Enregistrer réussite, durée, erreur, aide requise et satisfaction ; fixer les seuils après un pilote plutôt que publier une promesse arbitraire.

Pour les applications : scénarios métier comparés, capture à tailles/DPI fixés, arbre d'accessibilité, ordre d'événements, focus, clavier, données modifiées, états PDF et impression physique sur les périphériques concernés. Tester séparément langues, thème sombre, très longs textes, écran réduit, multiécran, réseau lent, permissions refusées et reprise d'une session.

Un rapport de parité doit identifier la version d'origine, l'OS, le moteur, les polices, la configuration, les jeux de données, le scénario et les tolérances. Les écarts acceptés restent listés. Les champs sans exemple représentatif, les composants sans sources et les paramètres opaques reçoivent un statut « non qualifié », jamais « compatible » par défaut.

## 8. Sources et limites

Les liens intégrés sont des sources primaires PC SOFT ou W3C, consultées via la recherche publique le 26 octobre 2026. Certaines pages de documentation indexées concernent 2024/2025 et le catalogue exhaustif historique concerne la version 26 ; leurs dates ne constituent pas une preuve du dernier état commercial disponible. L'annonce officielle 2026 confirme notamment IA conversationnelle, positionnement Grille, audit de sécurité et Hot Reload, sans permettre d'inférer leur disponibilité sur toutes les éditions et toutes les cibles. [Annonce officielle PC SOFT du 3 octobre 2025](https://forum.pcsoft.fr/fr-FR/pcsoft.fr.windev/278021-pcsoft-version-2026-windev-webdev-windev-mobile-est/read.awp).

Restent à qualifier sur des projets réels : l'intégralité des propriétés de chaque champ, les formats de personnalisation utilisateur, les comportements implicites des modèles, les différences d'événements par cible, l'import des scénarios, les versions de groupware, les limites des éditeurs documentaires et les contraintes d'impression. L'exhaustivité doit être produite et maintenue par inventaire versionné et tests ; ce document définit le périmètre UX de cette démarche.
