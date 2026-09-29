# Plan de lancement pilote — Growth / M0

**Delta DIR-012 — 30 septembre 2026 :** positionnement universel et priorités marketing confirmés par le porteur, intégrés par 21. Les propositions opérationnelles de 19 restent à examiner ; aucune campagne, aucun contact ni recrutement lancé. Les contrôles du rapport de v0.2 restent historiques.

## Identification et statut

| Champ | Valeur |
| --- | --- |
| Référence | GROWTH-M0-001, révision 0.3 ; delta de positionnement sur la contribution 0.2 |
| Objectif | Préparer un pilote utile et soutenable, comparer les options de recrutement et fournir des critères de suspension ou d'élargissement |
| Propriétaire | 19 — Growth / Lancement / Communauté ; aucun responsable humain ou compte reviewer confirmé |
| Destinataires | 00, 01, 02, 03, 04, 05, 09, 10, 12, 13, 14, 15, 16, 17, 18 et 21 selon les demandes ciblées de ce document |
| Date / référence | 29 septembre 2026 ; PR #2, branche documentation/m0-team-coordination, commit dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957 |
| Statut documentaire | PROPOSÉ — avis Growth ; décisions transversales et revues spécialisées attendues |
| Classement | Préparation M0 d'un MVP candidat ; prolongements Phase 2, Phase 3, International et Long terme explicités plus bas |
| Priorité | P0 : éviter un pilote vide ou une ouverture sans capacité humaine ; P1 : mesure et acquisition répétable |
| Périmètre | Hypothèses de valeur, recrutement, cohortes, animation, assistance, mesure, capacité, coûts internes et arrêt/élargissement |
| Exclusions | Autorisation de contacter des personnes, collecte effective, campagne, application, choix de stack/fournisseur, paiement, publication marketing et ouverture de pays |
| Blocages principaux | INT-1901 à INT-1907 avant l'ouverture concernée ; réponses et approbations NON REÇUES dans ce dossier |
| Réalisation | Document rédigé ; aucun recrutement réalisé, aucune campagne envoyée, aucun test applicatif exécuté par ce travail |

### Références d'entrée

