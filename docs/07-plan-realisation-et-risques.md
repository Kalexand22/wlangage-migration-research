# Plan de réalisation, validation et maîtrise des risques

Date de l'étude : **26 octobre 2026**. Ce chapitre est une **proposition de conduite du programme**, pas le compte rendu d'une implémentation existante. Aucun projet client, installation WINDEV, périphérique ou serveur HFSQL n'a été testé pour cette étude. Les seuils ci-dessous sont des critères de départ à contractualiser avec les pilotes.

Les seuils illustratifs sont rapprochés par stade dans le [registre de décision](../data/seuils-decision.csv). Ils restent non validés jusqu’à leur choix avant un essai sur un profil précis ; voir les [améliorations immédiates](12-ameliorations-immediates.md).

## 1. Résultat à financer et première décision

Le premier produit doit être un environnement capable d'importer un périmètre documenté, d'exécuter le WLangage d'origine et de signaler chaque incompatibilité. La première décision d'investissement porte sur cette capacité mesurée, pas sur une promesse de remplacement universel de WINDEV, WEBDEV et WINDEV Mobile.

La trajectoire proposée suit l'architecture du chapitre [05](05-architecture-cible.md) : représentation intermédiaire WLangage, moteur de compatibilité et premier backend .NET, applications Windows avec WinForms, puis moteurs d'interface web et mobile distincts. Avalonia pour l'IDE reste conditionné par un prototype du concepteur, du débogage et des intégrations Windows. Une technologie choisie pour l'IDE n'impose pas celle des applications générées.

Conserver HFSQL dans les premiers pilotes et changer le langage d'exécution d'abord réduit le nombre de variables. Une migration PostgreSQL constitue un chantier séparé, avec sa propre preuve d'équivalence. Le maintien d'un composant PC SOFT dépend des droits applicables décrits au chapitre [09](09-propriete-intellectuelle-et-licences.md).

## 2. Corpus pilote à constituer

Sélectionner cinq applications réelles détenues ou confiées légalement, et compléter par des microprogrammes originaux. Les nombres suivants décrivent **les jeux à rechercher**, sans prétendre qu'ils sont déjà disponibles.

| Pilote | Profil recherché | Difficultés qu'il doit révéler | Mesures de sortie |
| --- | --- | --- | --- |
| A — gestion Windows | 30–100 fenêtres, 20–80 tables, code procédural FR, HFSQL Classic | Tables fichier, FAA, fenêtres modales, états, installation réseau | Parcours commande-facture-stock, mêmes montants et événements |
| B — application ancienne | Version ancienne convertie légalement en texte, ANSI, composants internes | Options de compilation historiques, fichiers externes, copies de tableaux, valeurs implicites | Conservation exacte des sources, conversions et comportements datés |
| C — application concurrente | HFSQL C/S, droits, transactions et traitements longs | Verrous, reprise après incident, timeouts, procédures stockées | Invariants transactionnels et droits inchangés sous charge |
| D — WEBDEV | Pages navigateur/serveur, AJAX, sessions, REST, authentification | Frontière client/serveur, réentrance, expiration, erreurs réseau | Parcours E2E, isolation des sessions, absence de fuite de secrets |
| E — WINDEV Mobile | Android puis iOS, collecte hors ligne, code-barres, photos | Permissions, tâches de fond, synchronisation et conflits | Reprise après déconnexion, périphériques réels et publication test |

Un pilote simple qui évite toutes les difficultés ne prouve pas la migration du parc. Stratifier les projets selon version, édition, options de compilation, cible, base, volume, langue, interop native et fonctions dynamiques. Faire apparaître les zones non représentées. Obtenir pour chaque application un propriétaire métier, un référent WINDEV et un référent données.

Livrables d'entrée : copie immuable et empreintes des sources, inventaire des binaires dépendants, analyse, ressources, états, requêtes, dictionnaires, traductions, styles, composants, paramètres projet, installateurs et droits d'utilisation. Les bases sont synthétiques ou anonymisées; leur méthode de génération doit reproduire les cas de bord. Un environnement d'observation licencié reste distinct du code du nouveau produit.

