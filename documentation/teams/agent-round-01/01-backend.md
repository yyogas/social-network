# Agent 01 — Relecture Backend de convergence

Le texte v0.3 corrige plusieurs contradictions précises de v0.2. Il fournit désormais des invariants documentaires exploitables, mais ne ferme aucun constat propriétaire et ne rend pas L1 prêt pour le code. Cette revue autonome distingue la correction rédactionnelle, le choix encore ouvert et la preuve future ; elle ne constitue pas un nouvel avis officiel des équipes Web, Sécurité ou QA.

## Références réellement lues

- Backend, PR #28, `0a7fcd54b996cc292bfe98c61a835613837def32`, [api-contract-candidates.md, amendement C0–C9](https://github.com/yyogas/social-network/blob/0a7fcd54b996cc292bfe98c61a835613837def32/documentation/backend/api-contract-candidates.md).
- Architecture, PR #33, `a7901fc87e79975d8963e909a89fc8150410e40a`, [l1-session-convergence.md, §§2–6/8](https://github.com/yyogas/social-network/blob/a7901fc87e79975d8963e909a89fc8150410e40a/documentation/architecture/l1-session-convergence.md).
- Web, PR #29, `e363e751d4b797cceb6c6ab3ec79745d6e54e380`, [backend-l1-web-review.md, B01–B04](https://github.com/yyogas/social-network/blob/e363e751d4b797cceb6c6ab3ec79745d6e54e380/documentation/web-application/backend-l1-web-review.md).
- Sécurité, PR #30, `3221f762b5f98a552a3600fc24118fbe99b7a003`, [backend-l1-security-review.md, S14-L1-05/09/13](https://github.com/yyogas/social-network/blob/3221f762b5f98a552a3600fc24118fbe99b7a003/documentation/security/backend-l1-security-review.md).
- QA, PR #32, `cada61a7b6391a1119bfdf70b4ddc7b04ab13dbb`, [backend-l1-qa-review.md, L1-BE-07/08](https://github.com/yyogas/social-network/blob/cada61a7b6391a1119bfdf70b4ddc7b04ab13dbb/documentation/quality/backend-l1-qa-review.md).

Les trois avis portent sur Backend v0.2, `1acf84fffcaa8131c0826d4874126e107a4cf978`. Leur autorité ne se transfère pas au nouveau SHA. Agent 01 désigne ici le rôle de cette ronde ; le propriétaire canonique du contrat reste **04 Backend**.

## Corrections établies et limites restantes

| Constat | Correction vérifiable dans v0.3 | Encore ouvert |
| --- | --- | --- |
| Web B01 | C1 exige un snapshot liant projection, version, intention, vue et CSRF ; deux GET indépendants ne prouvent plus la cohérence. Séquence nominale 003 et course A→B décrites. | Bundle conceptuel seulement : schéma, transport, acquisition après changement de vue et primitive de liaison restent 03/04/05/14. |
| Web B02 | C1 retire explicitement la comparaison email saisi/049. Un succès appartient à I ; réponse perdue signifie résultat inconnu, sans lookup email ni second login automatique. | Attribution attestée de I et éventuel résultat B restent à spécifier. Le besoin est corrigé ; le protocole consommable ne l’est pas encore. |
| Web B03 | C2 reconnaît qu’un reçu ne prouve pas un DELETE jamais reçu. A impose une authentification fraîche après perte de vue ; B doit apporter une continuité démontrée. | A/B, coût reload, portée et fin du verrou ne sont pas adoptés. Relecture 049 seule demeure insuffisante. |
| Web B04 ; S14-L1-05 ; QA 08 | C2/C7 ajoutent ancienne paire cohérente, paire croisée, deux ordres de cookies et vue demeurée active. La garantie globale est explicitement BLOCKED. | Aucun mécanisme n’identifie C1/C2 indépendants comme même navigateur. HQ/05/14 doivent accepter une portée par racine ou demander un mécanisme supplémentaire à 03. |
| S14-L1-09 | C4 distingue miss cache, absence autoritative intègre, scope explicitement retiré et autorité invérifiable. 409 exige un état connu ; sinon 503 et admissions fermées. | Choix registre/tickets, démonstration d’intégrité, barrière D hors rollback, runbook et cycle de conservation restent 03/14/exploitation/15. La perte silencieuse est expressément hors garantie. |
| S14-L1-13 ; QA 07 | C3 fait avancer T au logout, sépare reçu immuable et fence, revalide E à L et conserve les protections jusqu’au commit. Login préparé avant logout : 409 ; nouvelle intention après : admissible. | Primitive de sérialisation, budget transactionnel, durabilité et frontière exacte des continuations F restent à ratifier. |

