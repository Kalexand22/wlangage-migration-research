# Cahier des charges des prototypes de décision

Date : **26 octobre 2026**. Ces six prototypes sont **à réaliser**. Aucun résultat, fichier de test, mesure ou compatibilité ci-dessous n'est présenté comme déjà obtenu. Ils servent à décider si l'[architecture proposée](05-architecture-cible.md) mérite un investissement plus large.

Les seuils illustratifs sont rapprochés par stade dans le [registre de décision](../data/seuils-decision.csv). Ils restent non validés jusqu’à leur choix avant un essai sur un profil précis ; voir les [améliorations immédiates](12-ameliorations-immediates.md).

## Cadre commun

Les durées sont des **hypothèses de charge en jours-personnes**, pour des ingénieurs expérimentés disposant des outils et des entrées, hors obtention des droits et remise en état du patrimoine. Elles ne constituent ni devis ni calendrier. On fige pour chaque essai : version/build PC SOFT, configuration, options, encodage, cible, architecture, système, polices et données. Les nombres de cas sont des minima de caractérisation du prototype, jamais des preuves d'exhaustivité.

**Exclusion ferme : aucun outil, DLL, framework, SDK, pilote, serveur HFSQL ou pont PC SOFT à aucune étape, y compris import, build, CI, tests et comparaison.** Aucun WINDEV ou exécutable d'origine n'est lancé comme oracle, même chez un client pour notre workflow. Les six prototypes utilisent du code original et des outils tiers non PC SOFT. Fichiers/exports, fixtures, traces et PDF déjà disponibles peuvent être fournis comme données passives avec provenance ; aucun outil PC SOFT n'est sollicité pour les créer ou les compléter.

Prévoir des dossiers déjà disponibles de trois projets : gestion avec états, interop tierce non PC SOFT, concurrence ou logique complexe. Les attendus proviennent de règles publiques sourcées ou de preuves passives reçues. Un attendu absent reste inconnu et bloque la revendication concernée, sans bloquer les expériences autonomes. Les jeux sont fictifs ou anonymisés. Chaque dossier restitue entrées/empreintes, provenance, scripts, résultats et limites. L'accord de nos deux moteurs peut partager un défaut : il ne prouve pas une parité totale avec PC SOFT.

**Gate commun à tous les prototypes, à implémenter :** SBOM et fermeture transitive des dépendances, liste positive d'outils avec empreintes, processus enfants, modules/assemblages chargés, services/connexions et paquet inspectés sur machine propre sans PC SOFT. Toute dépendance PC SOFT locale, distante ou déléguée fait échouer le gate. Un composant non identifié n'est pas admis implicitement. Aucun avis juridique préalable n'est posé comme condition au code original autonome.

Les seuils ci-dessous sont des **propositions à arrêter avant l'exécution**, puis à conserver dans le dossier. Une divergence critique de montant, transaction, ordre métier, document ou sécurité interdit le passage au pilote concerné, même si le taux moyen est élevé.

| Prototype | Question décisive | Charge indicative |
| --- | --- | --- |
| P1 | La chaîne conserve-t-elle la sémantique sur un sous-ensemble précis ? | 20–35 jours-personnes |
| P2 | Peut-on récupérer les éléments sans reconstruction généralisée ? | 10–20 jours-personnes |
| P3 | Le modèle d'événements permet-il un vrai parcours Windows ? | 12–20 jours-personnes |
| P4 | L'adaptateur original sur PostgreSQL satisfait-il les contrats H* définis ? | 15–25 jours-personnes |
| P5 | Les états restent-ils utilisables et exacts ? | 12–20 jours-personnes |
| P6 | Le développeur débogue-t-il effectivement son WLangage ? | 8–15 jours-personnes |

P1 et P2 peuvent commencer en parallèle. P3–P5 consomment leurs contrats stabilisés. P6 s'appuie sur le backend de P1 et un écran de P3. Ces charges incluent des composants réutilisés entre prototypes et ne doivent pas être additionnées sans dédoublonnage.

## P1 — Compilateur et runtime sémantique

**Entrées.** Profil déclaré, exemples originaux, documentation publique et fixtures/traces déjà fournies. Viser 200 cas : nombres, conversions, chaînes, dates, références, tableaux, ordre d'évaluation et erreurs. Chaque attendu porte sa source et son statut : règle documentée, observation passive reçue, ou hypothèse non vérifiée. Grammaire limitée et périmètre annoncés avant mesure.

