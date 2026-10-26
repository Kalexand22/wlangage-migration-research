# Orchestration des agents, preuves et gates de livraison

Proposition de conception du 26 octobre 2026. Ce chapitre définit comment exécuter et vérifier le plan de réalisation de la plateforme. **Le plan est documentaire : ses tâches sont initialement `planifie` et ses vérifications `non_execute`. Aucun succès d'exécution n'est revendiqué.** Le moteur d'orchestration, ses contrôles et ses adaptateurs devront être implémentés puis éprouvés avant de recevoir des travaux réels.

Cette conception est autonome. Elle ne requiert ni environnement, ni runtime, ni outil PC SOFT pour fabriquer, tester, distribuer ou exploiter la nouvelle plateforme. Les références historiques d'une étude de compatibilité ne deviennent pas des dépendances d'exécution.

## 1. Unité de travail et taille des missions

Le plan distingue trois objets :

- Un **bloc** `Bxx` rassemble une capacité livrable et ses critères d'ensemble.
- Une **tâche** `T-Bxx-nn` produit un résultat limité, vérifiable et révisable.
- Une **gate** `G-Bxx` décide si la capacité intégrée satisfait le contrat du bloc sur une révision précise.

Le découpage vise des missions d'environ **deux à six heures de travail effectif d'agent**, comme budget de planification à réviser après mesure. Ce n'est ni un délai garanti, ni une estimation de tout le projet, ni une raison de clôturer un travail incomplet. Les attentes externes, les builds et la revue sont suivis séparément. Une mission qui demande plusieurs décisions de conception, modifie plusieurs contrats indépendants ou ne possède pas de test de sortie doit être redécoupée avant attribution.

Chaque tâche doit avoir un effet visible : par exemple une règle sémantique implémentée et éprouvée sur des cas limites, un importeur borné avec diagnostics, ou un adaptateur dont les comportements d'échec sont démontrés. « Faire le compilateur » ou « terminer l'interface » sont des blocs, pas des tâches atomiques. Une tâche de recherche peut produire une décision et ses éléments contradictoires ; elle ne doit pas prétendre produire une fonctionnalité exécutable.

Le résultat est accepté en fonction de ses critères, pas du nombre de fichiers, de lignes ou de tests. Le parent conserve ses critères d'intégration même lorsque toutes ses tâches ont été acceptées.

## 2. Contrat minimal d'une tâche

Le [plan JSON](../data/plan-realisation.json) fixe les champs du backlog proposé ; le [modèle de preuve](../examples/preuve-gate.exemple.json) décrit les résultats à renseigner lors d’une exécution réelle. Le contrat conceptuel suivant précise aussi les champs de tentative, d’affectation et de révision à rendre obligatoires dans le futur ordonnanceur ; le plan statique ne les fournit pas encore et n’est pas directement un ordonnanceur exécutable.

| Élément | Information exigée |
|---|---|
| Identité | Identifiant stable, bloc parent, révision du plan et type de mission |
| Objectif | Résultat attendu et problème concret résolu |
| Périmètre | Fichiers/composants autorisés, contrats modifiables et travaux exclus |
| Entrées | Révision source de départ, documents applicables et données de test autorisées |
| Prérequis | Tâches acceptées, gates requises, capacités machine et accès nécessaires |
| Livrables | Code, documentation ou artefacts précisément identifiés |
| Acceptation | Invariants et scénarios mesurables, dont refus/erreurs nécessaires |
| Vérification | Commandes ou procédures attendues, environnement et résultats à examiner |
| Risques | Inconnues, effets persistants et conditions d'arrêt |
| Budget | Temps cible, ressources, coût maximal et nombre de tentatives autorisées |
| Responsabilités | Agent d'implémentation, relecteur distinct et autorité de gate |
| Intégration | Branche candidate, contrat de dépendance et stratégie de retour arrière |

Le contexte remis à l'agent contient les sources de l'exigence et les critères complets. Il n'est pas remplacé par un résumé généré dont la fidélité serait supposée. Les références sont versionnées ; un changement de besoin devient une nouvelle révision du plan et une analyse d'impact.

