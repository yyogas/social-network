# Avis QA ciblé sur le delta Backend L1

## 1. Identification, portée et conclusion

| Champ | Valeur |
| --- | --- |
| Propriétaire | 18 — QA / Testing / Release |
| Version et date | v0.1 — 30 septembre 2026, UTC |
| Statut | EN REVUE ; avis documentaire QA, propositions de compléments à arbitrer |
| Delta examiné | PR Backend [#28](https://github.com/yyogas/social-network/pull/28), commit exact `1acf84fffcaa8131c0826d4874126e107a4cf978` |
| Document examiné | `documentation/backend/api-contract-candidates.md`, complément « Delta propriétaire L1 — GAP-L1-01 à 04 — v0.2 », dont les onze critères L1-BE |
| Intégrité de la source | Blob Backend `2bfcfeed3ffd853e6b9fbef700720d8dcedfe6e9` ; arbre du commit `01734ad8af79ce5d0017045bb99541d9457d1f21` |
| Périmètre | Testabilité, correspondances documentaires, résultats attendus, concurrence, pannes et preuves navigateur des GAP-L1-01 à 04 |
| Classement | MVP proposé pour FEAT-001/002 et projection d'identité nécessaire à L1 ; aucune inclusion au MVP ratifiée par cet avis |
| Priorité | P0 pour établir les oracles d'identité, de révocation et de reprise avant READY |
| Exclusions | Pas de code applicatif, de fusion, de changement des contrats propriétaires ni de réanalyse générale du corpus |

**Conclusion : quatre critères ACCEPTÉS AU NIVEAU DOCUMENTAIRE, cinq À AMENDER et deux BLOQUANTS pour leur passage à READY.** L1-BE-07 et L1-BE-08 demandent un oracle propriétaire sur l'ordre login/logout et la liaison des contextes concurrents. Les GAP-L1-01 à 04 restent ouverts ; cet avis ne donne aucun GO code, protocole ou release.

« ACCEPTÉ AU NIVEAU DOCUMENTAIRE » signifie que le résultat spécifié est assez précis pour préparer le scénario dans le profil candidat. Cela n'approuve ni les choix de sécurité ni une implémentation. « BLOQUANT » désigne ici une ambiguïté empêchant de choisir un résultat de test unique ; ce n'est pas un bug applicatif reproduit. Tous les scénarios détaillés ci-dessous sont **PLANNED** ; leur exécution reste **BLOCKED**, sans preuve applicative reçue.

### Sources ciblées et faits établis

Les références suivantes sont figées au SHA examiné. Les autres documents ont été consultés seulement pour les identifiants et scénarios cités par ce delta.

- [Backend : complément GAP-L1-01 à 04 et critères L1-BE](https://github.com/yyogas/social-network/blob/1acf84fffcaa8131c0826d4874126e107a4cf978/documentation/backend/api-contract-candidates.md).
- [Readiness L1 : GAP, S01–S04h, S08 et conditions de sortie](https://github.com/yyogas/social-network/blob/1acf84fffcaa8131c0826d4874126e107a4cf978/documentation/quality/first-lot-contract-readiness.md).
- [Matrice QA existante : TEST-1801…1848](https://github.com/yyogas/social-network/blob/1acf84fffcaa8131c0826d4874126e107a4cf978/documentation/quality/acceptance-test-matrix.md).
- [Tests documentaires Sécurité : TEST-1401/1402/1415/1418/1419](https://github.com/yyogas/social-network/blob/1acf84fffcaa8131c0826d4874126e107a4cf978/documentation/security/security-operations-requirements.md).
- [Scénarios Web : W03/W04 et TEST-WEB-0003/0004](https://github.com/yyogas/social-network/blob/1acf84fffcaa8131c0826d4874126e107a4cf978/documentation/web-application/web-requirements.md).
- [Mandat et arbitrages HQ, section 10](https://github.com/yyogas/social-network/blob/1acf84fffcaa8131c0826d4874126e107a4cf978/documentation/project-governance/m0-mvp-arbitration.md).
- [Modèle de livrable spécialisé](https://github.com/yyogas/social-network/blob/1acf84fffcaa8131c0826d4874126e107a4cf978/documentation/teams/deliverable-template.md).

| Nature | Constat et conséquence |
| --- | --- |
| CONFIRMÉ par lecture | Les onze critères et les identifiants de tests cités existent dans les sources. Le delta maintient les quatre GAP ouverts. La matrice QA conserve ses cas applicatifs BLOCKED. |
| PROPOSÉ par Backend | Profil Web same-origin, session opaque sans refresh périodique, API-BE-049, L1-CTX, reçu de logout, paramètres et règles associées. Les oracles ci-dessous restent conditionnels à ce profil. |
| PROPOSÉ par QA | Sous-cas, permutations, preuves et corrections de traçabilité du présent avis. Aucun ID TEST existant n'est renommé, aucun statut source n'est promu. |
| À VÉRIFIER | Mécanismes approuvés, budgets temporels, sérialisation effective, comportement des cookies, absence de fuite et effets après restauration. |
| NON REÇU dans cette revue | Build applicatif, environnement d'essai, tests automatisés applicatifs, traces serveur/navigateur, résultat de charge, approbations spécialisées clôturant les GAP. |

Phase 2, Phase 3, International et Long terme : aucune nouvelle fonctionnalité affectée à ces phases par cet avis. Le cas Web mobile relève de la compatibilité du même contrat s'il est retenu ; un client natif, un autre transport ou une autre origine requiert son propre contrat et reste hors de cette revue. Aucun pays, langue, âge ou public pilote n'est présumé.

## 2. Verdicts et correspondances avec les tests existants

Les correspondances sont des liens entre spécifications, pas la preuve qu'un test exécutable couvre le cas. Les compléments proposés sont des sous-cas locaux des identifiants existants.

| Critère et verdict | Correspondances du delta vérifiées | Justification et correction attendue |
| --- | --- | --- |
| L1-BE-01 — ACCEPTÉ AU NIVEAU DOCUMENTAIRE | S01 ; TEST-0401 ; TEST-1801, TEST-1802 | Unicité de l'activation, reçu minimal et séparation activation/recovery observables. Préciser les sous-cas de perte avant/après commit et les compteurs d'effet selon §3.1. Pas de session automatique attendue. |
| L1-BE-02 — À AMENDER | S01/S04g ; TEST-1402 ; TEST-1804, TEST-1833 | Portée de K et refus du rejeu hors contexte explicités. Le résultat sous perte du registre pendant un contexte encore valide, la conservation des tombstones et la rotation de l'empreinte ne sont pas assez définis pour tous les cas. 04, avec 03/14/15, doit fixer la distinction clé nouvelle/état perdu et la continuité du rejeu autorisé (§3.2). |
| L1-BE-03 — ACCEPTÉ AU NIVEAU DOCUMENTAIRE | S03a/b/h ; TEST-0402, TEST-0403 ; TEST-1832 | L'union anonyme/authentifié, les identifiants distincts et le rejet d'un ciblage client sont testables. TEST-0403 ne constitue qu'une couverture partielle : ajouter un sous-cas DTO dédié à S03h. Le dictionnaire des capacités et les recours restent dépendants de GAP-L1-05, sans les valider ici. |
| L1-BE-04 — À AMENDER | S03c/e/g ; TEST-1401 ; TEST-1833, TEST-1834 | 503 distinct d'anonyme et absence de prolongation par 049 acceptables. Ajouter le contrôle positif d'une activité interactive approuvée, le point de lecture de l'horloge et le résultat après dépassement de CONTEXT_MAX_AGE. Paramètres/allowlist et état UX doivent être fournis par 04/05/14 (§3.4). |
| L1-BE-05 — ACCEPTÉ AU NIVEAU DOCUMENTAIRE | S03d/f ; TEST-WEB-0004 ; TEST-1832, TEST-1833 | Rejets des réponses A obsolètes et absence de vue privée A après B sont formulés. Compléter par la matrice de preuves §4, dont BFCache et deux lectures A séparées par une restriction. Ne pas confondre rejet du JSON et contrôle du cookie, traité par L1-BE-08. |
| L1-BE-06 — À AMENDER | S04a/b/c ; TEST-1803, TEST-1833 | Un reçu 204 lié à l'opération permet de distinguer effet confirmé et logout incertain. Le mapping TEST-1803 doit distinguer deux clients partageant la même session logique et deux sessions indépendantes : logout cible la première, recovery révoque toutes les anciennes sessions du compte. Ajouter limites du reçu et perte du contrôle (§3.6) ; son amorçage dépend du blocage L1-BE-08. |
| L1-BE-07 — BLOQUANT | S02/S04d/e ; TEST-1401, TEST-1419 ; TEST-1803 | 004 inactif est testable dans le profil sans refresh. En revanche, « login contre logout » ne distingue pas un login déjà préparé avant logout d'une nouvelle intention explicite après logout. Le logout ne faisant pas avancer la génération proposée, 04/03/14 doivent préciser quelle intention peut encore committer et quelles sessions sont des continuations révoquées (§3.7). |
| L1-BE-08 — BLOQUANT | S04f ; TEST-WEB-0004 | Le cookie A tardif et la perte explicite de B ont un oracle. Le delta laisse expressément ouverts les bootstraps simultanés et la perte du cookie de contrôle. Sans liaison initiale déterminée, « refaire multi-onglets et amorçage concurrent » n'a pas de résultat complet. 04/03/05/14 doivent fournir les ordres et sorties attendus (§3.8). |
| L1-BE-09 — ACCEPTÉ AU NIVEAU DOCUMENTAIRE | S04g ; TEST-1402 ; TEST-1803, TEST-1804 | Une consommation atomique et la vérification de credential_epoch au commit donnent un oracle cohérent. Ajouter les deux ordres login/reset, deux preuves distinctes ainsi que la preuve que la simple demande 006 ne révoque rien (§3.9). Aucune validation du mécanisme MFA/admission par QA. |
| L1-BE-10 — À AMENDER | S04h/S08 ; TEST-1415 ; TEST-1833 | TEST-1415 cible les journaux et TEST-1833 les pannes réseau : ils ne couvrent pas à eux seuls restauration et toutes les bornes serveur. Relier S08 à TEST-1840 ; proposer les sous-cas auth de TEST-1847 pour l'audit et de TEST-1401/1803 pour l'expiration. Définir les fixtures et preuves §3.10 avant READY. |
| L1-BE-11 — À AMENDER | W03 ; TEST-WEB-0003 ; TEST-1401, TEST-1418 | W03 couvre surtout les erreurs de session/recovery, pas une campagne d'anti-énumération. Ajouter TEST-1845 pour origine/CSRF/limites. Séparer équivalence des réponses éligibles, mesure statistique du temps, refus CSRF et déduplication de l'outbox : aucune garantie de livraison email exactement une fois (§3.11). |

**HORS MANDAT QA dans cette revue :** choisir le mécanisme d'identité, approuver SameSite/CSRF/entropie, la conservation des reçus, les droits après restriction, un moteur de stockage ou un mécanisme de restauration. QA peut en formuler les preuves d'acceptation ; ces décisions appartiennent aux propriétaires avec le HQ.

## 3. Résultats attendus, concurrence et pannes

Les erreurs et résultats repris du delta sont conditionnels au contrat candidat. Les demandes de précision ci-dessous ne remplacent pas ce contrat. Dans chaque cas, observer séparément réponse HTTP, état serveur durable et état UI ; une absence de réponse ne signifie pas absence d'effet.

### 3.1. L1-BE-01 — activation et isolation des preuves

Préconditions : identité synthétique admissible selon la règle fournie, contexte contrôlé, challenge d'activation non consommé, K fixé. Le chemin normal produit un unique passage à l'état actif et un reçu 200 minimal, sans session ni cookie de session.

Permutations à exécuter :

- Perte avant réception serveur : aucun effet ; reprise de la même intention peut effectuer la première activation.
- Commit puis réponse perdue : reprise même contexte/K/entrée = même statut et reçu, sans nouvelle mutation, preuve ou session.
- Deux requêtes simultanées même tuple : au plus une mutation ; un 409 OPERATION_IN_PROGRESS intermédiaire est possible selon le contrat, puis reçu réconcilié.
- Deux K différents, même challenge : un succès, l'autre 409 CHALLENGE_CONSUMED après arbitrage atomique ; ne pas exiger deux succès.
- Challenge recovery présenté à l'activation : 400 CHALLENGE_INVALID sans effet. Challenge reconnu à sa limite : 410 CHALLENGE_EXPIRED pour une première consommation expirée.
- Scan/GET du lien : pas de consommation ; ne pas inclure de secret dans les preuves exportées.

Preuves : nombre de transitions d'activation, de consommations et de sessions avant/après, reçu expurgé et ordre des commits. La simple égalité de deux réponses 200 ne démontre pas l'unicité.

### 3.2. L1-BE-02 — contexte, clé et réconciliation

Même contexte vérifié, même version, même K et entrée canonique : un seul effet, puis reçu autorisé dans sa fenêtre. Même tuple avec entrée différente : 409 IDEMPOTENCY_CONFLICT, sans remplacement automatique de K. K possédé seul ou contexte tiers : refus sans lecture d'un reçu privé ; ne pas donner à K la fonction d'un secret.

Tester séparément contexte absent/invalide/expiré, version périmée, challenge expiré, opération en cours, registre indisponible et registre effectivement perdu. Le 401 PREAUTH_CONTEXT_REQUIRED/EXPIRED, le 409 AUTH_CONTEXT_CHANGED et les erreurs d'expiration correspondent à des préconditions distinctes : une priorité d'erreur est à préciser lorsque plusieurs sont vraies.

À amender par 04 :

1. Pour une entrée d'idempotence manquante alors que le contexte reste valide, préciser comment l'oracle distingue une intention jamais reçue d'une intention committée dont la preuve est perdue. En cas d'effet non réconciliable, aucun succès ni nouvel effet ne doit être déduit ; la réponse candidate est 409 OPERATION_RECONCILIATION_REQUIRED ou 503 si l'autorité est indisponible, à rattacher à une précondition exacte.
2. Définir la règle de continuité du fingerprint pendant sa fenêtre de validité si la clé serveur change. Le même corps ne doit pas être testé comme « entrée différente » sans décision explicite. Mécanisme et rétention : 14/15 avec 03/04.
3. Fixer la durée et la disparition des tombstones, le point d'évaluation des expirations et la priorité de refus avant recherche du reçu.

Mesurer avant, à et après chaque échéance avec une horloge serveur contrôlée ; le reçu d'une activation déjà committée peut survivre à l'expiration du challenge mais pas à l'expiration autorisée du contexte. Un bail de worker expiré ne prouve pas un rollback. Interrompre le worker avant et après commit, puis reprendre la même opération sans deuxième effet.

### 3.3. L1-BE-03 — projection d'identité

Tester 049 sans mémoire client pour : session valide active, session valide restreinte, absence/expiration/révocation de session. Attendus :

- 200 anonyme : authentication anonyme, viewer nul et aucune donnée privée.
- 200 authentifié : account_ref opaque, profile_ref distinct ou nul, account_state autorisé et capacités dédupliquées dans l'allowlist.
- Ciblage par query/entrée inconnue : 400 VALIDATION_FAILED ; le client ne choisit jamais le compte lu.
- Champs obligatoires manquants, union contradictoire ou enum inconnue : état client UNAVAILABLE, pas d'identité ni de droits inventés.
- Capacité inconnue : jamais accordée ; champ additionnel compatible ignoré suivant la règle documentée.
- Toutes les réponses 049, erreurs comprises : Cache-Control no-store et aucun Set-Cookie de création, renouvellement ou suppression.

Le fixture « restricted avec capacités vides » teste le schéma ; il n'approuve pas la privation de recours ou de droits privacy. La liste des capacités effectives et leur résultat API reste à fournir au titre de GAP-L1-05. Ne pas assimiler profile_ref nul à un compte absent ou à une permission de créer un profil.

### 3.4. L1-BE-04 — autorité indisponible et vieillissement

Autorité indisponible avec réponse possible : 503 AUTHORITY_UNAVAILABLE, UI indisponible ; aucune transformation en 200 anonyme et aucun droit servi depuis une autorité périmée. Perte réseau : état incertain/indisponible, avec reprise bornée ; 429 suit Retry-After sans boucle illimitée.

Répéter 049 jusqu'au franchissement de la borne idle, sans autre activité : ces lectures ne prolongent ni idle ni durée absolue. Ajouter le contrôle positif d'une opération approuvée « interactive » et vérifier que celle-ci ne prolonge jamais la borne absolue. Cette allowlist manque : ne pas la fabriquer dans le test.

Après restriction confirmée, une mutation interdite préparée sur l'ancien DTO doit être refusée au point d'autorité défini. Un 403/404 d'objet ne déconnecte pas globalement l'utilisateur. Pour les deux lectures 049 entourant la restriction, seule la génération/actualité admissible peut rétablir la vue ; 04/05 doivent préciser l'état UI lorsque CONTEXT_MAX_AGE est dépassé. Aucune promesse d'effacer des octets déjà reçus n'est déduite.

### 3.5. L1-BE-05 — réponses obsolètes, historique et compte courant

Pour A puis B, inverser indépendamment l'ordre des réponses 049, profil, requête protégée, 401 ancien et erreur réseau ancienne. Observer texte visible, arbre d'accessibilité, actions disponibles et prochaine requête : aucune donnée privée A ni action envoyée sous une identité A présentée comme B.

Après logout confirmé : retour arrière/avant, rechargement, restauration d'onglet et retour de BFCache. Avant vérification fraîche, vue privée masquée et état VERIFYING. La projection 049 reste en mémoire seulement, sans persistance localStorage/sessionStorage ni cache partagé/service worker. Inspecter aussi les données de profil, chemins d'erreur et HTML privés pour démontrer l'absence de réapparition de A ; cet avis n'étend pas silencieusement les règles de stockage à tous les autres contrats produit.

Répéter avec deux onglets du même profil navigateur et avec deux réponses A de part et d'autre d'une restriction connue. Les lecteurs obsolètes ne redonnent ni vue privée ni capacité. Le mécanisme d'invalidation inter-onglets relève de 05 ; un test unitaire de store client ne remplace pas ce parcours.

### 3.6. L1-BE-06 — logout confirmé et incertain

Fixtures distinctes : A1 partagé par deux clients ; A1 et A2 sessions indépendantes ; B dans le même contexte après changement de compte.

| Injection/ordre | Résultat attendu du contrat candidat |
| --- | --- |
| Logout A1 reçu et committé | 204 ; A1 et ses continuations refusés sur les deux clients qui le partagent. Ne pas attendre la révocation d'A2 par un simple logout A1. |
| Coupure avant réception | LOGOUT_UNCONFIRMED ; privé masqué. Une reprise valide de la même intention peut effectuer la première révocation. |
| Commit de révocation puis perte de réponse | Même opération/contexte vérifiés : reçu 204, sans deuxième révocation ni nouveau ciblage de /current. |
| 049 retourne encore A1 après une tentative incertaine | Ne pas rouvrir automatiquement le privé ; cela ne clôt pas l'intention de déconnexion. |
| 049 retourne anonyme, ou accès protégé renvoie 401 | Cela ne prouve pas que cette opération de logout a committé ; absence de reçu = résultat de l'opération non confirmé. |
| Contrôle absent, expiré ou perdu | Pas de reçu privé sur la seule connaissance de K ; refus et reprise explicite définis par le contrat. |
| K différent après mort du credential | 401 ; pas de nouvelle opération réussie par simple possession de K. |
| A1 terminé, B connecté, ancienne intention rejouée | 409 AUTH_CONTEXT_CHANGED ; B demeure non révoqué. Un ancien 204 ne modifie pas l'UI de B. |
| Audit obligatoire indisponible avant commit | Pas de 204 fictif ; aucun effet revendiqué comme confirmé. État réel et erreur à observer suivant §3.10. |

Ajouter les bornes exactes du reçu de logout, distinct du reçu préauth. La fenêtre candidate de dix minutes n'est pas approuvée. Un reçu expiré ne justifie jamais un DELETE automatiquement reciblé sur B. Les règles de nettoyage du contrôle après perte et au prochain bootstrap restent bloquées par L1-BE-08.

### 3.7. L1-BE-07 — ordre des transitions à arbitrer

Dans le profil candidat sans refresh, deux appels API-BE-004, y compris simultanés, renvoient 404 RESOURCE_UNAVAILABLE avec zéro création de session et zéro Set-Cookie. Les courses sur login/réauthentification subsistent ; S02 et S04d/e ne deviennent pas entièrement « non applicables ».

**Ambiguïté bloquante :** le delta précise que login avance la génération, tandis que logout termine la session sans avancer cette génération pour préserver le reçu. Il ne donne pas l'oracle complet de cet ordre :

1. Un login/réauthentification L commence et lit le contexte/génération g.
2. Logout D de la session cible committé, reçu 204 confirmé.
3. L tente de committer avec g ; ses headers arrivent en dernier.

Le critère exige l'absence de continuation valide après révocation, mais ne distingue pas suffisamment L d'une nouvelle intention explicite autorisée après D. Aucun défaut de code n'est établi ; il manque la définition de cette frontière dans l'oracle.

**À transmettre à 04/03/14/05 et HQ :** décrire le point de sérialisation, le lien session/intention/génération et le résultat de L dans chacun des ordres L-avant-D, D-avant-L et L-préparé-avant-D/commit-après-D. QA recommande de séparer explicitement une continuation préparée de l'ancienne intention d'une nouvelle connexion consciente après logout, avec un refus sûr pour la première. Le mécanisme reste à choisir par les propriétaires ; ne pas imposer ici une incrémentation de génération qui pourrait casser le rejeu du reçu.

Deux logins A/B simultanés sur une même génération : observer au plus une transition admise, ou la sérialisation explicitement choisie ; jamais deux identités courantes concurrentes pour un même contexte. Les requêtes munies de la version devenue périmée reçoivent 409 AUTH_CONTEXT_CHANGED. Une connexion explicite après D peut être autorisée selon le contrat ratifié ; ne pas écrire un test exigeant l'interdiction perpétuelle de login.

### 3.8. L1-BE-08 — cookies tardifs et amorçage multi-onglets

Partie testable : login A committé, headers retenus ; A révoqué ; login B ; puis livraison réelle des anciens headers A. Le cookie A peut écraser B dans le navigateur, mais le secret A doit rester invalide côté serveur. Résultat autorisé par le delta : perte explicite de B et demande de reconnexion, jamais retour à A ni action sous une identité affichée incorrecte. La préservation transparente de B n'est pas une exigence du candidat.

Retarder séparément une réponse de logout A, recovery, 049 anonyme ou une erreur ancienne : aucune ne doit créer/supprimer le cookie de session B ni envoyer Clear-Site-Data. Vérifier les headers reçus, le cookie réellement envoyé ensuite et le refus/identité serveur ; abort() ou ignorer le body ne neutralise pas les headers.

**Partie bloquante reconnue ouverte dans le delta :** deux onglets sans cookie de contrôle lancent L1-CTX ; les réponses C1/C2 sont livrées dans les deux ordres, puis login sous C1 pendant l'arrivée de C2. Refaire avec contrôle perdu après login et pendant LOGOUT_UNCONFIRMED. À obtenir :

- Quelle liaison est courante après chaque ordre ? Quelle réponse peut poser/remplacer le contrôle et sous quelles préconditions ?
- Comment rejeter l'ancienne intention sans la rattacher à un autre compte ou perdre silencieusement le suivi d'une révocation ?
- Que deviennent l'opération incertaine, son reçu et les sessions orphelines ? Quel état visible et quelle action de reprise restent autorisés ?
- Quels statuts/body/headers sont attendus lorsque le client ne peut plus prouver la liaison, y compris au bootstrap suivant ?

04/03/14 définissent le protocole ; 05 définit les états et la coordination UI. En attendant, sécurité minimale de l'oracle : aucun rattachement implicite à un contexte tiers, aucune ancienne session réautorisée et aucun faux succès. Cela ne suffit pas pour déclarer le scénario complet READY.

### 3.9. L1-BE-09 — recovery, sessions et epoch

Créer deux sessions indépendantes du même compte sur deux profils/appareils, et une session d'un autre compte comme contrôle. Demande 006 : 202 neutre, aucune révocation ni changement du secret. Reset 007 valide : une consommation, un changement du secret et invalidation atomique des anciennes sessions du compte ; aucune session créée implicitement, aucun effet sur l'autre compte.

Variantes : même preuve et même K, même preuve et K différents, deux preuves valides distinctes pour le même sujet/révision. Le contrat doit garantir un seul reset de cette révision ; le statut exact du perdant pour deux preuves distinctes est à expliciter par 04 avant automatisation.

Login avec ancien secret :

- Commit login avant reset : la session obtenue appartient aux anciennes sessions invalidées au commit reset.
- Vérification du secret avant reset, commit login après reset : 401 AUTH_INVALID par contrôle d'epoch, pas de nouvelle session valide.
- Login après reset avec nouveau secret : possible selon les droits en vigueur ; ne pas lever restriction, admission ou MFA par récupération.

Couper la réponse après reset et rejouer : reçu minimal sans deuxième reset/epoch ni nouvelle session. Croiser une restriction pendant le reset ; les permissions résultantes sont celles du contrat métier ratifié, pas un retour supposé à un compte actif sans restriction.

### 3.10. L1-BE-10 — horloges, pannes et restauration

Préparer des horloges serveur contrôlables sans dépendre de sleeps aléatoires : instant avant, égal et après chaque limite. Le candidat prévoit la fin à now >= min(dernière activité interactive + idle, émission + absolu). Tester séparément challenge, préauth, reçu, idle et absolu ; inclure une requête qui franchit l'échéance entre réception et commit. Le point de contrôle doit être fixé par 04/14.

Injecter des pannes distinctes :

- Autorité indisponible avant autorisation : aucun droit positif tiré d'un cache périmé, 503 si réponse possible.
- État durable committé, réponse perdue : ne pas assimiler timeout et rollback ; reprendre uniquement selon l'opération et son reçu.
- Audit obligatoire indisponible avant commit : mutation refusée ; faire vérifier par 04/14 le couplage durable avec l'effet. Panne de diagnostic après commit : effet conservé, reprise sans doublon.
- Restauration isolée d'un état antérieur à une révocation/reset : anciens secrets non acceptés après réouverture ; observer chaque ancienne session et chaque route protégée pertinente. Le mécanisme de GAP-L1-08 est une dépendance 03/14/15, pas une décision de cet avis.
- Canaris synthétiques dans password, challenge, cookie, CSRF, contexte et DTO : absents des logs/traces/export de preuve non autorisés, avec résultats corrélables par identifiants non secrets.

Compléments de mapping proposés : S08 → TEST-1840 (restauration), audit auth → sous-cas de TEST-1847, expiration → TEST-1401/1803. TEST-1847 ne vise pas actuellement FEAT-001/002 : cette extension doit être explicite à la prochaine mise à jour de la matrice, et ne constitue pas une couverture déjà acquise.

### 3.11. L1-BE-11 — origine, neutralité et mails

Séparer quatre campagnes pour éviter un oracle trompeur :

1. Origine étrangère, absente, CSRF absent/invalide/lié à un autre contexte, version obsolète : login/logout/reset sans effet non autorisé, avec 403 REQUEST_ORIGIN_DENIED ou CSRF_INVALID selon le cas défini. Si plusieurs contrôles échouent, demander l'ordre de priorité à 04/14. Ajouter registration/activation/demande recovery, que le delta soumet aussi à ces contrôles.
2. Anti-énumération : comparer des requêtes autrement valides, sous contrôles équivalents, pour identité existante/inexistante/inadmissible. Vérifier 202 neutre de 001/006 et 401 AUTH_INVALID uniforme du login invalide, corps et headers non révélateurs. Ne pas exiger l'égalité entre login réussi et login refusé, ni entre reçu autorisé et contexte tiers.
3. Temps : mesures répétées et distributions avec caches, quotas, coûts de hash et conditions réseau documentés. Seuil d'acceptation et protocole statistique à fournir par 14 avec 04 ; aucun nombre de répétitions, p-value ou budget de fuite inventé comme seuil approuvé.
4. Mails : même tuple rejoué après commit = aucune nouvelle entrée d'outbox. Worker redémarré après acquittement fournisseur perdu = une livraison physique dupliquée peut subsister selon le delta, avec le même challenge ; ne pas la confondre avec un second challenge ou une deuxième consommation. K différent est une nouvelle intention soumise à quotas/déduplication, pas une promesse générale « exactement une fois ».

TEST-1845 couvre le cadre abus/CSRF/limites. Pour l'outbox auth, proposer un sous-cas S01/S04g inspiré de TEST-1838 ; la liste actuelle de fonctionnalités de TEST-1838 n'inclut pas FEAT-001/002, donc son extension est à tracer explicitement. Les limites N-1/N/N+1, le taux et la durée de charge restent à paramétrer par 04/14 ; aucun test de performance n'a été exécuté.

### Paramètres candidats à figer dans les fixtures

Ces valeurs proviennent du delta et restent PROPOSÉES. Une exécution exploratoire peut les paramétrer ; un résultat de release exige leur approbation et leur version de contrat.

| Paramètre candidat | Valeur / règle reprise | Vérification attendue |
| --- | --- | --- |
| Préauth / challenge | 30 minutes / 15 minutes | Avant, à et après expiration ; contexte expiré refusé avant accès au reçu |
| Reçu préauth | Jusqu'à expiration du contexte, sans prolongation | Rejeu après expiration du challenge mais dans le contexte, puis refus hors fenêtre |
| Session | Idle 30 minutes ; absolu 12 heures ; pas de remember-me | 049/poll/assets/rejeu de reçu exclus de l'activité ; allowlist interactive encore ouverte |
| Contrôle et reçu de logout | Contrôle distinct maintenu pendant session ; fenêtre après logout candidate 10 minutes | Reçu autorisé uniquement pour opération liée, sans droits sociaux après révocation |
| Reprises client | Timeout 10 secondes ; au plus deux reprises dans 30 secondes pour lectures/rejeux sûrs | Respecter Retry-After ; si hors budget, arrêter ; aucun login ou nouveau K automatique |
| Paramètres non reçus | CONTEXT_MAX_AGE, quotas, tailles, bornes de DTO/capacités, tolérance d'horloge, conservation des tombstones | Ne pas inventer les seuils ; cas correspondants BLOCKED jusqu'à réponse propriétaire |

## 4. Preuves navigateur et dossier d'exécution requis

| Lot de preuve | Dispositif minimal proposé | Ce que la preuve doit démontrer |
| --- | --- | --- |
| Identité/UI | Comptes synthétiques A/B, état actif/restreint et profil nul ; capture UI/arbre d'accessibilité liée aux appels | Identité affichée et actions cohérentes ; privé masqué pendant vérification/incertitude ; aucune donnée A sous B |
| Headers/cookies | Navigateur réel avec interception des réponses avant réception des headers, cookie jar réel ; observations serveur expurgées | Ordre effectif des Set-Cookie et valeur logique du credential envoyé à la requête suivante ; impossibilité d'utiliser un ancien secret |
| Multi-onglets | Deux onglets partageant le même profil/cookies, barrières de test contrôlées | Bootstrap, génération, login/logout et livraison dans les deux ordres ; un verrou JavaScript local ne sert pas de preuve serveur |
| Multi-appareils | Deux profils de cookies indépendants, plus un compte témoin | Portée session du logout et portée compte du recovery sans effet sur le témoin |
| Navigation/cache | Historique/BFCache, reload, restauration de session et service worker s'il est présent | Pas de réapparition du privé avant revalidation ; pas de stockage privé interdit, y compris réponses d'erreur |
| Réseau | Offline avant envoi, coupure après réception, après commit et avant headers/body ; latence/reconnexion contrôlées | LOGOUT_UNCONFIRMED/UNAVAILABLE corrects ; pas de retry login ni de K nouveau automatique ; reprises bornées selon paramètres approuvés |
| Compatibilité | Versions exactes des navigateurs/OS retenus ; proposition Chromium, Firefox et WebKit, plus Safari iOS réel si supporté | Effets de cookies, cache et onglets vérifiés sur les cibles approuvées ; une émulation WebKit seule ne vaut pas preuve Safari iOS |
| Autorité et durable | Barrières avant validation, avant commit, après commit ; horloge test et compteurs d'effet | Résultat lié à l'ordre serveur, pas seulement à l'ordre des captures d'écran ou aux temps clients |

Pour chaque sous-cas : identifiant L1-BE + S/TEST existant, version du contrat approuvée, SHA build, environnement, navigateur/OS, fixture, préconditions, ordre imposé, résultat HTTP/UI/durable attendu et observé, nombre d'effets et lien vers la preuve expurgée. Ne jamais joindre de HAR brut contenant des secrets ; exporter des valeurs remplacées par des aliases stables et les attributs de cookies nécessaires. Conservation et accès au dossier : à fixer avec 14/15.

Les scénarios API peuvent vérifier refus, DTO et compteurs ; les tests unitaires peuvent vérifier unions et calcul de bornes. Ils ne démontrent ni Set-Cookie tardif, ni BFCache, ni partage entre onglets. Une CI de documentation ne démontre aucun de ces résultats.

## 5. Dépendances, questions ciblées et risques

Les repères QA-A à QA-F sont locaux à cet avis, pas de nouveaux IDs du registre global. Les transmissions ci-dessous sont **À TRANSMETTRE** ; publier la PR ne prouve pas leur réception par les équipes.

| Repère / GAP | Question, propriétaire et livrable attendu | Blocage et risque associé |
| --- | --- | --- |
| QA-A / GAP-L1-04 | 04 + 03/14, avec 05 : fournir table des ordres login préparé / logout / nouveau login et lien intention-génération-session ; HQ arbitre l'option structurante | BLOQUANT L1-BE-07 : oracle ambigu pouvant masquer une reprise de session après déconnexion |
| QA-B / GAP-L1-02/04 | 04 + 03/05/14 : diagramme ou table des bootstraps C1/C2, cookies tardifs, contrôle perdu, reçu et sessions orphelines ; résultats HTTP/UI pour chaque ordre | BLOQUANT L1-BE-08 : perte de liaison, mauvais compte ou faux logout confirmé |
| QA-C / GAP-L1-02 | 04 + 03/14/15 : règle du registre perdu/purgé, tombstones, empreinte après rotation et priorité des refus ; politique de durée avec preuve d'approbation | Bloque les sous-cas L1-BE-02 : duplication d'effet, exposition de reçu ou impossibilité de réconciliation |
| QA-D / GAP-L1-03/04 | 04/05/14 : allowlist d'activité, bornes serveur, CONTEXT_MAX_AGE et budgets retries/quotas ; préciser comportement au dépassement | Bloque READY des cas paramétrés 04/06/10/11 ; faux maintien de session ou boucle de reprises |
| QA-E / GAP-L1-05, dépendance seulement | 04/05 + 09 Trust & Safety/15 : capacités après restriction et accès aux recours/droits, fixture autorisée et refus API | Bloque l'acceptation intégrée « restreint » ; un fixture à capacités vides pourrait sinon devenir une interdiction non approuvée |
| QA-F / GAP-L1-08, dépendance seulement | 03/14/15, avec opérations : invariant et procédure de restauration/révocation ; environnement isolé et instrumentation fournis par 04/05/21 | Bloque l'exécution S08/L1-BE-10 ; risque de réactiver des secrets après restauration |

Autres réponses ciblées : 04 précise le perdant de deux preuves recovery distinctes (§3.9) ; 14/04 définissent le protocole de mesure anti-énumération (§3.11) ; 05/HQ confirment les cibles navigateur, sans ajout de stack par QA. Les recommandations « sans refresh », attributs de cookies et durées candidates nécessitent les validations 03/05/14/15 pertinentes avant arbitrage HQ. QA ne transforme pas leur présence dans le delta en accord.

Priorités : P0 pour incohérence d'identité/révocation/droits ou preuve impossible ; P1 pour compléter traçabilité et format de preuve lorsque l'oracle existe. Aucune probabilité chiffrée n'est établie. Aucun ticket de bug applicatif n'est créé sans reproduction ; les défauts décrits sont des lacunes de contrat/testabilité.

## 6. Contrôles réellement exécutés

Le périmètre de vérification documentaire est ce nouveau fichier et ses références au snapshot examiné. Les contrôles du dépôt sont distincts des scénarios applicatifs ci-dessus.

Exécution locale du 30 septembre 2026, Linux / Python 3.12.14. Les scripts et leurs tests ont été lus au SHA Backend examiné ; un espace de préparation isolé a servi à contrôler ce nouveau fichier.

| Contrôle réellement exécuté | Résultat et limite |
| --- | --- |
| `python3 -m unittest discover -s tests/repository -p 'test_*.py' -v` | 24 tests de l'outillage du dépôt réussis ; aucun test du produit |
| Contrôle textuel ponctuel `python3 check-review.py` (outil local de préparation) | 11 lignes de verdict uniques, répartition 4/5/2 ; tous les IDs TEST cités retrouvés dans les sources consultées ; 7 liens au SHA exact vers des chemins présents dans l'arbre |
| `inspect(..., require_layout=False)` du validateur du dépôt, appelé par le contrôle ciblé | Réussi sur ce seul nouveau fichier ; aucune validation locale prétendue de l'arborescence complète |
| `git diff --cached --check` | Réussi sur l'ajout documentaire préparé |

Le résultat de CI sur le commit publié et la vérification du diff distant sont consignés dans la description de la PR de cet avis. Aucun succès CI de la PR Backend n'est utilisé comme preuve du protocole. **Aucun test applicatif unitaire, API, intégration, frontend, mobile, E2E, performance ou sécurité n'a été exécuté dans cette revue.**

Conditions de futur READY : réponse propriétaire versionnée sur les points ouverts, avis spécialisés requis, arbitrage HQ référencé, fixtures et environnement reçus, oracle et preuve attendue figés pour le sous-cas. Conditions de PASS : exécution réelle avec résultat observé et preuve référencée ; la simple existence d'un mapping ne suffit pas.

## 7. Compte rendu de fin d'étape

1. **Décisions prises / à valider.** QA adopte cette décomposition documentaire et conserve les IDs existants. Quatre verdicts documentaires favorables, cinq amendements, deux blocages de testabilité. Aucun choix de sécurité, permission, durée, architecture ou passage à READY approuvé par QA.
2. **Livrables.** Présent avis v0.1, chemin `documentation/quality/backend-l1-qa-review.md`, référencé au commit exact de la PR #28. La PR de publication fournit son commit et ses contrôles ; aucun document propriétaire existant n'est modifié.
3. **Tests exécutés.** Revue des onze correspondances et contrôles documentaires dont le relevé est joint à la PR. Aucun test applicatif exécuté, aucun PASS applicatif déclaré.
4. **Questions.** QA-A à QA-F, résultat du perdant recovery, priorités d'erreurs, mesure des timings et matrice navigateurs ; propriétaires désignés en §5.
5. **Dépendances.** 04 Backend, 03 Architecture, 05 Web, 14 Sécurité, 15 Privacy, 09 Trust & Safety et 21 pour les moyens d'exécution. Demandes ciblées À TRANSMETTRE ; aucune réception inter-équipe présumée.
6. **Risques.** Réapparition d'une ancienne identité, mauvaise liaison de contexte, logout faussement confirmé, effet rejoué après perte du registre, secrets restaurés et couverture surestimée. Mesures : contrat explicite, permutations contrôlées et preuves API/serveur/navigateur.
7. **Prochaines étapes / HQ.** Transmettre prioritairement QA-A/QA-B, obtenir les amendements propriétaires, puis mettre à jour uniquement les sous-cas et mappings concernés. HQ arbitre avec les propriétaires ; QA prépare ensuite l'exécution sur un build et un environnement reçus. Les quatre GAP restent ouverts et L1 bloqué pour code selon la référence, sans fusion demandée par cet avis.