- [PR #2](https://github.com/yyogas/social-network/pull/2), examinée au commit ci-dessus ; PR ouverte à la lecture, elle dépend de la PR #1 et n'est pas une baseline approuvée.
- [Mandat M0-TEAM-19](../teams/work-orders.md), [plan documentaire](../documentation-plan.md), [modèle de livrable](../teams/deliverable-template.md).
- [Vision](../product/product-vision.md), [catalogue FEAT](../product/feature-catalog.md), [parcours J01–J07](../product/user-journeys.md).
- [Gouvernance](../governance.md), [registre HQ](../project-governance/decision-register.md), [coordination](../project-governance/coordination-board.md), [roadmap](../project-governance/global-roadmap.md), [stratégie QA](../quality/test-strategy.md).
- Brouillon GROWTH-M0-001 v0.1 visible dans cette discussion : réutilisé pour la boucle contenu/participation et les dépendances. Pas de copie brute de conversation ni de données de participants dans Git.

Les IDs REQ-1901 à REQ-1911, INT-1901 à INT-1909, RISK-1901 à RISK-1906 et TEST-1901 à TEST-1918 sont proposés pour cette contribution ; aucune occurrence préexistante dans l'instantané examiné. 00/17 doivent recontrôler les collisions entre PR concurrentes. Les FEAT existants conservent leur autorité ; un REQ précise un besoin Growth et ne crée pas une fonctionnalité approuvée.

### Nature des affirmations et delta depuis v0.1

| Nature | Élément et preuve / limite |
| --- | --- |
| CONFIRMÉ | Mandat documentaire reçu de l'utilisateur ; propriétaire 19 et chemin du livrable confirmés par M0-TEAM-19 |
| CONFIRMÉ | Public universel, peuple kabyle inclus, et priorités marketing : DIR-012 remplace DIR-002 sur instruction du porteur du 30 septembre 2026 |
| CONFIRMÉ | Pays, langues, âge, visibilité, communautés et MVP restent à arbitrer : OPEN-001/003/004/007, DEC-0001/0002 encore attendues |
| PROPOSÉ | Scénarios 40 puis 100 participants, recrutement manuel, seuils, calendrier, règles Growth, permissions et données ci-dessous |
| À VÉRIFIER | Besoin récurrent, disponibilité des animateurs, adhésion des créateurs sans rémunération, capacité opérationnelle, faisabilité de la mesure et coûts réels |
| NON REÇU | Entretiens, accords de partenaires, budget, roster humain, autorisation d'ouverture, contrats d'accès/invitation/mesure, décisions pays/âge et validations QA spécialisées |

Les propositions antérieures de 20–30 partenaires et de séquence sur 90 jours deviennent des options pour un élargissement ultérieur. Elles ne sont pas des prérequis automatiques du petit pilote. Les paliers de 1 000 à 10 millions restent des horizons, sans prévision ni date promise.

## 1. Besoin, contribution indispensable et options du pilote

### 1.1 Valeur à tester

Hypothèse : une personne rejoint un petit réseau parce qu'elle y retrouve un rendez-vous utile et des interlocuteurs qui répondent, avec un contrôle compréhensible de son audience. Proposition de promesse à tester avec 01 : « Retrouvez un petit cercle actif pour partager et échanger autour de vos centres d'intérêt. » Aucun message public n'est diffusé par ce document.

Growth prépare les premiers interlocuteurs et contenus, accompagne l'accueil, recueille les difficultés, distingue participation volontaire et participation suscitée par l'équipe, puis recommande poursuivre, corriger, suspendre ou élargir. Les bénévoles et créateurs n'acquièrent aucun pouvoir de modération du seul fait de leur rôle d'animation.

### 1.2 Deux segments proposés, sans liste nominative

| Segment | Besoin hypothétique | Proposition pilote | Canaux à examiner après autorisation | Critère de sélection / risque |
| --- | --- | --- | --- | --- |
| A — Animateurs associatifs, étudiants et membres de cercles locaux | Partager des ressources et retrouver un échange récurrent | Rendez-vous hebdomadaire et entraide par texte/image | Canaux détenus par les associations, bureaux étudiants, relais d'événements | Au moins un animateur et un suppléant disponibles ; éviter un cercle limité aux proches de l'équipe |
| B — Créateurs culturels, artistes et lecteurs | Recevoir des réponses compréhensibles autour d'un contenu original | Petite série éditoriale et temps de réponse annoncé | Canaux propres des créateurs, artistes, médias et entrepreneurs partenaires | Capacité de publier sans promesse de paiement ; dépendance à une célébrité à éviter |

Les médias et entrepreneurs sont des relais possibles, pas des pages professionnelles promises au MVP. Un événement peut être évoqué dans une publication autorisée ; aucune billetterie, inscription native à un événement ou fonction de calendrier n'est induite. Aucun scraping de membres, import de carnet d'adresses ou sélection automatique par origine n'est proposé.

Protocole de recherche candidat : 8 entretiens, 4 par segment, après autorisation spécifique et modalités validées par 15. Questions : dernier besoin concret ; solution actuelle ; moment où un petit réseau serait utile ; raison de revenir ; audience acceptable ; langues d'aide nécessaires ; difficultés de connexion ; raisons d'arrêter. Les notes sont synthétisées en besoins et objections sans coordonnées, origine déduite ni verbatim identifiant dans Git. Cet échantillon sert à découvrir des problèmes, pas à représenter toute la population mondiale ou tous les marchés prioritaires.

### Priorités marketing reçues — distinctes du lancement

**CONFIRMÉ :** pays prioritaires : États-Unis, Canada, Inde, France, Allemagne, Royaume-Uni, Japon, Chine, Brésil, Argentine, Colombie, Mexique, Algérie, Maroc, Afrique du Sud, Espagne et Australie. Régions ou ensembles prioritaires : Kabylie, monde arabe et Asie. La portée reste mondiale, y compris les publics non cités ; aucun classement entre ces priorités n'est imposé. Source : [DIR-012](../project-governance/decision-register.md).

**PROPOSÉ pour 19/01/16 :** préparer pour chaque marché étudié une fiche besoin/segment d'usage, canaux contextuels ou partenaires volontaires, langues à qualifier, messages, hypothèse de coût et mesure de résultat. Comparer ces fiches avant de proposer vagues et budgets au HQ. Ne pas inférer une origine depuis une langue, un lieu, un abonnement ou une région marketing. L'acquisition marketing du réseau n'active pas la fonctionnalité de publicité intégrée FEAT-030.

**À VÉRIFIER / NON REÇU :** taille et besoins des segments, disponibilité du service, localisation, support/modération, avis pays, moyens et calendrier. Cette liste autorise la préparation documentaire ; les campagnes, dépenses et contacts exigent leur autorisation propre. La cohorte ne reste pas implicitement limitée à la France ou à un groupe culturel.

### 1.3 Comparaison structurante à soumettre à DEC-0002 / OPEN-003

| Option | Produit nécessaire | Bénéfice Growth | Coût / risque | Avis Growth |
| --- | --- | --- | --- | --- |
| A — Cercles animés autour des abonnements | FEAT-005, FEAT-006/007, FEAT-008/010 ; sélection explicite de personnes à suivre | Apprendre avec le noyau candidat sans gouvernance de groupe supplémentaire | Pas d'espace privé collectif ; risque de confusion sur « communauté » et davantage d'accueil manuel | Recommandée pour le premier test si les besoins n'exigent pas une audience collective fermée |
| B — Communautés intégrées dès le pilote | FEAT-020, J07, adhésion, rôles, départ, fermeture, modération locale/globale | Espace et rendez-vous identifiables ; valeur possible pour les associations | Contrats de permissions, gestion du dernier responsable et charge de revue supplémentaires | À retenir si 01 établit que l'espace collectif est indispensable et si 04/09/14/15/18 valident les prérequis |

Les abonnements ne simulent pas une communauté privée. Si la confidentialité collective est indispensable, l'option A ne convient pas à ce segment ; adapter le segment ou attendre l'option B. Le pilote communautaire au sens social n'implique pas l'activation de FEAT-020.

## 2. Besoins et fonctionnalités classés

Toutes les phases et priorités de cette table sont PROPOSÉES. « MVP » signifie candidat nécessaire au scénario concerné, avec dépendances explicites.

| Besoin | FEAT / parcours liés | Acteur, problème et résultat attendu | Phase / priorité | Préconditions / critère de succès |
| --- | --- | --- | --- | --- |
| REQ-1901 — Préparer l'offre initiale | FEAT-006/007/010, J02/J03 | Animateur/créateur : éviter un accueil vide ; disposer de contenus et de répondants | MVP / P0 | Auteurs volontaires, audience et règles connues ; 3 publications de départ par cercle et un rendez-vous documenté, cible à tester |
| REQ-1902 — Accueil et première participation | FEAT-001/003/004/005/008/010/021/022, J01/J03 ; FEAT-020/J07 conditionnels | Nouveau membre : comprendre quoi faire et qui peut le lire | MVP / P0 | Langues et admissibilité décidées ; choix explicite de suivre/rejoindre, possibilité de passer ou quitter ; AC-G19-01/02 |
| REQ-1903 — Accès pilote par lien | FEAT-001/004/012 ; extension à examiner par 01/04/14/15 | Invité : accéder à la bonne cohorte sans obtenir de droits indus | MVP / P1, seulement si accès fermé retenu | Contrat d'admission validé ; lien expiré/révoqué compréhensible et aucune adhésion ni permission implicite ; AC-G19-03/04 |
| REQ-1904 — Partage externe contrôlé | FEAT-004/006/007/012/014/018, J02/J03 | Membre/visiteur : découvrir un contenu partageable sans fuite | Phase 2 / P1 par défaut ; contenu public au MVP à arbitrer | Pages anonymes et aperçus absents du contrat reçu ; permissions, retrait et caches définis avant boucle publique ; AC-G19-05/06 |
| REQ-1905 — Animation et retour volontaire | FEAT-006/008/010/011/022, J03 | Membre : retrouver un échange récurrent | MVP / P1 | Formats éditoriaux simples ; aucune relance individuelle ni notification additionnelle automatique ; AC-G19-07 |
| REQ-1906 — Retours et assistance | FEAT-013/015/016/017, J04–J06 | Participant/opérateur : distinguer question produit, incident, recours et demande de droits | MVP / P0 | Point d'assistance validé par 10 ; remontée sensible vers 09/15, visibilité limitée ; AC-G19-08/09 |
| REQ-1907 — Cohortes et mesure minimale | FEAT-019 ; J01/J03 | Growth/Produit : décider sur activation, retour, qualité et capacité | MVP / P1 | Définitions 13 et conditions de collecte 15 approuvées ; compter les dénominateurs et la maturité des cohortes ; AC-G19-10/11/12 |
| REQ-1908 — Ambassadeurs et contenu de découverte | FEAT-021/027/028 ; extension éditoriale à examiner | Relais : reproduire l'accueil et rendre les contenus publics utiles trouvables | Phase 2 / P2 | Deux cohortes exploitables, formation, responsabilités et pages publiques validées ; mandat révocable sans privilèges implicites |
| REQ-1909 — Parrainage avec avantages | FEAT-019/031 ; besoin additionnel à cataloguer par 01 | Parrain/filleul : comprendre conditions, abus et éventuel avantage | Phase 3 / P2 | Business, privacy, fraude, règles de contestation et coûts validés ; aucune récompense sur simple inscription ; tests à spécifier avant phase |
| REQ-1910 — Ouverture par marché | FEAT-032 | Membres/relais locaux : disposer d'une expérience et d'un recours opérables | International / P1 | Matrice pays/langues/support/modération et décision d'ouverture spécifique ; AC-G19-17 |
| REQ-1911 — Expansion aux grands paliers | FEAT-032/034 selon les décisions futures | HQ/opérations : soutenir un réseau beaucoup plus vaste | Long terme / P3 | Rétention, économie et capacité démontrées par marché ; pas de passage automatique au franchissement d'un compteur |

REQ-1903/1904/1908/1909 signalent des besoins insuffisamment couverts par le catalogue actuel. 01 attribuera un nouveau FEAT uniquement si une fonctionnalité distincte est retenue. Cette table ne renumérote pas le catalogue. Acquisition payante et outils Ads ne sont pas nécessaires au pilote proposé.

## 3. Parcours, états, transitions et erreurs

### 3.1 Parcours opérationnel nominal

1. HQ valide la fiche pilote : segment, périmètre, accès, budget maximal, rôles humains et fenêtre d'ouverture.
2. Après autorisation spécifique de prise de contact, Growth recrute les animateurs volontaires et documente leurs engagements réels. Ils préparent leurs contenus sous les règles normales d'audience et de modération.
3. Une personne reçoit volontairement une information ou un lien, consulte les informations d'accès, puis choisit de s'inscrire. L'accès pilote, l'activation du compte et la permission de lire un contenu sont trois contrôles distincts.
4. Après J01, l'accueil propose quelques interlocuteurs sélectionnés manuellement ou une communauté disponible si FEAT-020 est retenue. Rien n'est suivi/rejoint automatiquement ; aucun contenu fictif n'est présenté comme une activité réelle.
5. La personne lit un fil accessible, choisit de contribuer ou simplement de lire. Un animateur répond dans ses créneaux annoncés. Une réponse d'équipe est distinguée d'un échange spontané dans l'évaluation.
6. Le retour vient d'une série ou d'un rendez-vous utile. Préférences de notification, désabonnement, blocage, sortie et suppression restent accessibles.
7. Growth examine les agrégats et retours autorisés avec 01/13 ; 09/10/14 communiquent une synthèse opérationnelle. HQ décide maintien, correction, suspension ou élargissement.

### 3.2 États et transitions proposés

| Objet | États et déclencheur | Annulation / reprise / limites |
| --- | --- | --- |
| Cohorte | BROUILLON → PRÊTE APRÈS REVUES → OUVERTE → OBSERVATION → DÉCISION ; OUVERTE → ACQUISITION SUSPENDUE sur alerte | Suspendre les nouveaux entrants ne supprime pas les comptes existants. Reprise après décision documentée et confirmation des propriétaires concernés |
| Relation partenaire opérationnelle | À ÉVALUER → CONTACT AUTORISÉ → CONTACTÉ → ACCORD EXPLICITE → PRÊT → ACTIF ; RETIRÉ possible | Aucun état CONTACTÉ/ACCORD sans preuve hors Git au stockage approuvé. Retrait stoppe les sollicitations selon les modalités approuvées, sans sanction de compte |
| Accès par lien, si retenu | ACTIF → UTILISÉ, EXPIRÉ ou RÉVOQUÉ ; quota épuisé si lien collectif approuvé | Le type de lien et sa limite sont ouverts. Une reprise réseau retourne le résultat existant ; expiration/révocation ne modifie pas silencieusement une inscription achevée |
| Accueil | CHARGEMENT → PROPOSITIONS ou VIDE ; choix utilisateur → CONFIRMÉ ; ERREUR ou INDISPONIBLE | Continuer sans suggestion est possible si les autres conditions d'accès sont réunies ; une panne de suggestions n'interdit pas de quitter l'accueil |
| Contenu d'accueil | BROUILLON → PUBLIÉ selon J02 ; RESTREINT, RETIRÉ ou AUTEUR SUSPENDU selon les contrats | Retirer le contenu des sélections et aperçus concernés ; ne pas remettre automatiquement une copie hors ligne à disposition |
| Retour opérationnel | REÇU → TRIÉ → ORIENTÉ → TRAITÉ selon contrat 10 ; EN ATTENTE si réponse spécialisée nécessaire | Un accusé ne promet pas une résolution. Un signalement ou recours garde son dossier et son autorité 09/10 |

Ces états décrivent des besoins observables, pas des tables ou enums backend approuvés.

### 3.3 Erreurs et cas limites

| Raison métier provisoire | Réponse utilisateur et récupération | Trace minimale / destinataire |
| --- | --- | --- |
| Lien invalide, expiré, révoqué ou quota atteint | Message neutre ; moyen d'assistance approuvé si disponible ; aucune ouverture forcée | Résultat et corrélation technique selon 04/14 ; jamais le jeton d'invitation |
| Déjà inscrit / lien consommé / double clic | Connexion ou reprise sûre sans révéler l'existence du compte à un tiers ; une seule admission | Résultat dédupliqué ; contrat 04/14 à définir |
| Admissibilité non satisfaite | Refus selon politique 15 et parcours 02 ; aucune incitation à déclarer un autre âge ou pays | Motif limité aux rôles autorisés ; données Growth agrégées seulement |
| Réseau perdu ou résultat inconnu | État en attente puis vérification du résultat ; ne pas annoncer « rejoint » avant confirmation | Identifiant de requête approuvé, sans contenu personnel |
| Fil vide / animateur absent | Explication factuelle, choix alternatif autorisé ou possibilité de revenir plus tard | Problème d'offre de contenu pour 19/01 ; pas de faux abonnements ni comptes d'animation déguisés |
| Contenu retiré / audience modifiée / blocage | Message d'indisponibilité sans extrait privé ni motif révélant une relation ; autorisation réévaluée au moment de l'accès | Échec d'accès pour 04/14, état éditorial minimal pour 19 |
| Communauté fermée / dernier responsable perdu | Aucun accès de secours inventé ; appliquer J07 et proposer assistance / départ selon contrat | Escalade 09/10 ; suspendre l'acquisition de cet espace |
| Mesure manquante, tardive ou supprimée | Afficher « données insuffisantes » et la fenêtre analysable ; ne pas remplacer par zéro ni reconstituer clandestinement | Statut de qualité et révision d'agrégat chez 13 |
| Signal de sécurité, harcèlement ou demande de droits dans un retour | Orienter vers canal approuvé 09/10/15 ; limiter copie et accès au strict dispositif validé | Référence de dossier protégée ; aucune accusation nominative dans Git ou dashboard Growth |

UX à faire examiner par 02/05/16 : libellés courts, langue disponible explicitement indiquée, choix « passer » et « quitter », navigation clavier, focus d'erreur, chargement et résultat annoncés aux aides techniques, confirmation de copie de lien sans prétendre que le destinataire l'a ouvert. Les textes publics, messages sensibles et formats de date attendent les validations spécialisées.

## 4. Permissions, données et contrats candidats

### 4.1 Matrice de permissions à faire valider

| Acteur | Action / ressource / portée proposée | Refus et limite |
| --- | --- | --- |
| Anonyme | Consulter les informations d'accès et, uniquement si approuvé, un contenu public | Un lien ne confère aucun accès à une audience restreinte, aux données de cohorte ou à la liste des participants |
| Membre admissible | Choisir ses abonnements/adhésions ; participer dans son audience ; copier un lien autorisé | Chaque action reste soumise aux règles de compte, de ressource et de blocage |
| Auteur / partenaire fondateur | Publier, retirer et décider du partage de ses propres contenus selon FEAT-004 | Le statut fondateur n'autorise ni visibilité publique forcée, ni modification d'autrui, ni contournement d'une sanction |
| Autre membre / personne bloquée | Accès selon matrice FEAT-004/012 examinée par les propriétaires | Aucun contournement par lien Growth, aperçu, cache ou suggestion ; Growth ne définit pas seul la portée du blocage anonyme |
| Compte suspendu / en suppression | Actions définies par 09/15 ; démarches de recours et droits via parcours approuvé | Aucune réactivation, nouvelle admission ou récompense décidée par Growth |
| Animateur / ambassadeur | Accueil éditorial avec les mêmes pouvoirs qu'un membre ; rôle local seulement si explicitement attribué | Aucun accès automatique aux signalements, données personnelles des invités ou pouvoirs globaux |
| Opérateur Growth | Gérer les opérations autorisées et consulter des agrégats approuvés, limités à son mandat | Aucun accès aux messages privés, contenus restreints, motifs détaillés de signalement, credentials ou graphe nominatif de parrainage |
| Support / modération / analyste | Actions propres aux contrats de 09/10/13/14/15 | Révocation effective des habilitations, refus côté service et audit des accès sensibles ; pas seulement masquage de bouton |

### 4.2 Données et cycle de vie proposés

Aucune donnée personnelle réelle n'est jointe. Aucun stockage, accès ou délai n'est approuvé par ce tableau. Les durées relèvent de 15 avec les propriétaires et doivent être connues avant collecte. Le dépôt contient uniquement protocole, décisions, exemples synthétiques et agrégats publiables revus.

| Catégorie / origine | Minimum envisagé et finalité | Accès / propriétaire / stockage proposé | Conservation, modification, export et suppression |
| --- | --- | --- | --- |
| Accord d'un partenaire volontaire | Alias interne, moyen de contact volontaire, disponibilité, preuve d'accord et langue d'échange choisie ; préparer l'animation | 19 et opérateurs désignés ; outil opérationnel à choisir avec 14/15, jamais Git | Durée et retrait à fixer par 15 avant contact ; rectification et demande de droits via 10/15 ; preuve d'opposition éventuelle limitée selon politique examinée |
| Cohorte analytique | Code de cohorte neutre, date d'activation, rôle analytique fondateur/membre/test et rattachement temporaire si nécessaire | 13 ; 19 reçoit les agrégats ; stockage et habilitations décidés par 04/14/15 | Pas de nom de communauté sensible ni origine dans le code ; rétention et effet de suppression sur agrégats à définir avant instrumentation |
| Attribution facultative | Code de canal générique autorisé, par exemple pilote-a ; finalité comparer les canaux | 13/15 ; éviter par défaut identifiant personnel du parrain, URL complète et empreinte d'appareil | Sans base/mécanisme validé, valeur « inconnue » ; absence d'attribution ne bloque pas l'inscription ; durée à arbitrer |
| Événements d'activation et retour | Type d'action, horodatage utile, identifiant technique seulement si approuvé ; aucune copie du texte, image, titre privé ou adresse réseau pour Growth | Produit 04, gouvernance 13/15 ; agrégats 19, accès pseudonymes non assimilés à anonymat | Déduplication, suppression, retard, changement d'audience et révision des résultats à contractualiser ; pas de collecte « au cas où » |
| Retours volontaires | Catégorie, obstacle, satisfaction facultative ; texte libre uniquement dans un canal autorisé | 10 pour triage ; synthèse expurgée vers 01/19 ; dossier sensible réservé à 09/15 | Relire les extraits avant partage ; suppression/export selon politiques du canal ; aucun enregistrement d'entretien par défaut |
| Santé opérationnelle / temps passé par équipe | Heures agrégées, créneaux couverts, volume de dossiers et dépassements de délais approuvés | 09/10/14 produisent ; 19 et HQ reçoivent synthèse sans preuves de dossier | Conserver le niveau nécessaire à la décision ; règles de rétention, petites cellules et droits à examiner |

Restauration : 04/14/15 doivent empêcher qu'une sauvegarde réactive une invitation révoquée, une sollicitation arrêtée ou un compte supprimé. Les journaux techniques ne servent pas de source de substitution pour une attribution ou une mesure non autorisée. Les coordonnées, tokens, cookies et contenus privés sont exclus des logs Growth.

### 4.3 Interfaces requises, au stade de besoins v0.1

Les références ci-dessous sont locales au livrable ; 04/13 attribueront les contrats canoniques. Aucun endpoint ou schéma de base n'est imposé. Les types et codes sont candidats, pas des erreurs API déjà existantes.

| Interface | Producteur → consommateur ; accès | Entrée / sortie minimales proposées | Résilience, contrôle et preuve attendue |
| --- | --- | --- | --- |
| I1 — Admission pilote, si accès fermé retenu | 04 → 05, futurs autres clients ; anonyme avant activation, vérifications d'admissibilité 14/15 | Entrée : preuve d'invitation opaque, données d'inscription du contrat FEAT-001 ; sortie : admissible / invalide / expiré / utilisé / révoqué, suite autorisée sans données de tiers | Validation d'expiration et portée côté service ; consommation atomique contre double usage ; même tentative = résultat cohérent ; timeout, quotas, clé de reprise et nombre de retries À DÉFINIR 04/14 avant code ; AC-G19-03/04 |
| I2 — Lecture depuis un lien et aperçu | 04/08 → 05, éventuellement système d'aperçu approuvé ; autorisation du lecteur réévaluée | Entrée : référence de ressource et contexte d'accès ; sortie : contenu/média autorisé ou indisponibilité neutre | GET sans effet d'adhésion ; restriction/retrait invalide la diffusion contrôlée ; délais de caches et timeout À DÉFINIR 04/08/14 ; ne pas promettre effacement des captures externes ; AC-G19-05/06 |
| I3 — Mesure minimale et agrégats | 04/05 → 13 ; 13 → 19/HQ via rôles approuvés | Événement candidat : id, version, type, date, cohorte et acteur technique si autorisé ; sortie agrégée : période, définition, N admissible, N résultat, exclusions, inconnus, maturité, qualité, assistance d'équipe | Type autorisé et minimisation ; producteur identifié, déduplication par événement, validation temporelle, événements tardifs et suppression ; panne analytique ne bloque pas l'action sociale ; transport, rétention, timeout/retry et agrégation à fixer par 13/04/15 ; AC-G19-10/11/12 |
| I4 — État opérationnel pour décision d'ouverture | 09/10/14 → 19/HQ ; échange manuel de rapport accepté pour M0 | Entrée : cohorte, fenêtre, plafond envisagé ; sortie : couverture humaine, état des incidents et tests, capacité et réserve, avis daté sans données de dossiers | État absent/périmé = non prêt à élargir ; cadence hebdomadaire proposée, alerte immédiate selon procédure incident ; timeout technique non applicable au rapport manuel ; AC-G19-14/15 |

Règles communes à instruire : version et date de définition visibles, corrélation technique sans identifiant public de participant, audit adapté au risque, compatibilité des consommateurs examinée avant retrait d'un champ. Une modification d'une métrique crée une nouvelle version et interdit de comparer silencieusement deux définitions. Les chiffres de timeout, retry, quotas et rétention manquants bloquent l'implémentation de l'interface concernée, pas la rédaction du protocole Growth.

## 5. Cohortes, moyens humains, coûts et calendrier conditionnel

### 5.1 Scénarios internes de dimensionnement

Estimations de travail PROPOSÉES, non mesurées, sans prix fournisseur ni promesse de recrutement. Le nombre de comptes est un plafond de préparation, pas une capacité technique démontrée. Les fondateurs et comptes de test sont suivis séparément des nouveaux membres dans les métriques.

| Élément | Scénario S1 — apprentissage | Scénario S2 — extension contrôlée |
| --- | --- | --- |
| Inscrits visés | 40 : 8 fondateurs/animateurs + 32 autres participants | 100 : 10 fondateurs/animateurs + 90 autres participants |
| Répartition proposée | Deux cercles d'intérêt, 4 fondateurs et 16 participants chacun | Trois cercles ; répartition à ajuster selon besoin et couverture humaine |
| Préparation éditoriale | 3 publications utiles par cercle ; 1 rendez-vous hebdomadaire ; réponses sur créneaux annoncés | Même principe, après vérification de la disponibilité par cercle |
| Admission par vague | 20 comptes maximum, puis revue d'accueil avant la vague suivante | Vagues de 25 maximum ; cadence décidée sur capacités et résultats |
| Préparation interne | 24 h : cadrage/recherche 8 h, préparation partenaires 8 h, supports d'accueil et coordination 8 h | 36 h : 12 h pour chaque poste ; delta réel à réestimer si S1 a déjà produit des supports |
| Exploitation hebdomadaire hypothétique | Growth 8 h ; animation 8 h ; support/modération 8 h ; Data/revue 2 h ; total 26 h | Growth 12 h ; animation 16 h ; support/modération 20 h ; Data/revue 4 h ; total 52 h |
| Sur quatre semaines d'ouverture | 24 + 4 × 26 = 128 h | 36 + 4 × 52 = 244 h |
| Valorisation purement interne à 40 €/h | 5 120 € ; réserve 25 % = 1 280 € ; enveloppe humaine illustrative 6 400 € | 9 760 € ; réserve 25 % = 2 440 € ; enveloppe humaine illustrative 12 200 € |

Le coefficient 40 €/h est une hypothèse de calcul, pas un tarif de marché, salaire, devis ou coût employeur validé. Une heure bénévole doit aussi être comptée ; elle n'est pas une ressource illimitée. Enveloppe totale = valorisation humaine + hébergement/médias + outils + éventuels frais participants/traduction/conseil + réserve adaptée. Ces postes supplémentaires sont NON REÇUS ; le total complet et toute autorisation de dépense restent ouverts avec HQ/14/15/16. S1 et S2 sont deux scénarios complets, pas des incréments à additionner automatiquement.

Les 8 h ou 20 h de support/modération représentent une estimation de charge, pas une amplitude garantie ni un engagement 24/7. 09/10 doivent établir un planning, un suppléant, le traitement des urgences et les limites visibles ; 14 son astreinte/exploitation selon le dispositif retenu. Sans cette couverture confirmée, les plafonds ci-dessus ne permettent pas l'ouverture.

### 5.2 Responsabilités à nommer avant ouverture

| Fonction | Responsable attendu / preuve | Limite |
| --- | --- | --- |
| Coordination pilote | 19 : personne et suppléant, créneaux, tableau de tâches | Ne valide pas pays, permissions ou levée d'incident |
| Animation de chaque cercle | Fondateurs volontaires : accord, disponibilité et remplaçant | Comptes identifiables comme animateurs ; pas de fausse activité organique |
| Support et modération | 09/10 : équipe habilitée, horaires et escalade ; 15 pour demandes de droits | Pas de transfert automatique aux ambassadeurs |
| Mesure et révision | 13 : propriétaire des définitions et qualité des données | Pas d'outil ni collecte choisi par Growth |
| Go / suspension / reprise | HQ après avis 01/09/10/14/15/18 concernés | Alerte Growth peut suspendre l'acquisition selon mandat d'urgence approuvé ; fermeture du service relève de la procédure incident |

### 5.3 Calendrier relatif, sans date de lancement

| Séquence | Travail | Condition de sortie |
| --- | --- | --- |
| Préparation M0 | Examiner ce dossier, conduire la recherche autorisée, choisir scénario et contrats | DEC-0001/0002 et responsables des prérequis identifiés ; pas d'engagement calendaire |
| Pré-ouverture | Autorisations de contact, partenaires, contenus, support, tests et information utilisateurs | Fiche de préparation signée par les autorités concernées ; exigences critiques résolues |
| Semaine 1 après ouverture autorisée | Première vague, accueil manuel et registre d'obstacles | Aucun blocage critique ouvert, charge réelle compatible avec le planning |
| Semaine 2 | Vague suivante si acceptable, analyse des premiers retours J7 | Plafond du scénario respecté ; garder la cohorte précédente identifiable dans les agrégats |
| Semaines 3–4 | Formats éditoriaux répétés, entretien volontaire de sortie, observation | Données interprétables, causes d'échec et coût humain recensés |
| À partir de la semaine 6 | Examiner la fenêtre J30 de chaque cohorte arrivée à maturité | Les personnes admises tardivement attendent leur propre fin de fenêtre ; décision HQ datée |

## 6. Mesures, seuils candidats et conditions d'arrêt

### 6.1 Définitions proposées à 13/01/15

L'origine de la cohorte est la date d'activation du compte, pas celle de l'envoi d'un lien. Les fenêtres sont en jours écoulés depuis cette activation, à contractualiser avec Data ; les tableaux présentent aussi la date limite des données et leur version. Les comptes de test, doublons confirmés et fraude confirmée suivent une règle d'exclusion documentée ; une simple suspicion ou un départ ne permet pas d'améliorer artificiellement le dénominateur. Suppression et maintien d'agrégats doivent rester conformes au cycle validé par 15.

| Mesure | Numérateur / dénominateur et fenêtre | Usage / limite |
| --- | --- | --- |
| Première interaction reçue A7 | Nouveaux membres ayant reçu au moins un commentaire autorisé d'un autre compte sur leur publication ou commentaire dans [0,7 jours) / tous les nouveaux membres admissibles dont les 7 jours sont écoulés | Indice d'accueil social ; afficher séparément réponses de fondateurs/opérateurs et réponses des autres membres ; ni auto-commentaire ni réaction seule |
| Retour contributif R7 | Nouveaux membres ayant publié ou commenté lors de [7,14 jours) / tous les nouveaux membres admissibles ayant 14 jours de recul | Ne pas conditionner le dénominateur à A7 ; ne mesure pas la valeur pour les lecteurs silencieux |
| Retour contributif R30 | Même action dans [28,35 jours) / tous les nouveaux membres admissibles ayant 35 jours de recul | Pas un résultat « J30 » calculable à quatre semaines ; résultats de cohortes immatures exclus et signalés |
| Réponses aux publications | Publications admissibles ayant reçu un commentaire d'autrui sous 48 h / publications admissibles ayant 48 h de recul | Compter l'unité publication ; montrer couverture par cercle et rôle du répondant ; ne pas inciter aux réponses artificielles |
| Retour qualitatif | Réponses volontaires déclarant une utilité et un contrôle compréhensible / réponses exploitables, avec nombre sollicité et non-réponses | Questions aux lecteurs et partants également ; biais de sélection explicite ; ne vaut pas un taux pour toute la cohorte |
| Charge et qualité | Heures opérateurs réellement consommées, capacité planifiée, incidents, dossiers hors délai approuvé, recours ouverts | Chiffres agrégés fournis par 09/10/14 ; une absence de signalements ne prouve pas la sécurité |
| Conversion d'acquisition facultative | Comptes attribuables / visites mesurables avec les mêmes règles et fenêtre approuvées | À définir uniquement si mesure visite permise ; sinon « inconnue ». Aucun assemblage de logs pour compléter les absents |

L'indicateur conversationnel d'« interaction utile » devient ici une hypothèse opérationnelle A7, complétée par l'enquête et les retours. Un commentaire détecté ne prouve ni utilité ni satisfaction ; 01/13/09 doivent accepter les exclusions avant d'en faire un KPI canonique. Les petites cellules par communauté ou canal sont masquées/agrégées selon le seuil que 13/15 auront validé.

### 6.2 Seuils d'apprentissage, pas benchmarks validés

Propositions pour comparer S1/S2 : A7 ≥ 50 %, R7 ≥ 30 %, R30 ≥ 20 %, et réponses sous 48 h sur ≥ 70 % des publications admissibles. Choix exploratoires de l'équipe, sans donnée historique ni prétention statistique ; à examiner avant mesure puis à versionner si modifiés. Montrer systématiquement les nombres et dénominateurs. Exemple fictif : avec 32 nouveaux membres tous arrivés à maturité, A7 exige au moins 16 personnes ; R7 au moins 10 ; R30 au moins 7.

| Décision proposée | Déclencheur observable | Action et autorité |
| --- | --- | --- |
| Ne pas ouvrir | Préconditions pays/âge/visibilité, revue QA ou couverture humaine manquantes | Maintenir préparation documentaire ; HQ obtient les avis requis |
| Suspendre l'acquisition concernée | Fuite plausible, contournement de blocage, abus critique sans prise en charge ou capacité indisponible | Alerter immédiatement 09/14/15 et HQ via canaux approuvés ; arrêter nouveaux contacts/admissions du périmètre selon mandat ; 09/14 instruisent l'incident |
| Réduire le débit | Deux revues hebdomadaires consécutives dépassent de plus de 20 % les heures planifiées, ou dépassement du plafond/délai opérationnel validé par 09/10 | Réduire/suspendre les vagues, recalculer capacité et coûts ; ne pas attendre deux semaines pour un risque critique |
| Corriger avant élargissement | Seuils de valeur manqués, ou réponses surtout produites par l'équipe, ou retours d'exclusion/visibilité incomprise | 01/19 formulent une correction et une nouvelle observation ; ne pas compenser par davantage d'acquisition |
| Données insuffisantes | Moins de 30 nouveaux membres à maturité sur une cohorte, collecte incomplète ou absence de mesure approuvée | Analyse qualitative et maintien du plafond ; aucune conclusion généralisée ni hausse automatique |
| Proposer élargissement | Deux cohortes examinées séparément, chacune ≥ 30 nouveaux membres matures pour les fenêtres utilisées ; seuils atteints ou écarts motivés ; capacité, qualité, coûts et avis spécialisés acceptables | Growth recommande ; HQ décide et fixe nouveau plafond. Un bon résultat quantitatif n'annule aucun blocage critique |
| Reprendre après suspension | Cause maîtrisée, exigences concernées revérifiées, couverture rétablie et décision datée | Avis 09/14/15/18 selon cause, puis HQ ; réouvrir par vague contrôlée |

S1 fournit une première cohorte d'apprentissage. Un S1 favorable peut justifier un deuxième test plafonné après décision HQ ; il ne suffit pas, seul, à autoriser l'acquisition ouverte. Les seuils de valeur restent ajustables sur preuve, jamais rétroactivement pour présenter un échec comme une réussite.

## 7. Horizons de croissance à réexaminer

Les paliers désignent des inscriptions cumulées ; ils ne déterminent pas le nombre d'actifs, la charge ou un calendrier. Les phases produit ne changent pas automatiquement à chaque palier.

| Horizon | Travail Growth envisagé | Preuve préalable / dépendance |
| --- | --- | --- |
| 1 000 | Reproduire le pilote dans quelques cercles ; envisager 20–30 partenaires fondateurs selon capacité ; deux canaux d'acquisition suivis | Cohortes matures, capacité de support/modération, coûts constatés et permissions validées |
| 10 000 | Ambassadeurs encadrés, calendrier éditorial, partage externe et contenu public utile si retenus | Acquisition de membres qui reviennent via plusieurs relais ; aucune dépendance excessive à une seule personnalité |
| 100 000 | Extension par villes/intérêts, outils créateurs et découverte selon phases approuvées | Qualité et coûts acceptables dans chaque nouveau cercle ; capacités techniques testées par 14/18 |
| 1 million | Organisation Growth et opérations par marché ; expériences mesurées | Gouvernance de données, revues locales, budgets et résilience démontrés |
| 10 millions | Accroître la disponibilité et la capacité dans le cadre du public universel DIR-012 | Chaque marché démontre une utilité, une viabilité et une capacité locale ; aucun marché total extrapolé depuis une seule cohorte |

Boucle publique future : contenu autorisé → partage → lecture permise → inscription choisie → échange → nouvelle contribution. Si les pages anonymes ne sont pas retenues au MVP, cette boucle reste différée ; le pilote utilise des relais et admissions encadrés. Le SEO de contenus publics dépend de cette décision et ne justifie pas de rendre des profils ou contenus privés indexables. L'invitation ne déclenche ni abonnement, ni notifications marketing, ni récompense automatique.

## 8. Acceptation et vérification à préparer avec 18

Tous les critères ci-dessous sont **PLANNED**. Les IDs TEST sont proposés, aucune exécution applicative ni expérience terrain n'est revendiquée. Données de test : comptes, contenus, langues et codes de cohorte synthétiques uniquement.

| Critère | Besoin / FEAT | Scénario et résultat observable | Test / type | Statut / dépendance |
| --- | --- | --- | --- | --- |
| AC-G19-01 | REQ-1902, FEAT-005/020 | Étant donné option A retenue, lorsque le nouveau membre passe l'accueil, alors aucune adhésion à une communauté inexistante ni abonnement non choisi n'est créé | TEST-1901 / E2E | PLANNED — 01/02/04/05 |
| AC-G19-02 | REQ-1902, FEAT-018/021 | Avec fil vide, langue approuvée et navigation clavier, l'utilisateur comprend l'état, peut choisir une suite et quitter sans focus perdu | TEST-1902 / accessibilité/E2E | PLANNED — 02/05/16 |
| AC-G19-03 | REQ-1903, FEAT-001 | Avec lien actif et deux soumissions simultanées, le nombre d'admissions respecte le quota contractuel et une reprise ne crée pas deux comptes | TEST-1903 / intégration | PLANNED — contrat 04/14 |
| AC-G19-04 | REQ-1903, FEAT-001/004 | Avec lien expiré/révoqué ou compte inadmissible, l'accès pilote échoue sans donnée de tiers ni contournement de politique | TEST-1904 / API/E2E | PLANNED — 04/14/15 |
| AC-G19-05 | REQ-1904, FEAT-004/007 | Après restriction d'audience, un ancien lien et ses aperçus/médias contrôlés ne livrent rien à un lecteur non autorisé selon les délais validés | TEST-1905 / intégration sécurité | PLANNED — 04/08/14/15 |
| AC-G19-06 | REQ-1904, FEAT-012/014 | Après retrait ou blocage, cliquer un lien ou une suggestion respecte l'interdiction applicable et ne réexpose pas un extrait privé | TEST-1906 / API/E2E | PLANNED — 09/04/14 |
| AC-G19-07 | REQ-1905, FEAT-011/022 | Avec notifications désactivées ou invitation refusée, aucun rappel Growth additionnel n'est envoyé et le retour manuel reste possible | TEST-1907 / intégration | PLANNED — 01/04/15 |
| AC-G19-08 | REQ-1906, FEAT-013/015/017 | Un retour contenant un incident est orienté vers le dossier habilité ; un opérateur Growth ne lit pas les preuves ni l'identité du signalant sans permission | TEST-1908 / permissions | PLANNED — 09/10/14 |
| AC-G19-09 | REQ-1906, FEAT-016 | Une demande de retrait/export suit son parcours ; une restauration ne réactive pas la sollicitation ni les accès révoqués selon la politique approuvée | TEST-1909 / intégration/reprise | PLANNED — 04/10/14/15 |
| AC-G19-10 | REQ-1907, FEAT-019 | Sur jeu synthétique incluant fondateurs/tests, événements dupliqués et cohortes immatures, les N, exclusions et fenêtres A7/R7/R30 correspondent au calcul documenté | TEST-1910 / données | PLANNED — 13/18 |
| AC-G19-11 | REQ-1907, FEAT-019 | Lorsqu'une mesure est interdite, manquante ou supprimée, l'inscription continue et le tableau indique inconnus/limites sans reconstruire depuis les logs | TEST-1911 / intégration privacy | PLANNED — 13/15/04 |
| AC-G19-12 | REQ-1907, FEAT-019 | Lorsqu'un opérateur Growth demande une petite cellule ou un détail personnel, l'agrégation/refus suit les seuils et droits approuvés | TEST-1912 / autorisation | PLANNED — 13/14/15 |
| AC-G19-13 | REQ-1901/1905, FEAT-006 | Avec un cercle sans animateur ou sans contenu prêt, la revue pré-ouverture identifie le manque et refuse la vague plutôt que d'afficher de faux contenus | TEST-1913 / exercice opérationnel | PLANNED — 19/01 |
| AC-G19-14 | REQ-1906/1907 | Lors d'un exercice d'incident critique, le relais nommé alerte les autorités, suspend l'acquisition concernée et conserve une décision de reprise séparée | TEST-1914 / exercice de crise | PLANNED — 09/10/14/19/HQ |
| AC-G19-15 | REQ-1907 | Avec une cohorte trop petite, immature ou une capacité non validée, la recommandation porte « données insuffisantes » ou « non prêt », même si les inscrits augmentent | TEST-1915 / exercice de décision | PLANNED — 13/19/HQ |
| AC-G19-16 | REQ-1901/1902, FEAT-020 | Si option B est retenue, perte du dernier responsable ou fermeture suit J07 ; Growth n'attribue pas un rôle de remplacement sans autorisation | TEST-1916 / intégration/opérations | PLANNED — 01/04/09/10 |
| AC-G19-17 | REQ-1910, FEAT-032 | Si une langue est traduite mais sans support/modération locale validés, la fiche marché n'autorise pas l'ouverture | TEST-1917 / revue opérationnelle | PLANNED — 09/15/16/HQ |
| AC-G19-18 | REQ-1901/1907 | Dans une simulation de coûts, toutes les heures y compris bénévoles et les coûts externes inconnus restent visibles ; l'enveloppe humaine ne devient pas le coût total du pilote | TEST-1918 / revue de scénario | PLANNED — 19/14/HQ |

Les contrôles réellement exécutés sur les fichiers figurent dans le [rapport documentaire](pilot-launch-validation.md). Ils ne remplacent aucun des tests ci-dessus.

## 9. Décisions importantes à instruire

### Contribution à DEC-0001 — Public et pays pilotes (NON APPROUVÉ)

- Objectif/problème : recruter des personnes partageant un besoin récurrent sans promettre huit ouvertures simultanées.
- Solution candidate : tester les segments A/B, puis choisir un seul périmètre d'ouverture opérable avec 15/16 ; France à comparer en premier comme hypothèse de proximité de la société, sans en déduire faisabilité juridique ou présence d'une équipe locale.
- Alternatives : plusieurs pays simultanés, segment créateurs seul, segment associatif seul. Aucune n'est rejetée officiellement ; la simultanéité augmente les prérequis de support et modération à instruire.
- Dépendances : INT-1901/1902/1903/1907 ; besoin, âge, langues, capacité et budget.
- Risques/impact business : échantillon biaisé, bassin limité, coût d'accueil ; améliore la possibilité d'apprentissage sans prévision d'acquisition.
- Impact technique : périmètre d'admissibilité et messages d'indisponibilité ; aucune géolocalisation ou règle de filtrage choisie ici.
- Priorité/phase/autorité : P0, MVP ; HQ après avis 01/09/15/16/19. Réexamen si les entretiens ou la disponibilité humaine contredisent les hypothèses.
- Delta demandé : compléter DEC-0001 et OPEN-001/004 avec segment, accès, pays ouverts, langues, politique d'âge, moyens et limites explicites.

### Contribution à DEC-0002 — Contrat MVP et mode de lancement (NON APPROUVÉ)

- Objectif/problème : obtenir une interaction récurrente sans exiger tacitement communautés, pages publiques ou invitations avancées.
- Solution candidate : option A et scénario S1 ; liens d'admission uniquement si un accès fermé est décidé ; partage public et ambassadeurs outillés différés par défaut.
- Alternatives : option B si besoin collectif fermé indispensable ; accès public immédiat ; pilote créateurs très réduit. Aucun rejet approuvé. L'accès public impose une capacité de modération différente à chiffrer.
- Dépendances : INT-1901/1903/1904/1905/1906 ; permissions, onboarding, mesure, tests et budget.
- Risques/impact business : plus d'accueil manuel, valeur communautaire potentiellement insuffisante ; 128 h et 6 400 € humains illustratifs pour S1, hors postes ouverts.
- Impact technique : préciser FEAT-020/J07 inclus ou différés ; définir admission et droits des liens si retenus ; aucune stack ajoutée.
- Priorité/phase/autorité : P0, MVP ; HQ avec 01/03/04/09/14/15/18/19. Réexamen si les utilisateurs exigent une audience collective ou si le coût manuel n'est pas soutenable.
- Delta demandé : inscrire option, capacités, exclusions, plafond, mesure et conditions d'arrêt ; examiner REQ-1903/1904 pour couverture du catalogue.

Les choix d'instrumentation/traitements de FEAT-019 restent des propositions 13/15 à soumettre au HQ en lien avec OPEN-007. Option minimale recommandée : agrégats autorisés et retours volontaires ; alternative : tracking individuel durable ou graphe de parrainage, non recommandé au pilote faute de nécessité démontrée. Impacts : granularité réduite mais moindre collecte ; coûts et rétention à instruire, pas de conformité juridique proclamée.

## 10. Dépendances, contradictions, risques et transmission

### 10.1 Demandes ciblées

Émetteur de toutes les demandes : **19**. État réel : **À TRANSMETTRE**, réponse **NON REÇUE**. La publication de la PR rend ce dossier consultable mais ne prouve pas sa lecture dans une autre discussion.

| ID / destinataire | Question et livrable attendu, delta à examiner | Bloque quoi ? |
| --- | --- | --- |
| INT-1901 — 00/01 | Examiner §1/2/9 ; choisir segment, option A/B, noyau et limite des liens ; fournir delta DEC-0001/0002 et couverture FEAT | Bloque finalisation du scénario et implémentation dépendante ; recherche documentaire continue |
| INT-1902 — 15/16 | Examiner §1/4/9 : pays effectivement ouverts, âge, langues et recrutement autorisé, données d'accord/contact/mesure et durées ; fournir matrice ciblée et modalités d'entretien | Bloque contact/collecte puis ouverture concernés, pas les hypothèses de coûts |
| INT-1903 — 09/10/14 | Examiner §3/5/6 : personnes, créneaux, suppléants, délais, capacité et suspension/reprise ; fournir fiche opérationnelle et escalade | Bloque ouverture et élargissement ; aucune permanence présumée |
| INT-1904 — 13 avec 01/15 | Examiner §4.2/4.3/6 : définitions A7/R7/R30, maturité, rôle fondateur, exclusions, effacement, petites cellules ; fournir delta au plan de mesure et contrat d'agrégats | Bloque instrumentation et verdict chiffré ; retours de besoin autorisés restent possibles |
| INT-1905 — 02/04/05 avec 08/14 | Examiner REQ-1902/1903/1904 et I1/I2 : accueil option A, invitation si retenue, erreurs et aperçus ; fournir parcours/contrats versionnés avec droits, limites et reprises | Bloque réalisation de ces fonctions, pas recrutement préparatoire autorisé |
| INT-1906 — 18/21 | Examiner les 18 critères §8, vérifications documentaires et préconditions ; fournir mapping QA et revue indépendante de la PR sur SHA précis | Bloque validation/fusion selon gouvernance et ouverture ; tous les tests applicatifs restent PLANNED |
| INT-1907 — HQ/14/12 | Examiner §5 : budget disponible, coût d'hébergement, temps humain et valeur créateur sans paiement ; fournir capacité et enveloppe acceptées, aucun devis supposé | Bloque engagement de moyens et ouverture ; pas les scénarios internes |
| INT-1908 — 17/HQ | Indexer le livrable et son SHA ; vérifier unicité des IDs, enregistrer seulement les faits de réception ; harmoniser les trois écarts ci-dessous | Non bloquant pour revue métier ; nécessaire avant consolidation canonique |
| INT-1909 — 16/19, puis 09/15 | Pour §7 seulement : préparer la fiche de chaque expansion et ses conditions ; distinguer pays de recrutement et disponibilité du service | Bloque future expansion, aucun blocage supplémentaire du petit pilote |

### 10.2 Contradictions et écarts à consigner au HQ

| Références | Écart / impact | Proposition de résolution et propriétaire |
| --- | --- | --- |
| Orientation historique DIR-002 remplacée par DIR-012 | Le premier ciblage communautaire ne représente plus le mandat ; risque de conserver un recrutement fondé sur cette ancienne entrée | Correction de positionnement v0.3 par 21 ; 01/19 proposent des segments d'usage, 16/15 qualifient disponibilité/langues ; périmètre pilote encore ouvert |
| Brouillon Growth v0.1 et tableau §2 du registre HQ vs FEAT-020 / J07 | Communautés présentées comme base naturelle alors que l'inclusion reste à arbitrer ; risque de développer des rôles non validés | Option A/B explicite ; 00/01/17 ajouteront la mention conditionnelle au résumé du registre s'ils la retiennent ; aucun changement du registre par Growth |
| Ancienne boucle publique/invitations vs catalogue FEAT-001/004/018 | Pas de contrat reçu pour pages publiques, liens d'admission, aperçus ou attribution ; promesse implicite de fonctionnalités | REQ-1903/1904 et I1/I2 ; 01 décide couverture ou nouvel ID. Différer la boucle publique si non retenue sans bloquer le pilote interne |

### 10.3 Registre de risques proposé

| ID | Risque / impact | Propriétaire et mesure proposée | État |
| --- | --- | --- | --- |
| RISK-1901 | Démarrage vide ou activité créée seulement par l'équipe : fausse validation de valeur | 19/01/13 : préparation éditoriale, distinguer répondants, entretiens lecteurs/partants et cohortes matures | OPEN, probabilité non mesurée |
| RISK-1902 | Exposition indirecte par liens, audiences, codes de communauté ou identité supposée : impact potentiellement critique | 04/14/15 avec 19 : aucune origine inférée, codes neutres, mêmes droits sur tous les accès et tests négatifs avant boucle publique | OPEN ; lié à OPEN-007 |
| RISK-1903 | Modération ou assistance indisponible sous croissance : incidents non traités | 09/10/14/HQ : couverture confirmée, limites annoncées, suspension ciblée ; reprend RISK-0002 sans le remplacer | OPEN ; bloque ouverture si non couvert |
| RISK-1904 | Biais d'échantillon, faible effectif et incitation à satisfaire le fondateur : mauvaise décision d'élargissement | 01/13/19 : deux segments, dénominateurs séparés, limites explicites et contrôle qualitatif | OPEN |
| RISK-1905 | Coûts humains/externe sous-estimés, bénévoles indisponibles, concentration sur un créateur | 19/HQ/12/14 : réserve, suppléants, coûts réels et plusieurs relais ; pas de récompense promise | OPEN |
| RISK-1906 | Pays/langue ou rémunération annoncés trop tôt : attentes impossibles à tenir | 15/16/12/19 : message d'accès validé, aucun engagement public avant décisions ; lié à RISK-0003 | OPEN |

## 11. Compte rendu de fin d'étape

1. **Décisions prises / à valider.** Décision locale : produire ce plan au chemin M0-TEAM-19 et réutiliser v0.1 avec correction de la cible confirmée. Option A, S1/S2, données, seuils et permissions restent PROPOSÉS. DEC-0001/0002 sont attendues du HQ ; aucun budget ou droit nouveau n'est approuvé.
2. **Livrables / références GitHub.** Ce plan v0.3 avec delta DIR-012, son index de domaine et le rapport de vérification historique v0.2 ; source initiale PR #2 au SHA dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957. La PR courante fournit les références effectives de publication et les commits de preuve ; sa création ne vaut ni fusion ni approbation spécialisée.
3. **Tests.** Voir le rapport documentaire pour les commandes réellement exécutées et leur portée. Les 18 scénarios ci-dessus sont PLANNED ; aucun test applicatif, entretien ni campagne exécuté par cette contribution.
4. **Questions ouvertes.** HQ/01 : option A/B et segment ; 15/16 : pays/âge/langues/collecte ; 09/10/14 : capacité ; 13 : métriques ; HQ : budget et responsables humains. Les effets bloquants sont limités aux opérations indiquées dans INT-1901 à INT-1909.
5. **Dépendances.** Demandes ciblées ci-dessus À TRANSMETTRE ; aucun avis spécialisé ni réception inter-discussions affirmé. Le tableau de coordination reste tenu par HQ.
6. **Risques / limites.** Six risques Growth ouverts, seuils et budgets hypothétiques, faible effectif, modèle opérationnel non testé ; pas d'affirmation juridique ni de capacité technique vérifiée.
7. **Suite / informations HQ.** Examiner les contributions à DEC-0001/0002, arbitrer OPEN-001/003/004/006/007, faire revoir uniquement les sections adressées aux équipes, puis autoriser séparément contact, collecte et ouverture. Après revue et fusion de #2, retargeter la PR Growth vers la base convenue et revérifier son diff et ses checks. Rollback documentaire : revert ciblé des ajouts après contrôle des contributions suivantes ; aucun effet runtime.