Une tâche ne doit pas dépendre seulement d'un nom de branche susceptible de changer. Elle précise la preuve ou le contrat attendu de ses prérequis. Quand une interface évolue, les consommateurs sont identifiés et requalifiés avant d'être considérés prêts.

## 3. Dépendances : un DAG et des gates explicites

L'ordonnanceur doit valider le graphe avant chaque vague : identifiants uniques, références existantes, absence de cycle et compatibilité des contraintes. Une dépendance inconnue, absente, remplacée ou seulement déclarée terminée sans preuve ne peut satisfaire un prérequis.

Une tâche devient éligible uniquement lorsque les quatre conditions sont réunies :

1. Ses dépendances de tâches sont acceptées sur des livraisons identifiées.
2. Ses gates préalables ont une décision valable pour les versions concernées.
3. Ses entrées et autorisations sont présentes.
4. Les ressources nécessaires et un espace de travail isolé sont disponibles.

Dans le plan statique, `depends_on_blocks` déclare les blocs dont la gate est requise pour tout le bloc courant. Chaque tâche peut ajouter `requires_block_gates`, également rempli avec des identifiants de bloc comme `B09` ; la gate correspondante est `G-B09`. `depends_on` contient uniquement des identifiants de tâches. Le validateur combine ces trois types de liens pour détecter les cycles ; les fiches et le CSV affichent les gates supplémentaires au niveau du ticket concerné.

L'absence d'un item dans un fichier n'est jamais assimilée à une réussite. Les objets retirés conservent un état terminal explicite et une raison : livré, remplacé ou abandonné. Un remplacement ne satisfait une dépendance que par un nouveau lien accepté, avec les critères préservés.

Le parallélisme dépend aussi du périmètre d'écriture. Deux tâches indépendantes dans le DAG peuvent entrer en conflit sur une même grammaire, un registre d'API, un schéma ou une ressource de test. Le plan identifie ces ressources partagées et impose soit une sérialisation, soit des contrats suffisamment séparés. Une simple liste de chemins est un premier filtre, pas une preuve de compatibilité des changements.

## 4. Séparer plan, tentative et résultat

La tâche exprime le besoin stable ; une **tentative** représente une exécution particulière. Elle possède son propre identifiant, propriétaire, révision de départ, bail, budget, journal, artefacts et motif de fin. Une nouvelle tentative n'efface pas l'échec précédent.

Le cycle cible distingue préparation, attribution, exécution, vérification, revue et acceptation. Une tâche interrompue peut revenir en attente après réconciliation ; elle ne revient pas automatiquement à l'exécution parce qu'un délai a expiré.

| Situation | Effet attendu |
|---|---|
| Plan écrit | `planifie` ; aucune commande exécutée ni preuve positive |
| Précondition manquante | Attente ou blocage avec cause identifiable |
| Vérification réellement réussie | Preuve technique admissible pour la révision vérifiée |
| Vérification `FAIL` | Échec conservé ; correction puis nouvelle preuve requise |
| Vérification `BLOCKED` | Résultat non acquis ; dépendance ou environnement à résoudre |
| Commande non lancée ou interrompue | `non_execute` ou résultat inconclusif selon le cas, jamais `PASS` |
| Revue indépendante favorable | Condition supplémentaire ; ne remplace pas les tests |
| Toutes les tâches d'un bloc acceptées | Bloc candidat à la gate ; aucune validation implicite du bloc |

Les vocabulaires affichés et les codes machine doivent avoir une correspondance explicite. Une couleur dans un tableau de bord ne peut pas changer le sens d'un état. Un test ignoré, un job neutralisé ou une collection vide ne prouve pas que le comportement a été exercé.

## 5. Attribution concurrente, baux et espaces Git

L'attribution doit être une opération atomique : vérifier l'éligibilité et la révision du statut, réserver la tâche et ses ressources, créer la tentative, puis délivrer un jeton de propriété. Deux demandes concurrentes ne doivent jamais obtenir toutes deux le droit de finaliser le même travail.

