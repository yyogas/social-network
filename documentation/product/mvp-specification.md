# Spécification du MVP candidat — contribution Produit M0

**Delta de positionnement — 30 septembre 2026, par 21 sur instruction du porteur :** [DIR-012](../project-governance/decision-register.md) confirme le public universel et les priorités marketing. Les règles et phases fonctionnelles restent proposées ; cette révision ne prétend pas constituer un nouvel avis de 01.

## 1. Identification et statut

| Champ | Valeur |
| --- | --- |
| Objectif | Définir une boucle sociale pilote utile, contrôlable et exploitable, et donner à HQ un dossier d'arbitrage |
| Propriétaire | 01 — Produit / Product Management ; reviewer humain GitHub NON REÇU |
| Mandat | M0-TEAM-01 ; réponse spécialisée à INT-0001 |
| Version / date | v0.2 — 30 septembre 2026 ; delta DIR-012 sur la contribution v0.1 |
| Référence d'entrée | PR [#2](https://github.com/yyogas/social-network/pull/2), branche `documentation/m0-team-coordination`, commit `dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957` |
| Statut | PROPOSÉ — avis 02/03/04/08/09/10/13/14/15/16/18/19 et arbitrages HQ attendus |
| Approbation / implémentation / vérification applicative | NON REÇUES ; aucun code ni résultat applicatif attesté par ce livrable |
| Phases et priorités | Toutes PROPOSÉES ; P0 indispensable au candidat pilote, P1 important, P2 évolution, P3 exploration |
| Périmètre | Promesse, segments, FEAT-001 à FEAT-022, classement FEAT-023 à FEAT-034, options communautés, données et interfaces conceptuelles, recette |
| Hors périmètre | Stack, DDL, endpoints définitifs, seuils légaux, budget, dates, fournisseurs, développement applicatif |

Entrées réellement lues : [mandat](../teams/work-orders.md), [modèle](../teams/deliverable-template.md), [plan documentaire](../documentation-plan.md), [vision](product-vision.md), [catalogue](feature-catalog.md), [parcours](user-journeys.md), [gouvernance](../governance.md), [conventions](../repository-conventions.md), [registre HQ](../project-governance/decision-register.md), [questions](../project-governance/coordination-board.md), [roadmap](../project-governance/global-roadmap.md), README et CONTRIBUTING. Toutes ces entrées sont lues au commit ci-dessus. La PR #2 reste ouverte à cette lecture ; `main` utilise encore les chemins historiques. Ce document doit donc être intégré avec ses dépendances documentaires, pas ajouté isolément à `main`.

Travaux réutilisés : référentiel Produit et backlog v0.1 (24 fiches, 35 stories) puis spécification pilote M0 v0.1 (17 stories), produits dans cette discussion avant accès au dépôt. Le présent fichier intègre leur contenu utile avec les IDs canoniques FEAT/J/AC. Les anciens Fxx et M0-Pxx ne créent pas de seconde numérotation GitHub ; aucune conversation brute ni donnée personnelle n'est importée.

### Nature des affirmations

| Élément | Nature | Preuve ou manque |
| --- | --- | --- |
| Société en France, public universel dès la conception, peuple kabyle inclus, contrôle et respect du temps | CONFIRMÉ | DIR-012 et vision HQ actualisée ; pas preuve d'ouverture par pays |
| GitHub central, branches et revue avant fusion, contributions M0 | CONFIRMÉ | DIR-010 / DIR-011 et mandat reçu dans cette discussion |
| Promesse et besoins ci-dessous, phases et permissions candidates | PROPOSÉ | Analyse Produit ; validation spécialisée et recherche non reçues |
| Âge, pays, langues, support, effectifs et budget disponibles | À VÉRIFIER | OPEN-001/002/004/006 ; réponses non reçues |
| Architecture, contrats API, limites média et politiques détaillées | NON REÇU | Aucun contrat approuvé fourni à cette rédaction |
| Stack évoquée dans les anciennes discussions | À VÉRIFIER | Les instructions GitHub réservent le choix à HQ/03 ; déclaration d'équipe ne vaut pas ADR approuvé |
| Fonctionnement du service, tests métier et mesures de cohorte | NON REÇU | Ce livrable est documentaire, pas une preuve de produit livré |

## 2. Promesse, besoin récurrent et segments à tester

**Promesse candidate :** retrouver des proches, des créateurs et des personnes partageant ses centres d'intérêt, partager une nouvelle, lire les réponses, puis revenir volontairement poursuivre l'échange, avec une audience et des protections compréhensibles. Le fil chronologique et la possibilité de terminer sa lecture rendent le contrôle visible. Ces choix ne prouvent pas une différenciation de marché : elle doit être confrontée aux usages existants.

| Segment pilote candidat | Besoin hypothétique | Situation concrète | Valeur à vérifier | Recherche attendue de 19/01 |
| --- | --- | --- | --- | --- |
| A — personnes suivant des proches, artistes ou créateurs et partageant des centres d'intérêt | Maintenir un lien et suivre des nouvelles pertinentes malgré la distance | Suivre quelques personnes, publier une image, recevoir une réponse, revenir la lire | Publication simple, fil compréhensible, maîtrise d'audience ; utilité suffisante sans groupe | Entretiens et observation de J01/J02/J03 ; raison du retour et frein à changer d'outil |
| B — animateurs d'association et membres d'un collectif | Regrouper annonces et échanges avec règles et responsabilité | Rejoindre un espace, lire une annonce, commenter, signaler un incident | Une communauté structurée pourrait être indispensable ; un profil public n'est pas un groupe | Observation de J07 ; besoin de membres/adhésion et capacité réelle de modération |

**Recommandation PROPOSÉE :** tester A avec un noyau de suivi de personnes ; étudier B en parallèle sans engager FEAT-020. Si les entretiens établissent que l'adhésion à un espace fermé est le besoin central, réexaminer cette recommandation avant DEC-0002. Aucun nombre de participants, seuil de rétention ni calendrier n'est inventé. Le groupe concret et les disponibilités humaines restent ouverts.

La boucle principale est J01 → FEAT-003/005 → J02/J03 → réponse utile → retour choisi. J04/J05 et J06 constituent les voies de protection et de sortie du même produit. La découverte initiale peut se faire par liens de profils et sélection éditoriale consentie ; elle n'exige ni recherche globale ni recommandation personnalisée.

## 3. Périmètre et classement de chaque fonctionnalité

Le catalogue demeure la référence d'IDs. Le tableau conserve ses classes tout en exposant la variante Produit pour FEAT-020. Rien ici ne modifie silencieusement la roadmap.

