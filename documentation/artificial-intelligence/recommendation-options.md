# IA / Recommandation / Hub — options et contrats candidats M0

## Identification et statut

| Champ | Valeur |
| --- | --- |
| Objectif | Définir la contribution 07 au pilote et les conditions d'activation ultérieure des moteurs |
| Propriétaire | 07 — IA / Recommandation / Hub ; aucun reviewer humain désigné |
| Destinataires | HQ, 01–05, 08–16, 18–21 selon les demandes ci-dessous |
| Date / révision | 2026-09-29 / v0.2 ; premier livrable 07 au format du dépôt |
| Référence GitHub | PR #2 ; branche documentation/m0-team-coordination ; SHA dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957 |
| Statut | PROPOSÉ — revue spécialisée et arbitrage HQ attendus ; aucune approbation d'implémentation |
| Priorité | P0 : éligibilité et chronologie ; P2 : recherche des usages différés |
| Dépendances bloquantes | Périmètre et communautés 01/HQ ; permissions 04/14/15 ; modération/âge 09/15 ; critères et budgets 13/14/18 |
| Périmètre | Chronologie, éligibilité, découverte, personnalisation, assistance et séparation des moteurs |
| Exclusions | Code applicatif, modèle entraîné, fournisseur, stack, schéma physique, engagement de coût ou de date |

Entrées lues : [mandat M0-TEAM-07](../teams/work-orders.md), [modèle](../teams/deliverable-template.md), [plan](../documentation-plan.md), [vision](../product/product-vision.md), [catalogue](../product/feature-catalog.md), [parcours](../product/user-journeys.md), [registre](../project-governance/decision-register.md), [stratégie QA](../quality/test-strategy.md), gouvernance et conventions. Les onze fichiers de cadrage relus par le connecteur ont été comparés à la copie locale par SHA de blob Git : identiques au SHA de référence. Main reste une structure antérieure ; la contribution dépend de #2, elle-même empilée sur #1.

### Nature des affirmations

- **CONFIRMÉ** par le mandat utilisateur : chronologie toujours accessible, recommandations explicables, commande « Pourquoi je vois ceci ? », réduction/exclusion de sujets, réinitialisation, protection renforcée des mineurs, minimisation des attributs sensibles et quatre responsabilités séparées.
- **CONFIRMÉ** : autorisation de travail documentaire M0 ; elle n'autorise pas le MVP, une stack, des traitements de données ou un modèle économique.
- **PROPOSÉ** : toutes les phases, règles détaillées, interfaces, durées et options de ce document, sauf principes explicitement confirmés ci-dessus.
- **À VÉRIFIER** : utilité des recommandations pour le public pilote, qualité linguistique, performance, coût, capacité de modération et validité des politiques.
- **NON REÇU dans les entrées examinées** : contrats approuvés, données d'évaluation, seuils de lancement, réponses spécialisées aux demandes ci-dessous. Cela ne prétend pas inventorier toutes les autres PR du projet.

### Réutilisation et écarts explicites

Travaux locaux lus : `AI_RECOMMENDATION_HUB_SPEC_v0.1.md` et `SOCIAL_NETWORK_07_AI_RECOMMANDATION_M0_v0.1.md`, produits dans cette discussion le 29 septembre. Ils ne sont pas des références GitHub approuvées. Leur substance utile est reprise ici pour rendre ce livrable autonome.

| Écart | Sources et impact | Traitement proposé / autorité |
| --- | --- | --- |
| Stack présupposée | v0.1 générale §2 nomme NestJS/Python/PostgreSQL/Redis/OpenSearch/ClickHouse sans ADR reçu | Aucune stack héritée dans ce livrable ; 03/HQ décide après comparaison |
| Hub et personnalisation trop précoces | v0.1 générale §9 « MVP 1 / MVP 2 » ; FEAT-029 au catalogue est Phase 3 ; M0 v0.1 propose report | Conserver FEAT-029 en Phase 3 proposée ; Hub facultatif hors pilote ; 01/HQ arbitre |
| Fallback qui change le produit | v0.1 générale §4 suggère des contenus publics sans suivis | Fil vide explicite ; aucune découverte injectée silencieusement dans le fil suivi ; 01/02 valide |
| Modèle et décision de modération confondus | v0.1 générale §6 présente ALLOW/BLOCK comme sorties Safety | Distinguer annotation du modèle et décision autorisée par politique 09 ; pas de sanction définitive autonome implicite |
| Pondérations illustratives | v0.1 générale §3–5 donne 5/3/2/1 et pourcentages non évalués | Ne pas reprendre comme paramètres par défaut ; poids à calibrer, ni activation ni apprentissage M0 |
| Taxonomie de phases | Anciennes mentions Post-MVP/MVP 2 | Utiliser les cinq classes demandées ; aucune échéance déduite |

Ces corrections portent sur la proposition de l'équipe 07 ; elles ne modifient ni les décisions HQ ni les documents des autres propriétaires.

## Besoin, fonctionnalités et parcours

### Classement et alternatives sans IA

Les FEAT du catalogue sont conservés. Les suffixes désignent des volets du même FEAT, pas de nouveaux identifiants globaux. REQ-0701 à REQ-0705 sont proposés pour les besoins sans FEAT dédié, à ratifier par 00/17 après vérification globale d'unicité.

