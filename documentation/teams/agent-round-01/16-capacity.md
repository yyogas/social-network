# Agent 16 — Capacité, concurrence et anti-abus L1

**Avis documentaire indépendant, proposé, sans adoption ni benchmark.** Base : Backend #28 v0.3, SHA `0a7fcd54b996cc292bfe98c61a835613837def32`, convergence C3–C6 ; `documentation/hosting/hosting-comparison.md`, `documentation/quality/test-strategy.md`, `documentation/security/security-operations-requirements.md` ; avis locaux `10-data-model.md` et `11-devops.md`. Aucun code, test applicatif ou changement distant exécuté. Cet avis ne représente aucune discussion propriétaire.

## Paramètres à ratifier

Architecture/Backend/Sécurité doivent distinguer attente d’admission, calcul du hash, attente de verrou, section L→commit et réponse réseau. Un timeout client ne borne pas automatiquement le travail serveur. Produit/Web/QA fixent ensuite les objectifs de parcours compatibles avec ces bornes.

- **Hash hors verrou :** si password retenu, choisir fonction et paramètres après mesure CPU/mémoire sur l’environnement candidat ; borner taille d’entrée, nombre de calculs simultanés et file d’attente avant travail coûteux. Vérifier E à L après le hash ; aucun résultat calculé avant reset ne suffit à autoriser. Aucun appel réseau sous protection transactionnelle.
- **L→commit :** ratifier ordre des verrous, attente maximale, budget transactionnel, traitement des deadlocks et politique d’abandon. Mesurer séparément attente et durée protégée. L après attente revalide temps/droits/R/T/F/E ; protections conservées jusqu’au commit durable. Une échéance franchie après L n’interdit actuellement pas tout commit : l’oracle dépend du budget ratifié. L’échec ou l’incertitude du commit interdit un succès présumé.
- **Files :** fixer plafonds d’admission, connexions DB, hash concurrents, workers, profondeur et âge maximal des jobs. Définir rejet, expiration, drainage et équité entre opérations. Séparer capacité des tâches différables et disponibilité des parcours critiques ; une queue durable ne garantit pas leur délai. L’indisponibilité d’autorité conserve le refus fermé prévu.
- **Retries :** ratifier le budget candidat C6, sans transformer ses valeurs en SLO. Inclure réseau, attente et `Retry-After` dans la borne globale ; conserver tuple exact, scope et vue valides. Aucun login automatique, K neuf ou retry infini. Compter aussi reprises serveur/DB/jobs pour éviter l’amplification multiplicative ; distinguer tentative, opération logique et effet durable.
- **Rate limits :** quotas combinés par route/ressource, contexte et compte autorisé ; IP comme signal complémentaire. Borner bootstrap, recovery, renvois et replays. Définir comportement si compteur indisponible, quotas globaux et réponse de saturation, sans priorité révélant l’existence du compte. Mesurer faux refus sur IP partagées et accessibilité.
- **Timing :** ratifier modèle d’attaquant, chemins à comparer et seuil de distinction acceptable. Réponse neutre et hash factice éventuel doivent être évalués sous charge ; un délai artificiel seul ne prouve pas l’absence de canal auxiliaire et peut consommer la capacité.

## Objectifs mesurables proposés

Définir, pour chaque parcours et profil approuvés, bornes p95/p99 de latence, taux d’erreur technique, attente de verrou, âge des files, ressources et amplification des retries. Séparer refus métier, anti-abus et panne. Objectifs invariants : aucun double effet durable ni accès interdit ; saturation avec ressources bornées ; retour à un régime stable après rafale. Chaque cible nécessite valeur, fenêtre, charge, propriétaire et règle d’arrêt avant conformité ; aucune valeur arbitraire ajoutée ici.

## Protocole futur et limites

QA/14 figent SHA, configuration, ressources et données synthétiques. Exécuter nominal, montée progressive, palier, rafale puis récupération, avec profils d’authentification et de contention distincts du mix social. Forcer reset pendant hash, expiration pendant verrou, deux logins R/T, replay concurrent et réponse perdue après commit. L’oracle continuation/logout demeure conditionnel selon l’avis 10. Injecter lenteur DB, panne d’autorité et saturation des files ; vérifier invariants et arrêt des retries. Comparer statistiquement distributions temporelles existant/inexistant et secret invalide, avec échantillonnage/pouvoir de détection préétablis. Conserver mesures et traces expurgées ; rattacher aux TEST-1413/1414/1419. Exécution actuellement BLOCKED.

Population inscrite, sessions simultanées, coût du hash, distribution des accès, contention, médias, données, restauration, disponibilité et travail humain restent différents facteurs. Les scénarios hébergement sont des charges à tester ; sans implémentation, topologie ratifiée, mesures reproductibles et budget complet actualisé, promettre « X utilisateurs pour tel coût » serait infondé.
