# Améliorations proposées et différenciation vérifiable

Recherche arrêtée au 26 octobre 2026. Ce chapitre est une proposition de produit, pas une évaluation par essai comparatif de WINDEV. Chaque idée doit être validée avec des projets et des équipes représentatifs. Une fonction existante chez PC SOFT peut être améliorée par un contrat plus ouvert, une mesure précise ou une meilleure continuité de migration ; il serait trompeur de la présenter comme absente.

## 1. Positionnement recommandé

La promesse centrale doit être : **« Vos sources WLangage restent votre point de travail ; chaque compatibilité annoncée est démontrée et chaque écart est localisé. »** Le produit doit d'abord réduire les modifications nécessaires et la durée de retour à une application fiable. Une liste de nouvelles technologies ne constitue pas à elle seule un avantage pour les développeurs qui maintiennent une application de gestion depuis quinze ans.

Ne pas revendiquer « nous apportons Git, les tests, l'IA, l'audit ou le rechargement à chaud » comme si ces concepts étaient absents. La documentation PC SOFT traite déjà Git, tests automatisés, audits, profilage et télémétrie ; l'annonce 2026 cite IA conversationnelle, audit de sécurité et Hot Reload. Les variantes historiques/SaaS et les cibles doivent être distinguées. [Tests sur exécutable](https://doc.windev.com/en-US/?2019029=), [Mises à jour WINDEV 2025](https://doc.pcsoft.fr/fr-GEN/?9000050=&verdisp=300), [Annonce officielle 2026](https://forum.pcsoft.fr/fr-FR/pcsoft.fr.windev/278021-pcsoft-version-2026-windev-webdev-windev-mobile-est/read.awp).

**Décision proposée :** privilégier trois avantages fondateurs : une migration mesurable, des projets entièrement exploitables avec les outils standards et une liberté durable de compilation/exploitation. Les autres innovations se greffent sur ces bases. Le tableau ci-dessous décrit les preuves nécessaires, sans affirmer que PC SOFT ne pourrait pas fournir certaines capacités comparables.

## 2. Quinze améliorations concrètes

### A01 — Rapport de compatibilité expliqué jusqu'à la ligne

À l'import, construire le graphe des objets, API, propriétés, événements, dépendances et accès aux données. Chaque élément reçoit un statut : reconnu, implémenté mais non qualifié sur cette cible, testé sur corpus, écart connu, dépendance externe, conversion manuelle requise. Un lien ouvre la source et la preuve associée.

Le rapport distingue code repris sans modification, écrans fidèles, données converties et scénarios métier validés. Un blocage unique doit rester visible même si 99 % des références sont reconnues. L'estimation de migration affiche ses hypothèses et son intervalle, avec l'impact des composants sans sources et des usages dynamiques non résolus.

**Preuve d'acceptation :** sur un jeu de projets de référence, aucun appel connu comme non implémenté ne passe en statut compatible ; chaque diagnostic peut être relié à un test ou à une raison d'incertitude. **Dépendance :** inventaire d'API et analyse sémantique. **Risque :** faux sentiment de sécurité si le dénominateur compte seulement des lignes de code.

### A02 — Comparaison automatique avec l'application d'origine

Un enregistreur capture entrées, événements observables, appels contrôlés, résultats et effets de données. Le même scénario est rejoué dans un environnement isolé sur la version d'origine et le nouveau moteur. La comparaison présente le premier écart pertinent : calcul, focus, ordre d'événements, requête, donnée modifiée ou pagination.

Les horloges, aléas, fichiers et services tiers doivent être injectables ou enregistrés. Les opérations de paiement, d'envoi et de production restent simulées dans la recette. Les captures d'écran complètent les assertions métier ; elles ne les remplacent pas.

**Preuve :** un scénario injectant une différence volontaire de total ou d'ordre d'événements échoue avec une localisation utile. **Dépendance :** environnement original autorisé et instrumentable. **Limite :** les composants non déterministes exigent une normalisation déclarée ; toute tolérance doit être visible.

### A03 — Projet texte complet, stable et réversible

Publier un schéma de projet pour le code, les fenêtres, les états, les données, les événements, les ressources et les configurations. Utiliser des identifiants stables, un ordre de sérialisation déterministe et des fichiers limités à des responsabilités cohérentes. Les parties non reconnues d'un import sont conservées dans un compartiment opaque avec provenance et empreinte.

