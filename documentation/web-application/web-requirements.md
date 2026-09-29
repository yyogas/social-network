# Web App — exigences et contrats consommateurs M0

## Identification et statut

| Champ | Valeur |
| --- | --- |
| Objectif | Décrire le parcours web du pilote candidat et fournir une matrice écran → contrat → droits → états → tests |
| Propriétaire | 05 — Web App ; mandat M0-TEAM-05 ; aucun reviewer humain désigné |
| Révision | v0.2, 29 septembre 2026 ; consolidation des deux cadrages Web v0.1 |
| Base GitHub | PR #2, branche `documentation/m0-team-coordination`, commit `dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957` |
| Statut | PROPOSÉ — revue spécialisée et arbitrage HQ attendus ; aucune autorisation d'implémentation ajoutée |
| Destinataires | 00/01/02/03/04/08/09/10/13/14/15/16/17/18/20/21 ; 06 pour cohérence des clients |
| Classement | MVP candidat P0 pour les parcours indispensables ; phases proposées détaillées ci-dessous |
| Périmètre | Site public et client social responsive ; console opérateur détenue par 10, infrastructure par 14, politiques par leurs propriétaires |
| Dépendances bloquantes | WEB-DEP-01 à 07, réutilisés du cadrage précédent ; détail et travaux affectés en fin de document |

Références consultées : [mandat](../teams/work-orders.md), [modèle](../teams/deliverable-template.md), [plan documentaire](../documentation-plan.md), [vision](../product/product-vision.md), [catalogue](../product/feature-catalog.md), [parcours J01–J07](../product/user-journeys.md), [gouvernance](../governance.md), [conventions](../repository-conventions.md), [registre](../project-governance/decision-register.md), [stratégie QA](../quality/test-strategy.md). Les six premières références ont été relues via GitHub au SHA ci-dessus ; leurs blobs correspondent aux copies locales.

Travaux réutilisés : `SOCIAL-NETWORK-WEB-APP-Cadrage-v0.1.md` et `SOCIAL-NETWORK-05-WEB-M0-v0.1.md`, lus dans l'espace de travail. Leur contenu utile est consolidé ici ; ces noms désignent des sources historiques hors dépôt, pas des chemins canoniques ni des preuves d'approbation. Les propositions Backend/Privacy citées dans ces anciens documents ne sont pas réputées revalidées par cette passe.

| Nature | Éléments et preuve/limite |
| --- | --- |
| CONFIRMÉ | Mandat utilisateur 05, priorités accessibilité/performance/sécurité/réutilisation et demande Next.js, React, TypeScript ; instruction actuelle de produire et publier la documentation ; dépôt accessible et PR #2 vérifiée |
| PROPOSÉ | Toutes les routes, interfaces consommateurs, règles UX, phases et budgets de ce document ; le catalogue HQ demeure une proposition |
| À VÉRIFIER | Ratification de la stack dans le registre global, pilote web en premier, communautés, visibilité, langues/pays/âge, budgets et capacité de modération |
| NON REÇU dans les pièces examinées | Design System approuvé, API versionnées approuvées, matrice d'accès, stratégie de session/cache, catalogue analytics et avis spécialisés définitifs |

La stack est une demande explicite du mandat Web ; ce document ne la transforme pas en ADR global. Aucun composant, endpoint, test applicatif ou déploiement n'est déclaré existant.

## Besoin, fonctionnalités et parcours

Le pilote doit permettre de rejoindre le service, comprendre l'audience, publier et lire, contrôler les interactions puis demander de l'aide ou quitter le service. La contribution Web indispensable est une interface cohérente sur petit écran et réseau limité, qui reflète les décisions du serveur et permet de récupérer d'un échec sans annoncer de faux succès.

### Matrice des écrans candidats MVP

Toutes les lignes sont **PROPOSÉES**. Les routes sont conceptuelles, sans engagement d'URL publique définitive. `C-*` désigne un besoin consommateur local v0.1 décrit plus bas, pas un identifiant API officiel. Les composants sont des besoins adressés à 02, sans choix de bibliothèque. Les critères `AC-J*` existants sont réutilisés ; les scénarios Web supplémentaires figurent dans la matrice de vérification.

