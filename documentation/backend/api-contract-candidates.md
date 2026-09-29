# Contrats API candidats — Backend M0

**Révision courante : v0.2, delta propriétaire L1 GAP-L1-01 à 04 en fin de document (30 septembre 2026).** La section v0.1 est conservée comme entrée historique ; ses contrats restent proposés. Le delta précise les seuls sujets du mandat HQ §10, sans approuver les politiques ni ouvrir le code.

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

## Delta propriétaire L1 — GAP-L1-01 à 04 — v0.2

**30 septembre 2026, Europe/Paris — 04 Backend/API — PROPOSÉ, avis spécialisés NON REÇUS.** Réponse au [mandat HQ §10](../project-governance/m0-mvp-arbitration.md) reçu au SHA `206b1804df5cb602140729613fa85080fea32c7c`. Base de publication : PR #27, `85319286222559c22f943f4c94838840c23dae97`, qui conserve ce mandat et ajoute le candidat de cycle de session. Entrées bornées : [préparation L1 §3–4.2 et S01–S04h](../quality/first-lot-contract-readiness.md), C1–C8 et API-BE-001–011 ci-dessus, REQ-1401/1402 de [14](../security/security-operations-requirements.md), C-IDENTITY/W03/W04 de [05](../web-application/web-requirements.md), catégories P01/P02 et droits de [15](../privacy/privacy-requirements.md). Aucun réaudit du corpus.

Le mandat de cette discussion est **reçu et exécuté pour la rédaction** ; cela ne change pas les statuts de réception des autres discussions. DIR-012 confirme le public universel ; ni origine, ni pays servi, ni langue, ni âge admissible ne sont déduits d'une priorité marketing. FEAT-001/002/003/004/018/021 restent **MVP P0 candidats**. Client natif : Phase 2 candidate ; aucun transport natif livré. Les autres phases et GAP-L1-05 à 08 ne sont pas reclassés. **Les quatre GAP restent OUVERTS ; L1 BLOQUÉ POUR CODE.**

Portée de v0.2 : propositions plus précises pour L1, à lire avant les formes conceptuelles v0.1 lorsqu'elles diffèrent. Ce n'est pas une rupture d'API déployée : aucun runtime n'est reçu. API-BE-001–007 conservent leurs IDs ; API-BE-049 est proposé ci-dessous, sans collision dans la base examinée. Les auxiliaires notés L1 sont des repères locaux à ratifier, pas des endpoints déjà approuvés. Les arbitrages et contrats des autres propriétaires ne sont pas réécrits.

### GAP-L1-01 — identité, preuves et transport

**Objectif :** obtenir un compte activé et une session attribuable à un titulaire, avec une reprise compréhensible. Producteur : 04 ; consommateur candidat : 05 ; choix de protocole à ratifier par 03/14, données par 15, portée par HQ.

| Option d'identité | Valeur / contraintes / avis Backend |
| --- | --- |
| Email vérifié + mot de passe | **Recommandée comme hypothèse de travail Web L1**, faute de preuve d'une disponibilité universelle des passkeys pour le public retenu. Pas de fournisseur d'identité imposé ; exige stockage de secrets par fonction de hachage dédiée, anti-abus, délivrabilité, récupération et accessibilité à tester. Coût de support et risque de phishing à instruire avec 14/19. |
| Passkey avec récupération indépendante | Alternative recevable ; réduit la saisie d'un secret partagé, mais exige un contrat d'enrôlement, multi-appareils et récupération/accessibilité. Ne pas l'écarter définitivement ni prétendre que le candidat password serait approuvé. |
| Lien/code email sans mot de passe | Alternative plus simple côté secret applicatif, dépendance à la boîte mail pour chaque connexion, délivrabilité et rejeu à spécifier ; à comparer avec 14/15/05. |
| Fédération | Alternative si besoin démontré ; dépendances fournisseur, claims minimisés, liaison de comptes et récupération à documenter. Aucune fusion de comptes par email reçu d'un tiers. |

La vérification de boîte mail démontre un contrôle du canal au moment de la preuve, **pas l'identité civile, l'âge, la résidence ou l'admissibilité**. L'admission reste un contrôle séparé issu des politiques 01/15/HQ. À politique absente : aucun compte activé par défaut ; erreur neutre de disponibilité du service pour tous les demandeurs concernés, sans distinguer un compte existant. L'analyse indépendante des transitions peut continuer.

**Transport recommandé conditionnellement au Web de même origine :** session autoritative serveur ; credential opaque dans cookie `Secure`, `HttpOnly`, sans `Domain`, `Path=/`, préfixe `__Host-`, `SameSite=Lax` proposé. HTTPS requis. Credential jamais dans JSON, URL, localStorage, sessionStorage, logs ou analytics. La portée navigateur est distincte de l'identité du compte. Aucune session opérateur ni exemption MFA définie par ce delta.

Mutations authentifiées et préauthentifiées : vérification d'origine exacte et preuve CSRF liée au contexte serveur, y compris login/logout/récupération ; refus 403 `REQUEST_ORIGIN_DENIED` ou `CSRF_INVALID`, sans mutation. Origine absente non acceptée implicitement pour ce profil Web ; cas légitime à contractualiser avec 05/14. `SameSite` n'est pas le seul contrôle. CORS avec credentials vers une origine arbitraire interdit dans l'option proposée. Frontend/API inter-origines : choix distinct 03/05/14, sans adaptation silencieuse à `SameSite=None`. Une XSS n'est pas résolue par HttpOnly/CSRF : contrôles Web et CSP restent 05/14.

