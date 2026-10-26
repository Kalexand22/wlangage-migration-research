# Propriété intellectuelle, interopérabilité et licences

Date de recherche : **26 octobre 2026**. Objet : définir une méthode de développement indépendante et les vérifications qui conditionnent les chemins techniques. Ce chapitre explique les textes et propose une organisation; il ne tranche pas les droits attachés à un contrat client non fourni.

## 1. Trois droits à distinguer dès le départ

Le projet doit séparer : **les sources métier de l'utilisateur**, **l'implémentation de PC SOFT** et **les dépendances redistribuées**. Posséder les sources d'une application ne donne pas automatiquement le droit de copier le compilateur, les DLL, la documentation, les images, les modèles ou les composants d'un tiers. À l'inverse, l'existence de droits sur le compilateur ne suffit pas à interdire toute implémentation indépendante d'un langage.

L'inventaire juridique accompagne donc l'inventaire technique : auteur/titulaire, contrat ou licence, version, provenance, acte envisagé, destinataires, pays et preuve conservée. L'import d'un projet autorisé, l'observation d'un comportement, la copie d'une DLL dans un produit et la mise en ligne d'un exemple sont quatre actes différents. Ils ne reçoivent pas une autorisation unique par analogie.

## 2. Cadre européen et français pertinent

La [directive 2009/24/CE, article 1](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32009L0024) protège l'expression des programmes, tout en distinguant idées et principes, notamment ceux des interfaces. Ses articles 5 et 6 encadrent respectivement certains actes d'utilisation/observation et les actes indispensables à l'interopérabilité. Les conditions ne permettent pas de copier librement un produit concurrent.