La différence recherchée n'est pas « avoir Git », puisque l'écosystème le permet déjà : c'est garantir qu'une édition indépendante du projet ne dépend pas d'un blob impossible à interpréter pour les éléments pris en charge. Le format ouvert doit être versionné, accompagné d'exemples et d'un validateur utilisable sans IDE.

**Preuve :** ouvrir/sauver sans modification produit un diff nul ; un changement de libellé ne réécrit pas toute la fenêtre ; une migration de format peut revenir à sa représentation précédente lorsqu'elle est déclarée réversible. **Risque :** promettre la réversibilité vers un format propriétaire opaque serait injustifié. Le retour garanti porte d'abord sur le format propre du produit et sur les originaux conservés.

### A04 — Fusion sémantique et visuelle des interfaces

Lors de changements concurrents, comparer propriétés et événements par identifiant, indépendamment de leur position dans un fichier. Présenter « libellé modifié par A », « validation modifiée par B », « champ supprimé et encore référencé » et afficher l'aperçu de la fusion. Résoudre explicitement les collisions de noms, les déplacements et les suppressions.

**Preuve :** deux développeurs modifient des champs distincts sans conflit artificiel ; une suppression opposée à une modification déclenche un conflit réel ; les tests de compilation et de scénario s'exécutent après résolution. **Dépendance :** schéma stable et AST conservant commentaires/formatage. **Risque :** une fusion automatique ne peut pas déduire toutes les intentions métier.

### A05 — Compilateur autonome et compilation reproductible

Fournir CLI, version épinglée du compilateur/runtime, verrouillage des dépendances, manifeste d'entrées et génération automatisable sans interaction graphique. Le client peut reconstruire la version livrée à partir du dépôt, avec les droits de redistribution des dépendances explicités. La politique de licence proposée garantit la continuité d'exécution et une procédure durable de reconstruction des versions acquises ; ses conditions exactes doivent être contractualisées.

**Preuve :** deux environnements de construction propres produisent des artefacts identiques quand les outils et formats le permettent ; les variations de signature/horodatage sont isolées et expliquées. **Bénéfice :** audit, reprise d'activité et indépendance de l'IDE. **Risque :** la signature et les chaînes propriétaires mobiles imposent leurs propres contraintes.

### A06 — WLangage utilisable dans plusieurs éditeurs

