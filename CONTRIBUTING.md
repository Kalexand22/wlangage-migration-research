# Faire évoluer la recherche

1. Décrire la fonctionnalité ou l'écart avec un identifiant stable. Ajouter une ligne à `data/fonctionnalites.csv` pour une exigence nouvelle ; ne pas renuméroter les lignes existantes.
2. Séparer fait documenté, proposition de conception, résultat d'essai et inconnue. Citer une source primaire précise et sa version quand elle est connue. Une référence thématique ne prouve pas toutes les variantes d'une exigence.
3. Pour une preuve future de compatibilité, indiquer profil/version/build/options/cible, corpus, cas, oracle et résultats bruts. Un statut de recherche ne devient pas « implémenté » sans faire évoluer explicitement le périmètre du dépôt et ses contrôles.
4. Conserver dans le dénominateur les inconnus et échecs. Les exclusions et non-applicabilités sont justifiées par périmètre ; une fonction rare n'est pas supprimée pour améliorer un score.
5. Éviter de copier la documentation propriétaire, les exemples sous droits inconnus, les projets clients et les secrets. Conserver des liens, des métadonnées et des spécifications originales.
6. Mettre à jour les références et lancer les deux commandes ci-dessous avant un commit.

```bash
python3 tools/build_bibliography.py
python3 tools/assemble_report.py
python3 tools/update_metrics.py
python3 tools/check_repository.py
```

Ces commandes ne réalisent ni migration, ni comparaison avec WINDEV, ni vérification réseau de toutes les sources. Les pages PC SOFT peuvent évoluer ou avoir des URL équivalentes ; l'index bibliographique compte des URL distinctes, pas des documents indépendants.

Une demande de correction doit indiquer le chapitre ou l'identifiant, l'affirmation concernée, la source ou le cas contradictoire, et la correction proposée. Les revues conservées dans `data/revue-*.md` sont des notes datées de contrôle, pas une liste automatiquement à jour des écarts encore ouverts.

La phase actuelle est l’évaluation de faisabilité. Ne pas introduire de droits de publication, de dépendance PC SOFT redistribuée ou d’obligation générale d’avis préalable au code original à partir d’une simple recommandation documentaire. Les utilisations effectives de logiciels et les actes sensibles doivent être distingués et qualifiés.
