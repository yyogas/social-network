# Plan de mesure — Fondation M0

## Identification et statut

| Champ | Valeur |
| --- | --- |
| Référence | M0-TEAM-13 / FEAT-019 — v0.1 |
| Objectif | Mesurer valeur récurrente, qualité des échanges, sécurité et coût du pilote avec collecte minimale |
| Propriétaire | 13 — Data / Analytics / BI ; aucun reviewer humain désigné |
| Destinataires | 00, 01, 03–07, 09–19, 21 selon dépendances ci-dessous |
| Date / référence | 29 septembre 2026 ; PR #2, branche documentation/m0-team-coordination, SHA dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957 |
| Statut | PROPOSÉ — avis spécialisés et arbitrages HQ attendus |
| Classe / priorité | MVP candidat / P1 selon FEAT-019 ; garanties privacy proposées P0 avant collecte |
| Portée | Mesure interne pilote et fondations des phases futures |
| Implémentation | Aucun SDK, pipeline, dashboard, migration ou collecte activés |
| Blocages | Valeur 01/19, traitements 15, accès 14/10, sources 04, architecture 03 |

Références lues : [mandat 13](../teams/work-orders.md), [modèle](../teams/deliverable-template.md), [plan documentaire](../documentation-plan.md), [vision](../product/product-vision.md), [catalogue](../product/feature-catalog.md), [parcours](../product/user-journeys.md), [gouvernance](../governance.md), [conventions](../repository-conventions.md), [registre HQ](../project-governance/decision-register.md), [coordination](../project-governance/coordination-board.md). Source : [PR #2](https://github.com/yyogas/social-network/pull/2).

Réutilisation : SN-DATA-M0-001 v0.1, rédigé dans la discussion 13 le 29 septembre 2026. Ce plan adapte ce brouillon au mandat GitHub. Sa publication ne vaut pas approbation des propositions antérieures.

| Nature | État |
| --- | --- |
| CONFIRMÉ | Mandat documentaire reçu ici ; séparation analytics/personnel/finance/sécurité demandée ; références ci-dessus consultées |
| PROPOSÉ | Formules, fenêtres, durées, accès, événements, phases détaillées et options ci-dessous |
| À VÉRIFIER | Validité des signaux, représentativité, volumes, coûts, caractère anonyme des agrégats |
| NON REÇU à cette référence | MVP approuvé, avis 15, matrice d'accès 14, contrats 04, budget et résultats d'étude 01/19 |
| Non établi | Collecte autorisée, conformité juridique, application implémentée ou résultats fonctionnels |

## Besoin, fonctionnalités et parcours

### Fonctions et phases proposées

Réutilisation des FEAT existants. M/E/AC/D/R sont des repères locaux sous FEAT-019, pas des IDs globaux concurrents.

| Fonctionnalité / parcours | Acteur, problème et résultat | Phase / priorité | Préconditions |
| --- | --- | --- | --- |
| FEAT-019 avec FEAT-001/005/006/010 ; J01–J03 | Produit/Growth : comprendre première valeur et retours ; améliorer accueil | MVP / P1 | Population et action utile approuvées |
| FEAT-019 avec FEAT-006/009/010 ; J02–J03 | Produit : mesurer échanges entre personnes au-delà du volume | MVP / P1 | Admissibilité des réponses et fenêtre |
| FEAT-019 avec FEAT-013/014/015/017 ; J04–J05 | Safety : dimensionner charge, prise en charge, recours | MVP / P1 | Contrats dossiers 09, accès restreints |
| FEAT-019 avec FEAT-004/016/022 ; J03/J06 | UX/Privacy : vérifier compréhension audience, contrôle et satisfaction | MVP / P1 | Étude volontaire 02/19, protocole 15 |
| FEAT-019 avec FEAT-007 | HQ/14 : connaître coût total, médias, charge humaine | MVP / P1 | Sources réelles/estimées distinguées |
| FEAT-020 avec FEAT-019 ; J07 | Produit/Growth : évaluer espaces communautaires | MVP / P1 conditionnel | OPEN-003 ; données minimales sans catégorisation sensible |
| FEAT-023/025/026/027 | Mesure recherche/mobile/vidéo et statistiques créateurs propres à leurs ressources | Phase 2 / P2 | Contrats dédiés ; pas de liste de spectateurs |
| FEAT-029/030/031 | Évaluation recommandations, publicité, revenus et abonnements | Phase 3 / P2 | 07/11/12/15, autorité finance à désigner |
| FEAT-032 | Comparabilité langues, marchés et fuseaux | International / P1 | 16/15 ; pays d'ouverture distinct d'origine |
| FEAT-033/034 | Direct et intégrations ; recherche causale sur valeur/temps utile | Long terme / P3 | Besoin démontré, protocole et budget |

### Parcours et UX du dashboard interne

Un analyste habilité choisit métrique et période, consulte définition/version, population, source, exclusions, fraîcheur et numérateur/dénominateur. Il compare des fenêtres de même maturité. Seules les dimensions autorisées sont disponibles. Un export exige une permission distincte et expire selon contrat 10/14/15. Une anomalie ouvre une investigation qualité, sans export brut automatique. Une correction affiche période, raison technique et version.

Clavier, focus, en-têtes de tableaux, alternatives textuelles aux graphiques, statut non fondé sur la couleur, nombres localisés et fuseau explicite sont proposés à 02/10/16/18. Un visiteur ou membre n'accède pas à cette surface. Les statistiques créateurs appartiennent à Phase 2.

| Objet | États / transition | Erreur, annulation et reprise |
| --- | --- | --- |
| Événement | reçu → validé → accepté durablement → traité ; rejet/quarantaine sinon | Accusé définitif après persistance ; reprise au même ID |
| Doublon | même producteur + event_id + contenu | Ignoré sans incrément ; contenu différent au même ID = CONFLICT, investigation |
| Validation | UNKNOWN_VERSION, INVALID_FIELD, PURPOSE_DENIED | Refus ; correction producteur ; corps interdit absent des logs |
| Transport | UNAVAILABLE, RATE_LIMITED | Retry borné, backlog surveillé ; perte éventuelle visible |
| Dashboard | chargement, prêt, vide, partiel, périmé, indisponible, restreint | Zéro seulement sur données complètes ; dernier résultat daté en mode dégradé |
| Autorisation | ACCESS_DENIED, rôle retiré | Recontrôle côté service, cache/export invalidé selon contrat |
| Agrégat | provisoire → stabilisé → corrigé si nécessaire | Date et version de recalcul visibles ; stabilisé ne signifie pas immuable |
| Effacement | demandé → en cours → vérifié ; échec/reprise | Blocage des replays concernés, propagation aux dérivés et restauration |

Proposition 03/04 : panne analytique ne bloque pas publication ou signalement ; garantir la capture autorisée des faits par un mécanisme indépendant du traitement analytique. Atomicité métier, transport et comportement de saturation restent à contractualiser.

## Dictionnaire des métriques

**Population proposée :** comptes admissibles du pilote observables pour la finalité approuvée. Exclure fixtures, comptes techniques et trafic invalide selon règle versionnée. Suspension et suppression n'impliquent pas une réécriture historique arbitraire : politique 09/15 attendue. Publier limites de couverture ; aucune extrapolation aux non-mesurés sans méthode. Ne pas ajouter un traceur pour mesurer qui refuse le suivi.

**Action Q candidate :** suivre, publier, réagir ou commenter après succès métier. Les lecteurs silencieux sont exclus par Q : appeler les résultats « comptes contributifs/interactifs » jusqu'à décision Produit, pas toute l'audience. Alternative à examiner : visite authentifiée du feed autorisé, sans IDs de contenu, si besoin et traitement validés par 01/15. Une réponse serveur ne prouve pas la lecture humaine.

**Fenêtres candidates :** jours calendaires UTC ; WAU/MAU sur 7/30 jours, jour D inclus ; activation dans [création, création + 7 jours). Cohorte par date UTC de création. Stabilisation indicative 48 h après fenêtre puis corrections versionnées ; pas de SLA approuvé.

| Repère | Définition / dénominateur | Décision et limite |
| --- | --- | --- |
| M01 Activation J7 | Comptes de cohorte avec ≥ 1 Q en 7 jours / comptes éligibles dont la fenêtre complète est observable | Corriger accueil ; onboarding obligatoire non retenu sans décision 01 |
| M02 DAU/WAU/MAU | Comptes distincts avec Q sur D / D−6 à D / D−29 à D ; comptes absolus | Ne pas sommer DAU pour WAU ; Q ne couvre pas tous les lecteurs |
| M03 Rétention J1/J7/J30 | Comptes d'une cohorte J0 avec Q exactement J0+n / comptes éligibles de J0 ; cohortes maturées seulement | Distinguer retour exact et retour sur intervalle |
| M04 Création | Publications réussies et auteurs distincts ; taux = auteurs / actifs même fenêtre | Contribution et concentration, pas objectif de volume maximal |
| M05 Qualité d'échange | Posts admissibles avec ≥ 1 commentaire d'autrui dans 7 jours / posts admissibles dont fenêtre de 7 jours est complète | Exclure auto-réponses, doublons, fixtures et spam confirmé selon règle |
| M06 Interactions | Commentaires/réactions créés et acteurs distincts ; stock net séparé du flux de créations | Retrait/ajout ne crée pas un nouvel acteur |
| M07 Compréhension visibilité | Participants réglant puis identifiant correctement l'audience / participants ayant commencé la tâche ; abandons inclus | Étude volontaire ; erreurs de protocole signalées séparément |
| M08 Satisfaction/contrôle | Réponses 4–5 sur échelle 1–5 / réponses valides ; publier aussi invitations et taux de réponse | Biais de sélection ; pas de score de bien-être inféré du temps |
| M09 Safety | Médiane/p95 création → première prise en charge sur dossiers pris en charge ; stock ouvert et ancienneté en parallèle ; décisions révisées / recours clos | Ne pas masquer dossiers ouverts ; clôture ≠ prise en charge ; timestamps incohérents signalés |
| M10 Coûts | Total mensuel réel par catégorie ; coût/actif = coût attribuable / MAU ; coût/image = traitement+stockage+diffusion attribuables / images acceptées | Devise, allocations, temps humain visibles ; estimé séparé du réel |
| M11 Communautés | Adhésions créées/retirées ; membres Q dans l'espace / membres éligibles selon règle temporelle 01 | Seulement si FEAT-020 retenue ; pas de classement des petits groupes |
| M12 Churn d'activité | Actifs sur fenêtre 30 j précédente sans Q sur fenêtre 30 j suivante / actifs précédente ; fenêtres adjacentes achevées | ≥ 60 jours nécessaires ; distinct de résiliation ou suppression |
| M13 Revenus / ARPU | Phase 3 : revenu reconnu Finance / actifs même période ; ARPPU = revenu / payeurs distincts ; abonnements actifs/nouveaux/résiliés séparés | Encaissement ≠ revenu ; taxes, frais, remboursements, devise à contractualiser |
| M14 Ads | Phase 3 : CTR = clics valides/impressions valides ; CPM = dépense/impressions × 1000 ; CPC = dépense/clics ; CPA = dépense/conversions attribuées ; ROAS = valeur attribuée/dépense | Attribution, validité et portée annonceur par 11 ; aucune attribution opportuniste |

Tout ratio à dénominateur nul affiche « non calculable ». Cohorte incomplète = « immature ». Temps utile : non défini comme durée continue ; M07/M08 proposés comme mesures initiales. Absence de signalements ne prouve pas absence de dommages.

**Exemple entièrement fictif :** 10 comptes de cohorte mature, 6 avec Q en 7 jours, 4 exactement J7, 2 exactement J30 : activation 60 %, J7 40 %, J30 20 %. 8 posts maturés dont 3 avec réponse d'autrui : M05 = 37,5 %. 5 personnes commencent une tâche, 3 réussissent, 1 échoue, 1 abandonne : M07 = 60 %. Ces effectifs testent les formules ; ils n'autorisent pas une diffusion de petites cellules réelles.

## Permissions, données et contrats

### Permissions candidates — avis 10/14/15 requis

| Acteur | Ressource/action/portée | Refus / audit |
| --- | --- | --- |
| Anonyme, membre, bloqué/suspendu | Aucun accès BI interne ; droits individuels via FEAT-016 | Refus serveur, y compris URL/export direct |
| Produit/Growth | Agrégats approuvés, dimensions bornées | Pas de jointure identité ou export brut ; accès/export journalisés |
| Data habilité | Calcul/qualité pseudonymes dans finalité approuvée | Pas de réidentification libre ; investigation justifiée et limitée |
| Safety/modération | Charge agrégée restreinte ; dossiers dans outil 09/10 | Identités/preuves absentes de BI générale |
| Finance | Zone financière et agrégats approuvés | Pas de croisement avec usage personnel par défaut |
| Security/Ops | Santé du pipeline, logs minimisés | Aucun corps privé, secret ou token |
| Créateur/entreprise Phase 2 | Mesures autorisées de ses ressources | Pas de liste d'audience individuelle ni métriques d'autrui |
| Producteur de service | Écriture allowlist version/finalité | Aucun droit BI ; identité/quota/audit |

Une authentification n'autorise pas à elle seule une collecte. Changement de rôle, export asynchrone et cache doivent être contrôlés côté service.

### Catalogue minimal candidat v1

Enveloppe : event_id, event_name, schema_version=1, occurred_at_utc, received_at_utc attribué serveur, producer, environment, purpose_code. Clés sujet/objet ajoutées seulement si requises ci-dessous. Pas de session_key globale, IP brute, fingerprint, localisation fine, texte libre, contenu privé, origine ethnique ou appartenance inférée.

| Événement / source → consommateur | Champs spécifiques | Finalité → destinataire / sensibilité | Rétention proposée / agrégation / alternative |
| --- | --- | --- | --- |
| E01 account_created / 04 → 13 | actor_key analytique, date création | M01/M03 → Produit/Growth ; pseudonyme | 45 j → cohorte/jour ; compteurs sans lien sujet si mesure longitudinale refusée |
| E02 social_action_committed / 04 → 13 | actor_key, action enum follow/post/comment/reaction/community_join ; object_key uniquement post/comment, parent_post_key et is_self_reply pour commentaire | M01–M06/M11 → Produit ; relation sociale potentiellement révélatrice | 45 j → acteur/jour et faits post/réponse ; compteurs simples si lien sujet non autorisé |
| E03 content_metric_corrected / 04/09 → 13 | Référence fait/événement, révision, retrait/rétablissement, raison technique contrôlée sans détail sensible | Correction M04–M06 → Data ; pseudonyme | 45 j → recalcul faits conservés ; pas de reconstruction des individus effacés |
| E04 safety_daily_summary / 09/10 → 13 | Jour, stock, comptes de dossiers, p50/p95 calculés source avec effectif et méthode | M09 → Safety ; agrégat restreint | 90 j → jour ; aucun actor_key, case_id, motif ni texte de plainte |
| E05 pilot_study_summary / 02/19 → 13 | Période, protocole/version, tâches commencées/réussies, invitations, réponses valides et histogramme 1–5 | M07/M08 → Produit/Growth ; agrégat soumis au seuil | 90 j → étude/période ; notes et identités hors BI sous protocole 15 distinct |
| E06 cost_period_summary / 14/HQ → 13 | Période, catégorie, montant décimal, devise, réel/estimé, allocation/version, images acceptées, heures humaines agrégées | M10 → HQ ; confidentiel business | 13 mois → mois/catégorie ; aucune facture personnelle ni identifiant payeur |
| E07 privacy_measurement_change / 15/04 → traitement 13 | Sujet analytique, portée, effet/échéance approuvés, request_id opaque | Exécuter effacement/retrait/correction ; Privacy/Data seulement | Données demande retirées après vérification selon durée à valider 15 ; preuve minimisée proposée 90 j ; aucun KPI produit |

Les durées sont des hypothèses de conception, **pas des délais légaux ou adoptés**. E07 est un contrôle de cycle de vie, pas une collecte de comportement. L'autorité et la portée sont vérifiées auprès de 04/15. E01 ne signifie pas compte vérifié : admissibilité fournie par contrat 04 sans identité/justificatif copié.

45 jours couvrent J30 et une reprise, mais pas M12 (60 jours) : différer M12 ou faire approuver une extension ciblée, sans prolonger toute la collecte. Agrégats produit proposés 13 mois si l'examen 15 de réidentification le permet ; sinon moins de dimensions et durée réduite. Expiration calculée depuis l'événement/période, pas depuis un replay. Les données opérationnelles sources ne sont pas conservées plus longtemps au seul motif de la BI.

**Cycle :** projection minimale → staging éphémère → faits nécessaires → agrégats bornés. Staging proposé ≤ 24 h après acceptation ; payload invalide rejeté sans conservation brute. Modification/retrait : recalcul dérivés et version de règle. Export : champs autorisés, destinataire et expiration à contractualiser. Effacement : clés/faits, dérivés encore personnels, caches, exports, files de reprise ; preuve minimisée distincte. Sauvegardes : inventaire 14/15, expiration approuvée et réapplication des suppressions avant remise en service. Absence de nom ne prouve pas anonymat.

**Seuil de diffusion candidat :** 10 personnes distinctes minimum pour agrégats de personnes ; ce seuil seul ne garantit pas l'anonymat. Dimensions bornées, suppression complémentaire des totaux et prévention des différences de filtres. Les petits effectifs Safety restent soumis à une décision restreinte 09/14/15, jamais copiés dans Produit. Pays, langue ou communauté peuvent devenir révélateurs : revue de chaque dimension.

### Interfaces, validation et panne

| Dimension | Contrat documentaire proposé E01–E06 |
| --- | --- |
| Producteur / consommateur | Tableau ci-dessus ; fait métier serveur après succès ; fiche distincte requise pour mesure client |
| Authentification / autorisation | Identité de service, allowlist événement/version/finalité ; mécanisme précis 03/14 NON REÇU |
| Entrée / sortie | Enveloppe et champs fermés ; sortie event_id + accepted/duplicate/rejected/retryable + raison minimisée |
| Validation | Types, tailles, enums, environnement, dates, finalité et références ; inconnus refusés ; aucune quarantaine brute non filtrée |
| Timeout / retry | Candidats à mesurer : émission 3 s, backoff 1/5/30 s puis file reprise ≤ 24 h ; transport 03/04 à décider |
| Idempotence / concurrence | producteur+event_id unique ; contenu différent refusé ; ordre non garanti ; correction par version monotone |
| Limites | Proposition 8 KiB/événement, lots ≤ 100 ; quota producteur à fixer 14 ; pas de listes individuelles E04/E05 |
| Audit / corrélation | event_id, corrélation technique opaque si utile ; métadonnées seulement dans logs |
| Panne | Accepté après persistance ; retry même ID ; alertes backlog, rejet, perte ; KPI partiel si couverture compromise |
| Compatibilité | Version explicite ; changement cassant = nouvelle version et coexistence définie ; deux versions ne comptent pas deux faits |
| Tests | AC-DATA-01 à 12, PLANNED |

Le retry 24 h ne remplace pas la réconciliation : reprise plus ancienne par tâche contrôlée, excluant sujets effacés. Déduplication ne prouve pas livraison exactement une fois de bout en bout.

**E07 et tâches :** identité 04/15 vérifiée ; demande request_id+révision idempotente ; retour par zone avec état et date de vérification. Concurrence et priorité de demandes à définir avec 04 ; retry jusqu'à résolution/escalade, pas d'abandon silencieux. Délai exact bloqué par 15. Backfill autorisé par période/finalité/version, exclusions vérifiées avant écriture, dénominateurs rapprochés ensuite.

**Safety :** p95 de périodes multiples doit être recalculé à la source ou via distribution approuvée ; ne pas moyenner des p95 journaliers. Nombre de dossiers, effectif de délai et dossiers ouverts visibles ensemble.

## Fiches de décisions importantes — propositions à HQ

Aucun DEC/ADR global attribué ici ; HQ/17 évitent les collisions.

| Champ | Proposition A — minimum collecté |
| --- | --- |
| Objectif / problème | Mesurer valeur et retour sans télémétrie exhaustive |
| Recommandation | E01–E03 bornés si approuvés, E04–E06 agrégés source, E07 cycle de vie |
| Alternatives | Compteurs uniquement : moindre exposition, pas de rétention individuelle ; tracking généralisé : rejet proposé faute de besoin démontré |
| Dépendances / priorité | 01/19 objectifs, 15 traitement, 14 accès, 04 sources ; MVP P1, garanties P0 |
| Risques / réponse | Biais et réidentification ; couverture explicite, seuils, minimisation et tests |
| Impact business / technique | Éclairer recrutement/budget ; volume limité mais contrats de suppression nécessaires |
| Autorité / réexamen | HQ avec 01/14/15/19 ; supprimer tout événement sans décision concrète à éclairer |

| Champ | Proposition B — stockage analytique |
| --- | --- |
| Objectif / problème | Chiffres reproductibles sans infrastructure disproportionnée ni surcharge source |
| Recommandation | Contrats indépendants du moteur ; comparer extraction/batch sur projection dédiée et ClickHouse isolé |
| Alternatives | Batch borné : coût initial moindre, charge à mesurer ; ClickHouse : exploitation additionnelle à justifier ; flux massif permanent différé |
| Dépendances / priorité | 03/04/14, volumes et budget HQ ; MVP P1 |
| Risques / réponse | Charge, retard et cohérence ; benchmarks et réconciliation avant adoption |
| Impact business / technique | Coût fixe maîtrisé ; migrations, effacement et recalcul nécessaires quel que soit moteur |
| Autorité / réexamen | HQ/03/14 ; volume/jour, durée batch, fraîcheur, charge source, coût comme critères à mesurer |

ClickHouse reste envisagé, pas adopté par ce plan. Aucun fournisseur, SDK ou schéma physique choisi.

## Acceptation et vérification

Tous les critères sont **PLANNED** ; IDs de tests globaux à attribuer par 18. Fixtures synthétiques, aucun test applicatif exécuté.

| Critère / FEAT | Scénario et résultat attendu | Type futur / propriétaire bloquant |
| --- | --- | --- |
| AC-DATA-01 / FEAT-019 | Publication confirmée rejouée deux fois compte une fois ; même ID altéré → CONFLICT | Intégration ; 04/03 |
| AC-DATA-02 / FEAT-019 | Champ privé/inconnu/finalité refusée → rejet ; contenu interdit absent logs/quarantaine | Contrat/sécurité ; 14/15 |
| AC-DATA-03 / FEAT-019 | Fixture reproduit M01/M03 ; J30 immature non calculable ; WAU distinct non somme DAU | Unitaire données ; 01 |
| AC-DATA-04 / FEAT-019 | 8 posts maturés dont 3 répondus par autrui → 37,5 % ; auto-réponses/doublons exclus | Unitaire/intégration ; 01/04/09 |
| AC-DATA-05 / FEAT-019 | Panne → données partielles ; stock ouvert visible avec délai des dossiers pris en charge ; p95 non moyennés | Intégration/BI ; 09/14 |
| AC-DATA-06 / FEAT-019/017 | Rôle retiré ne lit ni cache ni export ; membre/créateur refusés sur BI interne | API/E2E ; 10/14 |
| AC-DATA-07 / FEAT-019/016 | Effacement supprime faits et dérivés concernés ; replay/backfill/restauration ne réintroduisent pas | Recovery ; 04/14/15 |
| AC-DATA-08 / FEAT-019 | Correction concurrente/retard → résultat déterministe et versionné ; replay ne prolonge pas rétention | Intégration ; 03/04 |
| AC-DATA-09 / FEAT-019 | Cellule 9 personnes supprimée selon seuil candidat ; filtres/totaux ne la reconstruisent pas | Privacy/BI ; 15 |
| AC-DATA-10 / FEAT-019/022 | Zéro réponse → non calculable ; satisfaction avec taux réponse ; parcours utilisable au clavier | UX/E2E ; 02/10/18 |
| AC-DATA-11 / FEAT-019 | Expiration appliquée à staging/faits/exports/reprise ; retard de purge alerté par zone | Intégration/Ops ; 14/15 |
| AC-DATA-12 / FEAT-019 | Coût réel/estimé distincts ; zéro dénominateur non calculable ; devise/allocation visibles | Données/BI ; 14/HQ |

J01 → AC-DATA-03 ; J02/J03 → 01/04/08 ; J04/J05 → 05/06 ; J06, AC-J06-03/04 → 07/11 ; J07 conditionnel. Ces tests complètent les parcours, sans prouver leur fonctionnement par seule instrumentation.

## Dépendances, risques et transmission

D1–D8 et R1–R6 sont des repères locaux. HQ peut les rattacher à INT/RISK. Toutes les demandes sortantes sont **À TRANSMETTRE** ; publication PR ne prouve pas réception dans les discussions.

| Repère / émetteur | Destinataire | Question précise / livrable attendu | Blocage |
| --- | --- | --- | --- |
| D1 / 13 | 01/19/HQ | Examiner Q, M01/M03/M05/M08 ; fixer valeur, cohorte et seuils arrêt/élargissement | Officialisation KPI |
| D2 / 13 | 15/14 | Examiner E01–E07, 45 j/90 j/13 mois, seuil 10, mineurs, exports/restauration ; matrice traitements/accès | Collecte personnelle réelle |
| D3 / 13 | 04/03 | Contrat après commit métier, IDs, corrections/reprise et ADR de stockage A/B | Pipeline |
| D4 / 13 | 09/10 | États prise en charge/clôture/réouverture, recours et agrégation E04, accès BI | Métriques Safety exactes |
| D5 / 13 | 14/HQ | Volumes, budget, réel/estimé, coût humain agrégé et fraîcheur | Infrastructure/M10 |
| D6 / 13 | 02/05/06/16 | Parcours dashboard/étude, accessibilité/fuseaux ; justification de mesure client | Instrumentation client |
| D7 / 13 | 18/17/21 | Mapper AC aux tests, indexer chemin, revoir delta au SHA publié | QA et intégration |
| D8 / 13 | 07/11/12 | Besoins Phase 2/3, réutilisation autorisée, M13/M14 | Fonctions futures uniquement |

| Risque | Impact / propriétaire | Mesure proposée |
| --- | --- | --- |
| R1 Q exclut lecteurs | Biais d'usage / 01/19 | Libellé précis, étude ou alternative justifiée |
| R2 Petits groupes identifiables | Exposition indirecte / 15/14 | Pas d'origine inférée, dimensions bornées, anti différenciation |
| R3 Durée assimilée à valeur | Incitation contraire à promesse / 01/02/19 | Satisfaction, contrôle et échanges |
| R4 Doublons/corrections | Mauvaises décisions / 03/04/13 | Identité de faits, réconciliation et versions |
| R5 Persistance après effacement | Réintroduction / 14/15/13 | Vérifications replay, dérivés et restauration |
| R6 Infrastructure prématurée | Coût/complexité / 03/14/HQ | Comparer option simple mesurée |

### Écarts identifiés avec le brouillon initial

- SN-DATA-M0-001 imposait onboarding terminé + Q pour activation ; vision HQ propose suivre/publier/commenter. Recommandation Q seul en 7 jours, D1 arbitre. Aucune définition officielle remplacée.
- Le brouillon risquait de confondre durée active et temps utile ; M07/M08 proposent valeur déclarée et tâche réussie. Q incomplet pour les lecteurs est explicitement signalé.
- Transport durable et ClickHouse semblaient imposés ; proposition B ouvre le choix à 03/HQ.
- 45 jours bruts ne suffisent pas à churn 60 jours : M12 différé ou extension ciblée D2, jamais prolongation automatique.
- Work-orders identifie 14 pour Security/Ops et 15 pour Privacy/Legal ; identité d'équipe connue, validation NON REÇUE.
- Coordination-board reste sous autorité HQ : réception/revue à inscrire après lecture ; l'équipe 13 ne s'auto-approuve pas.

## Compte rendu obligatoire de fin d'étape

1. **Décisions prises/à valider :** rattachement FEAT-019, format du mandat 13 et repères locaux ; propositions A/B, KPI, conservation et permissions à arbitrer.
2. **Livrables :** documentation/analytics/measurement-plan.md v0.1 ; base dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957 ; publication et SHA du delta font foi dans sa PR.
3. **Tests :** 12 critères PLANNED, aucun test applicatif exécuté ; contrôles documentaires et commandes consignés dans la PR.
4. **Questions :** Q et objectif 01/19, traitements 15, accès 14/10, sources 04/03, coût 14/HQ.
5. **Dépendances :** D1–D8 À TRANSMETTRE ; aucune réponse tierce présumée.
6. **Risques :** R1–R6 ; chiffres fictifs, durées candidates ; ni avis juridique ni benchmark.
7. **Suite/HQ :** examiner D1/D2, arbitrer A/B, revue 03/04/09/14/15/18 puis 21 avant fusion. Rollback documentaire par revert ciblé, aucune migration runtime.