Exposer complétion, références, diagnostics et refactorisations via LSP ; proposer le débogage par DAP quand le moteur le permet. Le protocole LSP vise précisément à séparer services de langage et éditeurs : il fournit une base d'intégration plutôt qu'une obligation de réécrire un IDE pour chaque hôte. [Spécification officielle LSP](https://microsoft.github.io/language-server-protocol/).

**Proposition :** atelier visuel complet pour la transition, extension d'éditeur pour le travail principalement en code et outils CLI pour la CI. La parité des services doit être testée ; le concepteur de fenêtres peut rester une fonction spécifique de l'atelier. **Preuve :** une même erreur renvoie le même code et la même localisation dans l'IDE, la CLI et l'extension. **Limite :** une interface protocolaire ne rend pas les éditeurs visuels portables automatiquement.

### A07 — Modernisation progressive avec variantes comparables

Conserver un rendu de référence puis permettre thèmes, densités, conteneurs flexibles, dispositions web/mobile et composants accessibles par écran. Prévisualiser la variante à côté de l'original avec noms et procédures partagés. Produire une liste de différences fonctionnelles attendues, pas seulement un changement de couleur.

**Preuve :** une équipe modernise une fenêtre pilote, annule la variante et retrouve le comportement de référence ; les procédures métier ne divergent pas entre versions. **Risque :** les règles de focus, validation et événement peuvent changer avec la disposition. Le thème moderne doit donc rester une évolution révisable jusqu'à sa recette.

### A08 — Accessibilité contrôlée dans l'éditeur

Ajouter diagnostics de nom accessible manquant, contraste, ordre de tabulation incohérent, cible trop petite et information transmise uniquement par la couleur. Relier chaque diagnostic à l'objet et proposer un correctif. Les critères WCAG sont formulés de manière testable et indépendante des technologies ; ils peuvent guider les exigences web. [WCAG 2.2, W3C](https://www.w3.org/TR/WCAG22/).

**Proposition :** bibliothèque de composants accessible, tests clavier et lecteurs d'écran, recettes avec utilisateurs et rapport exportable. **Preuve :** les problèmes connus du corpus sont repérés et les parcours prioritaires restent réalisables sans souris. **Limite :** aucun scanner automatique ne suffit à certifier toutes les obligations d'accessibilité ; les règles natives et web doivent être distinguées.

### A09 — Observabilité ouverte, corrélée au WLangage

Chaque action UI peut être reliée à une procédure, un appel service et une requête au moyen d'un identifiant de corrélation. Fournir traces, métriques et journaux exportables vers le système du client. OpenTelemetry fournit des composants et conventions pour collecter/exporter plusieurs signaux ; il ne constitue pas à lui seul un stockage ou une interface complète d'observabilité. [Présentation officielle OpenTelemetry](https://opentelemetry.io/docs/what-is-opentelemetry/).

**Proposition :** affichage des procédures WLangage dans les traces, échantillonnage, masquage des paramètres, collecte locale possible et activation explicite. **Preuve :** remonter d'une lenteur utilisateur à une requête et à sa ligne d'origine sur un scénario contrôlé. **Risque :** fuite de données dans les traces ; les valeurs sensibles doivent être exclues avant export.

### A10 — Transactions, migrations de données et droits explicables

Afficher ce que fait un accès implicite : contexte HFSQL utilisé, transaction active, paramètres, origine de la liaison et contraintes. Générer une migration de schéma relisible, avec analyse de perte, sauvegarde et retour arrière lorsque c'est techniquement possible. Pour les droits, présenter les règles applicables et la raison d'un refus.

**Preuve :** un développeur peut expliquer pourquoi une écriture a lieu et pourquoi un utilisateur n'accède pas à un écran ; une migration destructrice ne s'applique pas sans étape explicite. **Différenciation recherchée :** visibilité et contrôle de la sémantique, pas remplacement systématique de HFSQL par un autre moteur. **Risque :** un changement de moteur modifie tri, verrouillage ou NULL ; la preuve exige des tests différentiels.

### A11 — Assistant IA gouverné et facultatif

Proposer recherche dans le projet, explication d'un traitement, génération de tests et préparation de correctifs. Choisir un fournisseur autorisé, un modèle local ou aucun assistant. L'IA ne participe pas de manière obligatoire à la compilation ni à l'exécution de l'application.

L'assistant fournit les fichiers qu'il a consultés, produit un diff révisable et exécute les tests appropriés. Il ne doit pas annoncer une compatibilité parce qu'une traduction générée semble plausible. Les prompts externes excluent secrets et données de production selon une politique configurable ; coût et volume sont visibles.

**Preuve :** l'IDE et les builds fonctionnent sans réseau IA ; les changements générés sont attribuables et annulables ; un cas non pris en charge reste signalé même si l'assistant sait proposer une adaptation. **Risque :** divulgation de propriété intellectuelle et corrections silencieusement sémantiques.

### A12 — Composants et extensions avec contrats stables

Définir API d'extension, versionnement sémantique, compatibilité du moteur, licences, signatures, dépendances, permissions et tests de contrat. Séparer extensions d'éditeur, composants d'application, connecteurs et moteurs de rendu. Une galerie peut être auto-hébergée et filtrée par politique d'organisation.

**Preuve :** une extension désactivée ne corrompt pas un projet ; un connecteur annonce précisément ses capacités ; une mise à jour incompatible est bloquée avant déploiement. **Risque :** confondre composants WLangage avec sources et composants binaires propriétaires. Ces derniers nécessitent une stratégie spécifique, et parfois leur remplacement.

### A13 — Contrats de compatibilité et support à long terme

Publier les versions du langage, options sémantiques, bibliothèques et cibles couvertes. Chaque correction peut être activée sous un profil de compatibilité ; toute rupture a un cas de test, une note de migration et une période d'adaptation. Des versions LTS du compilateur et du runtime sont proposées avec une durée de maintenance annoncée.

**Preuve :** le corpus d'une version stable reste valide sur sa branche de maintenance ; une mise à jour ne modifie pas silencieusement l'évaluation d'une expression. **Risque :** conserver indéfiniment des défauts crée une dette ; distinguer le comportement de référence des correctifs de sécurité obligatoires, avec procédure d'impact.

### A14 — Migration par modules et retour arrière opérationnel

Permettre de déplacer un lot métier ou un service avant de réécrire tout l'atelier. Définir des frontières explicites de données et de transactions entre ancien et nouveau modules. Prévoir coexistence, observation des écarts, activation par population et retour vers le module d'origine.

**Preuve :** un pilote peut être retiré sans désynchroniser les données. **Dépendance :** contrats d'API et stratégie d'écriture uniques. **Risque :** la double écriture n'est pas une stratégie suffisante : elle introduit des divergences difficiles à réparer ; chaque cas exige journalisation, idempotence et réconciliation définies.

### A15 — Documentation et assistance reliées aux preuves

Chaque API prise en charge doit avoir signature, contraintes de cible, comportement d'erreur, différences connues, exemples originaux et tests de contrat. L'aide contextuelle doit afficher le profil courant et prévenir lorsqu'un exemple vise une autre version. Un incident peut exporter un petit cas reproductible avec secrets retirés.

**Preuve :** un diagnostic mène à une page décrivant exactement le statut rencontré ; l'exemple s'exécute en CI ; une fonction non qualifiée ne possède pas une page promettant la parité totale. **Bénéfice :** la documentation participe à la réduction du risque de migration, au lieu d'être séparée du moteur.

## 3. Priorisation proposée

| Vague | Améliorations | Pourquoi cet ordre |
|---|---|---|
| Fondations | A01, A03, A05, A13, A15 | Sans format, diagnostic et contrat de version, aucune promesse n'est vérifiable |
| Pilote métier | A02, A07, A10, A14 | Prouver reprise fonctionnelle et capacité à livrer/retirer un premier lot |
| Travail en équipe | A04, A06, A09, A12 | Réduire les coûts récurrents de maintenance et d'intégration |
| Qualité continue | A08 dès les composants initiaux, puis élargissement ; A11 optionnel | Éviter la dette d'accessibilité ; maintenir l'IA comme service indépendant |

Le classement ne constitue pas un chiffrage. Un pilote très orienté impressions peut placer le moteur d'états avant la fusion visuelle ; une application mobile hors ligne peut placer la synchronisation avant les extensions. La priorité se décide par blocages réels, fréquence et coût de correction, pas par nombre de fonctions dans une brochure.

## 4. Mesures permettant de juger le produit

Suivre le pourcentage d'objets importés sans perte connue, les appels résolus, la part de source préservée, les scénarios métier validés, les écarts visuels et d'impression, les blocs non qualifiés et la quantité de modifications manuelles. Les compteurs doivent toujours afficher leur dénominateur et ne pas mélanger reconnaissance syntaxique et comportement vérifié.

Pour la productivité, mesurer les tâches décrites dans le document UX : retrouver un événement, ajouter une rubrique, déboguer une erreur et générer une version. Pour l'exploitation, mesurer temps de build propre/incrémental, taille, démarrage, mémoire, latence, fiabilité, installation et retour arrière sur la configuration de référence. Pour l'ouverture, faire valider qu'une équipe indépendante peut reconstruire et maintenir une application sans accès à l'IDE commercial.

Éviter d'annoncer des gains comme « migration automatique à 100 % », « cinq fois plus rapide » ou « compatible avec tout WINDEV » avant une étude sur corpus. Publier les résultats par type d'application, version source et cible ; conserver les échecs dans le jeu de tests. Le véritable progrès recherché est une décision de migration mieux informée et une diminution démontrée du travail manuel.

## 5. Limites de la comparaison et sources

Les références PC SOFT prouvent l'existence de fonctions et de parcours, pas leur qualité relative à une solution qui n'a pas encore été construite. Aucun banc d'essai de performance, d'ergonomie ou de compatibilité avec une application client n'a été réalisé dans cette recherche. L'état de chaque édition, build et licence reste à contrôler au démarrage d'un projet concret. Les propositions ci-dessus doivent donc être testées, et ne constituent pas des reproches factuels à l'éditeur.

Sources primaires complémentaires : [Documentation PC SOFT](https://help.windev.com/fr-FR/), [Référentiel LSP](https://microsoft.github.io/language-server-protocol/), [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [OpenTelemetry](https://opentelemetry.io/docs/what-is-opentelemetry/). Les faits PC SOFT spécifiques sont cités près de leur utilisation ; toutes les idées A01 à A15 sont des recommandations de conception.