**Travail.** Réaliser lexer/parseur, AST, IR avec positions et effets, et primitives de runtime. Commencer par un interprète minimal afin d'obtenir des observations explicables ; produire ensuite un backend C# interne/.NET pour **le même sous-ensemble**. Les deux moteurs partagent les opérations sémantiques. L'ordre des conditions et les mutations d'arguments sont journalisés, pas seulement la valeur finale.

**Artefacts.** Grammaire, types/conversions, cas autoportants, attendus sourcés, résultats des deux moteurs originaux, traces de leur exécution, constructions refusées, inconnues et benchmark.

**Mesures et décision.** Tous les cas indispensables au sous-ensemble revendiqué doivent satisfaire leur attendu documenté, erreurs et effets compris. Publier hypothèses/inconnues séparément ; l'accord compilé/interprété mesure aussi la cohérence interne. Syntaxe hors périmètre refusée avec position utile. Mesurer temps/mémoire sur cinq charges et fixer un budget absolu ; le ratio illustratif 5× n'est utilisable que si une référence passive comparable existe déjà. Aucun PC SOFT n'est lancé pour la mesurer.

**Si échec.** Corriger le modèle de valeurs ou l'IR avant d'ajouter des API. Si .NET empêche un contrat indispensable, essayer un backend alternatif sur ces mêmes cas. Si la sémantique ne peut être caractérisée, réduire publiquement le profil ou abandonner la promesse de compatibilité correspondante.

## P2 — Import des fichiers/exports fournis et blocages binaires

**Entrées.** Copies immuables déjà disponibles, export texte fourni s'il existe, métadonnées et inventaires passifs avec provenance. Inclure fenêtre, état, analyse, requête, classe et ressources. Un natif ancien peut être fourni comme fichier ; aucune installation de sa version d'origine n'est requise ni utilisée.

**Travail.** Détecter format/encodage, lire via importeurs originaux, extraire traitements/propriétés/références et préserver les segments opaques. Un lecteur binaire indépendant n'est admis que si son fonctionnement est spécifié et testé sans composant PC SOFT. Sinon la portion reste opaque et sa fonctionnalité bloquée. Aucun IDE, exporteur ou convertisseur PC SOFT, même délégué au détenteur.

**Artefacts.** Inventaire des fichiers reçus et de leur extraction, empreintes, manifeste, correspondances objet/traitement, portions inconnues et diff d'une modification locale.

**Mesures et décision.** Retrouver tous les blocs/ressources de l'inventaire passif connu, avec identité d'octets ou transcodage déclaré. Sans décompte source fiable, la complétude reste indéterminée. Les propriétés indispensables absentes bloquent l'élément ; aucun inconnu supprimé. **Go binaire** seulement avec lecture indépendante éprouvée et métadonnées suffisantes. Le seul code texte ne démontre pas la reprise des écrans/états.

**Si échec.** Rechercher uniquement d'autres fichiers déjà disponibles, réduire la couverture ou déclarer l'élément non importable. Spécification/reconstruction originale explicite possible ; aucun nouvel export par PC SOFT ni pont en recours. Si la reconstruction devient systématique, reconsidérer la promesse de reprise maximale.

## P3 — Boucle d'événements, fenêtres et modalité

**Entrées.** Description d'écran déjà fournie, ou écran synthétique : table liée, modalité, validation, raccourcis, minuterie et callback. Définir douze parcours et quatre scénarios de concurrence à partir des contrats publics et traces déjà disponibles, sans capture nouvelle de l'original PC SOFT.

**Travail.** Exécuter le code importé via P1 dans un renderer Windows minimal. Construire répartiteur et contexte, puis tester focus, annulation, réentrance, modification programmée, fermeture pendant traitement et résultat modal. La prévisualisation du concepteur utilise ce même renderer dans un processus isolé.

**Artefacts.** Modèle UI, carte des événements, traces comparées, captures à DPI fixés, scénario clavier et liste de propriétés encore indisponibles.

**Mesures et décision.** Événements et effets conformes aux attendus documentés ; concurrence conforme aux relations d'ordre spécifiées, sans imposer d'horodatage identique. Zéro validation omise, double écriture ou mauvaise instance. Comparer les captures de notre renderer aux images passives disponibles, si leur contexte est connu. Un comportement sans référence reste non vérifié ; mesurer p95 et mémoire sur notre chaîne autonome.

