# Avis Sécurité — réponse Backend L1, GAP-L1-01 à 04

## Identification, référence et portée

| Champ | Valeur |
| --- | --- |
| Propriétaire de cet avis | 14 — DevOps / SRE / Security |
| Date / version | 30 septembre 2026, Europe/Paris / v0.1 |
| Mandat | Demande ciblée MASTER reçue dans cette discussion ; avis sécurité seulement |
| Delta examiné | [PR #28](https://github.com/yyogas/social-network/pull/28), commit exact `1acf84fffcaa8131c0826d4874126e107a4cf978` |
| Source propriétaire | [api-contract-candidates.md à la révision examinée](https://github.com/yyogas/social-network/blob/1acf84fffcaa8131c0826d4874126e107a4cf978/documentation/backend/api-contract-candidates.md), complément v0.2, lignes 305–505, quatre GAP et paramètres/critères associés |
| Blob source vérifié | `2bfcfeed3ffd853e6b9fbef700720d8dcedfe6e9` |
| Entrées de raccordement ciblées | [Mandat HQ §10](https://github.com/yyogas/social-network/blob/1acf84fffcaa8131c0826d4874126e107a4cf978/documentation/project-governance/m0-mvp-arbitration.md) ; [candidat L1 §4.2](https://github.com/yyogas/social-network/blob/1acf84fffcaa8131c0826d4874126e107a4cf978/documentation/quality/first-lot-contract-readiness.md) ; C1–C8 du Backend pour les règles héritées |
| Statut de la revue | AVIS DOCUMENTAIRE ÉMIS ; aucun avis d'une autre équipe attribué, aucune approbation globale du protocole |
| Phase / priorité | MVP candidat, P0 ; FEAT-001/002/003/004/018/021, sans changement de roadmap |
| Verdict de passage | **BLOQUANT avant READY/code** : liaison navigateur, traitement d'une perte K en contexte vivant et mécanisme d'ordre autoritatif à compléter ; autres amendements listés ci-dessous |
| Publication | Avis séparé ; document Backend et documents HQ/QA/Web/Privacy préservés ; aucune fusion |

Lecture bornée au delta et aux raccordements nécessaires. Aucun réaudit du corpus, du cloud ou des marchés. DIR-012 et le public universel sont préservés ; ce travail ne déduit pas une admissibilité depuis une priorité marketing. Le verdict ne signifie pas qu'une vulnérabilité runtime a été démontrée.

**Sens des verdicts :** ACCEPTÉ AU NIVEAU DOCUMENTAIRE = invariant recevable dans ce périmètre, sans preuve d'implémentation ni décision transversale ; À AMENDER = correction de précision attendue du propriétaire ; BLOQUANT = impossible de geler/implémenter sûrement le point tant que l'obligation indiquée n'est pas résolue ; HORS MANDAT = avis réservé au propriétaire nommé. La PR documentaire peut être revue et intégrée comme proposition sans lever ces blocages.

Repères S14-L1-01 à 18 locaux à cet avis ; ils ne créent ni nouvelles API ni nouveaux TEST globaux. Les corrections ci-dessous sont proposées au Backend, jamais appliquées silencieusement à son contrat.

## 1. Matrice de verdicts

| Point / ancrage Backend | Verdict | Justification sécurité | Correction ou condition attendue / responsable |
| --- | --- | --- | --- |
| S14-L1-01 — GAP-01, contrôle de boîte mail et admission | **ACCEPTÉ AU NIVEAU DOCUMENTAIRE** | Le canal vérifié n'est ni une identité civile ni une preuve d'âge ou de résidence ; absence de politique n'active pas arbitrairement le compte | Conserver cette séparation, les réponses neutres et l'admission au commit ; 01/15/HQ restent propriétaires de l'admission |
| S14-L1-02 — GAP-01, option email/password et alternatives | **À AMENDER** | L'option peut être instruite ; l'absence de preuve d'universalité des passkeys n'est pas une preuve comparative en faveur du password. Risques phishing, support et compte mail compromis restent ouverts | Qualifier la recommandation d'hypothèse provisoire ; 03/04/05/14 comparent capacité de récupération et bibliothèque éprouvée ; politique password et coût de hachage à tester avant READY, aucun algorithme maison |
| S14-L1-03 — GAP-01, transport web même origine | **ACCEPTÉ AU NIVEAU DOCUMENTAIRE** | Session opaque serveur, TLS, cookie host-only sécurisé et absence de credential dans JSON/stockage JS sont cohérents avec le profil proposé | Acceptation conditionnelle à même origine ; 03/05 ratifient topologie et terminaison TLS ; tout profil inter-origines ou natif demande un contrat distinct |
| S14-L1-04 — GAP-01, origine/CSRF et L1-CTX | **À AMENDER** | CSRF sur login/logout/reset et refus d'origine inconnue sont pertinents ; la règle « toute mutation préauth avec preuve CSRF » doit expliquer comment le premier contexte est créé avant cette preuve | Spécifier exception d'amorçage limitée à création de contexte sans pouvoir métier, origine exacte/configurée, absence/null refusés, Content-Type/méthode, lecture de réponse, quotas et erreurs sans mutation ; préciser où CSRF est transporté et comment il est lié/versionné ; 04/05/14, topologie 03 |
| S14-L1-05 — GAP-02/04, liaison navigateur, fixation et générations | **BLOQUANT** | La garantie est annoncée mais le mécanisme reste explicitement ouvert. Sérialiser un contexte ne sérialise pas deux contextes créés simultanément dans le même navigateur ; un secret généré par serveur n'est pas à lui seul une preuve anti-fixation | Fournir le contrat de liaison et la table cookie de contrôle/cookie session/version/CSRF, règles sur combinaison incohérente, perte/retour d'ancien cookie et amorçages concurrents ; aucune adoption silencieuse d'un contexte arbitraire ; 03/04/05/14, détails §2 |
| S14-L1-06 — GAP-04, secret neuf et génération à la connexion/élévation | **ACCEPTÉ AU NIVEAU DOCUMENTAIRE** | Le credential préauth n'est pas promu en credential social ; ancien secret invalidé et durée absolue non allongée lors d'une simple régénération | Conserver l'invariant. Documenter la succession de session logique sans réutiliser un secret préauth connu ; réalisation couverte par S14-L1-05/13 |
| S14-L1-07 — GAP-04, cookies tardifs | **À AMENDER** | Absence de Set-Cookie social dans logout/lecture/erreur évite une classe de courses. Le document ne généralise pas encore sa matrice aux écritures du cookie de contrôle, au bootstrap et aux intermédiaires | Décrire les réponses qui peuvent modifier chaque cookie et interdire toute réassociation/renouvellement implicite par middleware ; cookies tardifs de contrôle inclus dans L1-BE-08 ; perte explicite de B acceptable, retour à A interdit ; §2 |
| S14-L1-08 — GAP-02, K et reçu historique | **ACCEPTÉ AU NIVEAU DOCUMENTAIRE** | K n'autorise rien seul ; contexte, opération/version, entrée et preuve métier séparés ; reprise ne recrée ni session ni message ; résultat historique distinct du droit courant | Conserver le contrôle avant lecture/replay et les invariants hors registre K. Succès documentaire ne vaut pas exact-once de bout en bout ni preuve de livraison d'email |
| S14-L1-09 — GAP-02, K expiré ou perdu | **BLOQUANT** | Refus après expiration du contexte est défini. Si un enregistrement disparaît alors que le contexte reste valide, l'absence de ligne est aussi celle d'une première clé : le serveur ne peut promettre 409 de réconciliation sans information supplémentaire | 03/04 doivent distinguer clé neuve autorisée et histoire perdue : conservation durable jusqu'au terme du contexte, invalidation de génération après perte, ou admission d'opérations avec preuve durable équivalente. Ne pas traiter un miss cache comme première exécution ; §3 |
| S14-L1-10 — GAP-02, empreinte des champs secrets | **À AMENDER** | Éviter un hash rapide non secret des mots de passe est pertinent ; formulation « empreinte avec clé séparée » insuffisante pour la compatibilité des replays et rotations | Définir construction éprouvée (par exemple MAC standard), séparation de domaines, canonicalisation/version, key-id, accès et durée de disponibilité des anciennes clés ; clé indisponible = refus/réconciliation, pas nouvelle mutation ; 03/04/14/15 |
| S14-L1-11 — GAP-03, lecture d'identité et autorisation | **ACCEPTÉ AU NIVEAU DOCUMENTAIRE** | Panne distincte d'anonyme, compte/profil distincts, capacités sans rôle implicite, aucun effet de renouvellement et contrôle serveur à chaque opération | Aucun DTO ne devient une preuve d'autorisation. Projection et accès aux recours restent à ratifier par 09/15 ; pas de décision sur leurs champs métier ici |
| S14-L1-12 — GAP-04, absence de refresh web périodique | **ACCEPTÉ AU NIVEAU DOCUMENTAIRE** | Cohérent avec une session serveur opaque bornée ; supprime une route de rotation du profil sans supprimer les courses login/élévation/logout | 03/04/05/HQ ratifient ce profil et le comportement d'API-BE-004 ; ne pas présenter l'absence de refresh comme prévention du vol de cookie pendant sa validité |
| S14-L1-13 — GAP-04, révocation/epoch et commit autoritatif | **BLOQUANT** | Invariants recevables, primitive de sérialisation non choisie. Vérification avant transaction ou lecture de réplica obsolète ne démontre pas l'ordre annoncé | 03/04 doivent montrer l'ordre commun login/recovery/logout/écriture, contrôles d'epoch/génération/expiration au point choisi, transaction ou équivalent, réponse après commit durable et comportement crash/cache ; §4 |
| S14-L1-14 — GAP-01/02/04, récupération et autres preuves | **À AMENDER** | Reset atomique, pas d'auto-login et révocation de sessions antérieures sont recevables. La « révision » du challenge est mentionnée mais sa relation au credential_epoch et aux autres challenges outstanding n'est pas explicite | Définir si reset consomme/invalide toutes les preuves d'accès antérieures du compte ; proposition : invalider celles liées à l'ancienne révision. Tester deux challenges différents valides et login ancien en vol ; pas de levée de MFA/sanction ; 04/14, projection 09/15 |
| S14-L1-15 — GAP-04, reçu de logout | **À AMENDER** | Un reçu lié à l'effet durable peut confirmer une intention après perte de réponse ; 401 ou lecture anonymous ne le peuvent pas. La portée restreinte est pertinente mais dépend du contexte bloqué en S14-L1-05 | Fixer requête/headers, réponse 204 sans corps/no-store/sans mutation de cookies, validation CSRF possible après fin sociale, borne non glissante et départ de fenêtre ; K inconnu jamais rattaché après coup. Comparer maintien de l'incertitude sans reçu comme alternative ; §5 |
| S14-L1-16 — paramètres proposés | **À AMENDER** | Durées explicitement proposées : bon statut. Entropie, quotas et activité prolongeant idle restent ouverts ; leur omission empêche des tests aux bornes significatifs | Compléter le manifeste de paramètres (§6), mesurer charge/délivrabilité/accessibilité, faire ratifier par propriétaires ; aucun 30 min/12 h ni autre nombre approuvé par cet avis |
| S14-L1-17 — minimisation/rétention et accès aux droits après restriction | **HORS MANDAT** pour validation métier/privacy | Sécurité confirme absence de droit implicite et besoin d'accès contrôlé ; ne peut ratifier conservation ni choisir capacités de recours | 15 avec 09 examinent uniquement ces projections et données, sans déduire qu'une liste vide est une voie de recours suffisante |
| S14-L1-18 — exhaustivité du mapping des 11 critères et UX multi-onglets | **HORS MANDAT** pour approbation QA/Web | Les cas adverses ci-dessous alimentent QA et Web ; cette revue ne certifie ni leur couverture globale ni leur comportement navigateur | 18 vérifie les correspondances TEST ; 05 précise états, messages et reprise ; conserver PLANNED jusqu'à exécution probante |

## 2. Contexte navigateur et fixation — correction attendue de 04/03/05

Références exactes : GAP-01 tableau L1-CTX ; GAP-02 paragraphe initial ; GAP-04 deux login, cookies tardifs et dernier paragraphe sur amorçage. Backend a correctement signalé que la liaison reste une dépendance : cet avis confirme le blocage, il ne prétend pas découvrir une implémentation défectueuse.

**Contre-exemple documentaire à fermer :** deux onglets sans cookie lancent L1-CTX ; le serveur crée C1 et C2. Login A se lie à C1 ; login B à C2. Chaque contexte peut satisfaire séparément « au plus une session courante ». Si les réponses de création et de login arrivent dans un autre ordre, le cookie social A ou le contrôle C1 peuvent revenir après B. L'invalidation « même contexte » ne prouve alors pas à elle seule que A est invalide. Ce scénario est une déduction à tester, pas une exploitation observée.

Obligations de correction, sans imposer de tables ou de protocole :

- Identifier ce qui authentifie le contexte sur chaque route, distinguer référence publique, secret HttpOnly et génération ; aucune génération client ne crée une association.
- Définir création, réutilisation, changement d'identité, élévation, fin sociale, perte/reprise du contrôle et purge, avec instant d'effet et réponses en vol.
- Préciser si toute autorisation sociale exige cohérence session/contexte courant ; si oui, combinaison incohérente refuse ; si non, montrer le mécanisme équivalent empêchant une ancienne identité de redevenir autorisée.
- Examiner aussi le retour d'une paire ancienne cohérente, pas seulement deux cookies dépareillés. Le navigateur ne fournit pas un identifiant matériel fiable permettant d'assimiler arbitrairement deux contextes serveur à un appareil unique.
- Choisir mécanisme de convergence sûr, étape supplémentaire, ou restriction explicite du flux ; coordonner uniquement en JavaScript ne suffit pas. Ni IP ni empreinte intrusive de navigateur ne sont proposées comme solution implicite.
- Traiter contexte préauth fixé/copié, sous-domaines, doublons de noms de cookie et cookies invalides : pas de promotion du préauth en session réelle, ni élargissement de ses pouvoirs après login. Définir rotation/invalidation ou liaison renouvelée avec conservation strictement bornée des seuls reçus autorisés.
- Établir une matrice d'écriture des cookies : login, élévation, L1-CTX, récupération, logout, lecture, erreurs, proxy et middleware. L'interdiction doit porter sur l'effet HTTP réel, pas seulement sur le corps JSON. Une réponse abandonnée par fetch peut encore avoir des effets navigateur ; preuve par exécution requise.

Architecture doit proposer une primitive et ses hypothèses ; Sécurité revoit ce delta, Web précise l'issue visible. Si une solution fiable est trop complexe pour L1, proposer un profil plus simple avec reconnexion et limites explicites au HQ. Pas de modification silencieuse de la garantie « jamais retour à A ».

## 3. Idempotence et stockage perdu

Les invariants de challenge consommé et de compte unique sont nécessaires, mais ne suffisent pas à prouver la déduplication d'un envoi de récupération 006 lorsque son résultat K disparaît. La même requête dans un contexte vivant pourrait sinon être traitée comme nouvelle.

Correction minimale à faire choisir par 03/04 :

| Situation | Garantie à expliciter | Oracle à ajouter à L1-BE-02/11 |
| --- | --- | --- |
| Transaction K + mutation/outbox avant commit puis crash | Tout absent ou effet et reçu durables ; aucun effet externe non suivi avant commit | Un seul effet métier après reprise, pas de nouveau mail du seul replay |
| Commit réussi, cache K perdu, autorité disponible | Relire l'autorité, pas créer sur cache miss | Même reçu autorisé, aucune nouvelle intention |
| Autorité K réellement perdue dans contexte encore valide | Détecter la perte/mettre le contexte hors service ou disposer d'une admission durable ; sinon garantie impossible | Refus/réconciliation, jamais nouveau succès non dédupliqué |
| Purge normale | Fenêtre K couvre toutes les reprises autorisées ; contexte expiré refusé avant nouvelle création | Avant/à/après limite, pas de résurrection de clé |
| Livraison externe d'email après acceptation | Distinguer déduplication d'intention et garantie fournisseur ; outbox rejouée après résultat fournisseur inconnu | Aucun « livré une fois » promis sans primitive de déduplication vérifiable ; politique de reprise externe à documenter |

Empreinte des secrets : l'avis propose une MAC standard sous clé séparée et versionnée, avec domaine opération/schema/contexte ; cette recommandation reste à valider. Pas de password/challenge/K brut dans logs. Canonicalisation ne modifie pas le mot de passe ; champs secrets ne sont ni tronqués ni normalisés. Rotation des clés ne doit pas transformer un replay légitime en première exécution ; conserver la clé de vérification nécessaire dans une fenêtre approuvée ou refuser la reprise en cas de retrait. Ne pas conserver une clé compromise pour maintenir artificiellement la disponibilité.

## 4. Ordre autoritatif, expiration et récupération

Acceptation documentaire des intentions de GAP-04 : une récupération invalide l'ancien moyen et les sessions antérieures, une demande de récupération ne le fait pas, une session terminale ne repart pas, un ancien DTO ou cache ne donne pas de droit.

**Dépendance Architecture bloquante :** fournir un diagramme de séquence/ordre et une primitive de persistance pour les cas suivants ; pas seulement ajouter « atomique » à chaque ligne :

1. Lecture/vérification lente d'un password puis reset et commit du login : comparaison de la révision au point de commit, aucun accès ancien créé.
2. Régénération puis logout et ordre inverse : la portée logique révoquée couvre ses continuations ; nouvelle connexion indépendante suit sa propre génération.
3. Vérification de droit puis révocation/restriction avant commit métier : ordre commun défini, absence de fenêtre entre validation autoritative et mutation.
4. Attente/verrou faisant franchir expires_at : revalider la borne au point d'autorisation retenu ; opération autorisée avant expiration et committée après doit avoir une règle explicite, cohérente avec C6.
5. Crash après commit avant réponse : reçu durable consultable selon droits ; crash avant commit : pas de succès. Réplica retardé/cache ne peut infirmer une révocation confirmée.
6. Deux challenges de récupération différents émis sous la même ancienne révision : après premier succès, spécifier le sort du second et des anciennes preuves d'activation/récupération. La mention générique sujet/révision de GAP-02 doit devenir une règle testable.

Le mécanisme anti-retour arrière après restauration appartient à GAP-08 : la contrainte « aucune preuve ancienne réactivée » est acceptée, son implémentation n'est pas revue ici. Demander seulement à 03/04/14/15 l'interface de version/epoch nécessaire à L1 ; ne pas déclarer GAP-08 fermé ou exiger un réaudit du disaster recovery dans cette passe.

## 5. Reçu de logout et résultat incertain

Le modèle proposé est recevable sous conditions, sans approbation du mécanisme de contexte. Compléter la fiche API-BE-005, sans créer ici une route concurrente :

| Cas | Règle à conserver ou préciser |
| --- | --- |
| Première intention réellement reçue | Capturer la session logique avec credential valide, contexte/CSRF et génération ; K lié atomiquement à cet effet ; 204 après révocation durable |
| Première requête jamais reçue, reprise A encore valide | Même intention peut commencer seulement sous les mêmes preuves et génération ; changement B interdit avant résolution d'une nouvelle cible |
| Rejeu après succès | K déjà lié + preuve de contrôle + génération + CSRF/origine + fenêtre ; droit limité à ce résultat historique, pas au compte ; 204 sans corps |
| K inconnu après fin sociale | 401 ou refus contractuel ; ne pas reconstituer une liaison depuis le seul K, account_ref ou request_id |
| B connecté entre-temps | 409 AUTH_CONTEXT_CHANGED sans effet sur B ; aucune suppression/rotation de cookie sur réponse tardive A |
| Expiration de la session avant premier logout | Pas de reçu inventé d'une opération jamais committée ; API-BE-049 anonymous reste une observation |
| Fenêtre du reçu | Proposition : échéance calculée au premier effet durable, non glissante et indépendante des retries ; départ exact et interaction avec expiration/contrôle à ratifier |
| Panne de l'autorité | 503 ou résultat inconnu ; contenu privé masqué selon 05 ; pas de transformation en succès ni retour automatique à A |

Distinguer expiration du droit de replay et durée de conservation de sa preuve : la première est une borne opérationnelle, la seconde relève aussi de 15. Décrire comment un client obtient/vérifie sa preuve CSRF après fin sociale sans recréer un contrôle incompatible ni élargir l'accès. Toute réponse de reçu porte no-store et aucun Set-Cookie de contrôle ou social susceptible d'affecter une nouvelle connexion.

**Recommandation au HQ :** comparer le bénéfice de confirmation après perte de réponse à la complexité du second secret durable. L'alternative sans reçu reste recevable si l'incertitude est visible et si la procédure de reprise est décrite ; une lecture anonyme ne devient jamais une attestation de révocation de A. Le choix appartient à 03/04/05/14/15 avec HQ, pas à cet avis seul.

## 6. Avis sur les paramètres

Les valeurs numériques du Backend demeurent PROPOSÉES. Une durée de secret, de contexte, de cookie et de stockage ne doit pas être traitée comme la même horloge.

| Paramètre du delta | Avis sécurité / amendement précis | Responsable / effet |
| --- | --- | --- |
| IDLE 30 min / ABSOLUTE 12 h | Recevables pour étude sur membre ordinaire, pas validés. Définir activité autorisée, relecture après attente et risque de cookie volé ; pas de reset de durée absolue par polling/rotation | 04/05/14 ; bloque gel des bornes ; pas applicable aux opérateurs par défaut |
| Préauth 30 min | Garder borne non glissante ; préciser expiration lors passage à contrôle social et devenir des anciens reçus/challenges | 03/04/14/15 ; lié au blocage contexte |
| Challenge 15 min | Impossible d'évaluer résistance sans format/entropie, budget d'essais et réémission ; distinguer code saisissable et preuve aléatoire longue | 04/14, délivrabilité 05, conservation 15 |
| Reçu logout 10 min | Candidat à justifier par reprise utilisateur ; départ à fixer, jamais prolongé par polling ; invalidation à nouvelle génération | 04/05/14/15 ; pas autorisation d'un stockage indéfini |
| Timeout 10 s, 2 retries sur 30 s | Budget client, pas timeout transactionnel ni SLO. Respecter Retry-After sans dépasser budget/fenêtre ; pas de relance login ni K nouveau automatique | 03/04/05/14 ; distinguer annulation client et commit serveur |
| Secrets session/contrôle/CSRF et K | Fournir manifeste avec générateur cryptographique éprouvé, entropie, longueur encodée max, comparaison, représentation protégée et rotation. Proposition à examiner : secrets opaques de 32 octets aléatoires ; K non secret imprévisible avec au moins 128 bits. Ce ne sont pas des paramètres adoptés | 03/04/14 ; limites/validation/anti-abus nécessaires avant READY |
| Password et challenge à faible espace | Politique explicite, stockage spécialisé éprouvé avec coût benchmarké, bornes d'entrée ; budget d'essais atomique et limitation multi-dimensions, sans verrouillage arbitraire par tiers | 04/14/05 ; aucun seuil universel inventé |
| Quotas contextes, K, envois, hash jobs | Fixer cardinalité max, corps/header max, coût concurrent, maintien des compteurs après nouveau contexte/renvoi ; contexte seul ou IP seule insuffisants | 03/04/14 ; 09 seulement pour impact abus ; protège le store préauth |
| Horloge / CONTEXT_MAX_AGE | Autorité serveur, comportement décalage/recul horloge, bornes exactes et durée d'obsolescence d'affichage explicites ; autorisation serveur ne dépend jamais de fraîcheur DTO client | 03/04/05/14 ; 18 oracles temporels |
| Cookie client à borne absolue | Préciser effet d'une réponse tardive sur Expires/Max-Age ; ne pas déduire d'un Max-Age calculé avant délai réseau une égalité certaine avec la borne serveur | 04/05 ; autorité serveur refuse après expiration même si cookie persiste |

Les exigences de non-énumération doivent porter sur corps, statuts, headers, tailles, quotas et distribution temporelle sous environnement réel. Une attente fixe ou l'égalité d'un JSON n'est pas une preuve suffisante. Refus sur Origin:null/absent et origines proches doivent être testés ; un header d'origine n'authentifie pas un bot hors navigateur et ne remplace pas les preuves métier.

## 7. Compléments adverses proposés à QA/Web

Tous **PLANNED, non exécutés** ; correspondances indicatives à confirmer par 18, sans renumérotation des TEST existants.

| Critère Backend existant | Complément proposé par 14 | Résultat observable / preuve future |
| --- | --- | --- |
| L1-BE-01/02 | Réponse perdue, K en cache perdu vs autorité perdue, purge à borne, rotation clé MAC | Même reçu/effet ou refus défini ; jamais nouvelle consommation ni stockage de corps secret ; traces d'ordre transactionnel expurgées |
| L1-BE-03/04 | GET/HEAD/bootstrap et middleware, autorité retardée, attente franchissant idle/absolue | Pas de Set-Cookie social caché, pas de prolongation ; panne distincte d'anonyme, autorisation conforme à l'ordre choisi |
| L1-BE-05/08 | Deux contextes créés avant login ; retarder séparément cookie social et de contrôle, puis les deux, en plusieurs onglets | Jamais accès A après transition B selon garantie ratifiée ; perte explicite admissible ; headers réels et état serveur, pas uniquement assertions DOM |
| L1-BE-06 | Premier logout absent du serveur, expiré avant arrivée, rejoué après perte, K inconnu, contrôle perdu, ancienne réponse après B | 204 uniquement pour opération liée/effet prouvé ; pas de révocation/effacement B ; vérifier absence des deux types de Set-Cookie |
| L1-BE-07 | Login/élévation puis logout dans les deux ordres et crash aux points de commit | Pas de continuation valide après effet terminal ; pas de succès affiché depuis réponse ancienne |
| L1-BE-09 | Deux challenges différents sous ancienne révision, récupération concurrente login et changement de contexte | Politique d'invalidation appliquée une fois, sessions/credentials anciens interdits ; aucune sanction ou MFA levé |
| L1-BE-10 | Réutilisation après expiration/restauration et horloge contrôlée | Aucun retour de droit ; la preuve de restauration reste dépendante de GAP-08, pas prétendument fournie ici |
| L1-BE-11 | Origine absente/null/host voisin/sous-domaine, bootstrap sans CSRF préalable, types de requête simples et CSRF obsolète | Exception bootstrap étroite, aucune mutation métier inter-origines ; vérifications corps/statut/header/timing sans email réel |

Périmètre des preuves navigateur à convenir par 05/18 : navigateurs pris en charge, versions, transport réel TLS/cookies, ordre envoi/commit/livraison, multi-onglets et retour d'historique ; fixtures synthétiques et canaris de secrets. Une simulation unitaire des promesses fetch ne vérifie pas le traitement réel de Set-Cookie. Le contrôle des doublons d'email doit distinguer intention interne, outbox et fournisseur de test.

## 8. Dépendances et transmission au HQ

| Destinataire | Demande ciblée | Blocage / statut de transmission |
| --- | --- | --- |
| 04 Backend | Répondre point par point S14-L1-04/05/07/09/10/13/14/15/16 dans son delta propriétaire, préserver historique et statuts | Avant READY des routes dépendantes ; À TRANSMETTRE |
| 03 Architecture | Séquences/primitive pour contexte et générations, K durable/perte, ordre révocation/commit et clés MAC ; définir hypothèses et alternatives | Bloquant S14-L1-05/09/13 ; À TRANSMETTRE, avis NON REÇU |
| 05 Web | Matrice réelle d'écriture cookies, bootstrap/multi-onglets et issue de reconnexion ; vérifier conservation de l'intention sans secret en stockage persistant | Avant gel consommateur ; À TRANSMETTRE ; aucun avis UX attribué |
| 15 Privacy + 09 sur impact | Conservation des contextes/reçus et accès aux droits après restriction, selon leur mandat | Leur validation est hors présent avis ; À TRANSMETTRE |
| 18 QA | Reprendre les compléments du §7 dans les critères L1-BE/TEST existants avec résultats et preuves | Avant exécution/fermeture ; À TRANSMETTRE |
| HQ / 21 | Enregistrer avis 14 reçu lorsque transmission attestée ; conserver GAP-01…04 ouverts, faire revoir seulement les amendements ciblés | Publication ne prouve pas réception des discussions ; À TRANSMETTRE |

Le mandat de revue de cette discussion est REÇU par le message utilisateur ; l'avis est rédigé et publié par PR une fois le lien confirmé. Le statut initial « avis 14 non reçu » dans le document Backend est un état historique à actualiser par son propriétaire après réception, pas une contradiction à corriger ici.

## 9. Compte rendu en sept rubriques

1. **Décisions :** verdicts locaux émis ; invariants acceptés documentairement distingués des mesures à amender et des trois blocages S14-L1-05/09/13. Aucune adoption de transport, durée, permission ou primitive d'Architecture.
2. **Livrable :** présent avis v0.1 ; référence examinée exclusivement `1acf84fffcaa8131c0826d4874126e107a4cf978`. Nouvelle PR indépendante par son fichier et empilée sur la branche Backend pour conserver le contexte ; SHA de publication dans la description de PR.
3. **Tests exécutés :** relecture ciblée et contrôles documentaires uniquement, commandes/résultats réellement observés consignés dans la PR. Aucun test applicatif, navigateur, CSRF, récupération, charge ou restauration exécuté ; propositions §7 PLANNED.
4. **Questions :** mécanisme de liaison face à deux contextes, historique K perdu, ordre autoritatif, preuves recovery anciennes, utilité du reçu et paramètres ; destinataires §8.
5. **Dépendances :** 03/04/05/15/09/18/HQ/21 sur seuls deltas ; transmissions À TRANSMETTRE tant qu'envoi non attesté.
6. **Risques :** réapparition d'une ancienne identité, mutation après retrait de droit, nouvel effet après perte K, preuve de récupération ancienne réutilisable ; scénarios documentaires, pas failles runtime démontrées.
7. **Suite / HQ :** obtenir réponses 03/04, confronter avec avis 05/15/18, revoir uniquement les corrections, puis HQ arbitre et 21 contrôle la convergence. Conserver L1 BLOQUÉ POUR CODE ; aucune fusion ni GO pilote dans cette contribution.

## Appuis techniques limités

Sources primaires consultées le 30 septembre 2026 pour les principes, pas pour certifier le protocole propriétaire ni prescrire les paramètres proposés :

- [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) : défense des mutations, login CSRF et séparation pré-session/session.
- [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) : credential serveur, renouvellement aux transitions et expiration.
- [OWASP Forgot Password](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html) : preuve de récupération bornée et à usage unique.
- [MDN Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie) : effet navigateur du header, inaccessibilité au JavaScript frontend et attributs d'expiration.

Les contre-exemples, amendements, critères et verdicts sont l'analyse de l'équipe 14 sur le delta cité.
