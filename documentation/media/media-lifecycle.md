# Cycle de vie des médias — Fondation M0

## Identification et statut

| Champ | Valeur |
| --- | --- |
| Objectif | Définir upload, validation, traitement, publication, retrait et purge des images du pilote candidat |
| Propriétaire | 08 — Média / Vidéo / Caméra ; mandat M0-TEAM-08 ; aucun reviewer humain présumé |
| Destinataires | 00, 01, 02, 03, 04, 05, 06, 09, 10, 13, 14, 15, 16, 17, 18, 20, 21 |
| Date / version | 29 septembre 2026 / v0.1 |
| Référence examinée | PR [#2](https://github.com/yyogas/social-network/pull/2), branche documentation/m0-team-coordination, commit dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957 |
| Statut | PROPOSÉ — avis spécialisés et arbitrages HQ attendus ; non approuvé pour implémentation |
| Périmètre | FEAT-007 et dépendance avatar de FEAT-003 ; effets FEAT-004/012/014/015/016 ; fondations différées FEAT-026/033 |
| Classement | MVP image candidat P0 ; phases futures proposées ci-dessous |
| Limite des preuves | Aucun traitement média implémenté ou testé dans ce travail ; contrôles documentaires uniquement |

Entrées lues : [mandat](../teams/work-orders.md), [modèle](../teams/deliverable-template.md), [plan](../documentation-plan.md), [vision](../product/product-vision.md), [catalogue](../product/feature-catalog.md), [parcours](../product/user-journeys.md), [gouvernance](../governance.md), [conventions](../repository-conventions.md), [registre](../project-governance/decision-register.md), [statut](../project-governance/project-status.md), [stratégie QA](../quality/test-strategy.md). Revue ciblée J01/J02/J04/J05/J06/J07 pour les interfaces Media.

Travaux réutilisés : drafts de discussion `SOCIAL-08-Media-Platform-v0.1.md` et `SOCIAL-M0-MEDIA-FONDATION-v0.1.md`, du 29 septembre 2026. Le contenu nécessaire est consolidé ici ; leur disponibilité hors GitHub n'est pas un prérequis d'implémentation. Ce livrable fait évoluer leurs propositions, sans prétendre remplacer une décision approuvée.

| Nature | Éléments |
| --- | --- |
| CONFIRMÉ | Mandat documentaire reçu ; GitHub référence centrale ; IDs et phases du catalogue lus au SHA indiqué |
| PROPOSÉ | Limites, profils image, interfaces, permissions techniques, stratégie de retrait, hypothèses de coût et critères ci-dessous |
| À VÉRIFIER | Formats réellement produits par clients, capacité humaine de modération, coût et compatibilité des fournisseurs, budgets/SLO |
| NON REÇU | Décisions finales MVP/stack/audience/âge/rétention, contrats backend et permissions approuvés, benchmarks, preuves applicatives |

Une classe MVP et une priorité P0 sont des propositions de besoin, jamais une preuve d'approbation. La stack annoncée dans les mandats reste une orientation à examiner avec 03/HQ ; ce document ne la fige pas.

## Besoin, fonctionnalités et parcours

### Inventaire et phases

| Référence existante | Fonction / résultat utilisateur | Phase proposée | Priorité | Dépendances / condition d'entrée |
| --- | --- | --- | --- | --- |
| FEAT-007 | Ajouter une image et un texte alternatif ; voir traitement, résultat ou erreur ; annuler/réessayer | MVP | P0 | FEAT-004/006, 01/02/04/14/15 |
| FEAT-003, via FEAT-007 | Avatar : même admission sûre, recadrage dérivé, remplacement et retrait | MVP | P0 | Politique visibilité du profil à recevoir ; avatar par défaut en attendant |
| FEAT-004/012/014 | Afficher uniquement les dérivés autorisés, révoquer accès après restriction/blocage/modération | MVP | P0 | Matrice d'accès 09/14/15 et contrats 04 |
| FEAT-015/016 | Conservation restreinte de preuves, recours, export, retrait et purge | MVP | P0 | Politique 09/15 ; pas de durée légale inventée |
| FEAT-026 | Vidéo courte enregistrée, reprise upload, 360p/720p/1080p selon source, HLS/DASH à comparer, miniatures/sous-titres | Phase 2 | P2 | Coût séparé, matrice appareils, droits, modération, ADR 03 |
| FEAT-026, sous-périmètre à confirmer par 01 | Capture simple, filtres, texte/stickers et montage léger ; stories et audio/podcasts à délimiter | Phase 2 | P2 | Capacités produit distinctes à enregistrer par 01 avant engagement ; aucune nouvelle FEAT allouée ici |
| FEAT-026, extension à confirmer | Duo/remix, musique, templates, fond flouté et effets avancés | Phase 3 | P2 | Consentement, droits source/musique, budget et performance |
| FEAT-032 / FEAT-021 | Libellés/alt multilingues dès pilote ; régions/CDN et sous-titres étendus après décision pays | International | P1 | 16/15/09 ; ne pas différer l'accessibilité du pilote |
| FEAT-033 | Live et modération en direct ; AR expérimentale comme idée hors catalogue à arbitrer | Long terme | P3 | Capacité démontrée, procédure d'arrêt ; pas d'inclusion implicite dans FEAT-026 |

### Limites proposées, à soumettre à 01/14/15

Valeurs de travail pour dimensionner un premier protocole ; **aucune valeur validée**. Les contrôles serveur restent obligatoires après compression client.

| Paramètre | Proposition initiale | Motif / point de réexamen |
| --- | --- | --- |
| Entrées | JPEG et PNG statiques uniquement | Réduire la surface de décodage ; HEIC/WebP/GIF/RAW/SVG non promis ; conversion locale éventuelle à tester par 05/06 |
| Nombre | 1 image par publication candidate ; 1 avatar actif | Cohérence avec J02 ; carrousel soumis à 01 |
| Taille | 10 MiB maximum par fichier ; 20 mégapixels ; côté maximum 8 192 px ; toutes limites cumulatives | Borner réseau, mémoire et attaques ; tester photos mobiles avant ratification |
| Dérivés | Aperçu long côté 320 px, affichage long côté 1 600 px ; avatar 128/512 px ; sans agrandissement | Ratio conservé pour post ; recadrage avatar explicite ; qualité et poids cible après corpus |
| Encodage sortie | JPEG pour photos opaques, PNG pour transparence ; orientation appliquée, profil couleur normalisé selon tests | Pas de fichier original servi comme optimisation ; aucun format actif |
| Alt | Texte Unicode éditable, proposition 500 caractères maximum, langue facultative ; pas de génération IA obligatoire | 02/16 précisent comptage, libellés et traitement du champ vide/décoratif ; bloquant UX avant implémentation |
| Admission | 2 sessions simultanées/compte ; 20 initiations/heure et 200 MiB reçus/jour/compte ; budget global d'admission distinct | Limiter abandon et abus ; requêtes rejetées comptées dans un limiteur séparé ; anti-abus multi-comptes à 14 |
| Sessions | Session de 30 min ; autorisation d'upload de 5 min renouvelable si session valide | Tester réseau lent ; quota réservé et libéré explicitement |
| Nettoyage | Session expirée nettoyée sous 24 h ; média READY non attaché sous 24 h | Proposition opérationnelle ; exceptions preuve/conservation à valider par 15 |

Le MIME réel, le nombre de frames et le décodage sont contrôlés en plus de la signature. APNG ou autre animation cachée est refusé. Une taille compressée acceptable n'autorise pas un décodage sans limite. Aucun import par URL externe au pilote candidat (sinon contrat SSRF séparé).

### Parcours et UX

Auteur authentifié et admissible : choisir une image → aperçu local et alt → confirmation de l'audience du parent → upload privé → validation/traitement → décision de distribution → attachement/publication atomique côté métier → confirmation. L'échec conserve le texte saisi si autorisé ; publier sans image demande une action explicite. Aucun succès avant confirmation serveur.

L'avatar suit le même traitement mais possède un parent profil, jamais une audience de post par défaut. L'ancien avatar reste actif jusqu'au remplacement confirmé ; son accès est ensuite révoqué suivant la politique approuvée. Une suppression du compte retire aussi les avatars et dérivés historiques.

UX : état vide/import, progression accessible, traitement sans faux pourcentage, erreur avec action réessayer/retirer, indisponibilité et média retiré. Clavier, focus stable, annonces lecteur d'écran sans répétition excessive ; alt associé à la version visible, modifiable sans remplacement des pixels. Messages localisables ; texte alt traité comme texte non fiable, jamais HTML exécuté. En attente/rejet de modération, l'auteur voit seulement le motif autorisé et le parcours de recours. Persistance du brouillon local et nettoyage à la déconnexion à approuver par 15 ; aucun contenu privé en notification.

## États et transitions

Séparer trois dimensions évite de confondre un encodage réussi avec une publication autorisée.

| Dimension | États proposés | Invariant |
| --- | --- | --- |
| Traitement | INITIATED, UPLOADING, UPLOADED, VALIDATING, PROCESSING, READY, FAILED_RETRYABLE, FAILED_FINAL, CANCELLED | READY prouve seulement la préparation technique ; accès audience interdit à ce seul titre |
| Modération | PENDING, ALLOWED, REVIEW, RESTRICTED | Politique 09 décide pré/post-modération ; indisponibilité du contrôle requis laisse PENDING |
| Distribution | UNATTACHED, ATTACHED_DRAFT, PUBLISHED, WITHDRAWN, PURGE_PENDING, PURGED | Lecture exige parent autorisé et droit courant ; PURGED ne signifie pas effacement de toute sauvegarde |

| Déclencheur | Précondition et effet | Reprise / refus |
| --- | --- | --- |
| Initier | Compte, usage et quota admissibles ; réserver un budget, créer ID opaque et objet privé | Même clé + même requête rend la même session ; payload différent → conflit |
| Compléter | Session propriétaire valide ; contrôler taille/checksum ; figer une version d'objet immutable | URL d'upload réutilisée ne peut écraser la version à analyser ; sinon copier vers clé privée non inscriptible puis traiter |
| Valider/traiter | Worker borné et isolé, sans réseau sortant arbitraire ; scan et décodage autorisés | Timeout/ressource → privé et échec ; retry borné sans bypass du scan |
| Publier/attacher | Parent contrôlé, READY, ALLOWED, versions valides | Vérifier au commit ; suppression simultanée prime ; ni média d'autrui ni attachement à deux parents dans cette proposition |
| Réduire audience/bloquer | Changer l'autorité d'accès du parent, révoquer lecture média synchroniquement ou refuser la confirmation | Purge CDN asynchrone ensuite ; aucun simple événement eventual ne suffit à la confidentialité |
| Retirer | Révocation logique et tombstone avant confirmation, arrêter jobs et nouvelles URL | Jobs tardifs consultent tombstone/génération et ne republient pas |
| Purger | Inventorier original, dérivés, temporaires et versions ; vérifier absence de conservation restreinte justifiée | Retry avec backoff, alerte ; vérifier chaque clé avant PURGED ; backups séparés |
| Recours accepté | 09 autorise ; vérifier parent, compte, audience, absence de demande de suppression et présence d'objets | Nouvelle génération d'accès ; aucun lien ancien réactivé ; si données purgées, restauration non promise |

## Permissions, données et contrats

### Matrice d'accès proposée

| Acteur | Action / portée | Autorisation et refus |
| --- | --- | --- |
| Anonyme | Lire dérivé du parent | Uniquement si politique publique explicitement approuvée ; sinon refus sans révélation d'existence |
| Membre / tiers | Lire image ou miniature | Authentification si requise, parent accessible, blocages/statuts évalués à chaque requête autorisée ; aucun droit d'écriture |
| Auteur | Initier, compléter, annuler, état de sa session, alt, attacher, retirer | Propriété et permissions parent vérifiées ; auteur ne contourne pas une restriction Safety |
| Compte suspendu ou bloqué | Écriture/lecture selon politique | Refus des actions interdites côté serveur ; endpoints de suivi/recours uniquement selon permissions explicites 09/14 |
| Modérateur | Voir preuve et décider dans un dossier | Habilitation limitée au dossier, motif et audit ; jamais accès général aux buckets |
| Support | Suivre erreur technique | Métadonnées minimales ; pixels et preuves exclus sauf permission distincte approuvée |
| Worker | Lire original versionné, écrire dérivés de son job | Identité technique, portée limitée ; aucun pouvoir de publication ou d'extension de rétention |
| Opérateur purge | Effacer objets listés | Tâche interne autorisée, contrôles de rétention et audit ; pas de suppression arbitraire par clé client |

**Proposition d'accès et révocation :** origine privée ; vérification d'autorisation *avant* réponse, même sur cache hit. Lecture via passerelle authentifiée ou edge avec contrôle courant de l'audience et mécanisme de révocation. Recommandation pilote : passerelle de lecture qui vérifie l'état autoritaire ; comparer coût à edge avec 03/14. Cache objet interne possible, réponse privée client `no-store` proposée. Ne jamais fournir une URL d'origine contournant ce chemin. Jeton lié au média/version/contexte/client si applicable, et recontrôlé ; une URL bearer courte seule reste utilisable jusqu'à expiration et n'est donc pas suffisante pour promettre révocation immédiate.

Le refus des nouvelles lectures doit être effectif dès confirmation du retrait/restriction. Octets déjà reçus ou requêtes déjà autorisées/en cours ne sont pas récupérables ; coupure de flux en cours à qualifier. Cache tiers, captures et téléchargements antérieurs ne peuvent être effacés par la plateforme. Les previews externes privées sont exclues ; previews publiques éventuelles à arbitrer séparément. Si les dépendances d'autorisation sont indisponibles, refus contrôlé plutôt que diffusion avec permission périmée.

### Données et cycle de vie

| Catégorie / origine | Finalité et stockage proposé | Visibilité / modification / export | Conservation et suppression |
| --- | --- | --- | --- |
| Session, compte/parent, taille/quota, version, empreinte serveur | Admission et intégrité ; métadonnées transactionnelles | Auteur : état minimal ; worker : tâche ; empreinte non exposée ni utilisée pour dédupliquer entre comptes | Durée session/orphelin proposée ci-dessus ; 15 valide traces minimales |
| Original utilisateur | Validation et dérivés ; zone privée de quarantaine versionnée | Aucun public ; accès technique borné ; export seulement après autorisation/scan et décision 15 | Purge après dérivés et fin de finalité proposée ; délai définitif non reçu ; pas de promesse de conservation permanente |
| Dérivés + dimensions | Affichage ; stockage privé, cache interne | Droits du parent ; remplacement par nouvelle génération, export propre utilisateur selon contrat | Retrait logique puis purge ; versions anciennes incluses |
| Alt, langue, cadrage | Accessibilité et présentation | Même audience que parent ; auteur édite ; traitement/modération texte selon 09 | Suppression/export avec parent, pas dans logs techniques |
| Décision, preuve, recours | Modération, accès interne cloisonné | 09/10 habilités, export filtré selon 15 ; auteur reçoit résultat autorisé | Durée, finalité et gel exceptionnel à documenter par 15 ; retrait public demeure immédiat |
| Journaux, événements, mesure | Diagnostic, coûts, preuves d'action | IDs pseudonymes et codes, accès 14/13 limité ; aucun pixel/alt/URL signée ni nom de fichier sensible | Durées minimisées à définir avec 15 ; effacement/agrégation selon catégorie |
| Sauvegardes / réplications | Reprise après incident | Opérateurs habilités ; pas de lecture publique depuis backup | Délai d'expiration à recevoir ; rejouer tombstones avant toute remise en service restaurée |

Aucune rétention indéfinie implicite. Un gel de preuve ne permet ni republication ni accès support général. Registre de purge distingue stockage actif, cache, réplication, conservation restreinte et sauvegardes ; un état PURGED actif ne masque pas une conservation résiduelle.

### Interfaces candidates v0.1

Identifiants ci-dessous locaux au contrat Media, à normaliser avec 04, sans créer de nouvelles FEAT. Routes indicatives. Authentification selon contrat 04/14 ; limites ci-dessus proposées. Enveloppe erreur : code stable, message localisable, retryable, correlation_id ; jamais détails du stockage. Masquage 403/404 à harmoniser sans révéler un média privé.

| ID / route indicative | Producteur → consommateur | Entrée / sortie | Contrôles et erreurs |
| --- | --- | --- | --- |
| MEDIA-API-01 POST /v1/media/uploads | 05/06 → 04/08 | usage post_image/avatar, bytes, type déclaré, clé idempotence → media_id, session_id, expires_at, autorisation upload | Compte/quota/usage ; 401/403, 413 taille, 415 format, 429 quota |
| MEDIA-API-02 POST /v1/media/uploads/{id}/complete | 05/06 → 04/08 | version objet/empreinte si disponible → 202 + état | Objet effectif contrôlé côté serveur ; 409 session/version, 422 intégrité ; ne pas croire une clé objet client |
| MEDIA-API-03 GET /v1/media/{id}/status | 05/06 → 04/08 | ID → trois dimensions d'état et reprise permise | Auteur/opérateur autorisé ; 404 masqué ; aucune URL privée brute |
| MEDIA-API-04 attachement au commit du parent | 04 Posts/Profiles → 08 | media_id, parent_id/type, expected_version, alt/cadrage → référence de dérivés | Propriétaire, READY/ALLOWED, quota parent ; 409 concurrence, 422 non prêt ; publication parent autoritaire |
| MEDIA-API-05 GET /v1/media/{id}/variants/{variant} | Lecteur → contrôle d'accès 04/08 | contexte parent/session → octets dérivés autorisés | Audience/statuts version courante avant cache hit ; 404/403, 503 autorité indisponible |
| MEDIA-API-06 cancel / withdraw | Auteur ou 09/10 → 04/08 | ID/version, motif codé, clé idempotence → état retiré | Pouvoir exact et parent ; 409 concurrence, 503 révocation non confirmée ; jamais faux succès |

Timeout/retry candidats : API de contrôle 10 s maximum (à mesurer) ; après réponse perdue consulter état avant réessai ; 3 reprises client avec backoff et jitter, respecter Retry-After ; aucun retry automatique des refus métier. Upload image simple rejoué entièrement après contrôle d'état, sous quota réservé ; multipart à arbitrer seulement si bénéfice mesuré. Workers : budget proposé 30 s et 256 MiB par image, à vérifier sur corpus 20 MP ; 3 tentatives pour panne transitoire puis file d'échec/alerte, pas de retry automatique sur contenu invalide. Ces budgets non mesurés bloquent la validation de capacité, pas la rédaction.

Concurrence : idempotency key liée à acteur/opération et empreinte de requête ; durée proposée au moins session + 24 h, à aligner avec 04/15 ; contrôle de version/tombstone au commit ; quota réservé atomiquement et consommation libérée au terme. Les traitements à réception multiple ne doublent pas les dérivés. Pas de déduplication inter-comptes sans analyse séparée.

Événement MEDIA-EVENT-01 v0.1 : `media.state.changed`, producteur 08 → 04/09/14, avec event_id, schema_version, media_id, parent_ref si autorisée, processing_state, moderation_state, distribution_state, state_version, occurred_at, correlation_id. Authentification service, ACL par consommateur ; pas de contenu utilisateur. Livraison au moins une fois proposée, durable avec transaction/outbox à décider 03/04 ; consommateur déduplique event_id, ignore version obsolète, relit l'autorité sur trou de séquence. Retry borné puis file d'échec et réconciliation ; notification asynchrone ne remplace jamais le refus synchrone d'accès.

Tâches MEDIA-JOB-01 traitement / MEDIA-JOB-02 purge : version d'objet et génération, identité service, budget, idempotence (media_id, generation, job_kind), lease/timeout et compteur. Worker valide état avant écriture finale ; staging inaccessible puis promotion référencée. Purge idempotente traite clé déjà absente comme succès, enregistre les clés encore présentes et réessaie sans déclarer PURGED. Panne file/stockage : état en attente visible et privé, réconciliation depuis autorité, alerte 14.

Compatibilité : contrats v0.1 non approuvés ; schémas versionnés à adopter par 04 ; ajout optionnel compatible, suppression/renommage ou nouvel état non géré nécessite version et migration consommateurs. État inconnu côté client = attente/indisponible, jamais publié. Tests proposés ci-dessous couvrent API, workers et cache ; aucun contrat OpenAPI exécuté ici.

## Coût, performance et scalabilité

### Images : modèle séparé

Hypothèse illustrative **non mesurée** : 1 000 uploads/jour, original moyen 3 MB décimaux, deux dérivés totalisant 0,6 MB, 30 jours, original conservé 1 jour uniquement pour calcul. Fin de mois : 18 GB de dérivés + 3 GB d'originaux = 21 GB actifs, hors avatars, copies, backups, preuves et orphelins. Sur une arrivée uniforme, stockage moyen du premier mois ≈ 9 + 3 = 12 GB-mois (approximation de régime pour originaux). Ce n'est pas une proposition de durée privacy. 20 lectures/image du lot × 0,3 MB servis en moyenne = 180 GB sortants ; un hit ratio hypothétique de 90 % donne environ 18 GB origin→CDN, sans réduire les 180 GB vers lecteurs. Ajouter previews/chargements interrompus et overhead de protocole.

Coût = GB-mois actifs × tarif stockage + backup/versions + requêtes objet/CDN + secondes CPU validation/encodage × tarif calcul + modération humaine/automatique + GB origin + GB servis × tarifs réseau + logs et exploitation. Tarifs, régions et devis NON REÇUS ; aucun montant en euros revendiqué. Pas de double comptage si fournisseur inclut un poste. Coût passerelle autorisée à comparer explicitement au cache edge.

### Vidéo différée

FEAT-026 : coût calculé à partir minutes source, somme des débits renditions × durée / 8, temps encodeur par profil, sous-titrage/minute, modération et durée réellement visionnée × débit livré / 8. Upload reprenable, audio et keyframes/packaging ajoutent des postes distincts. Exemple purement arithmétique : 10 000 minutes regardées à 2 Mbit/s représentent 150 GB de payload ; exclut source, renditions stockées, protocoles et préchargement. Aucun budget image ne doit être présenté comme couvrant vidéo/live. HLS/DASH, codecs et encodeurs restent options Phase 2 à soumettre à 03/14.

### Protocole de mesure proposé

1. 01/19 fixent cohorte, publications/jour, vues et simultanéité ; 15 valide corpus synthétique/licencié sans données privées.
2. Corpus JPEG/PNG : petits/grands fichiers, orientations, transparence, couleurs, limites et malformations ; appareils/réseaux définis avec 05/06/18.
3. Mesurer taille entrée/dérivés, CPU/RAM maximale, durée traitement, échecs, coût ; distinguer cache froid/chaud et refus d'accès.
4. Charge progressive par paliers issus du pilote ; mesurer p50/p95/p99 upload→READY, âge/profondeur file, latence première image, saturation et débit purge. Injecter perte réseau, redelivery, worker tué, panne stockage/auth/cache.
5. Démontrer retrait sur requêtes neuves/cache chaud, lien ancien, jobs retardés et restore. Consigner SHA, config, versions, corpus, commandes et résultat avant tout objectif de capacité.
6. Fixer avec 14/HQ budgets et alertes ; autoscaling workers borné par budget et admission. Séparer API/traitement, quotas globaux/compte et file d'échec ; pas de Kubernetes/microservices imposés par cette spécification.

## Acceptation et vérification

IDs TEST-MEDIA-* et AC-MEDIA-* proposés localement, unicité globale à confirmer par 18/17. Tous PLANNED ; implémentation/contrats manquants empêchent une exécution applicative. Préconditions communes : limites et politique d'accès approuvées, fixtures fictives, environnement isolé.

| Critère | FEAT / parcours | Étant donné… lorsque… alors… | Test / type | Statut / blocage |
| --- | --- | --- | --- | --- |
| AC-MEDIA-01 | FEAT-007 / AC-J02-01 | Image valide et auteur autorisé ; publication ; seuls lecteurs autorisés reçoivent le dérivé et alt correspondant | TEST-MEDIA-01 / API/E2E | PLANNED — 04/05/18 |
| AC-MEDIA-02 | FEAT-007 / AC-J02-02 | Format interdit, animation masquée ou bombe de pixels ; upload ; refus privé, code stable et aucune variante accessible | TEST-MEDIA-02 / sécurité/intégration | PLANNED — 14/18 |
| AC-MEDIA-03 | FEAT-007 / AC-J02-03 | Réponse perdue ; même complétion/attachement répété ; un seul média et une seule consommation quota | TEST-MEDIA-03 / concurrence | PLANNED — 04 |
| AC-MEDIA-04 | FEAT-004/012 / AC-J02-04 | Lecteur exclu ; accès direct original/miniature/variante ou cache chaud ; aucun octet protégé servi | TEST-MEDIA-04 / API/cache | PLANNED — 04/14 |
| AC-MEDIA-05 | FEAT-004/014 / AC-J02-05 | Ancien accès obtenu ; retrait/audience restreinte confirmé ; nouvelle requête ancien lien refusée même avant purge | TEST-MEDIA-05 / E2E | PLANNED — 03/14 |
| AC-MEDIA-06 | FEAT-007 | Upload interrompu/session expirée ; reprise autorisée ; état compréhensible, budget cohérent, aucun doublon | TEST-MEDIA-06 / réseau | PLANNED — 05/06 |
| AC-MEDIA-07 | FEAT-007/016 / AC-J06-04 | Tombstone puis job retardé/restauration backup ; reprise ; aucun média supprimé ne redevient public | TEST-MEDIA-07 / intégration/restore | PLANNED — 04/14/15 |
| AC-MEDIA-08 | FEAT-007 | Image avec EXIF GPS/orientation ; traitement ; dérivé orienté sans métadonnées privées, original inaccessible | TEST-MEDIA-08 / traitement | PLANNED — 08/14 |
| AC-MEDIA-09 | FEAT-007/018/021 | Auteur clavier/lecteur d'écran ; upload et correction alt ; focus utilisable, état annoncé et texte non exécuté | TEST-MEDIA-09 / accessibilité | PLANNED — 02/05/16/18 |
| AC-MEDIA-10 | FEAT-014/015 / AC-J05-05 | Recours autorisé mais post supprimé ; réexamen ; aucune republication automatique ni réactivation ancien lien | TEST-MEDIA-10 / métier | PLANNED — 09/04 |
| AC-MEDIA-11 | FEAT-003 | Avatar remplacé ; accès ancien dérivé ; refus selon règle de retrait et nouveau portrait cohérent | TEST-MEDIA-11 / E2E | PLANNED — 01/04 |
| AC-MEDIA-12 | FEAT-007 | Objet complété puis URL upload réutilisée ; traitement ; version validée immutable ou échec privé | TEST-MEDIA-12 / sécurité/race | PLANNED — 14/04 |
| AC-MEDIA-13 | FEAT-007/016 | Purge partiellement échouée ; retry ; état PURGE_PENDING jusqu'à vérification, backups déclarés séparément | TEST-MEDIA-13 / panne | PLANNED — 14/15 |
| AC-MEDIA-14 | FEAT-007 | Quota atteint ou scan requis indisponible ; demande ; refus/retry contrôlé, aucune publication ni charge illimitée | TEST-MEDIA-14 / charge/abus | PLANNED — 14/18 |

## Décisions importantes à soumettre

Les labels D1–D3 sont locaux à ce document ; HQ attribuera DEC/ADR sans collision. Statut de chaque fiche : PROPOSÉ, priorité P0, phase MVP candidate. Aucune alternative formellement rejetée.

| Fiche | Objectif / problème | Recommandation et alternatives | Impacts / dépendances / validation |
| --- | --- | --- | --- |
| D1 — format et périmètre | Rendre FEAT-007 exploitable sans chaîne vidéo prématurée | Une image JPEG/PNG + alt, avatar réutilisant pipeline ; alternative formats étendus/carrousel, plus compatible mais plus coûteux | UX mobile HEIC à tester ; moins de décodage/charge ; 01/05/06/14 et HQ valident ; réexaminer si échecs d'import significatifs |
| D2 — distribution révocable | Éviter accès via URL conservée après changement de droits | Origine privée + autorisation courante avant chaque réponse/cache hit ; passerelle simple recommandée ; alternative edge autorisé, ou URL courte seule avec délai résiduel explicitement accepté | Coût lecture/latence et disponibilité contre confidentialité ; 03/04/14/15/HQ arbitrent ; budgets et matrice sont prérequis ; échec → blocage publication privée |
| D3 — original/preuve | Ne pas conserver indéfiniment ce qui sert seulement au traitement | Purge original après fin de finalité technique ; preuve éventuelle en espace restreint avec durée autorisée ; alternative rétention prolongée pour réencodage | Réencodage/export original limités après purge ; coût et privacy réduits ; 09/15/14/HQ fixent exceptions et durées ; réexaminer avant FEAT-026 |

## Dépendances, risques et transmission

Demandes MEDIA-H1–H8 locales, à rattacher par HQ aux INT existants ou nouveaux ; émetteur 08 ; toutes **À TRANSMETTRE**, sans preuve de réception des discussions. La publication GitHub rend le contenu consultable, sans changer ce statut.

| Demande | Destinataire | Question ciblée / livrable attendu | Blocage |
| --- | --- | --- | --- |
| MEDIA-H1 | 00/01 | Ratifier ou modifier une image/10 MiB/JPEG-PNG, alt, avatar et comportement sans image ; delta FEAT-003/007 | Contrat et implémentation |
| MEDIA-H2 | 03/04/14 | Choisir D2 ; schéma autorité parent, révocation synchrone, versions immutables et API Media candidates | Distribution et sécurité |
| MEDIA-H3 | 09/10 | Définir ALLOWED/REVIEW, pré/post-modération, rôles preuve, recours et capacité humaine | Politique de publication |
| MEDIA-H4 | 15/14 | Durées original/dérivés/quarantaine/logs/backups, exception preuve, purge/export et restauration | Données et release |
| MEDIA-H5 | 02/05/06/16 | Formats d'entrée réels, alt/cadrage/erreurs accessibles, réseau, persistance locale ; matrice et avis sur limites | Clients ; non bloquant pour présente rédaction |
| MEDIA-H6 | 13/14/19/HQ | Cohorte/volumes, tarifs datés, budget ; calcul image distinct vidéo et protocole de charge | Budget et capacité release |
| MEDIA-H7 | 18/21 | Revoir 14 critères, IDs et scénarios adverses ; exiger preuve retrait/cache/restore | Release, pas rédaction |
| MEDIA-H8 | 17/00 | Indexer ce chemin et résoudre les écarts de phase ci-dessous ; enregistrer avis/commit exact au tableau de coordination | Convergence documentaire |

| Risque local / registre lié | Impact | Mesure / propriétaire / état |
| --- | --- | --- |
| MEDIA-R1, détail RISK-0004 | URL ou cache contourne audience/blocage | D2 et AC-MEDIA-04/05 ; 03/04/14 ; OUVERT critique avant publication |
| MEDIA-R2, détail RISK-0002 | Absence modération/recours opérationnels | MEDIA-H3 et AC-MEDIA-10/14 ; 09/10 ; OUVERT critique avant pilote |
| MEDIA-R3, détail RISK-0004 | Job tardif/restore republie image supprimée | Tombstone/génération, AC-MEDIA-07/12/13 ; 04/14/15 ; OUVERT |
| MEDIA-R4, détail RISK-0001 | Vidéo ou formats étendus inclus sans budget | Classification FEAT-026/033, coûts distincts ; 00/01/08 ; OUVERT |
| MEDIA-R5 | Quotas insuffisants ou incompatibilité photos mobiles | Tests corpus et limites configurées ; 05/06/14 ; OUVERT |

### Écarts corrigés ou à arbitrer

- Drafts de discussion : READY mélangeait préparation et autorisation de modération. Cette proposition sépare traitement/modération/distribution ; contrat final à confronter à 04/09.
- Premier draft général proposait la vidéo au MVP et live en phase suivante ; le mandat GitHub place FEAT-026 Phase 2 et FEAT-033 Long terme. Ce livrable suit ces classes proposées, sans prétendre qu'un arbitrage officiel est déjà approuvé.
- Ancien draft orienté post_image omettait alt et avatar ; FEAT-007/003 et J01/J02 les rendent nécessaires à la revue Media. Ajout ici ; audience profil attendue de 01/15.
- URL signée courte n'est pas preuve de révocation : D2 expose l'alternative et son coût. Ce point doit être tranché avant un contrat d'accès privé.
- Une purge CDN ne récupère pas les copies déjà téléchargées ; les critères portent sur les accès nouveaux contrôlés et sur l'effacement des systèmes maîtrisés.

## Compte rendu de fin d'étape

1. Décisions locales : un livrable de domaine unique, IDs FEAT réutilisés, séparation des états, limites et contrats candidats explicitement PROPOSÉS. D1–D3 restent à valider par HQ et propriétaires.
2. Livrable : ce fichier v0.1 et README de domaine, publiables par branche/PR sur référence #2 ; références exactes de publication et contrôles consignées dans la PR. Pas d'approbation ou fusion revendiquée par le document.
3. Vérification : critères applicatifs tous PLANNED ; aucun test applicatif exécuté. Contrôles documentaires du dépôt et tests du validateur à consigner avec environnement et référence exacte dans la PR, sans les assimiler à la validation des médias.
4. Questions : MEDIA-H1–H6, notamment audience, modération, durées, formats clients et budget ; absence de réponse bloque seulement le lot concerné.
5. Dépendances : MEDIA-H1–H8 À TRANSMETTRE. Revues indépendantes et réponses spécialisées NON REÇUES dans ce livrable.
6. Risques : MEDIA-R1–R5 ouverts ; chiffres de travail non mesurés ; sécurité, privacy et capacité non validées.
7. Suite/HQ : examiner D1–D3 et les écarts, recueillir avis ciblés, figer contrats et critères, exécuter futurs tests après autorisation d'implémentation. 17 indexe ; 21 revoit cette contribution ; aucun merge automatique.