| ID | Capacité | Classe candidate | Priorité | Justification / limite |
| --- | --- | --- | --- | --- |
| FEAT-001 | Inscription et activation | MVP | P0 | Accès admissible ; méthode non fixée |
| FEAT-002 | Sessions, déconnexion et récupération | MVP | P0 | Protection et reprise d'accès |
| FEAT-003 | Profil minimal | MVP | P0 | Identité publique compréhensible ; champs facultatifs limités |
| FEAT-004 | Audience et confidentialité | MVP | P0 | Contrôler lecture et accès directs |
| FEAT-005 | Suivre / ne plus suivre | MVP | P0 | Source du fil ; abonnement social, sans paiement |
| FEAT-006 | Texte : créer, modifier, retirer | MVP | P0 | Boucle de création ; règle d'édition ouverte |
| FEAT-007 | Image et texte alternatif | MVP | P0 | Média simple ; ni vidéo ni caméra avancée |
| FEAT-008 | Fil chronologique | MVP | P0 | Ordre explicite et pagination ; pas de classement personnalisé |
| FEAT-009 | Réaction réversible | MVP | P1 | Conversation simple ; type unique proposé |
| FEAT-010 | Commentaires | MVP | P1 | Retour utile ; réponses profondes différées |
| FEAT-011 | Notifications essentielles | MVP | P1 | Centre interne proposé ; push et campagnes de réengagement exclus |
| FEAT-012 | Blocage | MVP | P0 | Arrêt des interactions définies ; pas promesse d'invisibilité absolue |
| FEAT-013 | Signalement | MVP | P0 | Réception traçable, protection du déclarant |
| FEAT-014 | Décision de modération | MVP | P0 | Mesures effectives, information et audit |
| FEAT-015 | Recours | MVP | P0 | Réexamen opérable, y compris compte suspendu |
| FEAT-016 | Accès/export et suppression de compte | MVP | P0 | Sortie du service et droits ; délais et exceptions à décider |
| FEAT-017 | Console de modération/support | MVP | P0 | Exploitation minimale avant ouverture UGC |
| FEAT-018 | Surface web responsive accessible | MVP | P0 | Proposition de première surface ; OPEN-002 non tranché |
| FEAT-019 | Mesures et santé minimales | MVP | P1 | Mesurer valeur et coût sans collecte excessive |
| FEAT-020 | Communautés | MVP conditionnel au catalogue ; Phase 2 recommandée par Produit | P1 | Arbitrage OPEN-003 ; jamais réputée incluse avant DEC-0002 |
| FEAT-021 | Langues du pilote | MVP | P0 | Interface, erreurs et modération dans les langues retenues |
| FEAT-022 | Respect du temps et commandes de lecture | MVP | P1 | Fin/rattrapage et préférences, sans maximiser durée |
| FEAT-023 | Recherche | Phase 2 | P1 | Liens de profil comme alternative pilote ; filtrage d'accès futur |
| FEAT-024 | Messages privés | Phase 2 | P2 | Modèle de sécurité, rétention et anti-abus à instruire |
| FEAT-025 | Applications mobiles natives | Phase 2 | P2 | Coût/valeur à comparer avec responsive/PWA par 06 |
| FEAT-026 | Vidéo et outils courts | Phase 2 | P2 | Coût, traitement, retrait et modération spécialisés |
| FEAT-027 | Outils et statistiques créateurs | Phase 2 | P2 | Dépend de mesures compréhensibles et minimisées |
| FEAT-028 | Pages professionnelles multi-gestionnaires | Phase 2 | P2 | Rôles délégués et usurpation à instruire |
| FEAT-029 | Recommandations facultatives | Phase 3 | P2 | Fil chronologique conservé ; contrôle et explicabilité |
| FEAT-030 | Publicité | Phase 3 | P2 | Économie, données, transparence et fraude avant ouverture |
| FEAT-031 | Revenus, abonnements payants et paiements créateurs | Phase 3 | P2 | Distinct du suivi FEAT-005 ; économie et litiges à décider |
| FEAT-032 | Expansion et opérations locales | International | P1 | Langue, pays et capacité humaine distincts |
| FEAT-033 | Live grande audience | Long terme | P3 | Procédure d'arrêt, capacité et modération démontrées |
| FEAT-034 | Intégrations et portabilité avancée | Long terme | P3 | Permissions, révocation et contrats versionnés |

Stories, événements, marketplace, Premium plateforme, newsletters, podcasts, AR, dons et Hub étendu figurent dans la vision ancienne mais n'ont pas d'ID distinct au catalogue reçu. **PROPOSÉ / À VÉRIFIER :** owners 01/07/08/11/12 et HQ doivent décider si ce sont sous-capacités d'une FEAT existante ou entrées nouvelles. Ne pas les implémenter sous un ID ambigu. Classe candidate à examiner : événements/Hub simple Phase 2 ; stories/marketplace/Premium/newsletters/dons Phase 3 ; podcasts/AR avancée Long terme. Aucun de ces ajouts n'est requis pour décider le noyau.

**Conditions d'ajout au MVP :** besoin central documenté auprès du segment retenu ; alternative simple insuffisante ; owner, contrats, permissions et recette définis ; coût et capacité de support/modération vérifiés ; impact sur les autres lots présenté à HQ. Une ambition ou un intérêt isolé ne suffit pas.

## 4. Fiches du candidat pilote

Toutes les règles suivantes sont PROPOSÉES. Elles expriment le besoin fonctionnel ; les owners 04/08/09/14/15 en ratifient les contrats, la sécurité et les données. États ci-dessous conceptuels, sans imposer enums DB ni codes HTTP. Valeurs de limites et durées restent À VÉRIFIER.

### FEAT-001 — Inscription et activation · MVP P0

- **Objectif/problème/acteur :** visiteur admissible souhaitant participer sans compte double ni collecte inutile. **Préconditions :** âge/pays, informations et méthode d'activation définis.
- **Parcours :** choisir langue → consulter informations → soumettre données → activer → accéder au profil ; champs facultatifs ignorables.
- **Règles/transitions :** en cours → attente activation → actif sur preuve recevable ; expiration permet reprise ; nouvelle tentative retrouve l'état sans double création.
- **États/erreurs :** données invalides, activation expirée/consommée, contact inaccessible, limite de tentatives, réseau incertain ; ne pas confirmer un succès non reçu.
- **Permissions/données :** visiteur crée seulement sa demande ; membre non activé limité selon politique ; contact, preuve d'admissibilité minimale et consentements séparés du nom public.
- **Dépendances/risques/succès :** 04/14/15/16 ; énumération, usurpation et exclusion par vérification ; observer complétion et abandon sans publier les contacts. Recette : AC-J01-01/02 et AC-PROD-001.

### FEAT-002 — Sessions et récupération · MVP P0

- **Objectif/problème/acteur :** membre voulant entrer, sortir et reprendre l'accès ; support ne doit pas contourner la vérification.
- **Parcours :** connexion → session → déconnexion ; perte d'accès → demande neutre → vérification → reprise → gestion des sessions.
- **Règles/états :** session active → révoquée/expirée ; récupération demandée → vérifiée/expirée ; la révocation protège aussi les accès directs.
- **Erreurs/reprise :** refus d'identité, délai ou limite de tentatives, transport incertain ; message neutre sur existence du compte, aucun droit créé avant vérification.
- **Permissions/données :** titulaire agit sur ses sessions ; suspendu conserve seulement les voies autorisées de recours/droits ; traces minimales, aucun secret de session dans analytics.
- **Dépendances/risques/succès :** 04/10/14/15 ; prise de contrôle et sessions résiduelles ; taux de récupération réussie et incidents. Recette : AC-J01-03/04 et AC-PROD-002.

### FEAT-003 — Profil · MVP P0

- **Objectif/problème/acteur :** membre souhaitant être reconnu et retrouver une personne. **Précondition :** compte admissible et règle de visibilité.
- **Parcours :** compléter nom d'affichage, bio et avatar facultatifs → aperçu → enregistrer → consulter un autre profil autorisé.
- **Règles/états :** non complété, enregistré, modification, indisponible/suspendu ; noms similaires permis selon politique, handle unique seulement si retenu au contrat.
- **Erreurs/cas limites :** entrée invalide, avatar échoué, profil supprimé entre chargement et action ; aucune écriture d'un tiers ni écrasement silencieux concurrent.
- **Permissions/données :** propriétaire édite ; tiers voit seulement champs autorisés ; contact et preuve d'âge jamais assimilés à la bio ; opérateur limité à son rôle.
- **Dépendances/risques/succès :** 02/04/08/14/15/16 ; usurpation et divulgation ; compréhension de l'identité, premiers suivis pertinents. Recette : AC-PROD-003.

