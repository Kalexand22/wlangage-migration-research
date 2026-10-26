# Améliorations immédiates et premier lot

Ce chapitre répond à la question « que peut-on améliorer tout de suite ? ». Il distingue les corrections du dossier déjà faites et les travaux de préparation ou de développement restant à exécuter.

**Le périmètre courant exclut tout outil ou composant PC SOFT, y compris pour importer ou tester.** Le [contrat d’indépendance](15-perimetre-independant-et-preuve-de-faisabilite.md) prime sur les comparaisons historiques.

## 1. Deux corrections livrées immédiatement

**Précision des références.** Quinze exigences P0 de la matrice renvoyaient à des références trop générales alors que des pages ciblées avaient été examinées. Leurs URL et leur portée sont désormais précisées : F-0002, F-0004, F-0011, F-0030, F-0032, F-0034, F-0036, F-0038, F-0039, F-0043, F-0046, F-0047, F-0050, F-0051 et F-0060. Les limites restent explicites : une page sur la suppression d'un tableau ne définit pas tous les comportements d'un tableau. Aucun statut d'implémentation ou de compatibilité n'a été augmenté.

**Ordre de travail.** Les 269 exigences P0 de la matrice révisée ne constituent pas un premier sprint. Le fichier [premier-lot.csv](../data/premier-lot.csv) définit dix tâches de préparation, avec dépendances, identifiants d'exigences, rôles et critères de sortie. Leur exécution reste à faire. Le plan permet d'avancer sur les contrats et l'outillage avant d'engager le développement complet du produit.

## 2. Ce qu'il faut améliorer ensuite, par ordre d'utilité

### A. Fermer un profil pilote

Choisir une cible proposée, puis obtenir les versions/builds et options d'un projet réel. Windows x64 et .NET/WinForms sont des choix initiaux de conception, pas un profil source déjà validé. Les versions du runtime, les options et les dépendances ne doivent jamais être choisies par déduction d'une date commerciale.

**Sortie attendue :** un profil renseigné et une liste des inconnus bloquants, avec leur responsable. Sans ces éléments, le meilleur résultat possible est « prêt à collecter les preuves », pas « compatible ».

### B. Séparer validité documentaire et préparation d'un essai

Le contrôle actuel du dépôt valide la syntaxe JSON, les liens et la matrice. Il ne garantit pas qu'un profil est prêt à compiler : les exemples comportent volontairement des champs `null` et aucune preuve. Cette distinction est correcte, mais un futur outil de préparation doit pouvoir refuser un profil incomplet.

Définir un schéma pour profil, cas et preuve, puis un contrôle des règles entre fichiers : références existantes, options résolues, références statiques déjà fournies et documentées, sources correspondant aux empreintes, cas liés aux exigences et absence de blocage ouvert. Les étapes « audit prêt », « génération prête » et « qualification documentée » ont des conditions distinctes. Un schéma conforme ne démontre jamais le comportement du moteur.

### C. Relier catalogue et preuves

Le prochain registre doit fermer la chaîne : **F-ID → contrat/signature et profil → prototype P1–P6 → cas → exécution → décision**. Un document peut décrire un excellent protocole sans qu'un cas précis le mette en œuvre ; cette liaison doit être contrôlée.

Commencer par les règles qui peuvent modifier silencieusement le métier : court-circuit et effets de bord, paramètres par référence, copie des tableaux, précision monétaire, NULL/vide, événements et curseurs HFSQL. Le détail des signatures reste à relever avant d'annoncer un catalogue API fermé.

### D. Tester les outils de preuve avant de leur faire confiance

Préparer des observations synthétiques volontairement différentes : un centime d'écart, une valeur NULL remplacée par vide, deux événements inversés, une mutation perdue après passage par référence et une normalisation qui masque un montant. Le comparateur doit les détecter, et expliquer le premier écart utile.

Ces fixtures peuvent être conçues sans projet client. Elles testeront le comparateur lorsqu'il sera réalisé ; elles ne seront jamais présentées comme des résultats de WINDEV. Aucun oracle PC SOFT n’est exécuté. Les attendus proviennent de spécifications publiques et de références préexistantes fournies ; les conclusions restent limitées à ces éléments.

### E. Centraliser les seuils

Les chapitres 07 et 11 donnent des seuils illustratifs différents selon le stade : prototype, pilote et comparaison de performance. Ils sont des propositions, pas des résultats ni des obligations universelles. Le registre [seuils-decision.csv](../data/seuils-decision.csv) les rapproche avec leur contexte et leur statut **non validé**.

Avant un essai, choisir une seule valeur applicable à sa mesure, au profil et au stade. Une alerte de lenteur d'un prototype ne devient pas une tolérance de production. Une tolérance géométrique ne permet jamais de modifier un total, un code-barres ou une information obligatoire. Les arbitrages devront être datés avant les résultats, pour éviter un déplacement des seuils après un échec.

## 3. Ce qui peut démarrer sans sources

Le premier lot porte sur le modèle de profil, les schémas, la traçabilité, les seuils, les fixtures synthétiques et le format des preuves. Les jours J1–J10 du CSV sont un **ordre indicatif de préparation**, pas un engagement de délai ni un programme de construction du compilateur en dix jours. Ils supposent les compétences et la disponibilité nécessaires.

Les essais d'import, l'exécution du WLangage, la compatibilité H*, la fidélité des fenêtres et des états requièrent ensuite un corpus exploitable indépendamment et des références statiques déjà disponibles avec provenance. Aucun environnement PC SOFT ne participe aux essais. Le [cahier des prototypes](11-cahier-des-charges-des-spikes.md) reste la référence pour ces développements. Ne pas écrire des résultats attendus imaginés pour remplir des colonnes de preuve.

## 4. Décision recommandée

Engager d'abord ce lot de préparation limité, puis le prototype d'import et le prototype sémantique sur un même profil réel. Poursuivre si les pertes sont toutes identifiées, les traitements originaux restent maintenus en WLangage et les divergences critiques sont résolubles. Réduire le profil ou changer d'approche si la reprise exige une reconstruction manuelle généralisée.

Les meilleurs gains immédiats sont donc la précision, l'ordre d'exécution et la qualité des preuves. Ajouter des familles à la liste restera nécessaire lorsqu'elles seront découvertes ; cela ne remplace pas la démonstration d'une première tranche complète.