Alternative bearer : recevable pour un client explicitement retenu, sous contrat d'audience, stockage, expiration et révocation ; non sélectionnée pour L1 Web. Alternative bootstrap serveur : conserve la sémantique d'identité du GAP-03, ne choisit pas un framework. Aucun choix NestJS/PostgreSQL/Redis nouveau n'est approuvé ici ; source autoritative transactionnelle requise, Redis seul non suffisant sans garanties ratifiées.

| Étape / contrat réutilisé | Entrée et preuve proposées pour la branche email/password | État, sortie et contrôles |
| --- | --- | --- |
| Préparation L1-CTX, auxiliaire candidat `POST /auth/contexts` | Corps vide, origine autorisée ; contexte aléatoire serveur et preuve CSRF ; preuve de possession du contexte, **pas preuve d'identité** | 201 `{state:"ready",context_ref,context_version,expires_at,csrf_token}` ; secret de liaison HttpOnly distinct du credential authentifié. Aucun compte ni capacité. Refus 429/503 ; contexte existant vérifié réutilisable, jamais un ID arbitraire fourni par client. Bootstrap équivalent possible si mêmes garanties. |
| API-BE-001 inscription | `identity` privée, `password` secret, `locale` proposée et éléments d'admission minimaux à définir ; contexte + K. Remplace le placeholder `registration_proof` seulement pour cette branche | 202 `{state:"accepted"}` neutre, compte pending et challenge seulement si admissible. Même réponse pour identité déjà connue ; aucune référence de compte ni `active` renvoyée ici. Envoi asynchrone accepté ne signifie pas email livré. |
| API-BE-002 activation | Challenge spécifique d'activation, contexte vérifié et K ; challenge lié côté serveur au sujet/purpose, consommation atomique | 200 reçu `{state:"active"}` seulement après contrôle de la preuve et admission ; aucune session implicite. Challenge recovery refusé. L'email ne choisit pas les capacités. |
| API-BE-003 connexion | `identity,password` sous HTTPS, contexte/CSRF ; vérification du credential et de sa révision au commit | 201 SessionResult minimal `{state:"authenticated"}` + cookie nouveau ; puis API-BE-049. Erreur 401 `AUTH_INVALID` uniforme pour inexistant/secret invalide/non admissible sans preuve suffisante. Aucun retry automatique de login. |
| API-BE-006 demande récupération | `identity`, contexte/CSRF + K | 202 `{state:"accepted"}` neutre ; aucune révocation ni changement de mot de passe. Livraison dédupliquée ; compte existant non confirmé au navigateur. |
| API-BE-007 récupération | Challenge recovery valide + `replacement_password`, contexte/CSRF + K | 200 `{state:"completed"}` après changement de credential et révocations atomiques du GAP-04 ; pas d'auto-login, pas de levée de sanction. |

Schémas fermés C2. Pour la branche password, choisir et tester politique/tailles/hachage avec 14 avant READY ; aucun mot de passe tronqué, normalisé ou réaffiché. Identité email : validation syntaxique et règle de comparaison explicites avant unicité ; ne pas fusionner arbitrairement points/alias/casse de partie locale. Erreurs purement syntaxiques 400 autorisées si indépendantes de l'existence d'un compte. Normalisation d'identité et admission restent GAP-06/07, propriétaires nommés, sans preuve juridique inventée.

Activation/récupération : préférer un code de preuve à saisir puis POST, ou un lien ne consommant rien avant POST explicite. Format/entropie, durée et nombre d'essais à fixer par 14 ; aucun secret dans query string/journal/referrer. Un scanner d'email/GET ne consomme pas la preuve. Changement de navigateur : le challenge prouve le contrôle du canal et peut lier une **nouvelle transaction**, après validation, à son nouveau contexte ; il ne donne pas accès aux reçus privés d'un ancien contexte. Admission et restrictions revérifiées au commit. Une preuve consommée ne peut être réaffectée pour reprendre ailleurs.

### GAP-L1-02 — idempotence préauthentifiée et réponse perdue

**Amendement propriétaire de C5 pour 001/002/006/007 :** K est un identifiant d'opération, jamais un secret suffisant. Portée : contexte serveur vérifié + opération/version + K ; pour une consommation de challenge, liaison interne au purpose/sujet/révision. La possession du contexte est vérifiée par cookie de liaison + CSRF/origine. Les mutations auth portent aussi `Auth-Context-Version`, version attendue obtenue lors de L1-CTX : version obsolète → 409 `AUTH_CONTEXT_CHANGED` avant nouvel effet ; ce nombre seul ne prouve rien. La version fait partie de la portée/empreinte K. L1-CTX ne remplace pas une liaison de session active par une nouvelle liaison anonyme ; il restitue le contrôle existant après vérification, sinon refuse la réinitialisation implicite. Les amorçages concurrents encore sans session restent à éprouver avec 05/14. Seule la preuve métier vérifiée permet activation/récupération. Aucune recherche de résultat par email, K ou request_id seuls. Le cookie de contexte n'est jamais promu en credential de session.

Empreinte canonique des seules entrées acceptées ; pas de mot de passe/challenge en clair dans le registre K. Pour les champs secrets, empreinte avec clé serveur séparée proposée, pas un simple hash rapide permettant un test hors ligne ; choix et rotation de clé avec 14/15. Résultat mémorisé = reçu minimal expurgé, référence interne et statut, jamais cookie/credential. Avant tout rejeu : vérifier contexte, liaison, durée, état de l'opération et droit au reçu ; le reçu décrit une opération historique, pas un droit social actuel.

