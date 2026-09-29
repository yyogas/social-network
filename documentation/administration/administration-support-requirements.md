# Console d'administration et support — exigences M0

## Identification et statut

| Champ | Valeur |
| --- | --- |
| Objectif | Rendre exploitable le candidat pilote : consulter un dossier autorisé, décider, vérifier l'effet, notifier, corriger et traiter un recours sans dépasser ses pouvoirs |
| Propriétaire | 10 — Admin / Support / KB / Tickets ; responsable humain GitHub à désigner par HQ |
| Destinataires | 00 HQ, 01 Produit, 02 UX, 03 Architecture, 04 Backend, 09 Trust & Safety, 14 Security/SRE, 15 Privacy, 16 International, 17 Documentation, 18 QA, 20 Code Source, 21 Intégration |
| Date / version | 29 septembre 2026 / v0.1 du livrable propriétaire au chemin canonique |
| Révision d'entrée | PR #2, branche `documentation/m0-team-coordination`, commit `dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957` |
| Statut | **PROPOSÉ — REVUES SPÉCIALISÉES ATTENDUES** ; implémentation et validation applicative non réalisées par ce travail |
| Mandat | M0-TEAM-10, DIR-011 ; approfondissement de FEAT-017, sans créer de second identifiant de fonctionnalité |
| Classement | MVP candidat pour la console minimale ; autres phases proposées ci-dessous |
| Priorité | P0 pour traiter les incidents du pilote ; aucune permission de production approuvée ici |
| Dépendances bloquantes | INT-1001 à INT-1007 : scope, politiques, accès, données, contrats, UX et capacité humaine |

Références lues : [mandat M0-TEAM-10](../teams/work-orders.md), [modèle](../teams/deliverable-template.md), [plan documentaire](../documentation-plan.md), [vision](../product/product-vision.md), [catalogue FEAT](../product/feature-catalog.md), [parcours J01/J04/J05/J06/J07](../product/user-journeys.md), [gouvernance](../governance.md), [registre HQ](../project-governance/decision-register.md) et [conventions](../repository-conventions.md). Toutes sont examinées au commit d'entrée indiqué ; leurs propositions ne valent pas validation spécialisée.

### Nature des affirmations et reprise de l'existant

| État | Contenu et preuve |
| --- | --- |
| CONFIRMÉ | Le mandat M0-TEAM-10 et le chemin de ce livrable sont reçus dans le message utilisateur et présents au commit d'entrée ; FEAT-017 est la capacité de référence, proposée MVP/P0 par le catalogue |
| PROPOSÉ | Les fonctionnalités détaillées, permissions, profils, états, données et interfaces de ce document ; la séparation console/session et l'indépendance du recours |
| À VÉRIFIER | Moyens humains, horaires, délais, âge/pays/langues, limites techniques, durées de conservation et architecture de la console |
| NON REÇU ICI | Avis approuvés de 09/14/15, contrats définitifs 04, scope MVP arbitré, maquettes validées, preuve d'une application ou de tests applicatifs ; aucune conclusion sur un travail éventuel non communiqué ailleurs |

