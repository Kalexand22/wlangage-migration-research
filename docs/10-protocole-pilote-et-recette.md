# Protocole indépendant d'audit, pilote et recette

Ce protocole décrit des travaux à réaliser ; **il n'a pas été exécuté sur des projets clients dans cette étude**. Les modèles du dossier `examples/` ne sont pas des formats PC SOFT normatifs et ne réalisent aucun import ni test de compatibilité.

**Contrainte ferme : aucune DLL ni aucun outil PC SOFT à aucune étape.** Import, compilation, exécution, qualification, déploiement et support utilisent une chaîne indépendante. Aucun serveur/pilote HFSQL, pont WINDEV/WEBDEV, convertisseur, outil d'extraction ou oracle PC SOFT ne doit être exécuté, y compris côté client pour ce protocole. La consultation de documentation publique et l'analyse des sources métier déjà fournies restent des travaux de recherche distincts.

## 1. Définir un périmètre fermé et des entrées déjà disponibles

Décrire le patrimoine à partir des informations reçues : produit/version/build d'origine, configuration, options, cibles, encodage, dépendances et fonctions métier. Un paramètre absent reste inconnu ; aucune exécution de l'ancien IDE ou de l'application n'est prévue pour le découvrir.

Le pilote possède quatre ensembles : originaux reçus immuables, métadonnées et données exploitables indépendamment, références préexistantes licites, résultats de la nouvelle implémentation. Le titulaire fournit ses sources métier ; il ne s'agit jamais de demander le code d'implémentation du compilateur, du moteur ou des DLL PC SOFT. Les données sensibles restent dans l'environnement autorisé et les preuves partagées contiennent des jeux synthétiques ou anonymisés.

Choisir une difficulté représentative : saisie maître/détail avec transaction ; recherche indexée et filtre ; état paginé ; traitement asynchrone ; intégration tierce indépendante. Si une famille est absente, justifier sa non-applicabilité et choisir un autre risque. Le choix dépend aussi des références disponibles : une fonction dépourvue d'attendu ne peut pas recevoir une preuve de parité par simple succès d'exécution.

## 2. Contrat du paquet d'entrée

Le tableau décrit des éléments **déjà fournis** et exploitables avec des lecteurs indépendants. Il ne constitue pas une demande de génération d'exports, d'instrumentation ou de relance du produit PC SOFT.

| Ensemble | Entrée admissible | Contrôle et blocage |
|---|---|---|
| Sources métier | Texte WLangage et éléments de projet lisibles déjà reçus | Droits, empreintes, inventaire et provenance ; absence d'outillage PC SOFT |
| Métadonnées d'origine | Version/build/options décrits dans fichiers ou documents préexistants | Cohérence et surcharges ; inconnu maintenu comme tel |
| Interface | Propriétés textuelles, ressources, événements, captures et descriptions déjà fournis | Objets recensés indépendamment ; propriété opaque signalée |
| Données | CSV/JSON/SQL ou autre format décrit, schéma, contraintes, clés et mémos | Types, encodage, précision, `NULL`, cohérence du lot et date de référence |
| États | Sources lisibles, ressources et documents préexistants licites | Pagination, droits des polices, données d'entrée et paramètres connus |
| Intégrations | Contrats et SDK non PC SOFT, matériel et bibliothèques indépendantes | Licence, architecture et dépendances transitives ; composant PC SOFT exclu |
| Déploiement cible | Manifeste et configuration de notre chaîne indépendante | Installation sur poste vierge sans serveur, pilote ni activation PC SOFT |
| Références de résultat | Fixtures, traces, exports, captures ou documents préexistants avec provenance | Profil connu, correspondance des entrées, intégrité et limites d'observation |
| Recette métier | Scénarios, invariants, erreurs attendues et décisions déjà disponibles | Responsable métier, criticité et distinction entre historique et nouveau contrat |