| Situation | Règle et réponse candidate | Confidentialité / reprise |
| --- | --- | --- |
| Même contexte vérifié + même K + mêmes entrées, première exécution | Validation puis écriture atomique de K, consommation éventuelle, état métier et événement/outbox ; 202 pour 001/006, 200 pour 002/007 | Un seul effet. État interne `in_progress` puis `completed` ; le 202 accepte le traitement, pas la livraison email. |
| Même tuple après succès, réponse initiale perdue | Même statut et reçu minimal mémorisé ; pas de nouveau challenge/email/session ; header candidat `Idempotency-Replayed: true` | Reçu d'activation/récupération ne signifie pas compte toujours actif ; droits courants lus séparément. Si reçu non délivrable : 409 `OPERATION_RECONCILIATION_REQUIRED`, aucun corps privé ancien. |
| Même K, entrée différente | 409 `IDEMPOTENCY_CONFLICT`, aucun effet ; conflit évalué dans la portée vérifiée | Ne pas révéler l'entrée précédente. Le client ne corrige pas cette erreur en créant automatiquement une nouvelle clé. |
| Clé différente, challenge non consommé, mêmes demandes concurrentes | Sérialiser sur le challenge et le sujet ; un gagnant 200, l'autre 409 `CHALLENGE_CONSUMED` | Aucun second reset/activation. Possession d'un secret de challenge valide requise pour un diagnostic spécifique ; faux challenge → 400 `CHALLENGE_INVALID`. |
| Clé différente sur 001/006 sans challenge consommable | Nouvelle intention possible, mais unicité du compte et anti-abus/déduplication de livraison s'appliquent ; 202 neutre ou 429 fondé sur contexte/quota | Pas de promesse d'exactly-once pour des clés différentes ; nouvelle tentative réseau doit conserver K. Une demande tierce ne remplace ni les données ni le secret d'un compte déjà actif ; modification d'une inscription pending exige un contrat de preuve distinct, non accordé par 001. Nouvelle demande neutre ne réinitialise pas les compteurs anti-abus. |
| Preuve consommée, tuple déjà complété | Retour du seul reçu historique si contexte et fenêtre encore valides ; **pas de nouvelle vérification donnant accès au compte** | Une autre clé/contexte ne récupère pas le reçu. Conserve la règle de refus d'une nouvelle consommation. |
| Preuve expirée avant première mutation | 410 `CHALLENGE_EXPIRED` pour preuve authentique reconnue ; aucun effet ; nouvelle procédure explicite | À l'instant limite `now >= expires_at`, refus. Une opération déjà committée peut rendre son reçu tant que la fenêtre K n'est pas expirée. |
| Contexte absent/invalide/expiré | 401 `PREAUTH_CONTEXT_REQUIRED` ou `PREAUTH_CONTEXT_EXPIRED`, aucun résultat privé | Recréer le contexte explicitement ; pas de retry transparent d'une preuve déjà consommée. Nouvelle preuve si résultat irréconciliable. |
| Opération en cours | 409 `OPERATION_IN_PROGRESS` avec `Retry-After`, aucune seconde exécution | Retry même tuple après délai, dans budget ; une lease worker expirée ne prouve pas le rollback. Examiner état transactionnel avant reprise. |
| Enregistrement K expiré ou perdu | 409 `OPERATION_RECONCILIATION_REQUIRED` lorsque l'ancien contexte/opération n'est plus réconciliable | Pas de nouvel effet supposé sûr. Invariants compte unique/challenge consommé subsistent indépendamment de K ; demander procédure explicite. |
| Autorité indisponible, timeout avant/après commit | 503 `AUTHORITY_UNAVAILABLE` si réponse disponible ; sinon résultat inconnu | Ne pas conclure échec. Rejouer le tuple si fenêtre encore valide ; après budget, action manuelle. Pas de secret dans les logs de panne. |

Expiration opérationnelle proposée, **non approuvée** : durée du contexte préauthentifié 30 minutes ; challenge activation/récupération 15 minutes ; récupération du reçu K jusqu'à l'expiration du contexte, sans extension par retry. Ces valeurs limitent le stockage et la réutilisation tout en permettant une reprise manuelle ; délivrabilité et accessibilité à évaluer avec 05/14/15, pas une exigence légale. Le serveur refuse une nouvelle opération sur un contexte expiré **avant** consultation/création K : une clé purgée dans ce contexte ne redevient pas une création autorisée. Un nouveau contexte est une nouvelle intention soumise aux invariants métier. Tentatives de preuve, plafond de contextes, fréquence de renvoi et rétention des tombstones : ouverts, 14/15/03, bloquent READY. Un compte ou challenge ne se recrée jamais du seul fait d'une purge K.

Effets asynchrones : acceptation, sujet et demande d'envoi durable associés au commit ; un replay ne produit pas un second message d'outbox. L'email peut néanmoins être délivré en double par un prestataire après réponse perdue : tolérer une copie du même challenge, aucun nouvel effet à sa consommation ; ne pas annoncer une livraison exactement une fois. Échecs transitoires repris selon politique 14 ; message épuisé remonté au support sans publier l'existence d'un compte.

### GAP-L1-03 — avis propriétaire sur le contexte courant

**Avis Backend : candidat §4.1 AMENDÉ, favorable à sa sémantique sous les réserves ci-dessous.** Ce n'est pas un accord 05/14/09/15. Recommandation : **API-BE-049, `GET /api/v1/auth/context`**, lecture dédiée ; même DTO possible dans un bootstrap privé, mais toujours possibilité de revérification explicite. Producteur 04, consommateurs 05 puis 06 si retenu. Pas de lookup par compte fourni, aucune usurpation support, corps métier vide ; query métier inconnue → 400 `VALIDATION_FAILED`.

