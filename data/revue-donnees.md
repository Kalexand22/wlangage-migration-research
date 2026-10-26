# Revue finale : données, intégrations et cibles

Revue du 26 octobre 2026 sur `docs/00-synthese-et-decisions.md`, `docs/04-donnees-integrations-et-cibles.md`, `examples/profil-migration.exemple.json` et les **500 lignes** de `data/fonctionnalites.csv` alors présentes. Aucun code ou moteur n'a été exécuté ; revue documentaire uniquement.

## Conclusions et corrections réalisées

- Aucune promesse générale de migration intégralement compatible ou de perte nulle n'a été trouvée dans la synthèse ; les profils et preuves sont conditionnels.
- Le profil JSON distingue proposition, absence d'implémentation et absence de qualification ; les valeurs inconnues bloquent la génération. Il ne démontre aucune compatibilité.
- Le chapitre 04 sépare bien ODBC, OLE DB, connecteurs WLangage et API `H*`. Il traite les curseurs, tampons, verrous, erreurs et différences des cibles.
- Le protocole de bascule interdit la double écriture indépendante et exige une autorité unique. Le retour arrière après écritures impose réconciliation, réplication inverse qualifiée ou perte explicitement décidée.
- **Précision ajoutée dans le seul chapitre 04 :** l'absence de perte signifie absence de perte supplémentaire par rapport au type et au profil source ; arrondis et troncatures d'origine doivent rester observables.
- **Ambiguïté corrigée dans le seul chapitre 04 :** le retour par simple routage concerne l'absence d'écriture **métier autoritative après bascule**, et non l'absence d'écriture technique de chargement initial. Il suppose aussi l'absence d'effets externes à compenser.

## Familles à expliciter lors de la fermeture du catalogue

Ces éléments ne sont pas explicitement distingués dans les 500 lignes relues. Une source thématique démontre une famille, pas sa disponibilité sur toutes les versions et cibles.

| Priorité | Famille | Recette proposée | Source primaire déjà consultée |
|---|---|---|---|
| P1 ou P0 si utilisé | Indexation et recherche full-text : mots vides, synonymes, pertinence et mise à jour de l'index | Comparer résultats, ordre, ajout/modification et configuration linguistique ; distinguer la recherche vectorielle | [Index des fonctions HFSQL](https://doc.pcsoft.fr/en-US/?1000025085=), notamment les familles FT et listes de mots |
| P1 ou P0 si utilisé | Vues matérialisées et rafraîchissement, distincts d'une vue SQL réévaluée | Comparer état avant/après rafraîchissement, droits, planification et reprise après échec | [Fonctions HFSQL, RefreshView](https://doc.pcsoft.fr/en-US/?1000025085=), [vues SQL et renvoi aux vues matérialisées](https://doc.pcsoft.fr/fr-FR/?9000157=) |
| P1 ou P0 si utilisé | Fichiers/enregistrements inaltérables et contrôle d'altération | Vérifier le contrôle après modification autorisée puis altération volontaire sur copie jetable ; ne pas déduire une conformité légale générale | [Fonctions HFSQL, CheckUnaltered](https://doc.pcsoft.fr/en-US/?1000025085=) |

## Précisions de contrats à prévoir

- **F-0261** regroupe réplication universelle et serveurs spare. Les garder comme sous-contrats distincts : réplica maître/abonné et paquets transportables ne partagent pas le protocole d'une réplication de serveurs ou d'une promotion de secours. [HCréeRéplicaTransportable, source historique](https://doc.pcsoft.fr/fr-FR/?3044209=&verdisp=210).
- **F-0265/F-0266** peuvent couvrir les requêtes préparées/paramétrées, agrégations, UNION et HAVING, mais la recette détaillée doit les nommer lors du relevé des API et dialectes réellement utilisés. Pas besoin de multiplier artificiellement les lignes de familles si le registre détaillé les prend en compte.
- **Profil JSON :** avant exécution réelle, compléter explicitement les règles numériques (taille/signe, précision/échelle, arrondi, débordement, conversions) et le profil de données (moteur/version/pilote, collation, isolation, verrous, nullabilité et source autoritaire). Le document reste actuellement un exemple non exécutable, donc l'absence de ces champs n'est pas un défaut d'implémentation.
- **Cibles :** le CSV possède une ligne de profil Windows/Linux/macOS et des lignes web/mobile. Pour la couverture calculée, décomposer chaque famille par OS, architecture et version source ; la colonne de cibles proposées n'est pas une déclaration de support PC SOFT uniforme.
- **Interop :** les exigences de JNI, COM, DLL, Office et matériel doivent conserver propriété de mémoire, threading, architecture et dépendance installée. Le chapitre 04 et les lignes existantes le signalent ; aucune portabilité automatique ne doit en être déduite.

Cette revue est une entrée du registre des inconnues. Les ajouts éventuels au catalogue principal doivent recevoir des identifiants stables et rester non implémentés/non qualifiés tant qu'aucune preuve n'existe.


## Clôture de la revue de livraison

La matrice finale comporte 517 exigences. Les familles supplémentaires signalées dans cette revue ont été intégrées et les contraintes des cibles natives ont été précisées. Les contrats détaillés et preuves d'exécution restent à construire suivant le chapitre 06. Le profil JSON inclut désormais des rubriques numériques et de données, laissées inconnues. Cette note conserve le constat historique de la revue, sans revendiquer une certification d'exhaustivité.