**Fichiers opaques :** un paquet uniquement composé de `.fic/.ndx/.mmo`, d'une analyse native illisible ou d'autres conteneurs sans lecteur indépendant qualifié bloque les fonctions qui en dépendent. Aucun lecteur complet n'est démontré ici. Les fichiers sont inventoriés sans être ouverts avec une DLL ou un outil PC SOFT. L'absence d'export logique exploitable n'est pas contournée par une demande d'extraction au client.

Un composant tiers compilé non PC SOFT peut rester une dépendance si ses droits, son interface et sa chaîne de chargement sont qualifiés. Un composant exigeant le framework PC SOFT est exclu, même présenté comme une DLL métier ou un service distant.

## 3. Inventaire des éléments, pertes et dépendances interdites

Chaque objet reçu possède un identifiant et une provenance : chemin, conteneur, élément, événement, intervalle de texte, empreinte et version du lecteur indépendant. Le graphe représente appels, lectures/écritures, affichage, contenu, héritage, impression et ressources.

Pour chaque propriété : `reconnue`, `préservée opaque`, `convertie avec règle`, `reconstituée par preuve`, `manquante` ou `non applicable justifiée`. Ces statuts décrivent l'import, pas la compatibilité d'exécution. Une propriété opaque peut être conservée pour diagnostic ; son utilisation reste bloquée si elle exige un composant PC SOFT. Aucun pont n'est autorisé comme solution de repli.

Le rapport indique traitements présents, événements attribués, sections non interprétées, sources absentes, chemins dynamiques indéterminés et dépendances exclues. La génération du périmètre concerné est bloquée si une absence peut affecter une exigence obligatoire. Une approximation graphique peut servir de maquette, mais ne compte pas comme import fidèle.

L'inventaire d'outillage couvre importeur, compilateur, interprète, bibliothèques, serveur, pilote de données, SDK, générateurs de documents, outils de tests et jobs CI. Croiser nomenclature, configuration, binaires et chargements observés. Un appel réseau vers un service PC SOFT ne devient pas admissible parce qu'aucune DLL locale n'est chargée.

## 4. Tranche verticale sur la nouvelle implémentation

Exemple synthétique : « enregistrer une commande et produire son document ». Il sert à illustrer la méthode ; il ne décrit pas un projet client reçu.

1. Charger le schéma et le jeu initial déjà fournis dans PostgreSQL ou un autre moteur indépendant qualifié.
2. Ouvrir l'écran produit par notre runtime ; vérifier valeurs, focus et événements selon la spécification disponible.
3. Saisir client et ligne ; contrôler masques, entrée/sortie et recalcul.
4. Provoquer une erreur métier puis une concurrence entre deux sessions de notre runtime ; observer transaction et état final.
5. Fermer puis rouvrir dans notre application ; vérifier clés, montants, relations et `NULL`.
6. Générer le document par notre moteur indépendant ; contrôler contenu, pagination et exports.
7. Simuler coupure réseau, manque d'espace ou arrêt de la cible à une étape pertinente, puis tester sa reprise.

Les effets externes utilisent des doubles de test ou un environnement tiers indépendant prévu pour la recette ; ne pas créer de commandes, paiements ou emails métier en double. Les entrées initiales et références sont figées avant comparaison. Aucune étape ne lance l'application d'origine.

## 5. Références acceptables et force de la preuve

Le référentiel attendu peut être constitué de résultats préexistants licites fournis, d'un contrat documenté ou d'une décision métier explicite. Il n'est pas un oracle PC SOFT exécuté par notre équipe, notre CI ou le client pour ce workflow. Une réponse de modèle de langage peut aider à formuler un cas, jamais devenir une observation historique.

| Type de référence | Ce qu'elle permet | Ce qu'elle ne démontre pas |
|---|---|---|
| Fixture historique déjà fournie, entrées et profil connus | Comparaison sur ce cas précis | Toutes versions, plateformes et surcharges |
| Trace ou document préexistant partiellement décrit | Vérification des observations réellement visibles | Événements internes ou contexte non enregistrés |
| Contrat public ou spécification métier indépendante | Test de conformité à ce contrat | Identité avec un comportement historique non observé |
| Invariants, propriétés et tests métamorphiques | Cohérence des résultats et résistance aux erreurs | Parité avec l'ancien moteur |
| Aucune référence exploitable | Détection d'un manque de preuve | Aucun statut conforme par défaut |