| Champ §4.1 | Avis Backend | Règle de projection candidate |
| --- | --- | --- |
| `authentication` | ACCEPTÉ | Obligatoire, exactement `anonymous` ou `authenticated`. Panne n'est aucune des deux variantes. |
| `viewer` | ACCEPTÉ | Obligatoire ; null si anonymous, objet si authenticated ; toute incohérence est une erreur consommateur sûre. |
| `viewer.account_ref` | ACCEPTÉ | ID opaque obligatoire, référence de compte dérivée de session, jamais credential. Nécessité de minimisation à ratifier 15. |
| `viewer.profile_ref` | AMENDÉ | Obligatoire, ID opaque ou null ; mapping interne account → profil exposable, aucune égalité supposée. Null ne supprime pas le compte et ne justifie pas une création automatique de profil. |
| `viewer.account_state` | AMENDÉ | Projection fermée proposée `active` / `restricted` ; pas de motif de sanction, âge ou résultat d'admission. Session de compte non activé ne doit pas exister dans l'option recommandée ; état incompatible → erreur sûre, pas active par défaut. Mapping source exact GAP-05 avec 09/14/15. |
| `viewer.allowed_capabilities` | AMENDÉ | Liste sans doublons issue d'une allowlist validée, jamais concaténation de rôles internes. Pas de privilège admin implicite, aucun wildcard. Codes GAP-05 non ratifiés → pas de capacité supposée. Une restriction conserve seulement les voies effectivement autorisées. |

Schémas candidats : `{"authentication":"anonymous","viewer":null}` ; fixture de projection sans droit implicite : `{"authentication":"authenticated","viewer":{"account_ref":"account_demo","profile_ref":null,"account_state":"restricted","allowed_capabilities":[]}}`. La seconde n'est **pas** la permission retenue pour les recours : tant que leurs capacités et canal alternatif ne sont pas définis, GAP-05 et GO pilote restent bloqués.

| Règle du §4.1 | Avis et précision Backend |
| --- | --- |
| Lecture sans mutation d'authentification | ACCEPTÉ : ni création/rotation/consommation de preuve, ni prolongation d'inactivité ou d'expiration absolue par cette lecture. |
| 200 anonyme pour absence/expiration/révocation reconnue | ACCEPTÉ uniquement pour API-BE-049 ; routes protégées gardent 401. Pas de raison de révocation dans la réponse anonyme. |
| Anonyme/restreint/panne distincts | ACCEPTÉ : validité de session indépendante de l'état métier ; source de droits indisponible → 503, jamais 200 avec droits devinés. |
| Erreurs schéma, quota, réseau | ACCEPTÉ avec codes ci-dessous ; 400 non rejoué ; 429/503/réseau repris dans budget proposé. Réponse illisible → `UNAVAILABLE`, pas logout. |
| Invalidation après auth/récupération/droit modifié | ACCEPTÉ : nouvelle lecture avant affichage privé ; une récupération n'authentifie pas. Backend réévalue droits à chaque opération, Web gère la projection. |
| 403/404 d'objet distinct de la session | ACCEPTÉ : pas de logout automatique sur ces seuls codes ; pas de boucle refresh. |
| Réponses anciennes, changements de compte, concurrence | ACCEPTÉ : génération locale et ordre de lecture nécessaires côté Web ; compléter par le protocole serveur GAP-04 pour les cookies, qui ne sont pas contrôlés par rejet du JSON. |
| Cache/mémoire/historique | ACCEPTÉ : contexte en mémoire seulement, aucune mise en cache partagée/service worker ; restauration de page privée revient à VERIFYING et masque les données. Le header seul ne prouve pas le comportement du navigateur. |
| Champs additionnels et enums inconnus | ACCEPTÉ : champs additionnels ignorés ; auth/état incohérent ou inconnu → UNAVAILABLE ; capacité inconnue n'accorde rien. Ne pas cacher définitivement l'accès aux droits : voie de reprise accessible 09/15/05 requise. |
| Détection d'une restriction distante | AMENDÉ : serveur courant à toute autorisation ; Web revérifie au chargement, reprise de focus, retour réseau et événement d'invalidation. Borne d'obsolescence maximale d'affichage `CONTEXT_MAX_AGE` encore ouverte avec 05/14 ; pas de polling choisi ni de garantie d'effacement d'une réponse déjà reçue. |
| Logs/minimisation | ACCEPTÉ : classe de résultat, request_id, latence ; aucun corps DTO, email, secret, motif de sanction ni session brute dans les diagnostics. |

Toutes les variantes et erreurs de cette lecture portent `Cache-Control: no-store` ; bootstrap HTML aussi s'il contient le contexte. GET n'émet **aucun Set-Cookie de création, renouvellement ou effacement de session**, même sur anonymous/401 : cela évite qu'une ancienne lecture supprime un cookie de session plus récent. Déchets de cookies traités par un flux séparé et sûr, pas sur réponse tardive de lecture. Diagnostic en panne seul : pas de logout ; autorité d'accès en panne : pas de réponse privée. Les permissions objet ne viennent jamais du DTO reçu par le navigateur.

| Résultat | HTTP / code | Web et reprise |
| --- | --- | --- |
| Session vérifiée, compte/projection cohérents | 200 authenticated | AUTHENTICATED ou RESTRICTED ; charger profil/paramètres séparément. |
| Absente ou fin reconnue par autorité | 200 anonymous | ANONYMOUS ; purger vues du contexte courant ; aucune preuve d'un logout précis. |
| Droits/session non vérifiables | 503 `AUTHORITY_UNAVAILABLE` | UNAVAILABLE, contenu privé masqué ; retry borné. |
| Entrée interdite / quota | 400 `VALIDATION_FAILED` / 429 `RATE_LIMITED` | Correction explicite / respecter Retry-After dans budget. |
| Schéma serveur/client incompatible | Erreur locale de protocole ; 503 `CONTEXT_UNAVAILABLE` si détectée serveur | Pas de fallback active, pas de credentials effacés automatiquement ; reprise accessible. |