### FEAT-004 — Visibilité · MVP P0

- **Objectif/problème/acteur :** auteur choisissant qui lit son contenu ; lecteur doit comprendre pourquoi un accès est refusé sans apprendre le contenu.
- **Parcours :** ouvrir réglages → voir audience actuelle → modifier → comprendre effet sur anciens abonnés/publications → confirmer.
- **Options :** public seul avec restriction de diffusion, ou public/privé avec approbation des suivis ; public/privé recommandé sous réserve de faisabilité et Privacy. Aucun défaut de visibilité décidé.
- **États/erreurs :** modification en cours, appliquée, propagation/échec contrôlé ; changement concurrent et liens déjà partagés ; ne pas promettre rappel d'une copie externe.
- **Permissions/données :** lecture réévaluée côté service sur détail, fil, média et aperçu ; auteur gère sa visibilité, opérateur n'obtient pas un droit global implicite ; règles d'audience et historique nécessaire.
- **Dépendances/risques/succès :** 03/04/09/14/15 ; fuite via surfaces secondaires ; taux de réussite d'une tâche d'audience et absence de divulgation dans les tests. Recette : AC-J02-01/04/05, AC-PROD-004.

### FEAT-005 — Abonnement social · MVP P0

- **Objectif/problème/acteur :** membre voulant recevoir les publications de personnes choisies. Aucun achat ou avantage payant.
- **Parcours :** profil accessible → suivre ou demander → voir état → fil ; annuler demande ou ne plus suivre.
- **Règles/transitions :** aucun lien → demandé si privé → accepté → retiré ; refus/annulation terminent demande ; répétition ne crée pas de relation double ; blocage prime selon matrice validée.
- **Erreurs/cas limites :** cible supprimée/suspendue, demande rejetée, blocage après clic, réseau incertain ; refléter état confirmé.
- **Permissions/données :** membre gère sa relation ; cible privée décide de l'admission si cette option retenue ; relation, demandes et horodatages minimaux ; compteurs selon Privacy.
- **Dépendances/risques/succès :** 03/04/09/14/15 ; graphe utilisé pour harcèlement ; suivre puis lire réellement un contenu autorisé. Recette : AC-J03-03, AC-PROD-005.

### FEAT-006 — Texte et cycle de publication · MVP P0

- **Objectif/problème/acteur :** auteur voulant partager et corriger/retirer sa publication ; audience visible avant envoi.
- **Parcours :** composer → audience → publier → confirmation → modifier ou retirer avec conséquence annoncée.
- **Règles/états :** brouillon → soumission → publié/échec ; édition selon validation et révision attendue ; retrait → inaccessible aux lectures ordinaires. Pas de promesse d'effacement immédiat des preuves/sauvegardes.
- **Erreurs/cas limites :** texte invalide, droits perdus, soumission répétée, réponse perdue après écriture, éditions concurrentes ; préserver saisie si sûr, réconcilier avant resoumettre.
- **Permissions/données :** auteur crée/édite/retire son texte ; modérateur peut retirer selon politique, sans éditer silencieusement le propos ; contenu, audience, statut, auteur et traces d'édition limitées.
- **Dépendances/risques/succès :** 04/08/09/15 ; spam, perte de saisie, doublons ; publication réussie et réponse utile. Recette : AC-J02-01/03/05, AC-PROD-006.

### FEAT-007 — Image · MVP P0

- **Objectif/problème/acteur :** auteur voulant joindre une image lisible et accessible ; lecteur autorisé doit seul accéder au fichier.
- **Parcours :** sélectionner image → validation → texte alternatif → traitement → association au texte → confirmation.
- **Règles/états :** sélectionné → upload → validation/traitement → prêt → associé/publié ; échec récupérable, média non validé non diffusé ; une image par publication proposée pour réduire coût.
- **Erreurs/cas limites :** type/taille refusés, traitement échoué, interruption, retrait pendant traitement, métadonnées sensibles ; aucune URL non contrôlée ne doit devenir voie de contournement.
- **Permissions/données :** auteur charge dans sa publication ; lecture suit audience et statut ; original/dérivés, texte alternatif et états ; traitement des métadonnées et purge par 08/15.
- **Dépendances/risques/succès :** 08/04/09/14/15 ; coût, fichier malveillant et géolocalisation involontaire ; lectures réussies, erreurs et accessibilité. Recette : AC-J02-02/04/05, AC-PROD-007.

### FEAT-008 — Fil chronologique · MVP P0

- **Objectif/problème/acteur :** membre voulant lire les publications de ses suivis dans un ordre intelligible.
- **Parcours :** ouvrir → lire page → demander suite → finir/rattraper ; fil vide mène à suivre une personne ou publier.
- **Règles/états :** chargement, vide, page, fin, nouvelles publications, erreur partielle ; ordre décroissant de publication et départage stable à définir par 04 ; édition ne remonte pas artificiellement au sommet, proposition à ratifier.
- **Erreurs/cas limites :** nouveau contenu pendant pagination, retrait/blocage, réseau lent ; garder contenu autorisé déjà affiché, ne pas dupliquer ni sauter sans explication selon contrat de pagination.
- **Permissions/données :** filtre d'éligibilité au service ; relation, publications et position éventuelle ; curseur n'octroie aucun droit durable. Pas de copie privée permanente dans analytics.
- **Dépendances/risques/succès :** 02/04/07/14/15 ; fil vide, cache périmé ; lecture utile, ordre compris, chargement réussi. Recette : AC-J03-01/02, AC-PROD-008.

### FEAT-009 — Réaction · MVP P1

- **Objectif/acteur :** lecteur voulant exprimer une réaction légère puis l'annuler.
- **Parcours/règles :** activer puis retirer ; une réaction simple par compte/contenu proposée ; retry et retrait sont idempotents au niveau métier.
- **États/erreurs :** aucune, en cours, active, retirée ; contenu supprimé, droits perdus, réseau incertain ; un état optimiste n'est pas preuve serveur et doit être corrigé.
- **Permissions/données :** lecteur autorisé et non interdit d'interagir ; auteur de réaction peut retirer ; lien contenu/compte/type, compteurs selon politique.
- **Dépendances/risques/succès :** 04/09/15 ; gonflage artificiel et métriques de vanité ; cohérence après reprise, qualité des retours. Recette : AC-J03-03, AC-PROD-009.

### FEAT-010 — Commentaires · MVP P1

- **Objectif/acteur :** lecteur voulant répondre et auteur de commentaire souhaitant retirer ses propos.
- **Parcours/règles :** saisir → envoyer → afficher confirmé → retirer ; fil simple proposé, réponses imbriquées multiples différées ; audience héritée du parent.
- **États/erreurs :** saisie, envoi, publié, retiré, refus ; parent retiré avant envoi, double soumission, auteur suspendu ; aucune écriture si droits perdus.
- **Permissions/données :** lecteur autorisé commente ; propriétaire retire son commentaire ; modérateur selon policy ; auteur de publication ne dispose pas implicitement d'un pouvoir global de suppression des autres commentaires.
- **Dépendances/risques/succès :** 04/09/15/02 ; harcèlement, décontextualisation ; réponses reçues et blocages/signalements. Recette : AC-J03-02 et AC-PROD-010.

### FEAT-011 — Notifications essentielles · MVP P1

