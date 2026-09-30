# Coordination déléguée — ronde 01

**30 septembre 2026. Mandat DIR-013 confirmé ; avis techniques PROPOSÉS.** Le porteur a demandé vingt sous-agents pour accélérer le travail et centraliser ses instructions auprès du HQ. Vingt missions distinctes ont été lancées, par vagues avec six sous-agents simultanés au maximum. Le HQ répartit, confronte, corrige et publie leurs résultats. Cette ronde ne crée pas vingt branches ni vingt demandes manuelles au porteur.

Ces sous-agents sont de nouveaux exécutants de la session. Leurs numéros ci-dessous ne désignent pas les équipes M0 portant les mêmes numéros. Ils peuvent lire les pièces GitHub et produire des contributions ; ils n'ont pas écrit dans les autres discussions ChatGPT et ne représentent pas leurs auteurs. La délégation ne constitue pas un service qui poursuit son travail après la fin de la session.

## Références examinées

| Pièce | Référence immuable / portée |
| --- | --- |
| HQ et documents M0 | [PR 27 à 4d3cd079](https://github.com/yyogas/social-network/tree/4d3cd079e92217936af3292429a38f91f7b576ff), 86 fichiers |
| Backend v0.3 | [Contrat PR 28 à 0a7fcd54](https://github.com/yyogas/social-network/blob/0a7fcd54b996cc292bfe98c61a835613837def32/documentation/backend/api-contract-candidates.md), amendement de convergence C0–C9 |
| Architecture | [PR 33 à a7901fc8](https://github.com/yyogas/social-network/blob/a7901fc87e79975d8963e909a89fc8150410e40a/documentation/architecture/l1-session-convergence.md) |
| Avis Web / Sécurité / Privacy / QA historiques | PR 29–32, SHAs e363e751 / 3221f762 / 81063238 / cada61a7 ; ils examinent Backend v0.2 à 1acf84ff, pas v0.3 |

Les annexes précisent leurs sources et hypothèses. Les anciennes copies de travail nommées `backend-pr28-v03.md` et `architecture-pr33.md` correspondent aux deux fichiers canoniques ci-dessus ; elles ne sont pas de nouveaux contrats. Les références à `outputs/` désignent les annexes de cette ronde, accessibles dans le tableau suivant.

## Vingt missions et livrables

| Sous-agent | Mission bornée | Pièce reçue |
| --- | --- | --- |
| 01 | Delta Backend v0.3 et amendements minimaux | [Backend](01-backend.md) |
| 02 | Relecture des trois blocages Sécurité | [Sécurité](02-security.md) |
| 03 | Acquisition et reprise Web | [Web](03-web.md) |
| 04 | Cycles de données et droits sous restriction | [Privacy](04-privacy.md) |
| 05 | Oracles de concurrence et corrections QA | [QA](05-qa.md) |
| 06 | Portée minimale des sessions et options A/B | [Architecture](06-architecture.md) |
| 07 | Rechargement, sortie et appareil partagé | [Produit](07-product.md) |
| 08 | Matrice des opérations sous restriction | [Trust & Safety](08-trust-safety.md) |
| 09 | Réception et suivi hors session sociale | [Support](09-support.md) |
| 10 | Invariants, transaction, L et commit | [Données](10-data-model.md) |
| 11 | Restauration, incarnation et CI | [Exploitation](11-devops.md) |
| 12 | Messages, états et localisation | [UX/localisation](12-localization-ux.md) |
| 13 | Focus, annonces et retrait du privé | [Accessibilité](13-accessibility.md) |
| 14 | Frontière profil/avatar et médias | [Médias](14-media-boundary.md) |
| 15 | Audit, diagnostic et preuves minimales | [Observation](15-observability.md) |
| 16 | Budgets de concurrence et mesures futures | [Capacité](16-capacity.md) |
| 17 | Sources, index et distinction des rôles | [Documentation](17-documentation.md) |
| 18 | Contradictions entre avis et sources | [Revue d'intégration](18-integration-review.md) |
| 19 | Chemin critique du prochain lot | [Livraison](19-delivery.md) |
| 20 | Relecture indépendante des revendications | [Contrôle final](20-final-qa.md) |

Les vingt pièces sont des analyses reçues, pas vingt approbations du produit. Les constats de revue sur un état antérieur sont conservés avec leur résolution HQ ci-dessous ; ils ne décrivent pas nécessairement le texte final de l'annexe corrigée.

## Synthèse HQ et divergences traitées

La v0.3 avance le fence T au logout, distingue résultat immuable et version mutable, rattache le succès du login à son intention et ne déduit plus un conflit de la seule absence de K. Elle reconnaît les limites des racines indépendantes et du logout jamais reçu. Ce sont des corrections documentaires réelles ; aucune ne prouve une exécution applicative.

**Rechargement et portée.** Les sous-agents 02/06 recommandent d'instruire A, avec authentification fraîche après perte de vue ; 03/07 recommandent une continuité ordinaire vérifiée. HQ conserve ce désaccord : A n'est pas adopté par défaut, B n'est pas réputé résoudre la perte d'intention et aucune garantie globale entre racines indépendantes n'est retirée silencieusement. Le prochain contrat doit exposer le comportement après reload, perte de stockage, réponse tardive et usage partagé, puis faire ratifier ce paquet. Les textes UX sont des candidats de revue, sans langue pilote adoptée.

**Oracle continuation/logout.** La revue indépendante 18, confirmée par 20, a repéré une clôture trop large proposée par 05. Si une continuation de F avance T, le logout préparé à l'ancien T rencontre le refus général 409 de C5 ; le 204 annoncé par C3 exige une précondition terminale spécifique. Un reçu d'une opération déjà committée ne règle pas la première mutation. La pièce QA est corrigée : QA-A/L1-BE-07 reste partiellement ouvert, et 07-b reste conditionnel/BLOCKED. Les autres ordres explicités ne ferment pas ce sous-cas. Renommer l'événement de logout en Q évite sa confusion avec l'incarnation D.

**Droits et conservation.** Les avis 08/09 fournissent une matrice et un parcours de réception candidats, sans créer un canal actif ni une permission. Reçu, email déclaré et numéro de dossier ne suffisent pas à obtenir un export ou à rétablir un accès. Privacy conserve P15-L1-05/08 ouverts : preuve d'identité, responsabilité réelle, horizons terminaux, copies, audit et purge doivent être contractualisés. Le runbook 11 distingue retrait de D et réapplication des effacements ; l'un ne démontre pas l'autre.

**État du lot : L1 reste BLOQUÉ POUR CODE.** Aucun constat propriétaire Web/Sécurité/Privacy/QA n'est fermé par la ronde. Les sous-agents préparent les textes et les revues suivantes ; le HQ n'attend pas une transmission manuelle du porteur pour les coordonner. MVP, stack, pays ouverts, langues, durées, permissions et budget restent dans leurs statuts antérieurs.

## Suite bornée à cinq actions

| Ordre / dépendance | Travail concret | Responsabilité canonique et sortie vérifiable |
| --- | --- | --- |
| 1 | Une fiche de portée/reprise avec reload, logout incertain, racines indépendantes et conséquence sur appareil partagé | HQ avec 01/05/14/15 : une décision explicite et ses contre-exemples ; aucune adoption par simple synthèse |
| 2 — après 1 pour la continuité | Figer acquisition I/W/CSRF, priorité 403/409 et continuation F/T ; corriger Q/D dès rédaction | 03/04/05/14 : amendement unique au contrat, tableaux nominaux et concurrents non ambigus |
| 3 — en parallèle de 1/2 | Matrice droits/recours hors session, preuve proportionnée et réception durable | 09/10/15/14 puis 04/05 : opérations, permissions et canal réellement désigné ; aucun contact inventé |
| 4 — en parallèle de 1/3 | Admission K, horizons de conservation et restauration hors rollback | 03/04/14/15 : primitive candidate, durées calculables, retrait D et réconciliation des effacements |
| 5 — après 2/3/4 | Relecture au SHA amendé puis gate du premier code | 18/20/21 et propriétaires concernés : statuts des constats, preuve documentaire, oracles ; code seulement après critères satisfaits |

Les limites de capacité, médias, accessibilité et observation sont rattachées à ces actions ; elles ne déclenchent pas dix-neuf nouveaux dossiers. Voir le [chemin critique](19-delivery.md) et les [preuves de validation](../../quality/agent-round-01-validation.md).

## Publication et branches

Le paquet enrichit la branche HQ `documentation/m0-reception-consolidation`, PR 27, par un commit documentaire. La lecture GitHub du 30 septembre constate sept PR ouvertes (27–33) et `main` à `ba26729aa10dc497338a960ae78ba904a72216b2`. PR 28 et 33 dépendent de HQ ; PR 29–32 restent les avis historiques empilés sur Backend. Aucun déplacement forcé, suppression de branche, changement de protection ou fusion applicative n'est demandé par cette ronde. Les constats FIND-21-02/05 restent ouverts.