### GAP-L1-04 — session logique, reprise et révocation

**Recommandation Backend : session serveur opaque sans refresh client périodique pour L1 Web.** API-BE-004 reste dans l'inventaire multi-options mais **non exposée dans ce profil recommandé** ; pas de renouvellement sur GET. Un appel à cette route absente retourne 404 `RESOURCE_UNAVAILABLE`, sans effet/cookie. Ce delta n'efface pas la route pour un futur client nécessitant un autre transport. Adoption/suppression effective requiert 03/05/14/HQ. S02 et S04d/e restent à tester : pour ce profil, vérifier l'absence de refresh puis les régénérations de connexion/élévation, pas déclarer le risque de concurrence inexistant.

Alternatives : rotation stricte (ancienne preuve consommée, réponse perdue peut imposer réauthentification et révocation de la continuation orpheline) ; rotation avec reprise bornée (liaison opération/contexte, résultat secret protégé, fenêtre et réautorisation). Non retenues pour la proposition Web, coût de protocole supérieur sans besoin client établi ; aucune tolérance de rejeu implicite. Si 14 exige un renouvellement périodique, rouvrir cette décision avec ces alternatives avant code.

Objets conceptuels distincts : compte ; révision de credential `credential_epoch` ; session logique ; secret transporté ; contexte navigateur vérifié et génération de ses transitions ; opération de déconnexion. Aucun nom de table ou migration créé. Les horloges et générations sont autoritatives serveur. Un ID fourni par le client ne permet jamais de choisir le compte à révoquer.

| Transition / course | Règle candidate, instant d'effet et résultat | Reprise Web et oracle |
| --- | --- | --- |
| Login 003 nominal | Vérifier preuve + admissibilité + credential_epoch au commit ; nouvelle session/secret indépendants du préauth ; 201 uniquement après persistance | API-BE-049 avant vue privée ; timeout = résultat inconnu, pas auto-login répété. |
| Deux login du même navigateur | Ordre serveur du contexte vérifié : au plus une session courante ; nouvelle transition invalide la précédente dans cette portée, même pour autre compte. CAS/version de contexte ; requête préparée sur ancienne génération → 409 `AUTH_CONTEXT_CHANGED` | Pas de priorité déduite de l'ordre des réponses ; intention rejetée doit être resoumise explicitement après relecture. Les autres appareils ne sont pas révoqués par une connexion ordinaire. Le login réussi avance la génération du contexte ; logout termine la session sans avancer cette génération afin de permettre le reçu borné. Nouvelle connexion, changement de liaison ou réinitialisation invalident les anciennes intentions. Un replay K complété dans la même génération ne crée pas de transition nouvelle. |
| Réponse login perdue | Session peut avoir été créée ; aucun secret récupérable par K/request_id. Si cookie reçu et identité correspond à l'intention encore courante, relecture utilisable ; sinon reprise explicite | Ne pas afficher un compte inconnu au titre de l'intention A. Nouveau login révoque l'ancienne session de ce contexte ; orpheline autrement soumise aux expirations. |
| Régénération à élévation/réauthentification | Nouveau secret après preuve ; ancien invalide au commit, même session logique ou relation de succession explicite ; pas de prolongation de durée absolue par simple rotation | N'invente aucun parcours admin ; si nécessaire au lot, contrat de preuve renforcée par 14 avant réalisation. |
| Logout 005 nominal | Cookie/session + CSRF ; capturer la session logique autorisée et son contexte avant mutation ; révoquer cette session et toutes ses continuations, même si une régénération a précédé le commit ; 204 après commit durable | « Session de ce navigateur révoquée », pas tous appareils ; aucune annulation promise d'une écriture antérieure déjà committée. |
| Logout réponse perdue puis retry | Extension proposée de 005 : K obligatoire pour l'intention logout, liée au contexte de contrôle vérifié et à la session capturée lors de la première exécution ; journal de résultat minimal durable | Même opération/contexte peut rendre 204 après révocation même si credential social terminé ; ce droit limité ne permet que lire/rejouer ce résultat, aucune action sociale. Sans preuve de liaison : 401, pas confirmation de révocation. |
| Retry logout après changement A → B | Comparer génération/contexte et liaison d'opération **avant résolution de /current pour une nouvelle mutation** ; opération A ne peut viser B | 409 `AUTH_CONTEXT_CHANGED`, aucun effet sur B ; pas de DELETE automatique sous nouveau credential. Ancienne réponse 204 ignorée par UI B. |
| Logout hors ligne, 503, autorité inaccessible | État local `LOGOUT_UNCONFIRMED`, aucune confirmation du serveur inventée | Masquer le privé immédiatement ; retry même intention dans budget seulement si contexte inchangé ; ne pas rouvrir automatiquement le privé si 049 retrouve encore A. |
| Expiration inactive/absolue | `now >= min(last_interactive_at + IDLE, issued_at + ABSOLUTE)` interdit toute nouvelle autorisation ; passage terminal ; pas de réactivation via cache | 049 anonyme, autres routes 401 `AUTH_REQUIRED` ; reconnexion explicite. |
| Demande de récupération 006 | 202 neutre n'invalide aucune session | Un attaquant ne provoque pas un logout par simple saisie d'email. |
| Récupération 007 réussie | Consommer preuve, remplacer credential, incrémenter credential_epoch et invalider **toutes les sessions antérieures du compte** dans une transaction/garantie atomique à ratifier ; 200 completed | Reconnexion explicite de tous appareils, restrictions métier conservées ; reçu K ne restitue pas le nouveau secret. |
| Login commencé avant recovery, committé après | Compare credential_epoch vérifié au credential_epoch courant ; discordance → 401 `AUTH_INVALID`, pas de session issue de l'ancien moyen | S04g : vérification lente du secret ne permet pas de contourner la révocation. Login par nouveau secret après recovery reste autorisé selon droits. |
| Révocation ou restriction concurrente avec mutation | Ordre autoritatif commun C6 : validation des droits au commit ou mécanisme équivalent ratifié par 03 ; aucune autorisation nouvelle après effet confirmé | Effet antérieur déjà committé reste distinct ; droits restreints et canaux recours/privacy selon GAP-05, non décidés ici. |
| Panne/cache obsolète/restauration | Pas d'autorisation sur simple cache positif obsolète ; autorité indisponible → 503. Réouverture après restauration invalide les secrets pré-restauration par epoch non rétrogradable ou reconstitution vérifiée des révocations | Aucune session réactivée d'une sauvegarde. Mécanisme persistant/clé et procédure 03/14/15 restent GAP-08 ; aucun test de restauration exécuté. |