- **Objectif/acteur :** membre voulant retrouver une réponse utile sans être sollicité excessivement.
- **Parcours/règles :** centre interne → lire → ouvrir destination autorisée → régler catégories ; commentaires et demandes de suivi proposés ; décisions/recours relèvent de messages de service distincts, règles par 09/15.
- **États/erreurs :** non lue/lue, source retirée, accès refusé ; doublon, diffusion retardée ; notification disparue ne révèle pas le texte retiré.
- **Permissions/données :** destinataire seul, préférences et référence d'événement ; pas d'aperçu privé sur canal non validé. Push mobile différé FEAT-025.
- **Dépendances/risques/succès :** 02/04/09/15 ; fatigue et fuite ; retour utile et désactivation par catégorie. Recette : AC-J03-05, AC-PROD-011.

### FEAT-012 — Blocage · MVP P0

- **Objectif/acteur :** membre voulant arrêter les interactions directes nuisibles.
- **Parcours/règles :** choisir blocage → lire effet → confirmer → résultat ; lever blocage ne restaure pas automatiquement le suivi, proposition à examiner par 09.
- **États/erreurs :** en cours, actif, levé ; demande répétée, compte supprimé, ancienne interaction en cache. La sanction et le signalement restent distincts.
- **Permissions/données :** titulaire gère son blocage ; services refusent actions visées par matrice ; relation protégée, pas d'identité du déclarant dévoilée via dossier.
- **Limite :** un contenu public déjà copié ou accessible anonymement ne peut être promis invisible à la personne bloquée ; règle exact public/privé à expliquer par 09/15.
- **Dépendances/risques/succès :** 09/04/14/15 ; contournement et fausse assurance ; refus sur toutes les interactions définies. Recette : AC-J04-01/03, AC-PROD-012.

### FEAT-013 — Signalement · MVP P0

- **Objectif/acteur :** membre signalant une publication ou un compte sans être exposé à la cible.
- **Parcours/règles :** motif → contexte minimal → envoyer → accusé et référence ; signaler n'implique pas sanction ; masquage/blocage disponible séparément.
- **États/erreurs :** saisie, transmission, reçu, suivi permis ; réseau absent, cible retirée, doublon ; pas de statut « reçu » sans accusé ; preuve admise définie par 09/15.
- **Permissions/données :** auteur voit son suivi limité ; agents habilités voient contexte nécessaire ; cible ne voit pas identité ni notes privées du reporter.
- **Dépendances/risques/succès :** 09/10/04/15 ; brigading, dossiers perdus ; réception fiable et triage. Recette : AC-J04-02/03/04, AC-PROD-013.

### FEAT-014 — Modération · MVP P0

- **Objectif/acteur :** agent habilité appliquant une règle motivée et vérifiable.
- **Parcours/règles :** ouvrir dossier → examiner → décision/motif → confirmer → application → notification ; application, audit et remise distincts en cas d'échec partiel.
- **États/erreurs :** à examiner, en examen, décision prise, application en attente/échouée/effective ; conflit de traitement, rôle révoqué ; retry n'applique pas deux sanctions.
- **Permissions/données :** lecture/action séparées ; pouvoirs selon rôle et périmètre ratifiés ; décision, preuve limitée, agent, effet et notification ; aucune note privée exposée au membre.
- **Dépendances/risques/succès :** 09/10/04/14/15 ; sur/sous-modération et saturation ; délais par gravité, corrections, stock de dossiers. Recette : AC-J05-01/02/03, AC-PROD-014.

### FEAT-015 — Recours · MVP P0

- **Objectif/acteur :** personne affectée contestant une décision selon policy.
- **Parcours/règles :** recevoir information autorisée → demander réexamen → consulter état → résultat motivé ; indépendance et limites à trancher par 09.
- **États/erreurs :** déposé, recevable/non recevable, en examen, confirmé/modifié/annulé ; session suspendue, décision introuvable, requête répétée, restauration partielle.
- **Permissions/données :** demandeur concerné et reviewer habilité ; accès restreint malgré suspension via contrat dédié ; dossier lié à décision, sans dévoiler reporter.
- **Dépendances/risques/succès :** 09/10/04/14/15 ; recours inaccessible et erreur irréversible ; états consultables et corrections traçables. Recette : AC-J05-04/05, AC-PROD-015.

### FEAT-016 — Accès/export et sortie du service · MVP P0

- **Objectif/acteur :** titulaire voulant récupérer ses données ou demander la suppression du compte.
- **Parcours/règles :** paramètres → conséquences et vérification → demande → état → résultat sécurisé ; export et suppression restent deux demandes distinctes.
- **États/erreurs :** demandé, vérification, traitement, prêt/expiré ou suppression en cours/terminée selon contrat ; traitement interrompu, demande déjà ouverte, lien périmé.
- **Permissions/données :** titulaire vérifié ; support limité ; contenu exportable, tiers, preuves, sessions, médias, jobs et sauvegardes traités par inventaire owner 15 ; aucun délai légal inventé.
- **Dépendances/risques/succès :** 15/04/10/14/08 ; export d'autrui, réintroduction lors restauration ; demandes réussies et états exacts. Recette : AC-J06-01 à 04, AC-PROD-016.

### FEAT-017 — Console minimale · MVP P0

- **Objectif/acteur :** modérateur/support traitant abus et problèmes de compte dans une habilitation limitée.
- **Parcours/règles :** session opérateur renforcée → file → dossier → action autorisée → audit ; pas d'impersonation générique ni d'export global implicite.
- **États/erreurs :** file vide/chargement, dossier déjà pris, rôle retiré, action partiellement échouée ; distinguer lecture, décision et action effective.
- **Permissions/données :** rôles 10 validés par 14/15 ; aucune super-permission adoptée ici ; motifs, références, audit minimal ; données privées seulement si nécessité/habilitation démontrée.
- **Dépendances/risques/succès :** 10/09/04/14/15 ; abus internes et erreur support ; tâches autorisées achevées, accès refusés tracés. Recette : AC-J05-01/03, AC-PROD-017.

### FEAT-018 — Web responsive et accessibilité · MVP P0 proposé

- **Objectif/acteur :** visiteur et membre utilisant les parcours prioritaires sur des écrans et modalités variés.
- **Parcours/règles :** mêmes buts J01–J06 ; navigation clavier et assistée, libellés et erreurs associés, focus maîtrisé, contenu adaptable ; détails et objectifs d'accessibilité par 02/05/18.
- **États/erreurs :** chargement, vide, hors ligne partiel, refus, suspension ; aucune réussite simulée offline ; brouillon local à examiner par 15.
- **Permissions/données :** interface reflète les droits mais service les contrôle ; cache privé révoqué selon 14/15 ; pas de navigateur réputé testé sans preuve.
- **Dépendances/risques/succès :** OPEN-002, 02/05/06/04/14/18 ; exclusion mobile ou assistive ; réussite des tâches sur supports retenus. Recette : AC-J03-04, AC-PROD-018.

### FEAT-019 — Mesures minimales · MVP P1

- **Objectif/acteur :** Produit/Data et exploitant évaluant utilité, fiabilité, coût et sûreté du pilote.
- **Parcours/règles :** définir événement/cohorte → collecter selon politique → calculer → comparer ; analytics, finance et audit sécurité distingués ; logs applicatifs ne sont pas source libre de données privées.
- **États/erreurs :** événement absent/retardé/dupliqué ; collecte désactivée selon règle applicable ; ne pas lire absence de données comme absence d'incident.
- **Permissions/données :** accès agrégé par défaut ; pas de texte, contact, secret ou contenu de signalement dans événement Produit ; schéma et rétention par 13/15.
- **Dépendances/risques/succès :** 13/14/15/19 ; surcollecte et métriques trompeuses ; définitions reproductibles, couverture et contre-mesures. Recette : AC-PROD-019.

### FEAT-020 — Communautés · inclusion MVP conditionnelle, Phase 2 recommandée

