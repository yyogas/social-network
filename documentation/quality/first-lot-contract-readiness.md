# Préparation contractuelle du lot L1 — compte, session et profil

**Entrée actualisée — 30 septembre 2026 :** [DIR-012](../project-governance/decision-register.md) confirme une audience universelle et des priorités marketing mondiales. Les pays servis, langues et règles d'admission restent ouverts ; les GAP applicables à ces paramètres doivent reprendre cette entrée. Aucune origine utilisateur n'est déduite d'un marché marketing.

## 1. Identification et verdict

| Champ | Valeur |
| --- | --- |
| Référence / version | SN-INT-M0-L1-001 — v0.4 ; repères GAP-L1 et S locaux, sans réserver de DEC/ADR/API/TEST global |
| Date | 30 septembre 2026, Europe/Paris |
| Propriétaire | 21 — Intégration / Code Review |
| Destinataires | HQ, 03/04/05/09/14/15/18/20 ; 02/08/10/16 selon les dépendances ci-dessous |
| Références Git | `main` : `ba26729aa10dc497338a960ae78ba904a72216b2` ; dossier d'arbitrage reçu dans la PR #27 au SHA `277a7e100d9f6c4e7e0d929e6bb679ed8d70fa82` |
| Statut | **PROPOSÉ — revue documentaire de préparation**, sans approbation des contrats propriétaires |
| Verdict | Préparation documentaire poursuivable ; **L1 BLOQUÉ POUR CODE** selon les gates de 20 ; aucun verdict de fonctionnement applicatif |
| Contribution indispensable | Rendre vérifiables les raccordements producteurs/consommateurs, nommer les décisions manquantes et les preuves de sortie avant que chaque implémentation invente ses règles |
| Périmètre | L1 de 20 : J01, FEAT-001 à 004/018/021 ; effets du blocage/suspension au niveau du contrat ; dépendance avatar L2 |

### Sources et nature des constats