## 3. Jalons et portes de sortie

Le calendrier ci-dessous est **une hypothèse budgétaire séquentielle de 36 mois**. Il suppose une équipe expérimentée, un corpus disponible dès M0 et l'absence de blocage juridique sur le chemin choisi. Les étapes sont séquentielles pour rendre les efforts lisibles; une parallélisation change les effectifs de pointe et ne supprime pas le travail.

| Phase | Fenêtre indicative | Équipe moyenne | Effort indicatif | Livrables et condition de passage |
| --- | --- | --- | --- | --- |
| P0 — qualification | M0–M2 | 5–7 ETP | 10–14 personnes-mois | Corpus, contrats, inventaire, export réel; 100 % des fichiers classés ou explicitement inconnus; aucune perte silencieuse |
| P1 — preuve sémantique | M2–M5 | 7–10 ETP | 21–30 personnes-mois | Parseur sans perte, profils, premiers types et fonctions, exécution différentielle; tous les cas retenus passent ou bloquent explicitement |
| P2 — tranche Windows | M5–M11 | 10–14 ETP | 60–84 personnes-mois | Import fenêtre/données/état, IDE familiarisé, débogage WLangage, build CI; parcours complet A sur données de test |
| P3 — Windows pilote | M11–M18 | 12–18 ETP | 84–126 personnes-mois | Extension API/champs, C/S, concurrence, packaging et rollback; trois pilotes Windows acceptés, zéro défaut critique ouvert |
| P4 — service et web | M18–M26 | 16–22 ETP | 128–176 personnes-mois | Services, séparation navigateur/serveur et première famille de pages; pilote D avec session/sécurité/performance validées |
| P5 — mobile et extension | M26–M36 | 20–30 ETP | 200–300 personnes-mois | Android/iOS sur périmètre annoncé, hors ligne, interop; pilote E et certification des profils publiés |
| P6 — couverture durable | Après M36 | À dimensionner sur le parc | Non chiffrable sans inventaire | Longue traîne API, états complexes, matériels, autres OS et nouvelles versions PC SOFT |

Total de l'hypothèse P0–P5 : **503–730 personnes-mois**. Ce total finance les périmètres des pilotes et l'industrialisation progressive; il ne constitue pas un devis pour l'intégralité de l'écosystème. Une équipe réduite peut produire un démonstrateur, mais elle doit réduire la couverture ou allonger le calendrier. Réestimer après P0 et P2 avec débit observé de fonctionnalités certifiées, taux de divergences et coût de maintenance.

Chaque passage de phase exige une démonstration reproductible à partir d'un checkout propre, un rapport des écarts encore présents et une décision du responsable produit. Un défaut bloquant provoque une réduction du périmètre annoncé ou une prolongation explicite. Il ne disparaît pas par reclassement en avertissement.

### Premier lot de 90 jours

1. J1–J15 : obtenir les sources, leurs paramètres, les droits et les scénarios; exporter un projet représentatif par la voie documentée.
2. J16–J30 : scanner les éléments, produire le manifeste et la carte des dépendances; conserver tous les fragments inconnus; choisir 50 microcas sémantiques à fort risque.
3. J31–J60 : lexer/parseur, arbre conservant le texte, profils de compilation, types numériques/chaînes, diagnostics; première exécution comparative automatisée.
4. J61–J75 : importer une fenêtre, une table, un événement et une requête, puis générer un état minimal; tester les événements et l'arrondi.
5. J76–J90 : démonstration reproductible et mesure du coût d'ajout d'une API/champ; décision poursuivre, concentrer la cible ou abandonner un chemin technique.

Ce lot ne se confond pas avec P1 terminé : il doit produire la preuve la plus informative avant le financement des modules suivants.

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

Avec une **hypothèse illustrative** de 9 000 à 16 000 € par personne-mois complet, 503–730 personnes-mois représentent 4,53 à 11,68 M€ de travail, avant postes additionnels et provision. Ces valeurs ne sont ni des tarifs PC SOFT ni des prix de marché vérifiés ni une offre commerciale. Remplacer chaque hypothèse par les coûts réels de l'organisation. Une provision de 20–35 % est un point de départ de planification, pas une preuve statistique. Ne pas additionner une seconde fois les mêmes QA, charges employeur ou équipements déjà intégrés au coût complet.