En France, [l'article L122-6-1 du CPI](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044365559) distingue l'observation ou le test réalisés lors d'opérations que l'on a le droit d'effectuer, et la reproduction/traduction de code indispensable à l'interopérabilité. Pour cette dernière voie, il faut notamment un utilisateur habilité, une information qui n'était pas déjà facilement accessible et une intervention limitée au nécessaire. L'utilisation et la communication des informations obtenues sont elles-mêmes encadrées. Le texte prévoit aussi la nullité de certaines stipulations contraires aux exceptions qu'il vise. Une restriction contractuelle ne se lit donc pas sans le droit applicable.

Dans [SAS Institute / World Programming, C-406/10, arrêt du 2 mai 2012](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:62010CJ0406), la CJUE distingue les fonctionnalités, le langage et certains formats de données de l'expression protégée du programme. Elle examine aussi l'observation par un licencié et le risque de reproduction d'éléments originaux du manuel. **Conséquence proposée pour ce projet** : fonder une implémentation indépendante sur des spécifications fonctionnelles et des tests originaux, en évitant la copie de code ou de documentation. L'arrêt ne constitue pas un feu vert général pour chaque méthode, interface graphique, licence ou territoire.

Il faut faire examiner par un juriste spécialisé les opérations sensibles effectivement envisagées, avec les contrats et faits précis. Les questions sont ciblées : qui est habilité à exécuter l'oracle, quel format manque, quelle information est publique, quel composant sera distribué et dans quels pays? Une étude de documentation publique et une implémentation originale peuvent avancer pendant la constitution de ce dossier; elles ne nécessitent pas une suspension générale du travail.

## 3. Ce qui a été vérifié chez PC SOFT et ce qui reste inconnu

Les [CGV publiées par PC SOFT](https://pcsoft.fr/pcsoft/conditions-generales-de-vente.htm), lien présent sur le site officiel, servaient lors de la consultation un PDF intitulé version 1.6 du 25 mars 2026. Elles renvoient au contrat de licence et au bon de commande. Les articles 4.9 et 6.6 décrivent un maintien d'une version figée sous conditions liées à la clé, à son activation/actualisation et au périmètre contractuel. Il serait donc inexact d'affirmer ici que toute fin d'abonnement enlève systématiquement tout droit d'usage. Leur applicabilité à une commande historique particulière n'est pas établie par la seule publication actuelle.

Une [licence spécifique du pilote OLE DB HFSQL](https://doc.pcsoft.fr/?1410087273) a aussi été consultée. Elle envisage des applications non WINDEV et une redistribution de fichiers désignés et de leur framework, avec conditions. Cela fournit une piste d'accès documentée; cela ne valide pas automatiquement un IDE concurrent ni tous les usages des autres pilotes.

Les documents contractuels de l'utilisateur, les licences exactes des moteurs/SDK choisis, les commandes, avenants, éditions et éventuels contrats particuliers ne sont pas disponibles dans cette étude. Les termes commerciaux actuels ou anciens ne doivent donc pas être déduits d'un forum ou d'une brochure. Pour chaque pilote, conserver la version du contrat applicable et son empreinte. Aucune affirmation globale « librement redistribuable » ou « sans redevance » ne doit être inscrite dans le produit avant cette vérification.

## 4. Matrice des chemins techniques et des contrôles associés

| Acte envisagé | Chemin de départ recommandé | Preuve à obtenir / point de vigilance |
| --- | --- | --- |
| Importer les sources métier | Copie ou export effectué par leur titulaire ou un mandataire habilité | Droits sur le projet, code salarié/prestataire et composants embarqués; confidentialité |
| Convertir un ancien projet | Utiliser la version de l'éditeur disponible légalement et la voie officielle | Licence utilisateur, versions autorisées, impact irréversible d'une conversion; conserver l'original |
| Lire le format texte hybride | Analyser les fichiers fournis, documenter sa propre représentation | Ne pas confondre lisibilité texte et spécification complète; provenance des exemples |
| Explorer un format natif opaque | D'abord rechercher documentation, export, SDK ou information accessible | Nécessité et proportionnalité d'une analyse supplémentaire; examen juridique ciblé avant décompilation |
| Reproduire la sémantique WLangage | Spécification originale et tests de comportement sur environnement autorisé | Conditions d'exécution de l'oracle; absence de copie du moteur, des tables ou des exemples propriétaires |
| Conserver HFSQL | Pilote/API officiellement documenté ou service applicatif légalement opéré | Contrat du serveur, pilote, framework et application; usage/redistribution distincts |
| Distribuer un pont WINDEV | Service séparé développé et distribué sous droits vérifiés | Périmètre de la licence, dépendance résiduelle, tarification éventuelle, maintenance |
| Remplacer HFSQL | Export logique autorisé puis adaptateur indépendant | Droits d'accès aux données; absence de contournement du chiffrement ou des permissions |
| Réutiliser une DLL/composant tiers | Chargement via interface publiée, dans environnement autorisé | Licence de déploiement, architecture, redistribution, maintenance et composants transitifs |
| Reproduire un workflow IDE | Conserver concepts utiles et terminologie métier | Création graphique propre, marques, signes distinctifs et absence d'apparence trompeuse |
| Fournir une aide de compatibilité | Documentation originale, citations brèves et liens | Pas de miroir non autorisé du manuel; droit sur illustrations, exemples et traductions |
| Publier un corpus de tests | Microprogrammes originaux et données synthétiques | Pas de code client confidentiel, secrets, datasets ou exemples propriétaires sans droits |

Un pilote disposant de sa propre licence ne confère pas cette licence à tous les futurs utilisateurs du produit. Le fonctionnement via service distant n'efface pas davantage les conditions du logiciel exécuté par ce service.

## 5. Organisation d'un développement indépendant

La méthode proposée de séparation des travaux, souvent appelée *clean room*, est un moyen de traçabilité; ce n'est pas une immunité juridique automatique.

1. **Registre des informations** : URL ou document, date, auteur, licence, statut public/confidentiel, version et personne ayant collecté l'information. Référencer les pages; ne pas les republier intégralement.
2. **Spécifications fonctionnelles originales** : valeurs d'entrée, sorties observables, états, événements, erreurs et variantes. Éviter la reprise du texte du manuel; les identifiants nécessaires à l'interopérabilité sont distingués de la rédaction explicative.
3. **Tests originaux** : écrire de petits programmes qui isolent un comportement. L'oracle exécute ces programmes dans le cadre des droits établis. Exporter valeurs et traces nécessaires, pas les binaires internes de PC SOFT.
4. **Implémentation traçable** : rattacher chaque changement au contrat fonctionnel et aux tests. Consigner les auteurs et origines des contributions. Écarter les soumissions contenant du code ou des assets dont la provenance n'est pas démontrée.
5. **Séparation renforcée si nécessaire** : pour une analyse sensible de format, faire produire une spécification minimale par une équipe d'analyse autorisée, puis une implémentation indépendante par une autre équipe selon un protocole validé.
6. **Revue avant diffusion** : contrôler code, dépendances, documents, marques et corpus de tests; joindre les notices et obligations des composants réellement livrés.

Les spécifications peuvent décrire qu'une fonction retourne une valeur précise et déclenche tel événement. Elles ne doivent pas contenir une traduction déguisée du code du moteur. Les journaux de recherche servent à démontrer cette distinction et à corriger une contamination si elle apparaît.

## 6. Expérience familière, identité propre

Le besoin de ne pas perdre les développeurs se traduit par des concepts reconnaissables : projet, analyse, fenêtre, champ, événement, état, procédure, débogueur, aperçu et génération. Le nouveau produit peut proposer une configuration de raccourcis et un lexique de correspondance. Il doit adopter son propre nom, ses icônes, visuels, modèles et textes.

Ne pas copier les logos, captures de ruban, gabarits ou bibliothèques d'images PC SOFT comme assets distribués. Les références à WINDEV/WLangage/HFSQL doivent rester descriptives et ne pas suggérer un produit officiel, un partenariat ou une certification. Une formulation telle que « environnement indépendant destiné à exécuter des sources WLangage selon les profils de compatibilité publiés » est plus précise qu'un nom de produit reprenant la marque. Faire vérifier les règles de marque et les communications prévues dans les territoires de diffusion.

Le droit sur l'apparence d'une interface ne se résume pas au droit du logiciel. L'arrêt SAS ne règle pas toutes les questions de marques, dessins, concurrence déloyale ou parasitisme. L'équipe UX doit donc travailler à partir des tâches et comportements recherchés, puis produire une interface originale, testée avec les développeurs concernés.

## 7. Dépendances, licences du nouveau produit et distribution

Le dépôt de recherche ne choisit pas à lui seul le modèle économique ou la licence du futur compilateur. Séparer les décisions pour le frontend langage, le runtime distribué avec les applications, l'IDE, les SDK d'extensions, le catalogue et la documentation. Une bibliothèque copyleft forte, une licence permissive et un composant commercial ont des implications différentes selon lien, modification et distribution.

Exiger une nomenclature de composants, version verrouillée, auteur, licence, empreinte, notice et modalité de distribution. Le format [SPDX](https://spdx.dev/use/specifications/) fournit une référence primaire pour structurer ces informations. Une SBOM décrit les composants; elle n'accorde aucun droit supplémentaire et ne remplace pas leur lecture juridique.

Pour .NET/WinForms et les autres bibliothèques pressenties, vérifier les fichiers LICENSE et THIRD-PARTY-NOTICES de **la version réellement embarquée**, les dépendances natives et les packs de distribution. Pour Avalonia, distinguer le cœur et les éventuels services/outils commerciaux. Pour Qt, si cette option revient dans les arbitrages, distinguer les modules, licences libres et offre commerciale; ne pas supposer qu'un choix de toolkit règle tout le produit.

Les polices, moteurs PDF, codecs, cartographie, connecteurs Office, cryptographie, pilotes matériels et composants mobiles méritent chacun une ligne. Les droits sur un code-barres ou un standard documentaire ne garantissent pas que la bibliothèque retenue soit redistribuable selon le modèle voulu. Les stores, certificats, SDK Apple/Android et contrats de signature appartiennent également au dossier de livraison.

## 8. Données clients et corpus de certification

La compatibilité nécessite souvent des données représentatives, mais le code source peut déjà contenir des identifiants, clés ou informations personnelles. Fournir un scanner local de secrets et un inventaire des fichiers avant tout transfert au support. Préférer des reproductions minimales et des données synthétiques; l'anonymisation doit être vérifiée, pas présumée par retrait des noms.

Si des données personnelles sont traitées, déterminer finalité, rôles, base légale, durée, hébergement, accès, sous-traitants et transferts. Le [RGPD, notamment articles 5, 25, 28 et 32](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32016R0679), donne le cadre primaire pertinent. Les logs différentiels et captures d'écran sont inclus dans ce périmètre. Une architecture exécutant les tests localement chez le client peut limiter les transferts; elle n'élimine pas les obligations de sécurité.

Ne pas utiliser les projets clients pour entraîner un assistant ou enrichir publiquement les tests sans droits et engagements adaptés. Les suggestions par IA doivent avoir une origine et une politique de données explicites; elles ne constituent pas une méthode de blanchiment d'un code propriétaire.

## 9. Dossier à clôturer avant chaque diffusion

Le responsable de livraison doit pouvoir relier chaque artefact à son droit d'usage et de distribution : sources originales, tests, modèles, bibliothèques, DLL et documentation. Les inconnus doivent devenir une restriction explicite du paquet ou être résolus avant qu'il contienne le composant concerné.

Questions concrètes à faire traiter : la voie d'export est-elle autorisée pour la version du pilote? L'observation est-elle réalisée par une personne habilitée? Le pilote HFSQL peut-il accompagner ce type de produit? Les fichiers redistribués sont-ils exactement ceux couverts par la licence applicable? Le corpus contient-il des données ou du code tiers? Le nouveau nom et les visuels prêtent-ils à confusion? Les obligations de chaque dépendance sont-elles remplies?

Le choix architectural de minimiser les composants propriétaires réembarqués réduit les dépendances contractuelles. Il n'autorise pas à ignorer celles qui subsistent. La décision juridique doit se fonder sur les actes et contrats réels, pas sur une conclusion générale « compatible donc permis » ou « propriétaire donc impossible ».

## Sources primaires consultées

| Source | Usage dans ce chapitre | État de consultation |
| --- | --- | --- |
| [Directive 2009/24/CE](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32009L0024) | Expression, observation, interopérabilité | Texte/extraits officiels indexés; ouverture web parfois soumise à contrôle JavaScript |
| [CPI, article L122-6-1](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044365559) | Conditions françaises | Version officielle indexée, en vigueur depuis le 26 novembre 2021 dans la page consultée |
| [CJUE, C-406/10, ECLI:EU:C:2012:259](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:62010CJ0406) | Fonctionnalités/langage/formats et manuel | Arrêt et résumé officiels; pas seulement conclusions de l'avocat général |
| [PC SOFT, CGV](https://pcsoft.fr/pcsoft/conditions-generales-de-vente.htm) | Contrats, version figée, périmètre | PDF récupéré et lu par extraction texte; v1.6 du 25 mars 2026 |
| [PC SOFT, licence pilote OLE DB HFSQL](https://doc.pcsoft.fr/?1410087273) | Accès d'applications non WINDEV et redistribution encadrée | Page officielle récupérée par HTTP et lue; outil web d'ouverture retournait 403 |
| [SPDX, spécifications](https://spdx.dev/use/specifications/) | Nomenclature de dépendances proposée | Référence officielle à consulter pour l'implémentation; pas une certification juridique |
| [Règlement (UE) 2016/679](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32016R0679) | Corpus, données et sous-traitance | Référence primaire du cadre; obligations à décliner selon le traitement réel |

Aucun manuel, PDF contractuel complet, code PC SOFT ou binaire propriétaire n'est redistribué dans ce dépôt. Les résumés sont originaux; les sources externes restent accessibles auprès de leur éditeur.
