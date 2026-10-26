# Revue contractuelle primaire — 26 octobre 2026

**Périmètre ferme retenu : cas A uniquement, chaîne 100 % indépendante.** Aucun logiciel, outil, DLL, runtime, SDK, pilote, serveur HFSQL ou pont PC SOFT ne participe à l'import, au build, à l'exécution ou aux tests. Le cas B d'observation active est exclu, même via un client ou un tiers; le cas C de réemploi est également exclu. La lecture et les liens de documentation publique sont permis, sans copie de code PC SOFT. Les seules entrées du client sont des fichiers, exports et traces **déjà existants**, assortis de leur provenance et des droits pertinents; aucune nouvelle exécution PC SOFT n'est commandée pour les produire.

Ce relevé conserve l'explication des clauses et jurisprudences examinées. Il ne transforme pas les cas historiques B/C en étapes actives et n'impose aucune notation M1 générique « critique » ou « moyenne » au prototype autonome. Aucun avis d'avocat n'a été obtenu; aucun avis général ne conditionne l'étude ou le code original. Le choix d'une licence de publication et la commercialisation restent différés. Voir [le chapitre juridique](../docs/09-propriete-intellectuelle-et-licences.md).

## Méthode et limites de la preuve

Les trois pages PC SOFT ont été récupérées directement en HTTPS le 26 octobre 2026, via `urllib.request` dans l'environnement autorisé; HTTP 200, sans modification de leur contenu ni contournement d'authentification. Le texte a été lu après retrait des balises de présentation et des scripts/styles. Les copies de travail étaient temporaires, hors du dépôt. Le dépôt contient les références, résumés originaux et trois extraits brefs; il ne contient pas les licences complètes ni des DLL.

Les empreintes ci-dessous portent sur **les octets de la réponse HTML reçue lors de cette consultation**. Elles identifient cette observation mais ne prouvent ni la version acceptée par un client ni un contenu immuable à l'URL; les pages peuvent intégrer des éléments variables. Les réponses originales ne sont pas redistribuées et une nouvelle requête peut donner une autre empreinte. Pour un dossier opposable, le conseil devra définir le mode de conservation adéquat des contrats effectivement conclus.