La convergence avec Architecture est réelle sur T, E, L, le reçu distinct et l’admission K. Backend conserve correctement A et B comme options ; il n’adopte ni la recommandation A ni le report conditionnel de B en Phase 2. Ce désaccord de niveau de décision est explicite, pas une contradiction cachée.

Deux points empêchent encore un oracle entièrement univoque. Premièrement, C3 annonce qu’une continuation F gagnante sera suivie d’un logout 204, alors que C5 refuse une version T obsolète : il faut préciser si cette continuation avance T et quelle précondition terminale autorise alors le logout. Deuxièmement, la frontière entre CSRF « autre contexte » (403, priorité 3) et liaison authentique périmée (409, priorité 4) mérite une règle pour le tuple authentique intégralement ancien. Enfin, C7 réutilise D pour la déconnexion alors que C4 l’emploie comme incarnation d’admission ; renommer cet événement évite un oracle mal lu.

## Amendements minimaux proposés à 04

Texte à ajouter, soumis aux propriétaires ; aucune primitive ni permission n’est adoptée par cette revue :

```diff
+ C1 — Avant gel, 04/05/14 doivent fournir une fiche unique d’acquisition :
+ opération porteuse, champs et headers, preuve de liaison, règles d’émission
+ des cookies, nominal et transition concurrente. AuthView demeure conceptuel
+ jusqu’à cette fiche ; aucune implémentation ne choisit seule l’alternative.

+ C3 — Le 204 après continuation de F suppose une précondition terminale
+ expressément ratifiée par 03/14. Préciser si la continuation avance T.
+ Sans exception approuvée, la règle générale de C5 s’applique : T périmé
+ produit 409 sans mutation. L’oracle de révocation après continuation reste
+ non READY ; une commande ne se recible jamais vers une famille indépendante.

+ C5 — Distinguer CSRF non authentique ou liée à une autre R/I, refusée 403,
+ de la preuve authentique correspondant au tuple R/T/I présenté mais devenu
+ obsolète, proposée au refus 409 de priorité 4. Faire confirmer cette
+ distinction par 14 avant de l’utiliser comme oracle consommateur.

+ C7 — Remplacer D signifiant déconnexion par « commit_logout ».
+ Réserver D à l’incarnation d’admission ; conserver L pour l’autorisation.
```

HQ doit demander une décision explicite sur portée et reprise ; 03/14 doivent fournir les garanties de concurrence/admission ; 04/05 doivent figer la fiche consommateur ; 15/14 doivent ratifier les cycles. QA 18 pourra ensuite réviser les seuls oracles affectés au SHA amendé. Les décisions sur les droits et le canal hors session restent aux propriétaires 09/10/15/14, indépendamment d’A/B.

## Responsabilité — sept lignes

1. **Décision :** corrections rédactionnelles reconnues ; aucun constat propriétaire fermé.
2. **Livrable :** cette revue locale et quatre amendements textuels proposés.
3. **Vérification :** lecture croisée des cinq fichiers aux SHAs cités ; aucun test runtime.
4. **Questions :** A/B, portée, acquisition, CSRF périmée, continuation F/T, intégrité et budgets.
5. **Dépendances :** HQ, 03/04/05/14/15/18 ; exploitation et 09/10 selon leur périmètre.
6. **Risques :** identité ancienne réadmise, faux logout confirmé, effet répété et oracle ambigu.
7. **Suite :** synthèse HQ puis relecture propriétaire au SHA exact ; aucune écriture distante, fusion ou autorisation code.