Le coût récurrent inclut maintien des profils historiques, certification des nouvelles versions d'OS, mises à jour de dépendances, support, sécurité, tests de périphériques et enrichissement du catalogue. La couverture complète n'est pas un état acquis définitivement.

## 5. Système de preuves de compatibilité

### 5.1 Quatre dénominateurs à publier

Un score unique masque les lacunes. Publier séparément :

| Mesure | Dénominateur | Preuve nécessaire |
| --- | --- | --- |
| Import sans perte | Éléments effectivement présents dans le corpus | Inventaire avant/après, empreintes, comptage code et ressources, inconnus conservés |
| Source inchangée | Unités WLangage originales sélectionnées | Empreintes des octets ou diff explicite; conversions d'encodage rapportées séparément |
| Compatibilité API utilisée | Signatures, propriétés, événements et modes rencontrés | Tests par profil/version/cible et cas d'erreur; appel dynamique signalé |
| Compatibilité fonctionnelle | Scénarios et invariants métier acceptés | Recette différentielle données/UI/PDF et traces signées |

Le catalogue global du produit donne un cinquième indicateur : entrées certifiées / entrées inventoriées **dans une édition et un périmètre datés**. Un très bon score sur trois pilotes ne devient pas une couverture mondiale de WLangage.

### 5.2 Oracle différentiel

Exécuter le même microprogramme original dans l'environnement PC SOFT autorisé et dans le moteur cible. Comparer valeurs typées, précision, erreurs, état global et effets observables. Enregistrer version exacte, options projet, architecture, langue système, fuseau, police, moteur données et graine de test. Les programmes ne doivent pas envoyer deux fois des emails, paiements ou commandes matériels : rediriger les effets vers des doubles contrôlés ou utiliser une capture/relecture.

Cas prioritaires : valeurs limites et nulles, décimaux, débordements, chaînes ANSI/Unicode, caractères combinés, indices, dates invalides, portée, référence/copie, ET/OU, procédures, exceptions, propriétés, ordre des événements, réentrance, curseurs, doublons et verrous. Un test d'erreur est aussi important qu'un résultat nominal. Employer tests génératifs et réduction automatique des cas défaillants; un millier de variantes d'une addition ne remplace pas un test du changement de portée.

### 5.3 Recette des interfaces et documents

Capturer navigation clavier, focus, tabulation, validation, clic/double-clic, raccourcis, glisser-déposer, menus contextuels, FAA, états de tri/filtre et persistance des préférences. Vérifier la même suite d'événements métier, pas seulement une capture visuelle similaire. Tester DPI 100/150/200 %, écrans multiples et lecteur d'écran sur le périmètre annoncé.

Pour les états : comparer le contenu extrait, montants et pagination; comparer ensuite géométrie, polices, sauts et superpositions. Une tolérance initiale de 0,2 mm sur les éléments imprimés peut être choisie puis ajustée au cas métier; les chiffres, identifiants, signatures et codes-barres n'admettent pas une altération cachée dans une tolérance visuelle. Tester de vraies imprimantes, étiquettes et lecteurs lorsque le pilote en dépend. Le hash d'un PDF ne suffit pas, car les métadonnées ou identifiants internes peuvent varier.

### 5.4 Données, concurrence et résilience

Comparer comptages par table, clés et relations, totaux monétaires exacts, valeurs nulles/vides, types, blobs, dates et encodages. Produire des empreintes de lignes après une canonicalisation documentée, avec traitement explicite des champs non déterministes. Contrôler également ordre des parcours et équivalences de recherche selon les collations.

Injecter crash avant/après commit, coupure réseau, expiration de session, disque plein, restauration, conflit offline et reprise de tâche. Vérifier qu'une opération acquittée n'est pas perdue, qu'une opération rejouée n'est pas facturée deux fois et que les verrous sont libérés. Définir RPO/RTO par pilote, puis les mesurer lors d'un exercice; une sauvegarde jamais restaurée n'est pas une preuve de reprise.

