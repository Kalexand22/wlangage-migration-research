# Réconciliation de la relecture critique

État examiné : **26 octobre 2026**. La relecture fournie indiquait n'avoir pu consulter que le README et une arborescence. Cette réponse s'appuie sur les fichiers complets, les sources primaires vérifiées et l'état GitHub observé. Elle distingue une lacune de la page d'accueil d'une absence dans tout le dossier.

## 1. Points retenus et changements

| Point de la relecture | Vérification et décision | Changement ou état restant |
| --- | --- | --- |
| M1 — clauses visant les outils de développement | Restrictions confirmées dans WINDEV et Framework; licence Outils distinguée | Risque qualifié par acte et composant, relevé des sources; pas de blocage général du code original par une clause d’usage d’un produit tiers |
| M2 — régimes juridiques distincts | Observation, interopérabilité et correction d'erreurs ne sont pas interchangeables | Directive/CPI/SAS déjà présents, maintenant complétés par Top System et portée des exceptions |
| M3 — absence de LICENSE | Absence confirmée; NOTICE réservait déjà le choix au propriétaire | Décision explicitement différée par le propriétaire pendant la faisabilité; absence de licence ouverte assumée, sans concession nouvelle |
| M4 — contexte commercial trop discret | Lacune de la présentation confirmée | Chapitre 14 : sources officielles, personas, coûts symboliques et inconnus; pas de ROI client inventé |
| M5 — comparaison du marché | 01 traitait déjà plusieurs voies et acteurs | Tableau enrichi des offres demandées; déclarations commerciales séparées des résultats prouvés |
| M6 — CI et contributions | Aucun workflow dans l'état initial examiné | Workflow de documentation, contrôle hebdomadaire informatif des liens, gabarits et historique ajoutés |
| I1 — sens du mot migration | La cible principale reste bien une plateforme indépendante compatible | README explicite la migration de chaîne d'outils et d'exécution; pas de renommage du dépôt |
| I2 — couverture non démontrée | Exigences et fonctions sont des unités différentes | Formulation vague retirée; nombre de fonctions et rattachement inconnus; aucun ratio artificiel |
| I3 — HFSQL peut maintenir une dépendance | Risque confirmé au niveau architectural et contractuel | Deux profils explicites, Continuité et Indépendance; aucun moteur imposé universellement |
| I4 — binaire résiduel et versions | Déjà partiellement couverts; précisions officielles utiles | Prérequis du parcours Git, propriétés avancées binaires et rupture entre updates documentés |
| I5 — paramètres 2026 | Réglage projet et mots-clés vérifiés dans la brochure | F-0046 précisée et F-0518 ajoutée; option et provenance dans le profil; surcharges par élément non établies ici |
| A1 — ordre du README | La décision et ses conditions doivent précéder le backend | Nouvelle ouverture : objectif, utilisateurs, risques, deux voies et navigation |

Le texte transmis s'interrompt au titre **A2**. Aucune proposition absente n'a été reconstruite ni attribuée à son auteur. La stratégie à deux étapes retenue dans ce dépôt est explicitement notre proposition : inventaire/exports/preuves, puis choix conditionnel de réalisation.

## 2. Trois conclusions que le dossier ne peut pas adopter telles quelles

### Clause contractuelle et interdiction générale

La clause est un risque majeur pour certaines méthodes de construction et de diffusion. Elle ne permet pas, à elle seule, de déclarer toute implémentation indépendante du langage illégale. Les actes réalisés, parties liées, contrats applicables et exceptions doivent être examinés. À l'inverse, les décisions SAS et les règles d'interopérabilité ne neutralisent pas automatiquement tous les contrats. [Analyse et sources primaires](09-propriete-intellectuelle-et-licences.md).

Une salle blanche sert à tracer et séparer les informations. La composition d'une équipe ou l'exécution des tests par un client ne garantit pas le droit de chaque opération. Le protocole doit être examiné sur ses bénéficiaires et flux réels; aucun avis juridique n'a été obtenu par cette recherche.

### Ratio entre exigences et API

Diviser 519 exigences par un chiffre promotionnel de fonctions serait dépourvu de sens. Une exigence peut recouvrir plusieurs signatures, tandis que plusieurs exigences peuvent porter sur la même fonction. Le catalogue doit aussi distinguer types, propriétés, événements, constantes, cibles et options.