Le bail contient une échéance renouvelable et un **numéro de génération**. Les changements d'état et l'intégration exigent le numéro courant. Si un agent perd son bail et qu'un autre reprend, les messages tardifs du premier sont refusés. L'expiration détecte une perte de maîtrise ; elle ne prouve pas que le processus ancien est arrêté. La reprise vérifie ses effets et son espace de travail avant de réattribuer.

Chaque tentative utilise une branche et un worktree dédiés, ou un clone indépendant lorsque l'isolation l'exige. Un worktree offre un arbre et un index distincts, tout en partageant des données Git avec le dépôt principal : il ne constitue pas à lui seul une frontière de sécurité. Les dépendances, caches, ports, bases de test et dossiers d'artefacts doivent être isolés ou protégés séparément. [Documentation officielle Git worktree](https://git-scm.com/docs/git-worktree).

Le gestionnaire refuse un espace déjà occupé ou modifié sans provenance connue. Il ne lance aucune remise à zéro destructive pour « nettoyer » la situation. Les fichiers modifiés par l'utilisateur et les autres agents sont hors périmètre. L'intégration est sérialisée par cible et contrôlée sur la révision attendue de la branche de destination ; un changement de cette base déclenche une nouvelle vérification appropriée.

Le nombre d'agents configuré ne prouve pas la capacité disponible. Commencer avec une concurrence faible, mesurer CPU, mémoire, I/O, quotas et contention des tests, puis augmenter seulement si les résultats le justifient. Les missions de lecture peuvent avancer pendant qu'un build lourd occupe l'unique ressource prévue pour ce type de travail.

## 6. Une preuve porte sur le SHA final et les effets réellement contrôlés

Un dossier de preuve doit identifier au minimum :

| Groupe | Données nécessaires |
|---|---|
| Sujet | Tâche, tentative, dépôt, SHA candidat, SHA de base et empreinte de l'arbre Git |
| État de travail | Arbre propre, ou inventaire complet et empreintes des modifications non commises ; présence de fichiers non suivis pertinents |
| Environnement | OS/architecture, versions du compilateur et du runtime, outils de test, dépendances verrouillées et configuration non secrète |
| Entrées de test | Version et empreinte du corpus, paramètres, fixtures et services simulés ou réels |
| Exécution | Commande exacte, répertoire, début/fin, code de sortie et statut du processus |
| Résultat | Tests découverts/exécutés, succès, échecs, exclusions et raison ; assertions métier contrôlées |
| Artefacts | Emplacement, empreinte, type, rétention et règles de confidentialité |
| Décision | Relecteur, conclusions motivées, réserves et autorité d'acceptation |

Le chemin ou le nom d'un fichier ne suffit pas à identifier sa version. Une attestation doit relier un résultat à un sujet immuable. Le modèle public in-toto formalise notamment ce lien par des empreintes d'artefacts ; il constitue une référence possible pour le format, sans imposer tout son écosystème au produit. [Spécification in-toto Statement v1](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md).

La vérification décisive s'exécute sur le **candidat final intégré à sa base prévue**, puis la revue examine ce même candidat. Toute correction après la revue invalide au moins les preuves et avis affectés. Un rebase, un merge ou une modification du corpus doit être évalué ; on ne réutilise pas une preuve parce que le titre de PR ou le nom de branche reste identique. Les contrôles GitHub eux-mêmes se rattachent à un commit identifié : leur rattachement ne dispense pas de vérifier quelles commandes et assertions ont réellement tourné. [API officielle des check runs](https://docs.github.com/en/rest/checks/runs).

Un test réussi sur des modifications non commises peut fournir un diagnostic, mais ne valide pas automatiquement un futur commit. La gate exige une preuve correspondant exactement à l'arbre de livraison. Les horodatages seuls et les phrases « tests OK » sont insuffisants.

## 7. Revue indépendante et protection des critères

Un agent implémente ; **un autre agent** relit. Le relecteur accède à l'objectif, aux critères, au diff complet et aux résultats bruts. Il recherche aussi les omissions, les changements hors périmètre, les erreurs de sémantique et les preuves qui pourraient passer sur une implémentation incorrecte. Il peut demander une vérification supplémentaire motivée ; il n'a pas à multiplier les tests sans lien avec un risque.