Conserver origine, auteur, date de production si connue, date de réception, droits, empreinte, version/profil déclaré et niveau de complétude. Un export de référence sans les entrées correspondantes peut être utile à l'analyse, mais ne ferme pas un test différentiel. Une trace déjà disponible ne justifie aucune nouvelle instrumentation de l'ancien produit.

Les comparaisons doivent détailler leur objet : types/valeurs/échelles et erreurs pour les calculs ; focus, navigation et observations d'événements pour l'interface ; clés, relations et effets de transaction pour les données ; texte, positions, ruptures et pages pour les documents ; encodages et messages pour fichiers/réseau ; état final et récupération pour les erreurs. Le contrôle d'un PDF ne démontre pas le même nombre d'appels à une procédure de bloc si aucune trace ne le renseigne.

Temps, aléatoire, GUID et chemins temporaires peuvent être normalisés avec une règle justifiée et testée. Ne pas ajouter un arrondi global qui masque un écart métier. Les performances de notre cible se mesurent ; une comparaison à l'ancien produit n'est publiée que si des mesures préexistantes suffisamment contextualisées sont disponibles.

## 6. Batteries à construire avec des outils indépendants

**Langage :** limites numériques, débordements, conversions, précision monétaire, dates vides/invalides, changements d'heure, ANSI/Unicode, indices, copie/référence, portées, paramètres, POO, erreurs, indirection et compilation dynamique de notre runtime. Tester chaque profil documenté ; l'inconnu n'est pas remplacé par le réglage le plus commode.

**Interface :** initialisation, entrée/sortie, validation, tabulation, raccourcis, fenêtres modales, réentrance, plusieurs fenêtres, redimensionnement, DPI, thèmes, langues, lecteurs d'écran et équivalents des FAA. Les tests pilotent uniquement l'interface de notre application et les composants tiers autorisés.

**Données :** contrat original de l'adaptateur `H*` sur PostgreSQL : tampon courant, recherches, doublons, filtres, parcours après insertion, suppression logique, verrou occupé, annulation, erreurs, tri, clés composées, mémos, import ouvert et évolution du schéma cible. Deux sessions indépendantes de notre runtime caractérisent la concurrence. Aucun pilote HFSQL n'est chargé.

**États et intégrations :** blocs, ruptures, polices, nombres localisés, pages limites, impression, PDF, fichiers bureautiques, courrier, API et matériel tiers. SDK système et fabricants non PC SOFT admis après contrôle des licences et dépendances. Les doubles de test ne remplacent pas la qualification matérielle réelle lorsque cette fonctionnalité est revendiquée.

**Exploitation :** installation indépendante, compte non administrateur, mise à jour interrompue, sauvegarde/restauration PostgreSQL, secrets, certificats, pertes réseau, espace disque et crash. Tester aussi l'absence de toute installation PC SOFT sur la machine de construction et d'exécution.

## 7. Mesurer sans fabriquer une parité totale

Définir avant calcul les ensembles versionnés, corpus et dénominateurs. Publier séparément :

- **Intégrité d'inventaire :** éléments identifiés avec provenance / éléments du paquet reçu ; les objets opaques restent inclus. Cette mesure n'établit pas que le paquet couvre tout le patrimoine historique.
- **Conservation textuelle :** blocs identiques / blocs importés ; conversions d'encodage et adaptations métier comptées séparément.
- **Absence de réécriture manuelle :** traitements utilisés sans modification manuelle / traitements revendiqués dans le périmètre.
- **Couverture des références :** cas avec attendu exploitable / cas exigés ; montrer les attentes absentes ou partielles.
- **Qualification exécutée :** cas exécutés avec preuve / cas exigés, en distinguant comparaison à une fixture historique et test d'une spécification indépendante.
- **Conformité observée :** cas conformes à leur référence déclarée / cas exigés ; publier échecs, inconnus, non-exécutés et dérogations.
- **Complétude documentaire API :** signatures/cibles avec statut / catalogue daté ; cette mesure ne prouve pas l'implémentation.