| Référence | Besoin / acteur | Phase proposée ; priorité | Option candidate et justification | Alternative déterministe |
| --- | --- | --- | --- | --- |
| FEAT-008 | Membre : lire les personnes suivies | MVP ; P0 | Chronologie stable, sans modèle ni profil inféré | Tri par date de publication et clé stable |
| FEAT-004/012/014/015 | Lecteur, auteur, modérateur : accès sûr et recours | MVP ; P0 | Appliquer droits et décisions métier avant diffusion ; aucun modèle obligatoire | Règles versionnées et revue humaine |
| FEAT-019 | Produit/QA : mesurer utilité et fiabilité | MVP ; P1 | Mesures minimales autorisées ; pas d'optimisation du temps passé | Tests synthétiques et entretiens volontaires |
| FEAT-023 | Lecteur : retrouver un objet connu | Phase 2 ; P1 | Recherche lexicale avec filtrage d'accès ; ne requiert pas de profil | Index lexical ou liste filtrée selon décision 03/04 |
| FEAT-029/profil | Membre : contrôler sa personnalisation | Phase 3 ; P2 | Préférences déclarées ; profil implicite seulement si justifié et autorisé | Suivis et choix explicites seuls |
| FEAT-029/recommandation | Membre : suggestions organiques facultatives | Phase 3 ; P2 | Baseline déterministe avant modèle appris ; exiger gain utile démontré | Récence des candidats explicitement choisis |
| FEAT-029/explication | Membre : comprendre et corriger une suggestion | Phase 3 ; P0 à l'activation | Motif fidèle, réduction/exclusion, désactivation et reset dès la première recommandation | Motifs issus de règles exactes |
| FEAT-029/Hub | Lecteur : découvrir contenus, communautés et créateurs | Phase 3 ; P2 | Surface distincte ; pas de dépendance nécessaire au pilote | Catalogue éditorial explicite, catégories et langues choisies |
| REQ-0701 | Modérateur : repérer spam et abus | Phase 2 ; P2 | Aide automatique graduelle, sans rendre un modèle indispensable à FEAT-014 | Quotas approuvés, détection de doublons, file de revue |
| REQ-0702 | Auteur : catégoriser un contenu | Phase 3 ; P2 | Annotation proposée, corrigeable, taxonomie non sensible | Catégorie choisie par auteur / éditeur |
| REQ-0703 | Lecteur : comprendre une autre langue | International ; P2 | Traduction à la demande évaluée pour chaque langue ; FEAT-021 n'en dépend pas | Original et traduction humaine si disponible |
| REQ-0704 | Lecteur/auteur : résumé et assistance créative | Phase 3 ; P2 | Résumé facultatif, brouillon contrôlé ; pas de publication automatique | Extrait clairement identifié, rédaction manuelle |
| FEAT-030 | Lecteur/annonceur : publicité transparente | Phase 3 ; P2 | Ad Ranking séparé après arbitrage économique, 11/15/HQ | Rotation contextuelle approuvée ou aucune annonce |
| REQ-0705 | Créateur/lecteur : recherche multimodale avancée | Long terme ; P3 | Étude après utilité prouvée et capacité 08/14 ; aucune collecte anticipée | Métadonnées et catégories déclarées |

### FEAT-008 — fil chronologique candidat MVP

Acteur : membre admissible et authentifié ; visiteur public exclu de ce contrat jusqu'à décision Produit/Privacy. Préconditions : FEAT-002, règles FEAT-004/012/014 et graphe de suivis utilisables. L'inclusion de ses propres publications et des communautés FEAT-020 reste à arbitrer ; baseline d'étude : publications des comptes suivis.

1. Le membre ouvre le fil ; le serveur résout son identité et les relations autorisées.
2. Il fixe une borne de lecture et sélectionne les publications éligibles triées par `published_at DESC, stable_id DESC`. Date serveur de première publication ; une édition ne remonte pas le contenu.
3. Chaque objet est autorisé à nouveau lors de sa lecture, y compris texte, aperçu et média. Les règles d'accès ne sont jamais des poids.
4. Il renvoie une page et un curseur opaque lié au lecteur, au mode et à la borne ; charger la suite conserve le départage.
5. Un rafraîchissement ouvre une nouvelle borne ; les publications arrivées depuis la première page ne sont pas insérées au milieu des pages déjà servies.

Proposition de concurrence : changements de suivis ou de mode invalident le curseur ; changements de visibilité sont réévalués même avec curseur valide. La sémantique transactionnelle exacte appartient à 04/14 : vérifier une autorisation au dernier point de décision serveur ne peut pas effacer une donnée déjà reçue par un client. Les garanties de révocation doivent nommer ce point, l'invalidation des caches et le comportement des réponses en vol.

