# Revue croisée : synthèse, options et compatibilité du langage

Revue du 26 octobre 2026. Fichiers lus : `docs/00-synthese-et-decisions.md`, `docs/01-options-et-solutions-existantes.md`, `docs/02-langage-et-import.md`. Cette note conserve les constats de la revue initiale. Les corrections 1 à 6 ont été intégrées par la revue finale ; le séquencement interprète/backend est aussi clarifié en 00 et dans le cahier des prototypes 11. Ce fichier ne constitue plus une liste de défauts ouverts.

## Constats de la revue initiale

| Priorité | Emplacement | Constat | Correction recommandée |
|---|---|---|---|
| Haute | 02, §5.1, phrase sur les montants | Exiger une « absence de perte décimale » absolue peut contredire la compatibilité : le programme source peut posséder une précision limitée, des arrondis ou des troncatures intentionnels. | Écrire : « L'exigence est l'absence de perte supplémentaire par rapport au type, aux arrondis et au profil de référence ; préserver aussi les limites et troncatures documentées du programme d'origine. » |
| Moyenne | 00, §3, profil inconnu | « Refuser une valeur indispensable inconnue » est ambigu : cela peut laisser croire que l'import et son inventaire sont refusés dès qu'un réglage manque. Le chapitre 02 distingue bien analyse et génération. | Écrire : « Conserver le réglage comme inconnu dans le bilan, puis bloquer la génération du périmètre concerné jusqu'à sa résolution. » |
| Moyenne | 01, §2.2, métadonnée `license` | L'API renvoie une propriété présente avec valeur `null`, pas un champ absent. Cette valeur signifie qu'aucune licence reconnue n'a été détectée ; elle ne prouve pas, seule, l'absence de toute autorisation ailleurs. | Remplacer « champ license absent » par « aucune licence reconnue détectée par GitHub (`license: null`) ». Ajouter l'absence de fichier de licence dans l'arbre examiné et d'annonce de licence dans le README, avec commit figé ci-dessous. |
| Moyenne | 01, §2.2, réutilisation de `wl2net` | La prudence sur le réemploi est correcte, mais une source primaire juridique est utile. Distinguer le droit de consultation/fork sur GitHub d'un droit général d'exploitation et redistribution. | Ajouter un lien vers [GitHub, Licensing a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository). Formulation proposée : « Aucune autorisation générale de réemploi n'a été identifiée dans les éléments examinés ; obtenir une licence ou autorisation explicite avant intégration. » |
| Moyenne | 01, §2.2, `ET` vers court-circuit | Le risque indiqué est juste. Il ne faut pas transformer cette alerte en affirmation que `ET` serait toujours non court-circuité. Une option rend l'évaluation optimisée active, notamment par défaut dans les nouveaux projets depuis 2024. | Ajouter [PC SOFT, opérateurs logiques](https://doc.pcsoft.fr/?1512003=) et renvoyer au profil importé. Le tableau du README `wl2net` annonce effectivement `ET/OU` vers `&&/||` ; ce n'est pas une preuve que toutes les options de projet sont gérées. |
| Faible | 02, §5.6, arguments exprimés | L'exigence de traitement des paramètres est pertinente, mais peut être comprise comme une promesse qu'une expression arbitraire se passe par référence. | Écrire : « Caractériser séparément variables affectables, éléments de tableaux, propriétés, constantes et expressions : création éventuelle d'un temporaire, conversions et possibilités de propagation des mutations. » |
| Faible | 00, §4 et 02, §6 | 00 privilégie un backend .NET ; 02 recommande de commencer la caractérisation avec un interpréteur ou une VM. Ce n'est pas contradictoire si l'on sépare prototype sémantique et backend produit, mais l'ordre mérite d'être explicite. | Ajouter : « Le premier harnais peut interpréter l'IR ; le backend .NET ne devient référence de production qu'après passage de la même suite de conformité. » |

## Vérification supplémentaire de `wl2net`

Lecture publique de l'API GitHub et du README effectuée pendant cette revue :

- Dépôt : [lukimperinetti/wl2net](https://github.com/lukimperinetti/wl2net).
- Branche : `main` ; `archived: false` ; `license: null`.
- Commit examiné : `7fd8a11402e71ce38b713b06e556669c45f33942`.
- Arbre récursif non tronqué : aucun fichier de licence identifié parmi les chemins retournés.
- Le [README figé](https://github.com/lukimperinetti/wl2net/blob/7fd8a11402e71ce38b713b06e556669c45f33942/README.md) ne contient pas de déclaration de licence repérée par les termes licence/license, copyright ou SPDX. Cela n'est pas un audit juridique de tous les fichiers et contributions.
- Le README annonce des limites sur l'UI, HFSQL, l'analyse sémantique et les types avancés. Le chapitre 01 les présente correctement comme déclarations de l'auteur, sans reprendre son estimation chiffrée de gain.

Une première commande `gh api` sur les métadonnées a renvoyé HTTP 401 pendant la revue ; la lecture publique HTTPS de ces mêmes métadonnées a ensuite réussi. Aucun résultat 401 n'a été interprété comme preuve d'absence du dépôt ou de sa licence.

## Points cohérents à conserver

Les trois chapitres distinguent correctement maintien du WLangage, import du projet, équivalence d'exécution et compatibilité UI. Ils n'annoncent ni conversion universelle des formats binaires ni réexport natif déjà assuré. Les limites sur le catalogue exhaustif, les cibles et les corpus absents sont explicites. Le traitement des options de court-circuit du chapitre 02 est juste ; il faut conserver cette nuance dans toutes les synthèses et exemples. Les citations PC SOFT fondées sur des extraits indexés sont accompagnées d'une réserve claire dans 02.