- **Objectif/acteur :** membre/animateur voulant un espace commun avec adhésion et règles.
- **Parcours/règles :** présentation → règles → admission selon type → échange → départ ; statut local distinct du compte ; rôle local sans pouvoir global.
- **États/erreurs :** demande, admis, refusé, exclu, parti, fermé ; dernier animateur perdu, fermeture, conflit entre blocage et cohabitation ; aucune résolution inventée par le code.
- **Permissions/données :** membre, animateur et modérateur plateforme distincts ; présentation, règles, membership, contenus et sanctions locales ; accès non-membre et devenir des contenus après départ ouverts.
- **Dépendances/risques/succès :** OPEN-003, 19/09/10/04/14/15 ; coût humain et audiences multiples ; utilité collective, participation récurrente et dossiers soutenables. Recette conditionnelle : AC-J07-01 à 04, AC-PROD-020.

### FEAT-021 — Langues du pilote · MVP P0

- **Objectif/acteur :** personne choisissant une interface et obtenant une information compréhensible.
- **Parcours/règles :** choix de langue disponible → parcours, erreurs, privacy et support cohérents ; langue d'interface, langue de contenu, résidence et appartenance communautaire séparées.
- **États/erreurs :** langue disponible, traduction manquante, fallback explicite ; écriture non latine, noms multilingues ; pas de traduction automatique du texte privé par défaut.
- **Permissions/données :** préférence de langue minimale ; aucun accès élargi à cause de langue ; champs privés restent protégés dans toutes les traductions.
- **Dépendances/risques/succès :** OPEN-004, 16/02/09/15/19 ; texte traduit sans modération disponible ; tâche comprise et support linguistique réel. Recette : AC-PROD-021.

### FEAT-022 — Respect du temps · MVP P1

- **Objectif/acteur :** lecteur voulant décider quand consulter et terminer sa lecture.
- **Parcours/règles :** lire → atteindre fin/rattrapage → quitter ou charger volontairement ; retrouver réglages de notification ; repère de lecture exact selon contrat, aucune fausse fin sur erreur réseau.
- **États/erreurs :** suite disponible, fin, nouveautés, chargement échoué ; changement de session ou volume de contenu ; indiquer limites du repère sans inventer lecture complète.
- **Permissions/données :** position/préférence propres au membre ; stockage local ou service à décider par 02/15 ; pas d'objectif de maximisation du temps.
- **Dépendances/risques/succès :** 02/04/13/15 ; commande cachée et boucle forcée ; contrôle perçu et tâche réussie. Recette : AC-PROD-022.

## 5. Permissions candidates, données et interfaces

### 5.1 Matrice fonctionnelle à ratifier — OPEN-007

| Acteur/état | Action et ressource | Portée et contrôle candidat | Refus / limite attendus |
| --- | --- | --- | --- |
| Anonyme | Lire profil ou texte/image | Public seulement si policy pilote autorise accès sans compte | Aucune donnée privée, aucun indice sensible dans extrait ; option pilote fermé à trancher |
| Membre actif | Publier, suivre, réagir/commenter | Son compte, contenu accessible, droits et limites valides | Refus après perte de droit même si bouton encore affiché |
| Propriétaire | Éditer/retirer son profil ou contenu | Ressource propre, état valide, contraintes de modération | Posséder ne permet pas contourner une restriction plateforme |
| Autre membre | Lire texte, dérivé média ou fil | Audience courante, relation et état modération applicables | URL, cursor, cache ou ancien lien ne constituent pas autorisation |
| Auteur avec audience privée | Admettre/révoquer abonnés si option retenue | Seulement demandes de son profil | Aucun droit sur autres profils ; accès réévalué après révocation |
| Membre bloqué | Lire/interagir selon matrice 09/15 | Refus des actions explicitement interdites | Pas promesse de rappel de copie publique ou d'identification de visiteurs anonymes |
| Compte suspendu | Activités sociales interdites selon sanction ; accès au recours/droits | Accès séparé et limité à ses démarches admissibles | Aucune publication nouvelle ; ne pas enfermer recours dans route interdite par la même suspension |
| Modérateur | Lire dossier, décider, appliquer mesure | Rôle, dossier, motif, habilitation et audit | Pas de réécriture d'un contenu ni lecture générale de données privées |
| Support | Répondre/récupération assistée/droits selon rôle | Informations et actions nécessaires au dossier | Pas de reset arbitraire, export global ou contournement de contrôle |
| Analyste | Mesures pilote | Agrégats autorisés, pas contenu privé | Données identifiantes et finance distinctes |

Cette matrice est un besoin à examiner, pas un RBAC/ABAC final. Les contrôles de lecture et d'écriture sont dans le service. 09/14/15 et HQ définissent défauts, exceptions, traitement des comptes existants et politique des visiteurs.

### 5.2 Données et cycle de vie conceptuels

Stockage physique, schémas, chiffrement et durées NON REÇUS, owners 03/04/14/15. Aucune donnée réelle dans le livrable. Modification/export/suppression sont à relier à FEAT-016 pour chaque catégorie.

| Catégorie / origine / finalité | Champs minimaux proposés et visibilité | Accès internes / événements | Modification, export, suppression et sauvegardes à définir |
| --- | --- | --- | --- |
| Compte, fourni/vérifié pour accès | Référence, contact, état, langue, preuve minimale admissibilité ; privé | Services AUTH et rôles habilités ; audit sans secret | Rectification vérifiée, export limité, désactivation et cycle d'effacement ; pas restoration réactivant compte supprimé |
| Profil, fourni pour représentation | Nom public, bio, avatar facultatif, audience ; champs publics distincts du compte | Modération nécessaire, pas accès générique | Édition, retrait des versions/dérivés et caches ; export des champs propres |
| Relations, actions sociales | Source/cible, statut suivi/demande/blocage ; visibilité à décider | Contrôle d'accès et anti-abus limités | Révocation cohérente ; export protège tiers ; suppression ne restaure pas suivis |
| Publication/commentaire/réaction, fourni pour échange | Auteur, texte, audience, parent, état, date ; public autorisé | Modération sur dossier/permissions ; analytics références minimisées | Retrait de diffusion distinct purge ; traitement des tiers, preuves et sauvegardes par 15 |
| Média, upload pour lecture | Original/dérivés, alt, état, audience associée ; contrôle d'accès | Chaîne 08 et examen habilité | Liens/caches/jobs retirés selon contrat, métadonnées minimisées, purge et restauration documentées |
| Dossier décision/recours, signalant et opérateur | Motif, références, contexte nécessaire, états, décision ; restreint | 09/10 et audit 14 ; reporter protégé | Conservation et exceptions par 15, correction traçable, export expurgé des tiers si requis |
| Préférences/notification/droits, actions utilisateur | Catégories, référence événement, état lecture, demande export/suppression ; titulaire | Service et support selon rôle ; pas contenu privé dans aperçu | Révocation/expiration, suppression/portabilité selon finalité et canal |
| Analytics/audit, événements systèmes | Type événement, cohorte/ref minimisée, résultat ; agrégats séparés des journaux sensibles | 13 agrégats, 14 audit, accès limités | Définitions, opt-in/out applicable, conservation et retrait par 13/15 ; restauration ne relance pas collecte interdite |

### 5.3 Besoins de contrats producteur/consommateur

IDs et versions API/event/job : NON REÇUS, attribution par 04/03. Aucun endpoint ou timeout numérique imposé. Pour chaque ligne 04 doit fournir authentification, autorisation, schémas, erreurs, délai, retry, idempotence, concurrence, quotas, corrélation, compatibilité et cas de tests. Les libellés d'erreur ci-dessous expriment des raisons fonctionnelles, pas des codes définitifs.

