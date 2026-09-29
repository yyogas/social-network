# Organisation et nommage

Date : 29 septembre 2026. Responsable : 20 — Code Source, avec 17 Documentation et 21 Intégration. Statut : règles demandées par le porteur du projet ; application proposée dans cette pull request.

| Dossier | Responsabilité | Propriétaires |
| --- | --- | --- |
| `applications/` | Interfaces web, mobile et administration, lorsqu'implémentées | 05, 06, 10, 20 |
| `services/` | Backend et traitements indépendants effectivement retenus | 03, 04, 07, 08, 13, 20 |
| `shared-packages/` | Contrats ou composants réellement partagés | 03, 20 |
| `tests/` | Tests transversaux, intégration, parcours et contrôles du dépôt | 18, 20, 21 |
| `documentation/` | Spécifications, décisions, guides et preuves | 17 et propriétaires de domaine |
| `scripts/` | Outils de développement, validation et exploitation | 14, 20 |
| `configuration/` | Exemples de configuration sans secrets | 14, 20 |
| `infrastructure/` | Déploiement et infrastructure versionnés après validation | 14 |
| `.github/` | Workflows et modèles reconnus par GitHub | 14, 20, 21 |

## Convention unique

Chemins en anglais, explicites et en `lower-kebab-case`, sans accents ni espaces. Fichiers documentaires en `.md`. Une responsabilité par dossier important, décrite dans un `README.md` ou l'index ci-dessus. Créer un dossier lorsque son contenu est nécessaire ; éviter les arborescences vides couvrant toutes les ambitions futures.

Exceptions : noms imposés par un outil (`README.md`, `CONTRIBUTING.md`, `.gitignore`, `.github`, futurs manifestes), scripts/tests Python en `snake_case.py` conformément au langage, conventions générées par les frameworks quand ceux-ci seront retenus. Documenter toute nouvelle exception. Aucun nom comme `divers`, `misc`, `new`, `final2` ou `temp` ne décrit suffisamment une responsabilité.

Git conserve l'historique : préférer `installation-guide.md` à une suite de copies `installation-final-v3.md`. Les IDs stables de décisions et tests sont conservés. Les versions de contrats, migrations et releases suivent leurs règles spécifiques ; ne pas les renommer comme de simples fichiers rédactionnels.

## Migration des chemins M0

| Ancien | Nouveau |
| --- | --- |
| `apps/` | `applications/` |
| `docs/` | `documentation/` |
| `infra/` | `infrastructure/` |
| `packages/` | `shared-packages/` |
| `docs/00-hq/registry.md` | `documentation/project-governance/decision-register.md` |
| `docs/00-hq/PROJECT-STATUS.md` | `documentation/project-governance/project-status.md` |

Les mentions de cette table sont historiques. Les liens actifs et les contrôles CI doivent utiliser les nouveaux chemins. Aucun script de déploiement applicatif n'existe actuellement à migrer. Rollback : revenir sur le commit de réorganisation après vérification des contributions ultérieures ; ne pas écraser les nouveaux fichiers d'autres équipes.