**Reçu de logout et permissions :** le contexte de contrôle est un secret navigateur distinct d'une clé K publique ; il persiste uniquement pour la fenêtre de résultat approuvée après fin sociale. Il ne permet pas de révoquer une session arbitraire, ni de lire compte/profil après logout. Premier logout : authentification sociale valide requise et contrôle du contexte ; replay : même opération déjà liée, preuve de possession du contrôle, CSRF/origine et fenêtre vérifiés. La première requête jamais reçue puis reprise dans le même contexte actif peut exécuter l'intention ; après bascule B elle est refusée par génération. K différent avec credential terminé → 401, aucune liaison reconstruite depuis K. Le 401 générique et 049 anonymous demeurent de simples observations, sans reçu d'effet. Ce mécanisme supplémentaire est **proposé**, revue 14/15 requise : alternative moins complexe = conserver résultat incertain et procédure manuelle, sans reçu de révocation affirmé.

**Cookies tardifs — proposition conservatrice et limite explicite :** aucune réponse de logout, récupération, erreur ou lecture 049 ne supprime/remplace le cookie de session par Set-Cookie. La fin de session est serveur ; le secret invalide peut rester dans le navigateur jusqu'à son expiration, avec durée client bornée. Aucun effacement global Clear-Site-Data sur réponse logout tardive. Nouvelle connexion émet un secret neuf et révoque les sessions précédentes du même contexte navigateur ; le secret d'une ancienne réponse login/élévation arrivée ensuite reste invalide. Si elle écrase le cookie B, l'issue autorisée est **perte d'accès explicite et reconnexion nécessaire**, jamais retour à A ou autorisation sous une identité incorrecte. Le Web revérifie, masque le privé et explique la reprise ; aucune préservation transparente de B n'est garantie. Les réponses logout tardives n'effacent pas B dans ce profil.

Le lien de contrôle navigateur ne doit ni être choisi par un client tiers ni être fixé par URL ; secret serveur + origine/CSRF, séparation d'avec l'authentification. Sa génération et les sessions liées sont sérialisées côté serveur, y compris multi-onglets. L'amorçage concurrent de contextes et la perte de ce cookie doivent aboutir à `AUTH_CONTEXT_CHANGED`/reconnexion, jamais au rattachement silencieux d'une session étrangère. **Le détail de cette liaison, sa résistance à la fixation et les tests navigateur S04f sont une dépendance explicite 03/05/14 avant READY** ; un verrou JS local ou annuler fetch n'en constitue pas la preuve. Alternative à examiner : credentials à emplacements distincts avec résolution autoritative, plus complexe ; non adoptée ici. Aucun protocole maison déclaré sûr par cette rédaction.

### Paramètres, données et critères transversaux de ce delta

| Paramètre / proposition | Motivation / propriétaire et blocage |
| --- | --- |
| IDLE = 30 min ; ABSOLUTE = 12 h, sans remember-me L1 | Proposition Backend de départ, compromis session utilisateur/support ; 14/05/15 doivent ratifier avec menace et parcours. Expiration client au plus tard à la borne absolue, calcul serveur décisif. Non applicable par défaut aux opérateurs. |
| Activité prolongeant IDLE | Seulement opérations authentifiées d'une liste explicite liée à une interaction ; 049, polling, assets et retries de reçu exclus. Liste exacte 04/05/14 ouverte ; pas de confiance dans un booléen client « humain ». ABSOLUTE ne bouge pas. |
| Contexte préauth 30 min ; challenge 15 min ; reçu K borné au contexte | Valeurs proposées GAP-02 ; aucune prolongation par polling. Contexte de contrôle de session distinct du délai des opérations préauth : reste vérifiable pendant la session, puis fenêtre logout candidate 10 min, sans droit social ; 14/15 valident conservation et nettoyage. |
| Timeout client 10 s ; au plus 2 retries sur 30 s pour lecture/replay sûr | Proposition d'ergonomie, non SLO mesuré ; respecter Retry-After, arrêter si hors budget/fenêtre. 03/05/14 confirment ; pas de retry auto de login, d'une mutation à clé nouvelle ou d'une autre génération. |
| Quotas, tailles IDs/secrets, politique password, bornes des DTO/capacités, marge d'horloge, CONTEXT_MAX_AGE | **OUVERTS** : 14/03/05/15 selon domaine ; critères nominaux rédigibles, tests de bornes et gel bloqués. Horloge serveur UTC, jamais timestamp client comme autorité. |
| Retention après usage, audits, refus, preuves et sauvegardes | **OUVERTE 15/14** ; expiration d'un secret ≠ délai légal d'effacement du compte. Aucune reprise implicite de 90 jours analytics/sécurité ni de sept jours export. |

