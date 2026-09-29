# Message commun à transmettre aux discussions 01–21

FROM : 00 — MASTER / DIRECTION / HQ
TO : Équipe spécialisée de cette discussion
PHASE : Fondation / M0
STATUT : travail documentaire autorisé dans ton domaine ; décisions structurantes à soumettre au MASTER.

Commence maintenant un livrable concret. Lis la PR de coordination sur la branche `documentation/m0-team-coordination` du dépôt `yyogas/social-network` : sa proposition documentaire dépend de la PR nº 1, non réputée fusionnée. Ne te limite pas à la branche main si ces PR sont encore ouvertes.

1. Lis `documentation/teams/work-orders.md` et prends le mandat M0-TEAM correspondant au numéro et au rôle de ta discussion. Si ton rôle n'est pas identifiable, demande-le sans inventer une attribution.
2. Consulte `documentation/documentation-plan.md`, les trois documents de `documentation/product/` (vision, catalogue, parcours) et `documentation/project-governance/coordination-board.md` seulement pour le contexte utile. Vérifie les décisions et les fichiers existants avant de créer des doublons.
3. Produis le livrable de ton mandat avec `documentation/teams/deliverable-template.md`. Détaille les grandes lignes de ton domaine, les fonctionnalités concernées, les règles, erreurs, permissions, données, dépendances et critères d'acceptation. Classe chaque idée en MVP, Phase 2, Phase 3, International ou Long terme, avec statut PROPOSÉ tant qu'elle n'est pas approuvée.
4. Démarre avec les informations disponibles. Marque les inconnues et formule des questions ciblées ; une dépendance absente ne bloque que la section concernée. Réutilise ton travail existant s'il est traçable, en produisant un delta plutôt qu'une réanalyse générale.
5. Soumets au HQ toute proposition modifiant fortement architecture, stack, sécurité, données personnelles, permissions, business model ou roadmap. Aucun code applicatif sans spécification et contrats suffisamment validés pour le lot concerné.
6. Publie par branche et PR si ton accès GitHub le permet, sans écraser les branches de coordination ni fusionner ton propre travail sans revue. Référence les PR dont tu dépends. Sinon fournis le contenu exact, le chemin cible et le statut RESTE À PUBLIER ; ne prétends pas avoir créé un commit ou une PR.
7. Termine par : décisions prises / à valider ; livrables et références GitHub ; tests exécutés et résultats (ou non exécutés avec raison) ; questions ouvertes ; dépendances ; risques et limites ; prochaines étapes et informations HQ. Retourne les références au MASTER pour consolidation.

Un document préparé par HQ est une entrée de travail, pas l'avis approuvé de ton équipe. Ne présente pas une discussion voisine comme informée, active ou ayant validé quelque chose sans preuve de transmission ou de réponse.
