# Options et exigences mobiles — Fondation / M0

## Identification et statut

| Champ | Valeur |
| --- | --- |
| Objectif | Décider la surface mobile du pilote et décrire ses contraintes avant réalisation |
| Propriétaire | 06 — Mobile iOS / Android ; aucun reviewer humain affecté |
| Destinataires | 00 MASTER, 01 Produit, 02 UX, 03 Architecture, 04 Backend, 05 Web, 08 Média, 09 Safety, 14 Security/SRE, 15 Privacy, 16 International, 17 Documentation, 18 QA, 20 Engineering, 21 Intégration |
| Date / révision | 29 septembre 2026 ; v0.1 ; référence GitHub `dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957` |
| Mandat | M0-TEAM-06, [ordres de travail](../teams/work-orders.md), [PR de coordination nº 2](https://github.com/yyogas/social-network/pull/2) |
| Modèle suivi | [Livrable spécialisé](../teams/deliverable-template.md) et [plan documentaire](../documentation-plan.md) |
| Document | **PROPOSÉ — À SOUMETTRE À MASTER ET AUX PROPRIÉTAIRES** |
| Classe / priorité | Étude M0 pour MVP P0 ; application installée FEAT-025 proposée Phase 2 P2 |
| Implémentation / vérification | Aucune application produite ; tests applicatifs non exécutés |
| Périmètre | Web mobile, PWA, Flutter, hybride WebView, natif séparé ; parcours du candidat pilote, données locales, permissions, plateformes et recette |
| Limites | Pas de code, dépendance runtime, choix de prestataire, budget, durée de conservation ou calendrier approuvés |

Entrées lues au SHA indiqué : [vision](../product/product-vision.md), [catalogue](../product/feature-catalog.md), [parcours J01–J07](../product/user-journeys.md), [registre](../project-governance/decision-register.md), [gouvernance](../governance.md), [conventions](../repository-conventions.md), [contribution](../../CONTRIBUTING.md) et [stratégie QA](../quality/test-strategy.md). La PR nº 2 est ouverte à la lecture initiale ; cette référence ne désigne pas une fusion dans main.

Réemploi : le cadrage Mobile v0.1 rédigé dans cette discussion le 29 septembre 2026 a fourni les contraintes réseau, uploads, permissions et risques. Ce document en porte la synthèse utile dans GitHub, remappe ses capacités sur les FEAT canoniques et remplace ses classifications provisoires pour cette proposition de dépôt. L'ancien fichier autonome reste un historique de préparation, sans autorité sur le catalogue actuel.

### Preuves et hypothèses

| Affirmation | Nature / preuve | Conséquence |
| --- | --- | --- |
| Mandat documentaire de l'équipe 06 et publication par branche/PR | **CONFIRMÉ** : instruction utilisateur et M0-TEAM-06 | Rédaction et proposition autorisées |
| Flutter/Dart a été demandé comme technologie principale de l'équipe ; Swift/Kotlin autorisés si nécessaires | **CONFIRMÉ comme orientation reçue**, pas comme ADR global approuvé | Flutter est le candidat privilégié du comparatif installé |
| Noyau compte/profil, suivi ou communautés, texte/image, fil chronologique, interactions et sûreté | **PROPOSÉ** : MVP-001 et FEAT-001–022 | Ni inclusion native ni MVP définitif |
| FEAT-025 et FEAT-026 en Phase 2 | **PROPOSÉ** : catalogue GitHub | Pas de promotion automatique au pilote |
| Restrictions OS/stores | **CONFIRMÉ dans le périmètre des sources consultées**, § Sources ; applicabilité au futur build **À VÉRIFIER** | Sources datées, pas de certification de l'app |
| Langues, pays, âge, accessibilité cible, OS minimum, parc réel, besoins d'installation | **À VÉRIFIER** : 01/02/14/15/16/18/19 | Empêche de figer distribution, permissions et engagements |
| OpenAPI approuvée, contrat de session, politique cache, maquettes finales, estimation équipe | **NON REÇU** au SHA d'entrée | Les exigences clientes avancent ; réalisation des lots concernés bloquée |
| Code mobile, binaire, test d'appareil, benchmark, validation store | **NON PRODUIT / NON EXÉCUTÉ** | Aucun PASS fonctionnel |

## Contribution au pilote et comparaison des options

Le livrable indispensable de 06 à M0 est l'avis argumenté sur l'installation, les contraintes des appareils et les critères de recette. Pour un pilote web, 05 produit la surface et 06 contribue à sa recette mobile avec 02/18. Pour une application installée, 06 réalise ensuite les parcours retenus à partir des contrats approuvés. Développer toutes les fonctions citées dans le mandat initial ne constitue pas un prérequis à ce choix.

Les coûts ci-dessous sont des **estimations relatives de complexité**, pour un même noyau texte/image et une équipe dont la capacité est inconnue. Ils ne sont ni devis ni durées mesurées.

| Option | Bénéfice utilisateur | Coût initial / maintenance proposé | Limites et conditions |
| --- | --- | --- | --- |
| A — Web responsive | Accès direct par lien, partage et publication sur téléphone | Faible relatif ; un client web, matrice navigateurs à maintenir | Installation non requise ; capacités OS et arrière-plan dépendantes du navigateur |
| B — PWA progressive sur le web | Retour depuis l'écran d'accueil ; interface hors ligne limitée ; push si supporté et autorisé | Intermédiaire ; service worker, versions de cache, installation et mises à jour à tester | Installation variable ; stockage local évictable ; pas de garantie de transferts persistants ; iOS Web Push conditionné à l'écran d'accueil [S1, S10, S11] |
| C — Flutter iOS/Android | Client installé, adaptations plateforme, intégrations système ciblées | Élevé relatif ; client supplémentaire, builds/signatures et deux matrices OS | Partage de Dart avec adaptations natives ; plugins et API OS restent à maintenir [S12] |
| D — WebView avec pont natif | Réemploi partiel de l'UI web avec certaines capacités installées | Intermédiaire à élevé ; deux environnements et pont à sécuriser | Ajoute packaging et contraintes stores ; une simple copie du site ne garantit pas l'admission App Store [S5] |
| E — Swift et Kotlin séparés | Contrôle spécifique de chaque plateforme | Le plus élevé dans cette hypothèse ; deux implémentations UI | Compétences et maintenance distinctes ; aucun bénéfice suffisant démontré pour le noyau actuel |

**Recommandation proposée :** A pour instruire le pilote ; B par capacité seulement si son utilité est démontrée ; C comme candidat privilégié de FEAT-025 Phase 2, conformément à l'orientation Flutter reçue. D et E restent comparés, sans rejet officiel. Le choix de canal ne change pas les obligations de visibilité, signalement ou suppression.

**Réexamen :** interviews du pilote démontrant une friction d'accès, besoin de capture incompatible avec le web choisi, besoin d'intégration système documenté, comparaison observée du parcours et capacité confirmée d'entretenir deux clients. La présence de concurrents sur stores ne suffit pas à valider une application au MVP.

## Besoin, fonctionnalités et parcours

Les phases sont **PROPOSÉES** et reprennent le catalogue. Une capacité métier MVP utilisée sur mobile web ne rend pas FEAT-025 native MVP. Les exigences ci-après s'appliquent aux surfaces effectivement retenues.

| FEAT | Besoin / acteurs / résultat | Phase / priorité | Préconditions et parcours nominal | États, limites et acceptation liée |
| --- | --- | --- | --- | --- |
| FEAT-001, FEAT-002 | Visiteur/membre : créer, récupérer et reprendre un accès | MVP P0 | J01 ; identité/âge/activation approuvés ; formulaire → activation → session → accueil | Invalide, expiré, suspendu, révoqué ; AC-J01-01–04 et TEST-0601/0602 |
| FEAT-003, FEAT-004 | Titulaire : afficher son profil et comprendre sa visibilité | MVP P0 | Profil accessible → édition autorisée → confirmation serveur | Champs privés exclus, autre compte refusé, changement concurrent ; TEST-0603/0607 |
| FEAT-005, FEAT-008 | Lecteur : suivre et lire chronologiquement | MVP P0 | J03 ; ordre/départage/cursor définis → profil → suivi → fil → page suivante | Fil vide, fin, refresh, retrait concurrent, réseau coupé ; TEST-0604/0605 |
| FEAT-006, FEAT-007 | Auteur : publier texte/image avec audience et texte alternatif | MVP P0 | J02 ; audience/limites/pipeline approuvés → sélectionner → prévisualiser → envoyer → état serveur | Annulation du picker, droit révoqué, média distant non téléchargé, traitement refusé, résultat incertain ; TEST-0606/0608/0609 |
| FEAT-009, FEAT-010 | Membre autorisé : réagir/commenter puis retirer selon règles | MVP P1 | Ressource autorisée → action → en attente → confirmation | Double appui, timeout, conflit, contenu retiré ; TEST-0610 |
| FEAT-011, FEAT-022 | Destinataire : voir l'information essentielle et maîtriser son attention | MVP P1 | Boîte in-app et catégories définies ; ouvrir, marquer lu, régler ; reprise du fil | Push facultatif, permission refusée, destination retirée ; TEST-0611/0612 |
| FEAT-012, FEAT-013 | Membre : bloquer et signaler | MVP P0 | J04 ; effet blocage/categories définis → expliquer → soumettre → accusé | Protection locale en attente distincte d'un blocage serveur confirmé ; TEST-0613/0614 |
| FEAT-014, FEAT-015 | Personne concernée : lire une décision et contester | MVP P0 | J05 ; accès au motif autorisé → recours → référence/état | Délai/éligibilité de recours définis par 09/15 ; opérateurs via FEAT-017 hors client membre ; TEST-0615 |
| FEAT-016 | Titulaire : exporter ou demander suppression | MVP P0 | J06 ; réauthentification et cycle approuvés → demande → suivi → accès contrôlé | Export expiré, demande déjà reçue, suspension ; pas de promesse d'effacement instantané ; TEST-0616 |
| FEAT-018, FEAT-021 | Visiteur/membre : parcours lisible et accessible sur téléphone | MVP P0 | Langues et support décidés ; focus, grossissement et lecteur d'écran | Petit écran, clavier virtuel, date/fuseau, texte long ; TEST-0617/0618 |
| FEAT-019 | Exploitation : comprendre échecs réseau et qualité sans contenu privé | MVP P1 | Événements, consentement et rétention examinés par 13/14/15 | Pas de token ni texte utilisateur dans les logs ; TEST-0619 |
| FEAT-020 | Membre : rejoindre et utiliser une communauté | MVP P1, inclusion à arbitrer | J07 ; types/adhésion/rôles approuvés → règles → adhésion → contenu | En attente, exclusion, fermeture, retrait de rôle ; TEST-0620 |
| FEAT-023, FEAT-024, FEAT-025, FEAT-026 | Recherche, messages, app installée, vidéo | Phase 2 P1/P2 selon catalogue | Contrats et sûreté propres avant réalisation ; M0 examine seulement les interfaces structurantes | FEAT-025 ne nécessite pas d'inclure FEAT-024/026 à sa sortie |
| FEAT-027, FEAT-028 | Créateurs et organisations | Phase 2 P2 | Droits d'équipes et mesures définis par propriétaires | Pas de tableau financier ou permission implicite dans le client |
| FEAT-029, FEAT-030, FEAT-031 | Recommandation, publicité et rémunération | Phase 3 P2 | 07/11/12/15 instruisent contrôle, données et règles par marché | Aucune collecte publicitaire, suivi tiers ni achat ajouté à M0 |
| FEAT-032 | Utilisateur d'une nouvelle région/langue | International P1 | 16/15 valident locale, distribution et support | Préparation des ressources localisées dès MVP ; pas de lancement multi-pays implicite |
| FEAT-033, FEAT-034 | Live à grande audience et intégrations avancées | Long terme P3 | Modération, charge, scopes et révocation instruits | Hors réalisation M0 |

**Capacités du brief non identifiées dans le catalogue :** Hub, stories, événements et AR. Proposition de classement à soumettre à 01 : Hub/événements/stories Phase 2 P2 ; AR Long terme P3. Elles ne reçoivent pas de nouveaux FEAT ici. Sans besoin pilote prouvé, elles n'imposent ni onglet, ni permission, ni traitement de fond.

### États et transitions communs

| Situation / déclencheur | Précondition et transition proposée | Affichage, récupération et log |
| --- | --- | --- |
| Ouverture/reprise de l'app | Session inconnue → vérification → autorisée ou connexion requise | Ne pas montrer le cache d'un autre compte pendant la vérification ; correlation ID si requête |
| Requête de lecture | Initial/vide → chargement → résultat/fin/erreur | Réessai explicite ; annuler requête devenue inutile ; message localisé et code technique filtré |
| Mutation | Prêt → envoi → confirmé, refusé ou résultat inconnu | Un timeout n'est pas un refus du serveur : réconcilier par identifiant d'opération avant resoumission |
| Mise en arrière-plan | Suspendre lecteur/caméra/travail non indispensable ; enregistrer uniquement l'état local autorisé | Aucun envoi silencieux ajouté ; à la reprise relire session, droits et opération en cours |
| Annulation | Annuler un picker ne crée rien ; annuler un upload demande arrêt puis réconciliation | L'annulation locale ne prouve pas le retrait d'une publication déjà confirmée |
| Perte de droits / contenu retiré | Invalider le contenu concerné, l'aperçu et les actions ; relecture contrôlée | « Contenu indisponible » sans expliquer une ressource privée à un tiers |
| Compte suspendu | Bloquer les écritures ordinaires selon contrat | Conserver seulement les parcours autorisés de recours/privacy ; l'étendue appartient à 09/14/15 |
| Déconnexion/changement de compte | Retirer l'affichage privé et séparer l'espace local ; révoquer la session selon contrat | Hors réseau, fermeture locale immédiate ; révocation distante en attente signalée, aucun succès distant inventé |
| Erreur de stockage | Mémoire/disque indisponible ou quota atteint | Continuer en mode sans persistance si possible ; prévenir avant perte d'un brouillon |

Ces noms décrivent des états UI candidats ; ils ne créent pas les enums métier du backend. Le couple statut HTTP/code métier sera arrêté par 04.

### Erreurs et reprise attendues de 04

| Catégorie candidate | Réaction du client | Reprise / journalisation |
| --- | --- | --- |
| Validation, fichier refusé, quota métier | Erreur liée au champ/fichier ; conserver uniquement la saisie admissible | Pas de retry automatique ; code sûr, taille agrégée si autorisée |
| Session expirée/révoquée | Suspendre écritures ; renouvellement unique si le contrat le permet | Ne pas boucler sur refresh ; rejeu d'une mutation seulement avec contrat d'idempotence |
| Action interdite ou ressource absente/masquée | Retirer actions et contenu incompatible | Revalidation ; aucun contournement par URL profonde ou ancien cache |
| Conflit de version | Recharger l'état ; proposer réapplication explicite | Ne pas écraser une édition plus récente |
| Limite de débit | Expliquer attente ; respecter délai serveur s'il est fourni | Retries bornés avec délai variable, aucun polling agressif |
| Serveur/réseau indisponible | Afficher indisponibilité et état exact du brouillon/upload | Lecture rejouable ; mutation réconciliée ; request_id sans payload sensible |

## Permissions, données et contrats

### Permissions métier candidates — à revoir par 09/14/15

| Acteur | Action / ressource / portée | Autorisation et refus attendus |
| --- | --- | --- |
| Anonyme | Lecture des profils/posts déclarés publics | Seulement champs et médias autorisés ; publication/exports refusés |
| Membre actif | Lire/interagir sur ressource admissible | Audience, blocage et statut contrôlés à chaque API ; cache/UI ne font pas autorité |
| Propriétaire | Éditer/retirer son profil/contenu ; demander export/suppression | Propriété et réauthentification sensible côté serveur ; concurrence contrôlée |
| Autre utilisateur | Consulter, signaler si autorisé | Aucun pouvoir d'édition, accès export ou preuve privée du signalant |
| Compte bloqué / suspendu | Lecture/actions selon matrice des propriétaires | Le mobile ne définit pas l'étendue du blocage ni les exceptions de suspension |
| Rôle communautaire | Action dans sa communauté si FEAT-020 approuvé | Aucun privilège global implicite ; rôle retiré invalide les actions |
| Opérateur interne | Traitement des dossiers | Client membre sans pouvoir admin ; FEAT-017 détenu par 10, accès et audit séparés |

### Permissions du téléphone — proposition de minimisation

| Capacité | Web/PWA | iOS installé | Android installé | Moment et alternative en cas de refus |
| --- | --- | --- | --- | --- |
| Choisir une image | Sélecteur de fichier ; comportement de capture à tester | Picker système ; accès complet Photos inutile pour la simple sélection [S2] | Photo Picker limité aux éléments choisis ; fallback document si absent [S3] | Action « Ajouter une image » ; annulation garde le texte ; aucune demande au lancement |
| Capture photo directe | getUserMedia exige contexte sécurisé et autorisation [S13] | Caméra si capture native retenue | Caméra si capture intégrée retenue ; délégation système à distinguer | À la capture ; sélectionner un fichier existant reste possible |
| Microphone | Uniquement si futur enregistrement audio/vidéo l'exige | Idem | Idem | Aucun besoin pour le pilote texte/image ; permission reportée |
| Push | Détection de capacité, permission ; iOS écran d'accueil [S1] | Contrat notifications OS à valider sur parc cible | Permission POST_NOTIFICATIONS pour notifications non exemptées sur Android 13+ [S4] | Activation volontaire ; inbox in-app disponible si refus |
| Contacts, localisation, Bluetooth, accès global fichiers | Aucun besoin établi | Aucun besoin établi | Aucun besoin établi | Ne pas les demander pour suivre, publier ou participer au pilote |
| Suivi publicitaire | Hors noyau M0 | Choix futur par 11/15 | Choix futur par 11/15 | Ne pas ajouter de SDK ni identifiant publicitaire au cadrage pilote |

L'autorisation système ne remplace ni la base de traitement, ni le consentement requis pour un usage distinct. Refus permanent, permission limitée, révocation depuis Réglages, fichier cloud indisponible et retrait de l'accès à une URI font partie de la recette. Pas d'insistance répétée ni de blocage général du compte pour un refus de caméra/push.

### Données et cycle de vie local — proposition, durées non arrêtées

| Catégorie / origine / minimum | Finalité et visibilité | Stockage/accès proposés | Modification, conservation, export et suppression |
| --- | --- | --- | --- |
| Session émise par 04 : références/credentials nécessaires au client | Accès du seul titulaire | Web selon contrat de session sécurisé ; installé stockage OS adapté, revue 14 ; aucun secret dans logs | Rotation/révocation ; purge à déconnexion ; politique de backup et restauration à définir ; aucun secret de session dans l'export |
| Profil et préférences venant de 04 | Affichage du compte actif | Cache séparé par compte ; accès interne local nul hors support autorisé | Relecture après édition ; durée à 15 ; purge changement de compte ; export métier côté serveur |
| Posts/médias servis par 04/08 | Lecture de l'audience autorisée | **MVP proposé : pas de persistance hors ligne de contenus privés** ; cache public borné, politique 15 ; service worker exclut réponses sensibles | Retrait observé → purge locale ; limite : aucun retrait immédiat garanti sur un appareil déconnecté ; pas de promesse de recall d'une copie déjà reçue |
| Brouillon saisi et image choisie | Préparation volontaire d'une publication | Mémoire par défaut ; persistance seulement après politique approuvée et choix explicite ; pas de synchronisation cloud implicite | Effacer sur abandon/déconnexion selon choix expliqué ; après confirmation purge des temporaires ; perte possible si mémoire seule |
| Opération d'upload : ID, étapes, octets, référence locale | Réconcilier reprise/annulation sans doublon | État minimal ; URL signée éphémère jamais en log ; accès accordé au fichier limité au besoin | Expiration/abandon → nettoyage coordonné avec 08 ; confirmation validée auprès de 04 ; durée et backup à décider |
| Abonnement push/token et préférences | Acheminer un avis à un appareil du titulaire | Référence côté backend ; payload minimal ; fournisseur et SDK non sélectionnés | Révoquer association à déconnexion/changement de compte ; rotation ; supprimer les notifications locales concernées ; livraison/affichage non garantis |
| Signalement, recours, export | Transmettre une demande protégée | Pas de preuve privée ni archive export en cache général ; fichier export explicite au choix utilisateur | Serveur propriétaire du dossier ; rétention/backup/accès opérateur par 09/10/15 ; téléchargement déjà exporté hors contrôle de purge de l'app |
| Diagnostic technique minimisé | Mesurer erreur, réseau, temps de rendu et version | Événements approuvés 13/14/15 ; accès opérateurs habilités | Sans contenu, URL signée, token, capture d'écran ni device fingerprint ; consentement/rétention/effacement à définir |

**Limite de sécurité à arbitrer :** un appareil hors ligne ne reçoit pas une révocation récente. Une stratégie « afficher tout le cache privé puis vérifier » pourrait exposer un contenu retiré. Proposition pour M0 : cache privé persistant désactivé, révalidation avant réaffichage sensible à la reprise, durée de fraîcheur en mémoire à examiner par 14/15. Cela ne garantit pas l'effacement de copies ou captures déjà faites.

### Interfaces candidates producteur → consommateur

Ce sont des fiches de besoins du client, pas des endpoints nouvellement imposés. IDs provisoires d'interface ci-dessous à relier aux contrats de 04 ; aucune version filaire approuvée. Champs conceptuels, données synthétiques uniquement.

**Enveloppe commune proposée :** authentification/autorisation côté service ; identifiants opaques ; schema version et fenêtre de compatibilité d'anciens clients ; `request_id` de corrélation et détail d'erreur sûr. Timeout par opération, limites de taille, fenêtre de retry, portée/durée de déduplication et règles d'expiration doivent être chiffrés par 03/04/08/14 avant implémentation. Aucun délai n'est inventé comme contrat acquis.

| Référence candidate / FEAT | Producteur → consommateur ; requête/réponse conceptuelle | Validations, erreurs et comportement client |
| --- | --- | --- |
| Session-client / FEAT-001–002 | 04 → 05/06 ; preuve d'auth selon méthode retenue → compte/session/échéance autorisés | Révocation, récupération, admissibilité ; refresh concurrent mutualisé ; aucun rejeu aveugle après erreur |
| Feed-client / FEAT-004/005/008 | 04 → 05/06 ; curseur/limite bornée → items autorisés/prochain curseur/fin | Ordre et départage stables ; invalidation blocage/suppression ; lecture annulable et répétable, déduplication d'items |
| Publication-client / FEAT-006–010 | 04 → 05/06 ; texte/audience/media ID/clé d'opération/version attendue → ID/état/version | Taille et type ; résultat inconnu après timeout ; même opération rejouée sans doublon ; changement de payload détecté ; réconciliation et conflit d'édition |
| Upload-client / FEAT-007/026 | 04/08 → 05/06 ; metadata déclarée → autorisation/session upload ; completion → état de traitement | Serveur valide fichier réel/audience/quotas ; URL expirée, accès local perdu, checksum attendu si retenu ; reprise par parties seulement si support contractuel |
| Notification-client / FEAT-011/025 | 04 → 05/06 ; préférences/abonnement → état/version ; signal → ID de destination minimal | Enregistrement/révocation lié au compte ; lire l'objet via API avec droits actuels ; doublons et délai de livraison tolérés ; pas de contenu privé dans aperçu par défaut proposé |
| Safety-client / FEAT-012–015 | 04/09/10 → 05/06 ; cible/motif minimal/opération → dossier/état/accusé | Signalant protégé ; compte/cible supprimés, suspension et demande répétée contractualisés ; UI n'annonce réception qu'après accusé |
| Privacy-client / FEAT-016 | 04/15 → 05/06 ; demande vérifiée → état et accès export limité | Réauthentification, lien expiré, demande déjà reçue ; perte de session après suppression ; aucune archive dans le cache applicatif |

Aucun WebSocket n'est requis par le noyau proposé. Si adopté plus tard, 04/03 définissent auth, expiration, reprise/ordre et charge ; les signaux ne dispensent pas d'une relecture autorisée. Les transitions locales optimistes sont réconciliées avec la réponse serveur.

## Contraintes iOS / Android, accessibilité et distribution

### Réseau, performance et anciens appareils

Propositions clientes : images adaptées à la taille rendue ; pagination et cache bornés ; annulation des chargements hors écran ; aucune vidéo autochargée au pilote texte/image ; pas de polling ni réveil périodique sans besoin démontré. En Phase 2, un lecteur vidéo actif, pause hors écran/arrière-plan, préchargement limité et commande d'économie de données sont à instruire avec 08. Une optimisation n'est pas déclarée efficace avant mesure.

Le retour d'une connectivité apparente n'est pas une preuve d'accès API : traiter captive portal, lenteur, perte partielle, serveur indisponible et Wi-Fi vers mobile. Une action sensible hors ligne reste non envoyée. L'app doit distinguer brouillon récupérable, envoi suspendu et résultat inconnu.

Les tâches Android doivent supporter interruption et report ; le choix entre WorkManager et transfert initié par utilisateur dépend du scénario [S8]. Sur iOS, la configuration URLSession de fond ne constitue pas une autorisation d'exécuter indéfiniment l'app [S9]. **M0 ne promet pas d'upload ininterrompu en arrière-plan** ; reprise/reconciliation à l'ouverture exigée du futur contrat.

Matrice QA proposée, sans inventer d'OS minimum : un iPhone au minimum supporté à décider, un iPhone récent, un Android à RAM limitée au minimum retenu, un Android récent ; navigateur et mode PWA installée distincts. Pour chaque parcours mesurer temps jusqu'au résultat utile, mémoire maximale, octets transférés, erreurs/reprises, frames manquées et énergie avec outils adaptés. Protocole candidat : froid/chaud, réseau normal puis profil contrôlé 400 kbit/s descendant, 200 kbit/s montant, 400 ms RTT et 1 % perte, coupure franche puis reprise, arrière-plan et processus arrêté. Ces valeurs sont des paramètres de test proposés, ni description du marché ni SLO. Répétitions, seuils p95, taille média et budgets seront arrêtés avec 18/14 sur ce parc.

### Accessibilité et localisation

Mêmes objectifs sur les surfaces : ordre de lecture cohérent, libellés annoncés, focus restauré après modale/picker, actions possibles sans gestes exclusifs, grossissement sans perte d'action, clavier virtuel ne masquant pas l'envoi, chargement/erreur/confirmation annoncés sans interruption excessive. Recette proposée avec VoiceOver iOS et TalkBack Android et clavier sur le web ; aucun résultat acquis. Contrastes, tailles tactiles et seuils relèvent de 02/18.

FEAT-021 impose les langues du pilote après choix de 16. Préparer ressources externes, pluralisation, texte long, noms et contenus multilingues, horodatage/fuseau distincts. Tester RTL si une langue RTL est retenue ; ne pas déduire langue ou nationalité de la localisation du téléphone.

### Publication sur stores — condition de la surface installée

| Sujet | Constat officiel daté | Conséquence projet / propriétaire |
| --- | --- | --- |
| Contenu utilisateur | Apple exige notamment mécanismes de filtrage, signalement, blocage et contact ; Google demande modération continue, signalement/blocage et règles UGC [S5, S6] | 09/10/15 fournissent traitement opérationnel, interface et contact ; simple bouton sans traitement insuffisant |
| Suppression de compte | Apple demande une suppression dans l'app si elle permet création de compte ; Google demande aussi une ressource web pour solliciter la suppression [S5, S7] | FEAT-016 et J06 concernent la sortie installée ; 04/05/15 alignent états, demandes et exceptions |
| Simple encapsulation | Le critère Apple 4.2 demande une utilité dépassant un site simplement reconditionné [S5] | Option D soumise à évaluation ; aucune promesse d'acceptation automatique |
| Versions, pays, déclarations et signatures | Dossier de publication propre au futur build **NON REÇU** | 14/15/16/18/20 doivent fixer SDK/target, comptes/signatures, tests de distribution, fiches de données, politique de confidentialité et pays avant soumission |

Les règles boutiques sont des contraintes de distribution, pas une validation juridique du service. Revérifier sources et applicabilité au build au moment de la publication. Les frais, exigences SDK courantes, règles de paiement et distribution alternative sont volontairement hors décision M0 ; aucune valeur non vérifiée n'est retenue.

## Acceptation et vérification

Critères spécialisés proposés : les TEST-0601–0622 sont réservations **locales à cette proposition**, à confirmer par 17/18 lors de l'intégration. Réemploi des FEAT et AC-J existants ; aucun nouveau FEAT pour le même besoin. Tous sont **PLANNED**, ni prêts à exécuter ni PASS. Les contrats ouverts et l'absence de client empêchent l'exécution applicative.

| Test ID / type | FEAT et critères d'entrée | Scénario observable | Statut / dépendance |
| --- | --- | --- | --- |
| TEST-0601 / E2E | FEAT-001/002 ; AC-J01-01/02 | Activation valide → un compte ; activation expirée → refus et reprise compréhensible | PLANNED ; 01/04/14/15 |
| TEST-0602 / API+client | FEAT-002 ; AC-J01-03 | Session révoquée puis reprise app → action protégée refusée, aucune boucle de refresh | PLANNED ; session 04/14 |
| TEST-0603 / privacy | FEAT-003/004 | Changement de compte pendant chargement → aucune donnée du précédent rendue ou cachée pour le suivant | PLANNED ; 04/14/15 |
| TEST-0604 / concurrence | FEAT-008 ; AC-J03-01 | Nouvelles publications entre pages → ordre contractuel, absence de doublons, fin explicite | PLANNED ; ordre/cursor 04 |
| TEST-0605 / réseau | FEAT-008/018 | Fil vide ou coupure pendant page suivante → contenu autorisé stable, erreur et réessai accessibles | PLANNED ; 02/04 |
| TEST-0606 / appareil | FEAT-007 | Annuler/refuser sélecteur ou fichier cloud inaccessible → texte conservé, aucune publication créée | PLANNED ; 02/08 |
| TEST-0607 / permissions | FEAT-004/012 ; AC-J02-04/05 | Changement d'audience/retrait avant accès direct → média/détail refusés ; reprise privée attend validation | PLANNED ; 04/08/14/15 |
| TEST-0608 / upload | FEAT-007 ; AC-J02-02 | Fichier invalide, espace insuffisant ou traitement rejeté → échec distinct de « publié », temporaires nettoyés | PLANNED ; 08/15 |
| TEST-0609 / idempotence | FEAT-006/007 ; AC-J02-03 | Serveur accepte mais réponse perdue → reprise même opération, une publication ; annulation concurrente réconciliée | PLANNED ; 04/08 |
| TEST-0610 / API+client | FEAT-009/010 ; AC-J03-02/03 | Double appui/retry puis contenu retiré → aucun doublon et refus sans écriture non autorisée | PLANNED ; 04/09 |
| TEST-0611 / appareil | FEAT-011/025 ; AC-J03-05 | Refus push ou capacité absente → noyau et inbox restent utilisables ; pas de sollicitation en boucle | PLANNED ; 01/02/04 |
| TEST-0612 / privacy | FEAT-011/025 | Notification ancienne ouverte après blocage/changement de compte → destination recontrôlée, aucun contenu privé exposé | PLANNED ; 04/14/15 |
| TEST-0613 / API+client | FEAT-012 ; AC-J04-01 | Blocage confirmé → retrait du contenu concerné ; blocage hors ligne → protection locale indiquée, attente serveur | PLANNED ; 09/04 |
| TEST-0614 / API+client | FEAT-013 ; AC-J04-02/03/04 | Signalement interrompu puis repris → pas de faux accusé ni fuite du signalant ; cible supprimée traitée selon contrat | PLANNED ; 09/10/15 |
| TEST-0615 / E2E | FEAT-014/015 ; AC-J05-04 | Compte suspendu autorisé à faire recours → seulement les opérations prévues, suivi de sa propre demande | PLANNED ; 09/14/15 |
| TEST-0616 / E2E+API | FEAT-016 ; AC-J06-01/02/03 | Demande vérifiée → état exact ; autre compte/export expiré refusé ; purge locale selon cycle approuvé | PLANNED ; 04/15 |
| TEST-0617 / accessibilité | FEAT-018/025 ; AC-J03-04 | Parcours création/signalement avec lecteur d'écran, texte agrandi, petit écran/clavier → toutes actions accessibles | PLANNED ; 02/18 |
| TEST-0618 / localisation | FEAT-021/032 | Langue retenue, texte long et fuseau différent → labels/erreurs/date cohérents ; RTL si applicable | PLANNED ; 16/02 |
| TEST-0619 / inspection | FEAT-019 | Erreurs d'auth/upload/recours → logs sans secrets, URL signée, payload privé ni empreinte appareil | PLANNED ; 13/14/15 |
| TEST-0620 / permissions | FEAT-020 ; AC-J07-01/03 | Exclusion/rôle retiré → purge et refus d'action au retour ; aucun privilège global | PLANNED ; arbitrage 01/09/04 |
| TEST-0621 / PWA | FEAT-018/025 | Mise à jour, stockage évicté et ancien cache → interface reprend sans données d'autre compte ni écriture hors ligne silencieuse | PLANNED ; option B, 05/14/15 |
| TEST-0622 / performance | FEAT-007/008/025/026 | Protocole réseau/appareils ci-dessus → mesures reproductibles et comparaison aux budgets approuvés | PLANNED ; 08/14/18 |

**Vérification documentaire à l'intégration :** validateur du dépôt, tests existants de ce validateur, espaces, liens locaux et références FEAT/AC-J. Commandes, environnement, SHA publiés et résultat réel sont consignés dans la PR ; cette exigence ne transforme pas les lignes PLANNED en résultats exécutés.

## Décision structurante proposée au HQ

**DEC-0601 — Surface mobile du pilote**, identifiant proposé non trouvé dans le corpus d'entrée, à confirmer par 00/17. Statut **PROPOSÉ**. Autorité : MASTER avec 01/03 et avis 02/05/06/08/14/15/18/19/20. Liée à OUV-002, INT-0003 et FEAT-018/025 ; aucun ADR de stack approuvé par ce document.

| Champ | Proposition |
| --- | --- |
| Objectif | Rendre le noyau pilote utilisable sur téléphone avec une charge de maintenance soutenable |
| Problème | Besoin d'installation, capacité équipe et budgets non établis ; risque de réaliser deux clients sans avantage mesuré |
| Solution candidate | A web responsive d'abord ; B examiné capacité par capacité ; C Flutter Phase 2 sauf preuve justifiant un changement |
| Alternatives | B complète, C dès MVP, D WebView, E natif séparé ; **aucune rejetée officiellement** ; complexité et limites au comparatif |
| Dépendances | Périmètre 01, parcours 02, contrats 04, media 08, sécurité/privacy 14/15, données pilote 19 et estimation 20 |
| Risques | Qualité mobile web insuffisante, installation PWA peu adoptée, dette de cache, délai natif et store ; mesures via pilote et recette |
| Impact business | Coût et délai relatifs à estimer ; aucun taux d'adoption ni revenu prédit |
| Impact technique | Surface à maintenir, cycle de versions API, stockage local, distribution et QA ; ne préjuge pas du backend |
| Priorité / phase | P0 pour l'arbitrage M0 ; FEAT-025 Phase 2 P2 proposée |
| Preuve attendue / réexamen | Besoin pilote documenté, estimation par option, résultat comparatif UX/réseau, budget et responsables ; revoir si besoin natif démontré |
| Delta après approbation | 00 inscrit décision ; 01 met à jour FEAT-018/025 ; 02 adapte navigation ; 05/06/18/20 reçoivent un delta ciblé |

### Contradictions et corrections de trajectoire

1. Le cadrage mobile autonome présentait Flutter comme base de travail et comparait seulement web/natif. Le mandat GitHub exige aussi PWA et hybride et réserve l'adoption globale de stack : le présent comparatif le respecte. Orientation reçue et adoption globale sont désormais distinctes.
2. Les anciens brouillons locaux Produit/UX/Backend divergeaient sur vidéo, messages et communautés. Le catalogue GitHub fixe une **proposition commune** : FEAT-024/025/026 Phase 2 ; FEAT-020 MVP conditionnel. Il sert à ce livrable, sans prétendre que MASTER a clos l'arbitrage.
3. Le cadrage autonome rangeait certains éléments en Post-MVP et le live en Phase 3. Ici les cinq classes demandées sont appliquées ; FEAT-033 est Long terme, conformément au catalogue. Aucune modification du catalogue n'est proposée sur ce point.
4. La proposition antérieure de lire du contenu privé « récemment autorisé » hors ligne était insuffisamment précise sur la révocation. La politique restrictive du tableau des données est **soumise à 14/15**, pas déclarée validée.
5. Hub, stories, événements et AR n'ont pas de FEAT à la référence lue. Demander à 01 une classification ciblée avant de fixer leurs routes ; les parties indépendantes du pilote restent documentées.

## Dépendances, risques et transmission

Identifiants INT-0601–0610 et RISK-0601–0605 proposés pour cette contribution ; absence de collision vérifiée contre le SHA d'entrée, allocation globale à confirmer par 00/17. Correspondance avec les anciennes demandes locales conservée dans la colonne Delta.

| ID / émetteur → destinataire | Question et livrable attendu | Delta / blocage | État |
| --- | --- | --- | --- |
| INT-0601 / 06 → 00/01/03 | Arbitrer DEC-0601, suivi ou communautés, fonctions exclues et signal de réexamen | Ex-MOB-M0-01 ; lié INT-0001/0003 ; bloque engagement natif, pas rédaction | À TRANSMETTRE |
| INT-0602 / 06 → 02/05 | Navigation du noyau, comparaison web/PWA, états OS, écran vide, erreurs, focus | Ex-MOB-M0-02/08 ; bloque UI finale, pas comparatif | À TRANSMETTRE |
| INT-0603 / 06 → 03/04 | Session mobile, API versionnée, curseurs, retries/idempotence, anciens clients, invalidation et erreurs | Ex-MOB-M0-03 ; bloque client connecté | À TRANSMETTRE |
| INT-0604 / 06 → 14/15 | Avis ciblé sur cache privé hors ligne, séparation comptes, backup, purge, réauth et notifications | Ex-MOB-M0-04 ; bloque stockage sensible/push | À TRANSMETTRE |
| INT-0605 / 06 → 08/04 | Types/limites/états média, annulation, résultat incertain et reprise d'upload ; politique de métadonnées | Ex-MOB-M0-06 ; bloque publication image ; vidéo indépendante reportée | À TRANSMETTRE |
| INT-0606 / 06 → 09/10/15 | Effet précis du blocage, accusé et recours du compte suspendu ; exigences stores UGC | Ex-MOB-M0-05 ; bloque ouverture publique sûre | À TRANSMETTRE |
| INT-0607 / 06 → 16/19/01 | Langues/écritures/pays et appareils réels du pilote ; preuve du besoin installé | Complète ancienne question pilote ; bloque support annoncé | À TRANSMETTRE |
| INT-0608 / 06 → 18/14/20 | Parc minimum, protocole réseau, budgets et estimation A–E ; préparation signatures/stores si retenus | Ex-MOB-M0-07 ; bloque promesse de performance/date, pas analyse | À TRANSMETTRE |
| INT-0609 / 06 → 17/21/00 | Intégrer le chemin propriétaire, contrôler réservations d'IDs et revue du delta de PR | État de réception à renseigner par HQ sur preuve ; non bloquant rédaction | À TRANSMETTRE |
| INT-0610 / 06 → 01 | Rattacher Hub/stories/événements/AR au catalogue ou confirmer report | Aucun FEAT parallèle créé ; bloque seulement ces extensions | À TRANSMETTRE |

Publication GitHub et envoi à une discussion sont deux faits distincts. Le [tableau de coordination](../project-governance/coordination-board.md) appartient à HQ ; la PR présente une réponse de 06 à examiner et n'atteste pas la réception d'autres équipes. Les demandes ci-dessus restent À TRANSMETTRE tant que leur envoi réel n'est pas prouvé.

| ID | Risque, impact et statut | Propriétaire / mesure proposée |
| --- | --- | --- |
| RISK-0601 | Double client prématuré, coût/délai élevés ; **OPEN**, probabilité non mesurée | 00/01/20 ; DEC-0601 et estimation comparative ; ex-MOB-R01 |
| RISK-0602 | Fuite via cache, preview push ou compte précédent ; **OPEN**, impact critique potentiel | 14/15/04/06 ; contrat de cycle local, revalidation et TEST-0603/0607/0612 ; ex-MOB-R03 |
| RISK-0603 | Upload doublé/perdu après interruption ; **OPEN**, impact élevé | 04/08/06 ; réconciliation/idempotence/annulation, TEST-0609 ; ex-MOB-R04 |
| RISK-0604 | Batterie/réseau/mémoire et OS non représentatifs ; **OPEN**, impact élevé | 18/14/06 ; parc réel, budgets approuvés et TEST-0622 ; ex-MOB-R05 |
| RISK-0605 | Différences PWA/stores ou navigation de fonctions absentes ; **OPEN**, impact élevé | 02/05/06/09/15 ; détection capacités, variante UX, revue UGC/suppression et exigences courantes ; inclut ex-MOB-R02 |

## Sources officielles et datation

Consultation le **29 septembre 2026**. Date d'édition indiquée seulement lorsqu'elle est connue. Les pages évolutives sont à revérifier avant implementation/publication ; ces constats ne remplacent pas les tests des OS/navigateurs effectivement supportés. Les implications et recommandations du document sont les inférences de l'équipe 06.

| Réf. | Source officielle | Constat utilisé / portée |
| --- | --- | --- |
| S1 | [WebKit — Web Push iOS/iPadOS](https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/) ; 16 février 2023 | Support à partir d'iOS/iPadOS 16.4 pour web apps ajoutées à l'écran d'accueil ; permission en réponse à une interaction ; conditions à tester sur cible |
| S2 | [Apple — Meet the new Photos picker, WWDC20](https://developer.apple.com/videos/play/wwdc2020/10652/) ; 2020 | Sélection système d'éléments sans autorisation générale de bibliothèque ; ne prouve pas la conformité d'un plugin Flutter |
| S3 | [Android — Photo picker](https://developer.android.com/training/data-storage/shared/photo-picker) ; mise à jour affichée 16 septembre 2026 | Accès choisi, disponibilité à détecter, fallback document ; accès URI à gérer sur longue opération |
| S4 | [Android — Notification runtime permission](https://developer.android.com/develop/ui/compose/notifications/notification-permission) ; page évolutive | POST_NOTIFICATIONS à partir d'Android 13 pour notifications non exemptées ; refus à prendre en charge |
| S5 | [Apple — App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) ; page évolutive | §1.2 UGC, §4.2 utilité d'une app installée, §5.1.1(v) suppression du compte |
| S6 | [Google Play — User Generated Content](https://support.google.com/googleplay/android-developer/answer/9876937) ; page évolutive | Règles acceptées, modération, signalement et blocage pour réseau social |
| S7 | [Google Play — Account deletion requirements](https://support.google.com/googleplay/android-developer/answer/13327111) ; page évolutive | Parcours de demande dans l'app et ressource web si création de compte ; exceptions/rétentions à expliquer |
| S8 | [Android — Data transfer background task options](https://developer.android.com/develop/background-work/background-tasks/data-transfer-options) ; page évolutive | Transfert initié utilisateur distinct du travail reportable ; annulation/retry et contraintes OS à gérer |
| S9 | [Apple — URLSession background configuration](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/background%28withidentifier%3A%29) ; page évolutive | Configuration de transferts de fond ; détails complets d'implémentation à revérifier, aucun SLA déduit |
| S10 | [Google web.dev — Offline data](https://web.dev/learn/pwa/offline-data) ; page évolutive | Stockage local et gestion des données offline ; ce n'est pas une source d'autorisation métier |
| S11 | [Google web.dev — PWA installation](https://web.dev/learn/pwa/installation) ; page évolutive | Installation et comportement variables selon plateforme ; ne pas confondre installabilité et compatibilité fonctionnelle |
| S12 | [Flutter — Platform channels](https://docs.flutter.dev/platform-integration/platform-channels) ; page évolutive | Interfaces Dart vers code plateforme ; choix de plugins/versions non effectué |
| S13 | [W3C — Media Capture and Streams](https://www.w3.org/TR/mediacapture-streams/) ; spécification évolutive | Capture exposée en contexte sécurisé avec contrôle d'autorisation ; compatibilité à tester |

## Compte rendu de cette étape

1. **Décisions prises / à valider :** publication d'un comparatif spécialisé suivant M0-TEAM-06 ; DEC-0601 et politique locale soumis à leurs propriétaires. Aucun code ni choix de stack globale validé.
2. **Livrable :** ce document v0.1, indexé depuis le README, fondé sur le SHA d'entrée indiqué. La PR de contribution porte les références de publication effectives.
3. **Vérifications :** contrôles documentaires et tests du validateur à consigner dans la PR avec environnement et commit ; aucun test applicatif exécuté ; TEST-0601–0622 restent PLANNED.
4. **Questions :** nécessité installée au pilote, capacité maintenance, cache privé, contrats session/upload, pays/langues/OS minimum et prise en charge des capacités non cataloguées.
5. **Dépendances :** INT-0601–0610, toutes À TRANSMETTRE, réponses spécialisées NON REÇUES pour ces demandes.
6. **Risques :** RISK-0601–0605 ouverts ; comparaison qualitative, aucune performance ou acceptation store démontrée.
7. **Suite / HQ :** revue ciblée 01/02/03/05 sur canal ; 04/08 sur interfaces ; 14/15 sur cache/permissions ; 18 sur protocole ; 17/21 sur intégration. MASTER enregistre ensuite l'arbitrage et transmet ses deltas. La fusion documentaire seule ne vaut pas approbation du MVP.