| FEAT / priorité / parcours | Écran, acteur, précondition et parcours nominal | Composants et données nécessaires | Contrat / droits | États, erreurs et reprise | Acceptation / analytics candidat |
| --- | --- | --- | --- | --- | --- |
| FEAT-018/021, MVP P0 | `/`, `/help`, `/rules`, `/privacy` ; visiteur ; contenus éditoriaux validés ; comprendre le service puis ouvrir l'inscription | PublicLayout, Navigation, EditorialPage, LanguageSelector ; texte versionné et langue | C-PUBLIC ; données éditoriales publiques uniquement | Loading, contenu disponible, page absente, indisponible ; accès à une aide statique si prévu par 14 | W01/W02 ; `public_entry_view` sans URL brute |
| FEAT-001/002, MVP P0, J01 | `/signup`, `/activate`, `/login`, `/recover` ; visiteur admissible selon politique ; remplir, valider, activer, accéder à une destination interne autorisée | AuthForm, Field, ErrorSummary ; champs d'identité minimaux, preuve d'activation, état de session | C-IDENTITY ; aucune donnée privée d'un tiers ; admissibilité serveur | Initial, validation, envoi, activation attendue, lien expiré/utilisé, limitation, réseau incertain ; réponse neutre pour récupération | AC-J01-01/02/04, W03 ; `auth_step_result` sans secret ni existence de compte |
| FEAT-002/018, MVP P0 | `/app` et déconnexion ; membre ; session valide ; ouvrir une section puis fermer la session | AppShell, Navigation, SessionNotice ; état utilisateur et capacités | C-IDENTITY ; contrôle de chaque requête protégée | Session en vérification, active, expirée, restreinte, déconnexion incertaine ; ne pas afficher « session révoquée » avant réponse | AC-J01-03, W03/W04 ; erreur technique agrégée |
| FEAT-003/005, MVP P0, J01/J03 | `/profiles/:id`, `/settings/profile` ; propriétaire ou lecteur autorisé ; lire/éditer/suivre puis voir le résultat confirmé | ProfileHeader, ProfileForm, FollowAction ; nom, bio, avatar autorisé, relation, version | C-PROFILE/C-SOCIAL ; écriture propriétaire, relation autorisée selon blocage | Vide, chargement, profil indisponible, sauvegarde, conflit de version ; relire avant réessai | AC-J03-03, W05 ; `profile_save_result`, `follow_result` sans identifiant de cible |
| FEAT-004, MVP P0, J02/J06 | `/settings/privacy` et audience du composer ; membre ; audiences autorisées reçues ; choisir et confirmer | AudienceControl, Explanation, Confirmation ; audience effective et capacités | C-PRIVACY/C-POST ; serveur autorise l'audience et chaque lecture | Options indisponibles, envoi, conflit, refus ; ne pas inventer une audience par défaut | AC-J02-01/04/05, W06 ; aucune valeur d'audience sensible dans analytics |
| FEAT-006/007, MVP P0, J02 | `/compose`, `/posts/:id/edit` ; auteur ; session, limites et droits connus ; saisir texte, décrire image, uploader, vérifier audience, publier ; modifier/retirer ensuite | Composer, MediaPicker, UploadProgress, AltTextField, StatusNotice ; texte, média opaque, texte alternatif, version | C-MEDIA/C-POST ; média rattaché à l'auteur ; mutation propriétaire autorisée | Brouillon mémoire, upload, traitement, prêt, soumission, confirmé, refus, résultat inconnu ; réconcilier avant nouvel envoi | AC-J02-01 à 05, W07/W08 ; `publish_result` après confirmation serveur |
| FEAT-008/022, MVP P0/P1, J03 | `/feed`, `/posts/:id` ; lecteur autorisé ; suivre puis lire, charger la suite, rafraîchir volontairement | FeedList, PostCard, LoadMore, EndOfFeed ; publications filtrées, curseur opaque, versions | C-FEED/C-POST ; filtrage serveur sur chaque page et accès direct | Premier chargement, vide réel, chargement suite, erreur partielle, fin, contenu retiré ; conserver position et éléments encore autorisés | AC-J03-01/04, W09 ; `feed_page_result`, pas de mesure imposée du temps passé |
| FEAT-009/010, MVP P1, J03 | Détail et cartes ; membre autorisé ; réagir/commenter, éditer/retirer son commentaire selon contrat | ReactionAction, CommentList/Form ; état de réaction, commentaire, version et capacités | C-SOCIAL ; droits recontrôlés sur publication et commentaire | Envoi, conflit, parent retiré, droits perdus, limite ; réaction incertaine relue avant réessai | AC-J03-02/03, W10 ; `interaction_result` sans texte |
| FEAT-011/022, MVP P1, J03 | `/notifications`, `/settings/notifications` ; titulaire ; lire une notification puis régler une catégorie | NotificationList, PreferencesForm ; types autorisés, statut de lecture, destination opaque | C-NOTIFY ; données du titulaire et cible encore accessible | Vide, chargement, cible indisponible, préférence non sauvegardée ; pas d'aperçu privé sur refus | AC-J03-05, W11 ; `notification_action_result` sans contenu |
| FEAT-012/013, MVP P0, J04 | Menu compte/post, `/safety/reports/:id` ; membre ; bloquer et/ou signaler puis lire l'accusé | BlockConfirmation, ReportForm, Receipt ; cible opaque, catégorie, description minimale et référence | C-SAFETY ; signalant seulement pour son accusé ; identité protégée | Envoi, reçu, échec, résultat inconnu, cible retirée, doublon ; aucune promesse de traitement avant accusé | AC-J04-01 à 04, W12 ; analytics métier du signalement absent par défaut |
| FEAT-014/015, MVP P0, J05 | `/safety/decisions/:id`, `/safety/appeals/:id` ; personne concernée, éventuellement restreinte ; comprendre puis contester si recevable | DecisionNotice, AppealForm, CaseStatus ; motif communicable, décision, capacité et état du recours | C-APPEAL ; périmètre personnel ; aucun accès aux preuves privées du déclarant | Recours recevable, envoi, reçu, examen, résultat, non recevable ; transitions métier à confirmer par 09 | AC-J05-04, W13 ; diagnostics minimaux, aucun motif privé dans analytics |
| FEAT-016, MVP P0, J06 | `/settings/data` ; titulaire vérifié ; demander export ou suppression puis consulter l'état | DataRequestForm, ConsequenceSummary, RequestStatus ; référence, statut et expiration autorisés | C-DATA ; vérification renforcée à définir ; export du titulaire uniquement | Vérification, demandé, en cours, prêt/expiré/échec ; suppression distincte de son simple accusé ; annulation seulement si contrat | AC-J06-01 à 04, W14 ; aucun lien d'export en télémétrie |
| FEAT-020, MVP P1 conditionnel, J07 | `/communities/:id` ; visiteur/membre/responsable local ; lire présentation autorisée, rejoindre, publier, quitter | CommunityHeader, Rules, MembershipAction ; adhésion, règles, rôle limité | C-COMMUNITY ; aucune permission globale induite par rôle local | En attente, refus, membre, exclusion, fermeture, absence de responsable ; comportement à valider | AC-J07-01 à 04, W15 ; `membership_result` sans cible |
| FEAT-019, MVP P1 | Transversal ; instrumentation seulement après avis 13/15 | EventsAdapter ; résultat, code technique assaini, famille d'écran | C-MEASURE ; conditions de collecte approuvées | Collecte inactive/permise, panne ; aucune panne de mesure ne bloque une action métier | W16 ; schéma et finalité avant activation |
| FEAT-017, MVP P0, interface avec 10 | Liens d'aide et suivi côté membre ; console opérateur hors ownership 05 | Aucun outil d'administration créé ici ; réutilisation DS à convenir | C-SAFETY/C-APPEAL côté membre ; contrat opérateur détenu par 10 | Traitement interne indisponible : pas de faux état résolu | AC-J05-01 à 05 sous responsabilité 10/18 ; lancement dépend de cette capacité |