**Si échec.** Modifier ordonnanceur et contexte ; comparer WinForms et Avalonia sur le composant bloquant. Conserver Windows comme profil séparé. Une modalité desktop incompatible avec le navigateur ne doit pas conduire à modifier silencieusement le code du pilote.

## P4 — Contrats H* originaux sur PostgreSQL

**Entrées.** Schéma et export logique déjà fournis, ou base synthétique PostgreSQL : clés composées, doublons, NULL, mémos/binaires et deux clients. Signatures H* tirées des sources reçues et documentation publique ; traces de données préexistantes si disponibles. Aucun fichier natif n'est lu par driver HFSQL.

**Travail.** Implémenter la couche sémantique originale sur PostgreSQL avec pilote non PC SOFT. Réaliser trente scénarios : recherche, parcours/fin, filtre, tampon courant, modification, erreur, transaction/rollback, verrou et interruption. Comparer aux contrats publics et attendus passifs reçus. Aucun serveur HFSQL, pilote, SDK ou pont.

**Artefacts.** Contrat du fournisseur, traces de curseur et d'erreur, dump logique canonique, contrôles de volumes/empreintes, script de concurrence et procédure de restauration.

**Mesures et décision.** État final, retour, curseur, transaction et invariant conformes aux contrats explicitement retenus. Lacunes et contradictions de références restent visibles et bloquent la revendication concernée. Mesurer p50/p95, débit et reprise après arrêt de notre chaîne. La réussite de SQL ne prouve pas H* ; aucun résultat ne prétend à une parité totale avec HFSQL non exécuté.

**Si échec.** Corriger l'émulation originale, réduire le contrat ou annoncer un changement fonctionnel nécessitant adaptation. Si un cas indispensable reste insoluble, bloquer le module. HFSQL, pont et maintien du runtime d'origine ne sont jamais des solutions admises.

## P5 — États, pagination et PDF

**Entrées.** Sources déjà fournies de trois états, ou modèles originaux : facture, ruptures/sous-totaux, images/codes-barres/événements. Polices tierces non PC SOFT sous droits adéquats, papier/marges et PDF de référence déjà disponible avec provenance. Cinq jeux par état : vide, une ligne et limites de pagination incluses.

**Travail.** Importer bandes, liaisons et traitements ; construire un layout documentaire avec pagination et génération PDF. Tester aperçu et une impression réelle, sans remplacer les traitements d'état par une réécriture métier.

**Artefacts.** Modèle d'état, PDF générés, extraction de texte/valeurs, rapport de pagination, comparaison des zones et protocole d'impression.

**Mesures et décision.** Zéro montant, libellé obligatoire, ligne ou code-barres absent ; totaux et ordre identiques. Même nombre de pages sur les cas de fidélité retenus. Fixer une tolérance proposée de 0,5 mm pour les zones critiques, à confirmer selon l'usage, avec contrôle visuel des écarts restants. Vérifier lecture des codes-barres et absence de texte tronqué. Un simple pourcentage de pixels semblables n'est pas un critère suffisant.

**Si échec.** Corriger notre layout, essayer un moteur documentaire tiers non PC SOFT ou restreindre les types d'états. Sans état exigé fonctionnel, le pilote reste bloqué. Aucun maintien de l'impression PC SOFT ni génération de PDF d'origine à la demande.

## P6 — Débogage dans le code d'origine

**Entrées.** Backend compilé P1, écran P3, procédure interne, appel imbriqué, variable par référence et erreur déclenchable. Définir quinze manipulations attendues par un développeur WINDEV.

**Travail.** Relier positions conteneur/traitement/IR/backend ; implémenter DAP minimal, documents virtuels WLangage, variables et évaluation contrôlée. Tester points d'arrêt, pas à pas, pile, exception, modification de valeur et changement d'un fichier après compilation.

**Artefacts.** Tables de correspondance, adaptateur, enregistrement des parcours, tests de positions et rapport des capacités annoncées.

**Mesures et décision.** Les quinze manipulations s'effectuent sans ouvrir le C# généré ; chaque arrêt pointe vers le bon traitement et chaque valeur respecte le type WLangage. Un point non réalisable est indiqué non vérifié, jamais affiché comme actif à tort. Une version source discordante est détectée. Toute erreur de pile ou d'alias critique interdit la certification du débogueur.

**Si échec.** Renforcer le mapping ou fournir temporairement un mode interprété explicitement limité. Si le pilote n'est débogable qu'en langage hôte, la promesse d'expérience familière n'est pas validée.