### 5.5 Performance et sécurité

Établir une référence sur le même matériel et jeu de données. Comparer démarrage, compilation froide/chaude, import, consommation mémoire, tables volumineuses, impression et latences p50/p95/p99. Un seuil de départ tel que p95 inférieur à 1,2 fois la référence peut être un objectif pilote; il doit être négocié par scénario. Les fonctions plus lentes mais acceptables restent documentées.

Tester séparation des privilèges, contrôle d'accès serveur, injection, sérialisation, secrets, dépendances, accès disque/réseau des extensions et confinement des compilations dynamiques. Structurer les pratiques de développement sécurisé à partir du [NIST SSDF, SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final), sans confondre conformité à un processus et absence de vulnérabilité.

## 6. Déploiement progressif et retour arrière

Pour chaque pilote : sauvegarde restaurable, version applicative et runtime verrouillées, empreintes des artefacts, plan de changement du schéma, utilisateurs pilotes, surveillance et procédures d'escalade. Livrer d'abord en environnement de recette, puis à un groupe limité avec un responsable métier joignable.

Le retour arrière du **binaire** est simple seulement si les données restent lisibles par l'ancienne version. Préférer des changements de schéma additifs, puis retirer les anciennes structures dans une livraison ultérieure. Tout changement destructif exige export de reprise et réconciliation éprouvés.

Pendant la comparaison, une seule pile écrit les données métier faisant autorité. La seconde lit un snapshot ou reçoit un flux de comparaison sans effets externes. Une double écriture improvisée créerait des divergences difficiles à réparer. Si une réplication est nécessaire, définir ordre, idempotence, point de reprise et propriétaire de chaque entité.

Déclencheurs de repli proposés : perte/intégrité de données, erreur de montant, accès indu, incident critique, hausse de latence dépassant le seuil convenu ou taux d'échec d'un parcours essentiel. Le repli comprend arrêt des écritures, sauvegarde de l'état atteint, réconciliation et contrôle métier avant réouverture. Ne pas restaurer aveuglément une ancienne base en effaçant les opérations valides déjà réalisées.

## 7. Registre de risques initial

Probabilités et impacts sont des **appréciations initiales qualitatives**, à recalibrer après les pilotes. « Élevé » n'est pas un pourcentage observé.