| Opération / FEAT | Producteur → consommateurs | Entrée / sortie conceptuelles | Échec et reprise demandés |
| --- | --- | --- | --- |
| Activer/session/récupérer, 001/002 | 04 avec 14 → 05, 06 si retenu, 10 | Données minimales et vérification → état, prochaine action, session si autorisée | INVALID_INPUT, EXPIRED_PROOF, RATE_LIMITED ; message neutre, pas de droit sur retry avant vérification |
| Profil/audience/suivi/blocage, 003/004/005/012 | 04 avec 09/14/15 → clients, fil | Référence, action, révision attendue → état confirmé et visibilité | FORBIDDEN, NOT_AVAILABLE, STATE_CONFLICT ; contrôle courant, idempotence du suivi/blocage |
| Publication/édition/retrait, 006/007 | 04 + 08 → clients, fil, modération | Contenu, audience, média prêt, clé reprise/révision → ressource/état | MEDIA_NOT_READY, TRANSPORT_UNCERTAIN, VERSION_CONFLICT ; réconcilier création, pas écraser édition concurrente |
| Fil et interactions, 008/009/010 | 04 → 05/06, 13 minimisé | Cursor/requête ou parent/action → page autorisée ou résultat | ACCESS_CHANGED, PARENT_REMOVED ; cursor non autorisant, écriture refusée après changement |
| Notification, 011/014/015 | 04/09 → clients et canaux retenus | Événement et référence → statut livraison/lecture | DELIVERY_FAILED, SOURCE_UNAVAILABLE ; replay sans fuite/doublon, échec remise distinct échec décision |
| Signalement/décision/recours, 013/014/015/017 | 04/09/10 → console et membre concerné | Motif/dossier/action/révision → état, résultat et information limitée | ROLE_REVOKED, ALREADY_HANDLED, PARTIAL_FAILURE ; transaction/compensation par 04, application et audit distingués |
| Export/suppression, 016 | 04/15 → titulaire, support habilité, jobs 08 | Identité vérifiée/demande → référence, progression, résultat | VERIFICATION_FAILED, EXPORT_EXPIRED, PROCESSING_FAILED ; retry contrôlé, traitement des sauvegardes |
| Mesures, 019 | Services validés → 13/14 | Événement minimisé versionné → agrégat/état pipeline | Duplicate/delay/missing ; pas inventer données absentes ni déduire absence d'abus |

## 6. Backlog candidat et critères observables

Le backlog reprend les FEAT existantes. Stories rédigées, aucune « READY » : contrats, UX et décisions attendus. Leurs priorités sont celles du tableau §3. Les critères complémentaires ci-dessous sont proposés dans l'espace `AC-PROD` pour éviter collision avec les 31 `AC-Jxx-xx` HQ ; 17/18 en vérifient l'intégration. Identifiants TEST : NON ATTRIBUÉS, owner 18. **Tous les critères et tests métier ci-dessous sont PLANNED, non exécutés.**

| FEAT / story | User Story | Critère complémentaire et résultat observable | Type prévu / dépendance |
| --- | --- | --- | --- |
| 001 | En tant que visiteur admissible, je veux activer un compte, afin de participer au pilote. | AC-PROD-001 : Étant donné une activation reçue mais réponse perdue, lorsque la personne reprend, alors le service retrouve un seul compte et son état. | API/E2E ; 04/14/15 |
| 002 | En tant que membre, je veux gérer mes sessions, afin de protéger mon accès. | AC-PROD-002 : Étant donné une session révoquée, lorsque détail privé ou upload est demandé, alors aucun accès protégé n'est délivré. | API ; 04/14 |
| 003 | En tant que membre, je veux présenter mon profil, afin d'être reconnu. | AC-PROD-003 : Étant donné un autre membre, lorsqu'il tente une modification du profil, alors elle est refusée et les champs privés sont absents de sa lecture. | API/E2E ; 04/15 |
| 004 | En tant qu'auteur, je veux choisir l'audience, afin de contrôler la diffusion. | AC-PROD-004 : Étant donné un accès révoqué, lorsque le lecteur utilise ancienne URL, cursor ou média, alors il ne reçoit pas contenu/dérivé non autorisé selon la matrice ratifiée. | Intégration/API ; 03/04/08/14/15 |
| 005 | En tant que membre, je veux suivre une personne, afin de lire ses nouvelles. | AC-PROD-005 : Étant donné un profil privé si retenu, lorsque suivre est demandé sans approbation, alors la relation reste en attente et ne donne pas lecture privée. | API/E2E ; 04/15 |
| 006 | En tant qu'auteur, je veux corriger puis retirer un texte, afin de maîtriser ma publication. | AC-PROD-006 : Étant donné deux éditions de la même révision, lorsque la seconde est soumise après la première, alors le conflit est signalé sans perte silencieuse. | API ; 04 |
| 007 | En tant qu'auteur, je veux joindre une image décrite, afin de partager un média accessible. | AC-PROD-007 : Étant donné un retrait pendant traitement, lorsque un dérivé est produit, alors il n'est pas diffusé contre le nouvel état. | Intégration ; 08/04/15 |
| 008 | En tant que lecteur, je veux un fil chronologique, afin de comprendre l'ordre des nouveautés. | AC-PROD-008 : Étant donné même date de publication et ajout concurrent, lorsque la suite est chargée, alors départage/pagination respectent le contrat et n'affichent aucun doublon. | API/E2E ; 04/07 |
| 009 | En tant que lecteur, je veux réagir et annuler, afin de donner un retour réversible. | AC-PROD-009 : Étant donné réponse perdue après réaction, lorsque la requête est rejouée, alors une seule réaction active est comptée. | API ; 04 |
| 010 | En tant que lecteur, je veux commenter, afin de participer à l'échange. | AC-PROD-010 : Étant donné parent retiré avant l'envoi, lorsque le commentaire est soumis, alors aucune écriture non autorisée n'apparaît et la reprise explique le refus. | API/E2E ; 04/09 |
| 011 | En tant que membre, je veux maîtriser mes notifications, afin de revenir sans pression. | AC-PROD-011 : Étant donné catégorie facultative désactivée, lorsque événement survient, alors sa diffusion respecte le contrat sans altérer les messages de décision distincts. | Intégration/E2E ; 04/09/15 |
| 012 | En tant que membre, je veux bloquer, afin d'arrêter des interactions nuisibles. | AC-PROD-012 : Étant donné blocage effectif, lorsque une interaction interdite est tentée avec ancien écran, alors le service la refuse ; lever le blocage suit la règle de non-restauration retenue. | API ; 09/04/14/15 |
| 013 | En tant que membre, je veux signaler, afin de demander un examen. | AC-PROD-013 : Étant donné coupure réseau, lorsque l'envoi reste sans accusé, alors interface ne dit pas « reçu » et peut vérifier/reprendre sans dossier incohérent. | E2E/intégration ; 04/09/10 |
| 014 | En tant que modérateur habilité, je veux décider avec motif, afin d'appliquer la politique. | AC-PROD-014 : Étant donné décision enregistrée mais application échouée, lorsque dossier est relu, alors décision, échec et reprise restent distinguables. | Intégration ; 04/09/10 |
| 015 | En tant que personne sanctionnée, je veux contester, afin de faire corriger une erreur. | AC-PROD-015 : Étant donné suspension sociale, lorsque le titulaire accède au recours autorisé, alors il peut déposer/consulter sans retrouver droits sociaux interdits. | API/E2E ; 04/09/10/14 |
| 016 | En tant que titulaire, je veux exporter ou supprimer, afin de quitter le service avec contrôle. | AC-PROD-016 : Étant donné demande traitée et restauration de sauvegarde, lorsque service reprend, alors les restrictions et effacements approuvés ne sont pas annulés par réintroduction. | Intégration/recovery ; 15/14/04 |
| 017 | En tant qu'agent, je veux un accès limité au dossier, afin de traiter sans excès de privilège. | AC-PROD-017 : Étant donné rôle retiré pendant session, lorsque l'agent agit, alors lecture/action désormais interdites sont refusées. | API ; 10/14/04 |
| 018 | En tant que personne utilisant le clavier ou une aide de lecture, je veux terminer les parcours, afin d'accéder au pilote. | AC-PROD-018 : Étant donné environnement retenu, lorsque J01/J02/J04 est exécuté au clavier/aide définie par 18, alors aucune action essentielle n'est inaccessible. | Accessibilité/E2E ; 02/05/18 |
| 019 | En tant que responsable Produit, je veux des mesures minimisées, afin d'évaluer le pilote sans exposer les membres. | AC-PROD-019 : Étant donné événements de test synthétiques, lorsque payload est inspecté, alors aucune catégorie de secret/contact/texte privé interdite n'y figure. | Schéma/intégration ; 13/15 |
| 020 | En tant que membre d'un collectif, je veux rejoindre un espace, afin d'échanger selon ses règles. | AC-PROD-020 : Étant donné exclusion ou départ si communauté retenue, lorsque contenu restreint est demandé directement, alors l'accès suit le nouveau statut et le rôle local ne donne aucun pouvoir global. | API/E2E conditionnel ; 04/09/15 |
| 021 | En tant que membre, je veux comprendre les erreurs dans ma langue, afin de reprendre une tâche. | AC-PROD-021 : Étant donné langue pilote choisie, lorsque erreur/refus/recours survient, alors le message et le support associé utilisent une traduction relue ou un fallback explicite validé. | Localisation ; 16/02/09 |
| 022 | En tant que lecteur, je veux choisir quand arrêter, afin de maîtriser mon temps. | AC-PROD-022 : Étant donné échec du chargement de suite, lorsque état est affiché, alors il n'est pas confondu avec « tout lu » et une reprise volontaire est proposée. | E2E ; 02/04/05 |

