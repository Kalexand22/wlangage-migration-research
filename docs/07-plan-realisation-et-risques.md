# Plan de réalisation, validation et maîtrise des risques

Date de l'étude : **26 octobre 2026**. **Le plan opérationnel actualisé est le [chapitre 16](16-plan-detaille-de-realisation.md) : base C#, multi-BDD, tickets d’agents et gates.** Le scénario budgétaire long ci-dessous est conservé comme hypothèse de plateforme étendue, sans devenir une estimation calendaire du nouveau backlog. Ce chapitre est une **proposition de conduite du programme**, pas le compte rendu d'une implémentation existante. Aucun projet client, installation WINDEV, périphérique ou serveur HFSQL n'a été testé pour cette étude. Les seuils ci-dessous sont des critères de départ à contractualiser avec les pilotes.

**Contrainte ferme : aucun outil, DLL, framework, SDK, pilote, serveur ou pont PC SOFT dans toute la chaîne, y compris import, build, CI, tests et référence de comparaison.** Aucune exécution d'un original PC SOFT n'est déléguée à un client pour notre workflow. On utilise code original, outils tiers non PC SOFT, spécifications publiques et fichiers/exports/fixtures/traces déjà fournis avec provenance. Aucun export ou conversion par outil PC SOFT n'est demandé.

Les seuils illustratifs sont rapprochés par stade dans le [registre de décision](../data/seuils-decision.csv). Ils restent non validés jusqu’à leur choix avant un essai sur un profil précis ; voir les [améliorations immédiates](12-ameliorations-immediates.md).

## 1. Résultat à financer et première décision

Le premier résultat attendu est une **preuve de faisabilité de reprise du WLangage**, réalisée avec du code original autonome. A conserve les traitements dans un compilateur/runtime indépendants avec exclusion PC SOFT dès le départ. Conversion ou réécriture B reste une alternative si la reprise du code échoue, sous la même exclusion. Le modèle commercial, la publication et la redistribution ne sont pas des préalables au codage autonome.

Le programme comporte deux étages : **prototype autonome, inventaire et cas synthétiques originaux**, puis **comparaison aux preuves passives disponibles et élargissement de la couverture**. Aucun oracle PC SOFT n'est exécuté. Documentation publique et fixtures/traces déjà fournies fondent les attendus ; leurs lacunes sont publiées. Sans preuve sur un comportement, on maintient l'inconnu plutôt que promettre une parité totale.

Le scénario des phases P1–P6 ci-dessous concerne la plateforme A si les preuves techniques justifient son élargissement. Il suit l'[architecture à prototyper](05-architecture-cible.md) : IR WLangage, runtime original, backend .NET candidat et Windows/WinForms en premier. Ces essais peuvent commencer sans WINDEV ni framework PC SOFT. Le scénario long n'est pas une décision d'investissement et ne chiffre pas une réécriture B.

La couche données cible plusieurs moteurs : PostgreSQL et SQLite au premier gate réel, SQL Server ensuite, chacun avec pilote non PC SOFT et admission propre. La couche `H*` doit être développée et testée indépendamment. La conservation de HFSQL, d'un driver PC SOFT ou d'un pont vers l'original appartient aux stratégies comparées **exclues**, même en transition ; elle ne constitue jamais une réponse à un blocage dans ce plan.

### Périmètre admis, exclusions et provenance