| État / déclencheur | Résultat et reprise |
| --- | --- |
| INITIAL → LOADING | Libellé de chargement accessible ; ne pas afficher des recommandations factices |
| READY / page reçue | Ordre stable ; compteur de résultats non autorisés non divulgué |
| EMPTY / aucun suivi ou résultat | Expliquer absence de contenu ; action de suivi approuvée par 01/02 ; aucune substitution par un Hub |
| END / fin des candidats de la borne | Marqueur de fin ; rafraîchissement volontaire |
| CURSOR_EXPIRED ou CONTEXT_CHANGED | Proposer rafraîchissement ; pas de mélange de pages ni boucle de retries |
| AUTH_REQUIRED / session révoquée | Arrêter les lectures protégées ; reprise après authentification |
| UNAVAILABLE / autorisation indisponible | Aucun nouveau contenu dont les droits ne sont pas vérifiables ; réessai explicite |
| Contenu retiré, compte bloqué, permission changée | Exclusion à la nouvelle lecture ; client retire l'élément selon contrat de révocation, sans exposer son motif privé |
| Réseau lent / réponse ancienne | Client ignore une réponse dont le contexte a changé ; déduplication par ID, sans masquer une erreur du serveur |

UX 02/05 : accès clavier au mode chronologique, état annoncé au lecteur d'écran, focus conservé au chargement, bouton réessayer, fin de fil compréhensible et libellés localisés. Les filtres de langue ne doivent pas cacher un suivi sans choix explicite. Un fil chronologique n'est pas neutre : auteurs prolifiques favorisés ; les limites anti-spam appartiennent à 09, sans reclassement caché.

### FEAT-029 — contrôles et découverte différés

Préconditions : activation approuvée, politique d'âge, taxonomie, finalités, données et budgets évalués. Aucun suivi implicite activé par ce document.

- **Profil** : déclarer langues/sujets autorisés → enregistrer une version → montrer l'effet. Les contrôles explicites priment sur les signaux inférés. Aucune déduction d'origine, religion ou opinion depuis une communauté, un périmètre marketing, les langues, lieux ou abonnements.
- **Pourquoi** : ouvrir la commande sur une suggestion → afficher le motif réellement enregistré au classement, sa provenance autorisée, et les commandes de correction. Pas d'explication générative inventée ; pas de révélation de liens privés d'un tiers.
- **Réduire / exclure** : « réduire » diminue le poids ; « ne plus recommander ce sujet » est un filtre impératif des recommandations futures. Cette exclusion ne promet pas la disparition de mentions dans tout le texte ni dans le fil suivi ; l'étendue est expliquée. Taxonomie versionnée ; un alias ne doit pas contourner l'exclusion.
- **Désactiver** : passer au mode non personnalisé ; aucune poursuite cachée de collecte dédiée à la personnalisation selon le contrat Privacy ; retrouver le fil suivi.
- **Réinitialiser** : confirmation des conséquences → nouvelle génération de profil → arrêt immédiat de l'usage des anciens dérivés → purge asynchrone suivie. États ACTIVE → RESETTING → RESET_DONE ou RESET_FAILED_RETRYABLE. Garder désactivation effective en cas d'échec ; ne pas annoncer une purge terminée sans preuve.
- **Concurrence reset** : événements et tâches portent la génération du profil ; un événement antérieur ne recrée pas l'ancien profil. Blocages et exclusions de sûreté persistent ; suppression des préférences explicites exige une action distincte.
- **Hub** : choisir une catégorie/langue → liste publique autorisée de contenus, communautés ou créateurs → motif de suggestion → consultation / suivi volontaire. Recommander n'inscrit jamais automatiquement à une communauté et ne révèle pas une communauté privée.
- **États communs** : désactivé, chargement, vide, actif, indisponible, préférence en cours, conflit de version, reset en cours/échoué. En panne, signaler le mode de secours ; ne pas changer silencieusement de surface.

### Assistance, Safety et Ads

REQ-0701 : modérateur habilité ouvre une alerte de spam avec indices limités → examine le contenu autorisé → décide selon politique 09 → notification et recours FEAT-015. Un nombre de signalements n'est pas une preuve de violation ; une panne du modèle ne transforme pas un contenu en ALLOW.

REQ-0702 : auteur propose une catégorie ou reçoit une suggestion → accepte/corrige ; confidence insuffisante = aucune annotation automatique. Exclure catégories sensibles du profil d'intérêts ; ne pas faire d'inférence sensible indirecte par proxy.

REQ-0703/0704 : lecteur autorisé demande traduction/résumé d'une version précise → résultat étiqueté, original accessible ; auteur seul peut intégrer un brouillon à sa publication. Source modifiée/supprimée ou droit révoqué invalide le dérivé. Langue non couverte, timeout, sortie douteuse ou quota épuisé : original / rédaction manuelle, sans résultat prétendu exact. Aucun résumé utilisé seul pour sanctionner. Les instructions dans les contenus sont des données, jamais des ordres pour accéder à des outils ou secrets.

FEAT-030 : candidat publicitaire approuvé et éligible → choix dans un emplacement distinct → mention sponsorisée et explication. Pas d'annonce si autorisation, politique d'âge, budget ou contrôle Safety manquent ; aucune facturation sur la seule sélection. Le contrat de facturation appartient à 11/04. Aucun modèle d'enchères adopté ici.

## Frontières et fiches de modèles

Séparation **logique** confirmée des quatre moteurs, pas prescription de quatre microservices. Backend reste propriétaire des autorisations ; 09 des décisions de modération ; 11 des règles publicitaires ; 07 des scores et annotations. 03 décide de la topologie. Fil chronologique et Safety métier ne dépendent pas d'un modèle entraîné.

