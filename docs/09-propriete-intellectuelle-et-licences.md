# Propriété intellectuelle, interopérabilité et licences

Date de recherche et de relecture : **26 octobre 2026**. Périmètre : étude de faisabilité, sans choix de licence de publication ni décision de commercialisation.

> **Périmètre ferme : seule l'implémentation A, 100 % indépendante, est retenue.** Aucun logiciel, outil, DLL, runtime, SDK, pilote, serveur HFSQL ou pont PC SOFT n'est utilisé dans l'import, la compilation, la construction, l'exécution ou les tests. Aucun oracle WINDEV n'est exécuté par l'équipe, un client ou un tiers pour ce workflow. La documentation publique peut être lue et référencée; aucun code PC SOFT n'est copié. Les seuls apports du client sont des fichiers, exports ou traces **déjà existants**, avec leur provenance et les droits correspondants; leur réception ne commande pas une nouvelle opération dans WINDEV.

## 1. Chaîne autonome retenue et portée des restrictions d'utilisation

La [licence WINDEV, article 4](https://doc.pcsoft.fr/fr-FR/?4510001=&name=License_WINDEV), et la [licence du Framework, article 3](https://doc.windev.com/fr-FR/?1000019581=&name=licence_framework_windev), visent l'utilisation des logiciels couverts pour créer et diffuser des outils de développement comparables. **L'applicabilité de cette restriction à notre chaîne qui n'utilise aucun de ces logiciels n'est pas démontrée.** Elle ne constitue pas ici un verrou ni un risque M1 générique imposé au prototype indépendant.

| Cas étudié dans la recherche | Statut dans le projet retenu | Conséquence |
| --- | --- | --- |
| **A — compilateur C#/runtime et outillage originaux** | **Seule voie active**, sans exécution ni incorporation de logiciel PC SOFT | Continuer étude, conception, importeur, moteur et tests originaux; tracer les sources d'information et les matériaux fournis. |
| **B — observation active d'un logiciel PC SOFT** | **Exclue des étapes actives**, y compris si un client ou prestataire exécuterait le logiciel pour nous | Les règles d'observation exposées plus loin expliquent la jurisprudence; elles ne servent pas à programmer un oracle ou une campagne comparative. |
| **C — réemploi de logiciel/composants/services PC SOFT** | **Exclu**, y compris runtime, SDK, serveur/pilote HFSQL, utilitaire et pont | Les licences analysées restent une information historique et comparative; aucun montage de réemploi n'est à valider pour la cible actuelle. |

L'étude, le code original et ses tests sur la nouvelle chaîne peuvent avancer. Les droits sur les fichiers reçus, les formats, la documentation et les signes distinctifs restent des questions séparées; l'absence de logiciel PC SOFT n'établit pas une licéité universelle de tous les matériaux ou de toute commercialisation future. Aucun avis d'avocat n'a été obtenu, et aucun avis général n'est posé comme préalable au prototype. Le [relevé de lecture](../data/revue-contractuelle-2026.md) conserve les sources et limites des analyses comparatives.

## 2. Trois droits à distinguer dès le départ

Le projet doit séparer : **les sources métier de l'utilisateur**, **l'implémentation de PC SOFT** et **les dépendances redistribuées**. Posséder les sources d'une application ne donne pas automatiquement le droit de copier le compilateur, les DLL, la documentation, les images, les modèles ou les composants d'un tiers. À l'inverse, l'existence de droits sur le compilateur ne suffit pas à interdire toute implémentation indépendante d'un langage.

Pour la chaîne retenue, l'inventaire porte sur auteur/titulaire, provenance, droits sur les fichiers fournis et sources publiques utilisées. Les fichiers applicatifs d'un client peuvent contenir des ressources ou composants tiers : ils doivent être distingués de son code métier. La compatibilité d'un format ou d'une syntaxe ne vaut pas autorisation de copier une implémentation ou un manuel.

## 3. Cadre comparatif UE, Royaume-Uni et États-Unis

**Cette section conserve l'explication juridique de l'étude. Elle n'autorise ni ne planifie une observation active, une décompilation ou l'utilisation de WINDEV dans la chaîne retenue.** Les données historiques licitement reçues sont examinées comme des entrées existantes, pas comme le résultat d'un oracle à faire fonctionner.

La [directive 2009/24/CE](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32009L0024) distingue l'expression protégée d'un programme de ses idées et principes. Son **article 5 §3** protège l'observation, l'étude et le test par l'utilisateur habilité à l'occasion des opérations visées; l'**article 9 §1** prévoit la nullité des clauses contraires aux exceptions qu'il désigne. L'**article 6** encadre un autre cas : reproduction/traduction de code indispensable à l'interopérabilité, information non facilement accessible, parties nécessaires et limites d'utilisation/communication. Le simple besoin d'observer des résultats n'oblige pas à passer par cette voie de décompilation.

En France, [le CPI L122-6-1](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044365559) protège au **III** l'observation/étude/test lors d'opérations que l'utilisateur est en droit d'effectuer; son dernier alinéa rend nulles les stipulations contraires aux **II, III et IV**. Ce caractère impératif doit être pris en compte dans l'analyse de la licence, et pas relégué derrière elle. Le **IV** concerne les actes indispensables à l'interopérabilité; le **I** traite utilisation conforme et correction, avec des modalités contractuelles possibles. Exécuter un programme test original et en comparer la sortie n'est pas en soi décompiler le compilateur. Ces règles restent attachées à leurs conditions et ne couvrent pas automatiquement la redistribution du moteur ou la copie d'un manuel.

Dans [SAS Institute / World Programming, CJUE C-406/10, 2 mai 2012](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:62010CJ0406), les points **50–53** établissent le droit d'observation et rappellent la nullité des clauses contraires; les points **59–62** l'articulent avec les actes que l'utilisateur a le droit d'effectuer et le respect des droits exclusifs. Il s'agit d'un appui substantiel à une implémentation compatible obtenue par observation licite, sans accès au code du programme d'origine. L'arrêt distingue aussi fonctionnalités/langage/formats de l'expression protégée et examine séparément les éléments originaux du manuel. Il ne juge pas la clause PC SOFT sur les faits de ce projet.

L'application nationale est vérifiable dans [SAS Institute v World Programming, High Court, **[2013] EWHC 69 (Ch)**, 25 janvier 2013](https://caselaw.nationalarchives.gov.uk/ewhc/ch/2013/69), notamment points **61, 64–79** : le juge retient la protection d'observation dans ce litige et écarte les restrictions incompatibles dans la mesure de cette contradiction. La finalité de construction du logiciel concurrent ne retire pas, dans son raisonnement, cette protection. Le point **82** conserve toutefois le succès partiel de la demande concernant le manuel. Cette décision, rendue au Royaume-Uni en application du droit de l'Union alors applicable, éclaire le cas B historique, exclu du workflow; elle ne constitue pas un jugement français sur toutes les clauses d'un autre éditeur.

La comparaison territoriale doit rester précise. Dans [SAS v WPL, Fourth Circuit, **24 octobre 2017**, nos 16-1808/16-1857](https://www.ca4.uscourts.gov/opinions/161808.P.pdf), la juridiction américaine confirme une responsabilité contractuelle en droit de Caroline du Nord et explique le désaccord avec le traitement européen, notamment pages 12–18 du PDF. L'arrêt du [**12 mars 2020**, nos 19-1290/19-1300](https://www.ca4.uscourts.gov/opinions/191290.P.pdf), porte sur des injonctions destinées à rendre effectif le jugement américain. Il ne renverse pas le droit européen d'observation. Ces décisions justifient d'examiner les territoires de commercialisation; elles n'invalident pas la faisabilité d'un code indépendant développé en France/UE.

L'arrêt [Top System / État belge, **C-13/20**, 6 octobre 2021](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:62020CJ0013), traite encore une autre finalité : la décompilation nécessaire à la correction d'erreurs par un acquéreur légitime, sans application automatique des conditions de l'article 6. Il encadre nécessité, modalités contractuelles et usage des résultats; voir points **53 et 57–74**. Le présent projet n'assimile pas la construction du compilateur compatible à la correction d'une erreur de WINDEV.

Enfin, [l'article 1190 du Code civil](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032041260/) donne une règle d'interprétation en cas de doute, notamment contre le proposant d'un contrat d'adhésion; ce n'est pas une règle générale d'annulation. [L'article 1199](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032041378/) rappelle l'effet relatif du contrat. Identifier les parties, employeurs et mandats est donc pertinent; cela ne dispense pas de respecter les droits opposables indépendamment d'un contrat.

## 4. Licences et HFSQL : résultats documentaires hors cible

Les licences WINDEV, Framework et Outils ont été lues pour vérifier les restrictions qui avaient été évoquées. La [licence des outils](https://doc.windev.com/fr-FR/?4510003=&name=Licence_Outils) lie leur diffusion aux applications qu'elle désigne; la clause identique de création d'outils concurrents n'a pas été trouvée dans cette page. Aucun de ces outils n'est utilisé ou livré par la cible actuelle.

Les [CGV publiées par PC SOFT](https://pcsoft.fr/pcsoft/conditions-generales-de-vente.htm) servaient lors de la consultation un PDF v1.6 du 25 mars 2026, décrivant notamment une version figée sous conditions. Cela renseigne les contrats historiques; aucune utilisation de ces logiciels n'est requise par le projet indépendant.

La [licence OLE DB HFSQL](https://doc.pcsoft.fr/?1410087273) envisage des applications non WINDEV et encadre des fichiers redistribuables. L'article 5 de la [licence WINDEV](https://doc.pcsoft.fr/fr-FR/?4510001=&name=License_WINDEV) décrit un cas de diffusion HFSQL lié à plus de 50 % des fonctionnalités réellement utilisées par des applications WINDEV/WEBDEV et d'autres conditions de licence/version. Il serait inexact d'en déduire une obligation universelle du seul fait d'employer un autre langage, sans confronter périmètre, usages et licences spécifiques. **Cette comparaison n'ouvre aucune piste de maintien d'HFSQL dans la cible : serveur, pilotes, SDK et ponts PC SOFT sont exclus.**

Un éventuel lecteur indépendant de fichiers autorisés ou un import d'export existant relève d'une autre question que l'exploitation du moteur HFSQL. Il nécessite sa propre étude de format, sa provenance et ses preuves de comportement; les licences d'utilisation d'un serveur ne démontrent ni sa faisabilité technique ni une autorisation universelle. Aucun nouveau lancement d'un outil de conversion PC SOFT n'est prévu pour obtenir ces entrées.

## 5. Entrées et opérations autorisées dans l'étude

| Opération | Voie retenue | Limites et preuve utile |
| --- | --- | --- |
| Recevoir les sources métier | Fichiers déjà disponibles, fournis par leur titulaire ou une personne habilitée | Provenance, autorisation d'analyse, code salarié/prestataire et composants tiers distingués |
| Recevoir un ancien export ou une trace | Artefact existant, daté si possible, sans commander de nouvelle exécution | Origine, version et paramètres connus; inconnus conservés; pas de délégation d'oracle au client |
| Lire le format texte hybride | Importeur original analysant les fichiers autorisés et la documentation publique | Format lisible ne signifie pas spécification complète; aucune copie de parseur ou code PC SOFT |
| Étudier un format natif opaque | Lecture documentaire et analyse indépendante de matériaux autorisés | Pas de SDK, convertisseur, moteur ou outil PC SOFT; incertitudes de format explicitement rapportées |
| Implémenter la sémantique WLangage | Spécifications originales tirées des faits documentés, tests originaux sur le nouveau moteur | Attendus documentaires, traces existantes et hypothèses distingués; pas d'affirmation d'équivalence différentielle non mesurée |
| Migrer les données | Importeur autonome sur exports/fichiers existants autorisés, vers le stockage indépendant retenu | Aucun serveur ou pilote HFSQL, aucun pont ni nouvelle extraction commandée; complétude et types à vérifier |
| Créer l'expérience IDE | Reprendre les concepts nécessaires avec une interface et des textes originaux | Pas de ressources, logo, gabarit ou bibliothèque propriétaire incorporés |
| Constituer les tests | Code et jeux synthétiques originaux; traces historiques utilisables avec provenance | Aucun oracle PC SOFT dans l'équipe, chez le client ou sous-traité; trous de preuve visibles |

L'importeur doit écarter les composants propriétaires exécutables et signaler leurs références comme dépendances à remplacer. Recevoir un fichier de projet ne signifie pas exécuter le programme, les scripts ou les bibliothèques qu'il désigne.

## 6. Provenance et validation indépendantes

La traçabilité soutient une création originale; la qualification *clean room* n'accorde aucune immunité juridique et n'impose pas ici une équipe n'ayant jamais détenu de licence.

1. **Registre des informations** : URL et date des pages publiques lues, auteur/titulaire des matériaux reçus, statut de confidentialité et droits d'analyse. Référencer la documentation; ne pas copier son code, ses exemples ou ses illustrations dans l'implémentation.
2. **Spécifications originales** : distinguer faits documentés, traces existantes, déductions et hypothèses. Décrire entrées, sorties, événements et erreurs dans une rédaction propre au projet.
3. **Tests sur le nouveau moteur** : microprogrammes originaux, invariants métier, tests génératifs et contrôles sur les artefacts existants. Tout résultat attendu dont l'origine reste inconnue conserve ce statut; aucune égalité avec WINDEV n'est déclarée démontrée par cette seule méthode.
4. **Contributions traçables** : rattacher les changements aux spécifications et aux sources autorisées; écarter le code ou les assets propriétaires dont la réutilisation n'est pas établie.
5. **Chaîne vérifiable** : inventorier les dépendances non PC SOFT du dépôt, du build, du runtime et des tests; refuser un import qui lancerait un exécutable ou chargerait un plugin PC SOFT.

Un client peut transmettre un export ou une trace déjà en sa possession s'il dispose des droits correspondants. Le workflow ne lui demande pas de lancer WINDEV, de produire une nouvelle trace comparative ou d'opérer un service oracle. Cette limite réduit les possibilités de preuve : les divergences non décidables restent inconnues ou bloquent la certification de la fonctionnalité concernée, sans être masquées par un test simulé présenté comme référence historique.

## 7. Expérience familière, identité propre

Le besoin de ne pas perdre les développeurs se traduit par des concepts reconnaissables : projet, analyse, fenêtre, champ, événement, état, procédure, débogueur, aperçu et génération. Le nouveau produit peut proposer une configuration de raccourcis et un lexique de correspondance. Il doit adopter son propre nom, ses icônes, visuels, modèles et textes.

Ne pas copier les logos, captures de ruban, gabarits ou bibliothèques d'images PC SOFT comme assets distribués. Les références à WINDEV/WLangage/HFSQL doivent rester descriptives et ne pas suggérer un produit officiel, un partenariat ou une certification. Une formulation telle que « environnement indépendant destiné à exécuter des sources WLangage selon les profils de compatibilité publiés » est plus précise qu'un nom de produit reprenant la marque. Faire vérifier les règles de marque et les communications prévues dans les territoires de diffusion.

Le droit sur l'apparence d'une interface ne se résume pas au droit du logiciel. L'arrêt SAS ne règle pas toutes les questions de marques, dessins, concurrence déloyale ou parasitisme. L'équipe UX doit donc travailler à partir des tâches et comportements recherchés, puis produire une interface originale, testée avec les développeurs concernés.

## 8. Dépendances, licences du nouveau produit et distribution

Cette étude de faisabilité ne choisit aucune licence de publication, aucun modèle économique et aucune modalité de diffusion du futur compilateur. À ce stade, inventorier les contraintes des dépendances suffit; les décisions sur la licence du code original restent ouvertes. Les questions de lien, modification ou distribution ne deviennent concrètes qu'avec les composants et le mode de livraison effectivement retenus.

Exiger une nomenclature de composants, version verrouillée, auteur, licence, empreinte, notice et modalité de distribution. Le format [SPDX](https://spdx.dev/use/specifications/) fournit une référence primaire pour structurer ces informations. Une SBOM décrit les composants; elle n'accorde aucun droit supplémentaire et ne remplace pas leur lecture juridique.

Pour les dépendances indépendantes retenues, notamment .NET/WinForms si confirmé, vérifier les fichiers LICENSE et THIRD-PARTY-NOTICES de **la version réellement embarquée**, les dépendances natives et les packs de distribution. Pour Avalonia, distinguer le cœur et les éventuels services/outils commerciaux. Pour Qt, si cette option revient dans les arbitrages, distinguer les modules, licences libres et offre commerciale; ne pas supposer qu'un choix de toolkit règle tout le produit.

Les dépendances indépendantes de polices, PDF, codecs, cartographie, Office, cryptographie, périphériques et mobile méritent chacune une ligne; aucun pilote ou composant PC SOFT ne fait partie de cette liste autorisée. Les droits sur un code-barres ou un standard documentaire ne garantissent pas que la bibliothèque retenue soit redistribuable selon le modèle voulu. Les stores, certificats, SDK Apple/Android et contrats de signature appartiennent également au dossier de livraison.

## 9. Données clients et corpus de certification

La compatibilité nécessite souvent des données représentatives, mais le code source peut déjà contenir des identifiants, clés ou informations personnelles. Fournir un scanner local de secrets et un inventaire des fichiers avant tout transfert au support. Préférer des reproductions minimales et des données synthétiques; l'anonymisation doit être vérifiée, pas présumée par retrait des noms.

Si des données personnelles sont traitées, déterminer finalité, rôles, base légale, durée, hébergement, accès, sous-traitants et transferts. Le [RGPD, notamment articles 5, 25, 28 et 32](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32016R0679), donne le cadre primaire pertinent. Les logs différentiels et captures d'écran sont inclus dans ce périmètre. Une architecture exécutant les tests localement chez le client peut limiter les transferts; elle n'élimine pas les obligations de sécurité.

Ne pas utiliser les projets clients pour entraîner un assistant ou enrichir publiquement les tests sans droits et engagements adaptés. Les suggestions par IA doivent avoir une origine et une politique de données explicites; elles ne constituent pas une méthode de blanchiment d'un code propriétaire.

## 10. Poursuite de la faisabilité et questions ultérieures

**L'étude et le prototype entièrement originaux peuvent avancer sans avis juridique général préalable.** La cible exclut l'utilisation de PC SOFT; aucune notation M1 générique « critique » ou « moyenne » n'est imposée au développement au titre des clauses d'utilisation de ces logiciels. Les anciens cas B/C servent uniquement à comprendre les textes et ne sont pas des étapes ou variantes actives.

Pendant la faisabilité, tenir un registre léger de provenance, inventorier les dépendances indépendantes et vérifier que l'import/build/runtime/tests ne lancent aucun logiciel PC SOFT. Conserver l'origine des fichiers, exports et traces existants; les références manquantes et comportements sans attendu fiable restent des questions de couverture à résoudre par la voie indépendante ou à déclarer inconnues.

Une consultation spécialisée reste recommandée avant une commercialisation éventuelle pour les matériaux réellement utilisés, formats, documentation, identité du produit et territoires. Elle peut être ciblée plus tôt si un acte sensible concret apparaît. Ce conseil n'est pas une condition pour commencer le code original. La licence de publication et les modalités de diffusion restent différées conformément au périmètre demandé.

L'absence de DLL ou d'outil PC SOFT ne règle pas à elle seule tous les droits sur le code client, les ressources, les données, la documentation ou les marques. Aucun avis particulier ni validation universelle de commercialisation n'est revendiqué par cette recherche.

## Sources primaires consultées

| Source | Usage dans ce chapitre | État de consultation |
| --- | --- | --- |
| [Directive 2009/24/CE](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32009L0024) | Expression, observation, interopérabilité | Texte/extraits officiels indexés; ouverture web parfois soumise à contrôle JavaScript |
| [CPI, article L122-6-1](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044365559) | Conditions françaises | Version officielle indexée, en vigueur depuis le 26 novembre 2021 dans la page consultée |
| [CJUE, C-406/10, ECLI:EU:C:2012:259](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:62010CJ0406) | Fonctionnalités/langage/formats, observation et clauses contraires | Points 50–53, 59–62; texte officiel indexé, reproduit également dans le jugement national officiel |
| [High Court, [2013] EWHC 69 (Ch)](https://caselaw.nationalarchives.gov.uk/ewhc/ch/2013/69) | Application positive de la protection d'observation dans SAS/WPL | Archives judiciaires officielles lues, notamment points 61, 64–79 et 82 |
| [Fourth Circuit, 24 octobre 2017](https://www.ca4.uscourts.gov/opinions/161808.P.pdf) | Responsabilité contractuelle en droit de Caroline du Nord | PDF officiel de la cour; ne pas transposer automatiquement à France/UE |
| [Fourth Circuit, 12 mars 2020](https://www.ca4.uscourts.gov/opinions/191290.P.pdf) | Injonctions d'exécution du jugement américain | PDF officiel; ne constitue pas une décision sur la validité des clauses PC SOFT en UE |
| [Code civil, art. 1190](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032041260/) et [1199](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032041378/) | Interprétation en cas de doute et effet relatif | Textes officiels Légifrance lus; pas de déduction de nullité universelle |
| [CJUE, C-13/20, ECLI:EU:C:2021:811](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:62020CJ0013) | Correction d'erreurs distincte de l'interopérabilité | Arrêt officiel, notamment points 53 et 57–74; pas une autorisation de créer un concurrent |
| [PC SOFT, licence WINDEV](https://doc.pcsoft.fr/fr-FR/?4510001=&name=License_WINDEV) | Restriction outils de développement, runtime et HFSQL | Page officielle HTTP 200 lue le 26 octobre 2026; version effectivement acceptée inconnue |
| [PC SOFT, licence du Framework](https://doc.windev.com/fr-FR/?1000019581=&name=licence_framework_windev) | Restriction portant sur l'usage du framework | Page officielle HTTP 200 lue le 26 octobre 2026 |
| [PC SOFT, licence des outils](https://doc.windev.com/fr-FR/?4510003=&name=Licence_Outils) | Diffusion liée à certaines applications | Page officielle HTTP 200 lue le 26 octobre 2026; mention WINDEV/WEBDEV 2025 dans le corps consulté |
| [PC SOFT, CGV](https://pcsoft.fr/pcsoft/conditions-generales-de-vente.htm) | Contrats, version figée, périmètre | PDF récupéré et lu par extraction texte; v1.6 du 25 mars 2026 |
| [PC SOFT, licence pilote OLE DB HFSQL](https://doc.pcsoft.fr/?1410087273) | Accès d'applications non WINDEV et redistribution encadrée | Page officielle récupérée par HTTP et lue; outil web d'ouverture retournait 403 |
| [SPDX, spécifications](https://spdx.dev/use/specifications/) | Nomenclature de dépendances proposée | Référence officielle à consulter pour l'implémentation; pas une certification juridique |
| [Règlement (UE) 2016/679](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32016R0679) | Corpus, données et sous-traitance | Référence primaire du cadre; obligations à décliner selon le traitement réel |

Aucun manuel, PDF contractuel complet, code PC SOFT ou binaire propriétaire n'est redistribué dans ce dépôt. Les résumés sont originaux; les sources externes restent accessibles auprès de leur éditeur.
