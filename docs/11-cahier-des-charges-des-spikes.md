# Cahier des charges des prototypes de décision

Date : **26 octobre 2026**. Ces six prototypes sont **à réaliser**. Aucun résultat, fichier de test, mesure ou compatibilité ci-dessous n'est présenté comme déjà obtenu. Ils servent à décider si l'[architecture proposée](05-architecture-cible.md) mérite un investissement plus large.

Les seuils illustratifs sont rapprochés par stade dans le [registre de décision](../data/seuils-decision.csv). Ils restent non validés jusqu’à leur choix avant un essai sur un profil précis ; voir les [améliorations immédiates](12-ameliorations-immediates.md).

## Cadre commun

Les durées sont des **hypothèses de charge en jours-personnes**, pour des ingénieurs expérimentés disposant des outils et des entrées, hors obtention des droits et remise en état du patrimoine. Elles ne constituent ni devis ni calendrier. On fige pour chaque essai : version/build PC SOFT, configuration, options, encodage, cible, architecture, système, polices et données. Les nombres de cas sont des minima de caractérisation du prototype, jamais des preuves d'exhaustivité.

Prévoir trois projets autorisés : gestion avec états, interop/matériel, concurrence ou logique complexe. Une installation PC SOFT autorisée et capable de reconstruire ces projets fournit l'oracle ; son absence rend l'essai **non concluant**. Les jeux contiennent des données fictives ou anonymisées. Chaque dossier restitue entrées et empreintes, scripts, versions, résultats bruts, comparaison, limites, décision et procédure de répétition. Le code métier n'est pas réécrit pour obtenir un résultat favorable. Un échec reste dans le dénominateur.

Les seuils ci-dessous sont des **propositions à arrêter avant l'exécution**, puis à conserver dans le dossier. Une divergence critique de montant, transaction, ordre métier, document ou sécurité interdit le passage au pilote concerné, même si le taux moyen est élevé.

| Prototype | Question décisive | Charge indicative |
| --- | --- | --- |
| P1 | La chaîne conserve-t-elle la sémantique sur un sous-ensemble précis ? | 20–35 jours-personnes |
| P2 | Peut-on récupérer les éléments sans reconstruction généralisée ? | 10–20 jours-personnes |
| P3 | Le modèle d'événements permet-il un vrai parcours Windows ? | 12–20 jours-personnes |
| P4 | L'adaptateur préserve-t-il les contrats H* utilisés ? | 15–25 jours-personnes |
| P5 | Les états restent-ils utilisables et exacts ? | 12–20 jours-personnes |
| P6 | Le développeur débogue-t-il effectivement son WLangage ? | 8–15 jours-personnes |

P1 et P2 peuvent commencer en parallèle. P3–P5 consomment leurs contrats stabilisés. P6 s'appuie sur le backend de P1 et un écran de P3. Ces charges incluent des composants réutilisés entre prototypes et ne doivent pas être additionnées sans dédoublonnage.

## P1 — Compilateur et runtime sémantique

**Entrées.** Profil figé, exemples originaux autorisés, documentation des constructions choisies et au moins 200 cas : nombres/arrondis, conversions, chaînes, dates vides/limites, paramètres par référence, tableaux, ordre d'évaluation et erreurs. Définir une grammaire volontairement limitée mais complète pour ces cas.

**Travail.** Réaliser lexer/parseur, AST, IR avec positions et effets, et primitives de runtime. Commencer par un interprète minimal afin d'obtenir des observations explicables ; produire ensuite un backend C# interne/.NET pour **le même sous-ensemble**. Les deux moteurs partagent les opérations sémantiques. L'ordre des conditions et les mutations d'arguments sont journalisés, pas seulement la valeur finale.

**Artefacts.** Grammaire, table des types/conversions, cas autoportants, exécutables de référence, traces, résultats des deux moteurs, liste des constructions refusées et benchmark documenté.