| Moteur / capacité | Entrées minimales et sorties | Signaux et poids proposés | Métriques, biais, garde-fous et fallback |
| --- | --- | --- | --- |
| Recommendation Engine | IDs de candidats autorisés, préférences permises, versions ; sortie IDs ordonnés, motifs, version | Baseline tri déterministe ; modèle futur : affinité explicite, récence, diversité ; poids NON DÉFINIS avant évaluation, durée/clic seul non objectif | Utilité déclarée, masquages/expositions, diversité auteurs ; biais popularité et activité ; filtres impératifs, reset ; secours fil suivi annoncé |
| Discovery Engine | Catalogue public éligible, catégories/langues choisies, requête ; listes distinctes contenus/communautés/créateurs | Règles éditoriales/récence ; modèle futur pertinence/diversité, poids NON DÉFINIS ; taille brute ≠ qualité | Suivis volontaires, retour négatif, couverture linguistique ; biais éditorial et langues dominantes ; pas de communautés privées ; secours catalogue si contrôles disponibles, sinon vide |
| Safety Engine | Contenu autorisé, métadonnées nécessaires, règles et décisions 09 ; annotation risque/confiance/version et demande de revue | Règles par type de risque, seuils NON DÉFINIS avec 09 ; pas de score universel ni sanction par popularité des signalements | Précision/rappel, faux positifs, recours acceptés, écarts linguistiques ; satire/dialectes/brigading ; revue/recours ; modèle en panne → UNKNOWN et circuit humain, jamais autorisation implicite |
| Ad Ranking Engine | Campagnes admissibles, contexte autorisé, état budget/fréquence/politique ; sélection ou aucune annonce | Mécanisme et poids NON DÉFINIS avec 11 ; pas d'accès implicite au profil organique | Répétition, signalements, intégrité facturation/coût ; biais gros budgets/proxy sensible ; séparation organique/sponsorisé ; secours aucune annonce |
| Profil d'intérêts | Choix explicites ; signaux implicites seulement si autorisés ; profil versionné avec provenance | Exclusion impérative avant scoring ; aucun coefficient 5/3/2/1 hérité ; durée de vue non collectée pour le pilote proposé | Correction, effacement, dérive ; biais utilisateurs actifs ; séparation par finalité et génération ; secours choix explicites |
| Catégorisation | Texte/version autorisés, taxonomie ; labels/confidence | Modèle et seuil à évaluer par langue ; pas de poids métier arbitraires | Macro-F1 et erreurs par label/langue ; biais de corpus ; correction humaine ; secours catégorie déclarée |
| Traduction | Texte autorisé, langue source/cible ; dérivé lié à la source | Aucune pondération métier ; modèle/fournisseur non choisis | Revue bilingue sens/registre et erreurs graves ; dialectes/translittération ; label automatique ; secours original |
| Résumé / assistance | Source autorisée/version, demande explicite ; dérivé/brouillon | Aucune optimisation d'engagement ; paramètres non choisis | Fidélité, omissions et hallucinations ; biais de formulation ; pas d'action automatique, citations de source quand possible ; secours original/manual |

Le gain d'un modèle est une hypothèse à comparer à sa baseline déterministe. La séparation des filtres, du score et des décisions métier reste exigée même si un seul processus les héberge.

## Permissions, données et contrats

### Permissions candidates — validation 04/09/14/15 requise

| Acteur | Action / portée | Autorisation et refus |
| --- | --- | --- |
| Anonyme | Fil suivi, profil d'intérêts, reset | Refus ; accès public éventuel à arbitrer, pas déduit du Hub |
| Membre actif | Lire fil/Hub et dérivés | Éligibilité du compte + permission sur chaque objet ; aucun contournement par score ou URL |
| Propriétaire du profil | Lire/modifier ses préférences, reset/export | Identité serveur ; version attendue ; action d'un tiers refusée |
| Autre membre / auteur d'un contenu | Consulter profils d'intérêts des lecteurs | Refus ; pas de liste d'intérêts privés fournie à l'auteur |
| Bloqué / suspendu | Lecture et interactions | Matrice 09/15/04 appliquée côté serveur ; aucun passe-droit IA |
| Mineur / âge inconnu | Personnalisation/découverte/publicité | Politique distincte à approuver ; proposition : fonctions comportementales non activées en attente, sans fixer seul l'âge d'accès |
| Modérateur / support | Annotations et dossiers | Permissions distinctes, limitées au dossier ; aucune modification libre d'un profil utilisateur |
| Service de scoring | Accès aux candidats/signaux autorisés | Identité de service, finalité, lot borné ; pas d'accès global DB ni possibilité d'élargir l'audience |
| Opérateur modèle | Publier/revenir à une version | Rôle et revue dédiés, audit ; pas d'accès automatique aux contenus privés |
| Annonceur | Campagnes et données de ses opérations | Aucun profil organique individuel ; décision 11/15 pour rapports permis |

### Données et cycle de vie proposés

Pas de tables ni de technologie choisies. Toute durée ci-dessous est une **hypothèse de minimisation**, pas une durée légale ni un accord Privacy. Aucune collecte différée « au cas où ».