Le relecteur ne reprend pas simplement le résumé de l'auteur et n'approuve pas ses propres changements. S'il devient nécessaire qu'il corrige directement le candidat, un autre relecteur indépendant doit examiner la révision résultante. La correction des remarques revient normalement à l'agent d'implémentation, avec réponse point par point et nouvelles preuves ciblées.

Les invariants et les résultats attendus sont établis depuis l'exigence, des spécifications publiques et des exemples autonomes autorisés. Les tests peuvent évoluer pour une raison fondée, mais il est interdit de supprimer un cas gênant, diminuer une assertion, régénérer une référence ou remplacer le chemin réel par un mock afin d'obtenir du vert. Toute modification d'un test d'acceptation doit expliquer son motif, son effet sur la couverture et recevoir une revue distincte.

Le plan doit prévoir des contre-exemples : erreurs d'import, valeur limite, refus d'accès, annulation ou entrée invalide selon le domaine. Lorsque le risque le justifie, montrer qu'une variante volontairement erronée échoue permet de vérifier la capacité du test à détecter la régression. Un pourcentage de couverture n'établit pas à lui seul cette capacité.

L'auteur ne peut ni modifier sa propre politique de gate, ni fabriquer un résultat de contrôle pour fermer sa tâche. Les permissions du runner de test, du validateur d'état et du mécanisme d'intégration doivent matérialiser cette séparation. La formulation dans un prompt ne constitue pas un contrôle suffisant.

## 8. Gate par bloc et progression sans contournement

La gate `G-Bxx` porte sur un **ensemble intégré**, pas sur l'addition de rapports de tâches. Elle vérifie les contrats internes, les interactions avec les blocs déjà acceptés et les scénarios utilisateurs du bloc. Les tests d'une bibliothèque isolée ne remplacent pas les parcours de l'application assemblée.

La décision exige :

1. Toutes les tâches requises acceptées avec leurs preuves valables.
2. Le candidat du bloc et sa base d'intégration identifiés.
3. Les vérifications obligatoires réellement exécutées et réussies sur ce candidat.
4. Une revue indépendante sans défaut bloquant non résolu.
5. Les limites, opérations de migration et moyens de retour arrière documentés et exercés selon le risque.
6. La décision de l'autorité de gate prévue par le plan, humaine pour les arbitrages produit/livraison qui lui sont réservés.

Une gate peut être évaluée automatiquement pour des critères déterministes ; cela ne donne pas à l'auteur le droit de s'approuver. Les gates métier peuvent exiger une recette humaine. La nature de chaque gate est fixée avant exécution et ne change pas pour accélérer un lot en difficulté.

**Un `FAIL` ou `BLOCKED` d'une vérification obligatoire maintient la gate fermée.** Un défaut préexistant est conservé et attribué ; il n'est pas transformé en succès. Si un contrôle n'est réellement pas applicable, cette décision appartient à une révision explicite de la politique, avec justification et contrôle compensatoire éventuel, examinée indépendamment. Le résultat historique en échec demeure visible. L'agent ne peut pas décider seul d'exclure le test après l'avoir vu échouer.

Ni l'ouverture d'une PR, ni sa fusion, ni l'expiration d'un délai, ni la clôture d'une issue ne valent preuve de gate. Les branches de livraison et dépendances entre blocs doivent empêcher mécaniquement la progression lorsque la gate requise reste fermée. Les blocs indépendants peuvent continuer si leurs propres préconditions sont satisfaites.

## 9. Échec, arrêt et reprise

Les réparations sont bornées par un nombre de tentatives et un budget. Deux échecs identiques sans nouvel élément ne doivent pas déclencher indéfiniment la même action. Le diagnostic distingue défaut produit, test instable, environnement absent, quota, dépendance et erreur de planification. Un test instable conserve ses échecs ; une relance réussie n'efface pas le problème.

Un arrêt contrôlé procède ainsi :