### Phases ultérieures et manques du catalogue

Chaque ligne est PROPOSÉE ; la phase ne constitue pas une validation de roadmap. Les détails runtime seront spécifiés avant le lot concerné.

| Fonctionnalité | Phase / priorité | Parcours et dépendances nécessaires | Limite / critère à instruire |
| --- | --- | --- | --- |
| FEAT-023 Recherche | Phase 2 / P1 | `/search` ; 01/04/15 ; champ, résultats, vide, indisponible | Résultats/extraits soumis aux droits ; requête non capturée par analytics ; découverte MVP par liens autorisés à confirmer avec 01/19 |
| FEAT-024 Messages | Phase 2 / P2 | `/messages` ; 04/09/14/15 ; liste, conversation, envoi/échec | Blocage et abus ; aucun transport ni chiffrement choisi par Web |
| FEAT-025 Mobile natif | Phase 2 / P2 | Propriété 06 ; liens profonds et contrats communs | Ne pas assimiler web responsive à application native/PWA/offline |
| FEAT-026 Vidéo | Phase 2 / P2 | `/videos` ; 08/09/14 ; upload, traitement, lecture, retrait | Sous-titres/accessibilité et budgets ; pas d'autoplay imposé ; retrait des dérivés à tester |
| FEAT-027 Creator Studio web initial | Phase 2 / P2 | `/studio` ; 12/13/15 ; publications et indicateurs autorisés | Statistiques définies, chargement/vide/erreur ; mesures d'un autre créateur refusées |
| FEAT-028 Pages entreprises | Phase 2 / P2 | `/business/:id` ; 01/04/14 ; page et gestionnaires | Révocation d'un gestionnaire répercutée ; ancienne proposition Web Phase 3 ne remplace pas ce classement HQ |
| FEAT-029 Recommandations | Phase 3 / P2 | 07/13/15 ; suggestions explicables et désactivation | Fil chronologique conservé ; Hub ne signifie pas automatiquement recommandation |
| FEAT-030/031 Publicité et monétisation | Phase 3 / P2 | 11/12/14/15 ; campagnes, statuts, paiements selon futurs contrats | Aucun outil financier ni tracking publicitaire inclus au pilote |
| FEAT-032 Ouverture internationale | International / P1 | 16/09/15 ; écritures, traductions, aide et modération par marché | Distinguer cette extension de FEAT-021 langues du pilote |
| FEAT-033 Live | Long terme / P3 | 08/09/14 ; diffusion, arrêt, panne, signalement | Capacité et procédure d'arrêt démontrées avant ouverture |
| FEAT-034 Intégrations | Long terme / P3 | 03/04/14/15 ; consentement et révocation | Scopes et quotas versionnés avant UI de connexion |
| Hub, ID FEAT à attribuer par 01/17 | Phase 2 / P2 proposée pour un écran dédié | 01/02/07 ; finalité, sources et droits à définir | Simple raccourci de navigation reste possible via FEAT-018 ; aucune agrégation recommandée implicite |
| Événements, ID FEAT à attribuer par 01/17 | Phase 2 / P2 proposée | 01/04/09/15/16 ; dates/fuseau, inscription et visibilité à définir | Besoin du mandat absent du catalogue ; pas de FEAT inventé ni route MVP promise |

### Transitions, reprise et erreurs communes

Lecture : initial → chargement → succès/vide/refus/erreur. Une erreur de chargement ne doit jamais être présentée comme un fil vide. Une requête devenue obsolète après changement de compte, navigation ou filtre est ignorée ; les données du compte précédent sont retirées avant d'afficher le suivant.