| Données conceptuelles nécessaires / finalité | Accès et cycle proposés |
| --- | --- |
| Identifiant privé, preuve de vérification canal, credential hash/epoch ; authentifier | Module auth seulement ; email absent du contexte courant ; hash dédié, pas de secret réversible ; export sans secrets, suppression/exception selon 15. Identité civile/origine/pays marketing non collectés par ce flux. |
| Challenge : purpose, sujet interne, empreinte protégée, expiry, essais, consumed_at | Consommation unique et compteur atomiques ; support ne lit pas le code. Tombstone empêche réutilisation après purge du reçu K ; rétention minimale et protection backup à ratifier. |
| Contexte/K : empreinte de liaison, opération/version, empreinte d'entrée protégée, statut, reçu expurgé, expirations | Pas de stockage de corps password. Accès technique borné au module ; purge selon finalité validée ; échec du store ne permet pas une mutation non dédupliquée. |
| Session : référence interne, empreinte du secret, compte, credential_epoch, génération navigateur, issued/last_interactive/expires/revoked | Autorité transactionnelle, révocation consultable au point d'accès ; pas de session_id brut dans DTO. Révision de droits indépendante. Restauration ne rouvre pas l'accès. |
| Reçu logout : opération, session capturée, génération, effet/instant serveur, échéance | Lecture limitée au contexte de contrôle vérifié, résultat sans ID de compte ; expiration ne réactive jamais la session. Aucun endpoint public de recherche de session. |
| Audit transitions sensibles et diagnostic | Audit durable associé aux changements auth ; logs séparés request_id/classe/latence sans cookies, CSRF, K brut, email, challenge ou password. Panne d'audit obligatoire avant commit → mutation refusée ; panne diagnostic seule n'annule pas un commit. Politique/rétention 14/15, GAP-08. |

Codes de ce delta héritent de l'enveloppe C3 `{code,message_key,request_id,field_errors?}`. `request_id` ne sert pas d'autorisation. HTTP 410 pour preuve authentique expirée et 409/401 préauth sont des **extensions proposées** au mapping v0.1 ; clients 05 doivent les accepter avant gel. Messages de formulaire n'échoent aucune valeur secrète. JSON/session/bootstrap et erreurs sensibles : `no-store`. Mode membre restreint demeure authentifié uniquement si matrice 09/14/15 l'autorise ; incapacité d'obtenir les droits courants refuse l'accès, jamais un rôle par défaut.

### Critères vérifiables — rattachement QA existant

Tous les scénarios ci-dessous sont **PLANNED**, jamais exécutés dans cette contribution. Oracles proposés à 18 ; les valeurs encore ouvertes rendent les cas aux bornes BLOCKED pour exécution. Repères locaux L1-BE, aucun nouveau TEST global.

| Repère / rattachement | Précondition → action → résultat observable |
| --- | --- |
| L1-BE-01 ; S01, TEST-0401, TEST-1801/1802 | Activation committée, réponse coupée → même contexte/K/corps → un seul compte activé, reçu identique sans session ; K différent → challenge consommé ; preuve recovery jamais acceptée comme activation. |
| L1-BE-02 ; S01/S04g, TEST-1402, TEST-1804/1833 | K connu mais contrôle absent/autre contexte → lire/rejouer → refus sans reçu ; changer l'entrée → 409 ; avant/à/après expiry → règle temporelle exacte ; même clé en cours → aucune seconde mutation. |
| L1-BE-03 ; S03a/b/h, TEST-0402/0403, TEST-1832 | Charger sans mémoire puis actif/restreint/expiré → 049 → union exacte et compte/profil distincts ; 200 anonyme sans privé ; ID cible refusé ; aucune capacité inconnue accordée. |
| L1-BE-04 ; S03c/e/g, TEST-1401, TEST-1833/1834 | Panne autorité puis lecture répétée automatique → 503/pas de faux logout ; horloge avance → pas de prolongation par 049 ; action interdite refusée malgré ancien DTO. |
| L1-BE-05 ; S03d/f, TEST-WEB-0004, TEST-1832/1833 | A puis B, inverser lectures profil/contexte et revenir par historique/onglet → aucune vue privée A ; 401 A tardif ne déconnecte pas B ; cache service worker exclu. |
| L1-BE-06 ; S04a/b/c, TEST-1803/1833 | Logout A confirmé/perdu avant ou après commit → même opération et contexte → 204 uniquement si effet établi ; sans liaison → 401/incertitude ; tentative sous B → 409 sans révocation B. |
| L1-BE-07 ; S02/S04d/e, TEST-1401/1419, TEST-1803 | Profil sans refresh retenu → deux appels 004 → 404 et zéro session/cookie créé ; régénération/login contre logout → aucune continuation valide après la révocation confirmée. Si option refresh retenue, cet oracle doit être remplacé par son contrat approuvé avant READY. |
| L1-BE-08 ; S04f, TEST-WEB-0004 | Navigateur réel : retarder Set-Cookie login A, révoquer A, connecter B, livrer A ; ancien secret refusé, jamais identité A ; si B perdu, reauth explicite. Retarder logout A : aucun header supprimant B. Refaire multi-onglets et amorçage concurrent. |
| L1-BE-09 ; S04g, TEST-1402, TEST-1803/1804 | Sessions sur deux appareils, double consommation recovery et login ancien secret en cours → un reset, anciennes sessions invalides, login stale refusé ; nouveau login autorisé selon droits ; aucune sanction/MFA contournée. |
| L1-BE-10 ; S04h/S08, TEST-1415, TEST-1833 | Horloge contrôlée et canaris secrets → bornes d'expiration, logs expurgés, pas de droit sur panne ; restauration isolée → secrets pré-restauration non acceptés. Preuve runtime future indispensable. |
| L1-BE-11 ; W03, TEST-WEB-0003, TEST-1401/1418 | Origine étrangère/CSRF absent sur login/logout/reset et identité inexistante/existante → refus mutation, réponses neutres comparées (corps/statut/temps) ; aucune émission répétée de mail par replay. Mesure de timing sur environnement réel, pas égalité supposée. |