Le compteur de 3 480 cité par la critique n'a pas été confirmé comme catalogue actuel fermé. La page primaire examinée affiche une annonce de **plus de 4 500 fonctions**, sans constituer davantage un dénominateur normatif de certification. Les observations et limites sont consignées dans le [chapitre 06](06-inventaire-fonctionnel-et-couverture.md). Le taux de couverture reste **non calculable**, et non extrapolé depuis le nombre d'exigences.

### PostgreSQL, coût et retour arrière

Changer la base peut réduire certaines dépendances et évite de reconstruire le moteur de stockage. Il reste à préserver les contrats H*, migrer les données et traiter les écritures après bascule. PostgreSQL seul, si d'autres composants PC SOFT restent actifs, ne démontre pas la fin d'obligations tarifaires ou contractuelles. [Contrats de données et profils](04-donnees-integrations-et-cibles.md).

Un export du client n'est pas une garantie universelle de droits; un changement de base n'est pas automatiquement réversible après de nouvelles écritures. Le programme conserve donc deux trajectoires explicites et un contrôle de sortie des dépendances composant par composant.

## 3. Ce qui était déjà présent et ce qui manquait réellement

Le chapitre 09 initial contenait les fondements UE/France, SAS, une organisation indépendante, la réserve sur les licences et l'absence de droits généraux de redistribution. **Il ne mettait pas en évidence la clause précise visant l’usage des outils PC SOFT pour construire certains outils concurrents : cette omission est corrigée, sans transformer cette clause en interdiction générale d’un compilateur indépendant.**

Le chapitre 02 et le profil JSON comportaient déjà `version` et `build`, la préservation des originaux et le traitement des zones opaques. La révision précise le parcours officiel de partage Git et le changement de format au sein de 2026. Elle ne remplace pas les inconnus d'un client par des numéros supposés.

Avant cette révision, l'état distant observé avait deux commits et treize chapitres; il était devenu public. La relecture mentionnait un commit et douze chapitres. Ces observations peuvent correspondre à des moments ou à un accès différents; le nouveau dossier publie ses fichiers générés et son historique pour faciliter une vérification reproductible.

## 4. Définition de la clôture

La correction d'un document n'est pas la résolution d'un risque produit. Les points suivants restent ouverts tant que leurs preuves n'existent pas : qualification des actes et composants réellement utilisés; catalogue API fermé; projet pilote et oracle dans un cadre autorisé; faisabilité et performances des moteurs. Les décisions commerciales et de publication sont ultérieures, sans conditionner l’étude technique.

Les contrôles de ce dépôt vérifient des fichiers, liens locaux, identifiants et dépendances de tâches. Le contrôle externe hebdomadaire ne prouve que des observations réseau ponctuelles. Ni l'un ni l'autre ne certifie l'exécution du WLangage.


## 5. Clarification du propriétaire après la première relecture

La phase actuelle est l’évaluation de faisabilité. Le choix d’une licence de publication est différé et aucune autorisation générale n’est ajoutée. La recommandation d’un avis avant tout codage est également retirée: un prototype original indépendant des logiciels PC SOFT peut être étudié sans en faire un prérequis général. Les opérations utilisant effectivement un produit, un contrat ou des informations sous droits restent à qualifier selon leur nature. Le chapitre 09 sépare le développement original, les observations légalement permises et la réutilisation/redistribution de composants.

La seconde lecture fournie par le propriétaire est une piste argumentée, pas un avis juridique obtenu. Le dossier ne conclut ni à l’invalidité générale de toute restriction concurrentielle ni à la sécurité absolue d’une expression commerciale ou d’un protocole de test. Les conditions impératives de protection de l’observation sont examinées pour leur portée concrète.


## 6. Contrainte finale : aucune utilisation de logiciels PC SOFT

Le propriétaire exclut désormais toute DLL ou tout outil PC SOFT, y compris pour l’import, les données et les tests, même via un tiers. Les options de pont, de serveur HFSQL et d’oracle exécuté sont donc retirées de la cible. La seule voie active est l’implémentation originale alimentée par des fichiers, spécifications et références préexistantes. Les analyses contractuelles des autres voies restent documentaires, sans en faire des prérequis au prototype indépendant. Voir le [périmètre retenu](15-perimetre-independant-et-preuve-de-faisabilite.md).

La description et les topics GitHub n’ont pas été modifiés : l’accès connecté a refusé la mutation des métadonnées avec HTTP 403. Cette opération de présentation n’est pas nécessaire à l’évaluation de faisabilité et aucun élargissement d’accès n’est demandé.