Mutation : saisie → validation → envoi → confirmé, refus explicite ou résultat inconnu. Annuler une requête côté navigateur ne prouve pas l'annulation serveur. En cas de résultat inconnu, conserver la clé de l'opération en mémoire, interroger l'état si le contrat le permet, sinon proposer une vérification ; ne pas créer une nouvelle opération automatiquement. Les limites numériques, durée de validité des clés et endpoints de réconciliation appartiennent à 04. Les brouillons ne persistent pas sur disque par défaut proposé ; fermeture, déconnexion et changement de compte demandent un comportement explicite validé par 02/15.

| Raison/codes candidats, à confirmer par 04 | Présentation et récupération proposées |
| --- | --- |
| Réseau interrompu / timeout | Message accessible, conservation des champs non secrets en mémoire si encore autorisé, réessai explicite ; lectures annulables, aucune file de mutations hors ligne |
| 401 | Session à rétablir, masquer les données sensibles, retour vers une destination interne permise ; aucun renvoi aveugle vers URL externe |
| 403/404 | Message uniforme lorsque la politique protège l'existence ; purger l'objet devenu inaccessible ; ne pas inférer une suspension de la cible |
| 409 | Recharger version/état puis laisser résoudre le conflit ; ne pas écraser silencieusement une édition concurrente |
| 413/415/422 | Limite/type/champ non conforme ; associer erreur au champ ; validation serveur reste autorité, valeurs de limites reçues du contrat |
| 429 | Attendre le délai serveur si fourni, action désactivée de façon accessible ; aucun retry agressif |
| 5xx / dépendance indisponible | Échec temporaire, état inconnu pour mutation si réponse perdue ; aide/correlation ID assaini, jamais réponse brute ou trace serveur |

Logs techniques proposés : famille d'opération, résultat, durée et identifiant de corrélation approuvé. Aucun mot de passe, token, cookie, texte saisi, corps de réponse, URL sensible ou lien signé. Les retry automatiques de lecture, si retenus, sont bornés par 04/14 ; aucune nouvelle mutation automatique sans contrat d'idempotence.

## Permissions, données et contrats

### Matrice de droits candidate

Le serveur autorise chaque lecture et mutation, y compris HTML rendu serveur, payload d'hydratation, média et téléchargement. Les capacités de l'UI indiquent une action possible sans constituer une autorisation durable. Matrice **PROPOSÉE**, validation 01/09/14/15 ; absence de règle = intégration concernée bloquée, pas permission accordée.

| Acteur | Action/portée | Refus attendu et effet UI |
| --- | --- | --- |
| Anonyme | Éditorial public ; profil/post seulement si explicitement lisible hors session | Aucune donnée privée préchargée ; indexable ne se déduit pas de lisible |
| Membre actif | Lire selon audience ; publier et interagir si capacités autorisées | Recontrôle après changement d'audience, blocage, retrait ou suspension |
| Propriétaire | Modifier ses objets selon état et version | Propriété ne contourne ni retrait modération ni règle d'audience |
| Autre membre | Lire/interagir selon audience et relations | Aucune modification du profil/post/commentaire d'autrui |
| Compte bloqué / relation de blocage | Portée exacte décidée par 09/15 | Ne pas promettre invisibilité absolue des données publiques ; appliquer le même refus sur tous les accès visés |
| Compte suspendu/restreint | Actions sociales selon politique ; accès au recours/sortie à spécifier séparément | Éviter une garde globale qui supprimerait tout accès au recours ; entrée sécurisée à convenir si connexion indisponible |
| Responsable communautaire | Actions sur sa communauté si retenue | Aucun rôle global ni accès aux preuves privées d'un dossier global |
| Opérateur interne | Interface et habilitations distinctes, propriété 10 | Aucun bouton caché ni rôle client ne fournit des pouvoirs administratifs |

Après blocage/retrait confirmé, Web retire les objets concernés des vues et caches mémoire connus. Au retour d'onglet et avant mutation, une revalidation est proposée. Un changement distant ne peut être promis « immédiat » dans un navigateur déconnecté : 03/04 doivent définir notifications d'invalidation ou politique de relecture, délai et traitement des caches. Les copies déjà vues/téléchargées ne sont pas révocables par l'interface. Ce manque bloque toute promesse de révocation instantanée globale.

### Données et cycle de vie

Stockages et durées définitifs **NON REÇUS**. Le backend demeure source d'état ; aucun schéma de table ni durée légale n'est défini ici. Les responsabilités ci-dessous couvrent modification, export, retrait, purge et restauration à préciser dans les contrats 04/15.