| Données / source | Finalité ; accès / propriétaire | Conservation proposée et modification | Export, suppression, sauvegardes |
| --- | --- | --- | --- |
| Publication, audience, état de modération / 04/09 | Autorisation fil ; service à portée utilisateur ; 04/09 | Référence aux objets canoniques, pas de copie dans un profil IA ; durée objet décidée par 15 | Révocation invalide candidats, médias et dérivés ; export canonique 04/15 |
| Suivis, blocages / action membre | Composer fil et appliquer choix ; 04/09 | Jusqu'au retrait/suppression selon politique propriétaire ; caches bornés et invalidés | Ne pas supprimer un blocage lors du reset IA ; export limité aux données autorisées du demandeur |
| Âge / service compte | Jeton de politique ou classe minimale ; 15/14 | Durée de requête côté moteur ; pas de copie de date de naissance | Aucun moteur ne déduit l'âge depuis image/texte ; renouveler politique obsolète |
| Préférences explicites / membre | Contrôle facultatif ; membre et service autorisé ; 01/15 | Jusqu'au changement/suppression ; persistance après reset inféré expliquée | Export lisible ; suppression explicite ; restauration respecte versions de retrait |
| Événements implicites / futur FEAT-029 | Seulement personnalisation autorisée ; 13/15 | Zéro collecte IA au pilote ; futur essai : maximum 30 jours proposé avant agrégation/purge | Arrêt d'usage au retrait/reset ; purge dérivés ; ne pas promettre qu'un reset désapprend un modèle global |
| Profil inféré / futur calcul 07 | Scoring autorisé ; 07/15 | Inactif M0 ; futur maximum 30 jours sans signal, recalcul autorisé seulement | Export provenance ; génération et purge, y compris index/caches ; pas d'entraînement global autorisé ici |
| Requête et candidats de score | Réponse transitoire ; services 04/07 | Mémoire de requête ; pas de journal intégral de liste privée | Suppression avec fin de requête ; identifiants de trace minimisés |
| Traduction/résumé/labels | Assistance autorisée ; 07/08/16 | À la demande, pas de rétention pilote ; futur cache maximum 24 h proposé, validité liée aux droits/version source | Suppression dérivés à retrait source ; fournisseur sans réutilisation d'entraînement à contractualiser |
| Mesures FEAT-019 | Utilité/fiabilité ; 13/14/15 | Priorité agrégats ; événements bruts proposés ≤ 7 jours, agrégats ≤ 90 jours, sous validation | Agrégat n'est pas automatiquement anonyme ; petits groupes protégés ; export/effacement selon inventaire 15 |
| Dossiers Safety et audit | Motiver et contester ; 09/10/15 | Durée NON REÇUE, à fixer avec finalité et recours ; pas d'archive parallèle IA | Exceptions et preuves documentées ; pas de purge aveugle par reset ; accès séparé |
| Données Ads | Contrats futurs 11/15 | Aucune collecte de classement Ads M0 | Cycle propre sans réutilisation implicite des données organiques |

Sauvegardes : 14/15 doivent fixer expiration et procédure de restauration ; réappliquer les suppressions et générations avant remise en service. Les données supprimées ne doivent pas réalimenter un profil par replay de jobs. Les traces techniques ne contiennent ni texte privé, ni signalement complet, ni secrets.

### Interfaces conceptuelles candidates v0.1

Labels C07-A à C07-F locaux à ce document ; IDs API/événements définitifs attribués par 04/03. Aucun endpoint déployé.

Règles communes proposées : schéma versionné et tailles bornées ; identité serveur pour le membre, identité de service pour appels internes ; champs inconnus traités selon version documentée ; corrélation opaque sans contenu ; refus non révélateur d'existence. Lecture rejouable dans son contexte ; aucune reprise infinie. Budget candidat : requête fil 2 s, score optionnel 300 ms, commande de préférence 2 s, assistance asynchrone 30 s avant état d'attente/échec. Ce ne sont pas des SLO mesurés ; 14/04 valide limites de page, taille, quota, concurrence, backoff et rétention des clés avant implémentation. Un retry de lecture au plus, avec jitter, uniquement si budget restant ; jamais après refus d'accès.

| Interface | Producteur → consommateur ; entrées | Sorties et validation | Défaillance, concurrence, compatibilité et vérification |
| --- | --- | --- | --- |
| C07-A / lecture fil | 04 → 05/06 ; identité, mode=chronological, cursor?, page_size bornée | items autorisés, next_cursor?, borne, mode, request_id ; curseur opaque lié au lecteur | AUTH_REQUIRED, INVALID_INPUT, CURSOR_EXPIRED, CONTEXT_CHANGED, RATE_LIMITED, UNAVAILABLE ; lecture rejouable ; tests 0701–0705 |
| C07-B / éligibilité | 04/09 → 04/07/08 ; lecteur/contexte, IDs objets, versions droits/politique | eligible, ineligible ou unknown par objet ; motif privé uniquement à rôle habilité | UNKNOWN ne vaut pas ALLOW ; cache obsolète refusé ; contrôle final avant service et révocation ; tests 0703/0704/0711 |
| C07-C / classement | 07 → 04 ; engine, candidats éligibles bornés, préférences/génération, policy_version | IDs du sous-ensemble fourni, motifs structurés, model_version, profile_generation | Timeout → secours explicite ; sortie inconnue/ancienne rejetée ; jamais hydrater un ID inventé ; tests 0706/0707/0713 |
| C07-D / préférences et reset | 04 → 05/06/07 ; acteur résolu, action, expected_version, idempotency_key pour reset | nouvelle version/génération, statut immédiat puis job de purge consultable par propriétaire | VERSION_CONFLICT oblige relecture ; même clé même demande = même opération, contenu différent = conflit ; fence avant ACK et purge reprise ; tests 0708/0709 |
| C07-E / invalidations | 04/09 → 07/08 ; event_id, object_id, type retrait/blocage/visibilité/préférence, version, horodatage | accusé technique, état appliqué ; pas de payload privé inutile | At-least-once proposé ; déduplication et rejet anciennes versions ; échec → file surveillée/reprise, pas d'autorisation sur cache périmé ; tests 0703/0709 |
| C07-F / annotation-assistance | 07 → 04/09 ; source ID/version autorisée, langue, tâche, politique | résultat étiqueté, provenance, confiance si pertinente, model_version ou UNKNOWN | Revalider droit à la restitution ; clé source/version/tâche/langue pour éviter doublons ; annuler si retrait ; pas de retry facturable aveugle ; tests 0710/0711 |

