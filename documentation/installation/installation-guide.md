# Installation et validation — état M0

Date : 29 septembre 2026. Propriétaires : 14 DevOps, 20 Code Source, 18 QA. **Statut : procédure du dépôt documentaire disponible ; installation de l'application BLOQUÉE par l'absence d'application et de contrats approuvés.**

## Ce qui peut être installé aujourd'hui

Un checkout du dépôt et ses contrôles Python. Prérequis de ces seuls contrôles : Git, Python 3.10 ou supérieur avec la bibliothèque standard, système de fichiers sensible à la casse recommandé. Pas de dépendance Python tierce. Le workflow utilise un runner `ubuntu-24.04` ; ce choix ne valide pas un OS de production du futur produit. Pour un poste documentaire, réserver provisoirement 1 CPU, 1 Go de RAM et 1 Go disque libre ; ces chiffres sont une estimation, pas un minimum applicatif mesuré.

### Depuis un poste disposant de Git et Python

1. Obtenir un accès autorisé au dépôt privé et authentifier Git par le mécanisme de l'organisation. Ne pas placer un token dans la commande ou l'URL.
2. Télécharger les sources :

```sh
git clone https://github.com/yyogas/social-network.git
cd social-network
git switch main
git rev-parse HEAD
python3 --version
python3 scripts/repository/validate_repository.py
python3 -m unittest discover -s tests/repository -p 'test_*.py' -v
```

Les contrôles de cette pull request ne seront présents sur `main` qu'après fusion. Avant fusion, utiliser la branche `docs/m0-engineering-foundation` et consigner le SHA testé. Les résultats attendus sont la réussite du validateur et des tests du validateur ; aucune API ou interface utilisateur ne doit être annoncée disponible.

### Périmètre de preuve

Un checkout/export propre des seuls fichiers versionnés permet de vérifier l'absence de dépendances implicites aux fichiers locaux. Ce contrôle ne constitue pas l'installation d'un OS vierge ni l'authentification Git d'un autre utilisateur. Les commandes et résultats réellement exécutés sont dans le [rapport de validation](../quality/validation-report.md).

## Contrat à compléter avant la première installation applicative

| Sujet | Livrable attendu | État / propriétaire |
| --- | --- | --- |
| OS et architecture CPU | Matrice OS/version/architecture supportée avec preuve | BLOQUÉ — 14/03 |
| Runtimes et dépendances | Versions exactes compatibles, manifestes et lockfiles | BLOQUÉ — 20/04/05/06 |
| Configuration | Variables, type, défaut, obligatoire, secret, mode de fourniture | BLOQUÉ — 14/20 |
| Base de données | Création, compte à droits minimaux, migrations et fixtures synthétiques | BLOQUÉ — 04/03 |
| Développement | Installation des dépendances, lancement, ports et arrêt | BLOQUÉ — 20 |
| Production | Build reproductible, artefacts, déploiement, TLS, health checks | BLOQUÉ — 14 |
| Vérification | Parcours, permissions et tests après installation | BLOQUÉ — 18 |
| Exploitation | Mise à jour, sauvegarde/restauration et rollback vérifiés | BLOQUÉ — 14/18 |

Les mandats mentionnent Next.js/React/TypeScript, NestJS, Flutter/Dart, Python et PostgreSQL. Cela ne suffit pas à établir leurs versions compatibles ni à fournir des commandes exécutables d'installation du produit. Le fichier [exemple d'environnement](../../configuration/examples/.env.example) reste un exemple documentaire sans variable runtime validée.

## Dépannage des contrôles actuels

- Python absent ou trop ancien : installer une version compatible depuis la source officielle adaptée au poste et vérifier `python3 --version`.
- Accès GitHub refusé : faire vérifier les droits du compte et l'authentification par le propriétaire ; ne pas partager de secrets dans un ticket.
- Lien local introuvable : corriger la cible ou le chemin après renommage ; consulter l'erreur du validateur.
- Fichier interdit détecté : retirer la donnée du changement et prévenir Sécurité si elle a déjà été partagée. Une suppression du fichier seul ne révoque pas un credential.