Ce livrable reprend et consolide les deux brouillons de cette discussion, `BACKOFFICE_INTERNAL_SPEC_V0.1.md` et `SOCIAL_NETWORK_M0_INTERNAL_TOOLS_V0.1.md` (29 septembre 2026, non présents au commit d'entrée). Les éléments utiles sont reproduits ici ; aucune lecture de conversation n'est requise pour l'implémentation future. Leur matrice étendue et leur ancien découpage « MVP 1 / MVP 2 » ne constituent pas des références d'autorisation.

## Besoin, fonctionnalités et parcours

### Périmètre et phases

L'acteur principal est un opérateur interne qui doit traiter une demande sans disposer d'un accès général aux données. Le résultat attendu est un dossier attribuable, un effet métier vérifiable et une possibilité de correction traçable. Tous les classements sont **PROPOSÉS**. « MVP » désigne le candidat pilote ; le scope officiel reste à arbitrer.

| Capacité / module | FEAT existante | Phase / priorité | Résultat et limite |
| --- | --- | --- | --- |
| Dashboard opérationnel | FEAT-017, FEAT-019 | MVP / P0 | Files assignées, âge des dossiers, échecs à reprendre ; métriques agrégées sans classement individuel des agents |
| Users : recherche ciblée et état | FEAT-017, FEAT-002 | MVP / P0 | Retrouver un dossier/compte pour un motif autorisé ; récupération sans contournement de l'authentification |
| Content | FEAT-017, FEAT-006, FEAT-007, FEAT-010 | MVP / P0 | Examiner texte, image ou commentaire lié à un cas, selon sa visibilité et l'habilitation |
| Moderation | FEAT-013, FEAT-014, FEAT-017 | MVP / P0 | Appliquer les actions définies par 09, avec motif, exécution et notification distincts |
| Appeals | FEAT-015, FEAT-017 | MVP / P0 | Réexamen lié à la décision et correction vérifiée ; indépendance proposée à 09/HQ |
| Support / Tickets / KB interne minimale | FEAT-017, FEAT-021 | MVP / P0 | Réponse ou escalade, notes internes isolées, procédures versionnées dans les langues retenues |
| Privacy : réception, suivi et escalade | FEAT-016, FEAT-017 | MVP / P0 | Accompagner export/suppression selon contrat de 15/04 ; aucune exportation libre depuis le support |
| Security / Audit Logs : socle interne | FEAT-002, FEAT-017 | MVP / P0 | MFA, sessions personnel, révocation et traces contrôlées ; sécurité détaillée à valider par 14 |
| Communities : outils locaux et escalade globale | FEAT-020, FEAT-017 | MVP conditionnel / P1 | Seulement si communautés retenues ; un responsable local ne reçoit pas de pouvoir global |
| KB enrichie, support multicanal et automatisations | FEAT-017 | Phase 2 / P2 | Macros validées, SLA différenciés, publication publique séparée ; pas d'envoi automatique décidé ici |
| Creators / Businesses | FEAT-027, FEAT-028, FEAT-017 | Phase 2 / P2 | Outils internes nécessaires à ces produits, sans paiement implicite |
| Analytics internes avancées | FEAT-019, FEAT-017 | Phase 2 / P2 | Rapports définis avec 13/15 ; pas d'export massif de données au pilote |
| Ads / Payments / monétisation | FEAT-030, FEAT-031, FEAT-017 | Phase 3 / P2 | Approbations, litiges et rapprochement à définir avec 11/12/14/15 avant activation |
| Routage régional et nouvelles langues | FEAT-032, FEAT-017 | International / P1 | Couverture humaine et linguistique vérifiée avant ouverture ; langues pilotes traitées dès MVP |
| Aide IA aux opérateurs / intégrations avancées | FEAT-029, FEAT-034, FEAT-017 | Long terme / P3 | Extension expérimentale de la console proposée, distincte du classement général de FEAT-029 ; aucune sanction automatisée approuvée |

Hors livraison de ce lot : code, base de données exécutable, APIs définitives, règles juridiques, application des sanctions sur données réelles et changement de roadmap. Une phase ultérieure pour l'ergonomie avancée ne reporte pas le traitement minimal des demandes FEAT-016.

### Recherche et ouverture d'un dossier

Préconditions : session personnel valide, capacité de lecture et scope de dossier autorisés, finalité liée à la tâche. Recherche MVP par référence exacte de ticket, cas ou compte ; recherche plus large uniquement sur filtres autorisés. Le serveur limite résultats, champs, aperçus et compteurs ; les recherches répétées sont limitées et traçables. Une requête sans résultat n'expose pas si un objet existe hors scope.

Parcours : ouvrir la file → filtrer → prendre/ouvrir un dossier → voir le contexte minimisé → choisir une action permise. États UX : chargement, file vide, aucun résultat, accès refusé, dépendance indisponible, objet supprimé, compte suspendu, dossier déjà traité. Le contexte supprimé affiche une référence et seulement les preuves conservées légalement selon politique 15 ; il n'est pas reconstitué automatiquement depuis une sauvegarde.

### Modération, application et reprise

09 définit motifs, sanctions, urgence, durée et données accessibles. 10 fournit l'interface et les contrôles : préparer une action → récapitulatif cible/effet/durée/motif → réauthentification ou approbation si requise → soumettre → suivre l'effet réel. Le blocage interpersonnel de FEAT-012 ne vaut jamais sanction globale.

Le cas conserve un état de traitement ; la décision, l'exécution et la notification ont des états séparés :

| Objet | États candidats | Transition, garde et reprise |
| --- | --- | --- |
| Cas | `new`, `triaged`, `assigned`, `in_review`, `escalated`, `resolved`, `reopened` | Assignation contrôlée par version ; résolution après décision et état d'application explicites ; escalade conserve responsable et file de destination |
| Décision | `draft`, `pending_approval`, `approved`, `rejected`, `superseded` | Auteur, cible, règle/version et portée immuables une fois approuvés ; modification crée une nouvelle révision et invalide l'approbation précédente |
| Exécution | `pending`, `running`, `succeeded`, `failed`, `reconciliation_required`, `compensated` | Timeout à résultat inconnu → réconciliation par operation_id ; aucun nouvel envoi aveugle de la sanction |
| Notification | `pending`, `sent`, `failed` | Échec de livraison ne transforme pas une sanction appliquée en échec métier ; reprise indépendante dédupliquée |
| Recours | `received`, `assigned`, `reviewing`, `decided`, `remedy_pending`, `resolved` | La résolution distingue décision rendue et réparation réussie ; reprise d'une réparation échouée avec la même opération |

Une correction référence la décision originale et crée un nouvel événement. Elle restaure uniquement les effets de cette décision encore réversibles : elle ne rétablit pas un objet supprimé par son auteur, ne lève pas une autre sanction active et ne réouvre pas une audience devenue interdite. Conflit ou résultat incertain → revue manuelle. La notification ne révèle ni identité du signalant ni notes internes.

### Recours

Le demandeur ne peut contester que la décision pour laquelle la politique lui reconnaît ce droit, y compris un compte suspendu via le canal adapté défini par 04/09/14. La console vérifie appartenance, délai applicable et références. Recommandation : réviseur distinct de l'auteur initial, sans auto-approbation possible par cumul de rôles. Si aucun réviseur n'est disponible, escalade explicite ; aucune confirmation automatique. Résultat : confirmer, modifier ou annuler selon catalogue 09, avec effet de réparation observable. Aucun délai réglementaire n'est inventé ici.

### Tickets, réponse et KB

Un ticket contient demandeur/référence, catégorie, langue, état, responsable, priorité, dates et liens autorisés. États : `new → assigned → in_progress → waiting_requester/waiting_internal → resolved → closed`, avec réouverture et motif. Un changement de file revalide l'accès de la destination ; les pièces ne suivent pas si leur accès n'est pas autorisé.

Réponse au demandeur et note interne sont deux champs/actions distincts : aperçu du destinataire et du contenu avant envoi ; doublon réseau dédupliqué ; échec non affiché « envoyé ». Pour les pièces, formats/taille/quota/scan sont à définir avec 08/14 ; pièce en attente, rejetée ou en échec d'analyse reste indisponible au téléchargement. Le texte libre est rendu sans exécution de contenu actif. Une note interne ne devient pas publique par changement de visibilité.

KB initiale : procédure de réception, modération, recours, compte inaccessible, incident sécurité, demande de données. Chaque article porte langue, version, auteur, propriétaire, validité et état `draft → review → published → archived`. Publication interne par réviseur habilité ; rollback vers une version explicitement revue. Les versions utilisées par un dossier restent référencées. Absence de traduction → escalade à la file linguistique disponible, sans annoncer une langue non couverte.

### Rétablissement de compte sans contournement

Le support peut ouvrir un dossier et déclencher, si autorisé, le parcours de récupération de FEAT-002. Il ne lit ni ne fixe le mot de passe, ne demande pas de code MFA, ne transmet pas de jeton à sa propre adresse, ne se connecte pas « en tant que » membre et ne modifie pas directement l'adresse de récupération. Aucun accès au compte n'est accordé avant vérification par le service d'identité.

Si le facteur de récupération est perdu, l'agent escalade vers une procédure 14/15 définissant les preuves minimales et leur traitement. Sans procédure approuvée, l'accès reste non rétabli. Une usurpation suspectée suit la file sécurité ; restaurer un accès n'annule pas une suspension de modération. Toute exception future exige décision HQ/14/15 et contrat 04, distincts d'un simple pouvoir d'administration.

### Demandes de données

Le support voit la référence, le type, l'état et les motifs d'erreur autorisés d'une demande FEAT-016, et peut l'escalader à 15. Le demandeur utilise le contrat de vérification de 04/14/15 pour l'export ou la suppression. L'opérateur ne télécharge pas automatiquement l'export et ne supprime pas directement les tables. Une demande en attente de vérification, bloquée, expirée ou partiellement exécutée reste visible comme telle. Effets sur sessions, médias, jobs et sauvegardes à définir par 04/08/14/15 avant implémentation.

### UX et accessibilité communes

Navigation par tâches et permissions ; tableaux avec filtres, pagination et libellés d'états ; détail avec historique, motif, preuve minimisée et actions. Clavier, focus visible et restauré après modal, nom accessible des boutons, erreurs reliées aux champs, contraste et absence de dépendance à la couleur à définir/tester avec 02/18. Messages compréhensibles en réseau lent, session expirée et conflit. Une action en cours ne peut être relancée par double-clic ; après perte réseau, afficher « résultat à vérifier » puis consulter l'opération. Le format responsive reste aligné sur le choix de surface approuvé.

## Permissions, données et contrats

### Matrice candidate rôle / action / périmètre / justification / audit

Les sept verbes demandés sont `view`, `create`, `edit`, `delete`, `export`, `approve`, `escalate`. Une combinaison sans règle explicite est refusée. `delete` doit distinguer archivage, retrait de publication et effacement irréversible ; aucun droit générique de suppression n'est déduit du titre du rôle. RBAC apporte les capacités ; ABAC restreint objet, équipe/file, assignation, finalité, visibilité et contexte de session. Attribut manquant, session révoquée ou policy indisponible → refus. 14/15/HQ doivent examiner cette proposition avant adoption.

| Rôle du catalogue | Actions candidates | Ressources et portée | Justification / validation | Audit attendu |
| --- | --- | --- | --- | --- |
| Super Admin | `view`, `escalate` ; gestion de droits via capacité distincte, à valider | Métadonnées d'exploitation ; habilitations sans accès universel aux contenus | Motif et approbateur distinct pour attribution ; aucune auto-élévation | Demande, décision d'habilitation et révocation ; pas de secret |
| Admin | `view`, `edit`, `escalate`, `approve` selon domaine | Assignation des files et actions métier explicitement déléguées | Motif ; approbation interdite sur sa propre demande | Ancien/nouvel état autorisé, acteur, règle et dossier |
| Modérateur | `view`, `create`, `edit`, `escalate` ; retrait par action métier dédiée | Cas assignés, contenu/preuves autorisés, décisions relevant des règles 09 | Référence cas et règle ; décision sensible soumise à contrôle | Lecture sensible, décision, exécution et correction |
| Support | `view`, `create`, `edit`, `escalate` | Ses tickets, références et champs minimaux de compte/demande ; pas de contenu privé par défaut | Dossier de support ; pas de pouvoir de sanction, d'export ou de changement d'identité | Recherche, consultation sensible, réponse, transfert et récupération déclenchée |
| Analyste | `view` ; `export` agrégé seulement après contrat distinct | Mesures agrégées FEAT-019, sans dossier nominatif | Finalité validée 13/15 ; hors socle si non nécessaire | Consultation/export avec filtres et finalité |
| Ads Manager | Aucun accès pilote par ce seul rôle | Phase 3 FEAT-030 | Autorisations détaillées avant lancement Ads | À spécifier avec 11/14/15 |
| Finance | Aucun accès pilote par ce seul rôle | Phase 3 FEAT-031 | Remboursements/versements et seuils à définir | À spécifier avec 12/14/15 |
| DPO | `view`, `edit`, `escalate`, `approve` selon procédure | Dossiers FEAT-016 autorisés ; aucun accès global automatique | Finalité, vérification de demande et politique 15 | Lecture, décision, exception de conservation et suivi |
| Security | `view`, `create`, `edit`, `escalate` ; révocation dédiée | Incidents, habilitations/session dans son scope ; contenu sur habilitation spécifique | Incident/motif, contrôle renforcé selon action | Révocation et résultat, changements de politique, accès aux traces |

Le réviseur de recours est une capacité attribuée à un personnel habilité, pas un dixième rôle implicite. L'auteur initial est exclu même s'il cumule Admin et Modérateur. Les scopes se propagent aux listes, compteurs, médias, notifications, jobs et exports ; masquer un bouton ne protège rien côté API. L'audit n'est ni éditable ni supprimable depuis la console ; son cycle de rétention relève d'un mécanisme contrôlé par 14/15.

| Acteur / état | Résultat proposé |
| --- | --- |
| Anonyme ou membre authentifié ordinaire | Accès API/console interne refusé ; canaux publics de support/recours séparés |
| Propriétaire d'un compte/d'une publication | Aucun privilège interne par propriété ; accès à ses demandes via contrat public |
| Autre utilisateur ou utilisateur bloqué | Aucune lecture de dossier, preuve ou identité de signalant ; blocage ne confère aucun accès |
| Compte suspendu | Aucun accès interne ; possibilité de recours public selon politique 09/14, distincte des permissions sociales |
| Responsable de communauté | Aucune administration globale ; pouvoirs locaux à définir si FEAT-020 retenue |
| Personnel dont le droit vient d'être retiré | Refus à la prochaine opération, y compris job différé et lien de preuve ; délai de propagation à contractualiser |

### MFA, sessions et actions sensibles proposées

Identité personnel nominative et sessions distinctes des sessions membres ; MFA requis, mécanisme et récupération à valider par 14. Durées absolue/inactivité, fraîcheur de réauthentification, limitation des tentatives et propagation de révocation restent à fixer par 14/04 avant test READY. Les notes de ce document ne fixent pas un niveau normatif d'authentification.

| Action | Traitement candidat | Réversibilité et protection |
| --- | --- | --- |
| Assignation/changement de priorité | Permission + motif selon champ + version attendue | Nouvelle modification tracée ; conflits refusés |
| Retrait ordinaire de contenu | Catalogue 09, aperçu cible/effet/motif et confirmation | Correction distincte si conditions de restauration réunies |
| Suspension durable, bulk, suppression de communauté | Réauthentification récente, deux acteurs distincts, approbation liée à la version et périmètre | Blocage si politique/seuil non reçu ; bulk non inclus au pilote |
| Attribution de droits ou modification de règle d'accès | Double contrôle et interdiction d'auto-élévation | Révocation/compensation ; sessions et opérations en attente recontrôlées |
| Export de données personnelles ou accès exceptionnel à preuve privée | Finalité, scope temporaire, approbation et contrôle à chaque téléchargement | Expiration/révocation avant accès ; copie téléchargée non récupérable, à limiter |
| Effacement définitif / purge de preuve | Workflow 15/04 avec règles de rétention, confirmation et vérification | Irréversible après purge ; jamais bouton générique Support |
| Révocation d'une session compromise | Capacité sécurité et motif incident ; circuit urgent à décider par 14 | Session révoquée non ressuscitée ; reconnexion selon procédure normale |

Les mesures d'urgence éventuelles doivent être bornées et revues ; ce lot n'introduit aucun accès « break glass » universel.

### Données et cycle de vie

Stockage ci-dessous : catégories logiques proposées, pas DDL. Durées et lieux sont **À VÉRIFIER par 15/14/04** ; absence de règle de conservation bloque la mise en service du traitement concerné, pas la rédaction.

| Données | Origine / minimum / finalité | Visibilité et propriétaire | Cycle de vie, événements et sauvegardes |
| --- | --- | --- | --- |
| Cas / signalements | Canal public ; référence cible, catégorie, dates, références signalants ; traiter l'abus | 09 métier ; 10 via dossier autorisé ; identité du signalant masquée à la cible | Registre métier 04 ; regroupement sans fusionner identités ; corrections tracées ; export filtré des tiers ; suppression/rétention selon 15 |
| Décisions / recours | Opérateur ou demandeur ; règle/version, motif, effet, état et liens | 09 métier ; opérateurs habilités et projection publique minimisée | Décisions immuables après validation, correction par nouvelle entrée ; conservation limitée selon 15 ; restauration de backup rejoue suppressions/restrictions avant remise en service |
| Tickets / notes | Demandeur/support ; catégorie, texte minimal, propriétaire, état, langue | 10 métier ; réponses publiques séparées des notes internes | Texte libre minimisé ; édition versionnée ; export selon droits des tiers ; purge définie 15 ; sauvegardes ne réintroduisent pas données effacées |
| Pièces / preuves | Référence média ou copie minimale si autorisée ; analyse, empreinte, classification | 09/15 ; téléchargement court et contrôlé pour agents habilités | Stockage objet proposé 08/04 ; aucune collecte exhaustive automatique ; original supprimé ne justifie pas conservation infinie ; expiration, purge et backups selon politique |
| Habilitations / sessions | Identité personnel ; rôles, scopes, versions, expiration/révocation | 14 ; administrateurs d'accès autorisés | Stockage identité à décider 03/04/14 ; suppression de session et révocation ne sont pas réversibles par restauration naïve ; pas d'export support |
| Audit | Application ; acteur, action, objet, résultat, code motif, policy version, corrélation et temps UTC | 14/15 ; lecture audit séparée de la modération | Traces protégées contre modification ; pas de secrets, sessions brutes, preuves privées ou corps complets ; rétention/purge contrôlées et accès exports bornés |
| KB | Rédacteurs ; texte procédural, langue, version, validation, propriétaire | 10/17 ; personnel autorisé ; aucune donnée de dossier réelle | Archivage et restauration de version approuvée ; publication externe séparée ; nettoyage des exemples avant indexation |

### Interfaces candidates pour 04

Identifiants `FEAT-017 / I1` à `I6` : références locales de discussion version 0.1, **pas contrats API canoniques**. 04 décide noms, routes et schémas finaux. Les membres utilisent un canal public distinct pour soumettre une demande ; aucun token membre ne devient une session opérateur.

| Interface / producteurs → consommateurs | Entrée / validation | Sortie, permission et erreur spécifique |
| --- | --- | --- |
| I1 lecture/recherche : console → backend | Référence exacte ou filtres autorisés, curseur, limite bornée ; scope côté serveur | Projection masquée, next_cursor et version ; `view` ; objet hors scope non révélé |
| I2 décision : console → modération backend | Cas, target_version, règle/version, action autorisée, motif, durée si prévue, clé d'idempotence | decision_id, operation_id, état et version ; capacité décision ; `POLICY_CHANGED`, `VERSION_CONFLICT`, `APPROVAL_REQUIRED` |
| I3 recours/correction : console → backend | Appel lié, décision initiale, résultat motivé, version et réparation permise | review_id et remedy_operation_id ; capacité réexamen et indépendance ; `SELF_REVIEW_FORBIDDEN`, `TARGET_CHANGED` |
| I4 ticket/réponse/escalade : console → support backend | Catégorie, état, note interne OU réponse, destinataire autorisé, version et clé | Ticket/version, état de livraison distinct ; capacités ticket ; `DESTINATION_SCOPE_DENIED`, `ATTACHMENT_UNSAFE` |
| I5 récupération/demande privacy : console → backend identité/privacy | Référence ticket/demande et opération autorisée ; aucune valeur secrète manipulée par agent | État générique et opération de vérification par canal approuvé ; `VERIFICATION_REQUIRED`, `RECOVERY_POLICY_UNAVAILABLE` |
| I6 événements/exécution : backend métier → worker, audit, notification et console | Event id, type/version, object ref, operation id, corrélation, projection minimale ; worker authentifié et scope vérifié | Accusé durable, état d'exécution/livraison ; doublon ignoré, échec isolé et réconciliable ; aucune donnée privée dans événement générique |

Contrat commun candidat v0.1 : authentification personnel ou service selon producteur ; autorisation côté serveur à l'acceptation **et** avant effet différé ; version optimiste sur mutation ; idempotence par acteur/opération/clé et empreinte de charge (même clé + charge différente refusée). Limite de page, taille de texte/pièce, quotas, timeout, durée de déduplication, nombre de retries et backoff : décisions explicites attendues de 04/14, bloquantes avant READY. Un timeout ne vaut pas annulation : rechercher l'opération puis réconcilier, et ne retenter une écriture qu'avec même clé selon contrat. Les lectures peuvent être retentées dans une limite approuvée ; les refus permanents ne le sont pas automatiquement.

Les événements supposent une livraison pouvant être répétée ; le consommateur déduplique par event_id. Compatibilité : changements additifs contrôlés, ancienne version maintenue jusqu'à migration explicitement décidée ; notification publique rendue depuis projection autorisée au moment de l'envoi. Corrélation commune entre demande, décision, job, notification et audit. Si audit durable indispensable indisponible, bloquer l'action sensible ; mécanisme transactionnel/outbox et procédure d'urgence à décider 03/04/14. Aucun modèle distribué n'est imposé par cette exigence.

### Erreurs et abus à traiter

| Raison candidate | Réponse opérateur | Trace et récupération |
| --- | --- | --- |
| `AUTH_REQUIRED` / `SESSION_REVOKED` | Reconnexion ; aucune action validée en cache | Trace sans jeton ; recharger dossier et droits |
| `FORBIDDEN` / objet hors scope | Refus sans données ni confirmation d'existence inutile | Motif technique restreint à l'audit ; demander habilitation par canal distinct |
| `VERSION_CONFLICT` / `POLICY_CHANGED` | Recharger, comparer, recommencer confirmation | Aucune écriture silencieuse ni réutilisation d'une approbation obsolète |
| `OPERATION_UNKNOWN` / timeout | État à vérifier, pas succès | Réconciliation par identifiant ; pas de double sanction |
| `DEPENDENCY_UNAVAILABLE` / audit indisponible | Action sensible suspendue, file de reprise visible | Incident corrélé ; reprise après disponibilité selon contrat |
| `RATE_LIMITED` | Délai et possibilité de reprise contrôlée | Détection d'énumération, pas d'augmentation automatique des privilèges |
| `TARGET_DELETED` / suspension | Contexte résiduel autorisé et effet possible explicites | Pas de restauration automatique ; suivre contrat de recours/privacy |
| Pièce dangereuse / texte actif | Pièce inaccessible, texte rendu inerte | Motif d'analyse, jamais contenu malveillant exécuté dans la console |

Abus anticipés : curiosité d'un agent sur un compte connu, recherche de masse, export détourné, usurpation par récupération, collusion d'approbateurs, action sur dossier hors file, dévoilement du signalant, rejeu d'une ancienne approbation. Mesures proposées : scopes, justification, limites, séparation des fonctions, audit et tests négatifs ; leur efficacité reste à démontrer.

## Acceptation et vérification

IDs de test proposés dans l'espace 1001–1015, à normaliser par 17/18 ; ils ne créent pas de nouveaux FEAT. Données fictives : opérateurs A/B, membre U, tiers V, cas C, contenu P. Tous les tests sont **PLANNED** ; aucun n'est exécuté par ce livrable.

| Critère | Référence | Étant donné / lorsque / alors | Test / type | Statut et blocage |
| --- | --- | --- | --- | --- |
| AC-ADMIN-01 | FEAT-017, AC-J05-01 | A sans scope demande C par ID ou recherche : réponse sans dossier/champ/compteur révélateur | TEST-1001 / API | PLANNED ; 04/14 |
| AC-ADMIN-02 | FEAT-017, AC-J05-01 | Habilitation A révoquée après ouverture : mutation et job différé refusés selon délai contractuel | TEST-1002 / intégration | PLANNED ; 04/14 |
| AC-ADMIN-03 | FEAT-014, AC-J05-02 | A et B agissent sur même version C : résultat conforme au contrat, aucun écrasement silencieux | TEST-1003 / intégration | PLANNED ; 04 |
| AC-ADMIN-04 | FEAT-014, AC-J05-03 | Timeout après acceptation : reprise par operation_id sans double sanction | TEST-1004 / API/intégration | PLANNED ; I2/I6 |
| AC-ADMIN-05 | FEAT-014, AC-J05-03 | Sanction appliquée, notification échouée : états distincts ; reprise notification seule | TEST-1005 / intégration | PLANNED ; 04/09 |
| AC-ADMIN-06 | FEAT-015, AC-J05-04 | A décide puis reçoit son recours avec rôle Admin ajouté : réexamen refusé | TEST-1006 / API | PLANNED ; indépendance 09/HQ |
| AC-ADMIN-07 | FEAT-015, AC-J05-05 | Autre sanction active ou suppression auteur : correction ne restaure pas P hors conditions | TEST-1007 / intégration | PLANNED ; 04/09/15 |
| AC-ADMIN-08 | FEAT-002, J01 | Support ouvre récupération : aucun secret ni changement d'identité direct ; vérification requise | TEST-1008 / API/E2E | PLANNED ; 04/14/15 |
| AC-ADMIN-09 | FEAT-017 | Note interne et réponse existent : preview/envoi public excluent la note et identité du signalant | TEST-1009 / API/E2E | PLANNED ; I4 |
| AC-ADMIN-10 | FEAT-016, AC-J06-01 | Support ou V tente de récupérer export U : refus ; U avec lien expiré refusé | TEST-1010 / API | PLANNED ; 04/15 |
| AC-ADMIN-11 | FEAT-017 | Action approuvée modifiée ensuite : exécution refusée, nouvelle approbation requise | TEST-1011 / intégration | PLANNED ; 04/14 |
| AC-ADMIN-12 | FEAT-017 | Recherche/consultation sensible et décision : audit attribuable sans secrets ni preuve brute | TEST-1012 / intégration | PLANNED ; 14/15 |
| AC-ADMIN-13 | FEAT-017, FEAT-021 | Triage au clavier avec erreur puis modal : focus et erreur compréhensibles ; langue non couverte signalée | TEST-1013 / E2E + revue accessibilité | PLANNED ; 02/16/18 |
| AC-ADMIN-14 | FEAT-017 | Pièce non analysée ou rejetée : lecture et téléchargement direct refusés | TEST-1014 / API/intégration | PLANNED ; 08/14 |
| AC-ADMIN-15 | FEAT-016, AC-J06-04 | Restauration de sauvegarde contenant donnée effacée : restrictions/suppressions réappliquées avant accès | TEST-1015 / reprise | PLANNED ; 04/14/15 |

Les vérifications documentaires effectivement exécutées sont consignées séparément dans [administration-validation.md](administration-validation.md). Elles ne prouvent aucun comportement applicatif.

## Fiches de décisions importantes — propositions

IDs locaux de proposition D1 à D3 rattachés à M0-TEAM-10 ; HQ attribuera un `DEC-XXXX` ou `ADR-XXXX` canonique avant adoption. Les propositions précédentes INT-M0-001 à INT-M0-004 de la discussion sont couvertes ci-dessous et ne sont pas des décisions approuvées.

| Champ | D1 — périmètre de console | D2 — accès personnel | D3 — recours et correction |
| --- | --- | --- | --- |
| Statut / phase | PROPOSÉ / MVP | PROPOSÉ / MVP | PROPOSÉ / MVP |
| Objectif / problème | Exploiter le pilote sans construire les 17 modules ; scope trop large | Attribuer chaque action et limiter les données ; rôle trop puissant | Permettre une contestation et corriger sans réintroduire un effet interdit |
| Solution candidate | Files, contenu autorisé, décisions, recours, tickets/KB, suivi privacy, audit | Identité/session interne distincte et capacités par action/objet/scope ; double contrôle ciblé | Réviseur distinct ; réparation comme opération versionnée, traçable et réconciliable |
| Alternatives / rejet proposé | Suite entière dès MVP : coût/délai disproportionné ; outil externe : à comparer si exigences satisfaites | Session membre partagée ou Super Admin illimité : exposition et ambiguïté ; séparation réseau stricte : coût à évaluer | Auto-réexamen : conflit ; restauration aveugle : autres sanctions/suppressions ignorées |
| Dépendances | HQ/01/09/15/19, contrats 04 | 03/04/14/15, moyens humains HQ | 09/04/14/15/18, couverture humaine HQ |
| Risques / propriétaire | Sous-estimer support/urgence — 10/HQ | Complexité et collusion résiduelle — 14 | Indisponibilité de réviseur, réparation partielle — 09/10 |
| Impact business | Réduction d'effort initial ; capacité humaine toujours nécessaire | Coût d'identité et de revue contre abus internes | Confiance, délai de traitement et besoin de second opérateur |
| Impact technique | Console modulaire ; pas de stack décidée | Contrôle central, champs masqués, révocation, audit | États séparés, concurrence, idempotence et correction conditionnelle |
| Priorité / réexamen | P0 ; revoir si scope public change | P0 ; revoir après modèle de menaces ou changement d'organisation | P0 ; revoir avec politique 09 et preuve de capacité |
| Delta à ratifier | FEAT-017 et décision MVP, sans modifier silencieusement le catalogue | Matrice et frontières ; contrat d'authentification | Politique de réexamen J05 et contrat de réparation |

## Dépendances, contradictions, risques et transmission

### Deltas par rapport aux brouillons et au HQ

1. **Demandes de données :** ancien M0 « workflows privacy complets Post-MVP » ambigu face à FEAT-016 candidat MVP/P0. Présent document inclut réception/suivi sécurisé dès pilote ; automatisation avancée seule différable. 15/01/HQ doivent confirmer la portée, sans considérer le report antérieur comme décidé.
2. **Rôles :** matrice générique précédente attribuait des droits étendus sans granularité suffisante. Elle est retirée comme candidate d'implémentation au profit de cette matrice limitée, toujours non approuvée ; `delete` est distingué d'un retrait métier.
3. **Recours :** indépendance stricte proposée ici ; J05 laisse la règle ouverte. Ce n'est pas une contradiction entre décisions approuvées : c'est l'arbitrage D3 à instruire.
4. **Recherche interne :** recherche ciblée de dossier pour FEAT-017 MVP ; FEAT-023 recherche sociale reste Phase 2. Ne pas confondre ces deux surfaces.
5. **International :** FEAT-021 langues pilotes demeure MVP ; seule l'expansion FEAT-032 relève d'International. Les capacités humaines support/modération conditionnent l'ouverture.

### Demandes ciblées — toutes À TRANSMETTRE aux discussions

Publication en PR ne signifie pas réception par les équipes. IDs ci-dessous proposés et contrôlés sans collision au commit d'entrée ; 17/HQ coordonnent leur réservation lors d'intégration.

| ID / émetteur | Destinataires | Question / livrable attendu / delta | Blocage |
| --- | --- | --- | --- |
| INT-1001 / 10 | 00/01/19 | Confirmer scope FEAT-017, communautés, volume, horaires et budget humain ; arbitrage D1 | Périmètre définitif et lancement |
| INT-1002 / 10 | 09/00 | Catalogue actions/motifs, urgence, notifications, délais et indépendance du recours ; examiner parcours et D3 | Actions réelles et recours |
| INT-1003 / 10 | 14/03/00 | Matrice capacités/scopes, MFA/sessions/récupération, révocation, approbation et panne audit ; examiner D2 | Implémentation des accès |
| INT-1004 / 10 | 15/04/08 | Champs visibles au support, preuves, rétention, export/suppression et sauvegardes ; examiner tableau données + FEAT-016 | Traitements concernés et lancement |
| INT-1005 / 10 | 04/03/20 | Contrats I1–I6, valeurs limites/timeouts/retries, états, concurrence, audit durable et réparation | Code consommateur et tests READY |
| INT-1006 / 10 | 02/05/16/18 | Maquettes de files/détail/confirmation, langues et accessibilité ; mapper AC-ADMIN aux tests QA | UI et preuve de validation |
| INT-1007 / 10 | 17/21/00 | Indexer chemin canonique, intégrer références/IDs sans collision ; revue du delta de cette PR | Intégration documentaire, pas rédaction indépendante |

| Risque proposé | Impact / propriétaire | Mesure et état |
| --- | --- | --- |
| RISK-1001 | Consultation/exfiltration interne excessive ; élevé, 14/15 | Matrice et scopes à revoir, téléchargements contrôlés, tests négatifs ; OUVERT |
| RISK-1002 | Usurpation par récupération support ; élevé, 14/04 | Aucun contournement d'identité, procédure d'exception validée avant usage ; OUVERT |
| RISK-1003 | Double sanction ou restauration abusive ; élevé, 04/09 | Idempotence, version, réconciliation et correction conditionnelle ; OUVERT |
| RISK-1004 | Recours sans opérateur indépendant ou file urgente non couverte ; élevé, HQ/09/10 | Capacité nominative/horaires et escalade avant pilote ; OUVERT |
| RISK-1005 | Conservation excessive ou réintroduction de données ; élevé, 15/14 | Politique par catégorie, purge et exercice de restauration ; OUVERT |
| RISK-1006 | Confondre publication, approbation et implémentation ; élevé, HQ/17/21 | Statuts séparés, revue sur SHA et autorisation ciblée du futur lot ; OUVERT |

## Compte rendu de fin d'étape

1. **Décisions :** chemin du mandat utilisé, FEAT réemployés, consolidation des deux brouillons ; D1–D3 restent proposés, droits non adoptés.
2. **Livrables :** ce document v0.1, index de domaine et rapport de validation. Publication suivie dans la PR de contribution, empilée sur #2 ; aucune fusion implicite.
3. **Tests :** 15 cas applicatifs PLANNED, aucun exécuté. Contrôles documentaires et limites dans le rapport lié.
4. **Questions :** politique 09, accès 14, données 15, contrats 04, moyens humains et scope HQ ; réponses NON REÇUES ici.
5. **Dépendances :** INT-1001 à INT-1007, transmissions aux discussions À TRANSMETTRE ; cette PR constitue une soumission GitHub à revue.
6. **Risques :** RISK-1001 à RISK-1006 ouverts ; aucune conformité, maturité de production ou réussite applicative proclamée.
7. **Suite / HQ :** faire examiner uniquement les tableaux et parcours concernés ; arbitrer D1–D3 puis normaliser avec 17 ; 04/14/15 ferment les contrats avant autorisation du lot d'implémentation ; 21 revoit la PR avant fusion.