| Catégorie / origine | Finalité et visibilité | Copie Web proposée / accès internes | Cycle et responsabilité |
| --- | --- | --- | --- |
| Identité/session, saisie et 04 | Accès personnel, secrets exclus des vues/mesures | Pas de secret dans localStorage ; mécanisme de session à valider 14 ; support selon pouvoirs 10 | Vider champs secrets après usage ; révocation serveur ; rétention et récupération 04/15 |
| Profil et relations, 04 | Affichage des seuls champs autorisés | Mémoire liée au compte/session ; aucun cache partagé de contenu privé | Édition/version, export/suppression selon 04/15 ; compteurs limités selon policy |
| Texte, commentaires, audience, 04 | Publication/lecture pour audience autorisée | Brouillon mémoire, rendu texte sûr sans HTML arbitraire ; accès opérateur limité 09/10 | Retrait/invalidation multi-vues ; export et suppression avec exceptions documentées 15 |
| Image et alt, utilisateur/08 | Illustration accessible selon mêmes droits | Aperçu local temporaire libéré après usage ; média traité seulement ; pas de lien signé en logs | Validation/traitement/purge des originaux et dérivés 08 ; métadonnées et rétention 15 |
| Signalement/recours, membre/09 | Traitement et suivi individuel | Pas de stockage persistant client ni analytics de contenu ; preuves réservées aux habilités | Statuts et rétention 09/15, accès internes 10 ; aucune preuve dévoilée à la cible |
| Export/suppression, 04/15 | Exercice d'une demande personnelle | Référence et état minimal ; téléchargement vérifié, non préchargé | Expiration, exceptions, révocation et sauvegardes définies par 15/04/14 ; ne pas annoncer purge totale au simple accusé |
| Mesures, UI/13 | Qualité et utilité documentées | Collecte désactivée avant approbation ; accès analytique limité ; aucun identifiant cible/texte/requête | Conditions, conservation, agrégation et effacement validés par 13/15 |

Le plan de restauration doit empêcher la réapparition de contenus retirés selon la politique approuvée (AC-J06-04, propriétaires 04/14/15). Web vérifie le résultat visible ; il n'atteste pas seul de l'effacement des sauvegardes.

### Interfaces consommatrices v0.1 — propositions à 04

Pas d'endpoints ni de schéma OpenAPI déclarés officiels. Champs ci-dessous conceptuels ; type, nullabilité, enums, contraintes et taille doivent être normalisés par le producteur avant intégration. Consommateur : 05 Web ; autres clients 06/10 à consulter.

| Référence locale | Producteur métier/technique | Entrée → sortie minimale demandée | Contrôle / concurrence / défaillance spécifique |
| --- | --- | --- | --- |
| C-PUBLIC | 01/15, diffusion 03/14 | langue et page → contenu versionné, statut | Public éditorial uniquement ; mode de diffusion non choisi |
| C-IDENTITY | 04/14 | données minimales ou preuve, destination interne → session/état/capacités | Anti-énumération, CSRF et révocation ; état compte distinct des droits de recours |
| C-PROFILE | 04/01 | ID opaque, champs modifiés, version → profil filtré/version | Conflit si version périmée ; tiers ne reçoit pas champs privés |
| C-PRIVACY | 04/15 | audience autorisée, version → audience effective/capacités | Validation serveur ; impact cache et liens à décrire |
| C-MEDIA | 08/04 | type/taille déclarés, fichier via méthode autorisée, alt → ID opaque, progression/état/erreur | Valider contenu réel ; upload n'accorde pas publication ; reprise et révocation à contracter |
| C-POST | 04/01 | texte, audience, média prêt, clé opération, version → objet/état/version | Idempotence création ; verrou/version édition ; résultat inconnu réconciliable |
| C-FEED | 04/01 | curseur opaque et contexte → objets filtrés, curseur suivant, fin | Ordre/départage et concurrence définis serveur ; dédoublonnage par ID sans reclassement arbitraire |
| C-SOCIAL | 04/01 | cible, état souhaité de relation/réaction ou commentaire, clé/version → état confirmé | État souhaité préférable à toggle ambigu ; quotas et droits revérifiés |
| C-NOTIFY | 04/01 | curseur ou préférences/version → notifications filtrées/état | Revalider destination ; aucune fuite par aperçu ou compteur |
| C-SAFETY | 04/09/10 | cible opaque, catégorie, description minimale, clé → accusé/référence/état autorisé | Séparer blocage et dossier ; doublon/cible retirée contractés |
| C-APPEAL | 04/09/10 | décision autorisée, explication, clé → recours lié/état | Recevabilité et accès compte restreint ; aucune preuve tierce retournée |
| C-DATA | 04/15 | type demande, vérification, clé → référence/état/expiration | Réauthentification selon 14 ; export réservé ; suppression asynchrone distincte de réussite finale |
| C-COMMUNITY | 04/01/09 | communauté, action adhésion, version → rôle/état/règles | Conditionnel MVP ; rôles strictement locaux ; départ et contenus à spécifier |
| C-MEASURE | 13/14/15 | nom événement approuvé, résultat, famille écran → acceptation technique | Pas de donnée saisie, secret ni replay de session ; échec non bloquant et buffer borné à définir |

Contrat commun demandé pour chaque ligne : version explicite et compatibilité ascendante ; authentification et autorisation par opération ; schémas et limites ; codes métier stables traduisibles ; corrélation assainie ; timeouts distincts lecture/mutation/upload ; politique de retry ; clé d'idempotence et durée/déduplication si applicable ; versions pour concurrence ; audit des actions sensibles côté serveur. Une modification incompatible exige revue 03/04/05/06/18 et période de migration documentée, sans durée inventée. Tous les tests de contrat restent PLANNED.

## UX, accessibilité, compatibilité, SEO et performance

**Design System commun.** Demander à 02 les comportements de Field/ErrorSummary, Dialog, Navigation, StatusNotice, Progress, Skeleton, EmptyState, ErrorState, Card et Pagination. Ne pas dupliquer tokens ou règles d'interaction dans chaque page. L'UI conserve libellés visibles, ordre de focus logique, fermeture et restauration du focus des dialogues, actions accessibles au clavier, annonces d'erreur/succès non intrusives et réduction des animations. Le chargement ne prend pas le focus ; une erreur de formulaire place le focus sur son résumé et relie les champs invalides.

