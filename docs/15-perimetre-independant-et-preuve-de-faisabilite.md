# Périmètre retenu : aucune DLL ni aucun outil PC SOFT

**Instruction explicite du propriétaire : aucune utilisation de DLL ou d'outil PC SOFT.** Cette contrainte gouverne la solution et sa chaîne de développement, import, compilation, exécution, test et déploiement. Elle remplace les options antérieures de pont, de maintien du moteur HFSQL et d'oracle exécuté sous WINDEV. Le [registre de contraintes](../data/contraintes-projet.json) en donne la forme structurée.

## 1. Ce qui est retenu ou exclu

| Sujet | Voie retenue | Voie exclue |
| --- | --- | --- |
| Sources | Fichiers utilisateur déjà fournis, lecture et analyse indépendantes | Ouvrir ou convertir le projet avec un IDE/outil PC SOFT dans notre procédure |
| Compilation | Frontend WLangage, IR et backend développés avec des outils indépendants | Compilateur, SDK, framework ou DLL PC SOFT |
| Exécution | Runtime original et composants tiers non PC SOFT admis pour leur version et leur usage | Chargement direct ou indirect d'un runtime PC SOFT |
| Données | PostgreSQL proposé, adaptateur H* original, schéma et données exploitables indépendamment | Serveur HFSQL, pilotes PC SOFT ODBC/OLE DB, WDSQL ou service relais WINDEV |
| Interface et états | Modèles et renderers originaux, métadonnées lisibles et références statiques | Moteur d'interface ou d'impression PC SOFT hébergé ou redistribué |
| Tests | Spécifications publiques, cas synthétiques et références préexistantes fournies avec provenance | Exécuter WINDEV comme oracle, ou déléguer cette exécution à un client/prestataire dans le protocole |

L'exclusion concerne les logiciels PC SOFT, pas le langage des sources utilisateur ni la lecture de documentation publique. Les références à .NET, à un compilateur C#, à PostgreSQL ou à une bibliothèque indépendante désignent des candidats. Leurs droits d’usage et obligations doivent être établis pour la version et l’acte envisagés avant leur utilisation effective. La similarité de noms d'API ne signifie pas la réutilisation de leur implémentation.

## 2. Conséquences sur l'import et les données

Un export textuel déjà disponible peut être lu sans appeler son outil d'origine. Sa provenance, sa version et ses limites restent enregistrées. Le système ne demandera pas une conversion supplémentaire sous WINDEV comme étape cachée de la migration.

Si les fenêtres, états ou fichiers de données ne sont disponibles que dans un format opaque, trois états sont possibles : un lecteur indépendant a été qualifié pour ce format précis ; une représentation exploitable existe déjà parmi les entrées ; ou l'élément reste non importable. Il est conservé et signalé, et la génération de la fonctionnalité affectée est bloquée. Aucune reconstruction hypothétique n'est considérée comme fidèle.

En particulier, choisir PostgreSQL ne rend pas automatiquement lisibles des fichiers `.fic`, `.ndx` ou `.mmo`. Il faut un schéma et des données déjà exploitables, ou développer et qualifier une voie de lecture indépendante. Les propriétés HFSQL observables dans le code H* restent à reproduire dans un adaptateur original ; les traduire en SQL ne suffit pas toujours.

## 3. Preuve de faisabilité possible dans ce périmètre

La première démonstration peut construire et exécuter un sous-ensemble WLangage synthétique sans installer PC SOFT : lexique, types, conversions, appels, événements et stockage indépendant. Elle prouve le fonctionnement de ce sous-ensemble selon sa spécification.

Des sources, sorties, documents ou traces déjà fournis peuvent ensuite servir de références statiques si leur origine et leurs droits sont identifiés. Le comparateur doit détecter les divergences sans fabriquer de valeur de référence. Une observation manquante reste inconnue. Cette méthode peut établir une conformité sur des cas documentés ; elle ne certifie pas tous les comportements historiques de WINDEV.

Un patrimoine qui ne fournit ni métadonnées interprétables ni résultats de référence pourra donc présenter des blocages de faisabilité. Ils doivent être mesurés et expliqués. La contrainte d'indépendance est conservée même lorsqu'elle rend une migration particulière impossible sans travail supplémentaire.