Compatibilité : ajout facultatif documenté, pas de modification silencieuse des motifs, taxonomies ou sémantiques de reset ; une rupture nécessite version et migration des consommateurs. Explication publique n'expose pas scores d'abus ni données de tiers. Le contrat Ads complet n'est pas rédigé avant choix 11/HQ ; cette absence bloque uniquement son activation.

## Acceptation et vérification

Critères et IDs TEST-0701–0714 **proposés** à ratifier par 18/17. Tous PLANNED, aucun test applicatif exécuté. Les contrats et l'implémentation sont absents ; ces critères ne sont pas des garanties déjà livrées.

| Critère / test | FEAT ou REQ | Étant donné / lorsque / alors | Type ; statut |
| --- | --- | --- | --- |
| AC-0701 / TEST-0701 | FEAT-008 ; AC-J03-01 | Dates égales et insertions entre deux pages ; lecture paginée ; départage stable, pas de doublon, nouveaux éléments seulement après refresh | Intégration/concurrence ; PLANNED |
| AC-0702 / TEST-0702 | FEAT-008 | Aucun suivi/aucun résultat ; ouverture ; état vide sans injection Hub, actions clavier et fin de fil annoncées | E2E/accessibilité ; PLANNED |
| AC-0703 / TEST-0703 | FEAT-004/008/012 | Blocage ou retrait confirmé avant point d'autorisation de lecture ; fil/détail/média/cache ; aucune donnée interdite servie | API/sécurité ; PLANNED |
| AC-0704 / TEST-0704 | FEAT-004/014 | Service d'autorisation indisponible ; demande ; UNKNOWN et absence de nouvelle exposition non vérifiable | Intégration/panne ; PLANNED |
| AC-0705 / TEST-0705 | FEAT-008 | Curseur d'autrui/altéré, session révoquée ou contexte changé ; lecture ; refus contrôlé sans données, reprise explicite | API ; PLANNED |
| AC-0706 / TEST-0706 | FEAT-029 | Scoring indisponible ; demande recommandée ; secours expliqué et accès chronologique conservé | Intégration/E2E ; PLANNED |
| AC-0707 / TEST-0707 | FEAT-029 | Suggestion réelle ; « Pourquoi » ; motif conforme au calcul et aucun intérêt privé de tiers révélé | API/UX ; PLANNED |
| AC-0708 / TEST-0708 | FEAT-029 | Sujet exclu/désactivation ; nouvelle suggestion ; exclusion appliquée, aucune ancienne réponse acceptée | Intégration ; PLANNED |
| AC-0709 / TEST-0709 | FEAT-029/016 | Reset et jobs concurrents puis restauration ; reprises ; anciens dérivés non utilisés/recréés, blocages conservés, état purge exact | Concurrence/privacy ; PLANNED |
| AC-0710 / TEST-0710 | REQ-0702/0703/0704 | Source retirée ou langue non couverte ; demande de dérivé ; pas de dérivé interdit, original autorisé ou indisponibilité | API/linguistique ; PLANNED |
| AC-0711 / TEST-0711 | REQ-0701 ; FEAT-014/015 | Annotation douteuse, modèle en panne ou faux signalements ; traitement ; revue/recours sans sanction automatique inventée | Safety/intégration ; PLANNED |
| AC-0712 / TEST-0712 | FEAT-029/030 | Mineur ou âge inconnu ; appel ; application exacte de la politique validée, pas de profil Ads partagé implicitement | Privacy ; PLANNED |
| AC-0713 / TEST-0713 | FEAT-019/029 | Scoreur renvoie ID hors lot ou logs avec texte privé ; validation ; rejet/alerte et absence de fuite dans traces | Sécurité ; PLANNED |
| AC-0714 / TEST-0714 | FEAT-030 | Campagne non admissible, état budget inconnu ou événement répété ; sélection/facturation ; aucune annonce non autorisée ni double facturation | API métier ; PLANNED |

### Protocole d'évaluation et coûts