**Responsive et langues.** Proposition de couverture : largeurs 320, 390, 768 et 1280 CSS px, zoom 200 %, grands textes et pseudolocalisation. Pas de défilement horizontal sur les formulaires/cartes ordinaires ; actions sans survol obligatoire. Externaliser les messages, utiliser pluriels/formats locaux et langue du document, supporter les noms multilingues sans en déduire origine/pays. Langues réellement traduites et supportées à décider par 16/09 ; aucune conformité d'accessibilité certifiée ici.

**Navigateurs — tous NON TESTÉS.** Proposition : Chrome, Edge et Firefox desktop, Safari macOS/iOS et Chrome Android ; version stable au gel QA et précédente lorsque disponible/supportée. 18/14 doivent fixer versions exactes, OS, appareils et technologies d'assistance dans le rapport d'exécution. Prévoir NVDA avec Firefox/Chrome et VoiceOver avec Safari. Aucun numéro de version ni compatibilité actuelle affirmé ; pas de dépendance à une API navigateur particulière choisie par ce document.

**Connexion limitée.** Images dimensionnées avec variantes autorisées, chargement différé hors écran, pagination explicite et squelette de taille stable ; texte et commandes prioritaires. Ne pas télécharger toutes les pages ni ajouter une vidéo au fil candidat. Pas de service worker/cache offline privé proposé au pilote avant revue 14/15.

**SEO.** Rendu indexable seulement pour éditorial validé puis, si arbitrage favorable, objets publics explicitement indexables. Ne pas considérer `noindex` ou robots comme contrôle d'accès. HTML, payload, Open Graph, JSON-LD, sitemap, préchargement, cache CDN et images doivent respecter la même politique. Rendu dynamique privé et cache partagé interdit pour données personnelles constituent une proposition à 03/14 ; configuration finale et preuve attendues avant ouverture. Retrait de l'index externe ne peut pas être promis instantané.

**Budgets proposés, non mesurés.** Pour un scénario contrôlé à 1,6 Mbit/s, RTT 150 ms et ralentissement CPU ×4, proposer LCP ≤ 2,5 s, CLS ≤ 0,1 et INP ≤ 200 ms sur parcours prioritaires ; première route ≤ 250 Kio de JavaScript transféré compressé et écran initial avec images ≤ 1 Mio. Ce sont des objectifs de discussion, pas des résultats ni une déclaration de conformité à un standard. 14/18 doivent arbitrer profil matériel/réseau, méthode, échantillon et seuils avant gate. Répéter les essais de navigation, composer et signalement ; publier distribution et conditions, sans déduire un percentile terrain d'un seul essai labo. Les mesures terrain restent conditionnées par 13/15.

## Acceptation et vérification

Les scénarios sont **PLANNED**, aucune exécution applicative. Préconditions communes : décision sur le lot, contrats et permissions approuvés, application et environnement de test disponibles ; 18 transforme ces scénarios en tests exécutables. Les identifiants locaux W01–W16 et TEST-WEB-* sont proposés, unicité interbranches à contrôler par 17/18. Ils ne remplacent pas les AC-J*.

