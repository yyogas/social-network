# État du projet

## État courant — coordination déléguée, 30 septembre 2026

Sur instruction du porteur (DIR-013), le HQ a lancé vingt missions de sous-agents, avec six simultanées au maximum. Le [dossier de ronde 01](../teams/agent-round-01/README.md) centralise leurs avis, sources, corrections et cinq actions suivantes. Ces nouveaux exécutants ne sont pas les auteurs des vingt-et-une discussions spécialisées ; aucune transmission à ces conversations n’est supposée. Le porteur peut donner ses instructions ici, sans relayer manuellement cette ronde.

Backend PR 28 est relu à v0.3 `0a7fcd54b996cc292bfe98c61a835613837def32`, Architecture PR 33 à `a7901fc87e79975d8963e909a89fc8150410e40a`. Les avis propriétaires PR 29–32 portaient sur v0.2. La revue croisée a corrigé une clôture QA trop large : continuation F/T puis logout reste ouverte. Le choix de reprise A/continuité ordinaire et la portée entre racines restent non adoptés. **L1 demeure BLOQUÉ POUR CODE.** La prochaine pièce attendue est un delta contractuel consommable, pas une nouvelle campagne générale.

Publication documentaire sur la PR 27 ; [preuves et limites](../quality/agent-round-01-validation.md). DIR-012 reste applicable au positionnement universel ; MVP, pays ouverts, langues, stack, permissions et budget restent à arbitrer. Les sections suivantes conservent les états antérieurs à cette ronde.

## Préparation des arbitrages — 30 septembre 2026

Le [dossier d’arbitrage pilote/MVP](m0-mvp-arbitration.md) prépare trois choix HQ : public/admission, suivi ou communautés, surface/langues. **DIR-012 confirme le public universel et les priorités marketing sur instruction du porteur du 30 septembre 2026** ; le périmètre pilote, la stack, les données et les permissions restent à arbitrer. Les recommandations par défaut France/français sont retirées pour réexamen dans ce cadre mondial. Base relue : `main` à `ba26729aa10dc497338a960ae78ba904a72216b2`, 26 PR fusionnées et aucune ouverte avant cette nouvelle proposition ; [preuves finales #24](https://github.com/yyogas/social-network/pull/24). Les demandes ciblées restent À TRANSMETTRE.

## État courant — consolidation documentaire v0.2

Complément factuel de 21, 29 septembre 2026. Phase **Fondation / M0**. Les 21 réponses spécialisées #3–23 sont reçues et **intégrées dans main** au SHA `8b2e75da39d9d4ceadbefc71690e233939fb9515` ; le bilan HQ est #24. Les CI PR et push ont été vérifiées pour chacune. La fusion documentaire conserve leurs statuts PROPOSÉ. Les fondations #26/#25/#1/#2 sont intégrées dans `main` au SHA `71d7fd16be174381b7d937182979cdf7225cecb9`. Le [bilan de réception](m0-reception-report.md) et l'[état d'intégration](../quality/m0-branch-integration-status.md) consignent la progression suivante et ses preuves exactes.

**Prochaine action HQ : arbitrer les propositions reçues**, en commençant par public/pays/langues/âge et MVP, puis contrats, architecture, permissions, données, capacité et budget. L'intégration documentaire garde les statuts PROPOSÉ et les critères applicatifs PLANNED/BLOCKED. Elle n'autorise ni lancement ni implémentation sur des contrats ouverts.

FIND-21-01/03/04 sont corrigés et vérifiés dans la fondation ; FIND-21-02 (protections/reviewers durables, HQ/14/20) et FIND-21-05 (maintenance checkout, 14/20) restent ouverts. Aucun paramètre de protection ou visibilité modifié ; aucune branche supprimée. Les transmissions aux autres discussions restent À TRANSMETTRE.

## Archive — préparation et réception initiale DIR-009/010/011

Les états « collecter », « en revue », « à recevoir » et « corrections avant intégration » ci-dessous sont historiques. L'ancienne audience de départ est remplacée par DIR-012 ; sa mention dans cette archive ne porte aucune orientation active. Consulter l'état courant et les preuves de fusion, sans réattribuer les anciennes preuves à de nouveaux SHA.

**Date :** 29 septembre 2026
**Phase :** Fondation / M0
**Objectif :** constituer les preuves et contrats nécessaires pour décider le premier MVP.

## Confirmé

- Nom du projet : Social Network.
- Société basée en France ; première audience envisagée : communauté kabyle et diaspora.
- MASTER coordonne les équipes 01 à 21 ; les décisions structurantes lui sont remontées.
- M0 a été ouvert par `DIR-008` dans le registre HQ.
- Structure de dépôt et premier commit local `14c215e` créés par `DIR-009` ; dépôt GitHub privé `yyogas/social-network` créé et accès en écriture vérifié.

## Proposé

- Parcours pilote : profil, personnes suivies ou communautés, texte/image, fil chronologique, interactions, visibilité, blocage et signalement, modération et recours.
- Les frontières et l'ordre des phases restent soumis aux propriétaires et à MASTER.

## En attente de preuve ou d'arbitrage

- Public et pays pilotes (`DEC-0001` à créer après examen des réponses).
- Contrat MVP (`DEC-0002` à créer après examen des réponses).
- Budget, capacité, calendrier, langues, politiques de modération, exigences privacy, architecture et contrats.
- État de tout code, test et déploiement éventuellement produits ailleurs.

## Prochaine action

Collecter les livrables M0 des équipes 01 Produit, 09 Trust & Safety, 15 Privacy, puis 02 Design, 03 Architecture, 18 QA, 20 Code Source et 21 Intégration. Les demandes préparées `INT-0001` à `INT-0010` figurent dans le registre HQ ; leur inscription ne prouve pas leur envoi ni leur réception.

## Référence versionnée

Dépôt : https://github.com/yyogas/social-network — visibilité privée. Remote local : `origin`. L’import initial passe par les API GitHub ; les commits de préparation locaux ne sont pas des références de release.

## Travail DIR-010 en revue

Organisation et noms explicites, règles de contribution, CI du dépôt, tests du validateur, documentation d'installation/exploitation et scénarios d'hébergement : préparés dans la branche `docs/m0-engineering-foundation`. Suivre la PR pour statut de revue et résultat CI. Les suites applicatives, l'installation du produit sur OS vierge et les tests de charge restent BLOQUÉS ; la revue indépendante et les protections de branche restent à finaliser.


## Campagne documentaire DIR-011

Les 21 mandats sont préparés dans le [tableau de coordination](coordination-board.md). Le HQ propose une vision, un catalogue, des parcours et une [roadmap](global-roadmap.md) ; les avis spécialisés restent à recevoir. Travail publié par une PR distincte dépendant de la PR nº 1 ; la publication ne vaut ni transmission aux discussions ni approbation du MVP. Le [plan documentaire](../documentation-plan.md) définit les responsabilités et les éléments restant à compléter.


## Réception spécialisée — 29 septembre 2026

Les 21 réponses sont reçues et leurs publications vérifiées dans les PR nº 3–23 : [bilan et références](m0-reception-report.md). Cette mise à jour remplace l'état NON REÇU de la préparation de DIR-011 ; elle n'approuve pas les contenus. Les 21 runs documentaires observés sont success. La revue 21 demande toutefois des corrections de fondation (FIND-21-01 à 03) avant intégration de la pile. MVP, architecture, politiques et ouverture restent à arbitrer. Les nouveaux handoffs sont préparés, pas réputés envoyés.