1. Empêcher de nouveaux départs pour le périmètre concerné.
2. Demander l'arrêt des seules tentatives possédées par l'ordonnanceur.
3. Capturer le SHA, les modifications, les commandes en cours, les artefacts et les effets persistants connus.
4. Marquer les résultats interrompus comme non acquis et invalider les baux concernés.
5. Conserver un point de reprise qui indique ce qui doit être vérifié avant tout nouvel effet.

Ne jamais terminer globalement tous les processus d'un langage ou d'un outil sur une machine partagée. La gestion des processus doit utiliser des identifiants et groupes créés pour la tentative, et tenir compte des sous-processus.

Au redémarrage, vérifier propriétaire, génération de bail, état Git, artefacts, effets externes et dernière révision du plan. Les compilations peuvent être relancées si elles sont reproductibles ; une publication, une migration de données ou un déploiement demande d'abord de déterminer si l'effet a déjà eu lieu. Une clé d'idempotence et un registre d'effet préviennent les doublons. Le texte d'une conversation ne suffit pas comme checkpoint durable.

## 10. Replanification et retour arrière

Redécouper une tâche crée des enfants avec des identifiants nouveaux et conserve les critères du parent. Les preuves déjà acquises sont rattachées aux parties qu'elles couvrent ; les écarts restent visibles. Le parent est marqué remplacé ou suspendu selon la politique et ne doit plus être exécuté en concurrence avec ses enfants. Les dépendances sortantes sont révisées explicitement.

Changer la portée, abandonner un critère ou changer une architecture n'est pas une réparation automatique. La proposition contient cause, options, impacts, coût consommé et décision nécessaire. Les travaux sans dépendance à cette décision peuvent avancer ; les autres restent bloqués.

Le retour arrière utilise les versions de **la nouvelle plateforme**, ses artefacts, son format de projet et ses sauvegardes. Il ne repose pas sur une installation PC SOFT. Prévoir distinctement restauration de code, retour de configuration et compensation des données : un revert Git ne récupère pas une colonne supprimée et ne retire pas un message déjà envoyé. Les opérations irréversibles ou publiées sont identifiées avant la gate, avec sauvegarde/restauration ou stratégie de compensation testée.

## 11. Vérifier l'orchestrateur avant de lui déléguer le plan

Son propre banc d'essai doit comprendre : double attribution simultanée, bail expiré avec ancien agent encore actif, résultat tardif, crash après effet avant confirmation, reprise après interruption, mutation concurrente du plan, dépendance absente/cycle, gate fermée, preuve d'un autre SHA, arbre sale et relecteur identique à l'auteur.

Il faut également tester qu'une tâche ne peut pas modifier ses critères, que le périmètre d'écriture est appliqué, qu'un échec obligatoire bloque l'intégration et qu'une replanification conserve les engagements. Les premières épreuves utilisent un dépôt et des données jetables propres à ce projet. Aucun plan documentaire n'active implicitement une routine, un service permanent ou une connexion à un autre projet.

Les journaux doivent permettre de reconstituer attribution, exécution, vérification, revue, décision et intégration, avec leur ordre et leurs révisions. Le magasin d'état doit protéger les transitions concurrentes ; choisir base transactionnelle ou autre implémentation après expérimentation. La présence d'un fichier d'événements ne suffit pas à assurer sa lecture, sa cohérence ou sa capacité de reprise.

## 12. Tableau de bord et première utilisation

Afficher par bloc : tâches prévues/acceptées/bloquées, gate, candidat évalué et preuves manquantes. Afficher par tentative : propriétaire, âge, bail, budget consommé, dernier événement et prochaine action. Séparer temps actif, attente d'environnement, attente de dépendance et attente de décision. Les dépenses et la qualité du résultat sont plus utiles qu'un simple compteur d'agents actifs.

La première mise en œuvre doit démontrer un petit bloc de bout en bout : une tâche, une seconde tâche dépendante, une revue distincte, une preuve sur SHA final et une gate qui refuse volontairement un contrôle manquant. L'élargissement vient après cette preuve et l'essai d'arrêt/reprise. Tant que ces essais ne sont pas réalisés, l'état public reste **planifié / non exécuté**.