1. Avec 01/13 : définir utilité choisie (retour déclaré, suivi volontaire, tâche terminée), dénominateurs et fenêtre ; les clics et le temps passé ne sont pas l'objectif principal.
2. Avec 09/15/16/18 : jeu synthétique puis corpus autorisé, provenance et droits documentés ; langues du pilote, kabyle et alternance de langues si retenues, translittération, satire, petits créateurs et cas d'abus. Aucune origine ethnique inférée pour constituer les segments.
3. Évaluation hors ligne : séparation temporelle apprentissage/validation/test, déduplication, prévention de fuite ; comparer chaque modèle à la règle déterministe et publier tailles d'échantillon, incertitudes et limites.
4. Safety : mesurer faux positifs/faux négatifs, précision/rappel par langue, erreurs graves et désaccords humains ; seuils approuvés par 09/18 avant activation. Une moyenne globale ne valide pas une langue non couverte.
5. Recommandation : utilité déclarée, diversité, masquages par exposition, nouveaux auteurs et coût/latence. Les métriques d'engagement ne démontrent pas seules une utilité causale. Tests en ligne seulement après protocole 01/13/15 et exclusions/protections de cohortes décidées.
6. Gates proposés : aucune fuite d'accès dans les scénarios critiques ; reset/exclusions/fallback fonctionnels ; seuils chiffrés de qualité et coût définis par les propriétaires avant essai. Une langue non évaluée reste non couverte.
7. Régression ou coût dépassé : désactiver modèle par version, conserver chronologie, appliquer contrôles de droits ; 14 suit incident, 09 prend la décision de sûreté. Pas de rollback réintroduisant profils effacés.

Modèle de coût à renseigner, sans tarifs ni benchmark inventés :

- Fil déterministe : nombre de lectures × coût de sélection/autorisation + caches autorisés + exploitation.
- Recommandation : requêtes × coût de scoring + index/candidats + calcul des profils + évaluation/revue.
- Assistance : tâches × taille de source/sortie × coût unitaire à obtenir + stockage dérivés + contrôle linguistique.
- Safety : volume évalué × coût automatique + cas revus × temps humain ; les faux positifs et recours font partie du coût.
- Ads : sélection, vérification budget, antifraude et rapprochement facturation ; revenus non garantis.

Volumétrie, budget et seuils : NON REÇUS. Demander à 13/19 volumes et usage, à 14 coût mesuré et plafond, à 09 temps humain. Aucun fournisseur à comparer sur un prix supposé dans ce lot.

## Décisions importantes proposées

Reprendre DEC-0002 pour l'arbitrage MVP et INT-0003/RISK-0001–0004 pour les sujets déjà ouverts. Les labels D07-A–C ci-dessous sont locaux ; HQ attribue un DEC/ADR définitif, sans collision.

| Champ | D07-A — pilote déterministe | D07-B — responsabilités séparées | D07-C — données et contrôles avant modèle |
| --- | --- | --- | --- |
| Objectif | Fil utile et vérifiable au pilote | Éviter confusion classement/droits/sanctions/publicité | Préserver contrôle et minimisation |
| Problème | Personnalisation précoce sans preuve d'utilité | Un score pourrait devenir autorité de permission | Profilage et effacement non contractés |
| Solution candidate | FEAT-008 sans classement personnel, Hub ni Ads nécessaires | Quatre moteurs logiques ; autorisation Backend, politique 09, règles Ads 11 | Aucun profil implicite M0 ; future activation conditionnée aux réglages/reset/politiques |
| Alternatives, non rejetées officiellement | Hub éditorial pilote : valeur d'accueil à prouver ; modèle : coût/données supplémentaires | Quatre services : coût opérationnel ; moteur fusionné : couplage dangereux | Choix explicites seuls ; apprentissage global ultérieur exigeant nouvelle analyse |
| Dépendances | 01/02/04/09/15/19 ; DEC-0002 | 03/04/09/11/14 | 01/13/14/15/18 |
| Risques | Démarrage à vide, auteurs prolifiques | Divergence de versions et décisions | Reset incomplet, signaux sensibles indirects |
| Impact business | Réduit coût IA mais exige plan d'accueil et de contenu | Coût initial de contrats, facilite maintenance | Réduit collecte, limite personnalisation et coût de traitement |
| Impact technique | Tri/pagination/permissions à finaliser | Topologie laissée ouverte ; contrat versionné | Génération de profil, invalidation et purge à spécifier |
| Priorité / phase | P0 / MVP | P1 / fondation des phases futures | P0 avant activation / Phase 3 |
| Statut / autorité | PROPOSÉ / HQ + 01 | PROPOSÉ / HQ + 03/04/09/11/14 | PROPOSÉ / HQ + 15/14/13/09 |
| Réexamen | Échec d'accueil démontré par mesure/entretiens | Charges ou besoins d'isolation mesurés | Utilité, données autorisées et validation QA établies |

Delta HQ demandé : intégrer les options au futur DEC-0002, enregistrer les écarts v0.1, rattacher cette contribution au mandat 07 ; ne pas changer automatiquement les phases du catalogue.

## Dépendances, risques et transmission

Toutes les demandes suivantes sont **À TRANSMETTRE** aux discussions. La publication GitHub n'est pas une preuve de réception. Elles précisent le delta à relire ; aucun nouveau scan global n'est demandé. Les labels locaux H07 évitent de réserver arbitrairement des INT globaux.