Une fixture conforme démontre le cas comparable, pas la parité globale du WLangage. Un test d'invariant réussi démontre l'invariant de notre moteur, pas un comportement PC SOFT non observé. Les inconnus et dépendances interdites ne sont pas retirés discrètement du dénominateur. Publier les effectifs bruts et blocages critiques en plus des pourcentages.

## 8. Critères du premier pilote

Critères proposés, non atteints à ce jour : aucun composant PC SOFT dans la chaîne complète ; entrées lisibles suffisantes ; aucun élément requis perdu silencieusement ; événements attribués ; contrat et limites de chaque appel publiés ; aucun écart métier critique ouvert ; traitements revendiqués conservés sans réécriture ; aucun correctif direct du code généré ; reconstruction sur poste vierge ; restauration et rejeu sur la cible indépendante exercés.

Si les seules données sont opaques, si les options source restent critiques et inconnues ou si une référence indispensable manque, le résultat est « bloqué » ou « preuve insuffisante ». Le réduire à un sous-périmètre de prototype peut être décidé explicitement ; il ne devient pas une certification de migration complète.

Fixer budgets de latence, débit et mémoire par parcours avec volumes et matériel. Les défauts historiques visibles dans les références sont consignés ; leur correction volontaire devient une adaptation approuvée, sans être comptée comme reproduction identique.

## 9. Chargement, bascule et reprise sans retour au produit PC SOFT

Le paquet déjà fourni doit préciser cohérence, date et périmètre. Des incréments sont admissibles seulement s'ils sont déjà disponibles dans un format ouvert exploitable indépendamment, ou produits ensuite par un système indépendant qualifié. Une extraction nécessitant HFSQL, WDSQL, un pont ou un autre outil PC SOFT n'est pas une étape de secours ; elle bloque le mode de migration concerné.

La cible possède une seule autorité d'écriture par domaine. Charger d'abord dans une zone isolée, vérifier clés/effectifs/mémos/agrégats et règles métier, enregistrer les lots, puis publier le périmètre validé. Une copie de comparaison n'écrit pas en production. Toute propagation indépendante utilise ordre, idempotence, gestion des erreurs et reprise explicites.

Avant écritures métier autoritatives et effets externes, un chargement initial peut être annulé puis recommencé. Après écritures, restaurer une sauvegarde seule perdrait les opérations suivantes : exiger journal et rejeu, compensation qualifiée ou perte explicitement décidée. Le retour de version du code exige aussi un schéma compatible. Mesurer délai de reprise et perte maximale sur la nouvelle chaîne.

La procédure ne relance pas l'ancienne application et ne restaure pas HFSQL. Un export neutre de sauvegarde reste un moyen de réversibilité de notre cible ; il ne prouve pas qu'un produit exclu saurait l'ingérer. Le périmètre qui ne dispose pas d'une reprise indépendante acceptable reste bloqué pour la production.

## 10. Dossier de preuve à livrer

Livrer manifeste, profil, nomenclature des outils et dépendances, provenance des sources et données, inventaire des pertes, contrats API, adaptations, fixtures préexistantes et leurs limites, tests exécutés, résultats comparés, contrôles de données, empreintes, exploitation et écarts résiduels. Chaque preuve indique qui, quoi, quand, avec quelle entrée, quelle référence et quelle configuration indépendante.

La preuve vaut pour un corpus et une version de notre runtime. Tout changement susceptible d'affecter les résultats remet les cas concernés à qualifier. La documentation décrit le patrimoine PC SOFT sans l'exécuter ; les résultats de notre implémentation et ceux déjà reçus sont distingués explicitement.