**Mesures et décision.** Exiger 100 % des cas déclarés dans le sous-ensemble conformes dans les deux moteurs, y compris erreurs et effets observables ; aucune approximation numérique non prévue. Chaque syntaxe hors périmètre doit être refusée avec position utile. Mesurer temps et mémoire sur cinq charges fixes ; un ralentissement compilé supérieur à 5× sur une charge représentative déclenche une analyse avant décision, sans imposer cette limite à l'interprète diagnostique.

**Si échec.** Corriger le modèle de valeurs ou l'IR avant d'ajouter des API. Si .NET empêche un contrat indispensable, essayer un backend alternatif sur ces mêmes cas. Si la sémantique ne peut être caractérisée, réduire publiquement le profil ou abandonner la promesse de compatibilité correspondante.

## P2 — Import texte hybride et voie des projets binaires

**Entrées.** Copies immuables des trois projets, dont un export texte identifié et, si le parc en contient, un projet natif ancien avec sa version autorisée. Inclure fenêtre interne, état, analyse, requête, classe, composant et ressources. Obtenir un inventaire de référence à partir de l'outil d'origine.

**Travail.** Détecter format/encodage sans se fier seulement à l'extension ; extraire traitements, propriétés et références avec provenance. Préserver les segments opaques. Pour le binaire, tester d'abord l'ouverture et l'export sur copie via les outils autorisés ; aucun décodeur binaire universel n'est présupposé. Reconstruire la référence après conversion pour détecter une altération due à celle-ci.

**Artefacts.** Inventaire avant/après, empreintes, manifeste normalisé, correspondances objet/traitement, archive des inconnues, journal de conversion et diff d'une modification locale.

**Mesures et décision.** Retrouver 100 % des blocs de code et ressources inventoriés du périmètre, avec identité octet pour octet ou transcodage réversible déclaré. Toutes les propriétés indispensables au pilote sont récupérées ou bloquent explicitement l'élément. Aucun inconnu n'est supprimé. Un changement de libellé ne doit modifier que les éléments attendus. **Go binaire** uniquement si une voie reproductible restitue les métadonnées requises ; un export du code seul ne suffit pas.

**Si échec.** Demander un export plus complet au détenteur, limiter les versions prises en charge ou déclarer l'élément non importable. Si le parc prioritaire exige une reconstruction manuelle systématique, arrêter l'orientation « migration maximale » et chiffrer explicitement une autre approche.

## P3 — Boucle d'événements, fenêtres et modalité

**Entrées.** Écran Windows avec table liée, fenêtre modale, validation, raccourcis, événements de saisie/sortie, minuterie et callback. Capturer douze parcours déterministes et quatre scénarios de concurrence/fermeture sur la référence.

**Travail.** Exécuter le code importé via P1 dans un renderer Windows minimal. Construire répartiteur et contexte, puis tester focus, annulation, réentrance, modification programmée, fermeture pendant traitement et résultat modal. La prévisualisation du concepteur utilise ce même renderer dans un processus isolé.

**Artefacts.** Modèle UI, carte des événements, traces comparées, captures à DPI fixés, scénario clavier et liste de propriétés encore indisponibles.

**Mesures et décision.** Identité des événements déterministes et de leurs effets métier ; pour la concurrence, respect des relations d'ordre convenues sans exiger des horodatages identiques. Zéro validation omise, double écriture ou événement délivré à la mauvaise instance. Tous les parcours clavier terminent avec le même résultat. Les écarts visuels sont localisés et acceptés individuellement ; ils ne compensent pas un défaut fonctionnel. Mesurer latence p95 et mémoire sur matériel identique.

**Si échec.** Modifier ordonnanceur et contexte ; comparer WinForms et Avalonia sur le composant bloquant. Conserver Windows comme profil séparé. Une modalité desktop incompatible avec le navigateur ne doit pas conduire à modifier silencieusement le code du pilote.

## P4 — Contrats H* et conservation des données