| Risque | Probabilité / impact | Signal précoce | Réduction et réponse | Responsable |
| --- | --- | --- | --- | --- |
| Formats natifs insuffisamment lisibles | Élevée / critique | Métadonnées absentes après export | Priorité texte officiel, conserver les inconnus, échantillonner les versions; ne pas inventer les données | Import |
| Options de compilation historiques perdues | Élevée / critique | Même source, résultat divergent | Profils explicites, tests ET/OU/portée/copie; bloquer profil inconnu | Langage |
| Sémantique dynamique non détectée | Élevée / élevée | Appels résolus uniquement en production | Traces autorisées, analyse conservatrice, runtime contrôlé, diagnostic actionnable | Runtime |
| ODBC confondu avec les fonctions H* | Élevée / critique | Différences de recherche ou verrouillage | Adaptateur sémantique certifié, pont légal ciblé, migration données séparée | Données |
| Ordre des événements différent | Élevée / critique | Double validation, fenêtres bloquées | Traces événements, tests réentrance et modalité | UI |
| Pagination ou précision financière altérée | Élevée / critique | État visuellement proche mais totaux faux | Comparaison structurée + géométrie + recette imprimée | Reporting |
| Composant externe sans source | Élevée / élevée | Uniquement DLL ou composant compilé | Réutilisation autorisée via contrat documenté ou remplacement annoncé; pas de promesse de recompilation | Interop |
| Dépendance COM/ActiveX Windows | Élevée / élevée | Blocage web/mobile/Linux | Isoler adaptateur Windows, diagnostic cible, alternative explicite | Plateforme |
| Droits d'exploitation insuffisants | Moyenne / critique | EULA/contrat manquant ou restriction pertinente | Dossier de provenance, revue ciblée, architecture sans redistribution litigieuse | Juridique |
| Budget de longue traîne sous-estimé | Élevée / critique | Coût par API/champ croissant | Mesurer débit, trier par usage, budget maintenance, réviser périmètre annoncé | Produit |
| Corps de tests trop simple | Élevée / élevée | Pilote passe, nouveau client échoue | Stratification du corpus, programme de pilotes, critères par profil | QA |
| Sources modifiées silencieusement | Moyenne / critique | Diff sans explication | Copie immuable, import sans perte, patchs séparés et revue | Import |
| Dual write incohérent | Moyenne / critique | Soldes et événements divergents | Autorité d'écriture unique, idempotence, réconciliation | Données |
| Perte au retour arrière | Moyenne / critique | Schéma incompatible ancien binaire | Migrations additives, répétition de repli, journal opérations | Exploitation |
| Régression sécurité de compatibilité | Moyenne / critique | Ancienne permission devient accès global | Profil sécurité séparé, pas d'affaiblissement implicite, tests négatifs | Sécurité |
| Extension ou package compromis | Moyenne / élevée | Artefact non signé ou origine inconnue | Versions verrouillées, SBOM, vérification d'origine et politique d'extensions | DevSecOps |
| Performance non acceptable | Moyenne / élevée | p95 dégradé sur gros jeux | Mesures précoces, profiler, backend adapté; annoncer les limites | Runtime |
| Stores et permissions mobiles changent | Élevée / élevée | Rejet de publication ou permission retirée | Veille éditeurs, tests appareil, releases de maintenance | Mobile |
| Développeurs désorientés | Moyenne / élevée | Temps de tâche ou erreurs augmentent | Tests avec développeurs WINDEV, terminologie et raccourcis configurables | UX |
| Compétence clé concentrée | Moyenne / élevée | Un seul mainteneur pour un sous-système | Binômage, spécifications exécutables, revue croisée et formation | Direction technique |
| Catalogue périmé | Élevée / élevée | Nouvelle API non classée | Inventaire daté, delta par version, statut inconnu visible | Compatibilité |
| Test oracle non reproductible | Moyenne / élevée | Version historique ou licence inaccessible | Images et installations conservées légalement, manifeste complet, export des résultats | QA / juridique |

Un registre vivant ajoute pour chaque risque une date de revue, un propriétaire nommé, une action, une échéance et une preuve de réduction. Une probabilité basse ne dispense pas de traiter une perte de données potentielle.

## 8. Documentation, support et maintenance

Livrer un guide « je viens de WINDEV », un dictionnaire concepts/raccourcis, les limites par version/cible, un tutoriel d'import réel, un guide débogage et un diagnostic consultable depuis l'IDE. Chaque message d'incompatibilité indique l'élément source, la signature concernée, la cible, le comportement manquant, la voie de contournement et le test de certification attendu.

Publier notes de version, schéma du projet ouvert, politique de compatibilité, durée de support, procédure de rapport de bug et procédure de minimisation des reproductions. Les projets clients envoyés au support nécessitent consentement et filtrage des secrets; proposer un diagnostic local et des reproductions synthétiques.

La déclaration d'une version stable doit nommer les profils certifiés, les cibles, l'ensemble de tests et les exclusions. Conserver une branche corrective pour les pilotes en production. Une nouvelle optimisation du compilateur doit rejouer les tests historiques qu'elle peut affecter. Une nouvelle version majeure PC SOFT n'est compatible qu'après son propre inventaire et ses preuves.

## Sources et nature des informations

- [Architecture proposée](05-architecture-cible.md) et [compatibilité langage](02-langage-et-import.md) : recommandations internes de cette étude.
- [NIST, Secure Software Development Framework SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) : référence primaire de processus de développement sécurisé.
- [Directive 2009/24/CE](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32009L0024) : cadre du travail d'interopérabilité; détaillé au chapitre 09.

Les charges, calendriers, scénarios, répartitions et seuils sont des propositions originales de planification. Ils devront être remplacés par des mesures du corpus et les engagements des pilotes.
