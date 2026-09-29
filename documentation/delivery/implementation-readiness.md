# Préparation de l’implémentation — M0 / équipe 20

## Identification et statut

| Champ | Valeur |
| --- | --- |
| Mandat / objectif | M0-TEAM-20, réponse à INT-0006 : préparer des lots implémentables et leurs preuves sans adopter une architecture ou un MVP |
| Propriétaire | 20 — Code Source / Repository ; aucun reviewer humain désigné |
| Destinataires | 00 HQ, 21 Intégration ; 01–18 selon les demandes ciblées ci-dessous |
| Date / révision | 29 septembre 2026 — v0.1 de ce livrable GitHub |
| Référence exacte examinée | PR [#2](https://github.com/yyogas/social-network/pull/2), branche `documentation/m0-team-coordination`, commit `dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957` ; dépend de la PR [#1](https://github.com/yyogas/social-network/pull/1), commit `8590a095d76965880e94614328a8eafbe09b93cb` |
| Statut | PROPOSÉ — aucune autorisation d’implémentation, approbation spécialisée ou aptitude au lancement délivrée |
| Classe / priorité | Préparation M0 des capacités candidates MVP, P0 ; autres horizons repris du catalogue, sans engagement de date |
| Portée | Organisation du dépôt, responsabilités, conventions, contrats nécessaires, lots, critères de fin, contrôles existants/manquants |
| Hors périmètre | Code applicatif, choix de framework/fournisseur, DDL, configuration de permissions GitHub, merge, évaluation exhaustive de sécurité |
| Preuves manquantes | MVP et architecture approuvés ; contrats et permissions détaillés ; schémas/migrations ; tests applicatifs et exploitation réelle |

Entrées lues : [mandat 20](../teams/work-orders.md), [modèle](../teams/deliverable-template.md), [plan documentaire](../documentation-plan.md), [vision](../product/product-vision.md), [catalogue](../product/feature-catalog.md), [parcours](../product/user-journeys.md), [registre HQ](../project-governance/decision-register.md), [coordination](../project-governance/coordination-board.md), [conventions](../repository-conventions.md), [contribution](../../CONTRIBUTING.md), [tests](../quality/test-strategy.md), [installation](../installation/installation-guide.md) et [exploitation](../operations/operations-readiness.md).

### Réutilisation et corrections des brouillons précédents

Les brouillons de cette discussion `SOCIAL-NETWORK-Code-Source-Engineering-Ruleset-v0.1.md` et `SOCIAL-NETWORK-CODE-SOURCE-M0-Fondation-v0.1.md` alimentent ce delta. Leurs principes de contrat commun, migration compatible, revue et preuve sont conservés ici. Leur lecture n’est pas requise pour utiliser ce livrable ; aucun export de conversation n’est ajouté.

- Leur constat « dépôt non reçu » est historique : le dépôt et les deux PR sont maintenant consultés. Au SHA examiné, 42 fichiers sont présents ; outils Python du dépôt et tests de validateur existent, aucune application n’est présente.
- Leurs chemins candidats `apps/`, `docs/`, `packages/` sont remplacés ici par les chemins de la PR de fondation : `applications/`, `documentation/`, `shared-packages/`. C’est un alignement sur la proposition versionnée à revoir, pas une adoption de sa topologie runtime.
- Numéros rectifiés d’après le mandat courant : 02 Design, 04 Backend, 05 Web, 08 Médias, 09 Trust & Safety, 14 Sécurité/DevOps. Les anciens numéros mal attribués ne doivent pas être transmis.
- La stack évoquée dans le brief reste une entrée pour OPEN-005, pas une décision approuvée. Le classement courant des 34 FEAT remplace les regroupements approximatifs précédents, notamment notifications essentielles au candidat MVP et recherche en Phase 2.
- Les anciens CODE-HO et M0-DEC-CODE restent des références de brouillon. Les demandes ci-dessous réutilisent INT-0001 à INT-0010 et OPEN-001 à OPEN-008 ; aucune deuxième décision DEC n’est créée.

## 1. État probant et organisation proposée

| Nature | Constat et portée |
| --- | --- |
| CONFIRMÉ | DIR-010/011 et mandat : rédaction, branche, PR, preuve de contrôle et revue avant fusion demandées |
| CONFIRMÉ | PR #1 et #2 ouvertes, non fusionnées au relevé initial ; leur contenu a été lu sur les SHA ci-dessus |
| CONFIRMÉ | Arbre complet des 42 fichiers récupéré ; contenu local de chaque fichier comparé à son SHA blob GitHub ; aucun AGENTS.md dans cet arbre |
| CONFIRMÉ | Workflow documentaire, validateur et dix cas de test présents ; cela ne démontre aucune fonction sociale |
| PROPOSÉ | Lots et critères de préparation des sections suivantes, répartition logique des modules et chaîne de génération de contrats à choisir |
| CONFIRMÉ / À VÉRIFIER | API GitHub de branche `main` consultée : `protected: false`, protection indiquée désactivée au relevé. Comptes reviewers, accès et règles administratives complètes restent à confirmer par 00/14/21 ; aucune configuration modifiée |
| NON REÇU au SHA examiné | Spécifications propriétaires attendues par le plan, autorisations MVP/architecture, contrats applicatifs approuvés, modèle DB, application et résultats de tests métier |

L’absence à ce SHA n’établit pas l’absence dans toute autre branche ou discussion. Toute contribution ultérieure doit être rapprochée de ce livrable par delta.

### Avis local de Code Source sur la PR de fondation

L’organisation proposée attribue un rôle lisible aux racines et fournit une porte d’entrée, des conventions et des contrôles documentaires. Elle convient comme support de rédaction, sous réserve de la revue indépendante de 21. Les racines ne déterminent ni le nombre de services, ni le framework, ni les schémas. Un module logique peut rester dans un même processus ; une séparation déployable exige l’arbitrage de 03/HQ.

| Racine constatée | Usage proposé avant le premier lot | Limite / propriétaire |
| --- | --- | --- |
| `applications/` | Client retenu, puis interfaces opérateurs nécessaires | 05/06/10 ; ne pas créer tous les studios par anticipation |
| `services/` | Backend et traitements réellement approuvés | 03/04/08 ; aucun service par FEAT imposé |
| `shared-packages/` | Contrats ou composants utilisés et versionnés | 03/20, 02 pour UI ; aucune entité de stockage privée publiée aux clients |
| `configuration/` | Exemples sans secret, descriptions de configuration | 14/20 ; pas de variable runtime inventée avant contrat |
| `infrastructure/` | Déploiement retenu après validation | 14 ; aucun fournisseur choisi ici |
| `tests/`, `scripts/`, `.github/` | Suites pertinentes, outils et CI traçables | 18/20/21 et 14 ; pas d’assimilation du validateur à un test produit |
| `documentation/` | Décisions, contrats, critères et preuves canoniques | 17 + propriétaire métier ; compléter l’index ciblé attendu de 17 |

Documents existants à maintenir : README, CONTRIBUTING, conventions, guides installation/exploitation, stratégie de tests, registre, catalogue et parcours. Avant code, leur ajouter les contrats et spécifications du lot, les commandes réellement utilisables et les preuves. Une page ARCHITECTURE ou SECURITY d’entrée pourra référencer ses propriétaires sans dupliquer leurs décisions. Aucun nouveau manifeste de package, SDK, migration ni dossier runtime dans cette contribution.

## 2. Besoins d’intégration et classement des fonctionnalités

Les FEAT et priorités viennent du catalogue au SHA de référence : **toutes ces capacités restent PROPOSÉES**. La contribution 20 est de préparer leur intégration, pas de changer leur priorité métier. La présence dans un lot ne vaut pas autorisation de le coder. Les intitulés ci-dessous sont condensés ; le catalogue reste canonique.

<!-- feature-mapping-start -->
| FEAT | Fonctionnalité | Phase proposée | Priorité | Lot / contribution Code Source |
| --- | --- | --- | --- | --- |
| FEAT-001 | Inscription et activation, méthode à décider | MVP | P0 | L1 |
| FEAT-002 | Connexion, sessions, déconnexion et récupération | MVP | P0 | L1 |
| FEAT-003 | Profil, nom d'affichage, avatar et description | MVP | P0 | L1 + L2 (avatar) |
| FEAT-004 | Confidentialité et contrôle de visibilité | MVP | P0 | Tous lots MVP |
| FEAT-005 | Suivre et ne plus suivre une personne | MVP | P0 | L3 |
| FEAT-006 | Publier, modifier et retirer du texte | MVP | P0 | L2 |
| FEAT-007 | Ajouter une image, texte alternatif et contrôler son traitement | MVP | P0 | L2 |
| FEAT-008 | Fil chronologique avec pagination et états vides | MVP | P0 | L3 |
| FEAT-009 | Réagir et retirer sa réaction | MVP | P1 | L3 |
| FEAT-010 | Commenter et gérer ses commentaires | MVP | P1 | L3 |
| FEAT-011 | Notifications essentielles et préférences | MVP | P1 | L3 + L4 |
| FEAT-012 | Blocage et arrêt des interactions visées | MVP | P0 | L1 (contrat) + L3/L4 |
| FEAT-013 | Signaler un contenu ou un compte | MVP | P0 | L4 |
| FEAT-014 | Examiner, restreindre et notifier une décision de modération | MVP | P0 | L2 (contrat) + L4 |
| FEAT-015 | Contester une décision et recevoir un résultat | MVP | P0 | L4 |
| FEAT-016 | Demandes d'accès/export et suppression de compte | MVP | P0 | L5 |
| FEAT-017 | Console minimale de modération et support | MVP | P0 | L4 + L5 |
| FEAT-018 | Web responsive et accessibilité des parcours prioritaires | MVP | P0 | L1–L6 |
| FEAT-019 | Mesures minimales d'usage et de santé du pilote | MVP | P1 | L6 |
| FEAT-020 | Communautés, membres, rôles et règles — INCLUSION À ARBITRER | MVP | P1 | L7 conditionnel |
| FEAT-021 | Langues du pilote et contenus multilingues | MVP | P0 | L1–L6 |
| FEAT-022 | Respect du temps : commandes de lecture et préférences | MVP | P1 | L3 |
| FEAT-023 | Recherche de comptes, contenus et communautés accessibles | Phase 2 | P1 | Futur : contrat + données + permissions + validation avant ouverture |
| FEAT-024 | Messagerie privée avec contrôles anti-abus | Phase 2 | P2 | Futur : contrat + données + permissions + validation avant ouverture |
| FEAT-025 | Applications mobiles natives et notifications associées | Phase 2 | P2 | Futur : contrat + données + permissions + validation avant ouverture |
| FEAT-026 | Vidéo enregistrée, formats courts et outils de création | Phase 2 | P2 | Futur : contrat + données + permissions + validation avant ouverture |
| FEAT-027 | Outils créateurs : publication et statistiques compréhensibles | Phase 2 | P2 | Futur : contrat + données + permissions + validation avant ouverture |
| FEAT-028 | Présence professionnelle et gestion à plusieurs | Phase 2 | P2 | Futur : contrat + données + permissions + validation avant ouverture |
| FEAT-029 | Recommandations facultatives et explication des suggestions | Phase 3 | P2 | Futur : contrat + données + permissions + validation avant ouverture |
| FEAT-030 | Publicité transparente et gestion des campagnes | Phase 3 | P2 | Futur : contrat + données + permissions + validation avant ouverture |
| FEAT-031 | Rémunération, abonnements et paiements aux créateurs | Phase 3 | P2 | Futur : contrat + données + permissions + validation avant ouverture |
| FEAT-032 | Nouvelles régions, langues, écritures et opérations locales | International | P1 | Futur : contrat + données + permissions + validation avant ouverture |
| FEAT-033 | Direct vidéo et interactions en temps réel à grande audience | Long terme | P3 | Futur : contrat + données + permissions + validation avant ouverture |
| FEAT-034 | Écosystème développeurs, intégrations et portabilité avancée | Long terme | P3 | Futur : contrat + données + permissions + validation avant ouverture |
<!-- feature-mapping-end -->

Pour les FEAT-023 à FEAT-034, M0 documente seulement les interfaces susceptibles d’affecter le noyau : contrats clients compatibles, droits de lecture, cycle des médias et données minimisées. Pas de collecte « pour la future IA », ni d’index de recherche, infrastructure vidéo, système financier ou serveur multi-région implicite. FEAT-021 est une exigence du pilote à préciser ; FEAT-032 est une expansion distincte. Stories et autres idées absentes du catalogue restent à classer par 01/HQ avant création d’un nouvel ID.

### Responsabilités logiques et données possédées — PROPOSÉ

| Domaine logique | Producteur responsable | Consommateurs / frontière | Données et invariants à faire définir |
| --- | --- | --- | --- |
| Identité / sessions | 04, revue 14/15 | Client 05 ou 06 ; outils 10 selon droits | Identité, état du compte, session, récupération ; unicité et révocation |
| Profil / relations / visibilité | 04 avec 01/09/15 | Publication, fil, interfaces ; 14 pour autorisation | Profil, suivis, blocages, règles d’audience ; pas de droits décidés par cache ou UI |
| Publications / interactions | 04 avec 01/09 | Client, médias, fil et modération | Texte, version, auteur, audience, réaction, commentaire ; propriétaire et concurrence |
| Médias | 08 avec 04/14/15 | Publication et accès autorisé ; 05/06 | Original, dérivés, état de traitement, droits, nettoyage ; jamais publié avant validation prévue |
| Signalements / décisions / recours | 09/10, réalisation 04 | Console, notification, contenu, audit | Dossier, preuve admise, motif, décision, recours ; séparation de consultation et action |
| Droits sur les données | 15/04, opérations 10/14 | Identité, publication, médias, sauvegardes | Demande, vérification, état par système, export protégé ; pas de réintroduction lors de restauration |
| Mesure / exploitation | 13/14 avec 15 | Tableau pilote, alertes, release | Événements autorisés et signaux techniques ; minimisation et accès distincts |

20 vérifie les interfaces, les dépendances et la compatibilité ; chaque propriétaire conserve ses règles. Les imports entre modules doivent passer par des interfaces explicites. Les packages communs ne doivent pas exporter des accès DB, secrets ou privilèges à un client. La convention de noms JSON/SQL et la direction de génération restent à décider via OPEN-005 ; l’identité métier doit rester constante dans les mappings.

## 3. Prérequis et futurs lots

### Matrice de préparation à l’implémentation

| Porte / responsable | Pièce d’entrée attendue | État au SHA examiné | Effet et critère de levée |
| --- | --- | --- | --- |
| Périmètre — 00/01 | DEC-0001/0002 et critères des FEAT retenus | NON REÇU ; vision/catalogue PROPOSÉS | Bloque code métier du lot ; une décision datée indique inclus/exclus et parcours |
| Architecture — 03/14 | Frontières, stack/outils, exécution et ADR applicables | NON REÇU ; OPEN-005 | Bloque squelette applicatif ; interfaces et dépendances validées pour le lot |
| Contrats — 04 + consommateurs | Schémas, états, erreurs, compatibilité, quotas et reprise | NON REÇU | Bloque intégration correspondante ; producteurs/consommateurs valident la même révision |
| Permissions — 09/14/15 avec 01/10 | Matrice acteur/action/objet/état, visibilité et accès internes | NON REÇU ; OPEN-007 | Bloque opérations concernées ; refus et accès directs ont résultats attendus |
| Données — 04/15/03 | Modèle/invariants, rétention, export/effacement, migrations | NON REÇU | Bloque persistance métier ; compatibilité, backfill et récupération documentés |
| Client / langues — 02/05/06/16 | OPEN-002/004, états UI, accessibilité et langues retenues | NON REÇU | Bloque intégration client dépendante ; parcours et messages examinés |
| Qualité — 18/21 | Cas QA par AC, environnement et règle de revue | Stratégie documentaire présente ; suites métier NON REÇUES | Bloque verdict fonctionnel ; critères exécutables et revue indépendante définis |
| Livraison — 14/20/00 | Runtime/outils versions, installation, CI, secrets, rollback, budget | Préparation documentaire présente ; application NON REÇUE | Bloque build/release concernés ; environnement reproductible, preuve et responsable |

### Lots candidats et critères de fin

L0 à L7 sont des repères locaux de planification, pas des IDs produit ni de nouvelles décisions. Priorité d’intégration P0 des prérequis de lancement ; les priorités FEAT restent celles du tableau précédent.

| Lot / phase | Entrées et travail proposé | Propriétaires / prérequis | Critère de fin observable | État actuel |
| --- | --- | --- | --- | --- |
| L0 — préparation, MVP | Dépôt, conventions, modèles PR et matrice présente ; compléter les pièces des gates | 20/17/14/21 ; mandat M0 | Pièces et blocages reliés à un owner, diff contrôlé et revue demandée | Rédaction autorisée ; approbation NON REÇUE |
| L1 — compte/session/profil minimal, MVP | J01, FEAT-001 à 004/018/021 ; contrat de blocage/suspension ; avatar dépend de L2 | 04/05 ou 06, 02/14/15/16 ; décisions des gates, migration et modèle session | AC-J01-01 à 04 vérifiés ; champs privés absents pour tiers ; langue/clavier selon cibles ; preuve reliée au commit | BLOQUÉ POUR CODE |
| L2 — texte/image/visibilité, MVP | J02, FEAT-006/007 ; auteur, audience, upload et retrait, interface de décision de modération | 04/08/05, 09/14/15 ; L1 minimal + contrats conjoints avec L4 | AC-J02-01 à 05 ; test URL directe et réessai ; aucun média refusé affiché comme publié | BLOQUÉ POUR CODE |
| L3 — suivis/fil/interactions, MVP | J03, FEAT-005/008 à 012/022 ; règles de notification, blocage et concurrence | 01/02/04/05/09 ; L1/L2, règle d’ordre et révocation | AC-J03-01 à 05 ; ACL revalidée sur pagination/commentaire ; pas de double réaction | BLOQUÉ POUR CODE |
| L4 — signalement/modération/recours, MVP | J04/J05, FEAT-013 à 015/017 + notification nécessaire ; dossiers, actions et réexamen | 09/10/04/14/15 ; contrats L1/L2, rôles internes, capacité opérateur | AC-J04-01 à 04 et AC-J05-01 à 05 ; échec partiel et rôle révoqué vérifiés ; opération manuelle définie | BLOQUÉ POUR CODE |
| L5 — export/suppression, MVP | J06, FEAT-016 et pouvoirs limités FEAT-017 ; données de L1–L4 | 15/04/08/10/14 ; inventaire, rétention et sauvegardes | AC-J06-01 à 04 ; état réel par système, export privé, restauration sans réintroduction interdite | BLOQUÉ POUR CODE |
| L6 — préparation pilote, MVP | FEAT-018/019/021 transversales ; installation, instrumentation minimale, backup/restore, incidents et release | 14/18/13/16/20/21 ; lots retenus, objectifs de charge/coûts et capacité humaine | Parcours retenus vérifiés ; build reproductible ; restauration et rollback exercés ; critères QA/release et avis propriétaires réunis | BLOQUÉ POUR OUVERTURE |
| L7 — communautés, MVP conditionnel | J07/FEAT-020 ; visibilité, adhésion, rôle local et articulation globale | 01/09/10/04/19 ; OPEN-003 puis contrat dédié | AC-J07-01 à 04 ; dernière responsabilité, fermeture et retrait de rôle vérifiés | CONDITIONNEL, NON AUTORISÉ |

**Première tranche recommandée à HQ :** L1 limité à un compte, une session révoquable et un profil dont la visibilité est définie, sur le client retenu, avec tests d’autorisation. Différer l’avatar jusqu’au contrat L2 ou intégrer cette dépendance explicitement. Ce choix d’ordre reste proposé ; L1 seul ne constitue pas un pilote prêt à ouvrir.

**Cycle à résoudre sans attente circulaire :** FEAT-006 dépend de FEAT-014, qui dépend de FEAT-013, qui référence FEAT-006 ; FEAT-007/006 et certaines permissions sont également liés. Ces relations décrivent la cohérence du produit. 03/04/08/09/10 doivent préparer ensemble états et interfaces avant de choisir la séquence de réalisation. Une fixture de test peut exercer une interface selon contrat ; elle ne prouve pas la présence du service réel. L’ouverture exige les parcours L2/L4 et les contrôles retenus réellement intégrés. L5 et la préparation de L6 commencent dès L1 ; leur fin exige les catégories et systèmes réellement déployés.

### États d’un lot et d’une contribution — PROPOSÉ

`PROPOSÉ` → `PRÉREQUIS EN REVUE` → `AUTORISÉ PAR HQ` → `EN IMPLÉMENTATION` → `EN REVUE` → `VÉRIFIÉ SUR SHA`. L’autorisation indique périmètre et décisions ; l’implémentation et la vérification ont chacune leur preuve. Publication et ouverture pilote sont deux événements supplémentaires, décidés par les propriétaires concernés. Un lot peut devenir `BLOQUÉ` à toute étape sur divergence critique ; seuls les changements dépendants sont suspendus. Un nouveau SHA invalide l’application automatique d’une revue antérieure au delta.

## 4. Règles, états, erreurs et permissions à contractualiser

### Parcours de contribution d’un développeur

Préconditions : mandat, dépôt/ref exacts, décision ou proposition clairement marquée, propriétaire et scope. Lire conventions et contrats → créer branche courte → réaliser un delta cohérent → actualiser tests/docs → exécuter contrôles pertinents → publier PR avec preuves → revue propriétaire et 21 → fusion par acteur habilité après conditions satisfaites. Une PR empilée cible sa branche parente et explique le re-ciblage après intégration de celle-ci. Pas de force-push sur branche partagée ; pas d’auto-approbation présentée comme indépendante.

| Erreur / cas limite | Réponse et reprise proposées | Preuve attendue |
| --- | --- | --- |
| Contrat absent ou versions contradictoires | Bloquer la mutation dépendante ; conserver les deux refs, demander le delta au propriétaire | INTEGRATION CONFLICT dans PR et question HQ |
| Branche parente modifiée pendant préparation | Comparer les SHA, intégrer sans écraser d’autres contributions, revoir les contrôles affectés | Nouveau diff et SHA testés |
| Échec CI / pipeline indisponible | FAIL ou BLOCKED explicite ; aucune fusion sur seul résultat d’un ancien SHA | Commande, log expurgé, correction et réexécution |
| Réseau interrompu après demande d’écriture | Interroger état de branche/commit/PR avant de répéter ; éviter PR ou changements dupliqués | Référence effectivement créée |
| Revue manquante / droits Git retirés | Publication et approbation restent distinctes ; demander acteur habilité vérifié | Avis indépendant, contrôle d’accès et événement de fusion |
| Migration concurrente ou irréversible | Contrôler ordre, compatibilité et verrous ; forward fix ou restauration documentée, jamais rollback fictif | Essai représentatif et décision DB/DevOps |

### États fonctionnels que les contrats du lot doivent couvrir

| Parcours | États/transitions candidates à faire valider | Échecs/concurrence et comportement attendu |
| --- | --- | --- |
| J01 | Activation demandée → vérifiée ; session active → révoquée/expirée ; compte suspendu | Activation consommée, erreur de récupération, retry ; état serveur autoritatif, aucune divulgation d’un compte tiers |
| J02 | Saisie → soumission → traitement média → publié/refusé ; modification/retrait selon contrat | Timeout à résultat inconnu : consulter/rejouer selon idempotence avant nouvel envoi ; fichier refusé non public ; course audience/retrait revalidée |
| J03 | Vide/chargement → page reçue ; interaction en attente → confirmée/refusée | Curseur/ordre stable à préciser ; suppression ou blocage entre pages ; aucune écriture fondée seulement sur une ancienne vue UI |
| J04/J05 | Signalement envoyé → reçu → examiné ; décision et application distinguées ; recours reçu → résultat | Accusé seulement après persistance prévue ; doublon ou double traitement selon contrat ; échec notification ne masque pas état de sanction |
| J06 | Demande vérifiée → en traitement → résultat disponible/échec ; suppression suivie par catégorie | Export expiré, job relancé, restauration ; pas de promesse d’effacement instantané ni de réussite partielle cachée |
| J07 si inclus | Adhésion en attente/acceptée/refusée ; rôle retiré, membre parti/exclu ; fermeture | Dernier responsable, ressource devenue privée : contrat décidé avant code, aucun pouvoir global implicite |

États UI communs : initial/vide/chargement/succès/erreur/indisponible ; refus d’accès et retrait sans fuite sur l’existence privée. 02/05/06/16 précisent libellés traduits, clavier, focus, annonces de résultats, lecture assistée et tailles d’écran. Persistance des brouillons/offline, annulation d’un traitement et délais de retry restent ouverts avec 04/15. Les codes HTTP/corps d’erreur appartiennent à 04 ; aucune nouvelle API normative n’est inventée ici.

### Matrice de couverture des permissions — propositions de critères, pas rôles adoptés

| Acteur / état | Action et ressource | Règle à obtenir du propriétaire / refus attendu |
| --- | --- | --- |
| Anonyme | Inscription, connexion, lecture éventuelle | Surface publique à décider ; aucun champ privé/session/export ; réponse sans divulgation inutile |
| Authentifié | Suivre, publier, réagir, commenter | Admissibilité, état de compte, visibilité et blocages vérifiés côté serveur |
| Propriétaire | Modifier profil/contenu, demander données | Identité et propriété revalidées ; version/concurrence ; aucun droit automatique sur les données de tiers |
| Autre membre | Lecture d’objet ou média, modification d’un tiers | Audience autorisée seulement ; modification refusée hors délégation explicite |
| Bloqué | Lecture/interactions/aperçus | Étendue exacte à décider par 01/09/14/15 ; mêmes règles sur API, URL média, fil et notification |
| Suspendu / session révoquée | Action protégée ou reprise de job | Refus selon état ; contrat précise effets sur sessions et opérations déjà acceptées |
| Opérateur interne | Consulter preuve, décider, notifier, réexaminer | Permissions distinctes, périmètre, motif et audit ; retrait de rôle effectif, aucune autorité fondée sur UI |
| Responsable communautaire | Membres, contenus et dossiers locaux | Seulement si FEAT-020 approuvée ; aucune extension aux dossiers globaux |

Les droits de contribution Git sont distincts des droits applicatifs. 00/14/21 confirment qui peut pousser, revoir, administrer ou fusionner et l’exécution des checks obligatoires (OPEN-008). Aucun compte ni règle de protection n’est ajouté par ce livrable.

## 5. Données, interfaces, migrations et observabilité

### Données et cycle de vie requis par lot

| Catégorie / origine | Finalité, champs conceptuels minimaux / visibilité | Propriétaire et cycle à définir |
| --- | --- | --- |
| Comptes/profils/sessions — membre et service | Identifiant, état, profil autorisé, références de session ; champs publics/privés explicités, secrets hors logs | 04/15/14 ; rectification, récupération, export/effacement et révocation ; pas de durée fixée ici |
| Contenus/interactions/médias — auteur et traitement | Auteur, version, audience, texte/image, alt, état, relation/réaction ; accès hérite des règles approuvées | 01/04/08/09/15 ; original/dérivés, changement de visibilité, retrait, purge, effet sur caches/liens et sauvegardes |
| Signalements/décisions/recours — membre/opérateur | Références de cible/dossier, catégorie, motif, état, acteur habilité ; preuves minimales et signalant protégés | 09/10/15/14 ; réexamen, correction, conservation des preuves et suppression différenciées à décider |
| Export/effacement — demandeur/service | Identité vérifiée, portée, état par système, résultat et expiration d’accès ; export limité au demandeur habilité | 15/04/14 ; contenu concernant des tiers, sauvegardes et reprise après restauration à contractualiser |
| Événements/mesure/logs — composants | Type, temps, résultat, corrélation et propriétés autorisées ; aucune saisie/contenu privé ou secret par défaut | 13/14/15 ; finalité, accès, rétention, export/suppression et cardinalité à décider |
| Preuves d’ingénierie — Git/CI | Décision, PR, SHA, commande, environnement et résultat ; traces expurgées et fixtures synthétiques | 20/18/21/14 ; accès au dépôt privé, durée des artefacts CI et traitement d’incident à préciser |

Les lieux de stockage applicatifs, champs physiques et durées sont NON REÇUS. Un modèle conceptuel ne constitue pas une migration autorisée. Les données de production ne servent pas de fixtures. Le système de sauvegarde devra préciser ce qu’une restauration réintroduit et comment réappliquer les restrictions/suppressions requises avant réouverture.

### Fiches de contrat attendues, sans inventer d’API ou de DB

Les regroupements suivants sont des demandes à 04/03, pas des identifiants de contrat déjà attribués. Chaque fiche aura ID/version, producteur/consommateur, auth et droits, entrée/sortie, validation, erreurs, timeout, retry, idempotence, concurrence, quotas, corrélation/audit, compatibilité/dépréciation et tests.

| Groupe / FEAT | Producteur → consommateur | Entrée/sortie conceptuelle | Sémantique à préciser / panne et reprise |
| --- | --- | --- | --- |
| Identité, FEAT-001 à 004 | 04 → 05/06/10 | Données admises, preuve de récupération → état, session et vue filtrée | Expiration/révocation, limitation et non-divulgation ; réseau après succès inconnu ; tests J01 |
| Publication/média, FEAT-006/007 | 04/08 → client/fil/modération | Texte, média autorisé, audience, référence de tentative → ID/version/état | Réessai sans doublon, résultats de traitement, taille/formats, restriction ; tests J02 |
| Fil/interactions, FEAT-005/008 à 012/022 | 04 → clients et notification | Curseur, relation/action, cible/version → vue permise et résultat | Ordre/départage, changement de droits, quotas, notification privée ; tests J03/J04 |
| Modération/recours, FEAT-013 à 015/017 | 04/09/10 → console/auteur | Cible, catégorie, motif, décision/version → dossier, effet et notification distincts | Atomicité/intention durable à évaluer ; double sanction interdite ; timeout ou notification échouée ; J04/J05 |
| Droits données, FEAT-016 | 04/15 → demandeur/opérateur/job | Demande vérifiée/portée → état par catégorie, accès export contrôlé | Job interrompu/doublon, expiration, tiers et sauvegarde ; J06 |
| Mesure et signaux, FEAT-019 | Composants → 13/14 | Schéma minimal/version/corrélation → réception/état de traitement | Perte/doublon et indisponibilité sans fuite ; méthode de collecte et rétention validées avant instrumentation |

Aucun timeout, quota, délai d’effacement ou mécanisme de queue n’est choisi par 20. La perte d’une dépendance doit produire un état contrôlé, un résultat observable et une reprise documentée. Le contrat définit si l’opération peut être répétée et pendant quelle durée ; un timeout ne prouve pas son échec métier. Choisir une seule source contractuelle, puis produire les modèles clients adaptés ; les outils et versions seront décidés avec 03/04/05/06/14.

### Contribution et changement de schéma

Reprendre CONTRIBUTING et les conventions du dépôt : branche courte, nommage anglais explicite, petit delta, référence de décision, tests pertinents et revue avant fusion. Les règles strictes de TypeScript/Dart/Python du brouillon historique sont conditionnées au choix de stack. Un check de format/analyse correspond au langage effectivement retenu. Une dépendance future doit avoir justification, licence, maintenance, vulnérabilités, coût et propriétaire examinés au moment de l’ajout ; aucun paquet ni lockfile ajouté ici.

Chaque modification de données comporte raison, owner 04, avis 15/14 si pertinent, schéma/version, invariants, compatibilité anciens/nouveaux clients/jobs, volumes/verrous, backfill reprenable, seuil d’arrêt, vérification, rollback possible ou forward fix/restauration. Préférer ajouter → migrer → vérifier → déprécier → retirer avec preuve d’absence de consommateurs ; aucun retrait brutal. Ordre et outil de migration à approuver après OPEN-005. Les versions de code, API, contrats et DB ne sont pas supposées identiques.

Un flag est lié à un besoin approuvé, owner, état par défaut, populations autorisées, comportement des deux états, mesure et retrait ; il n’accorde aucun droit et n’annule aucune migration. Le ciblage par pays/communauté et les traitements induits restent à revoir avec 01/15. Les composants critiques auront logs structurés sans secrets/contenus privés, métriques, health checks et traces utiles ; 14 fixe leur protocole, accès et alertes. Mesurer les performances sur un parcours et une charge définis avant optimisation ou promesse de capacité.

## 6. Acceptation et contrôles

Les AC-J01 à AC-J07 du document produit restent les critères métier sources (31 critères PLANNED). Les critères ci-dessous ajoutent la préparation d’intégration. IDs proposés dans l’espace 20 : REQ-2001 à 2008, TEST-2001 à 2008 ; unicité locale vérifiée, confirmation globale demandée à 17/HQ lors de l’intégration.

| Critère | Besoin / lot | Scénario et résultat attendu | Test / type | Statut et blocage |
| --- | --- | --- | --- | --- |
| REQ-2001 | Autorisation L1–L7 | Étant donné un contrat critique absent, lorsqu’un lot est proposé, alors seule l’implémentation dépendante reste bloquée et propriétaire/réponse attendue sont nommés | TEST-2001 revue de préparation | PLANNED ; revue 21/HQ NON REÇUE |
| REQ-2002 | Contrats L1–L5 | Étant donné deux clients supportés, lorsqu’un schéma change, alors compatibilité, génération et vues privées sont vérifiées pour ces versions | TEST-2002 contrat/API | PLANNED ; schémas et clients NON REÇUS |
| REQ-2003 | Visibilité L2–L4 | Étant donné un contenu devenu interdit, lorsqu’il est demandé par détail, fil ou média direct, alors aucun accès non autorisé n’est servi selon la politique approuvée | TEST-2003 API/intégration ; AC-J02-04/05, AC-J03-02, AC-J04-01 | PLANNED ; matrice 09/14/15 attendue |
| REQ-2004 | Reprise L2–L5 | Étant donné une réponse perdue après écriture, lorsqu’une tentative est rejouée, alors résultat et unicité suivent le contrat sans double publication/sanction | TEST-2004 concurrence ; AC-J02-03, AC-J05-02/03 | PLANNED ; idempotence/concurrence à valider |
| REQ-2005 | Migrations tous lots persistants | Étant donné ancienne/nouvelle version et données synthétiques représentatives, lorsqu’un upgrade/backfill est interrompu, alors reprise et compatibilité sont démontrées sans perte interdite | TEST-2005 migration/intégration | PLANNED ; modèle, outil et code NON REÇUS |
| REQ-2006 | Révocation/suppression L1/L4/L5 | Étant donné droit retiré ou demande recevable, lorsque UI, API, job ou restauration agit, alors règles approuvées et limites de conservation restent effectives | TEST-2006 permission/recovery ; AC-J01-03, AC-J05-01, AC-J06-03/04 | PLANNED ; contrats et sauvegardes NON REÇUS |
| REQ-2007 | Contribuer et exploiter L0/L6 | Étant donné un nouveau développeur et un environnement autorisé, lorsqu’il suit les guides, alors il installe, teste et modifie sans information exclusive aux conversations | TEST-2007 installation/documentation | PLANNED ; parcours applicatif BLOCKED par absence de runtime validé |
| REQ-2008 | Pilote L6 | Étant donné les lots retenus, lorsqu’une ouverture est proposée, alors tests applicatifs, review indépendante, restauration, support/modération et limites sont associés aux révisions concernées | TEST-2008 release/revue | PLANNED ; critères propriétaires et exécutions manquants |

Un scénario planifié n’est pas déclaré PASS. Les suites applicatives exécutables restent BLOCKED en l’absence d’implémentation. Toute correction ultérieure ajoute la non-régression pertinente, automatisée ou manuelle justifiée par 18.

### Inventaire des contrôles réellement présents au SHA de référence

| Contrôle | Présence observée / mécanisme | Couverture et limite |
| --- | --- | --- |
| Arborescence, nommage, fichiers requis | `scripts/repository/validate_repository.py`, fichiers suivis via Git | Liste actuelle de chemins/règles ; ne valide pas une architecture runtime |
| Liens locaux Markdown | Même script | Liens inline de fichier hors blocs de code ; pas d’ancres, URLs externes ou syntaxe de liens exhaustive |
| Fichiers sensibles / clés privées | Extensions/dossiers interdits et marqueur de clé privée | Contrôle partiel ; pas scanner complet de secrets, licences ou vulnérabilités |
| Tests du validateur | `tests/repository/test_repository_validation.py`, dix cas | Nom/liens/exemples/env/clé/structure ; tests du gate, aucun test métier |
| GitHub Actions | `.github/workflows/repository-quality.yml`, PR et push main | Checkout fixé, permissions lecture, timeout, validateur, dix tests et whitespace ; aucun déploiement |
| Espaces | `git show --format= --check HEAD` dans CI | Erreurs de whitespace du commit examiné ; pas revue sémantique |

Contrôles **manquants** avant les lots concernés : analyse/types/build du langage retenu (20/14), comparaison/génération de contrats et tests clients (04/05/06/18), tests DB/migrations/transactions (04/18), autorisations et abus (14/09/18), UI/accessibilité/localisation (02/05/06/16/18), installation/recovery/charge (14/18), détection complète de secrets et dépendances (14/20), règles de branches et reviewers (00/14/21), traçabilité automatisée FEAT→AC→tests (17/18/20). Choix des outils et seuils à proposer ; pas de taux de couverture arbitraire.

### Vérifications de cette contribution

Matérialisation locale des 42 fichiers via GitHub, comparaison de chaque contenu à son SHA blob : effectuée. Relecture mandat/modèle, FEAT/phases, statuts, dépendances et anciens brouillons : revue documentaire de 20, pas revue indépendante de 21. Les commandes exactes, résultat local et preuve CI du commit publié sont consignés dans la PR de ce livrable ; elles portent sur les fichiers du dépôt et le validateur. Aucun test applicatif, migration, benchmark, restauration ou déploiement exécuté par ce travail.

## 7. Arbitrages, dépendances et handoff ciblé

### Proposition structurante rattachée à OPEN-005, puis DEC/ADR à enregistrer par l’autorité

| Champ | Proposition pour examen |
| --- | --- |
| Objectif / problème | Permettre une tranche vérifiable sans multiplier les stacks, services ou contrats incompatibles |
| Solution candidate | Conserver le plan de classement de #1, réaliser L1 après décision MVP/surface/architecture et préparer ensemble les interfaces L2/L4 ; une source contractuelle versionnée pour les clients |
| Alternatives / motifs | Créer toutes les applications/services immédiatement : coût et owners non démontrés ; maintenir des modèles clients manuels indépendants : risque de dérive ; démarrer par publication : nécessite d’emblée média/visibilité/modération. Rejets seulement proposés, pas décidés |
| Dépendances | INT-0001/0003/0004/0005/0008, OPEN-002/005/007 ; 04/05/06/08/10/14 |
| Impact business | Réduit le travail repris ; ne livre pas encore la valeur sociale complète. Aucun budget ou délai estimé sans capacité connue |
| Impact technique | Contrats et migrations compatibles, ownership explicite ; choix du langage, workspace, générateur et processus reporté à la décision applicable |
| Risques / prévention | L1 utilisé comme pilote incomplet : gate L6 ; interfaces définies prématurément : revue des producteurs/consommateurs ; cycle des FEAT : conception conjointe ciblée |
| Priorité / phase / autorité | P0 pour préparation MVP ; PROPOSÉ ; 00 avec 01/03/04/14/15 et consommateurs |
| Réexamen / delta | Si surface, communautés, données ou architecture changent ; actualiser seulement les lots/contrats affectés, puis relier DEC-0002/ADR approuvés |

DEC-0001 et DEC-0002 restent réservées à leur objet HQ. Aucun numéro ADR ni approbation ne leur est attribué par cette contribution.

### Demandes à transmettre — réponses NON REÇUES pour cette révision

Les repères H20-A à H20-H sont des lignes locales de cette réponse INT-0006, pas un nouveau registre de transmission. Le tableau de coordination HQ reste l’unique registre courant.

| Repère / rattachement | Destinataire et question ciblée | Livrable / delta attendu | Blocage précis |
| --- | --- | --- | --- |
| H20-A — INT-0001, OPEN-001/002/003/004 | 00/01 avec 05/06/16/19 : quelles FEAT et surfaces/langues pour L1 et le pilote ? | DEC-0001/0002, spécification MVP avec inclusion FEAT-020 et contraintes client | L1 métier ; L7 si communautés ; pas rédaction |
| H20-B — INT-0003, OPEN-005 | 03/04/14 : quelles frontières et outils, et comment résoudre le cycle 006→014→013→006 ? | Proposition architecture et contrats conjoints L2/L4 ; avis sur une source de schéma | Squelette applicatif/DB/API dépendants |
| H20-C — INT-0004/0005, OPEN-007 | 09/10/14/15 : effets du blocage, suspension, droits internes et retrait ? | Matrice par acteur/surface, dossier/recours, règles de preuve et rétention | Contrôles L1–L5 ; sécurité ouverture |
| H20-D — INT-0003/0005 | 04/08/15 : règles de reprise upload, accès direct, export et effacement ? | Contrats versionnés, cycle des données et migrations compatibles, points de restauration | L2/L5 et persistance concernée |
| H20-E — INT-0002/0009 | 02/05/06/16 : erreurs, clavier, focus, lecture assistée et langues ? | États UX et contraintes client reliés J01–J06 ; J07 conditionnel | UI concernée ; backend indépendant peut se préparer |
| H20-F — INT-0008 | 18 avec 13/14 : méthode pour REQ-2001..2008 et AC-Jxx ? | Cas et données synthétiques, environnements, signaux minimaux et critères release | Verdicts fonctionnels et L6 |
| H20-G — INT-0010 | 17 : intégrer ce delta et vérifier noms/IDs sans rescanner tout le projet | Index canonique et liens ; unicité globale proposée des REQ/TEST-200x | Non bloquant rédaction ; nécessaire à la traçabilité du lot |
| H20-H — INT-0007, OPEN-008 | 21/00/14 : revoir organisation et livrable sur SHA, confirmer reviewers/checks ? | Revue indépendante, identités, preuves des protections et critères merge | Fusion/release selon règle de contribution ; pas production de la PR |

**État : À TRANSMETTRE.** La publication de la PR dépose ce retour pour examen ; elle ne prouve pas sa lecture par les discussions ni leur approbation. Aucun état REÇU/APPROUVÉ n’est écrit à leur place dans le tableau HQ.

### Conflits et risques à porter au HQ

| Référence | Constat / risque | Conséquence, owner et mesure |
| --- | --- | --- |
| OPEN-005 / RISK-0004 | Brief historique nomme une stack ; référentiel HQ demande examen et décision | 03/HQ arbitrent ; conserver la proposition historique, ne générer ni framework ni DB depuis elle |
| OPEN-005 / RISK-0004 | Cycle de dépendances publication/modération/signalement | 03/04/08/09/10 définissent ensemble interfaces ; distinguer ordre de code et gate de lancement |
| RISK-0004 / OPEN-007 | Divergence des permissions entre client, API, jobs et médias | 14/04/08/09/15 : contrat unique, tests d’accès direct et de révocation ; impact critique si fuite |
| RISK-0002 | L1 ou contenu livré sans recours/modération opérationnels | 00/09/10/18 : conserver gate L6 ; capacité humaine et parcours de décision vérifiés avant ouverture |
| RISK-0001 | Phase/P0 pris comme approbation ou dossier pris pour service | 00/01/03 : classification proposée visible, gate par lot, pas de création anticipée |
| OPEN-008 | Workflow présent pris pour contrôle de fusion obligatoire | 00/14/21 : preuve des réglages et reviewer ; ne pas généraliser PASS documentaire à sécurité produit |
| PR #1/#2 | Contributions empilées et HEAD des équipes pouvant diverger | 20/21 : SHA exact, diff limité, re-ciblage après fusion parente et checks sur le nouveau résultat |

## 8. Compte rendu de fin d’étape / CODEBASE HANDOFF documentaire

1. **Décisions prises / à valider.** Alignement local sur chemins et numéros du mandat courant, réutilisation FEAT/INT/OPEN existants et rédaction de ce livrable. Lots, critères, recommandation L1 et contrats restent PROPOSÉS ; décisions MVP/stack/permissions attendues des autorités.
2. **Livrables et GitHub.** Nouveau `documentation/delivery/implementation-readiness.md` et lien depuis le README delivery ; version 0.1, base exacte en identification. Branche et PR de publication portent commit et preuves. API, DB/migration, dépendance, feature flag et code applicatif ajoutés : aucun.
3. **Tests.** Exécutés localement sous Linux / Python 3.12.14 sur la base examinée et ce delta : validateur du dépôt PASS (43 fichiers), dix tests du validateur PASS, contrôle des espaces PASS ; contrôle ciblé FEAT/phases/priorités et références AC PASS. Commandes et révision publiée sont consignées dans la PR ; un commit de préparation local ne vaut pas SHA distant. Aucun nouveau test applicatif ; aucun résultat PLANNED converti en PASS par rédaction.
4. **Questions ouvertes.** DEC-0001/0002, OPEN-002/003/004/005/007/008 et demandes H20 ; chaque absence bloque seulement le travail dépendant.
5. **Dépendances.** INT-0006 reçoit cette réponse de 20 ; H20-A à H20-H restent À TRANSMETTRE aux propriétaires. 21 fournit la revue indépendante ; 17 normalise le delta examiné.
6. **Risques / limites.** Scope de revue limité au SHA examiné et aux responsabilités 20. Aucun verdict complet de sécurité, conformité, fonctionnalité ou disponibilité. Pas de merge ni de déploiement. Dette technique nouvelle : aucune dérogation au code introduite ; lacunes de spécification recensées comme prérequis, pas dissimulées en dette acceptée.
7. **Suite / HQ.** Faire examiner ce retour INT-0006 ; arbitrer les questions du lot choisi ; enregistrer décisions et ownership ; autoriser uniquement le lot mûr ; relier contrats, migrations, tests et revue au commit lors de son implémentation. En cas de correction documentaire, modifier ou reverter le delta en préservant les contributions ultérieures ; aucun rollback runtime concerné.
