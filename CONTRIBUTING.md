# Contribuer à Social Network

GitHub est la référence centrale des fichiers du projet. Lire le [statut](documentation/project-governance/project-status.md), la [gouvernance](documentation/governance.md) et les [conventions](documentation/repository-conventions.md) avant modification.

## Cycle de contribution

1. Identifier le besoin, son propriétaire, la décision ou demande de référence, les dépendances et les critères d'acceptation.
2. Vérifier l'état de `main`, puis créer une branche courte : `documentation/sujet`, `feature/sujet`, `fix/sujet` ou `infrastructure/sujet`.
3. Modifier les fichiers nécessaires, les tests pertinents et la documentation dans le même changement. Le code, les configurations modèles, migrations, scripts et procédures indispensables doivent être versionnés.
4. Exécuter les contrôles applicables. Conserver les commandes, résultats, environnement et commit testé. Ne pas assimiler un test prévu à un test exécuté.
5. Ouvrir une pull request avec objectifs, décisions, changements, vérifications, risques, dépendances et rollback. Le modèle est fourni par GitHub.
6. Faire revoir avant fusion : équipe propriétaire ; équipe 21 pour intégration/code ; avis 03 Architecture, 09 Safety, 14 Sécurité, 15 Privacy selon l'impact. MASTER arbitre les changements transversaux. Aucun auto-avis d'un auteur ne constitue une revue indépendante.
7. Fusionner seulement quand les critères applicables sont satisfaits. L'exigence de revue est une règle du projet ; son verrouillage technique par protection de branche est encore à configurer.

## Commits et travail partagé

Messages explicites, par exemple `docs: documenter la restauration PostgreSQL` ou `fix: contrôler la permission de modification du profil`. Décrire le résultat ; éviter « update » seul. Faire de petits changements cohérents et utiliser une change request pour modifier une décision officielle. Ne pas pousser de force sur une branche partagée. Résoudre les conflits en préservant les décisions et les travaux des autres équipes.

Les branches sont un mécanisme de revue, pas une architecture applicative. La réorganisation documentaire de M0 ne modifie pas la stack ni les frontières métier.

## Données et secrets

Ne pas versionner de credentials, clés privées, mots de passe réels, données personnelles ou sauvegardes de production. Les exemples contiennent des valeurs fictives. Utiliser des fixtures synthétiques pour les tests. Les secrets sont fournis par le mécanisme validé pour l'environnement ; `.gitignore` ne nettoie pas un secret déjà commité. En cas de fuite : révoquer/renouveler le secret, prévenir le propriétaire sécurité, traiter l'historique et consigner l'incident. Ne jamais recopier la valeur dans un ticket ou un journal.

## Commandes disponibles en M0

```sh
python3 scripts/repository/validate_repository.py
python3 -m unittest discover -s tests/repository -p 'test_*.py' -v
git diff --check
```

Ces commandes vérifient le dépôt documentaire et son validateur. Elles ne testent pas encore un réseau social en fonctionnement.