Le [contrat WINDEV, article 4](https://doc.pcsoft.fr/fr-FR/?4510001=&name=License_WINDEV), et la [licence du framework, article 3](https://doc.windev.com/fr-FR/?1000019581=&name=licence_framework_windev), encadrent des usages de produits qui sont exclus de notre chaîne. Leur applicabilité au code original autonome n'est pas démontrée ; aucun avis préalable au prototype n'est exigé par ce plan. Provenance des informations, droits sur les entrées et éventuelle diffusion future restent des sujets distincts, détaillés au [chapitre juridique](09-propriete-intellectuelle-et-licences.md).

| Entrée ou opération | Traitement dans le plan | Information à conserver |
| --- | --- | --- |
| Code original, outils tiers non PC SOFT, cas synthétiques et documentation publique | Démarrer le prototype et ses tests | Provenance, versions, dépendances transitives, résultats et limites |
| Fichiers/exports et fixtures/traces déjà disponibles | Lire comme données passives avec nos importeurs ; ne pas lancer les logiciels qui les ont produits | Empreintes, provenance, profil connu, couverture et informations manquantes |
| Format natif opaque ou composant compilé PC SOFT | Préserver l'inventaire ; bloquer la fonctionnalité si lecture/réimplémentation indépendante non disponible | Portion inconnue, impact, raison de blocage ; aucun exporteur/pont propriétaire en recours |
| IDE, compilateur, runtime, SDK, DLL, pilote, serveur HFSQL ou oracle PC SOFT, local ou délégué | **Exclu de toute étape**, même transitoirement | Détection dans le contrôle d'exclusion, suppression ou blocage du module |
| Commercialisation/diffusion ultérieure de notre produit autonome | Analyse ciblée du produit réel à cette étape | Sources, composants non PC SOFT, droits sur les entrées et destinataires |

La réponse à un blocage reste une correction originale, une réduction documentée du périmètre ou une réécriture explicite ; l'exclusion n'admet pas d'exception par licence ou autorisation de pont. Aucun avis juridique individualisé n'a été obtenu. La recherche et le prototype autonome continuent, sans reprendre une stratégie propriétaire exclue.

## 2. Corpus pilote à constituer

Commencer par les microprogrammes synthétiques originaux, puis rechercher des dossiers déjà disponibles de cinq applications, avec sources et preuves passives reçues légalement. Les nombres suivants décrivent **les dossiers à rechercher**, sans demander au détenteur de lancer PC SOFT pour les produire. Les modèles de données d'origine décrivent le patrimoine, pas les serveurs admis dans notre chaîne.

| Pilote | Profil recherché | Difficultés qu'il doit révéler | Mesures de sortie |
| --- | --- | --- | --- |
| A — gestion Windows | Fichiers déjà fournis : 30–100 fenêtres, 20–80 tables, code FR et export logique des données | Tables fichier, FAA, modalité, états ; reprise sur PostgreSQL | Parcours commande-facture-stock conforme au contrat et aux traces disponibles |
| B — application ancienne | Export texte ancien déjà fourni, ANSI, composants internes en source | Options historiques, fichiers externes, copies de tableaux, valeurs implicites | Conservation des sources et règles documentées ; binaire opaque bloquant sans lecteur indépendant |
| C — application concurrente | Sources et traces déjà fournies sur droits, transactions et traitements longs | Sémantique des verrous, reprise, timeouts à réimplémenter sur PostgreSQL | Invariants définis et contrats observables couverts, sans lancer le moteur d'origine |
| D — WEBDEV | Pages navigateur/serveur, AJAX, sessions, REST, authentification | Frontière client/serveur, réentrance, expiration, erreurs réseau | Parcours E2E, isolation des sessions, absence de fuite de secrets |
| E — WINDEV Mobile | Android puis iOS, collecte hors ligne, code-barres, photos | Permissions, tâches de fond, synchronisation et conflits | Reprise après déconnexion, périphériques réels et publication test |

Un pilote simple qui évite toutes les difficultés ne prouve pas la migration du parc. Stratifier les projets selon version, édition, options de compilation, cible, base, volume, langue, interop native et fonctions dynamiques. Faire apparaître les zones non représentées. Obtenir pour chaque application un propriétaire métier, un référent WINDEV et un référent données.

Entrées passives : fichiers sources et empreintes, métadonnées, analyse, ressources, états, requêtes, traductions et paramètres déjà disponibles ; inventaire documentaire des composants bloquants ; jeux synthétiques ou exports logiques anonymisés déjà fournis. Les installateurs ou exécutables PC SOFT ne sont pas lancés ni chargés pour validation. Le dossier signale les éléments absents, sans demander un export ou une observation supplémentaire par PC SOFT.

## 3. Jalons et portes de sortie

Le calendrier ci-dessous est **une hypothèse budgétaire séquentielle de 36 mois pour une plateforme A complète sur les pilotes**. Il suppose une équipe expérimentée et un corpus utilisable pour les phases de conformité. Il ne conditionne pas le démarrage du prototype à un avis juridique, à un modèle commercial ou à une décision de diffusion. Les étapes sont séquentielles pour rendre les efforts lisibles ; une parallélisation ne supprime pas le travail. La preuve de faisabilité initiale doit précéder tout engagement de cette ampleur. Si B est choisie, produire un plan propre au patrimoine.

| Phase | Fenêtre indicative | Équipe moyenne | Effort indicatif | Livrables et condition de passage |
| --- | --- | --- | --- | --- |
| P0 — cadrage technique et patrimoine | M0–M2 | 5–7 ETP | 10–14 personnes-mois | Prototype autonome, corpus synthétique, fichiers déjà fournis, provenance ; inconnues classées ; premier contrôle d'exclusion PC SOFT |
| P1 — preuve sémantique bornée | M2–M5 | 7–10 ETP | 21–30 personnes-mois | Parseur sans perte, profils, types et fonctions ; conformité aux règles publiques/fixtures reçues, comparaison des deux moteurs originaux et limites de preuve publiées |
| P2 — tranche Windows | M5–M11 | 10–14 ETP | 60–84 personnes-mois | Import fenêtre/données/état, IDE familiarisé, débogage WLangage, build CI; parcours complet A sur données de test |
| P3 — Windows pilote | M11–M18 | 12–18 ETP | 84–126 personnes-mois | API/champs, PostgreSQL et couche H* originale, concurrence, packaging/rollback ; pilotes acceptés dans le contrat annoncé, exclusion vérifiée |
| P4 — service et web | M18–M26 | 16–22 ETP | 128–176 personnes-mois | Services, séparation navigateur/serveur et première famille de pages; pilote D avec session/sécurité/performance validées |
| P5 — mobile et extension | M26–M36 | 20–30 ETP | 200–300 personnes-mois | Android/iOS sur périmètre annoncé, hors ligne, interop; pilote E et certification des profils publiés |
| P6 — couverture durable | Après M36 | À dimensionner sur le parc | Non chiffrable sans inventaire | Longue traîne API, états complexes, matériels, autres OS et nouvelles versions PC SOFT |

Total de l'hypothèse P0–P5 de plateforme A : **503–730 personnes-mois**. Ce total concerne les pilotes et l'industrialisation progressive, sans constituer une décision d'engagement, un devis exhaustif ou le prix d'une réécriture B. La preuve de concept initiale porte sur un sous-ensemble bien plus réduit ; son résultat permet de réestimer la suite avec débit observé, divergences et coût de maintenance.

Chaque passage de phase technique exige démonstration reproductible, rapport des écarts, limites des preuves et décision de périmètre. Le gate d'exclusion ci-dessous doit passer. Une dépendance PC SOFT découverte bloque le module jusqu'à retrait ; la faire exécuter par un tiers ne la rend pas acceptable. Un échec de conformité ne disparaît pas par reclassement en avertissement.

### Premier lot de 90 jours

1. J1–J15 : définir le sous-ensemble WLangage, écrire les cas synthétiques et les premiers types/parseur autonomes ; inventorier les métadonnées disponibles, préparer la collecte de provenance et les scénarios de comparaison.
2. J16–J30 : scanner les éléments, produire le manifeste et la carte des dépendances; conserver tous les fragments inconnus; choisir 50 microcas sémantiques à fort risque.
3. J31–J60 : compléter lexer/parseur, CST, profils, types et diagnostics ; faire fonctionner interprète et backend .NET originaux sur le même sous-ensemble ; comparer aux attendus publics et fixtures reçues, sans oracle PC SOFT.
4. J61–J75 : importer une fenêtre, une table, un événement et une requête, puis générer un état minimal; tester les événements et l'arrondi.
5. J76–J90 : démonstration reproductible et mesure du coût d'ajout d'une API/champ; décision poursuivre, concentrer la cible ou abandonner un chemin technique.

Ce lot ne se confond pas avec P1 terminé. Une entrée absente limite la mesure de conformité concernée ; elle ne bloque pas les expériences autonomes. Le lot doit permettre de mesurer ce qui fonctionne, ce qui diverge et ce qui demande encore une référence, avant de décider l'élargissement de l'atelier compatible.

## 4. Équipe et modèle de coût

Prévoir les compétences suivantes, avec cumul possible dans le noyau initial : direction technique des langages, ingénieurs compilateur/runtime, spécialiste WINDEV senior, développeurs concepteur/IDE, spécialiste UI Windows et impression, ingénieurs données/HFSQL, backend/web, mobile, QA automatisation, UX/accessibilité, sécurité/DevSecOps et documentation/support. Un expert fonctionnel client doit participer aux recettes; il n'est pas remplacé par un test de compilation.

Une allocation en régime établi peut consacrer 25 % au langage/runtime, 20 % à l'IDE/designer, 15 % aux données/intégrations, 15 % aux cibles, 15 % à QA/conformité et 10 % à sécurité, exploitation et documentation. Réviser cette répartition selon les goulets observés. Les personnes qui connaissent à la fois WLangage et les compilateurs constituent une capacité rare à sécuriser tôt.

Formule de cadrage :

```text
Budget = Σ(personnes-mois par rôle × coût mensuel complet du rôle)
       + licences/outils + machines et périphériques + infrastructure CI
       + conseil juridique + audits spécialisés + assistance pilotes
       + provision de risque explicitement affectée.
```

Pour le scénario de plateforme A seulement, une **hypothèse illustrative** de 9 000 à 16 000 € par personne-mois complet donne 4,53 à 11,68 M€ de travail pour 503–730 personnes-mois, avant postes additionnels et provision. Ces valeurs ne sont ni des tarifs PC SOFT ni des prix de marché vérifiés ni une offre commerciale. Remplacer chaque hypothèse par les coûts réels. Une provision de 20–35 % est un point de départ de planification, pas une preuve statistique. Ne pas additionner une seconde fois les mêmes charges déjà intégrées au coût complet. Aucun budget B n'est déduit de ces nombres.

Le coût récurrent inclut maintien des profils historiques, certification des nouvelles versions d'OS, mises à jour de dépendances, support, sécurité, tests de périphériques et enrichissement du catalogue. La couverture complète n'est pas un état acquis définitivement.

## 5. Système de preuves et contrôle d'exclusion

### 5.0 Gate technique : aucune dépendance PC SOFT

Exigence **à implémenter**, pas contrôle produit déjà livré : produire SBOM/inventaire transitif, liste positive d'outils tiers et empreintes, journal des processus enfants, modules/assemblages chargés, services/connexions requis et contenu du paquet. Exécuter import, build, UI, DAP, tests de données et packaging sur agent propre sans produit PC SOFT. Vérifier origine et dépendances, pas seulement le nom des DLL. Refuser tout outil, SDK, driver, serveur HFSQL, service ou pont PC SOFT local/distant, même indirect ou délégué. Un composant inconnu reste non approuvé jusqu'à identification.

La preuve de fonctionnement doit être reproductible avec outils non PC SOFT uniquement. Un chemin d'erreur, un plugin ou un test qui requiert PC SOFT fait échouer ce gate ; aucun avis ou licence supplémentaire ne lève la contrainte choisie.

### 5.1 Quatre dénominateurs à publier

Un score unique masque les lacunes. Publier séparément :

| Mesure | Dénominateur | Preuve nécessaire |
| --- | --- | --- |
| Import sans perte | Éléments effectivement présents dans le corpus | Inventaire avant/après, empreintes, comptage code et ressources, inconnus conservés |
| Source inchangée | Unités WLangage originales sélectionnées | Empreintes des octets ou diff explicite; conversions d'encodage rapportées séparément |
| Compatibilité API utilisée | Signatures, propriétés, événements et modes rencontrés | Tests par profil/version/cible et cas d'erreur; appel dynamique signalé |
| Compatibilité fonctionnelle | Scénarios et invariants métier acceptés | Recette différentielle données/UI/PDF et traces signées |

Le catalogue global du produit donne un cinquième indicateur : entrées certifiées / entrées inventoriées **dans une édition et un périmètre datés**. Un très bon score sur trois pilotes ne devient pas une couverture mondiale de WLangage.

### 5.2 Spécifications, preuves passives et cohérence des moteurs originaux

Pour chaque cas, qualifier l'attendu : règle publique citée, trace/fixture déjà fournie avec provenance, ou hypothèse encore à préciser. Exécuter uniquement notre moteur, puis comparer valeur typée, précision, erreurs, état et effets aux attendus disponibles. Enregistrer profil déclaré, contexte connu et lacunes. Les effets externes sont simulés ou capturés par des outils originaux/tiers non PC SOFT.

Exécuter aussi le cas dans notre interprète et notre backend compilé : leur accord vérifie la cohérence interne, sans exclure un défaut partagé du runtime. **Aucun WINDEV ou framework PC SOFT n'est exécuté comme oracle**, et aucune trace manquante n'est produite chez un client pour notre workflow. La conformité revendiquée se limite aux contrats et observations réellement couverts ; absence de référence ou option inconnue demeure visible.

Cas prioritaires : valeurs limites et nulles, décimaux, débordements, chaînes ANSI/Unicode, caractères combinés, indices, dates invalides, portée, référence/copie, ET/OU, procédures, exceptions, propriétés, ordre des événements, réentrance, curseurs, doublons et verrous. Un test d'erreur est aussi important qu'un résultat nominal. Employer tests génératifs et réduction automatique des cas défaillants; un millier de variantes d'une addition ne remplace pas un test du changement de portée.

### 5.3 Recette des interfaces et documents

Sur notre renderer autonome, capturer clavier, focus, validation, clic/double-clic, raccourcis, glisser-déposer, menus, FAA, tri/filtre et préférences. Comparer au contrat documenté et aux images/traces déjà fournies lorsque leur contexte est connu ; ne pas lancer l'original pour en produire. Tester DPI 100/150/200 %, écrans multiples et lecteur d'écran sur le périmètre annoncé.

Pour les états : comparer le contenu extrait, montants et pagination; comparer ensuite géométrie, polices, sauts et superpositions. Une tolérance initiale de 0,2 mm sur les éléments imprimés peut être choisie puis ajustée au cas métier; les chiffres, identifiants, signatures et codes-barres n'admettent pas une altération cachée dans une tolérance visuelle. Tester de vraies imprimantes, étiquettes et lecteurs lorsque le pilote en dépend. Le hash d'un PDF ne suffit pas, car les métadonnées ou identifiants internes peuvent varier.

### 5.4 Données, concurrence et résilience

Comparer comptages par table, clés et relations, totaux monétaires exacts, valeurs nulles/vides, types, blobs, dates et encodages. Produire des empreintes de lignes après une canonicalisation documentée, avec traitement explicite des champs non déterministes. Contrôler également ordre des parcours et équivalences de recherche selon les collations.

Injecter crash avant/après commit, coupure réseau, expiration de session, disque plein, restauration, conflit offline et reprise de tâche. Vérifier qu'une opération acquittée n'est pas perdue, qu'une opération rejouée n'est pas facturée deux fois et que les verrous sont libérés. Définir RPO/RTO par pilote, puis les mesurer lors d'un exercice; une sauvegarde jamais restaurée n'est pas une preuve de reprise.

### 5.5 Performance et sécurité

Mesurer démarrage, compilation froide/chaude, import, mémoire, tables, impression et p50/p95/p99 sur matériel et jeu fixés. La référence est un budget absolu métier ou une mesure passive déjà fournie avec méthode connue ; ne pas lancer PC SOFT pour la créer. Le ratio illustratif p95 < 1,2× n'a de sens que si cette référence préexistante est comparable ; sinon publier un budget absolu. Aucun score de parité de performance n'est déduit d'un historique insuffisamment décrit.

Tester séparation des privilèges, contrôle d'accès serveur, injection, sérialisation, secrets, dépendances, accès disque/réseau des extensions et confinement des compilations dynamiques. Structurer les pratiques de développement sécurisé à partir du [NIST SSDF, SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final), sans confondre conformité à un processus et absence de vulnérabilité.

## 6. Déploiement progressif et retour arrière

Pour chaque pilote : sauvegarde restaurable, version applicative et runtime verrouillées, empreintes des artefacts, plan de changement du schéma, utilisateurs pilotes, surveillance et procédures d'escalade. Livrer d'abord en environnement de recette, puis à un groupe limité avec un responsable métier joignable.

Le retour arrière décrit ici vise une **version précédente de notre plateforme autonome**, sans runtime PC SOFT. Il reste simple seulement si les données sont compatibles ; préférer des changements de schéma additifs. Tout changement destructif exige sauvegarde PostgreSQL, reprise et réconciliation éprouvées avec outils non PC SOFT. Un retour qui nécessiterait de relancer l'application PC SOFT d'origine est hors périmètre.

Dans le protocole prévu, seules des instances de moteurs indépendants admis (PostgreSQL et SQLite initiaux) et des données de recette autorisées sont utilisées ; aucun service PC SOFT n'est sollicité pour une comparaison ou une réplication. La bascule métier ultérieure doit disposer de données d'entrée déjà disponibles et d'une procédure de reprise compatible avec l'exclusion. Si le retour exige de lancer PC SOFT dans notre workflow, ce plan de retour est exclu et la bascule reste bloquée jusqu'à définition d'une autre réponse.

Déclencheurs de repli proposés : perte/intégrité de données, erreur de montant, accès indu, incident critique, hausse de latence dépassant le seuil convenu ou taux d'échec d'un parcours essentiel. Le repli comprend arrêt des écritures, sauvegarde de l'état atteint, réconciliation et contrôle métier avant réouverture. Ne pas restaurer aveuglément une ancienne base en effaçant les opérations valides déjà réalisées.

## 7. Registre de risques initial

Probabilités et impacts sont des **appréciations initiales qualitatives**, à recalibrer après les pilotes. « Élevé » n'est pas un pourcentage observé.

| Risque | Probabilité / impact | Signal précoce | Réduction et réponse | Responsable |
| --- | --- | --- | --- | --- |
| Formats natifs insuffisamment lisibles | Élevée / critique | Métadonnées absentes des fichiers/exports déjà fournis | Importeurs originaux, portions opaques préservées et blocages explicites ; aucun exporteur/convertisseur PC SOFT en recours | Import |
| Options de compilation historiques perdues | Élevée / critique | Même source, résultat divergent | Profils explicites, tests ET/OU/portée/copie; bloquer profil inconnu | Langage |
| Sémantique dynamique non détectée | Élevée / élevée | Appels résolus uniquement en production | Traces autorisées, analyse conservatrice, runtime contrôlé, diagnostic actionnable | Runtime |
| SQL confondu avec les contrats H* | Élevée / critique | Différences de recherche, tampon ou verrouillage | Couche originale sur PostgreSQL, règles publiques/fixtures passives et limites visibles ; pas de pilote, serveur HFSQL ou pont de secours | Données |
| Ordre des événements différent | Élevée / critique | Double validation, fenêtres bloquées | Traces événements, tests réentrance et modalité | UI |
| Pagination ou précision financière altérée | Élevée / critique | État visuellement proche mais totaux faux | Comparaison structurée + géométrie + recette imprimée | Reporting |
| Composant externe sans source | Élevée / élevée | Uniquement DLL ou composant compilé | Réutilisation autorisée via contrat documenté ou remplacement annoncé; pas de promesse de recompilation | Interop |
| Dépendance COM/ActiveX Windows | Élevée / élevée | Blocage web/mobile/Linux | Isoler adaptateur Windows, diagnostic cible, alternative explicite | Plateforme |
| Applicabilité d'une clause aux travaux autonomes originaux | Non démontrée ; pas de classement critique automatique | Une condition serait invoquée alors que le prototype n'utilise ni WINDEV ni framework PC SOFT | Conserver provenance et inventaire des dépendances ; poursuivre le prototype autonome ; vérifier l'acte précis si un doute concret apparaît | Architecture |
| Provenance/couverture insuffisante des traces reçues | À constater sur chaque dossier / élevée | Profil ou méthode inconnus ; observation manquante | Déclarer la limite, retrouver les métadonnées déjà disponibles, compléter par spécification ou laisser bloquant ; aucune nouvelle exécution PC SOFT demandée | QA |
| Dépendance PC SOFT directe ou transitive | À contrôler / blocage ferme | Outil, DLL, SDK, pilote, serveur, service ou pont dans un chemin import/build/test/exécution | Gate SBOM/processus/modules/services ; retirer ou remplacer par du code original ; aucune exception transitoire ou délégation client | Architecture / CI |
| Budget de longue traîne sous-estimé | Élevée / critique | Coût par API/champ croissant | Mesurer débit, trier par usage, budget maintenance, réviser périmètre annoncé | Produit |
| Corps de tests trop simple | Élevée / élevée | Pilote passe, nouveau client échoue | Stratification du corpus, programme de pilotes, critères par profil | QA |
| Sources modifiées silencieusement | Moyenne / critique | Diff sans explication | Copie immuable, import sans perte, patchs séparés et revue | Import |
| Dual write incohérent | Moyenne / critique | Soldes et événements divergents | Autorité d'écriture unique, idempotence, réconciliation | Données |
| Perte au retour arrière autonome | Moyenne / critique | Schéma incompatible avec notre release autonome précédente | Migrations additives PostgreSQL, repli répété et journal ; aucun repli vers un binaire PC SOFT | Exploitation |
| Régression sécurité de compatibilité | Moyenne / critique | Ancienne permission devient accès global | Profil sécurité séparé, pas d'affaiblissement implicite, tests négatifs | Sécurité |
| Extension ou package compromis | Moyenne / élevée | Artefact non signé ou origine inconnue | Versions verrouillées, SBOM, vérification d'origine et politique d'extensions | DevSecOps |
| Performance non acceptable | Moyenne / élevée | p95 dégradé sur gros jeux | Mesures précoces, profiler, backend adapté; annoncer les limites | Runtime |
| Stores et permissions mobiles changent | Élevée / élevée | Rejet de publication ou permission retirée | Veille éditeurs, tests appareil, releases de maintenance | Mobile |
| Développeurs désorientés | Moyenne / élevée | Temps de tâche ou erreurs augmentent | Tests avec développeurs WINDEV, terminologie et raccourcis configurables | UX |
| Compétence clé concentrée | Moyenne / élevée | Un seul mainteneur pour un sous-système | Binômage, spécifications exécutables, revue croisée et formation | Direction technique |
| Catalogue périmé | Élevée / élevée | Nouvelle API non classée | Inventaire daté, delta par version, statut inconnu visible | Compatibilité |
| Preuve confondue avec parité générale | Élevée / élevée | Accord interprète/compilé ou quelques fixtures présenté comme compatibilité totale | Publier origine/portée des attendus, inconnues et défauts partagés possibles ; aucun oracle PC SOFT ni parité totale revendiquée | QA / compatibilité |

Un registre vivant ajoute pour chaque risque une date de revue, un propriétaire nommé, une action, une échéance et une preuve de réduction. Une probabilité basse ne dispense pas de traiter une perte de données potentielle.

## 8. Documentation, support et maintenance

Livrer un guide « je viens de WINDEV », un dictionnaire concepts/raccourcis, les limites par version/cible, un tutoriel d'import réel, un guide débogage et un diagnostic consultable depuis l'IDE. Chaque message d'incompatibilité indique l'élément source, la signature concernée, la cible, le comportement manquant, la voie de contournement et le test de certification attendu.

Publier notes de version, schéma du projet ouvert, politique de compatibilité, durée de support, procédure de rapport de bug et procédure de minimisation des reproductions. Les projets clients envoyés au support nécessitent consentement et filtrage des secrets; proposer un diagnostic local et des reproductions synthétiques.

La déclaration d'une version stable doit nommer les profils certifiés, les cibles, l'ensemble de tests et les exclusions. Conserver une branche corrective pour les pilotes en production. Une nouvelle optimisation du compilateur doit rejouer les tests historiques qu'elle peut affecter. Une nouvelle version majeure PC SOFT n'est compatible qu'après son propre inventaire et ses preuves.

## Sources et nature des informations

- [Architecture proposée](05-architecture-cible.md) et [compatibilité langage](02-langage-et-import.md) : recommandations internes de cette étude.
- [NIST, Secure Software Development Framework SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) : référence primaire de processus de développement sécurisé.
- [Directive 2009/24/CE](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32009L0024) : cadre du travail d'interopérabilité; détaillé au chapitre 09.
- [PC SOFT, contrat WINDEV, articles 4 et 5](https://doc.pcsoft.fr/fr-FR/?4510001=&name=License_WINDEV) et [licence du framework, article 3](https://doc.windev.com/fr-FR/?1000019581=&name=licence_framework_windev) : clauses dont la portée doit être analysée sur le projet réel ; aucun avis obtenu ici.

Les charges, calendriers, scénarios, répartitions et seuils sont des propositions originales de planification. Ils devront être remplacés par des mesures du corpus et les engagements des pilotes.
