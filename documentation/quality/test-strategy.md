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

## Complément spécialisé M0 — 18 QA (v0.1, PROPOSÉ)

Mandat M0-TEAM-18 ; base de rédaction `dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957`.
La [matrice d’acceptation](acceptance-test-matrix.md) relie les 31 critères Produit aux tests et décrit 17 cas transversaux supplémentaires. Cette section complète la stratégie ; approbation du périmètre et des règles métier demeure chez HQ et les propriétaires. Voir DEC-1801 proposée dans la matrice.

### Préparation, exécution et preuve

- Avant développement d’un lot : exigences et critères identifiés, hypothèses explicites, états/erreurs/permissions et contrats suffisamment définis. Une absence d’oracle critique bloque ce lot.
- Avant READY : test détaillé, fixture synthétique isolée, artefact/environnement/versions connus, oracle accepté, procédure automatisée ou manuelle reproductible et emplacement de preuve.
- PLANNED signifie cas conçu ; BLOCKED signifie prérequis d’exécution manquant. La matrice indique BLOCKED pour les 48 cas applicatifs à cette révision. RUNNING n’existe qu’après démarrage réel.
- PASS exige résultat conforme pour chaque sous-cas applicable ; FAIL exige écart observé. Une interruption d’infrastructure produit BLOCKED/échec de run distingué du défaut produit. Chaque nouveau run conserve l’ancien résultat.
- Un changement de code, contrat, permissions, migration, dépendance ou configuration déclenche une analyse d’impact. Les tests sensibles au delta sont rejoués. Une réutilisation de preuve non affectée exige justification et références exactes ; aucun PASS n’est copié automatiquement.

### Exécution proposée selon le risque

| Moment | Suites / responsabilité | Critère |
| --- | --- | --- |
| PR applicative future | 20 et propriétaires : unitaires, intégration, contrats, permissions touchées, non-régression ; 18 aide aux scénarios | Cas liés au delta et invariants critiques vérifiés |
| Staging / périodique | 18/05/06 : E2E étendus, UI, a11y, compatibilité, réseau, concurrence ; 14 : panne contrôlée | Données synthétiques, aucune perturbation de production |
| Candidat pilote | 18/14/21 et métier : P0, suites applicables, installation vierge, backup/restore, upgrade/rollback, charge selon objectifs reçus | Build/config identifiés, preuves révisées |
| Après déploiement autorisé | 14/18 : smoke synthétique, erreurs, latence, ACL et alertes ; owner opérationnel identifié | Poursuivre, stopper ou récupérer selon critères décidés |

Les outils applicatifs restent à choisir avec 20/14 et l’architecture retenue. Tests unitaires pour règles déterministes et validations ; intégration pour transactions/concurrence/jobs ; contrats/API pour consommateurs et permissions ; E2E pour parcours complets. Revue humaine nécessaire pour a11y, compréhension de visibilité et procédures de modération. Ni pourcentage de lignes couvertes ni nombre de tests ne garantit la sécurité.

### Gates du pilote à ratifier — DEC-1801 proposée

- Scope approuvé avec liste des FEAT, surfaces/locales, cas applicables et exclusions motivées, avant exécution du candidat. J07 conditionnel tant que FEAT-020 non tranchée.
- Tous les P0 applicables ont une preuve PASS valide sur l’artefact candidat et sa configuration ; aucun P0 ignoré, instable, FAIL ou BLOCKED. Une fonction retirée du pilote nécessite un arbitrage de scope et la vérification des chemins encore exposés.
- Aucun S0/S1 ouvert ; contrôle d’accès, confidentialité, sécurité des personnes, intégrité et capacité de récupération ne peuvent être contournés par un pourcentage global de réussite.
- P1/P2/P3 applicable : résultat ou non-exécution motivée. Toute exception indique impact, propriétaire, atténuation, expiration et tests de remplacement ; accord HQ et propriétaire concerné, plus 14/15/09 si leur domaine est touché.
- Installation vierge, restauration, changement de version et chemin de retour/récupération ont des preuves ; compatibilité client/API/DB explicitée. Un rollback applicatif ne prouve pas la réversibilité de la base.
- Profil pilote/SLO, limites de capacité, moyens humains de modération/support, alertes, runbooks, smoke et responsable d’arrêt sont documentés. Sans cible chiffrée approuvée, une mesure de charge ne prouve pas conformité.
- Rapport de release : version/commit/artefact/hash, configuration, migrations, scope, contrats, matrice de runs, anomalies/risques/exception, signataires et revue indépendante 21. QA recommande GO / GO WITH EXCEPTIONS / NO GO ; HQ désigne l’autorité finale.

### Arrêt et retour arrière à faire définir par 14 avec HQ

Un accès privé indu, corruption de données ou échec d’un parcours critique déclenche arrêt de progression et traitement d’incident selon runbook. Les seuils d’erreurs/latence et durées de surveillance restent à fixer à partir des SLO. 14 choisit avec propriétaires la désactivation ciblée, le retour de version compatible ou la restauration/réparation, en considérant les écritures intervenues depuis le déploiement. Après récupération : smoke, intégrité, permissions et non-résurrection de données supprimées avant reprise. Personne d’astreinte et limites du pilote doivent être connues avant ouverture.

### Bugs, régressions et instabilité

Registre à tenir dans les issues GitHub une fois l’anomalie observée : ID, FEAT/AC/TEST, version et environnement, données fictives, étapes, attendu/observé, fréquence, preuves expurgées, sévérité, priorité, owner et liens correction/non-régression. Aucune anomalie applicative n’est créée sur la seule hypothèse d’un risque.

| Sévérité proposée | Définition | Effet |
| --- | --- | --- |
| S0 critique | Prise de contrôle, fuite massive ou perte irréversible | Bloque ; circuit incident/sécurité |
| S1 majeure | Accès privé indu même circonscrit, parcours cœur ou protection essentielle indisponible, intégrité compromise sans contournement sûr | Bloque |
| S2 significative | Défaut circonscrit sans impact critique, contournement vérifié | Exception explicite ou correction |
| S3 mineure | Gêne limitée sans impact sur droits/intégrité/parcours critique | Planification suivie |

Cycle : NEW → TRIAGED → IN_PROGRESS → FIX_READY → VERIFY → CLOSED ; REOPENED si échec. Sévérité décrit l’impact ; priorité ordonne le travail. Correction accompagnée de test de non-régression pertinent, automatisé ou manuel justifié, qui vérifie le comportement corrigé et pas seulement le code ajouté.

Test instable : garder l’échec initial et sa fréquence, ouvrir une anomalie, attribuer owner/échéance ; un retry vert seul n’efface pas le risque. Mise en quarantaine explicite avec couverture de remplacement ; aucun cas P0 instable ne devient PASS par exclusion silencieuse. Suivre défauts échappés, réouvertures, couverture de risques, stabilité CI et disponibilité des preuves, sans quotas artificiels.

Les contrôles documentaires du présent delta sont consignés dans le [rapport QA M0](qa-m0-validation.md). Cette stratégie est une proposition de gates ; une CI verte demeure limitée à ce qu’elle exécute.
