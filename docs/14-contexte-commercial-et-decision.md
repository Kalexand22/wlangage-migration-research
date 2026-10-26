# Contexte commercial 2026 et choix de trajectoire

Date : **26 octobre 2026**. Ce chapitre constitue un cadre de décision avec scénarios génériques. Aucun devis client, contrat accepté, parc déployé ou prix négocié n'a été fourni. Il ne conclut donc ni à une économie garantie ni à une urgence universelle de sortie. Le propriétaire a précisé que la phase actuelle porte sur la faisabilité: ces scénarios restent un contexte ultérieur, sans imposer maintenant un choix de commercialisation ou de licence de publication.

## 1. Pourquoi examiner une alternative maintenant ?

Volaris a annoncé l'acquisition de PC SOFT le **26 mai 2025**. Cette source établit la date de communication; elle ne suffit pas à établir la date juridique exacte d'une prise de contrôle antérieure ou tous ses véhicules sociétaires. [Communiqué de l'acquéreur](https://www.volarisgroup.com/press-room/volaris-group-acquires-pc-soft/).

PC SOFT présente publiquement un mécanisme de sessions lié aux applications et aux accès aux bases de données. L'unité décrite associe application, machine, compte du système d'exploitation et type de base; elle ne se réduit donc pas à un nombre de personnes. Les conditions d'un contrat donné et les exemptions restent à vérifier. [Page officielle Sessions](https://windev.com/fr/sessions).

Une page officielle datée du **1er octobre 2026** présente un plan de continuité destiné aux entreprises de moins de dix salariés : deux ans sur WINDEV Suite 2025, jusqu'à fin 2028, commande avant fin 2026, avec un prix affiché de **2 290 € par an**. La communication du compte officiel évoque également l'absence de Sessions pour les clients éligibles. Ce prix de suite ne doit pas être comparé directement à une ancienne mise à jour ou à un abonnement d'un autre périmètre. [Plan de continuité](https://windev.com/fr/news/wdnews-off-plan-de-continuite), [communication officielle PC SOFT](https://www.linkedin.com/company/pc-soft/).

Ces évolutions justifient un examen des coûts, droits d'usage, dépendances et possibilités de reconstruction. Elles ne démontrent pas que chaque organisation doit migrer ni que conserver une version existante est toujours possible. Les CGV, commandes, contrats et mesures de continuité applicables doivent être rapprochés du cas réel. [Analyse juridique](09-propriete-intellectuelle-et-licences.md).

## 2. Ce qui est connu, supposé ou manquant

| Élément | État de preuve dans ce dossier | Conséquence |
| --- | --- | --- |
| Acquisition annoncée le 26 mai 2025 | Source primaire de l'acquéreur lue | Contexte établi; date de réalisation juridique distincte |
| Existence publique du dispositif Sessions | Présentation officielle lue en HTTP public | Relever les unités facturables et règles du contrat |
| Plan de continuité et prix de suite ci-dessus | Page officielle lue; observation datée | Vérifier éligibilité, périmètre, durée et devis |
| Tarif universel actuel de 290 ou 225 € par session | Chiffres fournis par la relecture; pas de grille actuelle établissant ici leur application générale | Ne pas les utiliser comme prix confirmé du client |
| Anciens prix 1 068/749 € et hausse dérivée | Périmètre et date non rapprochés d'un contrat dans cette étude | Comparer des offres équivalentes avant calcul |
| Date du 21 septembre pour l'annonce initiale du plan | Fournie par la relecture; la page officielle examinée porte une date d'octobre | Ne pas confondre publication consultée et première annonce |
| Exposition financière du propriétaire du dépôt | Parc, contrats et devis absents | Modèle symbolique; aucun ROI calculé pour son entreprise |
| Issues de contentieux commerciaux particuliers | Aucune décision judiciaire primaire examinée ici | Ne pas les transformer en règle générale ou en argument de vente |

Le [relevé des observations commerciales](../data/observations-commerciales-2026.json) conserve URL, date, statut HTTP et empreinte des pages publiques examinées. Il n'archive pas les corps de pages et ne certifie pas les droits d'un client. Une demande de devis est proposée sur le site officiel; aucun formulaire n'a été soumis par cette recherche. [Contact commercial](https://windev.com/fr/contact?ask=quote).

## 3. Pour qui, et qui finance ?

| Scénario générique | Objectif à confirmer | Payeur et périmètre à identifier | Preuve de valeur à obtenir |
| --- | --- | --- | --- |
| Éditeur d'un progiciel WINDEV déployé chez plusieurs clients | Conserver ses règles métier et maîtriser le coût marginal de déploiement | Éditeur, client final ou partage contractuel; applications, machines, comptes et moteurs | Coût contractuel du parc, coût de migration et possibilité de maintenir les sources |
| DSI avec applications internes | Assurer continuité, sécurité et reconstruction sur la durée | DSI et métiers; parc réel, SLA et contraintes de données | Exercice de reconstruction/restauration, qualité métier et coût total |
| Petite structure éventuellement éligible à un plan de continuité | Sécuriser un horizon court et préparer une décision soutenable | Structure titulaire; conditions du plan et capacité d'investissement | Délai utile obtenu, coût ferme et trajectoire à la fin du plan |

Ces personas ne décrivent pas des clients acquis. Le sponsor, le propriétaire des données, le référent WINDEV et le décideur budgétaire sont à nommer pour chaque pilote. Le financement d'une plateforme générale et le financement de la migration d'une seule application ne sont pas le même investissement.

## 4. Trois décisions distinctes

1. **Continuité immédiate :** conserver, stabiliser ou geler un périmètre lorsque les droits, la sécurité et les conditions économiques le permettent. Réévaluer l'horizon contractuel; ne pas présumer une perte systématique d'accès à toute fin d'abonnement.
2. **Compatibilité des sources :** faire exécuter le WLangage par une implémentation indépendante. Le langage reste une compétence et un patrimoine; les dépendances au compilateur, framework, pilotes et serveurs PC SOFT ne disparaissent que si elles sont effectivement remplacées et leurs contrats clôturés.
3. **Sortie des composants et du langage :** réécrire ou adapter vers une pile cible, éventuellement assistée par IA, et migrer les données si nécessaire. Cette voie accepte de changer la source maintenue et a son propre coût de preuve, de formation et de reprise de l'interface.

Le besoin initial de ce dépôt privilégie la deuxième décision : maintenir le code WLangage. Il serait incorrect de remplacer ce besoin par une réécriture sans le dire. Il serait tout aussi incorrect d'annoncer qu'une simple conservation du langage ou un passage à PostgreSQL garantit la sortie de toute tarification et obligation existante. Le critère est la chaîne réellement utilisée : génération, runtime, pilotes, serveur et exploitation. [Comparaison des voies](01-options-et-solutions-existantes.md), [profils de données](04-donnees-integrations-et-cibles.md).

## 5. Modèle économique à remplir

Pour chaque période, calculer les unités facturables selon le contrat applicable, puis appliquer les prix, packs, minima, exemptions et remises effectivement acceptés. Le comptage technique d'un parc aide à préparer cette vérification, sans se substituer au contrat.

```text
Coût actuel annuel = IDE et abonnements
                   + Σ(unités facturables par catégorie × prix contractuel)
                   + serveurs/pilotes/support/infrastructure applicables

TCO de la trajectoire sur H années
    = audit + développement/migration + qualification + formation
      + coexistence et bascule + exploitation et maintenance sur H
      + coûts résiduels PC SOFT + autres dépendances
      + scénarios de risque explicitement décrits

Écart de TCO(H) = TCO de continuité(H) − TCO de la trajectoire(H)
```

Un prix absent reste une variable, pas zéro. Une dépense passée irrécupérable ne devient pas une économie future. Les gains de productivité, réductions de risque et économies de licence ne doivent pas compter deux fois le même bénéfice. Le scénario de construction de plateforme du chapitre 07 ne constitue pas le coût d'une réécriture client.

Construire trois scénarios : continuité contractuelle favorable, scénario central fondé sur devis, évolution défavorable explicitement hypothétique. Faire varier le parc, l'effort de reprise et la durée de coexistence. Si l'éditeur renégocie ses conditions, le cas doit être recalculé : le résultat ne doit pas dépendre d'une hypothèse unique de hausse perpétuelle.

## 6. Positionnement face à la réécriture assistée

Une plateforme compatible vise à réduire les modifications de code et l'apprentissage requis. Une offre de réécriture vise la maintenance d'un nouveau code et l'adoption d'une autre pile. Les deux doivent démontrer la reprise des règles métier, données et documents; une extraction par IA ne constitue pas cette preuve à elle seule.

Le chapitre 01 recense des déclarations de prestataires et un playbook public, sans valider leurs taux de conversion, durées ou prix. Il faut comparer les approches sur le même corpus et le même contrat de sortie : sources livrées, dépendances restantes, construction hors service du fournisseur, preuves de non-régression et coûts récurrents. La différenciation du projet est une hypothèse de conservation vérifiable du code, pas l'affirmation qu'aucune alternative ne peut exister.

## 7. Décision avant industrialisation

Dans la phase actuelle, construire un prototype original sans aucun logiciel PC SOFT, à partir des entrées déjà fournies et de cas synthétiques. L’audit des contrats et du parc pourra documenter une décision d’exploitation ultérieure ; il n’est pas un préalable général au code autonome. La décision d'investir exige quatre réponses : quel code doit rester inchangé; quels composants doivent être remplacés; qui paie quel coût sur quel horizon; quelles preuves rendent la bascule acceptable.

Un changement de conditions commerciales peut modifier la priorité de migration. Les avantages durables d'une chaîne reconstructible, de formats documentés et d'une traçabilité métier peuvent toutefois rester pertinents. Leur valeur doit être discutée avec les utilisateurs, puis mesurée; elle n'est pas déduite d'une polémique ou d'un seul prix public.


## 8. Contrainte technique finale

La cible exclut les composants, outils, pilotes et serveurs PC SOFT à toutes les étapes, ainsi que l’exécution d’un oracle par un client ou un prestataire dans notre protocole. Les scénarios de continuité évoqués ici décrivent le contexte du marché, sans constituer des options de mise en œuvre de la solution. PostgreSQL et un adaptateur H* original sont la voie proposée ; les limites des entrées opaques et des références disponibles sont explicites dans le [chapitre 15](15-perimetre-independant-et-preuve-de-faisabilite.md). Aucun prix ni aucune licence de publication ne doit être décidé pour commencer cette preuve de faisabilité.