| Demande / rattachement | De → destinataire | Question et livrable attendu | Blocage |
| --- | --- | --- | --- |
| H07-01 / INT-0001, DEC-0002 | 07 → 01/HQ/19 | Fil suivi seul ? Ses propres posts et communautés inclus ? Hub reporté ? Delta périmètre + plan d'accueil sans recommandations | Contrat final FEAT-008 ; Hub non bloquant pour pilote si exclu |
| H07-02 / INT-0003 | 07 → 03/04/14 | Valider C07-A/B/E, point de révocation, curseur, cache, limites/timeouts et événements | Implémentation sûre du fil |
| H07-03 / INT-0004 | 07 → 09/10 | Politique ALLOW/UNKNOWN/revue, décision vs annotation, recours, capacité humaine et anti-spam sans modèle | Ouverture pilote ; modèle spam peut attendre |
| H07-04 / INT-0005 | 07 → 15/14/09 | Âge/âge inconnu, finalités, durées proposées, accès/export, fournisseurs et restauration ; matrice validée | Traitements concernés et politique d'admissibilité pilote |
| H07-05 / INT-0002 | 07 → 02/05/06 | Parcours chronologie/vide/retry ; futur Pourquoi/réduction/exclusion/reset accessible | UI concernée ; réglages futurs non bloquants pilote |
| H07-06 / INT-0008 | 07 → 13/18/14 | Valider définitions, seuils, 14 critères, volumes et protocole coût/charge | Validation et instrumentation, pas rédaction |
| H07-07 / INT-0009 | 07 → 16/09/08 | Langues testables, modèle de dérivés/version source et révocation médias | Pilote multilingue et futures assistances |
| H07-08 | 07 → 11/12/15 | Mécanisme Ads, éligibilité, publicité mineurs, contrat facturation et mesures créateurs | FEAT-030 uniquement ; hors pilote proposé |
| H07-09 / INT-0010, INT-0006/0007 | 07 → 17/20/21 | Indexer chemin, vérifier IDs proposés, revue du delta/PR empilée | Intégration documentaire ; aucun lot code à ouvrir implicitement |

| Risque / rattachement | Impact ; propriétaire | Mesure et état |
| --- | --- | --- |
| RISK-0001 — extension implicite du MVP | Inflation de coût/périmètre ; HQ/01 | Séparer principes et phases, supprimer l'héritage « MVP 2 » ; OUVERT |
| RISK-0002 — modération sans capacité | Abus et recours non traités ; 09/10 | Dimensionner file humaine, ne pas remplacer par score non évalué ; OUVERT |
| RISK-0003 — langues non évaluées | Faux positifs, exclusion de dialectes ; 09/16 | Corpus autorisé par langue et fallback humain/original ; OUVERT |
| RISK-0004 — droits et caches divergents | Exposition privée après retrait ; 04/14 | Contrat de révocation, contrôle final, tests concurrence ; OUVERT |
| Local 07 : fuite sensible par proxy | Langue/communauté assimilée à origine/religion ; 15/07 | Pas d'inférence sensible, audit des signaux et motifs ; OUVERT |
| Local 07 : réapparition après reset | Jobs/sauvegarde recréent profil ; 04/14/15 | Générations et reprise des suppressions avant restauration ; OUVERT |
| Local 07 : coût sans valeur | Modèles coûteux, qualité inconnue ; 01/13/14 | Baseline sans IA et gates avant essai ; OUVERT |
| Local 07 : isolement social initial | Fil vide sans découverte ; 01/19 | Parcours d'invitation/suivi proposé à Produit, pas ajout automatique d'un Hub ; OUVERT |

## Compte rendu de fin d'étape

1. **Décisions prises et à valider** : format et contenu de domaine rédigés ; propositions D07-A/B/C, phases et durées soumises aux autorités. Aucune stack, politique d'âge, sanction automatique ou roadmap approuvée.
2. **Livrable** : ce fichier v0.2, chemin canonique `documentation/artificial-intelligence/recommendation-options.md` ; ajout seul prévu sur branche dédiée à partir de #2. Référence exacte de publication dans la PR ; pas de SHA anticipé.
3. **Vérification** : comparaison de onze sources avec leurs blobs distants réussie ; relecture ciblée du mandat, catalogue, parcours et deux travaux 07. Contrôles du dépôt à consigner dans la PR après exécution. Aucun test applicatif, modèle, benchmark, expérience ou déploiement exécuté ; tests 0701–0714 PLANNED.
4. **Questions ouvertes** : périmètre du fil et Hub 01/HQ ; autorisations/révocation 04/14 ; âge, rétention et données 15 ; modération 09 ; langues 16 ; métriques/budgets 13/14/18 ; Ads 11.
5. **Dépendances** : H07-01 à H07-09 à transmettre ; absence de réponse ne bloque pas cette rédaction mais bloque les lots identifiés.
6. **Risques et limites** : aucune performance ou conformité démontrée ; copie locale de préparation sans historique distant ; seuls les blobs consultés sont attestés identiques. Le contrôle de nommage/liens ne prouve pas la sécurité du futur produit.
7. **Prochaines étapes / HQ** : revoir ce delta, arbitrer D07-A dans DEC-0002, faire ratifier les politiques et contrats ciblés, normaliser les IDs avec 17/18, puis autoriser un lot d'implémentation seulement après ses validations. PR à revoir avant fusion ; aucune fusion demandée ici. Retargeter après intégration de #2 et revérifier le diff. Rollback documentaire par revert du seul ajout après contrôle des références entrantes.
