# Plan de documentation et couverture M0

Date : 29 septembre 2026. Propriétaire : 17 — Documentation. Coordination : 00 — MASTER. Statut : **PROPOSÉ — travail documentaire autorisé, contenu métier à faire revoir**.

La documentation doit permettre à une personne extérieure aux conversations de comprendre le produit, contribuer, vérifier une fonctionnalité puis exploiter le service. Une page créée n'est pas une spécification approuvée. GitHub conserve les références, les deltas, les avis et les preuves ; une discussion sert à produire ou expliquer ces éléments.

## Ordre de lecture

1. Lire le [README du dépôt](../README.md), la [gouvernance](governance.md) et les [conventions](repository-conventions.md).
2. Vérifier le [registre des décisions](project-governance/decision-register.md) et l'[état du projet](project-governance/project-status.md).
3. Lire la [vision produit](product/product-vision.md), le [catalogue fonctionnel](product/feature-catalog.md) et les [parcours](product/user-journeys.md). Leurs propositions ne constituent pas un MVP approuvé.
4. Consulter les [ordres de travail des équipes](teams/work-orders.md), puis les spécifications de domaine utiles au changement.
5. Relier la spécification aux critères de la [stratégie de tests](quality/test-strategy.md), aux contrats applicables et aux preuves de validation.
6. Pour installer ou exploiter, partir du [guide d'installation](installation/installation-guide.md), de la [préparation à l'exploitation](operations/operations-readiness.md) et du [comparatif d'hébergement](hosting/hosting-comparison.md). Leurs limites actuelles doivent rester visibles.

## Hiérarchie et responsabilité

- `project-governance/` et `decisions/` : décisions, périmètres approuvés, priorités, risques et arbitrages transversaux ; propriétaire 00 avec avis des domaines concernés.
- `product/` : besoins, catalogue, parcours et critères métier ; propriétaire 01 avec 02, 09, 15, 16 et 19.
- Les spécifications de domaine : un propriétaire explicite et les interfaces qui les relient aux autres domaines. Les nouveaux dossiers apparaissent quand un livrable réel les justifie.
- `quality/` : stratégie, cas et preuves de validation ; propriétaire 18, avec 20 et 21 pour le code et l'intégration.
- `installation/`, `operations/`, `hosting/` et `delivery/` : procédures reproductibles, exploitation, estimations et livraison ; propriétaires 14, 17, 18, 20 et 21 selon le contenu.
- `teams/` : responsabilités, ordres de travail et format des échanges ; 00 coordonne, 17 maintient la lisibilité et les liens.

L'[index canonique](documentation-index.md) est fourni par 17 comme contribution spécialisée v0.1 proposée, avec références de révision, propriétaires, lacunes et preuves. Ce plan décrit la couverture et le travail restant, sans se substituer à cet index. La spécification `documentation/product/mvp-specification.md` est attendue de 01 ; les documents produit de cadrage préparés au HQ alimentent sa rédaction sans la remplacer. Ce dernier chemin reste une cible absente de la référence examinée par l'index. La présence de l'index dans une PR ne prouve ni réception HQ ni approbation métier.

17 ne choisit pas la stack, les permissions ou les durées de conservation à la place de leurs propriétaires. Chaque équipe entretient son contenu ; 17 vérifie sa structure, son intégration et sa traçabilité.

## Matrice de couverture

« Présent » désigne un fichier du dossier de travail, pas une approbation ni une présence sur `main`. Les références GitHub et SHA du compte rendu de publication déterminent ce qui a réellement été publié. Les trois documents produit sont des propositions de cadrage préparées dans ce lot, pas des livrables attribués à une discussion spécialisée qui n'aurait pas répondu.

| Domaine | Couverture présente | Complément attendu avant l'implémentation concernée | Propriétaire et interfaces |
| --- | --- | --- | --- |
| Gouvernance | Registre, statut, conventions et contribution | Décisions MVP, responsables de revue et résolution des contradictions | 00 ; 17, 20, 21 |
| Produit | Vision, catalogue et parcours proposés dans ce lot | Priorisation, exclusions, critères mesurables, scénarios d'erreur | 01 ; 02, 09, 15, 19 |
| UX et accessibilité | Parcours de principe ; aucun Design System validé | Navigation, écrans/états, formulaires, accessibilité, responsive | 02 ; 01, 05, 06, 16 |
| Architecture | README de mandat | Frontières, options comparées, ADR, dépendances, défaillances | 03 ; 04–08, 10, 13, 14, 20 |
| Backend et contrats | Attentes d'architecture ; pas de contrat approuvé | Requêtes/réponses, autorisation, erreurs, idempotence, versions | 04 ; 03, 05, 06, 08, 10, 18 |
| Données | Attentes privacy ; aucun modèle approuvé | Entités, contraintes, transactions, migrations, cycle de vie | 04 pour modèle applicatif ; 03, 13, 15 |
| Web et mobile | Mandats dans la liste d'équipes | Périmètre des clients, états réseau, sessions, compatibilité et contrats consommés | 05, 06 ; 02, 04, 14, 18 |
| IA et médias | Équipes identifiées ; pas de chaîne de traitement validée | Utilité et exclusions de l'IA, traitement des images, limites vidéo, coûts et abus | 07, 08 ; 03, 09, 14, 15 |
| Sécurité | Règles GitHub/secrets et contrôle documentaire limité | Menaces, authentification, sessions, permissions, accès internes, incidents | 14 ; 03, 04, 09, 10, 15, 18 |
| Privacy | README de mandat | Données/finalités, visibilité, rétention, suppression/export, pays et âge ; analyse datée | 15 ; 01, 04, 13, 14, 16 |
| Modération et support | README Trust & Safety | Blocage, signalement, décisions, recours, rôles support, accès et capacité humaine | 09, 10 ; 01, 14, 15, 18 |
| Infrastructure et hébergement | Comparatif estimatif et préparation à l'exploitation | Option retenue, budget, réseau, sauvegardes, secrets, reprise et supervision | 14 ; 03, 08, 13, 18 |
| Installation et livraison | Guide de préparation ; procédures applicatives bloquées | Versions/OS, commandes vérifiées, configuration, migrations, upgrade et rollback | 14, 20 ; 17, 18, 21 |
| QA et intégration | Stratégie, validateur du dépôt et rapport de contrôles | Tests métier/API/E2E, permissions, non-régression, charge et restauration | 18, 21 ; tous propriétaires concernés |
| Publicité et créateurs | Mandats identifiés ; aucun modèle économique approuvé | Options, transparence, consentement applicable, fraude, revenus et coûts | 11, 12 ; 00, 01, 13, 15 |
| Mesure et lancement | Mandats identifiés | Objectifs pilote, métriques minimales, événements et recrutement des premiers utilisateurs | 13, 19 ; 01, 09, 15, 16 |
| Internationalisation | Ambition et pays initiaux identifiés | Langues/écritures, formats, traduction, modération et déploiement par pays | 16 ; 02, 05, 06, 09, 15, 19 |

Cette matrice ne doit pas devenir une déclaration de conformité générale : chaque ligne progresse avec des références de livrables et des preuves. Une fonctionnalité reportée peut se limiter à son objectif, sa phase, ses dépendances et la raison du report.

## Fiche et traçabilité communes

Utiliser le [modèle de livrable](teams/deliverable-template.md). Réutiliser les identifiants du catalogue ; ne pas créer une deuxième numérotation pour la même fonctionnalité. Les formats `REQ-XXXX`, `FEAT-NNN` (par exemple `FEAT-001`) et `TEST-XXXX` sont proposés pour les nouveaux éléments sans identifiant existant ; 00 et 17 arbitrent les collisions avant intégration. Conserver les formats de décisions, risques et demandes existants.

La chaîne attendue est : besoin → fonctionnalité/parcours → décision applicable → contrat/données/permissions → critères d'acceptation → tests → implémentation → revue → preuve. Toute case absente est marquée avec son propriétaire et son effet réel sur la suite ; elle n'est pas masquée par « à compléter » sans explication.

## Revue et progression sans boucle inutile

1. **Cadrage M0** : recueillir les premiers livrables, faire apparaître les options et les dépendances. Une proposition peut avancer avec des hypothèses explicites.
2. **Avant l'implémentation d'un lot** : approuver son périmètre et les décisions structurantes qui le concernent. Définir suffisamment ses états, erreurs, données, permissions, contrats et critères de test. Une question critique non tranchée bloque ce lot ; une question indépendante n'immobilise pas tout le projet.
3. **Pendant l'implémentation** : modifier code et documentation dans la même PR lorsque possible ; sinon relier les PR dépendantes. Faire examiner le delta par les propriétaires affectés et effectuer la revue avant fusion.
4. **Avant le pilote** : exécuter les validations nécessaires, installation comprise, et disposer des procédures de sauvegarde, restauration, incident et retour arrière. Les tests non exécutés restent explicitement non exécutés.

Un avis favorable porte sur une révision identifiée. Il ne s'étend pas automatiquement aux changements suivants. Il n'est pas nécessaire de refaire une revue complète quand un petit delta n'affecte pas les conclusions précédentes.

## Maintenance des documents et conflits

Chaque transmission précise les chemins et SHA de référence, le delta à examiner, les décisions attendues et les destinataires. Ne pas demander à une équipe de relire une archive entière ni de recommencer toutes ses analyses pour une modification ciblée, sauf demande explicite ou justification de dépendance fournie au HQ.

Une nouvelle proposition ne remplace jamais silencieusement une référence approuvée. En cas de contradiction, enregistrer les deux références, l'impact, le propriétaire de l'arbitrage et les travaux réellement bloqués. Préserver l'ancienne référence jusqu'à une décision explicite et relier la décision qui la remplace.

Une transmission à une discussion existante reste **À TRANSMETTRE** tant que son envoi n'est pas établi, puis **ENVOYÉ** et **REÇU** sur preuve. Un agent parallèle ou un document préparé au HQ n'est pas, à lui seul, une réponse de cette discussion.
