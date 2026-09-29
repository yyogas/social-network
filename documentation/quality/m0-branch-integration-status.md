# État des branches et séquence d'intégration M0

Date : 29 septembre 2026. Source : métadonnées GitHub relues à la demande du porteur de projet. Ce document complète le bilan de réception HQ ; il ne ratifie aucune proposition métier.

## 1. Décisions prises et décisions à valider

Conserver les 26 branches existantes : main et 25 branches associées chacune à une PR ouverte. Les 25 PR sont ouvertes, non fusionnées et signalées mergeable par GitHub sur leur base actuelle. Ce signal ne prouve ni leur approbation, ni l'absence de conflits après les intégrations suivantes.

Aucune branche orpheline trouvée dans la liste paginée complète. Aucune suppression, force-push, modification de visibilité ou de permissions. Aucune fusion pendant cette vérification : la revue #19 demande encore des changements, et #25 n'a ni commentaire de revue ni approbation formelle lors de la consultation.

FIND-21-01/03/04 : correctif proposé dans #25, à réexaminer par 21 avec les preuves 18/14/20. FIND-21-02 : mode de protection/revue à arbitrer ; la restriction d'offre et main non protégée sont des constats historiques de #19, non des réglages revérifiés ici. FIND-21-05 : maintenance checkout toujours séparée.

## 2. Inventaire vérifié avant ajout de ce rapport

La ligne #24 décrit son SHA avant ce nouveau commit documentaire. Aucun état actuel n'est déduit du seul texte des anciennes PR.