### Avis ciblés préparés, décisions attendues et limites

Statut de chaque demande ci-dessous : **À TRANSMETTRE ; avis NON REÇU**. Le présent document constitue la réponse 04, pas la réception/approbation des équipes citées. Les références INT existantes sont réutilisées.

| Destinataire / référence | Delta exact à examiner et résultat attendu | Effet |
| --- | --- | --- |
| 05 Web, INT-0407 | GAP-01 transport même origine ; GAP-02 tableau K ; GAP-03 chaque champ/règle ; GAP-04 logout incertain, deux comptes et cookies tardifs. Confirmer/amender C-IDENTITY/W03/W04 et la branche perte de session → reconnexion, messages/accessibilité avec 02/16 | Bloque gel des interfaces consommées ; ne demande pas réanalyse des autres pages. |
| 14 Sécurité + 03, INT-0402/0404 | Identité/password vs options, fixation/contexte/CSRF, liaison K, secret/epoch/atomicité, suppression du refresh Web, reçu logout et paramètres. Fournir avis menace et contraintes, choix des primitives éprouvées, cas adverses/valeurs motivées | Bloque auth/modèle et READY ; aucune sécurité déclarée vérifiée par Backend. |
| 15 Privacy + 09 pour projection seulement, INT-0403/0405 | Necessité des champs account_ref/profile_ref, restricted/capacités, données auth/K/contexte/reçu et durées ; accès après suspension, récupération et canal alternatif. Fournir projection minimisée et cycle autorisé | GAP-05/06/08 restent ouverts ; aucun réexamen général des marchés demandé. |
| 18 QA, INT-0408 | Confirmer oracles L1-BE-01…11 et mapping S01–S04h/W03/W04 ; compléter ordre commit/livraison, cookies réels, avant/à/après expiry et preuves de panne | Tests PLANNED ; ne pas les marquer PASS à partir du validateur documentaire. |
| HQ + 03/20/21 | Arbitrer uniquement identité/transport/refresh/revocation selon avis ; 21 examine les amendements de §4.1/4.2 et le raccordement, 20 conserve gate L1 | Réception du delta ≠ fermeture GAP, ni autorisation code/pilote. |

Ajustement proposé à 21, **sans modifier son fichier propriétaire** : ajouter un lien vers ce delta, décrire « réponse 04 rédigée » sur les quatre lignes après réception, conserver les GAP ouverts ; remplacer les placeholders §4.1/4.2 seulement après les accords. Les onze API historiques ne couvrent pas API-BE-049 ni auxiliaire/extension logout : les ajouter à la matrice de raccordement lors de la convergence. S04f doit accepter uniquement l'issue explicite et observable de reconnexion si B n'est pas conservé ; aucun succès transparent inventé.

Risques RISK-0402/0403/0405 précisés : contexte préauth pris pour identité ; mot de passe/challenge dérivable d'un registre K ; rejeu de logout visant B ; secret tardif rétablissant A ; récupération n'invalidant pas un login ancien concurrent. Mesures proposées ci-dessus, **risques ouverts**. Le contrôle navigateur/epoch ajoute de la complexité : 14/03 doivent démontrer sa nécessité et sa réalisation sûre ou retenir une alternative moins complexe avec limites utilisateur explicites. Pas de fermeture automatique des autres GAP.

Appuis externes limités, consultés le 30 septembre 2026 : [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) pour invalidation serveur, cookies et expirations ; [OWASP Forgot Password](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html) pour réponse neutre, preuve unique et absence de connexion automatique après reset ; [MDN Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie) pour traitement navigateur des cookies. Les valeurs, DTO, choix de transport et mécanismes de concurrence ci-dessus sont **des propositions Backend**, pas des prescriptions ni une validation de protocole par ces sources.

### Compte rendu de ce delta

1. **Décisions prises / à valider :** réponse propriétaire GAP-01…04 rédigée ; avis candidat §4.1 amendé, options email/password + cookie opaque + lecture dédiée + absence de refresh Web recommandées, pas approuvées. Durées proposées distinctes des paramètres ouverts.
2. **Livrable :** présent document v0.2, source historique v0.1 conservée ; [rapport de contrôles](../quality/backend-contract-validation.md) complété. Publication par PR empilée sur #27 ; SHA et diff vérifiés dans la description de PR.
3. **Tests :** contrôles documentaires seulement, résultats dans le rapport ; aucun code applicatif ni test API/session/navigateur/sécurité/charge exécuté ; L1-BE et QA restent PLANNED.
4. **Questions ouvertes :** choix structurants, garantie de liaison navigateur/epoch et reçus, preuve d'identité, paramètres/quotas, projection de droits, conservation et délivrabilité ; propriétaires dans les matrices.
5. **Dépendances :** avis 05/14 puis 09/15 sur l'impact borné, oracles 18, architecture 03 et convergence HQ/21/20 ; À TRANSMETTRE, NON REÇUS.
6. **Risques :** identités/cookies/résultats confondus et fausse fermeture des GAP ; limitations du protocole et issue de reconnexion explicitement conservées.
7. **Suite / HQ :** transmettre les quatre avis ciblés, trancher avec leurs propriétaires, mettre à jour les seules matrices impactées puis revoir les gates L1. Aucun merge, code ou GO pilote autorisé par ce delta.