**Recette complémentaire transversale à transmettre à 18 :** mêmes parcours avec réseau lent/offline, transport incertain, compte suspendu, permissions modifiées, données invalides, créations/éditions simultanées et charge pilote à définir. Compatibilité navigateur, médias, rétention, sauvegarde et incident sont à intégrer aux plans propriétaires. Aucun critère de performance n'est qualifié PASS sur la base de cette rédaction.

## 7. Comparaison structurante et décisions à demander

Réutiliser DEC-0001 (public/pays) et DEC-0002 (contrat MVP) réservés par HQ. Aucun DEC/ADR supplémentaire n'est attribué unilatéralement.

### Dossier DEC-0001 — segment, pays et accès

- **Objectif/problème :** choisir un groupe assez cohérent pour tester utilité et capacité de soutien ; positionnement universel ne signifie pas ouverture simultanée de tous les pays ; sélectionner des besoins communs, sans critère d'origine.
- **Solution proposée :** segment A, cohorte recrutée par 19, supports web proposés ; pays, langue et âge définis avec 15/16/09, aucune présomption juridique.
- **Alternatives, non rejetées :** segment B association ; mix A+B ; ouverture large. B peut mieux différencier mais exige adhésion/modération ; mix et large brouillent la mesure et amplifient charge.
- **Dépendances :** besoin observé 19, faisabilité 05/06, support 09/10/16, budget HQ/14. **Impact business :** coût de recrutement et utilité récurrente ; revenus hors pilote. **Impact technique :** surfaces, audiences et langues.
- **Risques/priorité :** RISK-0002/0003, P0 pour bornes du pilote. **Réexamen :** incapacité à recruter ou besoin principal non servi. **Autorité :** HQ après avis ; PROPOSÉ.

### Dossier DEC-0002 / OPEN-003 — communautés

| Option | Valeur hypothétique | Complexité/coût à vérifier | Impact et risque | Avis Produit |
| --- | --- | --- | --- | --- |
| A — suivis seuls, FEAT-020 différée | Liens, créateurs et conversations individuelles | Moins de rôles et de transitions ; coût réel non chiffré | Ne répond pas à besoin de groupe fermé, contrôle collectif limité | Recommandée pour tester segment A |
| B — communautés dès MVP | Identité collective, règles, adhésion et échanges | Membres/rôles, transfert du dernier animateur, modération locale/globale, audiences croisées | Plus de risques d'accès et charge humaine ; effet blocage entre co-membres à définir | Préférable seulement si segment B dépend de cette valeur |
| C — profils fondateurs publics et liens choisis | Point d'entrée simple pour annonces | Curation manuelle, consentement et charge par 19/09 | Substitut incomplet ; jamais présenté comme communauté privée | Alternative de découverte, pas équivalent à B |

**Objectif :** cohérence et valeur du pilote ; **problème :** ajout de groupes sans moyen de les gouverner. **Solution candidate :** A plus découverte simple C. **Alternatives :** B non rejetée, sous étude. **Impact business :** A peut réduire différenciation, B accroît besoins humains ; aucun budget accepté. **Impact technique :** A réduit membership et pouvoirs locaux, B modifie données/contrats/audiences. **Dépendances :** 19/09/10/03/04/14/15/02. **Priorité :** P0 pour arbitrage. **Réexamen :** besoin collectif prouvé, moyens disponibles et recette J07 définie. **Autorité :** HQ, avis spécialisés ; statut PROPOSÉ.

DEC-0002 doit aussi décider FEAT-018, notifications minimales, public/privé, règle d'édition et inclusion FEAT-019/022. Les objectifs de simplicité ne dispensent pas des droits, médias sûrs, modération, recours ou opérations nécessaires.

## 8. Écarts des travaux précédents et questions ciblées

| Référence précédente → entrée GitHub | Écart | Traitement dans ce livrable / owner |
| --- | --- | --- |
| Ancien M0 : communautés Phase 2 → catalogue FEAT-020 MVP conditionnel | Proposition Produit plus étroite | Garder les deux options visibles ; OPEN-003 / DEC-0002 HQ |
| Ancien M0 : recherche arbitrable MVP → FEAT-023 Phase 2 | Divergence de phase | Suivre Phase 2 candidate ; liens/découverte sobre au pilote ; réexamen HQ si besoin attesté |
| Ancien M0 : notifications à arbitrer → FEAT-011 MVP P1 | Divergence de phase et scope | Centre interne minimal proposé MVP, aucun push ; avis 02/04/15 et HQ |
| Ancien M0 : messages Phase 3, ads/paiements Long terme → FEAT-024 Phase 2 et FEAT-030/031 Phase 3 | Classement ancien divergent | Utiliser classement HQ comme candidat ; aucune avancée de réalisation ; owners 11/12/15/07 |
| Ancien référentiel : vidéo MVP → FEAT-026 Phase 2 | Ancienne vision trop large pour pilote | Image seulement au noyau ; vidéo Phase 2 candidate |
| Ancien M0 : absence d'accès absolue après blocage → J04 demande limites expliquées | Assurance excessive sur contenu public/anonymat | Révoquer les actions définies, expliquer copies/visiteurs ; OPEN-007, 09/14/15 |
| Stack déclarée « actuelle » en discussion → OPEN-005 et mandats disent proposée | Preuve d'adoption non reçue | Aucune stack officialisée ici ; arbitrage 03/HQ |
| Travail Produit en discussion → tableau HQ « NON REÇU » au SHA d'entrée | Dossier HQ antérieur à contribution publiée | Ce fichier est la réponse spécialisée ; HQ met à jour réception après lecture, pas par déduction |

