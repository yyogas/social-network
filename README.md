# Social Network

Plateforme sociale internationale en phase **Fondation / M0**. La société porteuse est basée en France. Le premier public envisagé est la communauté kabyle et sa diaspora ; l'ouverture à d'autres publics est un objectif du produit.

## État vérifié

- Le mandat de direction et le registre HQ sont dans [`docs/00-hq/registry.md`](docs/00-hq/registry.md).
- Le MVP, la date de lancement, le budget et l'architecture détaillée restent à arbitrer.
- Ce dépôt initial contient de la gouvernance et des emplacements de travail. Il ne contient pas encore d'application, de service, de test exécuté ou de release.

## Repères

| Chemin | Rôle |
| --- | --- |
| `docs/00-hq/` | Registre MASTER et état du programme |
| `docs/decisions/` | Décisions transversales et ADR approuvés |
| `docs/product/` | Recherche, périmètre, parcours et critères d'acceptation |
| `docs/architecture/` | Domaines, contrats et cartes de dépendances |
| `docs/trust-safety/` | Politiques et outils de modération |
| `docs/privacy/` | Traitements de données et exigences de confidentialité |
| `docs/delivery/` | Jalons, qualité, exploitation et releases |
| `docs/teams/` | Mandats et propriétaires des équipes |
| `apps/`, `services/`, `packages/`, `infra/`, `tests/` | Emplacements réservés au code validé et à ses tests |

## Fonctionnement

Commencer par [`docs/00-hq/PROJECT-STATUS.md`](docs/00-hq/PROJECT-STATUS.md), puis consulter [`docs/GOVERNANCE.md`](docs/GOVERNANCE.md). Les discussions spécialisées proposent ; MASTER arbitre les choix transversaux et publie les décisions. Une proposition n'est pas une spécification approuvée.

Ne pas ajouter de secrets, de données personnelles réelles ou de exports de conversation bruts dans ce dépôt. La visibilité GitHub et les accès doivent être déterminés avant la publication.