## 4. Critères d'indépendance à vérifier

- Construire et lancer le prototype sur une machine propre sans installation PC SOFT.
- Examiner la provenance, les dépendances transitives et les composants du paquet, au-delà de leurs seuls noms de fichiers.
- Relever les commandes, processus, modules chargés et destinations réseau ; aucun outil, serveur ou service PC SOFT ne participe à une étape.
- Conserver des journaux de test et une nomenclature de dépendances permettant de répéter cette vérification.
- Signaler toute dépendance détectée au lieu de proposer automatiquement un pont ou un export PC SOFT.

Ces contrôles sont des exigences du futur prototype, pas des essais déjà exécutés. Les scripts du dépôt vérifient la cohérence documentaire de cette contrainte ; ils n'inspectent pas un compilateur ou une application encore inexistants.

## 5. Droit et publication

La clause d'utilisation de WINDEV ou de son framework ne doit pas être présentée comme un veto démontré contre une chaîne qui n'en utilise aucun. La provenance des informations, le droit sur les fichiers et ressources, la documentation, les marques et l'absence de copie de code restent des sujets distincts. Le [chapitre 09](09-propriete-intellectuelle-et-licences.md) conserve cette analyse sans imposer une consultation préalable générale au code original.

Le choix d'une licence de publication reste différé. L'évaluation porte maintenant sur l'import indépendant, la sémantique, le runtime, les données et la preuve de fonctionnement du sous-ensemble choisi.


## 6. Admission des outils et conformité documentée

La règle précisée par le propriétaire est : **n’accepter aucune incertitude juridique ou réglementaire identifiée non résolue pour un acte effectivement réalisé**. L’exclusion PC SOFT reste celle du scénario courant ; l’indépendance d’un autre outil ne lui donne pas automatiquement un droit d’entrée.

Avant d’introduire un outil, une bibliothèque, une dépendance transitive, une police, un modèle ou des données tiers dans le prototype, établir une fiche portant sur :

1. l’artefact, sa version ou son empreinte et son origine ;
2. les actes prévus — installer, prototyper, importer, compiler, tester, exécuter, héberger, modifier ou diffuser ;
3. le texte de licence, contrat ou autorisation applicable et les droits nécessaires à ces actes ;
4. les obligations correspondantes et leur respect : notices, attribution, modifications, accès aux sources ou restrictions lorsqu’elles sont applicables ;
5. les règles effectivement applicables au contexte, au rôle, au territoire et aux données, ou une non-applicabilité motivée ;
6. la décision, sa date, son périmètre et les événements imposant une nouvelle vérification.

Le [registre d’admission](../data/admission-outils.json) distingue les candidats et les usages admis. Les candidats actuels n’ont ni version sélectionnée ni admission ; la liste des composants du futur prototype réellement utilisés est vide. Ce registre concerne l’introduction des composants dans le produit étudié, et ne prétend pas réaliser un audit global des services de recherche déjà fournis par l’environnement.

**Doute, permission manquante, incompatibilité ou obligation non remplie : l’acte concerné reste bloqué.** Choisir un remplacement documenté, ou obtenir les éléments permettant de lever la question. Une interprétation spécialisée est recherchée si nécessaire ; aucun avis général n’est imposé à toute écriture de code original.

La vérification réglementaire part des activités réelles : droit sur les sources et ressources, confidentialité et données personnelles, puis exigences de sécurité produit ou d’IA si le produit, le rôle et l’usage entrent dans leur champ. Ne pas confondre l’utilisation d’un outil avec la mise sur le marché d’un produit, ni appliquer automatiquement toutes les obligations d’un autre acteur. L’absence d’usage ou une non-applicabilité doit être expliquée.

Une mise à jour, une nouvelle dépendance, un nouvel usage, un changement de licence, de territoire ou de traitement de données déclenche un réexamen. Une admission pour le build n’autorise pas implicitement la redistribution. Le choix de licence de publication de notre propre code reste différé.

Cette politique vise une conformité documentée et un refus des incertitudes non levées. Elle ne constitue ni une garantie absolue d’absence de risque juridique ni une certification automatique : les contrôles du dépôt vérifient les déclarations et leur cohérence, pas l’interprétation juridique des textes.
