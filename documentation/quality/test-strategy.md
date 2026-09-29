# Stratégie de validation

Date : 29 septembre 2026. Propriétaires : 18 QA, 20 Code Source, 21 Intégration. Statut : exigences du porteur de projet intégrées ; suites applicatives à construire au fil des fonctionnalités.

## Traçabilité par fonctionnalité

Chaque fiche doit relier besoin et critères d'acceptation à des tests nommés. Statuts : `PLANNED` (décrit), `READY` (exécutable), `RUNNING`, `PASS`, `FAIL`, `BLOCKED`. Pour une exécution : SHA, environnement, versions, commandes, horodatage, résultat et liens vers logs expurgés. `PASS` concerne une exécution et un périmètre précis ; ne pas le généraliser à toute la plateforme.

| Type | Risque couvert | Quand |
| --- | --- | --- |
| Unitaire | Règles, validation et gestion d'erreurs | Logique métier et correctifs |
| Intégration | Transactions, DB, jobs et interactions | Frontières de modules |
| API / permissions | Authentification, autorisation, payloads invalides | Toute opération exposée |
| End-to-end | Parcours utilisateur et erreurs visibles | Parcours critiques |
| Réseau / concurrence | Connexion lente, retries, doublons, course | Fonctions concernées |
| Charge | Débit, latence, saturation, coût | Avant promesse de capacité |
| Sécurité / privacy | Abus et traitement des données | Selon revue des propriétaires |

Chaque bug corrigé doit recevoir une non-régression pertinente ; documenter un cas manuel si un test automatisé n'est pas techniquement approprié. Couvrir les comptes suspendus, les droits insuffisants et l'isolation des données, pas seulement le happy path.

## CI actuellement livrée

Le workflow `repository-quality.yml` s'exécute sur pull request et push vers `main`. Il contrôle le dépôt et exécute les tests de son validateur, avec permissions `contents: read`, délai limité et checkout fixé à un SHA. Il ne déploie rien et ne reçoit pas de secret du projet.

Les suites applicatives et tests de charge sont `BLOCKED` par l'absence d'implémentation. Le workflow documentaire ne les simule pas. L'installation du produit sur un OS vierge reste également `BLOCKED`. Les règles de protection de branche devront imposer revue et checks lorsqu'elles seront configurées ; la présence d'un workflow seul ne les rend pas obligatoires.
