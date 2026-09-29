# Social Network

Plateforme sociale internationale en phase **Fondation / M0**. La société porteuse est basée en France. Le premier public envisagé est la communauté kabyle et sa diaspora ; l'ouverture à d'autres publics est un objectif du produit.

## État vérifié

- Le mandat de direction et le registre HQ sont dans [`documentation/project-governance/decision-register.md`](documentation/project-governance/decision-register.md).
- Le MVP, la date de lancement, le budget et l'architecture détaillée restent à arbitrer.
- Ce dépôt initial contient de la gouvernance et des emplacements de travail. Il ne contient pas encore d'application, de service, de test fonctionnel applicatif exécuté ou de release.

## Repères

| Chemin | Rôle |
| --- | --- |
| `documentation/project-governance/` | Registre MASTER et état du programme |
| `documentation/decisions/` | Décisions transversales et ADR approuvés |
| `documentation/product/` | Recherche, périmètre, parcours et critères d'acceptation |
| `documentation/architecture/` | Domaines, contrats et cartes de dépendances |
| `documentation/trust-safety/` | Politiques et outils de modération |
| `documentation/privacy/` | Traitements de données et exigences de confidentialité |
| `documentation/delivery/` | Jalons, qualité, exploitation et releases |
| `documentation/teams/` | Mandats et propriétaires des équipes |
| `applications/`, `services/`, `shared-packages/`, `infrastructure/`, `tests/` | Emplacements réservés au code validé et à ses tests |

## Fonctionnement

Commencer par [`documentation/project-governance/project-status.md`](documentation/project-governance/project-status.md), puis consulter [`documentation/governance.md`](documentation/governance.md). Les discussions spécialisées proposent ; MASTER arbitre les choix transversaux et publie les décisions. Une proposition n'est pas une spécification approuvée.

Ne pas ajouter de secrets, de données personnelles réelles ou de exports de conversation bruts dans ce dépôt. Le dépôt est privé ; les accès supplémentaires sont soumis à validation.

## Développement vérifiable

- [Contribuer et faire revoir un changement](CONTRIBUTING.md)
- [Organisation et convention de nommage](documentation/repository-conventions.md)
- [Installation : état réel et prérequis](documentation/installation/installation-guide.md)
- [Tests et validation](documentation/quality/test-strategy.md)
- [Rapport des vérifications exécutées](documentation/quality/validation-report.md)
- [Exploitation, sauvegardes et retour arrière](documentation/operations/operations-readiness.md)
- [Hébergement : pilote, intermédiaire et premium](documentation/hosting/hosting-comparison.md)

La CI actuelle vérifie le dépôt documentaire et les tests de son validateur. Les suites et l'installation applicatives restent à réaliser. Les protections de branche ne sont pas encore configurées.


## Construire le produit — campagne M0

- [Index canonique : propriétaires, versions, preuves et documents manquants](documentation/documentation-index.md)
- [Plan documentaire et couverture](documentation/documentation-plan.md)
- [Vision et principes produit](documentation/product/product-vision.md)
- [Catalogue des fonctionnalités proposées](documentation/product/feature-catalog.md)
- [Parcours et critères d'acceptation](documentation/product/user-journeys.md)
- [Mandats des 21 équipes](documentation/teams/work-orders.md)
- [Pilotage, questions et réception des livrables](documentation/project-governance/coordination-board.md)
- [Roadmap globale proposée](documentation/project-governance/global-roadmap.md)

La vision, le catalogue, les parcours et les mandats sont préparés par le HQ pour les revues spécialisées. L'index est une contribution de 17 — Documentation. Leur publication n'atteste pas de l'approbation des fonctionnalités ni de l'exécution des travaux par les autres discussions.