| Identifiant | Page officielle et URL consultée | Résultat / empreinte SHA-256 de la réponse |
| --- | --- | --- |
| CT-WD | [Licence WINDEV](https://doc.pcsoft.fr/fr-FR/?4510001=&name=License_WINDEV) | HTTP 200; `009de3ca16b9eace4313881291fb101b38e1c6be257eb2404423ea6822c3ff32` |
| CT-FW | [Licence Framework WINDEV](https://doc.windev.com/fr-FR/?1000019581=&name=licence_framework_windev) | HTTP 200; `145859d92f7e311a471289f5d7099ab6e195c5cc5f9dd50d3ce95470d0918e9f` |
| CT-OT | [Licence Outils](https://doc.windev.com/fr-FR/?4510003=&name=Licence_Outils) | HTTP 200; `e845f61631caffa8346453e225b879b7dd62a1024eb96f9ad14242c5f9a38798` |

## Constats vérifiés sur les licences — contexte historique hors cible

### CT-WD — restriction liée à l'utilisation de WINDEV

**Repère : article 4, utilisation.** Extrait de 10 mots : « Il est interdit d'utiliser ce LOGICIEL pour créer et diffuser ». La suite vise notamment des outils de développement, la création d'applications, des générateurs et des logiciels de nature comparable. La page contient aussi des restrictions sur la réutilisation du code Java généré, ainsi que sur des ressources graphiques.

**Constat complémentaire, article 5 :** diffusion des modules, code dynamique/MCU, HFSQL et États & Requêtes font l'objet de règles distinctes. Pour le cas de diffusion HFSQL décrit avec une application WINDEV, le seuil vise plus de 50 % des fonctionnalités réellement utilisées par des applications WINDEV/WEBDEV. Le texte expose également une licence par serveur avec condition de version pour d'autres usages et assimile une machine seule à un serveur. **Ce relevé n'en déduit aucune obligation universelle liée au seul fait d'employer un autre langage** : périmètre, usages réels et licences propres au moteur/pilote doivent être rapprochés. La licence OLE DB qui prévoit des applications non WINDEV est un autre texte pertinent; leur articulation n'est pas tranchée ici.

**Conséquence pour le périmètre retenu :** la clause vise l'utilisation du logiciel; son applicabilité n'est pas démontrée à notre chaîne C# originale qui n'utilise aucun logiciel/DLL PC SOFT. Les opérations d'observation et de réemploi dont traite la recherche ne sont pas retenues. La clause n'établit donc pas ici un préalable général au prototype; le relevé ne prononce pas davantage une nullité globale de la licence.

### CT-FW — restriction liée au framework

**Repère : article 3, utilisation.** Extrait de 10 mots : « Il est interdit d'utiliser ce FRAMEWORK pour créer et diffuser ». La suite vise également les outils de développement et logiciels comparables à WINDEV. Les définitions incluent les DLL du framework; cette page est distincte de la licence de l'IDE et des licences de pilotes.

**Statut : réemploi exclu.** Ces DLL ne sont ni embarquées, ni chargées, ni utilisées par un service de la chaîne. Aucun pont distant ou opérateur tiers ne remplace cette exclusion. La licence est conservée comme explication documentaire, pas comme voie technique à valider.

### CT-OT — périmètre de diffusion des outils

**Repère : article 2, diffusion.** Extrait de 9 mots : « avec des applications développées avec WINDEV ou WEBDEV 2025 ». La liste d'outils inclut notamment des utilitaires de données, de scripts, de déploiement et le centre de contrôle HFSQL. Dans le texte consulté, la restriction identique aux articles précités sur la création d'outils de développement n'a pas été trouvée. Il serait donc erroné de l'attribuer indistinctement à ces trois pages.

**Statut : outils exclus.** Aucun de ces outils n'est utilisé ou diffusé par la cible. La mention 2025 et les restrictions restent des faits documentaires; elles ne créent aucun besoin de licence d'outil pour notre implémentation autonome.

## Jurisprudence et observation — comparaison historique hors étapes actives

Les textes ci-dessous expliquent le droit d'observation et ses limites. **Aucune campagne d'observation PC SOFT, aucune décompilation et aucun oracle tiers n'en sont déduits pour le workflow retenu.** Les traces existantes éventuellement reçues restent des matériaux à provenance contrôlée.

| Référence primaire | Constat vérifié | Portée pour la faisabilité |
| --- | --- | --- |
| [Directive 2009/24/CE, art. 5 §3 et 9 §1](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32009L0024) et [CPI L122-6-1 III et dernier alinéa](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044365559) | Observation/étude/test protégés dans les conditions prévues; nullité des clauses contraires aux exceptions désignées | Fondement positif à l'observation sur copie licite; aucune autorisation préalable de PC SOFT présumée nécessaire lorsque l'acte relève effectivement de l'exception |
| [CJUE SAS / WPL, C-406/10](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:62010CJ0406), points 50–53 et 59–62 | Droit d'observation, nullité des clauses contraires et respect des droits exclusifs; fonctionnalités/langage/formats distingués de l'expression du programme | Une finalité concurrentielle ne permet pas de transformer automatiquement l'observation protégée en acte interdit; pas de jugement de la clause PC SOFT sur ce projet |
| [High Court, [2013] EWHC 69 (Ch), 25 janvier 2013](https://caselaw.nationalarchives.gov.uk/ewhc/ch/2013/69), points 61 et 64–79 | Application de l'exception à WPL et restrictions incompatibles écartées dans la mesure de leur contradiction; protection non perdue du seul fait de la finalité dépassant la licence | Appui concret à la voie B, distinct d'une déclaration de nullité universelle de toute clause concurrentielle |
| Même jugement, point 82 | La demande sur le manuel conserve un succès partiel | Refaire les fonctionnalités n'autorise pas la copie de l'expression protégée d'un manuel |
| [Fourth Circuit, 24 octobre 2017, nos 16-1808/16-1857](https://www.ca4.uscourts.gov/opinions/161808.P.pdf), notamment pp. 12–18 PDF | Responsabilité contractuelle confirmée selon le droit de Caroline du Nord; différence avec l'analyse européenne expressément discutée | Évaluer les territoires retenus avant commercialisation; ne pas projeter cette solution américaine sur le droit français |
| [Fourth Circuit, 12 mars 2020, nos 19-1290/19-1300](https://www.ca4.uscourts.gov/opinions/191290.P.pdf) | Injonctions liées à l'exécution du jugement américain | Pas de nouvelle décision invalidant le droit européen d'observation |
| Directive art. 6 et CPI IV, mêmes liens ci-dessus | Autre fondement pour reproduction/traduction de code indispensable à l'interopérabilité, sous conditions et limites de résultat | Ne pas assimiler une simple comparaison de sorties à la décompilation du compilateur |
| [CJUE Top System, C-13/20, 6 octobre 2021](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:62020CJ0013), points 53 et 57–74 | Décompilation nécessaire à la correction d'erreurs, fondement distinct de l'interopérabilité | Pas de transposition automatique à la création d'un compilateur indépendant |
| [Code civil 1190](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032041260/) et [1199](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032041378/) | Interprétation en cas de doute et effet relatif du contrat | Aident à déterminer sens et parties concernées; n'annulent pas indistinctement tous les contrats ou autres droits |

**Méthode complémentaire, 26 octobre 2026 :** le jugement britannique a été ouvert et lu sur les archives judiciaires officielles *Find Case Law*, notamment points 61, 64–79 et 82. Les arrêts américains ont été ouverts en PDF sur le site officiel du Fourth Circuit; dates et objets ont été vérifiés dans les décisions elles-mêmes. Les articles du Code civil proviennent de Légifrance. La CJUE a été lue via les extraits officiels indexés; les passages 50–62 sont également reproduits dans le jugement britannique officiel. Certaines ouvertures EUR-Lex imposaient un contrôle JavaScript. Aucun article de presse ou commentaire doctrinal n'établit les conclusions de ce relevé.

## Statut final des scénarios étudiés

| Scénario | Statut final | Conséquence pratique |
| --- | --- | --- |
| **A** : compilateur C#/runtime/outillage originaux, provenance autonome, aucun logiciel PC SOFT | **Seul retenu** | Étude, code et tests originaux peuvent avancer; pas de préalable contractuel générique lié à l'utilisation de logiciels absents de la chaîne |
| **B** : observation/comparaison active sur WINDEV ou autre logiciel PC SOFT | **Exclu des étapes actives** | Pas d'oracle lancé par l'équipe, un client ou un prestataire; pas de nouvelle production de traces ou d'exports demandée dans ces logiciels |
| **C** : runtime, pont, outils, SDK, serveur/pilote HFSQL ou redistribution PC SOFT | **Exclu** | Pas de maintien de moteur, chargement de DLL ou service distant PC SOFT; explications de licences hors cible |

Les qualifications de risque des anciens scénarios A/B/C ne sont pas reportées automatiquement au prototype autonome. L'applicabilité de la clause visant l'utilisation du logiciel couvert n'est pas démontrée à une chaîne qui n'en utilise aucun. Cela ne décide pas de tous les droits sur les formats, documents, sources et ressources reçus.

## Provenance et points ouverts dans la voie indépendante

- **Contributeurs :** aucun critère général imposant de n'avoir jamais détenu une licence n'est retenu. Documenter l'origine des contributions et les engagements effectivement pertinents; ne pas copier du code ou des assets PC SOFT.
- **Entrées client :** fichiers, exports et traces déjà disponibles, avec droits et provenance. L'équipe ne commande pas au client une opération WINDEV pour enrichir ces entrées.
- **Documentation publique :** lecture, liens et spécifications rédigées de façon originale; aucune copie de code PC SOFT dans l'implémentation.
- **Preuve fonctionnelle :** attendus documentaires, traces historiques et hypothèses sont distingués. Sans oracle actif, un comportement non suffisamment documenté reste inconnu; il ne reçoit pas une certification d'équivalence fictive.
- **Dépendances :** inventaire vérifiant absence de logiciel PC SOFT dans import, build, runtime et tests; import de projet sans exécution automatique des références binaires qu'il contient.
- **Questions ultérieures :** droits propres aux matériaux, formats, confidentialité et signes distinctifs; revue spécialisée recommandée avant commercialisation éventuelle ou sur une opération sensible précisément identifiée. La licence de publication demeure indécise et n'est pas une condition de l'étude.

**État : périmètre indépendant défini, aucune validation juridique universelle revendiquée.** L'étude et l'écriture du code original ne sont pas suspendues à un avis général, à une licence PC SOFT ou à une décision de publication. Les clauses et décisions historiques documentées ci-dessus restent utiles pour expliquer les distinctions, sans réintroduire l'observation ou le réemploi exclus.
