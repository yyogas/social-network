# Contrats API candidats — Backend M0

## Identification et statut

| Champ | Valeur |
| --- | --- |
| Objectif | Définir les ressources, opérations et invariants nécessaires pour décider puis spécifier le pilote. |
| Propriétaire | 04 — Backend / API ; aucun reviewer humain GitHub désigné. |
| Destinataires | 00, 01, 02, 03, 05, 06, 08, 09, 10, 13, 14, 15, 16, 17, 18, 20, 21 selon dépendance. |
| Date / révision | 29 septembre 2026 ; version documentaire 0.1 ; référence d'entrée `dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957`. |
| Mandat | M0-TEAM-04 dans les [ordres de travail](../teams/work-orders.md), [PR HQ nº 2](https://github.com/yyogas/social-network/pull/2). |
| Références | [Plan documentaire](../documentation-plan.md), [modèle](../teams/deliverable-template.md), [vision](../product/product-vision.md), [catalogue](../product/feature-catalog.md), [parcours](../product/user-journeys.md), [gouvernance](../governance.md), [registre](../project-governance/decision-register.md). |
| Statut | **PROPOSÉ** ; approbations spécialisées **NON REÇUES** ; aucune implémentation, migration ou validation applicative. |
| Phase / priorité | MVP candidat, P0 pour accès, publication, modération et droits sur les données ; interactions et notifications P1 selon catalogue. Phases ultérieures inventoriées seulement. |
| Limites | Contrats conceptuels, sans DDL, ORM, code serveur, OpenAPI exécutable, politique juridique ou permissions définitivement approuvées. |

**CONFIRMÉ :** mandat de rédaction, GitHub comme référence, lecture des documents ci-dessus à la révision indiquée, responsabilité Backend du modèle applicatif. TypeScript/NestJS/PostgreSQL/Redis sont la stack envisagée dans le mandat reçu ; cette pièce n'en prononce pas l'approbation architecturale.

**PROPOSÉ :** toutes les routes, schémas, états, limites et politiques techniques ci-dessous. **À VÉRIFIER :** visibilité, effets précis du blocage, âge, sessions, durée des liens, rétention, capacité pilote. **NON REÇU :** décisions DEC-0001/DEC-0002 approuvées, matrice de permissions, avis consommateurs et résultats applicatifs. Le dépôt et sa CI documentaire existent ; l'ancien statut « repository non reçu » de notre brouillon de conversation n'est plus applicable.

## Besoin, fonctionnalités et parcours

Une personne doit pouvoir rejoindre le pilote, publier pour une audience compréhensible, lire le fil, interagir et exercer ses contrôles ; un agent habilité doit pouvoir traiter un abus et un recours sans disposer de pouvoirs globaux implicites. La réalisation doit rester compatible avec les clients web/mobile et leur reprise après erreur réseau.

### Classement et correspondance des travaux existants

Les FEAT existants constituent l'identité canonique des fonctionnalités. Les anciens BE-01…BE-19 et M0-API-01…10 étaient des repères locaux de conversation ; ils ne créent pas de second catalogue. Cette synthèse intègre leurs éléments utiles et corrige les écarts ci-dessous. Les anciens fichiers autonomes restent des brouillons historiques, pas une autre autorité d'implémentation.

| FEAT | Contribution Backend / résultat attendu | Classe et priorité proposées | Préconditions / parcours |
| --- | --- | --- | --- |
| FEAT-001, FEAT-002 | Compte unique, activation, accès, sessions, récupération et révocation | MVP P0 | J01 ; âge, identité, mode de session validés par 01/14/15. |
| FEAT-003, FEAT-004 | Profil public filtré, paramètres privés, audience et contrôle objet | MVP P0 | J01/J02/J06 ; défauts et audiences décidés. |
| FEAT-005 | Follow idempotent, consultation des relations autorisées | MVP P0 | J03 ; compte privé et acceptation éventuelle à arbitrer. |
| FEAT-006, FEAT-007 | Texte, image contrôlée, texte alternatif, édition et retrait | MVP P0 | J02 ; limites et contrat média 08, politique de modification 01/09. |
| FEAT-008 | Fil chronologique stable et borné | MVP P0 | J03 ; règles d'éligibilité et ordre fixés avec 01/03. |
| FEAT-009, FEAT-010 | Réaction sans doublon, commentaire et retrait | MVP P1 | J03 ; visibilité et sanctions communes. |
| FEAT-011, FEAT-022 | Notifications essentielles, préférences, fin de page explicite | MVP P1 | J03 ; catégories facultatives/obligatoires et repère de lecture 01/02/15. |
| FEAT-012, FEAT-013 | Blocage et reçu de signalement, identité du signalant protégée | MVP P0 | J04 ; matrice de blocage et preuve admissible 09/15. |
| FEAT-014, FEAT-015, FEAT-017 | Dossiers, décision, effet réel, notification et recours distincts | MVP P0 | J05 ; habilitations, motifs, indépendance et limites 09/10/14/15. |
| FEAT-016 | Demande d'export/suppression, état de traitement et accès sécurisé | MVP P0 | J06 ; cycle approuvé par 15 ; ne pas utiliser un GET pour déclencher un export. |
| FEAT-018 | Erreurs et réponses consommables par le web accessible | MVP P0 | 02/05 ; le Backend ne choisit pas la surface de lancement. |
| FEAT-019 | Événements minimisés, mesures opérationnelles distinctes de l'analytics | MVP P1 | 13/14/15 ; aucune collecte produit implicite via les logs. |
| FEAT-020 | Adhésion et droits communautaires conditionnels | MVP P1, **INCLUSION À ARBITRER** | J07, OPEN-003 ; pas de bascule silencieuse en Phase 2. |
| FEAT-021 | Langue du contenu et codes d'erreur stables, champs Unicode | MVP P0 | 16/02 ; langues et écritures effectivement supportées à décider. |
| FEAT-023 à FEAT-028 | Recherche, messages, mobile, vidéo, créateurs, business | Phase 2 P1/P2 selon catalogue | Contrats différés ; IDs, états et accès extensibles sans nouveau runtime en M0. |
| FEAT-029 à FEAT-031 | Recommandation, publicité, rémunération | Phase 3 P2 | 07/11/12/13/15 ; aucune donnée de ciblage ni ledger financier créé ici. |
| FEAT-032 | Ouverture de nouveaux marchés | International P1 | 16/15 ; séparer résidence, pays légal, communauté, origine et langues. |
| FEAT-033, FEAT-034 | Live et intégrations développeurs | Long terme P3 | Architecture, médias, sécurité ; scopes et quotas publics avant ouverture. |

Le module historique BE-12 « événements » désigne des événements organisés (calendrier/participation), distincts des messages techniques EVT-BE. Absent des 34 FEAT du catalogue HQ : **Phase 2 P2 proposée, À VÉRIFIER avec 01/HQ**, sans attribuer un FEAT concurrent. Valeur attendue : organiser une rencontre ; dépendances : visibilité, modération, fuseaux et capacité. Avant contrat : décider invitations, annulation et liste des participants ; acceptation future : deux inscriptions concurrentes à la dernière place ne dépassent pas la capacité et un tiers ne voit pas les invités privés. Aucun endpoint événement organisé dans ce lot.

### Delta et contradictions à soumettre au HQ

| Références | Constat | Traitement proposé / blocage |
| --- | --- | --- |
| Ancien M0 : communautés Phase 2 recommandée ; catalogue FEAT-020 / OPEN-003 | Différence de classement proposé | Conserver FEAT-020 MVP conditionnel ; recommandation follow seul reste une option. HQ/01/09/19 arbitrent. |
| Ancien M0 : notifications à vérifier ; FEAT-011/022 | Couverture insuffisante | Documenter notifications/préférences MVP candidates sans imposer catégories, canal push ou suivi comportemental. |
| Ancien registre : `GET /me/export` ; FEAT-016 / J06 | Risque de déclencher une opération avec GET ; cycle incomplet | Proposer demande par POST, suivi par GET, téléchargement autorisé séparément. 15 valide le contenu et le cycle. |
| Ancien registre : blocage/retrait « immédiat » ; J02/J04 | Promesse excessive pour URL déjà signée, cache et copie téléchargée | Définir le point de prise d'effet API et le délai maximal média. Aucune garantie de retrait d'une copie déjà reçue. Bloque le contrat média de contenu restreint. |
| Ancien registre : erreur globale `ACCOUNT_SUSPENDED` ; J05/J06 | Risque de rendre recours et droits sur les données inaccessibles | Refuser les actions sociales suspendues, préserver un accès restreint aux décisions, recours et demandes privacy après authentification appropriée ; 09/14/15 arbitrent. |

## Permissions, données et contrats

### Règles communes et paramètres ouverts

Toutes les opérations héritent des règles C1 à C8 ; chaque ligne précise ses différences. `/api/v1` est le préfixe candidat pour les routes ci-dessous, y compris `/admin/...`. La version documentaire 0.1 n'est pas une release d'API.

- **C1 — Identité :** codes acteurs V = visiteur ; U = utilisateur authentifié ; P = propriétaire ; O = opérateur interne habilité. Une session suspendue peut conserver les seuls droits de recours/privacy approuvés. Cookie sécurisé/CSRF ou jeton mobile, MFA interne, rotation, durée et révocation dépendent de 14/03/05/06. Aucun token dans URL ou logs. Un ID opaque n'est jamais une autorisation.
- **C2 — Validation :** schéma d'entrée fermé, champs inconnus rejetés, IDs et enums validés, timestamps UTC ; champs absents dans PATCH inchangés, null autorisé seulement si documenté ; texte traité comme donnée et rendu sans exécution par les clients. Les maxima sont des paramètres nommés à approuver, pas des durées légales inventées. Toute route appelle les validations d'accès avant de retourner ses données.
- **C3 — Erreurs :** forme candidate `{code,message_key,request_id,field_errors?}` sans détails privés. 400 invalide, 401 authentification nécessaire, 403 action interdite sur ressource connue, 404 absent ou masqué, 409 conflit/idempotence, 412 version périmée, 422 état/règle incompatible, 429 quota avec `Retry-After`, 503 dépendance indisponible. Aucun message de récupération ne confirme l'existence du compte. Les clients traduisent `message_key` et associent `field_errors` aux champs sans dépendre du texte libre.
- **C4 — Temps et reprise :** `API_REQUEST_TIMEOUT`, `JOB_DEADLINE`, `MAX_RETRIES` et backoff/jitter à fixer par 03/14 avec 05/06 avant READY. Timeout ne signifie pas rollback assuré. GET rejouable ; PUT/DELETE rejouables si sémantique stable ; POST marqué K exige `Idempotency-Key` avant émission et conserve la même clé lors d'une reprise. Réseau incertain/429/503 : backoff borné puis suivi de la ressource/opération ; pas de retry automatique des autres 4xx. Client montre « état inconnu/en cours » tant que le résultat n'est pas confirmé.
- **C5 — Idempotence/concurrence :** K = clé portée par acteur + opération + empreinte canonique d'entrée ; même clé/entrée retourne la référence du résultat, entrée différente 409. Réautoriser chaque reprise, y compris la réponse mémorisée ; ne pas servir un ancien corps devenu privé. Clé et mutation sont atomiques ; concurrence en cours renvoie un état défini ou 409 avec reprise. `IDEMPOTENCY_WINDOW` et expiration à fixer. Après expiration, l'absence de doublon n'est pas garantie : les clients réconcilient avant une nouvelle création. Vn = `If-Match`/version requise ; absence 428, périmée 412 ; contraintes uniques et transaction pour éviter les courses.
- **C6 — Accès/cache :** contrôler acteur, état de compte, audience, relations, blocages, modération et portée interne au point d'autorisation de l'opération. Une écriture concurrente avec blocage/retrait doit être ordonnée explicitement par une transaction/verrou ou mécanisme équivalent à valider par 03 ; un contrôle avant transaction ne suffit pas. Après confirmation d'un changement, les nouvelles autorisations utilisent le nouvel état. Réponse déjà envoyée non récupérable. Cache privé `no-store` HTTP proposé ; Redis dérivé, jamais seule source de vérité pour un droit révoqué. En absence de contrôle autoritatif, refuser l'accès protégé. Les lectures anonymes restent conditionnelles à OPEN-007.
- **C7 — Corrélation :** `request_id` généré/validé côté serveur, contexte d'acteur filtré, code/latence ; audit séparé des logs techniques pour lecture de preuves et mutations sensibles. Écriture métier + événement dans une transaction via mécanisme candidat outbox. Aucun secret, corps privé, note de signalement ou URL signée dans les logs. Corrélation conservée lors d'une reprise sans réutiliser les tokens comme identifiant.
- **C8 — Compatibilité :** futurs schémas OpenAPI dérivés de ces contrats après arbitrage ; requêtes strictes, clients tolérant champs de réponse additionnels ; ajout d'enum à analyser avec consommateurs, changement cassant via version ou migration explicitement approuvée. Conditions de dépréciation à définir avant clients externes. CI future compare les contrats et génère tests ; non implémenté ici.

| Paramètre ouvert | Propriétaires | Conséquence tant que non fixé |
| --- | --- | --- |
| `PAGE_DEFAULT`, `PAGE_MAX`, `CURSOR_TTL`, `FEED_SCAN_BUDGET` | 01/03/04/05/06 | Contrat exact de pagination non READY. |
| `TEXT_MAX`, `COMMENT_MAX`, `ALT_TEXT_MAX`, profondeur de réponses | 01/02/09/16 | Validation de texte et accessibilité à confirmer. |
| `UPLOAD_BYTES_MAX`, pixels, formats, quota stockage, durée upload et retrait CDN | 08/14/15 | Publication image et lecture restreinte non READY. |
| Rate limits par compte/IP/session/route, quota par lot, anti-abus et mode panne | 09/14/04 | Pas de seuil arbitraire approuvé ; risque de surcharge et d'injustice NAT à mesurer. |
| Durée sessions, clés K, export et purge, recours, archives et sauvegardes | 14/15/09 selon objet | Contrats dépendants bloqués ; aucune durée légale déduite. |

**Précisions de reprise à valider (03/14) :** sur les routes anonymes marquées K, une clé fournie par le client ne constitue ni identité ni preuve. Définir une portée de transaction pré-authentification liée au challenge/contexte vérifié ; aucune réponse privée mémorisée accessible par clé seule. Activation/récupération : le rejeu authentifié de la même transaction retourne son reçu neutre ; une nouvelle transaction utilisant un challenge consommé est refusée. L’empreinte d’entrée ne conserve pas les secrets en clair. Pour DELETE avec Vn, un tombstone propre permet de reconnaître un retrait déjà effectué sans révéler l’objet à un tiers ; 204 après revalidation, sinon refus selon C3. Contrats non READY tant que portée, durée et preuve de reprise ne sont pas fixées.

### Matrice d'autorisation candidate

Les verbes de cette matrice désignent des permissions conceptuelles à revoir avec 09/10/14/15, pas des rôles runtime déjà accordés.

| Acteur / ressource | Lecture | Mutation / refus attendu |
| --- | --- | --- |
| V, profil/publication | Seulement si une audience anonyme est retenue ; aucun privé | Aucune mutation sociale ; 401. |
| U, objet d'un autre | Audience ET état ET blocage ; parents compris | Pas d'édition/suppression ; 403 ou 404 cohérent avec masquage. |
| P, profil/post/commentaire | Données propres autorisées ; retrait de modération distinct d'un accès public | Modification selon état et version ; ne restaure pas lui-même un objet modéré. |
| Utilisateur bloqué | Selon portée décidée par 09/01 ; appliquer la même règle aux médias/listes/aperçus | Interactions interdites refusées ; pas de notification révélant l'identité du bloqueur. |
| Compte suspendu | Espace limité décisions/recours/privacy proposé | Publication/follow/interactions refusés ; pas de suppression de preuve réservée. |
| O, dossier | Permission `case.read`, portée et nécessité ; preuve via `evidence.read` distincte | `decision.apply` et `appeal.resolve` distincts, motif/version ; révocation vérifiée à chaque action. |
| O, export personnel | Aucun accès automatique au téléchargement utilisateur | Assistance limitée à son mandat ; aucune usurpation implicite. |
| Responsable communauté éventuelle | Seulement sa communauté et ressources expressément déléguées | Aucun pouvoir global, ni accès automatique aux preuves ou données de compte. |

### Schémas conceptuels et exemples synthétiques

Notation : `Id` = chaîne opaque dont format final est ouvert ; `Version` = révision optimiste ; `State/Code` = enum versionné. Les objets ci-dessous définissent les sorties des opérations ; exemples `*_demo` entièrement fictifs. Les noms d'audience restent `audience_code` issu de la politique à approuver, sans valeur publique par défaut.

| Type | Schéma conceptuel minimal / exemple |
| --- | --- |
| AccountReceipt | `{registration_id:Id,state:State}` ; `{"registration_id":"reg_demo","state":"pending_verification"}`. Réponse externe uniforme si nécessaire contre l'énumération. |
| SessionResult | `{session_id:Id,account_state:State,allowed_capabilities:Code[]}` ; `{"session_id":"ses_demo","account_state":"active","allowed_capabilities":["social.read"]}` ; transport de credential séparé selon 14. |
| Profile | `{id:Id,display_name:string,bio?:string,avatar?:MediaRef,version:Version}` ; `{"id":"user_demo","display_name":"Membre exemple","version":1}`. Email absent. |
| Settings | `{visibility_policy:Code,notification_preferences:object,locale:Code,version:Version}` ; structure des préférences approuvée avec 01/15/16. |
| FollowState | `{target_id:Id,state:State}` ; `{"target_id":"user_demo","state":"following"}` ou pending si comptes privés retenus. |
| MediaRef | `{id:Id,state:State,alt_text?:string}` ; `{"id":"media_demo","state":"ready","alt_text":"Illustration fictive"}`. Accès fichier via grant séparé, jamais URL publique permanente présumée. |
| UploadReceipt | `{id:Id,state:State,upload_grant:opaque,expires_at:timestamp}` ; grant opaque fictif `upload_grant_demo`, lié à un objet et aux limites, non journalisé. |
| Post | `{id:Id,author:Profile,body:string,media:MediaRef[],audience_code:Code,state:State,published_at:timestamp,version:Version}` ; exemple contenu `"Texte exemple"`. |
| Comment | `{id:Id,post_id:Id,author_id:Id,body:string,state:State,version:Version}` ; `{"id":"comment_demo","post_id":"post_demo","author_id":"user_demo","body":"Réponse exemple","state":"visible","version":1}`. |
| Page<T> | `{items:T[],next_cursor:string|null,has_more:boolean}` ; `{"items":[],"next_cursor":null,"has_more":false}`. Pas de total non autorisé ; vide est succès. |
| Notification | `{id:Id,kind:Code,target_id?:Id,read:boolean}` ; `{"id":"notif_demo","kind":"decision_available","read":false}` ; aperçu revalidé, aucune preuve privée. |
| CaseReceipt | `{report_id:Id,receipt_ref:Id,state:State}` ; `{"report_id":"report_demo","receipt_ref":"receipt_demo","state":"received"}`. Pas d'identité d'enquêteur ou d'autres signalants. |
| Decision | `{id:Id,target_ref:Id,reason_code:Code,effect_state:State,notice_state:State,appeal_eligibility:Code,version:Version}` ; champs destinataire filtrés distincts du dossier interne. |
| Appeal | `{id:Id,decision_id:Id,state:State,outcome?:Code,version:Version}` ; `{"id":"appeal_demo","decision_id":"decision_demo","state":"submitted","version":1}`. |
| PrivacyJob | `{id:Id,kind:Code,state:State,created_at:timestamp,next_action?:Code}` ; `{"id":"job_demo","kind":"export","state":"queued","created_at":"2026-09-29T12:00:00Z"}`. Export/liste de catégories à valider avec 15. |
| DownloadGrant | `{grant:opaque,expires_at:timestamp}` ; exemple `grant_demo` ; identité et droits revalidés à la délivrance et selon mode retenu au téléchargement. |

### Catalogue d'opérations

**Producteur pour chaque ligne :** service Backend/API (04), domaine nommé dans la première colonne. 08 produit les résultats de traitement média ; 04 expose leur état aux clients sans refaire leur décision de validation. **Consommateurs :** W=05 Web, M=06 Mobile (contrats anticipés, pas inclusion MVP native), A=10 Admin. `∅` = aucune entrée/corps ; paramètres de chemin font partie de l'entrée. Toutes les sorties sont un exemple d'instance du type nommé ci-dessus, complété par les valeurs fictives de la ligne. Erreurs C3 s'appliquent à toutes les lignes ; la colonne erreurs précise les refus métier. Chaque ID API-BE est une opération candidate version 1, et non un identifiant FEAT.

| ID / domaine, FEAT | Méthode et chemin ; consommateurs | Entrée d'exemple → sortie conceptuelle, succès | Acteur, règle / reprise | Erreurs métier ; critère |
| --- | --- | --- | --- | --- |
| API-BE-001 Auth, FEAT-001 | POST /auth/registrations ; W/M | `{identity:"member@example.invalid",locale:"fr",registration_proof:"proof_demo"}` → AccountReceipt, 202 | V ; méthode d'identité/proof à fixer ; K | ADMISSION_UNRESOLVED, RATE_LIMITED ; AC-BE-01 |
| API-BE-002 Auth, FEAT-001 | POST /auth/activations ; W/M | `{challenge:"challenge_demo"}` → AccountReceipt avec state active, 200 | V avec preuve liée et à usage unique ; K | CHALLENGE_EXPIRED, CHALLENGE_CONSUMED ; AC-BE-01 |
| API-BE-003 Auth, FEAT-002 | POST /auth/sessions ; W/M | `{identity:"member@example.invalid",credential_proof:"proof_demo"}` → SessionResult, 201 | V ; preuve définie par 14 ; pas de retry aveugle d'une connexion | AUTH_INVALID, RATE_LIMITED ; AC-BE-02 |
| API-BE-004 Auth, FEAT-002 | POST /auth/session-refresh ; W/M | `{refresh_proof:"proof_demo"}` → SessionResult, 200 | Session avec preuve ; rotation/rejeu et perte de réponse à résoudre avec 14 ; contrat non READY | SESSION_REVOKED, REFRESH_REPLAY ; AC-BE-02 |
| API-BE-005 Auth, FEAT-002 | DELETE /auth/sessions/current ; W/M | ∅ → ∅, 204 | P ; révocation, repeat sans effet supplémentaire | AUTH_REQUIRED ; AC-BE-02 |
| API-BE-006 Auth, FEAT-002 | POST /auth/recovery-requests ; W/M | `{identity:"member@example.invalid"}` → `{state:"accepted"}`, 202 | V ; réponse neutre et timing contrôlé ; K, anti-abus | RATE_LIMITED ; AC-BE-02 |
| API-BE-007 Auth, FEAT-002 | POST /auth/recoveries ; W/M | `{challenge:"challenge_demo",replacement_proof:"proof_demo"}` → `{state:"completed"}`, 200 | Preuve vérifiée à usage unique ; K ; politique de révocation des sessions à valider | CHALLENGE_EXPIRED ; AC-BE-02 |
| API-BE-008 Profil, FEAT-003 | GET /profiles/{user_demo} ; W/M | ∅ → Profile, 200 | U ou V autorisé ; C6 | RESOURCE_UNAVAILABLE ; AC-BE-03 |
| API-BE-009 Profil, FEAT-003 | PATCH /me/profile ; W/M | `{display_name:"Membre exemple",bio:"Présentation fictive",avatar_id:null}` → Profile, 200 | P ; Vn ; avatar ready/autorisé, champs facultatifs | VALIDATION_FAILED, MEDIA_NOT_READY ; AC-BE-03 |
| API-BE-010 Paramètres, FEAT-004/021 | GET /me/settings ; W/M | ∅ → Settings, 200 | P ; données jamais publiques | AUTH_REQUIRED ; AC-BE-03 |
| API-BE-011 Paramètres, FEAT-004/021 | PATCH /me/settings ; W/M | `{locale:"fr",visibility_policy:"policy_demo"}` → Settings, 200 | P ; Vn ; langue/politique dans liste approuvée | POLICY_INVALID ; AC-BE-04 |
| API-BE-012 Graphe, FEAT-005 | PUT /users/{user_demo}/follow ; W/M | ∅ → FollowState, 200 | U ; ni soi ni relation interdite ; unique paire | FOLLOW_FORBIDDEN ; AC-BE-05 |
| API-BE-013 Graphe, FEAT-005 | DELETE /users/{user_demo}/follow ; W/M | ∅ → ∅, 204 | U ; retrait sans double effet | TARGET_UNAVAILABLE ; AC-BE-05 |
| API-BE-014 Graphe, FEAT-005 | GET /users/{user_demo}/follows?direction=followers ; W/M | `{cursor:null,limit:PAGE_DEFAULT}` → Page<Profile>, 200 | Lecteur autorisé sur liste et chaque profil ; direction enum | CURSOR_INVALID ; AC-BE-05 |
| API-BE-015 Média, FEAT-007 | POST /media/uploads ; W/M | `{mime_type:"image/png",size_bytes:2048,checksum:"checksum_demo"}` → UploadReceipt, 201 | P ; K ; limites 08, pas d'URL fournie par utilisateur à importer | UPLOAD_LIMIT, FORMAT_INVALID ; AC-BE-06 |
| API-BE-016 Média, FEAT-007 | POST /media/uploads/{upload_demo}/complete ; W/M | `{checksum:"checksum_demo"}` → MediaRef state processing, 202 | P ; K ; vérifier objet réel, taille et checksum serveur | UPLOAD_EXPIRED, CONTENT_MISMATCH ; AC-BE-06 |
| API-BE-017 Média, FEAT-007 | GET /media/{media_demo} ; W/M | ∅ → MediaRef, 200 | P ou lecteur de ressource liée autorisé | RESOURCE_UNAVAILABLE ; AC-BE-06 |
| API-BE-018 Média, FEAT-004/007 | POST /media/{media_demo}/access-grants ; W/M | `{context_type:"post",context_id:"post_demo"}` → DownloadGrant, 200 | U/V si retenu ; relation média/contexte vérifiée, K et C6 réappliqués | MEDIA_FORBIDDEN, MEDIA_NOT_READY ; AC-BE-04 |
| API-BE-019 Posts, FEAT-006/007 | POST /posts ; W/M | `{body:"Texte exemple",media:[{id:"media_demo",alt_text:"Illustration fictive"}],audience_code:"policy_demo"}` → Post, 201 | U autorisé ; K ; tous médias prêts et propriétaire/usage autorisés | MEDIA_NOT_READY, AUDIENCE_INVALID ; AC-BE-07 |
| API-BE-020 Posts, FEAT-004/006 | GET /posts/{post_demo} ; W/M | ∅ → Post, 200 | C6 pour texte et chaque média | RESOURCE_UNAVAILABLE ; AC-BE-04 |
| API-BE-021 Posts, FEAT-006 | PATCH /posts/{post_demo} ; W/M | `{body:"Texte corrigé",audience_code:"policy_demo"}` → Post, 200 | P ; Vn ; changement audience/texte réévalué, pas de restauration d'un retrait modération | POST_NOT_EDITABLE ; AC-BE-07 |
| API-BE-022 Posts, FEAT-006 | DELETE /posts/{post_demo} ; W/M | ∅ → ∅, 204 | P ; Vn pour première mutation ; répéter un retrait propre sans effet, selon authentification préservée | VERSION_CONFLICT ; AC-BE-04 |
| API-BE-023 Fil, FEAT-008/022 | GET /feed ; W/M | `{cursor:null,limit:PAGE_DEFAULT}` → Page<Post>, 200 | U ; filtres courants ; C6 | CURSOR_INVALID, TEMPORARILY_UNAVAILABLE ; AC-BE-08 |
| API-BE-024 Fil, FEAT-003/006 | GET /users/{user_demo}/posts ; W/M | `{cursor:null,limit:PAGE_DEFAULT}` → Page<Post>, 200 | Lecteur autorisé ; pas d'accès via liste à un détail refusé | CURSOR_INVALID ; AC-BE-08 |
| API-BE-025 Réaction, FEAT-009 | PUT /posts/{post_demo}/reactions/{kind_demo} ; W/M | ∅ → `{active:true}`, 200 | U ; cible accessible ; enum approuvé, unique acteur/cible/type | REACTION_INVALID, TARGET_UNAVAILABLE ; AC-BE-09 |
| API-BE-026 Réaction, FEAT-009 | DELETE /posts/{post_demo}/reactions/{kind_demo} ; W/M | ∅ → ∅, 204 | P de réaction ; suppression n'accorde aucune lecture du contenu | TARGET_UNAVAILABLE ; AC-BE-09 |
| API-BE-027 Commentaire, FEAT-010 | POST /posts/{post_demo}/comments ; W/M | `{body:"Réponse exemple"}` → Comment, 201 | U ; K ; accès cible contrôlé avec mutation | COMMENTS_CLOSED, TARGET_UNAVAILABLE ; AC-BE-09 |
| API-BE-028 Commentaire, FEAT-010 | GET /posts/{post_demo}/comments ; W/M | `{cursor:null,limit:PAGE_DEFAULT}` → Page<Comment>, 200 | Lecteur autorisé sur parent et enfant | CURSOR_INVALID ; AC-BE-09 |
| API-BE-029 Commentaire, FEAT-010 | PATCH /comments/{comment_demo} ; W/M | `{body:"Réponse corrigée"}` → Comment, 200 | P ; Vn ; conditions éditoriales approuvées | COMMENT_NOT_EDITABLE ; AC-BE-09 |
| API-BE-030 Commentaire, FEAT-010 | DELETE /comments/{comment_demo} ; W/M | ∅ → ∅, 204 | P ; Vn première mutation ; repeat sans effet | VERSION_CONFLICT ; AC-BE-09 |
| API-BE-031 Notification, FEAT-011 | GET /me/notifications ; W/M | `{cursor:null,limit:PAGE_DEFAULT}` → Page<Notification>, 200 | P ; revalider aperçu/cible, reçu de décision dédié | CURSOR_INVALID ; AC-BE-10 |
| API-BE-032 Notification, FEAT-011 | PUT /me/notifications/{notif_demo}/read ; W/M | `{read:true}` → Notification, 200 | P ; idempotent | RESOURCE_UNAVAILABLE ; AC-BE-10 |
| API-BE-033 Notification, FEAT-011/022 | PATCH /me/notification-preferences ; W/M | `{category_demo:false}` → préférences/version, 200 | P ; Vn ; catégorie désactivable approuvée, ne pas supposer décisions réglementaires facultatives | CATEGORY_NOT_CONFIGURABLE ; AC-BE-10 |
| API-BE-034 Blocage, FEAT-012 | PUT /me/blocks/{user_demo} ; W/M | ∅ → `{blocked:true}`, 200 | U ; interdiction self, état unique, C6 | SELF_BLOCK ; AC-BE-11 |
| API-BE-035 Blocage, FEAT-012 | DELETE /me/blocks/{user_demo} ; W/M | ∅ → ∅, 204 | P ; ne restaure pas implicitement follow/commentaires | AUTH_REQUIRED ; AC-BE-11 |
| API-BE-036 Safety, FEAT-013 | POST /reports ; W/M | `{target_type:"post",target_id:"post_demo",reason_code:"reason_demo",note:"Signalement fictif"}` → CaseReceipt, 202 | U ; K ; cible supprimée/blocage : règle de recevabilité 09/15 à fixer, aucune exigence de lecture sociale pour fermer un abus | REPORT_INVALID, REPORT_LIMIT ; AC-BE-12 |
| API-BE-037 Safety, FEAT-014/015 | GET /me/moderation-decisions ; W/M | `{cursor:null,limit:PAGE_DEFAULT}` → Page<Decision>, 200 | P visé, y compris accès restreint candidat ; masquer sources privées | CURSOR_INVALID ; AC-BE-13 |
| API-BE-038 Safety, FEAT-015 | POST /me/appeals ; W/M | `{decision_id:"decision_demo",statement:"Contestation fictive"}` → Appeal, 202 | P éligible ; K ; unicité du recours actif selon règle 09 | APPEAL_NOT_ALLOWED, APPEAL_DUPLICATE ; AC-BE-13 |
| API-BE-039 Safety, FEAT-015 | GET /me/appeals/{appeal_demo} ; W/M | ∅ → Appeal, 200 | P ; pas d'éléments d'enquête privés | RESOURCE_UNAVAILABLE ; AC-BE-13 |
| API-BE-040 Admin, FEAT-014/017 | GET /admin/moderation/cases ; A | `{cursor:null,limit:PAGE_DEFAULT}` → Page de dossiers filtrés `{id:"case_demo",state:"open",version:1}`, 200 | O case.read et portée ; pas de bulk export implicite | SCOPE_DENIED ; AC-BE-14 |
| API-BE-041 Admin, FEAT-014/017 | GET /admin/moderation/cases/{case_demo} ; A | ∅ → dossier filtré/version, 200 | O case.read ; evidence.read distinct pour preuve, audit lecture sensible | SCOPE_DENIED ; AC-BE-14 |
| API-BE-042 Admin, FEAT-014/017 | POST /admin/moderation/cases/{case_demo}/decisions ; A | `{action_code:"action_demo",reason_code:"reason_demo"}` → Decision avec effect_state pending, 202 | O decision.apply ; K + Vn ; effet ciblé, motif requis | ACTION_FORBIDDEN, CASE_CONFLICT ; AC-BE-14 |
| API-BE-043 Admin, FEAT-015/017 | POST /admin/appeals/{appeal_demo}/resolutions ; A | `{outcome:"overturn",reason_code:"reason_demo"}` → Appeal state resolving, 202 | O appeal.resolve ; K + Vn ; indépendance selon 09/15 | REVIEW_CONFLICT, EFFECT_CONFLICT ; AC-BE-15 |
| API-BE-044 Privacy, FEAT-016 | POST /me/exports ; W/M | `{scope_code:"scope_demo",verification_proof:"proof_demo"}` → PrivacyJob export, 202 | P vérifié ; K ; périmètre minimisé par 15 | VERIFICATION_REQUIRED, EXPORT_LIMIT ; AC-BE-16 |
| API-BE-045 Privacy, FEAT-016 | GET /me/exports/{job_demo} ; W/M | ∅ → PrivacyJob, 200 | P ; y compris compte en état restreint si approuvé | RESOURCE_UNAVAILABLE ; AC-BE-16 |
| API-BE-046 Privacy, FEAT-016 | POST /me/exports/{job_demo}/download-grants ; W/M | `{verification_proof:"proof_demo"}` → DownloadGrant, 200 | P vérifié ; K avec revalidation ; artifact ready/non expiré, pas d'accès tiers | EXPORT_NOT_READY, EXPORT_EXPIRED ; AC-BE-16 |
| API-BE-047 Privacy, FEAT-016 | POST /me/deletion-requests ; W/M | `{verification_proof:"proof_demo",confirmed_policy_version:"policy_demo"}` → PrivacyJob deletion, 202 | P vérifié ; K ; une demande active, pas de suppression directe par GET | VERIFICATION_REQUIRED, DELETION_IN_PROGRESS ; AC-BE-17 |
| API-BE-048 Privacy, FEAT-016 | GET /me/deletion-requests/{job_demo} ; W/M | ∅ → PrivacyJob, 200 | P via accès restreint à définir avant révocation sociale complète | RESOURCE_UNAVAILABLE ; AC-BE-17 |

**Limites explicites :** routes de comptes privés (demandes/acceptation), communautés, historique de sessions et MFA dépendent des arbitrages concernés ; elles ne sont pas inventées comme déjà complètes. Les demandes privacy autres qu'export/suppression et l'accès support exceptionnel nécessitent des contrats supplémentaires si 15/10 les exigent. Les opérations financières, messages, search et endpoints communautaires ne sont pas ajoutés à ce lot.

**Compléments nécessaires avant gel des parcours :** 05/06/10 doivent confirmer les besoins de lecture de la liste des blocages, des préférences de notification et de la file des recours administrateur. Ces lectures ne sont pas encore définies par les 48 opérations ; leur absence bloque le parcours consommateur concerné, pas cet inventaire M0. La route média de délivrance effective et son contrôle au téléchargement restent propriétaires 08/14 : un grant émis ne prouve pas le respect du retrait. Aucune couverture complète des parcours n’est revendiquée.

### Pagination, statuts et défaillances

**Fil :** tri `(published_at DESC, id DESC)` candidat, `published_at` immuable après première publication. Curseur opaque, lié au lecteur/requête/version de tri ; première page fixe un plafond, pages suivantes utilisent un keyset strictement inférieur à la dernière clé examinée. Nouvelles publications après plafond visibles au rafraîchissement ; filtres d'accès réévalués à chaque page. Pas de garantie de snapshot des relations follow/visibilité ; absence de doublon dans un parcours de curseur monotone, pas de promesse de complétude historique après changement des droits. Budget de scan borné ; une page courte/vide peut porter un `next_cursor` si des candidats restent. `has_more` décrit la continuation, pas un nombre garanti d'éléments visibles. Curseur expiré/incompatible : redémarrage explicite du client, sans concaténation aveugle. Compteurs exacts et total de contenus interdits non exposés.

| Domaine | États / transition candidates | Échec, annulation et reprise |
| --- | --- | --- |
| Compte/session | pending_verification → active ; suspension sociale distincte ; session active → revoked/expired | Récupération vérifie une preuve avant nouvel accès ; suspension ne prouve pas révocation des droits privacy/recours. Flux exact 14/09/15. |
| Média | awaiting_upload → processing → ready/rejected ; ready → restricted → purge_pending → purged | Fin d'upload ne signifie pas scan réussi. Retenter traitement avec même ID ; fichier rejeté non attachable. Objet orphelin nettoyé selon politique, aucune suppression d'un média référencé sans coordination. |
| Publication | published → restricted/removed ; version incrémentée sur édition | Retrait logique confirmé avant purge physique ; modifier ne restaure pas un retrait modération. Brouillon client éventuel distinct, stockage local à examiner avec Privacy. |
| Signalement/cas | received → triaged → reviewing → resolved ; fusion de doublons interne traçable | Reçu utilisateur stable même si plusieurs rapports rejoignent un cas ; accès au contenu signalé ne révèle pas le rapport. |
| Décision | proposed/pending_effect → applied ou failed ; notice pending/delivered/failed séparée | Aucun « sanction appliquée » sur simple mise en queue. Retry même ID, audit du résultat ; décision non modifiable silencieusement après application. |
| Recours | submitted → reviewing → resolving → resolved ; outcomes upheld/modified/overturned | Déposer ne lève pas automatiquement la sanction. Annulation compense la décision ciblée seulement ; autre sanction active ou suppression par auteur empêche la restauration automatique. |
| Export | queued → verifying/processing → ready → expired ; failed récupérable selon code | Reprise du job, téléchargement séparé ; filtrer données de tiers et preuves protégées selon 15. |
| Suppression | requested → verified → restricting → erasing → completed ; blocked/failed explicités | `completed` selon critères par catégorie et exceptions approuvés ; suivi compatible révocation. Annulation éventuelle et fenêtre uniquement si 15/01 l'approuvent ; pas de délai inventé. |

Clients : état vide = `items:[]`, chargement géré par W/M/A, erreur traduisible avec action de reprise, objet retiré = état neutre sans contenu ancien, session expirée = réauthentification puis revalidation. Les fonctions clavier/focus/lecteur d'écran sont de 02/05/06 ; Backend fournit IDs de champs, alt_text, texte Unicode et états déterministes. L'utilisateur ne voit ni exception SQL ni nom de worker.

### Modèle conceptuel, invariants et cycle de vie

Chaque ligne décrit une catégorie de données, **pas une table créée**. PostgreSQL comme source transactionnelle et S3 compatible pour fichiers restent candidats de la stack ; Redis ne porte aucune vérité irremplaçable. Révision, IDs stables et contraintes doivent être traduits en modèle détaillé par 04 avec avis 03/15 avant migrations.

| Catégorie / origine, finalité, propriétaire métier | Accès et stockage proposés | Mise à jour, export, suppression, rétention et sauvegardes |
| --- | --- | --- |
| Identité/preuve/session, fournie par personne ou authentificateur ; accès au service ; 04/14/15 | Secret/preuve isolés du profil, hachage/chiffrement selon usage ; support sans accès aux secrets ; événements de révocation sans credential | Export exclut secrets, révocation transactionnelle ; rétention session/audit à fixer par 14/15 ; restauration ne réactive pas d'anciens accès révoqués. |
| Profil et paramètres, personne ; présentation/contrôle ; 01/15 | Champs publics explicitement sélectionnés, paramètres propriétaires ; PostgreSQL candidat | Version d'édition ; export des données propres approuvées ; effacement/anonymisation et rétention par 15, avatars et caches compris. |
| Follow/blocage, personne ; graphe/anti-abus ; 01/09 | Paire orientée unique, pas de self ; données de blocage à accès limité | Blocage prime selon politique, déblocage ne recrée pas relation ; export sans violation des droits tiers ; suppression retire edges et compteurs, restauration réconcilie les tombstones. |
| Post/commentaire/réaction, personne ; échanges ; 01/09/15 | Audience et parent contrôlés ; unique réaction selon cardinalité produit | Édition versionnée ; médias/aperçus inclus dans restriction ; export/rétention d'historique à fixer ; tombstones et purge des projections, pas de réapparition après replay. |
| Fichiers/variantes, personne et 08 ; diffusion d'image ; 08/15 | Stockage privé, origine non contournable, accès selon contexte ; rôle média minimal | Scan, métadonnées EXIF à traiter par 08/15 ; retrait de toutes variantes et URLs ; purge/sauvegardes/délai borné à décider. |
| Notifications/préférences, événements utilisateur ; information ; 01/15 | Destinataire seulement, références minimales, aperçus revalidés | Marquage lu idempotent ; préférence appliquée avant livraison ; notification retirée/générique si cible inaccessible ; export et rétention à définir. |
| Signalement/preuve/décision/recours, usager ou agent ; résolution d'abus ; 09/10/15 | Stockage à accès restreint, signalant et preuve séparés des notifications ; audits d'accès | Motifs/version, correction par décision liée ; rétention/exception à suppression et export tiers selon 15 ; accès aux preuves autorisé après retrait public sans remise en ligne. |
| Demande/artifact privacy, personne et job ; exercice des droits ; 15 | Job propre, preuve vérification minimisée ; artifact privé, grant expirant | Date limite et exceptions approuvées ; purge de l'export ; registre d'effacement nécessaire au traitement d'une restauration, conservation à décider. |
| Outbox/déduplication/logs/audit, serveur ; fiabilité et accountability ; 04/14/15 | IDs/version/contexte minimal ; audit interne à permission propre ; analytics 13 séparé | Durées distinctes à fixer ; replay consulte état courant/tombstones ; données effacées ne doivent pas être recopiées depuis payload ancien ; restauration de tous stores coordonnée. |

Invariants : unicité et ownership contrôlés côté base ; parent comment/post cohérent ; références média vérifiées ; état métier, clé K et événement atomiques ; invariants d'accès appliqués avant publication d'un événement révélateur ; un rollback ne laisse ni compteur durable ni notification d'une écriture refusée. Les projections/compteurs sont reconstruisibles, avec déduplication et version monotone par agrégat. Les opérations batch futures gardent les mêmes contrôles par élément.

### Événements et tâches candidats

Version 1 ; identifiant stable `event_id`, `type`, `schema_version`, `aggregate_id`, `aggregate_version`, `occurred_at`, `correlation_id`, payload minimal. Auth interne et habilitation producteur/consommateur à fixer par 03/14. Publication après commit, livraison au moins une fois candidate ; aucun exactly-once global promis. Déduplication par consommateur/event, protection contre ordre inversé, backoff borné, dead letter visible et replay audité. Les timeouts/quotas de C4 s'appliquent ; événement invalide isolé sans bloqueur infini. Pas de payload de texte privé ou de secrets par défaut.

| Contrat | Producteur → consommateurs | Entrée → effet / exemple | Défaillance et critère |
| --- | --- | --- | --- |
| EVT-BE-01 content.changed.v1 | 04 Posts/Comments → projections 04, Média 08 selon retrait | `{aggregate_id:"post_demo",aggregate_version:2,change:"restricted"}` → projection version 2 | Rejouer ou recevoir version 1 après 2 ne restaure pas contenu ; AC-BE-18. |
| EVT-BE-02 access.changed.v1 | 04 Graphe/Identité → 04 accès, 08 grants | `{aggregate_id:"user_demo",aggregate_version:3,change:"policy_changed"}` → invalidation | Queue en retard : autorisation actuelle prévaut ; AC-BE-04/11/18. |
| EVT-BE-03 media.processed.v1 | 08 → 04 Media/Posts | `{aggregate_id:"media_demo",aggregate_version:2,state:"ready"}` → état autoritatif importé | Vérifier producteur, version et transition ; pas de remplacement d'un objet purgé ; AC-BE-06/18. |
| EVT-BE-04 moderation.changed.v1 | 04 Safety sous règles 09/10 → 04 contenu/notifications | `{aggregate_id:"decision_demo",aggregate_version:2,effect_state:"applied"}` → état/notification distincts | Application/notification peuvent diverger ; retry sans double sanction ; AC-BE-14/15/18. |
| JOB-BE-01 privacy-request.v1 | 04 Privacy → worker 04/14 + domaines de données | `{job_id:"job_demo",kind:"export",subject_id:"user_demo"}` → PrivacyJob | Revalidation avant délivrance ; progression/checkpoint par catégorie, panne explicite ; AC-BE-16/17. |
| JOB-BE-02 notification-delivery.v1 | 04 Notification → canal autorisé | `{notification_id:"notif_demo",recipient_id:"user_demo"}` → état livraison | Relire préférence/accès avant envoi, idempotence par destinataire/événement/canal ; AC-BE-10/18. |

## Acceptation et vérification

Tous les critères sont **PLANNED**. Les TEST-0401…0418 sont des identifiants proposés à QA, vérifiés sans collision dans la référence d'entrée ; aucun résultat fonctionnel n'est PASS. Leurs types futurs sont intégration/API, avec E2E W/M/A et sécurité selon le cas. Chaque opération du catalogue renvoie à un critère ci-dessous ; les critères communs C1–C8 s'appliquent aussi.

| Critère / Test proposé | FEAT / parcours existants | Précondition → action → résultat observable | Statut / dépendance |
| --- | --- | --- | --- |
| AC-BE-01 / TEST-0401 | FEAT-001 ; AC-J01-01/02 | Politique d'admission fixée, deux soumissions identiques → activation → un compte admissible ; challenge expiré/consommé rejeté ; aucune fuite d'identité | PLANNED ; INT-0401/0404/0405 |
| AC-BE-02 / TEST-0402 | FEAT-002 ; AC-J01-03/04 | Révocation/rotation/récupération → requête protégée et rejeu → session révoquée refusée ; récupération neutre ; droits restreints explicitement testés | PLANNED ; INT-0404 |
| AC-BE-03 / TEST-0403 | FEAT-003/004/021 ; J01/J06 | Tiers puis propriétaire → lire/modifier profil/settings → seuls champs autorisés, version et format linguistique respectés | PLANNED ; INT-0401/0405/0407 |
| AC-BE-04 / TEST-0404 | FEAT-004/006/007 ; AC-J02-01/04/05 | Réduire audience/retirer contenu → détail, cache, média, avatar, lien existant, liste → accès conformes au point d'effet et au délai média approuvés | PLANNED ; INT-0404/0405/0406 |
| AC-BE-05 / TEST-0405 | FEAT-005 ; AC-J03-03 | Follow concurrent/rejoué puis retrait → une relation, aucun total interdit ; self ou blocage rejeté, listes filtrées | PLANNED ; INT-0401/0403 |
| AC-BE-06 / TEST-0406 | FEAT-007 ; AC-J02-02/04 | MIME trompeur, taille/pixels excessifs, upload expiré ou scan échoué → confirmation/attachement → rejet sans publier ; média prêt autorisé accepté | PLANNED ; INT-0406 |
| AC-BE-07 / TEST-0407 | FEAT-006 ; AC-J02-03 | Même clé K/même corps, timeout puis retry → même post ; clé K/autre corps 409 ; édition version périmée 412 ; retrait de droits bloque replay privé | PLANNED ; INT-0402/0404 |
| AC-BE-08 / TEST-0408 | FEAT-008/022 ; AC-J03-01 | Publications ex æquo, nouvelles insertions, suppressions → parcours curseur → ordre stable, aucun doublon, filtre courant, page vide/continuation exacts | PLANNED ; INT-0401/0402/0407 |
| AC-BE-09 / TEST-0409 | FEAT-009/010 ; AC-J03-02/03 | Cible retirée ou blocage concurrent → commenter/réagir → résultat ordonné selon contrat, aucune écriture interdite ; retry sans double interaction | PLANNED ; INT-0402/0403 |
| AC-BE-10 / TEST-0410 | FEAT-011/022 ; AC-J03-05 | Préférence changée ou accès retiré avant livraison → job/retry/lecture → pas de contenu interdit, pas de duplication, catégorie applicable respectée | PLANNED ; INT-0401/0405/0407 |
| AC-BE-11 / TEST-0411 | FEAT-012 ; AC-J04-01 | Blocage confirmé puis retries et déblocage → API/listes/grants/interactions → règles sur chaque surface ; aucun follow restauré implicitement | PLANNED ; INT-0403/0404 |
| AC-BE-12 / TEST-0412 | FEAT-013 ; AC-J04-02/03/04 | Signalement sur cible retirée/blocage et réseau interrompu → retry → reçu ou refus documenté, aucune identité du signalant exposée | PLANNED ; INT-0403/0405 |
| AC-BE-13 / TEST-0413 | FEAT-014/015 ; AC-J05-04 | Compte suspendu éligible → consulter décision/déposer/suivre recours → accès limité fonctionnel ; autre utilisateur refusé | PLANNED ; INT-0403/0404/0405 |
| AC-BE-14 / TEST-0414 | FEAT-014/017 ; AC-J05-01/02/03 | Agent révoqué ou deux agents concurrents, effet/notification en panne → lire/agir → refus ou conflit, état effectif distinct et audit attribuable | PLANNED ; INT-0403/0404 |
| AC-BE-15 / TEST-0415 | FEAT-015 ; AC-J05-05 | Autre sanction active ou suppression auteur → annuler décision sur recours → aucune restauration interdite, compensation ciblée et historique préservé | PLANNED ; INT-0403/0405 |
| AC-BE-16 / TEST-0416 | FEAT-016 ; AC-J06-01/02 | Export tiers/expiré/job interrompu → suivi/grant/téléchargement/retry → refus tiers, état exact, données exportées conformes à la politique | PLANNED ; INT-0404/0405 |
| AC-BE-17 / TEST-0417 | FEAT-016 ; AC-J06-03/04 | Suppression validée et restauration backup/replay → réconciliation → absence de remise en circulation, suivi selon exceptions explicites, sessions sociales révoquées | PLANNED ; INT-0405/0406/0408 |
| AC-BE-18 / TEST-0418 | FEAT-019 et invariants ; J02–J06 | Événements dupliqués/inversés, Redis ou worker indisponible → reprise → état monotone, refus sûr si droit inconnu, aucun payload privé dans logs, retard observable | PLANNED ; INT-0402/0404/0408 |

Critères J07 restent PLANNED dans le document produit, dépendants d'OPEN-003 ; pas de fausse couverture par les 48 opérations ci-dessus. La charge, les seuils de temps et le téléchargement média après retrait nécessitent un environnement représentatif ; tests unitaires seuls insuffisants. Voir [rapport documentaire](../quality/backend-contract-validation.md) pour les contrôles réellement exécutés.

## Fiches de décisions importantes à arbitrer

Les fiches suivantes instruisent les OPEN existants ; les identifiants DEC/ADR définitifs seront attribués par 00/03. Aucun rejet d'alternative n'est officiel.

| Question / objectif, problème | Solution recommandée et alternatives écartées à titre proposé | Dépendances, impacts et risques | Priorité, phase et réexamen |
| --- | --- | --- | --- |
| OPEN-005 — simplicité et cohérence ; écritures métier/notifications pouvant diverger | Monolithe modulaire avec transaction/outbox ; services séparés dès M0 écartés provisoirement pour coûts et contrats supplémentaires | 03/14/20, consumers ; moins d'exploitation au pilote, maintien des frontières ; risque de backlog, reprise/dead letter nécessaires | P0 MVP ; ADR attendu ; extraction après mesure de contention/isolation/charge indépendante. |
| OPEN-003 — taille pilote ; communautés ajoutant rôles et modération | Follow initial recommandé ; communautés immédiates restent option si valeur pilote démontrée ; aucune modification FEAT-020 effectuée | 01/09/10/19/HQ ; effort réduit mais valeur communautaire potentiellement amoindrie ; intégrer coûts et capacité humaine | P0 arbitrage MVP ; revoir après retours des segments pilotes, pas après décision technique seule. |
| OPEN-007 — visibilité fiable ; liens privés déjà émis après retrait | Pour contenu restreint, accès autorisé au moment de livraison ou révocation CDN démontrable ; simple URL signée longue non retenue comme garantie immédiate | 08/14/15/03 ; coût/latence de validation vs risque confidentialité ; TTL/purge mesurés et caveat copies déjà reçues | P0 MVP ; test AC-BE-04 requis ; délai et architecture approuvés avant implémentation média. |
| OPEN-007 — recours/droits privacy sous suspension ; refus auth global trop large | Authentification avec capacités restreintes dédiées ; verrouillage total écarté si aucun canal alternatif approuvé | 09/10/14/15 ; accès aux droits sans réautoriser publication ; risque escalade évité par matrice précise et tests | P0 MVP ; examiner identité et suivi après suppression ; alternatives humaines possibles sur contrat validé. |

## Dépendances, risques et transmission

Émetteur de chaque demande : 04 Backend. Les IDs INT-0401…0408 et RISK-0401…0405 sont proposés, sans collision dans la révision d'entrée, à intégrer par HQ/17. **Toutes les transmissions aux discussions : À TRANSMETTRE** ; publication GitHub n'est pas preuve de lecture/accord d'un destinataire. Référence et delta communs : ce seul livrable, sections et critères cités ; pas de demande de réaudit du dépôt.

| ID / destinataire | Question ciblée / livrable attendu | Effet bloquant |
| --- | --- | --- |
| INT-0401 → 01 + 02/16/HQ | Trancher OPEN-003, audiences/défauts, cardinalité réactions, édition, catégories notification, langue et limites texte ; retourner règles FEAT-001…022 et états UX | Bloque schémas/énums des opérations touchées, pas conventions d'erreur ni inventaire. |
| INT-0402 → 03 + 20/21 | Examiner C4/C5/C6, feed, outbox, ownership et concurrence ; ADR avec garanties, timeouts et stratégie de migrations | Bloque mécanismes transactionnels et code, pas rédaction des cas d'acceptation. |
| INT-0403 → 09 + 10/15 | Matrice blocage/suspension, recevabilité report de cible invisible, motifs/états/recours et indépendance ; valider interfaces 034–043 | Bloque modération, droits suspendus et propagation des restrictions. |
| INT-0404 → 14 + 03/05/06 | Contrat sessions/rotation/récupération, MFA interne, anti-abus, révocation, grants et mode panne Redis ; revue matrice d'accès | Bloque auth/admin et garantie d'accès, pas classement des futures fonctionnalités. |
| INT-0405 → 15 + 01/09/10 | Catégories exportables, vérification demande, durées et exceptions, sauvegardes, suivi après révocation, preuve de signalement et âge | Bloque cycle données/exports/suppression, schéma final et ouverture pilote. |
| INT-0406 → 08 + 14/15 | Formats/pixels/tailles, scan, checksum, EXIF, variantes, alt_text, révocation effective des liens ; contrat media.processed | Bloque image publiée et AC-BE-04/06 ; texte seul peut continuer en spécification. |
| INT-0407 → 05/06/10 + 02/16 | Vérifier schémas/exemples/erreurs/retry K, concurrence Vn, pagination vide et statut inconnu ; accord consommateur ou delta ciblé | Bloque gel des contrats consommés ; native reste Phase 2 candidate. |
| INT-0408 → 18 + 13/14/17/20/21 | Reprendre AC-BE et AC-J, attribuer/ratifier TEST IDs, fixer charge et preuves CI ; 13/15 minimisation analytics ; 17 indexer ce livrable | Bloque PASS/READY applicatif ; revue documentaire possible immédiatement. |

| Risque | Impact / propriétaire | Mesure proposée et état |
| --- | --- | --- |
| RISK-0401 | Fuite par ancien lien, cache ou replay ; 08/14/15 | C6 et OPEN-007, délai de révocation démontré ; **OUVERT, critique avant média restreint**. |
| RISK-0402 | Double publication/sanction après timeout ; 04/03 | K atomique + Vn + tests concurrents, réponse revalidée ; **OUVERT**. |
| RISK-0403 | Suspension bloquant recours/privacy ou agent excessivement habilité ; 09/10/14/15 | Capacités distinctes, accès de preuve séparé et audit ; **OUVERT, critique avant pilote**. |
| RISK-0404 | Données supprimées recréées par backup/projection ; 04/14/15 | Tombstones, rejouer état courant, procédure restauration/purge validée ; **OUVERT**. |
| RISK-0405 | Schémas conceptuels pris pour contrat prêt, dérive du périmètre et IDs concurrentiels ; 00/03/17/21 | Statuts, contrôles de collision à intégrer, avis consommateurs, maintien FEAT ; **OUVERT**. |

## Compte rendu obligatoire de fin d'étape

1. **Décisions prises / à valider :** structure locale et traçabilité adoptées ; routes, schémas et politiques restent PROPOSÉS. OPEN-003/005/007 instruits ; aucune décision architecture, privacy ou MVP approuvée par 04.
2. **Livrables :** ce document version 0.1, index Backend et rapport documentaire lié ; publication par branche/PR avec référence réelle dans le compte rendu GitHub. Aucun autre domaine réécrit.
3. **Tests :** contrôles du dépôt et tests de son validateur décrits dans le rapport ; tests applicatifs, permission, API, charge, migrations et restauration NON EXÉCUTÉS. AC-BE et AC-J restent PLANNED.
4. **Questions :** paramètres C1–C8 et INT-0401…0408 ; aucune valeur inconnue déclarée approuvée.
5. **Dépendances :** contrats → 03/05/06/10/18 ; accès et cycle données → 09/14/15 ; média → 08 ; coordination → 00/17/20/21. État des transmissions aux discussions : À TRANSMETTRE.
6. **Risques :** RISK-0401…0405 ; avis indépendants NON REÇUS ; publication n'est pas autorisation de lancer le code.
7. **Suite / HQ :** faire examiner les deltas cités, arbitrer les OPEN, confirmer IDs et avis consommateurs, rédiger OpenAPI/modèle/migrations planifiées du seul lot retenu ; revue 21 et QA avant autorisation d'implémentation. Cette contribution dépend de la PR nº 2, elle-même dépendante de nº 1 ; rebaser/retargeter et revérifier le diff si les bases changent.