**Entrées.** Analyse et base fictive représentative, contraintes, clés composées, doublons, NULL, mémo/binaire et deux clients concurrents. Inventorier précisément les signatures H* utilisées ; disposer d'une interface HFSQL et de droits d'utilisation vérifiés.

**Travail.** Réaliser au moins trente scénarios : recherche exacte/approchée, parcours/fin, filtre, tampon courant, modification, erreur, transaction/rollback, verrou concurrent et interruption de connexion. Comparer un adaptateur conservant HFSQL à la référence. Un essai PostgreSQL éventuel est une variante distincte, avec son propre rapport.

**Artefacts.** Contrat du fournisseur, traces de curseur et d'erreur, dump logique canonique, contrôles de volumes/empreintes, script de concurrence et procédure de restauration.

**Mesures et décision.** Zéro divergence sur état final, retour, curseur, transaction et invariant métier dans les scénarios annoncés. Les blocages concurrents respectent le contrat convenu, sans exiger une durée identique. Mesurer latence p50/p95, débit et comportement lors d'un arrêt brutal. Aucun passage en production si l'interface ne couvre pas un contrat H* indispensable. La seule réussite de requêtes SQL ne vaut pas réussite du prototype.

**Si échec.** Pont autorisé plus proche du moteur d'origine, réduction du profil ou maintien du module existant. Pour un remplacement SQL, construire une émulation démontrée ou accepter un changement explicite ; aucune double écriture non transactionnelle n'est retenue comme solution par défaut.

## P5 — États, pagination et PDF

**Entrées.** Trois états autorisés : facture avec montants et totaux, état avec ruptures/sous-totaux, document comportant images, codes-barres et événements. Fournir polices sous droits adéquats, formats papier, marges, imprimante et PDF de référence. Utiliser cinq jeux par état, dont vide, une ligne et saut de page limite.

**Travail.** Importer bandes, liaisons et traitements ; construire un layout documentaire avec pagination et génération PDF. Tester aperçu et une impression réelle, sans remplacer les traitements d'état par une réécriture métier.

**Artefacts.** Modèle d'état, PDF générés, extraction de texte/valeurs, rapport de pagination, comparaison des zones et protocole d'impression.

**Mesures et décision.** Zéro montant, libellé obligatoire, ligne ou code-barres absent ; totaux et ordre identiques. Même nombre de pages sur les cas de fidélité retenus. Fixer une tolérance proposée de 0,5 mm pour les zones critiques, à confirmer selon l'usage, avec contrôle visuel des écarts restants. Vérifier lecture des codes-barres et absence de texte tronqué. Un simple pourcentage de pixels semblables n'est pas un critère suffisant.

**Si échec.** Évaluer un moteur documentaire différent sur les mêmes états, maintenir temporairement l'impression d'origine ou restreindre publiquement les types d'états supportés. La facture du pilote demeure bloquante.

## P6 — Débogage dans le code d'origine

**Entrées.** Backend compilé P1, écran P3, procédure interne, appel imbriqué, variable par référence et erreur déclenchable. Définir quinze manipulations attendues par un développeur WINDEV.

**Travail.** Relier positions conteneur/traitement/IR/backend ; implémenter DAP minimal, documents virtuels WLangage, variables et évaluation contrôlée. Tester points d'arrêt, pas à pas, pile, exception, modification de valeur et changement d'un fichier après compilation.

**Artefacts.** Tables de correspondance, adaptateur, enregistrement des parcours, tests de positions et rapport des capacités annoncées.

**Mesures et décision.** Les quinze manipulations s'effectuent sans ouvrir le C# généré ; chaque arrêt pointe vers le bon traitement et chaque valeur respecte le type WLangage. Un point non réalisable est indiqué non vérifié, jamais affiché comme actif à tort. Une version source discordante est détectée. Toute erreur de pile ou d'alias critique interdit la certification du débogueur.

**Si échec.** Renforcer le mapping ou fournir temporairement un mode interprété explicitement limité. Si le pilote n'est débogable qu'en langage hôte, la promesse d'expérience familière n'est pas validée.