| Critère / Test proposé | Besoin | Scénario observable | Type / statut | Blocage |
| --- | --- | --- | --- | --- |
| W01 / TEST-WEB-0001 | FEAT-018/021 | Étant donné chaque écran P0, parcourir et soumettre au clavier/lecteur d'écran ; focus, erreurs et résultat perceptibles sans perte de commande | Manuel accessibilité + E2E / PLANNED | 02/16/18, UI absente |
| W02 / TEST-WEB-0002 | FEAT-004/018 | Étant donné objet privé et visiteur, ouvrir URL/HTML/payload/média/métadonnées ; aucune donnée protégée exposée ; page éditoriale approuvée accessible | API + E2E + cache / PLANNED | 03/04/14/15 |
| W03 / TEST-WEB-0003 | FEAT-001/002 | Session expirée ou lien consommé : action refusée, reprise compréhensible, aucune donnée du compte précédent ni redirection externe | API + E2E / PLANNED | C-IDENTITY |
| W04 / TEST-WEB-0004 | FEAT-002/004 | Déconnexion confirmée puis retour navigateur/onglet/rechargement et connexion d'un autre compte : données privées précédentes absentes | E2E / PLANNED | Session/cache 04/14 |
| W05 / TEST-WEB-0005 | FEAT-003/005 | Deux éditions concurrentes et suivi répété : conflit explicite sans perte silencieuse ; relation unique et état confirmé après recharge | Contrat + E2E / PLANNED | C-PROFILE/C-SOCIAL |
| W06 / TEST-WEB-0006 | FEAT-004/012 | Changer audience ou bloquer : objets locaux connus retirés après confirmation ; relecture distante respecte la nouvelle règle dans le délai contractuel | API + multi-session / PLANNED | Délai/invalidation 03/04 |
| W07 / TEST-WEB-0007 | FEAT-006/007 | Réponse publication perdue après commit serveur, réessai avec même opération : un seul post et état final réconcilié | Injection panne + intégration / PLANNED | Idempotence 04 |
| W08 / TEST-WEB-0008 | FEAT-007 | Fichier refusé ou traitement en échec : jamais annoncé publié ; aperçu retiré à abandon/déconnexion ; alt préservé jusqu'à confirmation autorisée | Média + E2E / PLANNED | 08/15 |
| W09 / TEST-WEB-0009 | FEAT-008/022 | Ajouter/retirer des posts pendant pagination : ordre contractuel, aucun doublon ; erreur suite distincte de fin ; retour conserve position autorisée | Contrat + E2E / PLANNED | Curseur/ordre 04, UX 02 |
| W10 / TEST-WEB-0010 | FEAT-009/010 | Parent devenu inaccessible avant commentaire/réaction : refus sans écriture, aucune réapparition du parent dans le cache | API + E2E / PLANNED | C-SOCIAL |
| W11 / TEST-WEB-0011 | FEAT-011 | Notification visant contenu retiré puis clic : aperçu et détail ne dévoilent rien ; préférence sauvegardée reste effective après recharge | API + E2E / PLANNED | C-NOTIFY |
| W12 / TEST-WEB-0012 | FEAT-012/013 | Signalement avec accusé perdu : état incertain visible, reprise sans faux succès ; cible ne reçoit ni auteur ni description privée | API + E2E / PLANNED | 09/10/04 |
| W13 / TEST-WEB-0013 | FEAT-014/015 | Compte restreint autorisé à contester : atteint décision et recours ; ne retrouve aucune capacité sociale interdite ni preuves d'autrui | Permissions + E2E / PLANNED | Politique 09/14/15 |
| W14 / TEST-WEB-0014 | FEAT-016 | Export expiré/autre compte refusé ; erreur de suppression montre état réel ; suppression demandée distincte de purge terminée | API + E2E / PLANNED | Cycle et sauvegardes 04/14/15 |
| W15 / TEST-WEB-0015 | FEAT-020 | Rôle local retiré pendant session : action refusée après revalidation ; aucune extension de droits à une autre communauté | API + E2E / PLANNED | Arbitrage inclusion et C-COMMUNITY |
| W16 / TEST-WEB-0016 | FEAT-018/019/021 | Sur profils réseau/écran retenus, exécuter parcours et rapporter budgets ; inspecter événements : aucun contenu/secret, collecte inactive si non autorisée | Performance + privacy + responsive / PLANNED | Budgets/collecte 13/14/15/18 |

Contrôles documentaires exécutés et commit publié : consignés dans le compte rendu de PR. Ils ne valident pas les parcours ci-dessus. Aucun résultat navigateur, benchmark, test sécurité applicatif ni déploiement n'est attesté.

## Décisions proposées et contradictions à arbitrer

Réutiliser DEC-0002 pour l'arbitrage MVP ; ne pas créer un numéro DEC/ADR concurrent. Les labels WEB-CONFLICT et WEB-DEP sont des repères historiques locaux à mapper au registre par HQ/17.

| Sujet / statut | Objectif et problème | Recommandation, alternatives non rejetées | Impacts et autorité |
| --- | --- | --- | --- |
| WEB-CONFLICT-01, OUVERT | Définir la valeur communautaire sans élargissement implicite | Comparer A follow seul, B communautés minimales, C les deux ; 01/19 documentent besoin, 04/09/10 effort et exploitation avant choix | P0, DEC-0002 ; navigation, permissions et coût humain ; HQ avec 01/03/04/09. Ancien Backend BE-09 différé cité v0.1, statut courant NON REÇU ; HQ FEAT-020 est désormais explicitement conditionnel, pas une contradiction validée |
| Stack et surface, À VÉRIFIER | Mandat Next.js/React/TypeScript vs registre qui attend arbitrage de stack/surface | Conserver demande comme entrée ; demander sa ratification ciblée à 03/HQ ; comparer rendu public/privé et coûts avant ADR, sans choisir un autre framework localement | P0, impact maintenance/cache/SEO ; 03/14/20 ; aucun changement de stack exécuté |
| Recherche et démarrage réseau, PROPOSÉ | FEAT-023 Phase 2 laisse à préciser comment trouver les premiers comptes | Pilote via liens directs/liste éditoriale de profils accessibles validée par 01/19 ; alternative recherche limitée MVP à chiffrer | P0 pour utilisabilité ; coût éditorial vs API/recherche, permissions 15 ; HQ/01 arbitrent, pas de classement MVP silencieux |
| SEO social, PROPOSÉ | Acquisition publique peut exposer données et caches | Éditorial indexable d'abord ; profils/posts indexables seulement après règles et invalidation ; alternative ouverture publique élargie non rejetée | P0 sécurité, P1 acquisition ; valeur Growth vs surface d'exposition ; 01/03/14/15/HQ |
| Écarts de classement, PROPOSÉ | Ancien Web plaçait professionnel/Studio large en Phase 3 | Examiner présence pro et Studio initial Phase 2 FEAT-027/028 ; paiement reste Phase 3 FEAT-031 ; Hub/événements demandent IDs et définition | 01/HQ avec 07/12/17 ; éviter de confondre outils initiaux et produits avancés ; aucun périmètre livré |

Critère de réexamen : avis spécialisés référencés, DEC-0002 enregistrée, périmètre et budget/capacité pilote suffisamment définis. Aucune alternative n'est déclarée rejetée. Les choix locaux réalisés se limitent à la structure de cette spécification et à la réutilisation des identifiants FEAT/AC existants.