Les owners répondent sur ces deltas, pas par relecture de toutes les conversations. Pays, âge, langue, surface, budget et effectifs restent À VÉRIFIER ; aucune réponse d'autre équipe n'est présumée.

## 9. Mesures, risques et transmissions

### Mesure candidate — owner 13 avec 15/19

Activation : part de comptes de cohorte effectuant une action choisie (suivre/publier/commenter) dans une fenêtre à définir ; distinguer premier suivi puis première lecture et comptes sans contenu. Retour volontaire : part de cohortes revenant pour action utile, avec question qualitative sur sa raison ; aucun temps de session maximal comme objectif. Conversation : part de publications admissibles recevant réponse d'un autre compte, fenêtre et exclusions à fixer. Contre-mesures : masquages, blocages, signalements, erreurs d'audience, charge de modération, satisfaction et coût observé. Mesurer délai par gravité, stock, recours et corrections ; zéro signalement ne démontre pas sécurité. Cibles chiffrées NON REÇUES, aucune collecte mise en œuvre.

### Transmissions ciblées — toutes À TRANSMETTRE

INT-0001 est reçu par cette équipe via le mandat actuel ; la réception par HQ de cette réponse reste à établir. Les références ci-dessous utilisent les IDs existants OPEN/INT/FEAT ; aucune nouvelle série INT concurrente n'est créée.

| Cible / référence | Question ou action précise | Livrable attendu | Blocage réel |
| --- | --- | --- | --- |
| HQ, DEC-0001/0002, OPEN-001/002/003/006 | Choisir segment/surface/communautés et moyens ; lire §2/7/8 seulement | Arbitrage documenté + périmètre des avis | Fige MVP, pas rédaction indépendante |
| 19, INT-0001, FEAT-005/020 | A ou B : pourquoi revenir, qui produit premiers contenus, quel besoin manque sans communauté ? | Recherche pilote, recrutement et proposition de contenu consenti | Validation de valeur et ouverture utile |
| 02, INT-0002, J01–J06, FEAT-022 | Concevoir audience, fil vide/fin, reprise, suspension/recours et sorties accessibles | Flows et maquettes d'états | Ready des interfaces |
| 03/04, INT-0003, FEAT-004–010 | Aligner transitions, contrat d'édition, retry, accès direct et pagination | Contrats et invariants candidats révisés par consommateurs | Implémentation du lot social |
| 08, FEAT-007, J02 | Quand image devient lisible et comment retrait durant traitement révoque dérivés ? | Lifecycle, limites et schéma de reprise | Image du MVP |
| 09/10, INT-0004, FEAT-012–017 | Définir blocage, triage, sanctions, décision effective, recours sous suspension, capacité humaine | Politique, workflow, matrice rôles/actions et plan humain | Publication pilote UGC |
| 14/15, INT-0005, OPEN-004/007 | Valider âge/admissibilité, visibilité, sessions, données/export/retrait et sauvegardes | Matrice d'accès/cycle et analyse ciblée | Lots avec accès et données, pas recherche des segments |
| 16, INT-0009, FEAT-021/032 | Définir langues de service versus langues de contenu et pays réellement ouverts | Matrice langue/support/modération/pays | Ouverture et traduction des parcours |
| 13, FEAT-019 | Valider dictionnaire minimisé, fenêtres/dénominateurs, exclusions et contre-métriques §9 | Schémas d'événements et protocole pilote | Mesure, sans bloquer prototypes UX |
| 05/06, OPEN-002, FEAT-018/025 | Comparer faisabilité web responsive/PWA/natif pour J01–J06, sans promesse de plateforme | Écarts, contraintes et effort à vérifier | Arbitrage surface |
| 07, FEAT-008/029 | Définir fil déterministe et découverte sans IA ; ne pas exiger données pour modèle futur | Fallback et règles d'éligibilité | Contrat fil, pas IA future |
| 18, INT-0008 | Mapper 31 critères AC-J existants et 22 AC-PROD aux tests, erreurs/charge/recovery | Plan de recette référencé avec préconditions | Validation pilote |
| 17/20/21, INT-0010/0006/0007 | Examiner delta de ce fichier, collisions IDs, intégration avec PR #2 et statut de revue | Index/réception par HQ, revue et preuves de checks | Fusion et Ready, pas analyse Produit |

### Risques rattachés au registre existant

| Risque existant | Impact du delta Produit | Mesure et owner |
| --- | --- | --- |
| RISK-0001 | Catalogue/anciens MVP pris pour promesse, fonctionnalités sans ID ou phase | Classification explicite, options visibles et arbitrage HQ/01/17 |
| RISK-0002 | Modération/recours non opérables, blocage promettant invisibilité absolue | Pas ouverture UGC sans moyens 09/10 ; matrice et messages 14/15 |
| RISK-0003 | Traduction confondue avec marché juridiquement et humainement prêt | Pays/langues/âge/support par 15/16/19 avant DEC-0001 |
| RISK-0004 | Divergence des états/audiences/media entre clients et services | §5 puis contrats communs 03/04/08/14 et recette 18 |

Autres constats à enregistrer par HQ si nécessaires : fil vide empêchant preuve de valeur, capacité multi-support non estimée, métriques sensibles et confusion suivi social/paiement. Effort/coût/probabilité non mesurés. Les mesures proposées sont recrutement de fondateurs, comparaison de supports, minimisation et vocabulaire explicite.

## 10. Acceptation documentaire et compte rendu

Ce livrable couvre les deux segments demandés par INT-0001, les 34 FEAT du catalogue, les parcours nominaux/erreurs du pilote, les permissions/données/interfaces candidates, les alternatives et les critères complémentaires. Les contrats manquants indiquent leur owner et le lot bloqué. Il ne remplace pas les spécifications UX/API/Media/Privacy/Trust et ne les approuve pas.

1. **Décisions prises / à valider :** localement, réutilisation FEAT/J/AC et séparation suivi social/abonnements payants ; propositions DEC-0001/0002, public/privé et interfaces encore en revue. Aucun choix de stack, fournisseur, permission ou phase approuvé par Produit.
2. **Livrable / publication :** `documentation/product/mvp-specification.md` v0.2, delta DIR-012 sur la réponse M0-TEAM-01. Référence d'entrée exacte en §1 ; publication par branche/PR à documenter dans le compte rendu de livraison, aucune fusion annoncée par ce texte.
3. **Vérification :** critères AC-J/AC-PROD PLANNED ; aucun test applicatif exécuté. Contrôles documentaires et éventuelle CI rapportés avec leurs preuves dans la PR ; ils ne prouvent pas les parcours.
4. **Questions :** OPEN-001 à OPEN-007 ; segment/recrutement, âge/pays/langues, web/mobile, communautés, moyens, audience et cycle des données ; reviewers OPEN-008 à nommer par HQ.
5. **Dépendances :** §9 ; toutes transmissions vers autres discussions À TRANSMETTRE. Publication GitHub n'établit pas lecture/acceptation par chaque équipe.
6. **Risques :** RISK-0001 à 0004, fil vide, faux sentiment de contrôle et coûts non évalués ; limites et mitigations ci-dessus.
7. **Suite / HQ :** lire le delta §2/3/7/8 ; enregistrer options et avis, demander revues ciblées, décider public/pays puis MVP, compléter contrats/UX/recette des lots retenus, enfin autoriser implémentation. La rédaction peut progresser sans attendre un module reporté.