Sources de domaine reçues : [contrats Backend](../backend/api-contract-candidates.md), [exigences Web](../web-application/web-requirements.md), [Sécurité](../security/security-operations-requirements.md), [Privacy](../privacy/privacy-requirements.md), [Safety](../trust-safety/moderation-requirements.md), [lots et gates de 20](../delivery/implementation-readiness.md), [matrice QA](acceptance-test-matrix.md) et [dossier d'arbitrage](../project-governance/m0-mvp-arbitration.md). Lecture ciblée des contrats L1 et de leurs dépendances directes ; les 21 contributions ne sont pas réauditées.

| Nature | État observé / portée |
| --- | --- |
| CONFIRMÉ | Onze routes candidates API-BE-001 à 011 sont rédigées ; les règles communes C1–C8 couvrent déjà validation, erreurs, reprise, idempotence, versions, accès et audit. Les routes héritent de ces règles. |
| CONFIRMÉ | Web demande un état utilisateur et des capacités pour AppShell/C-IDENTITY. Le catalogue Backend examiné ne décrit pas l'opération de restitution de cette identité après rechargement ; cela ne prouve pas l'absence d'une solution future. |
| PROPOSÉ | Matrice de raccordement, demandes GAP-L1-01 à 08, candidats identité courante (§4.1) et cycle de session/reprise (§4.2), scénarios de cette pièce ; aucune route ni politique nouvelle n'est approuvée. |
| À VÉRIFIER | Choix d'identité, transport, admission, audiences, états de compte, durées, limites, architecture et accord des consommateurs. |
| NON REÇU | Arbitrage HQ de portée, contrats critiques approuvés, schémas exécutables L1, application, environnement et preuves applicatives. Aucun avis d'équipe n'est déduit de la publication. |

Les points ouverts sont des écarts de préparation documentaire, pas des vulnérabilités démontrées. Les contrats candidats les signalent déjà pour la plupart. Cette pièce apporte leur rapprochement et le constat ciblé GAP-L1-03. Elle ne constitue pas une revue indépendante de ses propres propositions.

## 2. Fonctionnalités, phases et limites

| Fonctionnalité / besoin | Acteurs, résultat attendu et précondition | Classement reçu / proposition locale |
| --- | --- | --- |
| FEAT-001 — admission et activation | Visiteur admissible ; compte unique activé avec preuve valide ; politique d'admission et méthode d'identité requises | MVP P0 proposé ; L1 |
| FEAT-002 — accès, session et récupération | Titulaire ; accès limité à ses droits actuels, déconnexion effective et récupération vérifiée | MVP P0 proposé ; L1 |
| FEAT-003 — profil minimal | Propriétaire édite ; lecteur voit seulement les champs autorisés ; limites et visibilité reçues | MVP P0 proposé ; L1 ; avatar avec L2 conformément à 20 |
| FEAT-004 — paramètres de visibilité | Propriétaire choisit une politique disponible ; service applique cette politique à la lecture | MVP P0 proposé ; contrat L1, propagation aux objets des lots suivants |
| FEAT-018 — surface et accessibilité | Utilisateur du client retenu ; formulaires, états et reprise utilisables au clavier et avec lecture assistée | MVP P0 proposé ; Web recommandé dans C1/C2, surface à arbitrer |
| FEAT-021 — langues du pilote | Utilisateur comprend les parcours critiques ; locale et contenu Unicode restent distincts de l'admission | MVP P0 proposé ; langues à arbitrer avec 16 |
| Clients natifs, messagerie et communautés selon B1 | Aucun contrat applicatif supplémentaire imposé à L1 ; FEAT-020 reste MVP conditionnel dans le catalogue tant que HQ n'a pas arbitré | Phase 2 candidate selon le dossier ; aucun reclassement adopté ici |
| Recommandation avancée / publicité ; extension pays/langues ; ambitions ultérieures | Hors revue L1 ; ne justifient pas de collecte ou d'architecture anticipée | Phase 3 / International / Long terme selon le dossier et les propriétaires ; inchangés |

**Correspondance des lots :** conserver les identifiants L0–L7 de 20. Les ordres 0–4 du dossier HQ regroupent des travaux et ne les renumérotent pas. L1 seul n'autorise pas l'ouverture du pilote ; les contrats de recours, droits sur les données et préparation opérationnelle commencent pendant L1, leurs preuves intégrées arrivent avec les lots concernés.

## 3. Raccordement des onze API candidates

Producteur : **04 Backend** ; consommateur initial candidat : **05 Web**, avis 14 sur identité et autorisation. 06 participe si un client natif est retenu ; son implémentation n'est pas un prérequis automatique du Web. Les formes et statuts ci-dessous sont ceux des propositions reçues, avec héritage C1–C8. Les exemples et `*_proof` ne définissent pas un protocole cryptographique.

| Contrat reçu | Entrée → sortie / succès candidat | Règle, état ou erreur déjà couvert | Complément de préparation / test existant |
| --- | --- | --- | --- |
| API-BE-001 — POST `/auth/registrations` | identity, locale, registration_proof → AccountReceipt / 202 | Visiteur, admissibilité, clé K ; ADMISSION_UNRESOLVED, RATE_LIMITED | GAP-01/02/07 ; AC-BE-01, TEST-1801 |
| API-BE-002 — POST `/auth/activations` | challenge → AccountReceipt actif / 200 | Preuve liée et à usage unique, K ; CHALLENGE_EXPIRED/CONSUMED | GAP-02/07 ; AC-BE-01, TEST-1801/1802 |
| API-BE-003 — POST `/auth/sessions` | identity, credential_proof → SessionResult / 201 | Pas de retry aveugle ; AUTH_INVALID, RATE_LIMITED | GAP-01/03/04 ; AC-BE-02, TEST-1803/1804 |
| API-BE-004 — POST `/auth/session-refresh` | refresh_proof → SessionResult / 200 | Rotation/rejeu/perte de réponse explicitement ouverts ; SESSION_REVOKED, REFRESH_REPLAY | GAP-01/04 ; AC-BE-02, TEST-1803/1833 |
| API-BE-005 — DELETE `/auth/sessions/current` | Vide → vide / 204 | Révocation, répétition sans effet supplémentaire ; AUTH_REQUIRED | GAP-04 ; AC-BE-02, TEST-1803/1833 |
| API-BE-006 — POST `/auth/recovery-requests` | identity → accepted / 202 | Réponse/temps neutres, K/anti-abus ; RATE_LIMITED | GAP-01/02/07 ; AC-BE-02, TEST-1804/1845 |
| API-BE-007 — POST `/auth/recoveries` | challenge, replacement_proof → completed / 200 | Preuve unique, K ; révocation des sessions ouverte ; CHALLENGE_EXPIRED | GAP-02/04 ; AC-BE-02, TEST-1803/1804 |
| API-BE-008 — GET `/profiles/{id}` | ID → Profile / 200 | Lecteur autorisé, C6 ; RESOURCE_UNAVAILABLE | GAP-03/05/06 ; AC-BE-03, TEST-1832/1848 |
| API-BE-009 — PATCH `/me/profile` | display_name, bio, avatar_id → Profile / 200 | Propriétaire, Vn, avatar autorisé/prêt ; VALIDATION_FAILED, MEDIA_NOT_READY | GAP-05/06/07 ; AC-BE-03, TEST-1848 |
| API-BE-010 — GET `/me/settings` | Vide → Settings / 200 | Propriétaire, données privées ; AUTH_REQUIRED | GAP-03/05/06 ; AC-BE-03, TEST-1832/1837 |
| API-BE-011 — PATCH `/me/settings` | locale, visibility_policy → Settings / 200 | Propriétaire, Vn, valeurs approuvées ; POLICY_INVALID | GAP-05/06/07 ; AC-BE-04, TEST-1832/1837 |

Dans cette matrice seulement, GAP-01 signifie GAP-L1-01, etc. Les erreurs communes incluent 401, 403/404 selon divulgation autorisée, 409, 412 et 428 pour Vn, 422, 429 avec Retry-After et 503. L'enveloppe reçue est `{code,message_key,request_id,field_errors?}`. 04/05 doivent fixer le mapping et les actions utilisateur ; les libellés de 14 et les HTTP génériques du Web ne constituent pas un second contrat concurrent.

## 4. Écarts à fermer et preuves demandées

Chaque ligne désigne un complément précis, pas une demande de réécriture de la contribution entière. Statut de toutes les demandes : **À TRANSMETTRE** aux propriétaires ; leur présence dans GitHub ne prouve ni envoi individuel, ni réception, ni approbation.

| Repère local / rattachement existant | Question et livrable attendu | Propriétaires / impact bloquant |
| --- | --- | --- |
| GAP-L1-01 — INT-0404, SYN-001/003 | Quelle méthode d'identité et quel transport pour le client retenu ? Fournir diagramme inscription/activation/connexion/récupération, preuve et vérification par étape, stockage client, CSRF/origine, neutralité des refus et paramètres d'expiration. Cookie opaque proposé par 14 et jeton éventuel restent des options. | 04/14 + 03/05/15, arbitrage HQ si structurant ; bloque contrat auth et modèle de données associé |
| GAP-L1-02 — INT-0402/0404 | Comment lier K à un contexte préauthentifié vérifié, consommer une preuve une fois et reprendre après perte de réponse ? Tableau : même contexte/même clé/même entrée ; clé différente ; entrée différente ; preuve consommée ; expiration ; mutation en cours. Fixer fenêtre K et réponse récupérable sans exposer un compte. La règle commune de liaison existe déjà. | 04/14 + 03/05 ; bloque 001/002/006/007 et leurs tests de concurrence/reprise |
| GAP-L1-03 — INT-0407, C-IDENTITY | Après rechargement, d'où viennent l'ID du compte, son état et ses capacités actuelles ? SessionResult ne contient pas d'ID de compte explicite et aucune opération de restitution n'est décrite dans le catalogue examiné. Examiner le candidat §4.1 : bootstrap serveur ou lecture dédiée, schéma, rafraîchissement/invalidation, état anonyme et panne. Ne pas imposer ici une route `/me`. | 04/05/14 ; bloque intégration AppShell/profil et restauration de session ; **OUVERT — candidat rédigé, avis propriétaires NON REÇUS** |
| GAP-L1-04 — INT-0404 | Examiner le candidat §4.2 : rotation concurrente/réponse perdue/expiration/révocation/récupération/déconnexion répétée, portée des sessions visées, durées, instant d'effet et preuve de réconciliation. Un 401 après perte du 204 ne prouve pas à lui seul la révocation de la session initiale. | 04/14/05, avis 15 ; bloque 003–007 et l'oracle de TEST-1803 ; **OUVERT — candidat rédigé, avis propriétaires NON REÇUS** ; aucune durée décidée ici |
| GAP-L1-05 — INT-0403/0405, SYN-006 | Fournir acteur × état de compte × opération × objet : lecture/modification profil/paramètres, session, accès restreint recours/privacy. Fixer visibilité initiale, blocage et ordre avec une mutation concurrente, refus masqué ou explicite. Désigner la source actuelle des droits et comportement si indisponible. | 04/09/14/15 + 10, consommation 05 ; bloque autorisations L1. Implémenter tout L4/L5 n'est pas nécessaire pour approuver ce contrat ; leurs preuves restent requises avant pilote. |
| GAP-L1-06 — INT-0405/0406/0407, SYN-002/004 | Rendre le schéma L1 exact : champs identité/profil séparés, null/absent, taille/unité/Unicode, enums locale/politique, sens de notification_preferences reçu mais encore générique. Appliquer l'option de 20 pour l'avatar : différé jusqu'à L2 ou dépendance intégrée ; documenter réponse/validation effective à L1. Fournir catégories, finalités, accès et rétention, sans importer les durées analytics. | 04/15/05 + 02/08/16, HQ pour langues/audience ; bloque les champs et politiques concernés, pas la rédaction des autres contrats |
| GAP-L1-07 — INT-0402/0404/0407 | Livrer schémas et réponses cohérents : AccountReceipt couvre pending_verification et l'état active annoncé par 002 ; erreurs/status/headers corrélés, 428/412/Vn, limites et Retry-After, timeout/retry et résultat inconnu. Fixer seuils avec leur justification et mode panne. Joindre exemples valides/invalides synthétiques et accord consommateur. | 04/05/14 + 18, avis 03 ; bloque gel du contrat consommé et tests aux bornes ; catalogue reçu conceptuel, pas un schéma exécutable défectueux |
| GAP-L1-08 — SYN-003/005, INT-0408, gates 20 | Rattacher les contrats retenus à la décision de portée/surface/architecture, au modèle de persistance/migration et à une stratégie de test/exploitation L1. Fixer événements d'audit, champs interdits, panne du journal et restauration sans réactivation de sessions. Budget/charge/reprise ont des valeurs et propriétaires, pas des valeurs implicites. | HQ/03/04/14/15/18/20 ; architecture/modèle nécessaires avant code ; preuves runtime nécessaires avant verdict fonctionnel, objectifs d'ouverture avant GO pilote |

**Options et recommandation d'intégration :** reprendre l'option de 20 « profil sans avatar jusqu'à L2 » pour réduire les dépendances du premier lot, sous confirmation 01/04/05/08 ; si l'avatar est indispensable dès L1, intégrer explicitement le contrat et les preuves médias. Pour GAP-L1-03, bootstrap et lecture dédiée sont deux solutions recevables si les droits courants, l'expiration et les erreurs sont observables. 21 recommande de résoudre ce raccordement avec le choix de session, sans choisir à la place de 03/04/05/14. Toute décision majeure rejoint les DEC/ADR existants via HQ.

### 4.1. GAP-L1-03 — candidat de restitution de l'identité courante

**PROPOSÉ par 21, MVP P0 candidat, FEAT-002/003/004/018 ; avis 04/05/14 NON REÇUS.** Delta préparé à partir du head PR #27 `c3e9f1b3d344fd3707ad6c87564a5fff0ca0cdcc` et des sources de domaine citées au §1. Objectif : AppShell retrouve le compte connecté et les actions affichables après rechargement, sans confondre absence de session, restriction et panne. Cette proposition ne ferme aucun GAP et n'ajoute pas d'API officielle, de stack, de mécanisme cryptographique ou de droit.

#### Options, frontière et schéma conceptuel

| Option à examiner | Avantage / coût / condition |
| --- | --- |
| Lecture dédiée du contexte courant | Réponse et erreurs explicites, réutilisables au chargement et lors d'une nouvelle vérification ; requête supplémentaire, quota et latence à mesurer. Méthode GET candidate, chemin et identifiant API attribués par 04 après accord. |
| Contexte fourni avec la page par le serveur | Peut éviter une requête initiale ; exige une page personnalisée non partagée, une sérialisation sûre et un moyen explicite de revérifier les droits sans réutiliser indéfiniment le contexte initial. N'impose pas de rendu serveur à la stack. |

**Recommandation :** faire approuver une même sémantique de contexte avant de choisir son transport avec 03/04/05/14. Une lecture dédiée est la candidate si le client charge une coque statique ; un bootstrap convient si l'architecture retenue rend déjà la page par session. Ces conditions ne sont pas encore établies. Un contexte conservé dans le navigateur ne remplace aucune des deux options ni le contrôle serveur C6. Impacts : une interface de plus à maintenir ou une réponse HTML à personnaliser, une stratégie de reprise Web et des preuves de cache/session ; aucun service supplémentaire ni budget chiffré déduit.

Entrée métier **vide** : l'identité est dérivée de la session vérifiée, jamais d'un `account_id`, d'un profil ou d'une capacité fournis par le client. L'authentification et le transport du credential suivent GAP-01/04. Pas d'identité cible arbitraire, d'usurpation support ou de lookup d'email ; un paramètre métier inconnu est rejeté selon C2. Lecture sans activation, récupération, consommation de challenge, création de session ou rotation implicite du credential ; l'effet éventuel sur l'activité de session doit être tranché avec 14.

| Champ candidat | Type / présence / finalité et limite |
| --- | --- |
| `authentication` | Obligatoire ; `anonymous` ou `authenticated`. Désigne le résultat de la vérification, pas l'état métier du compte. Valeurs proposées, non réservées globalement. |
| `viewer` | Obligatoire ; `null` seulement pour `anonymous`, objet seulement pour `authenticated`. Aucune capacité ou référence privée dans la variante anonyme. |
| `viewer.account_ref` | `Id` opaque obligatoire ; rattachement du contexte au compte, jamais preuve d'autorisation. 04/15 confirment nécessité, format et projection ; aucune nouvelle clé de base imposée. |
| `viewer.profile_ref` | `Id` opaque ou `null`, champ obligatoire ; référence utilisable par API-BE-008, `null` si aucun profil n'est exposable dans cet état selon le contrat approuvé. Ne pas supposer `Profile.id = account_ref` ; 04 fournit le mapping. |
| `viewer.account_state` | `State` obligatoire ; vocabulaire/version et projections exposables approuvés par 04/09/14/15. État métier distinct de la validité de session. |
| `viewer.allowed_capabilities` | Tableau de `Code` obligatoire, sans doublons ; uniquement capacités approuvées pour ce contexte. Tableau vide possible ; aucune capacité implicite du seul fait d'être connecté. Ne remplace pas l'autorisation par objet à chaque opération. |

Exemples **synthétiques**, non exécutables comme contrat validé ; `active` et `social.read` reprennent seulement l'exemple Backend reçu :

```json
{"authentication":"anonymous","viewer":null}
```

```json
{"authentication":"authenticated","viewer":{"account_ref":"account_demo","profile_ref":"profile_demo","account_state":"active","allowed_capabilities":["social.read"]}}
```

Ce DTO candidat est une projection privée du contexte, pas un remplacement décidé de `SessionResult`. Ne pas y copier email, date de naissance, résidence, origine, préférence marketing, motif de sanction, credential ou `session_id` sans besoin approuvé. Profil et paramètres restent des lectures séparées ; la locale d'interface ne prouve ni pays d'admission ni origine. Une panne de ces lectures ne déconnecte pas automatiquement un contexte d'identité valide. Conservation client proposée : mémoire du contexte courant uniquement ; toute collecte, export, suppression, rétention serveur et sauvegarde des données sources relève des contrats de 04/15, sans nouveau stockage métier exigé ici.

#### Réponses, états et reprise proposés

Le contrat doit rendre observables les mêmes résultats avec les deux transports. Pour une lecture dédiée, **200 avec variante explicite anonyme/authentifiée est proposé**, y compris lorsqu'une session présentée est reconnue expirée ou révoquée. Cela permet l'entrée normale sans session ; ce n'est pas une modification du 401 des autres routes protégées de C3. Alternative recevable : 401 pour l'absence de session valide, à mapper explicitement par 04/05/14. Choisir un mapping unique et documenter ses headers avant READY. Aucun credential ou compte fourni n'est validé par ce seul exemple.

| Observation autoritative ou événement | État et résultat Web candidats | Reprise / point à approuver |
| --- | --- | --- |
| Chargement, rechargement ou restauration d'une vue privée | `VERIFYING` ; contenu privé masqué jusqu'à vérification dans le contexte courant | Une opération logique en cours ; libellé accessible et reprise sans déplacement de focus intempestif ; 02/05/16 |
| Session valide et projection cohérente | `AUTHENTICATED`, ou `RESTRICTED` selon les états approuvés ; afficher seulement les capacités reconnues | Aucun privilège opérateur implicite. Une restriction sociale ne supprime pas les voies recours/privacy approuvées ; 04/09/14/15 |
| Absence de session, expiration ou révocation reconnue | `ANONYMOUS`, supprimer le contexte privé local ; proposition 200 anonyme | Reconnexion explicite ; ne pas annoncer la suppression du compte ni expliquer à un tiers un motif interne |
| Source d'identité/droits indisponible | 503 selon C3, `UNAVAILABLE`, aucun contexte privé présenté comme actuel | Pas de réponse anonyme fabriquée, de droits par défaut ni de faux succès logout ; reprise bornée selon C4 |
| Timeout, réseau interrompu, réponse illisible ou incohérente | `UNAVAILABLE`, données protégées masquées | Réessayer la lecture dans le contexte courant ; l'échec ne prouve ni expiration ni révocation |
| Entrée métier non autorisée / quota | 400 / 429 avec enveloppe C3 ; `Retry-After` pour 429 | Pas de retry automatique du 400 ; budget et délai bornés pour 429/503/réseau, puis action manuelle accessible |
| Authentification ou récupération terminée, changement de droits appris | Invalider le contexte précédent, revenir à `VERIFYING` | Nouvelle lecture avant de présenter ses droits comme actuels ; pas de boucle illimitée 401 → refresh → retry |
| Déconnexion demandée, réponse perdue | Masquer les données privées et montrer un état de confirmation incertaine | Ne pas annoncer la révocation serveur du fait d'un effacement local. Une lecture ultérieure indique la session courante, pas la révocation de toutes les autres sessions ; GAP-04 fixe l'oracle |

Les erreurs reprennent `{code,message_key,request_id,field_errors?}` ; 04/05/14 définissent les codes et headers précis. Ne pas transformer tout 403/404 d'une ressource en déconnexion. Les projections incohérentes (`anonymous` avec objet privé, `authenticated` sans référence obligatoire) sont inutilisables. Champs de réponse additionnels tolérés selon C8 ; enum d'authentification/état inconnu : accès protégé non accordé et reprise explicite. Une capacité inconnue n'accorde rien ; les capacités connues continuent de suivre le contrat approuvé. 09/15 définissent la voie de reprise sûre si l'incompatibilité empêche l'affichage du recours/privacy ; aucune validation d'un droit par le seul client.

#### Concurrence, cache et paramètres bloquants

1. Chaque requête cliente est rattachée au contexte local qui l'a émise. À la déconnexion, reconnexion, restriction connue ou bascule de compte, invalider les requêtes précédentes et purger leurs vues, formulaires privés et caches dérivés. Une réponse tardive de A, même 200, ne remplace pas le contexte B ; une réponse anonyme ou un 401 tardif de A ne déconnecte pas B. Appliquer cela également aux requêtes de profil/paramètres. Une génération locale en mémoire est une option d'implémentation Web, pas un jeton d'autorisation. L'annulation réseau ne prouve pas l'annulation serveur.
2. Ordonner également les vérifications concurrentes dans un même contexte : ne pas laisser une réponse plus ancienne écraser un résultat plus récent. 05 choisit sérialisation ou rejet des réponses périmées. Les messages inter-onglets sont des signaux d'invalidation ; le contrôle serveur demeure décisif. Effets des réponses de session concurrentes sur les cookies/credentials et rotation restent dans GAP-04 : ce DTO ne résout pas ce protocole.
3. Appliquer la proposition C6 `Cache-Control: no-store` au contexte, y compris aux réponses anonymes/erreurs de cette lecture et à la page si elle embarque des données privées. Exclure ce contexte du cache partagé, du cache applicatif/service worker et du stockage persistant client. Tester séparément retour navigateur, restauration d'onglet et cache de page : le header n'est pas une preuve de purge rétroactive. Aucune promesse de rappel des données déjà reçues ; aucun effacement global du navigateur imposé ici.
4. Revérifier au chargement et aux événements du tableau ; la détection d'un changement distant silencieux et sa borne d'obsolescence d'affichage sont à définir par 04/05/14. Les nouveaux accès serveur utilisent toujours les droits courants C6. Un polling, un push ou une durée de cache ne sont pas choisis implicitement. La vérification de contexte ne doit pas maintenir une session indéfiniment par simple activité automatique ; le calcul d'inactivité et l'expiration absolue restent serveur, selon GAP-04.
5. Journal diagnostic candidat : identifiant de requête validé, classe de résultat et latence, selon C7 ; pas de corps privé, token ou ID de session brut. 14/15 fixent accès/rétention et événements d'audit nécessaires. Une panne de diagnostic n'entraîne pas à elle seule une déconnexion.

Appui technique limité : [OWASP, Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html), sections « Manual Session Expiration » et « Web Content Caching », consultées le 30 septembre 2026 Europe/Paris. Elles préconisent l'invalidation serveur à la déconnexion et la maîtrise du cache des réponses sensibles. Elles ne valident ni ce DTO, ni un choix de transport, ni la politique du projet. L'avis Sécurité reste requis.

| Réponse propriétaire attendue — **À TRANSMETTRE** | Critère de sortie / impact |
| --- | --- |
| 03/04/05/14 : choisir lecture ou bootstrap, absence de session 200/401, interaction avec login/refresh/logout | Schéma, headers et transitions cohérents avec GAP-01/04 ; bloque le raccordement C-IDENTITY |
| 04/09/14/15 : fixer mapping compte/profil, états, capacités et cas de restriction ; 15 confirme la minimisation | Matrice et fixtures active/restreinte/anonyme ; bloque les projections et permissions, sans exposer les motifs internes |
| 04/05/14 : fixer tailles IDs, limites des listes/codes, timeout, nombre/délai maximal de retries, quota, borne d'obsolescence et effet sur l'activité de session | Valeurs justifiées et cas limites reproductibles ; aucune valeur inventée par 21 ; bloque READY |
| 05 avec 02/16 : décrire cache/historique/onglets, rejet des réponses anciennes, états et messages de reprise | Accord consommateur et parcours accessibles dans les langues retenues ; bloque intégration Web |
| 18 avec 04/05/14 : rattacher les sous-cas S03a–h du §6 aux tests existants | Oracles et fixtures versionnés, puis preuves exécutées sur SHA ; bloque verdict fonctionnel, pas la rédaction |

### 4.2. GAP-L1-04 — candidat de cycle de session et de réconciliation

**PROPOSÉ par 21, MVP P0 candidat, FEAT-002/018 ; avis 04/05/14/15 NON REÇUS.** Entrée Git : PR #27 `9ce0118d2a6072347f4d8c07d37a149f4d161894`. Sources ciblées : API-BE-003 à 007, C1/C3–C8, REQ-1401/1402, C-IDENTITY et W03/W04. Ce complément précise les issues à faire ratifier ; les contrats Backend restent candidats, aucun protocole de session n'est adopté. Gestion avancée des appareils et interface de révocation de toutes les sessions ne sont pas ajoutées au MVP ; leur éventuel classement appartient à 01/14/HQ. La capacité interne de révoquer les sessions selon la politique retenue est une dépendance de L1.

**Reprise HQ reçue pendant la préparation :** le [dossier, §10](../project-governance/m0-mvp-arbitration.md), ajouté au SHA `206b1804df5cb602140729613fa85080fea32c7c`, organise d'abord une réponse propriétaire 04 sur GAP-01 à 04, puis les avis ciblés. Ce candidat est une entrée complémentaire pour cette réponse ; il ne remplace ni le contrat Backend ni la revue spécialisée. La réception HQ pour instruction n'est pas une approbation du candidat. Les transmissions aux discussions restent À TRANSMETTRE selon ce mandat.

#### Objets et critères de succès à ne pas confondre

| Notion conceptuelle | Sens proposé / effet observable / propriétaire |
| --- | --- |
| Compte et état métier | Titulaire et droits actuels ; restriction sociale distincte de session valide/invalide. Une récupération ne lève pas une sanction. 04/09/14/15 approuvent les projections. |
| Session logique | Contexte d'accès à viser lors du logout ; peut survivre à un remplacement de credential si le modèle retenu le prévoit. 04/14 fixent son identité et sa portée ; pas de nouvelle table ou clé imposée. |
| Credential / génération | Preuve présentée pour cette session ; renouvellement éventuel, ancien/nouveau credential et descendance sont des notions de protocole. Ne pas assimiler arbitrairement le `session_id` conceptuel reçu au secret transporté. |
| Contexte du navigateur | Vues et requêtes liées au compte courant (§4.1) ; effacer ce contexte n'est pas une révocation serveur. Fermer un onglet n'est pas une preuve de fin de session. |
| Opération et résultat | Envoi → résultat confirmé, refus confirmé ou résultat inconnu. Le `request_id` est une corrélation, pas un reçu de révocation ni une autorisation pour lire l'état d'autrui. |

**Recommandation de portée à examiner :** le logout de la session courante invalide aussi les credentials issus de son renouvellement, s'ils existent ; une course refresh/logout ne doit pas laisser une continuation active de la session quittée. Une nouvelle connexion indépendante n'est pas automatiquement cette continuation. 04/14 doivent distinguer les deux et ordonner les opérations au point autoritatif, avec 03 pour les contraintes de persistance/cache. La confirmation signifie que les nouvelles autorisations serveur respectent la révocation ; elle ne promet pas de rappeler une réponse déjà livrée ni d'annuler une mutation précédemment confirmée. Une mutation encore en concurrence suit l'ordre C6 documenté.

#### Table de résultats et reprise à approuver

Les statuts de succès existants restent 201 (003), 200 (004/007), 204 sans corps (005), 202 (006) ; les codes ci-dessous sont ceux du catalogue reçu. Leur mapping HTTP exact et leurs headers restent à ratifier par 04/05/14. Aucun reçu, endpoint de suivi ou champ supplémentaire n'est inventé pour résoudre un cas ouvert.

| Cas / précondition | Résultat et règle serveur candidats | Action Web et limite de la preuve |
| --- | --- | --- |
| Connexion 003 confirmée | Preuve valide et admission/état autorisés ; SessionResult et credential selon transport approuvé ; renouveler l'identité de session aux transitions de privilège retenues par 14 | Invalider l'ancien contexte, vérifier l'identité courante. Si réponse perdue : aucune nouvelle connexion automatique ; réconciliation seulement si elle permet de reconnaître le contexte attendu, sinon reprise explicite. |
| Logout 005 avec session visée valide | Résoudre la session au début de l'opération autorisée ; 204 seulement après effet de révocation garanti selon le contrat approuvé. Panne avant ou après commit : ne pas annoncer un succès non établi | Retirer les vues privées dès la demande ; après 204 exploitable pour cette opération, annoncer la déconnexion de la portée confirmée, pas de tous les appareils. |
| 204 perdu, puis répétition de 005 | Répétition ne crée aucun effet additionnel. Le catalogue autorise `AUTH_REQUIRED` si la session n'est plus authentifiable ; un éventuel 204 neutre sur session déjà terminée serait une autre politique à approuver | Ne pas transformer le 401 générique en preuve que l'ancienne session a été révoquée. Distinguer « aucune session active détectée ici » de « révocation de la session visée confirmée ». Une réponse pour un autre contexte n'est pas une confirmation. |
| Logout hors ligne, timeout ou 503 | Effet serveur inconnu tant qu'aucune preuve autorisée ne l'établit ; le timeout n'annule pas une requête déjà reçue | Contexte privé masqué, état « déconnexion à confirmer », reprise bornée. Aucun retour automatique dans une vue privée si une lecture ultérieure retrouve la session encore active. |
| Refresh 004 nominal | Preuve admissible, session/état/droits revérifiés, transition atomique ancien → nouvel état selon option retenue ; aucun droit ajouté par la rotation | Une seule opération de renouvellement par contexte client lorsque possible ; adopter le résultat seulement dans le contexte courant et selon la politique de transport. |
| Deux refresh, ou succès 004 dont la réponse se perd | Pas de création de deux continuations indépendantes non prévues ; résultat du deuxième essai et devenir du premier explicités dans une option ci-dessous | Pas de retry aveugle. API-BE-004 n'est pas marqué K dans le catalogue : ne pas lui appliquer implicitement le mécanisme K de 001/002/006/007. Une simple lecture d'identité ne permet pas de récupérer un credential perdu. |
| Refresh concurrent avec logout, expiration ou récupération | Ordre autoritatif défini ; une transition déjà terminale ne redevient pas valide par refresh. Si le refresh précède la révocation, sa continuation est incluse dans la portée visée | Une réponse 200 tardive n'est pas une autorisation durable. Revérifier et empêcher ses effets obsolètes côté transport ; voir cas cookie ci-dessous. |
| Session expirée/révoquée, preuve de refresh rejouée | `SESSION_REVOKED` / `REFRESH_REPLAY` selon contrat, sans fournir une nouvelle preuve d'accès à un détenteur non autorisé ; absence de droit vérifiable : refus | Message neutre et reconnexion si appropriée ; aucun enchaînement automatique illimité vers refresh ou récupération. Un 403 métier seul ne prouve pas une fin de session. |
| Récupération 006 demandée | 202 neutre selon C3, timing/limites anti-énumération ; aucune session révoquée ni compte récupéré déduits de ce reçu | Message neutre localisable, aucun compte existant confirmé. Reprise K selon GAP-02 ; ne pas renvoyer de nouveaux emails en boucle. |
| Récupération 007 confirmée | Preuve spécifique vérifiée et consommée atomiquement ; changement de moyen d'accès et révocations selon portée approuvée ; maintien des restrictions métier | Le reçu `completed` ne crée pas automatiquement une session. La nouvelle authentification suit 003 ou une autre transition expressément approuvée ; effacer les saisies secrètes. |
| Suspension ou suppression de compte | Retrait de capacités / révocation selon matrice propriétaire, pas une équivalence automatique entre ces événements ; suppression et purge demeurent distinctes | Préserver les voies recours/privacy approuvées après authentification adaptée ; ne pas annoncer effacement complet du fait d'une session révoquée. |

Pour 005, **recommandation d'intégration :** conserver la distinction entre effet serveur et observation locale. 04/14 choisissent comment confirmer une révocation après perte de réponse, sans exposer de donnée ou de credential par une clé seule. Tant que cette preuve n'est pas spécifiée, le Web ne peut affirmer que la session initiale est révoquée à partir d'une réponse anonyme de GAP-03. Une reconnexion ou un changement de compte entre deux tentatives interdit le rejeu automatique de `/current` sous le nouveau credential : il pourrait viser la mauvaise session.

#### Options à arbitrer pour rotation et récupération

| Option de rotation / reprise | Bénéfice et coût / condition de recevabilité |
| --- | --- |
| Ne pas exposer de refresh client si le modèle serveur approuvé n'en a pas besoin | Réduit les échanges concurrents ; n'élimine ni régénération aux transitions de privilège ni expiration/révocation. Exige que 04/14 expliquent comment le cycle fonctionne et décident du sort d'API-BE-004 ; aucune suppression de route par 21. |
| Rotation stricte, preuve consommée non rejouable | Politique de rejeu explicite ; une réponse perdue peut imposer une réauthentification. Fixer expiration et invalidation du credential nouvellement créé lors d'une reprise/abandon, et portée de révocation en cas de rejeu. Le serveur ne sait pas nécessairement si le client a reçu la réponse ; aucune détection de perte supposée. |
| Rotation avec reprise bornée d'une même opération | Peut éviter une reconnexion après perte de réponse ; exige une liaison vérifiée au contexte et à l'opération, atomicité, fenêtre, réautorisation et protection du résultat contenant un credential. Une ancienne preuve seule ne doit pas ouvrir une fenêtre de rejeu indifférenciée. Coût de protocole et de tests supérieur. |

**Recommandation :** examiner d'abord si un renouvellement client est nécessaire dans l'option web opaque déjà proposée par 14 ; si oui, comparer les deux politiques de rotation avec leurs cas de panne. Ne pas ajouter une période de tolérance implicite pour contourner un problème de concurrence. Cela reste un choix 03/04/05/14 soumis au HQ si structurant, sans présumer OAuth, JWT ou un fournisseur d'identité.

Pour 007, deux portées sont à comparer : révoquer toutes les sessions antérieures du compte, ou une portée plus limitée justifiée par le scénario de récupération. **21 recommande d'instruire la révocation de toutes les sessions antérieures lorsqu'un moyen d'accès potentiellement compromis est remplacé.** Impact : reconnexion sur les autres appareils, traitement des opérations concurrentes, soutien utilisateur ; 14/15 et HQ ratifient. Définir l'ordre exact avec une connexion commencée avant la récupération : une ancienne preuve ne doit pas recréer un accès après celle-ci. Un simple timestamp client ou « fermer les autres onglets » n'est pas ce contrôle. Aucun MFA opérateur contourné ; suspension et droits de recours suivent GAP-05.

#### Transport, bornes et données à compléter

**Cas bloquant à transmettre à 04/05/14 :** différer une réponse refresh de A, confirmer son logout, connecter B, puis libérer la réponse ; refaire avec une ancienne réponse logout qui efface le cookie. Le rejet du corps JSON décrit au §4.1 ne garantit pas le traitement correct des headers `Set-Cookie` par le navigateur. Exiger une stratégie explicite qui empêche un credential ancien de redevenir utilisable, le remplacement silencieux de B par A et la suppression tardive du credential B. La coordination des écritures de session, y compris multi-onglets, et la révocation serveur sont des mesures candidates ; elles doivent être prouvées ensemble avec les réponses déjà en transit. Un simple verrou JavaScript par onglet ou l'abandon de `fetch` ne constitue pas cette preuve. Le comportement éventuel « session perdue, reconnexion nécessaire » doit être une issue explicite, sans affichage sous une identité erronée.

Appuis techniques, consultés le 30 septembre 2026 Europe/Paris : [MDN, Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie) décrit son traitement par le navigateur et son inaccessibilité au JavaScript frontend ; [OWASP, Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html), sections expiration/renouvellement, traite l'expiration serveur et les courses de renouvellement. **Le scénario et les mesures ci-dessus sont une déduction d'intégration à vérifier**, pas une vulnérabilité observée ni une validation de protocole par ces sources.

| Paramètre / artefact restant ouvert | Réponse précise attendue / responsable / impact |
| --- | --- |
| Durées et horloge | 04/14 : inactivité, durée absolue, durée de preuve, fenêtre de reprise éventuelle, instant de référence et bornes ; proposition de test avant/à/après expiration avec horloge serveur contrôlée. L'activité automatique et la rotation ne remettent pas implicitement le compteur absolu à zéro. Bloque les oracles temporels. |
| Ordre et portée de révocation | 03/04/14, avis 09/15 : session logique/credentials, événement terminal, transaction et source de vérité ; cache/replica indisponible ou en retard, concurrence login/refresh/logout/recovery. Succès annoncé seulement selon la garantie reçue. Bloque le modèle et les routes 003–007. |
| Schémas et codes | 04/05/14 : session/proof/erreur exacts, headers, CSRF/origine et réponse répétée ; mapper `AUTH_REQUIRED`, `SESSION_REVOKED`, `REFRESH_REPLAY` avec actions accessibles 02/16. Aucun secret dans URL, logs ou message d'erreur. Bloque READY. |
| Reprise et limites | 04/05/14 : timeout, budget/délai maximum, 429/503 avec reprise adaptée, coordination des requêtes et preuve de réconciliation ; aucun retry de mutation sur la seule présence de Retry-After. Bloque les cas de perte de réponse. |
| Traces et cycle des données | 04/14/15 : transitions autorisées et trace minimale (opération, corrélation, résultat, instant serveur et référence interne minimisée si nécessaire), stockage protégé, accès et rétention ; aucune preuve brute ou cookie conservé dans logs. 15 confirme export/effacement et exceptions ; aucune durée reprise des logs analytics. |
| Reprise après restauration | 03/04/14/15 : réappliquer les fins de session/retraits pertinents avant réouverture ; aucune réactivation d'une ancienne preuve par une sauvegarde. S08 reste le scénario de restauration, sans nouvel exercice déclaré. |

**À TRANSMETTRE** : 04/05/14 répondent à cette section avec une table choisie, schémas et séquences nominales/concurrentes ; 09/15 valident seulement les effets qui concernent leurs droits/données ; 18 confirme les oracles S04a–h ci-dessous ; 03/20/HQ vérifient les gates applicables. Publication ≠ réception. GAP-L1-04 reste **OUVERT**, autorisation d'implémentation **NON REÇUE**.

## 5. États, permissions et données à rendre observables

### Parcours et reprise candidats

1. Le visiteur fournit les données minimales et la preuve définies par l'admission ; le service renvoie un reçu cohérent et non divulgateur. L'activation valide fait évoluer l'état ; activation et création de session restent des opérations distinctes sauf décision explicite.
2. Le titulaire ouvre une session. Au chargement puis après rechargement, le client vérifie l'identité/capacité actuelle via le contrat GAP-L1-03 ; une valeur mémorisée n'autorise pas une requête serveur.
3. Il lit et modifie son profil ou ses paramètres. Chargement, validation, envoi, succès confirmé, version périmée et résultat inconnu sont distingués. Conserver les champs non secrets en cas d'erreur ; laisser relire/résoudre un conflit au lieu d'écraser.
4. Expiration ou révocation retire les accès définis ; une suspension sociale suit la matrice de droits restreints. Lors d'une déconnexion incertaine, l'UI attend une réconciliation avant d'affirmer la révocation.
5. La récupération vérifie une preuve à usage unique ; elle ne prouve pas à elle seule quelles autres sessions doivent être révoquées. Le tableau GAP-L1-04 fixe cet effet avant son implémentation.

Pour ces parcours, 02/05/16 fournissent libellés et actions de reprise, ordre du focus, résumé des erreurs, annonces d'état et compréhension dans les langues retenues. Aucun message ne contient de secret ni ne transforme une panne en preuve d'inexistence du compte.

| Acteur | Invariant candidat à confirmer par les propriétaires |
| --- | --- |
| Anonyme / preuve préauthentifiée | Aucun accès privé par la seule connaissance d'un ID ou d'une clé K ; lecture publique conditionnelle à la décision de visibilité |
| Titulaire actif | Modification de son profil/paramètres seulement ; schéma fermé et version contrôlée ; droit revérifié au point autoritatif |
| Tiers, exclu ou paire bloquée | Champs et opérations limités par la matrice ; ID substitué, compteurs et erreurs ne révèlent pas une ressource interdite |
| Compte limité/suspendu/en suppression | Capacités sociales distinctes des voies autorisées de recours et de droits sur les données ; pas de refus global inventé |
| Opérateur / service | Aucun pouvoir implicite du fait du rôle ou du compte technique ; actes et audit selon contrats 10/14/15 hors API de profil personnel |

| Catégorie | Contrat L1 reçu / complément attendu |
| --- | --- |
| Identité, admissibilité et preuve | Données privées séparées du profil ; 01/04/14/15 définissent collecte minimale, vérification, accès, suppression et conservation ; aucun champ d'origine déduit d'une langue |
| Session, challenge et K | Usage d'authentification/reprise ; portée, empreinte protégée, expiration, révocation et concurrence à fixer ; aucun credential ou preuve brute dans URL, logs ou export |
| Profil, paramètres et version | Projection publique/privée distincte ; modification par titulaire, enums et limites versionnés ; avatar soumis au cycle L2 ; droits de sortie préparés dès L1 |
| Journal et corrélation | Métadonnées minimales et finalité explicite ; distinguer audit de sécurité et diagnostic, accès interne limité, rétention approuvée ; panne de diagnostic ne bloque pas automatiquement le service |
| Sauvegardes / restauration | Modèle et procédure de 03/04/14/15 doivent réappliquer les révocations/suppressions pertinentes ; durée, exceptions et preuve de restauration restent ouvertes |

Stockage, versions techniques, délais et politique de rétention ne sont pas décidés par cette revue. L'événement candidat `access.changed.v1` ne remplace pas le contrôle actuel des droits et n'impose pas un nouveau service distribué.

## 6. Scénarios d'acceptation à rattacher aux tests existants

Ces sous-cas locaux sont **PLANNED** ; les tests applicatifs de 18 cités restent **BLOCKED**. Aucun code de test ni résultat applicatif n'est produit. Les fixtures futures utilisent des identités synthétiques `example.invalid`, des preuves fictives et une horloge contrôlée.

| Sous-cas local | Étant donné / action / attendu candidat | Références existantes ; prérequis |
| --- | --- | --- |
| S01 — activation et reçu perdu | Réponse d'activation perdue après mutation ; rejouer même contexte vérifié puis autre contexte/entrée. Une activation unique ; reçu seulement selon la règle approuvée ; aucune preuve consommée ne redonne arbitrairement un accès. | TEST-0401, TEST-1801/1802/1833 ; GAP-01/02/07 |
| S02 — rotation concurrente | Deux refresh concurrents et une réponse perdue ; appliquer la politique de rotation/rejeu reçue. Ensemble de sessions autorisées déterministe, aucun retry aveugle ni accès révoqué. | TEST-0402, TEST-1803/1833 ; GAP-01/04 |
| S03 — rechargement et identité | Session active puis expirée/révoquée, rechargement sans état client ; retrouver identité/capacités par le mécanisme choisi, ou état anonyme/indisponible sûr ; aucun cache ne rétablit un droit. | TEST-0402, TEST-1803/1832/1833 ; GAP-03/05 |
| S04 — déconnexion et récupération | Réponse de logout perdue puis retry ; récupération avec preuve valide/invalide ; appliquer la portée de révocation décidée, affichage cohérent et réponses non divulgatrices. | TEST-0402, TEST-1803/1804/1833 ; GAP-02/04 |
| S05 — suspension concurrente | Droit retiré avant requête ou avant commit ; lecture/mutation et tentative d'accès aux voies recours/privacy. Refus et autorisations suivent la matrice, sans blocage global déduit. | TEST-0402/0404, TEST-1832/1834 ; GAP-05 ; preuve L1 limitée aux interfaces disponibles, intégration L4/L5 distincte |
| S06 — profil et paramètres | Tiers, champ inconnu, chaîne aux bornes Unicode, Vn absente/périmée, locale/politique non admise et avatar indisponible à L1. Aucun effet interdit ; erreurs et version suivent le contrat, saisie non secrète récupérable. | TEST-0403/0404, TEST-1832/1837/1848 ; GAP-05/06/07 |
| S07 — limites et interface | Limite N-1/N/N+1, 429/503 et délai réseau ; vérifier reprise bornée, message accessible, focus et champs sensibles effacés. Même résultat métier sur les clients/langues retenus. | TEST-1833/1837/1844/1845 ; GAP-01/06/07 ; critères UX reçus |
| S08 — audit et restauration | Canari secret fictif, panne du journal, restauration d'un état avec session révoquée. Aucun canari journalisé, mode panne approuvé et aucune session interdite réactivée. | TEST-0402, TEST-1840/1847 ; GAP-04/08 ; déclinaison QA L1 à confirmer, exercice runtime non réalisé |

Déclinaison **PLANNED** de S03 pour le candidat §4.1 ; aucun nouvel identifiant global réservé et aucune exécution applicative :

| Sous-cas local | Précondition / action / oracle candidat | Rattachement proposé ; dépendance |
| --- | --- | --- |
| S03a — restauration valide | Session A valide, mémoire cliente vide ; recharger. Référence compte/profil cohérente, capacités courantes, aucune donnée privée avant vérification ; relire ensuite profil/paramètres selon leurs droits. | TEST-0402/0403, TEST-1803 ; GAP-03/05/06 |
| S03b — absence ou fin de session | Sans credential, puis credential expiré/révoqué ; lire le contexte. Variante anonyme ou 401 selon choix approuvé, aucun contexte privé ; un GET protégé reste refusé selon C3. | TEST-1401, TEST-1803, TEST-WEB-0003 ; GAP-01/03/04 |
| S03c — panne et reprise | Source de droits en panne, puis timeout/429 et reprise réussie. `UNAVAILABLE` ou attente bornée, aucun faux anonyme ni logout confirmé ; délai/budget respectés, retour explicite à l'état vérifié. | TEST-1833, TEST-WEB-0003 ; GAP-03/07 |
| S03d — réponses hors ordre | Retarder contexte/profil de A ; quitter A, entrer B ; livrer ensuite réponses A succès, anonyme et erreur. Aucun affichage de A ni déconnexion de B. Inverser aussi deux lectures de contexte A entourant un retrait de droit connu ; l'ancienne ne restaure rien. | TEST-1832/1833, TEST-WEB-0004 ; GAP-03/04/05 |
| S03e — restriction | Compte valide puis restriction confirmée ; relire contexte et tenter une action retirée. Refus serveur selon matrice, projection cohérente, seules voies recours/privacy approuvées accessibles. | TEST-1832/1834 ; GAP-03/05, interfaces L4/L5 pour preuve intégrée |
| S03f — historique et onglets | Logout confirmé puis retour navigateur, restauration d'onglet et connexion B. Aucune donnée privée A réaffichée ; contexte non persisté par cache applicatif/service worker ; vérifier aussi l'option HTML si retenue. | TEST-WEB-0004 ; GAP-03/04, environnement navigateur réel requis |
| S03g — lecture et expiration | Horloge contrôlée, lectures automatiques répétées sans action utilisateur. Pas de création/rotation/activation ni prolongation interdite ; expiration absolue et calcul d'inactivité respectent la politique reçue. | TEST-1401, TEST-1803 ; GAP-01/03/04 |
| S03h — schéma, minimisation et isolement | Fournir ID cible/champ inconnu ; injecter variantes incohérentes/enum inconnu dans fixtures consommateur ; observer corps/logs avec canaris fictifs. Refus d'entrée, aucun accès accordé par une valeur inconnue, pas de credential ou champ exclu ; `null` et absence traités selon schéma. | TEST-0403, TEST-1415, TEST-1832 ; GAP-03/05/06/07 |

Déclinaison **PLANNED** de S02/S04 pour le candidat §4.2 ; aucun test applicatif exécuté :

| Sous-cas local | Précondition / action / oracle candidat | Rattachement proposé ; dépendance |
| --- | --- | --- |
| S04a — logout confirmé et rejoué | Session A valide ; logout puis requête protégée/refresh avec anciennes preuves et répétition de logout. Refus d'accès/renouvellement ; aucun effet additionnel et résultat répétition conforme au mapping approuvé. | TEST-0402, TEST-1401, TEST-1803 ; GAP-01/04 |
| S04b — réponse logout perdue | Couper avant réception serveur, puis après commit/avant réponse ; répéter sous le même contexte si encore possible. Distinguer preuve de révocation, simple absence de session et résultat inconnu ; pas de faux succès/échec. | TEST-1833, TEST-WEB-0003/0004 ; GAP-03/04/07 |
| S04c — cible devenue autre | Logout A incertain, connexion B ou changement de credential ; déclencher une reprise. Aucun DELETE automatique de la session B pour terminer l'intention A ; aucun affichage privé A. | TEST-1832/1833, TEST-WEB-0004 ; GAP-03/04 |
| S04d — double refresh / réponse perdue | Deux requêtes avec même preuve et perte de la première réponse ; varier ordre de commit/livraison. Issue conforme à l'option retenue, aucune continuation supplémentaire autorisée par erreur, preuve usagée inutilisable hors règle approuvée. | TEST-0402, TEST-1401, TEST-1803/1833 ; GAP-01/04 |
| S04e — refresh contre événement terminal | Ordonner refresh avant/après logout, expiration et récupération ; livrer la réponse 200 en dernier. La session et les continuations visées restent inutilisables après confirmation de leur fin ; compte/restrictions inchangés par un refresh. | TEST-1401/1419, TEST-1803/1834 ; GAP-04/05 |
| S04f — headers tardifs et onglets | Navigateur réel avec transport retenu : réponse refresh A puis logout A/connect B hors ordre ; variante ancien logout effaçant le cookie. Contrôler cookies/credential réellement envoyés ensuite, identité observée et droits serveur ; pas seulement l'état UI. Aucun retour à A ou effacement silencieux de B ; issue de récupération explicite si le protocole ne préserve pas B. | TEST-WEB-0004, TEST-1832/1833 ; GAP-01/03/04, protocole transport requis |
| S04g — récupération et accès concurrents | Deux consommations du challenge, perte de réponse, connexion concurrente par ancien moyen, sessions existantes sur deux appareils. Un effet de récupération, reçu rejoué seulement selon GAP-02, révocations selon portée choisie, aucun MFA/sanction contourné ; pas de session automatique non prévue. | TEST-0402, TEST-1402, TEST-1803/1804 ; GAP-02/04/05 |
| S04h — temps, panne et traces | Horloge contrôlée avant/à/après bornes ; renouvellements automatiques, autorité indisponible, quota et canaris secrets fictifs. Expiration conforme sans remise à zéro implicite, aucun droit sur panne, reprise bornée et traces sans secrets. Restauration réutilise S08. | TEST-1401/1415, TEST-1833 ; GAP-04/07/08 |

Sortie documentaire attendue : chaque GAP applicable a une réponse versionnée du producteur, un avis du consommateur et une référence d'arbitrage si nécessaire ; 18 peut déduire un résultat attendu univoque. Sortie fonctionnelle ultérieure : exécution réelle avec version du contrat, SHA, environnement, commande, résultats et traces expurgées. Ni une case cochée ni la CI du dépôt ne remplace cette preuve.

## 7. Risques, suite et compte rendu HQ

| Risque local | Impact / mesure proposée / propriétaire |
| --- | --- |
| Deux consommateurs inventent leur identité courante ou reprise | Accès incohérents et doubles effets ; fermer GAP-02/03/04 dans une source commune ; 04/05/14 |
| Réponse de session tardive traitée seulement dans l'UI | Ancien cookie réinstallé ou nouveau credential effacé ; faire examiner protocole de transport et révocation ensemble, S04c–f ; 04/05/14. Risque de conception, aucune exploitation observée. |
| Profil, admission, langue et consentement confondus | Exposition ou collecte non voulue ; séparer schémas/finalités et faire revoir GAP-05/06 ; 01/15/16 |
| Préparation L1 prise pour un pilote prêt | Recours, opérations ou droits sur les données absents ; conserver gates L4/L5/L6 et GO d'ouverture distinct ; HQ/20/18 |
| Blocage global imposé à tout travail | Retard inutile ; avancer schémas et exemples indépendants, ne bloquer que le code dépendant et son verdict ; producteurs/20 |
| Preuve Git assimilée à une approbation métier | Autorité et sécurité non vérifiées ; conserver statuts et signatures ; FIND-21-02 ouvert, FIND-21-05 séparé ; HQ/14/20 |

1. **Décisions/verdicts :** rapprochement local des sources et conservation des IDs de 20 ; L1 non prêt pour code. Méthode d'identité, permissions, données, architecture et portée restent à valider par leurs propriétaires et HQ.
2. **Livrables GitHub :** cette v0.4, candidats GAP-L1-03/04 aux §4.1/4.2 et sous-cas S03a–h/S04a–h, liés depuis le dossier d'arbitrage v0.4 et l'index, publiables dans la [PR #27 existante](https://github.com/yyogas/social-network/pull/27). Aucun besoin de branche supplémentaire. Le SHA de publication et ses preuves sont consignés dans le corps de cette PR.
3. **Tests exécutés :** contrôles documentaires locaux et CI à consigner après exécution dans la PR avec commandes/SHA/job ; cette pièce n'annonce aucun PASS futur. Aucun test applicatif exécuté dans cette revue.
4. **Questions ouvertes :** réponses exactes GAP-L1-01 à 08 ; DIR-012 confirme le positionnement ; les choix de cohorte, pays ouverts, langues, âge et fonctionnalités A/B/C restent à arbitrer.
5. **Dépendances :** tableau §4, demandes À TRANSMETTRE ; avis 04/05/14 prioritaires pour identité/reprise, puis 09/15 pour droits et données, 18 pour oracles, 03/20/HQ pour gate de réalisation.
6. **Risques :** tableau ci-dessus ; absence de preuve runtime et de revue spécialisée approbative, sans nouveau défaut logiciel démontré.
7. **Prochaines étapes / HQ :** arbitrer A/B/C et obtenir les avis nécessaires ; faire répondre aux seuls GAP applicables ; joindre schémas et exemples versionnés, puis revue des producteurs/consommateurs ; HQ autorise L1 après ses gates. Préparer ensuite implémentation et tests sur ce contrat. Aucune fusion, suppression de branche ou autorisation de lancement n'est demandée implicitement par ce document.