| PR | Branche source | Branche cible | SHA source observé | CI observée |
| --- | --- | --- | --- | --- |
| [#1](https://github.com/yyogas/social-network/pull/1) | `docs/m0-engineering-foundation` | `main` | `8590a095d76965880e94614328a8eafbe09b93cb` | [success](https://github.com/yyogas/social-network/actions/runs/36615257604) |
| [#2](https://github.com/yyogas/social-network/pull/2) | `documentation/m0-team-coordination` | `docs/m0-engineering-foundation` | `dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957` | [success](https://github.com/yyogas/social-network/actions/runs/36617243179) |
| [#3](https://github.com/yyogas/social-network/pull/3) | `documentation/m0-ux-user-journeys` | `documentation/m0-team-coordination` | `71d6e1067f6ed2349d0f8682627e74083ebc2292` | [success](https://github.com/yyogas/social-network/actions/runs/36618625479) |
| [#4](https://github.com/yyogas/social-network/pull/4) | `documentation/m0-media-lifecycle` | `documentation/m0-team-coordination` | `2ffc7b043ee612685eb30e82a7472ccd83a19ef0` | [success](https://github.com/yyogas/social-network/actions/runs/36618648428) |
| [#5](https://github.com/yyogas/social-network/pull/5) | `documentation/m0-creators-monetization` | `documentation/m0-team-coordination` | `3374cd51d6028f3e8c493d835619b1beb531f476` | [success](https://github.com/yyogas/social-network/actions/runs/36618881023) |
| [#6](https://github.com/yyogas/social-network/pull/6) | `documentation/m0-architecture-proposal` | `documentation/m0-team-coordination` | `79f73f914255bbd4bc356e24b2e90a8ac168056d` | [success](https://github.com/yyogas/social-network/actions/runs/36618917107) |
| [#7](https://github.com/yyogas/social-network/pull/7) | `documentation/m0-team10-admin-support` | `documentation/m0-team-coordination` | `fb19574ba3d62ae2ea0e54354cfc8f24dc0e7ff5` | [success](https://github.com/yyogas/social-network/actions/runs/36619050507) |
| [#8](https://github.com/yyogas/social-network/pull/8) | `documentation/m0-web-requirements` | `documentation/m0-team-coordination` | `5a49cc713138e78122470125b04fd93240f33e23` | [success](https://github.com/yyogas/social-network/actions/runs/36619065246) |
| [#9](https://github.com/yyogas/social-network/pull/9) | `documentation/m0-product-specification` | `documentation/m0-team-coordination` | `b076be7231f0128ac0819fe509985b2b8511dc82` | [success](https://github.com/yyogas/social-network/actions/runs/36619152017) |
| [#10](https://github.com/yyogas/social-network/pull/10) | `documentation/m0-team14-security-operations` | `documentation/m0-team-coordination` | `ca77b561fd79fc01a527bb5cd57b90bbfdd361ea` | [success](https://github.com/yyogas/social-network/actions/runs/36619198719) |
| [#11](https://github.com/yyogas/social-network/pull/11) | `documentation/m0-advertising-options` | `documentation/m0-team-coordination` | `6c043d22f3f605a3cbdc198684c8e30cee3fbbc9` | [success](https://github.com/yyogas/social-network/actions/runs/36619242450) |
| [#12](https://github.com/yyogas/social-network/pull/12) | `documentation/m0-data-measurement` | `documentation/m0-team-coordination` | `70c14a465ece7b31a47c1cb2a8b385d6ac345a77` | [success](https://github.com/yyogas/social-network/actions/runs/36619324867) |
| [#13](https://github.com/yyogas/social-network/pull/13) | `documentation/m0-trust-safety` | `documentation/m0-team-coordination` | `d8c11551a141b836fab2efa201f3d96f6fdc9bed` | [success](https://github.com/yyogas/social-network/actions/runs/36619396259) |
| [#14](https://github.com/yyogas/social-network/pull/14) | `documentation/m0-team20-implementation-readiness` | `documentation/m0-team-coordination` | `8918ac04b7a0cfd28cbce033da145adbd55e1e6a` | [success](https://github.com/yyogas/social-network/actions/runs/36619504053) |
| [#15](https://github.com/yyogas/social-network/pull/15) | `documentation/m0-backend-api-contracts` | `documentation/m0-team-coordination` | `e685cc1e36c09c7a0be98a10e701e532d4c83cc9` | [success](https://github.com/yyogas/social-network/actions/runs/36619505311) |
| [#16](https://github.com/yyogas/social-network/pull/16) | `documentation/m0-team16-localization` | `documentation/m0-team-coordination` | `eebcfc593cf5a1ac8f01dff8355f5692aa522702` | [success](https://github.com/yyogas/social-network/actions/runs/36619508959) |
| [#17](https://github.com/yyogas/social-network/pull/17) | `documentation/m0-doc17-index` | `documentation/m0-team-coordination` | `3c174c4053d98dea63cae353686b09f38392c589` | [success](https://github.com/yyogas/social-network/actions/runs/36619516936) |
| [#18](https://github.com/yyogas/social-network/pull/18) | `documentation/m0-mobile-options` | `documentation/m0-team-coordination` | `b5d3482af45937eb5e5afe99714391ce195e238d` | [success](https://github.com/yyogas/social-network/actions/runs/36619518725) |
| [#19](https://github.com/yyogas/social-network/pull/19) | `documentation/m0-integration-review` | `documentation/m0-team-coordination` | `d0a7dcbad10efa4c27c7724b9f39226a6f01a384` | [success](https://github.com/yyogas/social-network/actions/runs/36619588620) |
| [#20](https://github.com/yyogas/social-network/pull/20) | `documentation/m0-growth-pilot-plan` | `documentation/m0-team-coordination` | `52783caac1dea5f6f11ad498ed2e4ee4ed84ebb4` | [success](https://github.com/yyogas/social-network/actions/runs/36619816197) |
| [#21](https://github.com/yyogas/social-network/pull/21) | `documentation/m0-team-07-recommendation-options` | `documentation/m0-team-coordination` | `8683b45e2f546510553a4f78bd03702602ec2070` | [success](https://github.com/yyogas/social-network/actions/runs/36619833642) |
| [#22](https://github.com/yyogas/social-network/pull/22) | `documentation/m0-qa-acceptance` | `documentation/m0-team-coordination` | `c503d80c2132f4ac95164a80f0dba4e7668fae07` | [success](https://github.com/yyogas/social-network/actions/runs/36619939803) |
| [#23](https://github.com/yyogas/social-network/pull/23) | `documentation/m0-team-15-privacy` | `documentation/m0-team-coordination` | `afb9d22b7d2fc3e28bfd16bdc25ae025c721a592` | [success](https://github.com/yyogas/social-network/actions/runs/36620796461) |
| [#24](https://github.com/yyogas/social-network/pull/24) | `documentation/m0-reception-consolidation` | `documentation/m0-team-coordination` | `5c936875543351c21858f9cd0d9ef780c48207d7` | [success](https://github.com/yyogas/social-network/actions/runs/36621670324) |
| [#25](https://github.com/yyogas/social-network/pull/25) | `fix/m0-repository-validation` | `docs/m0-engineering-foundation` | `786da003111f5ac985b521a4c872c7c3251dc00b` | [success](https://github.com/yyogas/social-network/actions/runs/36623392520) |

## 3. Vérifications exécutées

- Métadonnées des 25 PR relues : état, base, head, SHA, mergeability.
- Liste complète des branches : 26 ; page suivante vide.
- Workflow Repository quality : completed/success observé pour chacun des 25 SHA ci-dessus.
- #25 : liste des reviews vide et discussion/commentaires vides.
- Réexécution locale Linux/Python 3.12.14 sur le snapshot de correction :
  - `python3 -m unittest discover -s tests/repository -p 'test_*.py' -v` : 20 tests PASS.
  - `python3 scripts/repository/validate_repository.py` : PASS, 35 fichiers suivis.
  - `git diff HEAD^ HEAD --check` : exit 0 sur l'historique local de préparation.
- Les cinq blobs du workflow, des deux scripts et des deux fichiers de tests locaux ont été comparés aux SHA des fichiers GitHub au commit `786da003111f5ac985b521a4c872c7c3251dc00b` : tous identiques.
- Le commit local de préparation diffère du commit distant : les tests locaux ne sont pas présentés comme un checkout exact de l'historique distant.
- La non-régression du merge synthétique fautif échoue avec le nouveau contrôle et passe avec l'ancien, conformément au test exécuté.

Limites : CI #1–24 basée sur l'ancien contrôle whitespace ; succès historique insuffisant pour autoriser une fusion. Aucun test applicatif, installation, charge, restauration ou audit global des 21 spécifications exécuté ici. Ce contrôle HQ n'est pas la revue indépendante attendue de 21.

## 4. Questions ouvertes

- Équipe 21 : verdict ciblé sur #25 au SHA exact ci-dessus pour FIND-21-01/03/04.
- HQ avec 14/20 : mode de revue/protection compatible avec le dépôt privé, identité réelle des reviewers et capacité d'application des règles. Ne pas confondre contrôle procédural et protection technique.
- HQ et propriétaires : périmètre MVP, communautés, pays/langues/âge, stack, conservation, budget et exploitation restent à arbitrer selon le bilan #24.

## 5. Dépendances et ordre d'intégration

1. Obtenir la revue ciblée de #25 et résoudre le blocage FIND-21-02 selon une décision explicite et traçable.
2. Intégrer #25 dans la branche de #1 après revue favorable ; conserver les branches.
3. Revérifier le diff complet, les tests et la CI de #1 contre main ; fusionner seulement après les validations attendues.
4. Repositionner #2 vers main, incorporer la fondation corrigée par une fusion explicite sans réécriture d'historique, puis revérifier son diff et ses contrôles.
5. Après intégration de #2, traiter #3–24 individuellement : revue documentaire, base actualisée, préservation des apports concurrents, tests corrigés et CI au nouveau SHA avant chaque fusion. Actualiser l'index de 17 et le bilan HQ après les contributions pertinentes.
6. Supprimer une branche seulement après vérification de sa fusion et de l'absence de PR dépendante. Aucune branche actuelle n'est candidate à ce nettoyage.

La réussite actuelle de mergeability pour chaque PR isolée ne garantit pas que la séquence entière sera sans conflit. La publication d'un document ne vaut pas adoption de ses choix fonctionnels.

## 6. Risques et limites

Fusion massive prématurée, perte de contributions par suppression de branches, faux sentiment de sécurité lié aux anciens checks, revues revendiquées sans preuve, changement de base élargissant involontairement un diff. Mesures : séquence ci-dessus, contrôle du SHA et du diff à chaque étape, conservation des branches et revue des propriétaires.

## 7. Prochaines étapes et informations HQ

Le correctif existe déjà : inutile de demander à 20 de le réécrire. Le prochain besoin est un verdict de revue indépendant sur #25, avec validation ciblée QA et exploitation, puis l'arbitrage des protections de fusion. Handoff à transmettre aux discussions 21/18/14/20 ; aucune réception interdiscussion revendiquée.

Ce rapport est ajouté à la PR HQ #24 existante pour éviter une nouvelle branche documentaire. Son ajout ne clôture aucun finding, n'autorise aucun développement applicatif et n'altère pas les livrables spécialisés.
