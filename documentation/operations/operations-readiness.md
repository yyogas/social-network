# Exploitation et préparation à la production

Date : 29 septembre 2026. Propriétaires : 14 DevOps/SRE, 18 QA, 20 Code Source. Statut : exigences et procédures à préciser avant déploiement applicatif. Aucun environnement de production n'est créé.

## Mise à jour et rollback

Chaque release doit référencer un commit, un artefact reproductible, ses versions de dépendances, les migrations et les incompatibilités. Avant mise à jour : sauvegarde vérifiée, espace libre, dépendances saines et critères d'arrêt explicites. Appliquer d'abord en staging ; vérifier les permissions et le parcours critique ; surveiller erreurs, latence et saturation après déploiement. La suppression d'une migration destructive n'est pas un rollback. Le propriétaire des données doit documenter sauvegarde/restauration, compatibilité et éventuelle migration corrective.

## Sauvegarde et restauration

Définir données couvertes, RPO/RTO, fréquence, rétention, chiffrement, détenteur des clés et emplacement indépendant du système primaire. Séparer PostgreSQL, médias et configuration ; les réplicas ne remplacent pas les sauvegardes. Prévoir une restauration isolée avec données synthétiques ou traitement de données autorisé, contrôle d'intégrité, vérification des droits, preuve horodatée et temps mesuré. Aucune copie de production ni clé ne doit être ajoutée au dépôt ou aux artefacts CI.

## Supervision et incidents

Health/readiness, erreurs, latence p95/p99, saturation CPU/RAM/disque, connexions DB, temps des requêtes, profondeur et âge des jobs, taux d'upload échoué, sauvegardes et certificats. Logs structurés avec identifiant de corrélation et suppression des secrets/données non nécessaires. Chaque alerte doit avoir un propriétaire et un runbook. Les incidents sérieux nécessitent chronologie, impact, mitigation, cause, correctif et non-régression.

## Conditions de déploiement

| Condition | État actuel |
| --- | --- |
| Versions OS/runtime et procédure vierge validées | BLOQUÉ |
| Critères produit et permissions testés | BLOQUÉ |
| Migration et retour arrière exécutés en staging | BLOQUÉ |
| Restauration exécutée et RPO/RTO mesurés | BLOQUÉ |
| Supervision et escalade testées | BLOQUÉ |
| Privacy et sécurité du traitement approuvées | BLOQUÉ |

Ces blocages concernent l'application future. Ils n'empêchent pas la rédaction des contrats M0.
