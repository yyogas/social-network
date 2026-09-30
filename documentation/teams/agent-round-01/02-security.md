# Agent 02 — Sécurité : avis sous-agent sur Backend v0.3

Cet **avis sous-agent** est une relecture documentaire nouvelle, limitée à S14-L1-05/09/13 et à leurs dépendances. Il ne constitue ni un nouvel avis de la discussion 14, ni une clôture par son propriétaire. Aucun test applicatif, navigateur ou de restauration n’a été exécuté ; aucun PASS runtime n’est attribué.

Références figées consultées :

- Backend, PR #28, SHA `0a7fcd54b996cc292bfe98c61a835613837def32`, [api-contract-candidates.md](https://github.com/yyogas/social-network/blob/0a7fcd54b996cc292bfe98c61a835613837def32/documentation/backend/api-contract-candidates.md), v0.3 C1–C8.
- Sécurité, SHA `3221f762b5f98a552a3600fc24118fbe99b7a003`, [backend-l1-security-review.md](https://github.com/yyogas/social-network/blob/3221f762b5f98a552a3600fc24118fbe99b7a003/documentation/security/backend-l1-security-review.md), §§1–5.
- Architecture, PR #33, SHA `a7901fc87e79975d8963e909a89fc8150410e40a`, [l1-session-convergence.md](https://github.com/yyogas/social-network/blob/a7901fc87e79975d8963e909a89fc8150410e40a/documentation/architecture/l1-session-convergence.md), §§2–6 et 8.

| Constat | Verdict proposé pour cette relecture | Motif précis |
| --- | --- | --- |
| S14-L1-05 | **BLOQUANT maintenu** | C1/C2 reconnaissent correctement les racines indépendantes ; protocole de liaison et portée acceptée manquent encore. |
| S14-L1-09 | **BLOQUANT maintenu, contradiction documentaire corrigée** | C4 retire la promesse impossible fondée sur K absent ; mécanisme d’intégrité, admission et retrait D encore ouvert. |
| S14-L1-13 | **BLOQUANT maintenu, invariants précisés** | C3 répare le fence logout et précise L ; primitive commune, frontière de durabilité et budget restent à établir. |

**S14-L1-05 — Cookies, fixation et doubles amorçages.** Backend C1–C2 répond utilement à Sécurité §2 : bundle cohérent, absence de réparation implicite, matrice couvrant cookies sociaux et de contrôle, middleware/proxy, refus des combinaisons invérifiables. L’exception bootstrap est désormais limitée à une création préauth sans pouvoir métier, avec méthode/type/origine et erreurs définis. Ces amendements répondent aussi partiellement à S14-L1-04/07 ; ils ne prouvent pas l’anti-fixation.

Le contre-exemple reste celui de deux créations sans racine commune, C1 et C2, chacune suivie d’un login. Une ancienne paire **cohérente** peut revenir après la nouvelle tout en restant valide. Vérifier les seules paires croisées ne ferme donc pas ce constat. Le témoin W de A protège une page sans état contre la reprise privée par cookie seul ; il ne révoque pas une ancienne vue C1 encore liée. B conserve ce problème tant que son amorçage commun n’est pas démontré. Architecture §2 et Backend C2 l’indiquent correctement.

Amendement proposé : « Le profil retenu précise, route par route, la preuve établissant I/W et sa liaison à R/T/F, sa création, son renouvellement autorisé et son invalidation. Aucun W privé n’est acquis par cookie seul après perte de vue dans A. Toute référence client libre ou version publique est insuffisante. La garantie interracines reste exclue de toute acceptation tant que HQ/05/14 n’ont pas arbitré sa portée ou reçu un mécanisme démontré. »

Preuves attendues de 03/04/05/14 : matrice complète création/réutilisation/perte, contexte préauth fixé ou copié, doublons de cookies et portée ; permutations contrôle/social/W/CSRF, anciennes paires cohérentes, page toujours active, reload et BFCache. Capturer headers appliqués et requête suivante ; une assertion DOM seule ne suffit pas.

**S14-L1-09 — K neuf ou historique perdu.** C4 distingue désormais cache miss, autorité disponible, scope explicitement incertain et autorité invérifiable. Le 409 exige un état connu ; le 503 ferme l’admission lorsque l’intégrité ne peut être établie. L’atomicité mutation/registre/consommation/outbox, la fermeture avant purge et la distinction intention email/livraison physique répondent au défaut logique initial. La rotation de MAC est également précisée sans traiter un replay comme neuf.

La condition « l’autorité démontre l’intégrité » reste cependant une obligation sans mécanisme choisi. Une suppression partielle silencieuse est explicitement hors garantie. Un ticket préadmis restauré comme non consommé ne résout pas davantage un rollback. D placé dans la sauvegarde restaurée n’apporte pas une barrière indépendante.

Amendement proposé : « Retenir pour le profil candidat un registre dans la même autorité transactionnelle que l’effet. Interdire sa purge tant qu’un scope peut rejouer. Décrire l’événement qui ferme les admissions après perte suspectée, l’autorité qui retire D et la condition de réouverture refusant toutes les anciennes capacités. Si cette condition ne peut être établie, maintenir 503 sans nouvelle mutation. »

03/04/14 doivent choisir et documenter ce mécanisme ; 15 fixe les bornes de conservation. QA doit distinguer cache évincé, crash avant/après commit, purge prématurée, failover et restauration. Les inspections portent simultanément sur effet, K et outbox. Ce besoin d’interface anti-retour arrière ne vaut pas clôture du GAP restauration.

**S14-L1-13 — Révocation, login et commit.** C3 reprend correctement Architecture §4 : logout avance T ; reçu immuable distinct ; hash calculable hors transaction mais E revalidé à L ; protections conservées jusqu’au commit durable. Logout gagnant interdit le login préparé à l’ancien T. Login gagnant avant recovery produit une session ensuite invalidée ; recovery gagnant refuse le résultat de hash ancien. Deux challenges du même E ne permettent qu’un reset. Ces corrections rendent les oracles vérifiables sur papier.

Il reste à distinguer rigoureusement continuation de F et nouveau login indépendant B : l’ancien logout ne doit jamais devenir une commande visant la session courante B. La règle L valide puis commit après échéance est une sémantique candidate explicite, encore dépendante d’un budget non fixé.

Amendement proposé : « Choisir la primitive transactionnelle commune protégeant R/T, F, E et l’autorisation métier ; préciser l’ordre des verrous ou CAS, les conflits/reprises, la durée maximale L→commit et la frontière d’acquittement durable. Aucune lecture de cache/réplica ne remplace ce contrôle. Documenter, pour chaque opération, les ressources protégées et le résultat des deux ordres concurrents. »

**Candidat minimal à instruire : A**, avec authentification fraîche après perte de vue, résultat ambigu conservé comme inconnu, aucun reçu persistant obligatoire et une autorité transactionnelle commune. La garantie proposée est bornée à la racine connue, sous acceptation explicite HQ/05/14 ; elle n’est pas adoptée par cet avis. B ne doit être ajouté que pour un besoin de continuité confirmé. Même avec A, liaison initiale, admission K et sérialisation restent des préalables distincts ; la simplicité de l’option ne clôt aucun des trois constats.