## Dépendances, risques et transmission

Toutes les demandes suivantes restent **À TRANSMETTRE** aux discussions ; publication GitHub ne prouve ni leur réception ni leur approbation. Les destinataires n'ont pas été automatiquement sollicités. Lecture ciblée de ce fichier et des lignes citées, sans demande de refaire le corpus.

| Repère / destinataire | Question précise et livrable attendu | Blocage réel |
| --- | --- | --- |
| WEB-DEP-01 — HQ/01, avis 06/07/12/19 | DEC-0002 : web en premier, communautés, découverte sans recherche, définition Hub/événements, portée Studio/pro ; périmètre inclus/exclu et FEAT manquants | Implémentation du lot concerné et estimation ; rédaction indépendante possible |
| WEB-DEP-02 — 02 | Écrans/états de la matrice, composants communs, comportement clavier/focus, lecture/fin du fil et cible accessibilité | UI finale et validation des tâches ; analyse de contrats possible |
| WEB-DEP-03 — 03/04/08 | Revoir C-IDENTITY à C-COMMUNITY : schémas, session, erreurs, curseurs, résultat inconnu, versions, médias et délais d'invalidation ; ratification stack | Intégration métier, confidentialité et gestion de reprise |
| WEB-DEP-04 — 14/15, avec 13 | Matrice de visibilité/âge/pays, session/CSRF/cache/SEO, brouillons et schémas d'événements/finalité/rétention | Authentification, exposition publique et collecte ; analytics peut rester désactivé |
| WEB-DEP-05 — 09/10 | États accusé/décision/recours, droits compte restreint, cible supprimée et doublon ; preuve de capacité de traitement | Parcours sécurité complet et ouverture du pilote |
| WEB-DEP-06 — 18/20/21, avis 14 | Revue W01–W16, versions/appareils, budgets proposés, emplacement futur Web et gates de PR | Preuves qualité et démarrage lot autorisé ; pas la présente documentation |
| WEB-DEP-07 — 16/09/15 | Langues réellement servies, notices/support, formats/écritures et pays admissibles | Ouverture du pilote et traduction ; structure localisable indépendante |

| Risque réutilisé | Impact / propriétaire | Mesure proposée / état |
| --- | --- | --- |
| WEB-RISK-01 | Critique : fuite HTML/cache/média après restriction ; 03/04/14/15 | Contrat d'accès et invalidation, W02/W04/W06 ; OUVERT |
| WEB-RISK-02 | Élevé : signalement ou recours sans traitement effectif ; 09/10 | États probants, accès compte restreint, preuve opérationnelle avant pilote ; OUVERT |
| WEB-RISK-03 | Élevé : empilement de fonctions présenté comme MVP validé ; HQ/01 | Phases explicites et DEC-0002 ; OUVERT |
| WEB-RISK-04 | Moyen à élevé : médias lourds et échecs réseau produisant doublons/perte de saisie ; 05/08/18 | Budgets à mesurer, résultat inconnu et idempotence, W07/W08/W16 ; OUVERT |
| WEB-RISK-05 | Élevé : interfaces de consentement/pays/langue non conformes aux décisions ; 13/15/16 | Pas de collecte avant revue, libellés et règles localisés ; OUVERT |

Probabilités non évaluées ; ces niveaux expriment un impact candidat, sans analyse spécialisée achevée. Les risques et demandes existants RISK-0001 à 0004 et INT-0001 à 0010 restent au registre HQ ; 17/HQ doivent mapper les repères Web sans les dupliquer ni les clôturer automatiquement.

## Compte rendu et prochaines étapes

1. **Décisions prises/à valider** : matrice et identifiants réutilisés ; aucun MVP, droit, stack globale ou budget approuvé. Arbitrages de la section précédente à HQ et propriétaires.
2. **Livrable** : ce fichier v0.2 répond à M0-TEAM-05 et consolide les cadrages v0.1 ; cible canonique `documentation/web-application/web-requirements.md`. Branche/PR/commit réels précisés dans la PR de contribution, dépendante de #2.
3. **Tests** : uniquement contrôles documentaires exécutés et rapportés dans la PR ; W01–W16 PLANNED, aucun test applicatif exécuté. Aucun navigateur testé.
4. **Questions ouvertes** : périmètre et découverte 01/HQ ; session/contrats/invalidation 03/04/14 ; visibilité et cycle de données 15 ; traitement/recours 09/10 ; DS 02 ; langues 16 ; budgets et mesure 13/18.
5. **Dépendances** : WEB-DEP-01 à 07, À TRANSMETTRE ; aucune réception spécialisée inférée de la publication.
6. **Risques** : WEB-RISK-01 à 05 ouverts ; cette revue documentaire n'est ni audit sécurité, ni recette, ni validation juridique.
7. **Suite/HQ** : intégrer la référence de cette PR dans la ligne 05 du tableau de coordination après examen ; arbitrer les sujets ciblés avec leurs propriétaires ; faire normaliser les contrats et règles du premier lot ; autoriser ensuite seulement son implémentation avec 20 et revue 21. Ne pas fusionner automatiquement. Les autres équipes peuvent continuer leurs parties indépendantes pendant ces arbitrages.
