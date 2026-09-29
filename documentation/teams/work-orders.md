# Mandats documentaires des 21 équipes — Fondation / M0

Date : 29 septembre 2026. Émetteur : 00 — MASTER / Direction. Version documentaire initiale : 0.1.

Ce document prépare les instructions à transmettre aux discussions spécialisées. Il ne prouve ni leur envoi, ni leur réception, ni le démarrage de ces discussions. Les travaux de consolidation produits par HQ ne constituent pas une réponse indépendante des spécialistes.

## Instruction commune à transmettre avec chaque mandat

Travail documentaire autorisé dans ton domaine. Commence par un inventaire et un brouillon exploitable à partir des informations disponibles ; ne reste pas bloqué dans l'attente d'une autre équipe. Marque chaque hypothèse, chaque contrat provisoire et chaque question. Aucune hypothèse ne devient une décision par défaut. Les contrats seront ensuite confrontés aux producteurs et consommateurs concernés.

Lis les décisions et spécifications GitHub applicables avant de modifier un document. Si l'accès est indisponible, indique-le, liste les références non consultées et fournis un livrable explicitement « À PUBLIER ». Ne déclare jamais un commit, une PR, un test ou une validation réalisés sans preuve.

Toute modification importante de l'architecture, stack, sécurité, permissions, données personnelles, business model ou roadmap est une **PROPOSITION À SOUMETTRE AU MASTER et aux propriétaires concernés**. Aucun code applicatif ni choix de fournisseur n'est autorisé par ces mandats documentaires. La revue de la PR de fondation peut avancer parallèlement à la rédaction des spécifications.

Pour chaque fonctionnalité : ID stable, objectif utilisateur, phase proposée parmi MVP / Phase 2 / Phase 3 / International / Long terme, priorité P0–P3, acteurs, préconditions, parcours nominal, erreurs, permissions, données nécessaires, dépendances et critères d'acceptation observables. Pour une décision importante : objectif, problème, solution proposée, alternatives et motifs, dépendances, risques, impacts business et technique, priorité et autorité de validation. Les alternatives ne sont « rejetées » qu'après décision.

Fin de travail obligatoire : 1. décisions prises et restant à valider ; 2. livrables et références GitHub ; 3. tests exécutés et résultats, ou contrôles documentaires effectués ; 4. questions ouvertes ; 5. dépendances inter-équipes ; 6. risques et limites ; 7. prochaines étapes et informations à transmettre au HQ. Séparer tests prévus, exécutés, réussis, échoués et bloqués.

## Index des mandats et suivi de transmission

État initial à la préparation de ce document : **PRÉPARÉ / À TRANSMETTRE**, réponses spécialistes **NON REÇUES**. Cet état initial est historique et ne doit pas être actualisé ici. Le [tableau de coordination HQ](../project-governance/coordination-board.md) est l'unique registre courant des transmissions, réceptions, références livrées et validations. Toute évolution y exige une preuve : lien de discussion ou accusé reçu, puis fichier/PR et commit examinés.

Le tableau ci-dessous est un index statique des responsabilités. Les équipes sont des responsabilités de discussion ; aucun compte GitHub humain n'est affecté par ce document.

| Mandat | Équipe |
| --- | --- |
| M0-TEAM-01 | Produit |
| M0-TEAM-02 | UX/UI / Design System |
| M0-TEAM-03 | Architecture / CTO |
| M0-TEAM-04 | Backend / API |
| M0-TEAM-05 | Web App |
| M0-TEAM-06 | Mobile |
| M0-TEAM-07 | IA / Recommandation / Hub |
| M0-TEAM-08 | Média / Vidéo / Caméra |
| M0-TEAM-09 | Trust & Safety |
| M0-TEAM-10 | Admin / Support |
| M0-TEAM-11 | Publicité / Ads Manager |
| M0-TEAM-12 | Créateurs / Monétisation |
| M0-TEAM-13 | Data / Analytics |
| M0-TEAM-14 | DevOps / SRE / Security |
| M0-TEAM-15 | Juridique / Privacy |
| M0-TEAM-16 | International / Localisation |
| M0-TEAM-17 | Documentation |
| M0-TEAM-18 | QA / Testing / Release |
| M0-TEAM-19 | Growth / Lancement / Communauté |
| M0-TEAM-20 | Code Source / Repository |
| M0-TEAM-21 | Intégration / Code Review |

## M0-TEAM-01 — Produit

- **Livrable propriétaire** : `documentation/product/mvp-specification.md` ; consolider les propositions HQ existantes sans les déclarer approuvées.
- **Travail** : définir la promesse du pilote, les utilisateurs et leurs besoins ; détailler inscription, profil, publication texte/image, abonnement, fil, interactions, signalement et sortie du service. Comparer MVP avec et sans communautés. Définir ce qui est exclu et ce qui justifierait son ajout.
- **Questions** : quel besoin récurrent déclenche le retour volontaire ? Quelle valeur différencie le pilote ? Quel périmètre peut être exploité et modéré avec les moyens réellement disponibles ?
- **Entrées/dépendances** : vision HQ ; hypothèses de recrutement 19, parcours 02, faisabilité 03/04/08, règles 09/15, mesure 13.
- **Acceptation documentaire** : fonctionnalités classées par phase et priorité ; parcours nominal, refus et erreurs ; critères observables ; liste des arbitrages ouverts et impacts de chaque option. Aucun budget, délai ou validation inventés.
- **Handoff** : périmètre candidat → HQ ; besoins identifiés → 02/03/18 ; hypothèses d'adoption → 19/13.

## M0-TEAM-02 — UX/UI / Design System

- **Livrable propriétaire** : `documentation/user-experience/user-journeys.md`.
- **Travail** : carte des écrans et parcours du candidat MVP ; états vide, chargement, erreur, absence de permission, suspension ; interactions clavier et lecteur d'écran ; petits écrans ; composants et contenus nécessaires.
- **Questions** : comment rendre compréhensibles l'audience d'un contenu, le fil chronologique, le blocage et les réglages ? Comment permettre de terminer une session sans encourager artificiellement le temps passé ?
- **Entrées/dépendances** : 01 pour objectifs ; 09/15 pour messages sensibles ; 16 pour langues ; 05/06 pour contraintes d'interface.
- **Acceptation documentaire** : chaque parcours relie besoin, écran, action, résultat et critère vérifiable ; contraintes d'accessibilité proposées ; décisions graphiques et fonctionnalités distinguées. Ne pas figer un framework UI.
- **Handoff** : parcours → 01/05/06/18 ; ambiguïtés privacy → 15 ; besoins de composants → 20 après validation.

## M0-TEAM-03 — Architecture technique / CTO

- **Livrable propriétaire** : `documentation/architecture/architecture-proposal.md`.
- **Travail** : frontières des responsabilités, flux de données, stockage et traitements asynchrones ; comparer architectures simples et options de croissance ; formuler les contrats nécessaires ; comparer les stacks avec critères explicites sans en adopter une seul.
- **Questions** : quelle architecture sert le pilote avec une équipe limitée ? Où se trouvent les frontières de confiance, les points uniques de panne et les coûts de migration ?
- **Entrées/dépendances** : hypothèses 01, interfaces 04/05/06, médias 08, contraintes 14/15, volumes 13/19.
- **Acceptation documentaire** : options comparées, diagramme cohérent, hypothèses de charge explicites, limites, décisions à soumettre et dépendances producteur/consommateur. Aucun objectif de capacité annoncé comme mesuré.
- **Handoff** : proposition structurante → HQ/14/15/21 ; responsabilités retenues après validation → 04/05/08/20.

## M0-TEAM-04 — Backend / API

- **Livrable propriétaire** : `documentation/backend/api-contract-candidates.md`.
- **Travail** : inventaire des ressources et opérations candidates ; schémas conceptuels de requêtes/réponses ; erreurs, pagination, authentification, autorisation, idempotence, quotas et concurrence. Décrire les invariants de données et transitions de statut sans créer de tables arbitraires.
- **Questions** : qui peut lire, modifier ou supprimer chaque ressource ? Comment éviter doubles publications, accès à un objet d'autrui et incohérences après suppression/blocage ?
- **Entrées/dépendances** : 01/03 ; consommateurs 05/06/10 ; 08 pour médias ; 09/14/15 pour contrôle et cycle de vie.
- **Acceptation documentaire** : chaque opération a un producteur, des consommateurs, exemples non personnels, erreurs et critères de test ; champs non décidés signalés ; aucune migration implémentée.
- **Handoff** : contrats candidats → 03/05/06/10/18 ; invariants et matrice d'accès → 14/15 ; contradictions → HQ.

## M0-TEAM-05 — Web App

- **Livrable propriétaire** : `documentation/web-application/web-requirements.md`.
- **Travail** : inventaire des pages publiques/privées, routes conceptuelles, sessions, formulaires, navigation, rendu des publications, accessibilité, responsive et erreurs réseau ; besoins de compatibilité navigateur à proposer.
- **Questions** : quel parcours fonctionne sur connexion limitée ? Que voit un visiteur non connecté ? Comment refléter immédiatement un blocage ou un retrait de contenu ?
- **Entrées/dépendances** : parcours 02, périmètre 01, contrats 04, médias 08, sécurité 14, langues 16.
- **Acceptation documentaire** : matrice écran → contrat → droits → états → tests ; navigateurs non testés explicitement marqués ; pas de choix de framework implicite.
- **Handoff** : écarts UI/API → 02/04 ; budgets de performance proposés → 14/18 ; besoins d'implémentation → 20 après validation.

## M0-TEAM-06 — Mobile

- **Livrable propriétaire** : `documentation/mobile/mobile-options.md`.
- **Travail** : comparer web responsive, PWA et applications natives/hybrides ; contraintes de caméra, notifications, connectivité, accessibilité, permissions et publication sur stores. Distinguer recherche M0 et développement futur non autorisé.
- **Questions** : le pilote nécessite-t-il une application installée ? Quelle valeur justifie son coût de maintenance ? Quels droits du téléphone sont réellement nécessaires ?
- **Entrées/dépendances** : 01/02/05, médias 08, sécurité/privacy 14/15, langues 16.
- **Acceptation documentaire** : tableau coût/complexité/bénéfice/limites ; phase proposée par capacité ; sources officielles datées pour restrictions de plateformes ; aucun engagement de roadmap.
- **Handoff** : arbitrage web/mobile → HQ/01/03 ; contraintes communes → 02/04/08/18.

## M0-TEAM-07 — IA / Recommandation / Hub

- **Livrable propriétaire** : `documentation/artificial-intelligence/recommendation-options.md`.
- **Travail** : séparer fil chronologique, classement, recommandation, assistance créative et aide à la modération ; proposer des options sans IA ; décrire données minimales, contrôle utilisateur, explicabilité, erreurs et coûts. Recherche uniquement pour les fonctions non retenues au MVP.
- **Questions** : quel problème exige réellement un modèle ? Comment désactiver une personnalisation ? Comment mesurer une utilité sans viser seulement le temps passé ?
- **Entrées/dépendances** : principes HQ, 01/09/13/14/15 et médias 08.
- **Acceptation documentaire** : phase et justification de chaque usage ; alternative déterministe ; données et durée d'usage proposées ; protocole d'évaluation et limites, sans résultat simulé présenté comme réel.
- **Handoff** : options → HQ/03 ; besoins de données → 13/15 ; limites de modération automatique → 09/18.

## M0-TEAM-08 — Média / Vidéo / Caméra

- **Livrable propriétaire** : `documentation/media/media-lifecycle.md`.
- **Travail** : cycle upload → validation → traitement → publication → retrait → purge ; images MVP candidates et vidéo différée ; formats, tailles, quotas, métadonnées, stockage, diffusion, original et dérivés.
- **Questions** : quand un fichier devient-il accessible ? Comment révoquer l'accès aux dérivés et liens temporaires ? Quels traitements sont indispensables et quels coûts dépendent du volume ?
- **Entrées/dépendances** : 01/03/04/05/06, analyse de risque 14, rétention 15, modération 09.
- **Acceptation documentaire** : états et échecs décrits, vérification de permissions à chaque étape, quotas proposés distincts de valeurs validées, estimation d'images séparée de vidéo et protocole de mesure.
- **Handoff** : contrats média → 04/05/06 ; coûts → 14/HQ ; retrait/purge → 09/15 ; scénarios adverses → 18.

## M0-TEAM-09 — Trust & Safety

- **Livrable propriétaire** : `documentation/trust-safety/moderation-requirements.md`.
- **Travail** : catégories de signalement, blocage/mise en sourdine, triage, décisions, justification, recours, escalade et lutte contre spam/harcèlement ; besoins humains du pilote et limites de l'automatisation.
- **Questions** : qui traite chaque dossier et sous quelle cible de délai proposée ? Comment protéger déclarant et personne visée ? Comment prévenir les abus de signalement ?
- **Entrées/dépendances** : 01/08/10, analyse 07, sécurité 14, droit/privacy 15, langues 16.
- **Acceptation documentaire** : cycle de dossier, acteurs, accès et journal d'audit proposés ; situations prioritaires et procédures d'escalade ; critères de test, sans promesse de couverture humaine non confirmée.
- **Handoff** : outils et rôles → 10/04 ; conservation/preuves → 15/14 ; capacité de lancement → HQ/19 ; tests → 18.

## M0-TEAM-10 — Admin / Support

- **Livrable propriétaire** : `documentation/administration/administration-support-requirements.md`.
- **Travail** : catalogue des tâches d'administration/support, recherche de dossiers, actions sensibles, confirmations, révocation, audit et séparation des fonctions ; rétablissement des comptes sans contournement d'authentification.
- **Questions** : quelles actions doivent être interdites ou soumises à double contrôle ? Quelles informations le support peut-il voir ? Comment annuler une action erronée ?
- **Entrées/dépendances** : 09 pour modération, 14 pour permissions, 15 pour minimisation, 04 pour contrats et 02 pour parcours.
- **Acceptation documentaire** : matrice rôle/action/périmètre/justification/audit ; erreurs et abus possibles ; actions irréversibles identifiées ; aucune permission adoptée sans revue.
- **Handoff** : matrice candidate → 14/15/HQ ; besoins API → 04 ; parcours et tests → 02/18.

## M0-TEAM-11 — Publicité / Ads Manager

- **Livrable propriétaire** : `documentation/advertising/advertising-options.md`.
- **Travail** : explorer publicité contextuelle, placements, transparence, contrôle utilisateur, annonceurs, modération des annonces et facturation ; distinguer absence de publicité au pilote, expérimentation future et produit complet.
- **Questions** : quels revenus possibles avec quels coûts et risques ? Quel ciblage peut être évité ? Comment identifier clairement une annonce et expliquer sa diffusion ?
- **Entrées/dépendances** : HQ/01 pour business, 09/15 pour règles, 12 pour créateurs, 13 pour mesure et 14 pour anti-fraude.
- **Acceptation documentaire** : alternatives et phases proposées ; hypothèses chiffrées identifiées ; collecte requise par option ; aucune régie intégrée ni revenu garanti.
- **Handoff** : business proposal → HQ ; analyses de données/ciblage → 15/13 ; besoins futurs → 03/04, sans implémentation.

## M0-TEAM-12 — Créateurs / Monétisation

- **Livrable propriétaire** : `documentation/creators/creator-economy-options.md`.
- **Travail** : documenter besoins de publication, statistiques, communauté et outils professionnels ; comparer abonnements, dons, partage publicitaire et accès payant ; coûts de versement, remboursements et fraude comme questions d'étude.
- **Questions** : quelle valeur pour les créateurs avant tout paiement ? Quel modèle reste viable après frais, support et modération ? Quelles restrictions nécessitent avis spécialisé ?
- **Entrées/dépendances** : 01/08/11/13/15/19 ; 14 pour sécurité future des transactions.
- **Acceptation documentaire** : parcours créateur séparé du système de paiement ; phases et hypothèses de revenus ; risques et dépendances ; aucun prestataire ou taux de rémunération adopté.
- **Handoff** : options économiques → HQ/11 ; exigences juridiques à vérifier → 15 ; besoins fonctionnels → 01/02 et futurs contrats → 04.

## M0-TEAM-13 — Data / Analytics / BI

- **Livrable propriétaire** : `documentation/analytics/measurement-plan.md`.
- **Travail** : proposer indicateurs d'activation, rétention utile, qualité des échanges, sécurité et coûts ; catalogue minimal d'événements avec finalité, champs, sensibilité, rétention, accès et agrégation.
- **Questions** : quelle décision chaque événement permet-il de prendre ? Peut-on répondre sans identifiant durable ? Quels indicateurs évitent de confondre volume d'activité et satisfaction ?
- **Entrées/dépendances** : 01/19 pour objectifs, 09 pour sécurité, 14 pour exploitation et 15 pour traitement de données ; demandes futures 07/11/12.
- **Acceptation documentaire** : définition et dénominateur de chaque métrique ; événement → finalité → destinataire → durée proposée ; exemples fictifs ; pas de SDK ni collecte activés.
- **Handoff** : métriques → HQ/01/19 ; schémas candidats → 04/05 ; collecte et rétention → 15/14 ; vérifications → 18.

## M0-TEAM-14 — DevOps / Cloud / SRE / Security

- **Livrable propriétaire** : `documentation/security/security-operations-requirements.md` ; revue ciblée des documents existants d'hébergement, installation et exploitation, sans duplication.
- **Travail** : modèle de menaces, authentification/sessions, secrets, accès privilégiés, CI/CD, environnements, sauvegarde/restauration, alertes et incidents ; évaluer les trois niveaux d'hébergement déjà proposés avec leurs hypothèses.
- **Questions** : quelles protections sont indispensables avant pilote ? Quels RPO/RTO sont soutenables ? Qui reçoit les alertes et réalise les restaurations ?
- **Entrées/dépendances** : 03/04/08/10/13/15/18/20 ; budget et moyens humains à confirmer par HQ.
- **Acceptation documentaire** : risques liés aux flux, mesures et tests associés ; OS/versions et budgets marqués proposés ou vérifiés ; aucun engagement de disponibilité sans preuve ; procédure d'incident et critères d'ouverture du pilote.
- **Handoff** : décisions sécurité/hébergement → HQ/03/15 ; contrôles CI → 20/21 ; procédures et tests → 17/18.

## M0-TEAM-15 — Juridique / Privacy / RGPD

- **Livrable propriétaire** : `documentation/privacy/privacy-requirements.md`.
- **Travail** : inventaire des traitements, finalités, catégories de données, destinataires, sous-traitants possibles, transferts, droits et rétention ; options de politique d'âge et pays du pilote ; documents utilisateurs et besoins d'avis juridique.
- **Questions** : quelles exigences dépendent des pays, du public mineur, des médias ou du modèle économique ? Comment traiter export, suppression, opposition et demandes de recours ?
- **Entrées/dépendances** : HQ/01/09/10/13/14/16, explorations 07/11/12.
- **Acceptation documentaire** : sources officielles datées pour les affirmations juridiques ; faits, analyses et points à faire valider séparés ; traitement → données → base envisagée → durée → droits → responsable ; aucune conformité proclamée sans examen adapté.
- **Handoff** : arbitrages pays/âge/données → HQ ; contraintes → 01/04/08/09/13/14 ; textes à normaliser → 17/02/16.

## M0-TEAM-16 — International / Localisation

- **Livrable propriétaire** : `documentation/international/localization-requirements.md`.
- **Travail** : proposer langues du pilote, variantes d'écriture, formats de dates/nombres, fuseaux, contenus multilingues, recherche Unicode, accessibilité linguistique et futures interfaces de droite à gauche ; séparer pays de recrutement et ouverture effective du service.
- **Questions** : quels contenus doivent être traduits avant ouverture ? Comment gérer traductions absentes et qualité des messages de sécurité ? Quelles langues peuvent être modérées réellement ?
- **Entrées/dépendances** : 01/02/09/15/19, implémentation future 04/05/06.
- **Acceptation documentaire** : matrice langue/interface/support/modération ; glossaire initial ; exemples de formats et caractères ; phases proposées et validation humaine nécessaire ; aucune langue déclarée supportée sans preuve.
- **Handoff** : langues/pays candidats → HQ/01/15 ; contrats et UX → 02/04/05/06 ; couverture humaine → 09/19.

## M0-TEAM-17 — Documentation

- **Livrable propriétaire** : `documentation/documentation-index.md` ; maintenir les liens vers les spécifications des propriétaires sans en recopier le contenu.
- **Travail** : index documentaire, responsabilités, conventions d'IDs, statuts, glossaire, modèles de fiches et matrice des documents manquants ; contrôler cohérence entre installation, exploitation, contrats, produit et décisions.
- **Questions** : une autre équipe peut-elle identifier la version et le statut applicables ? Où un nouveau contributeur trouve-t-il les prérequis et preuves ? Quelles contradictions nécessitent un arbitrage ?
- **Entrées/dépendances** : tous les mandats et documents publiés ; conventions existantes ; 20/21 pour workflow et 18 pour preuves.
- **Acceptation documentaire** : chaque document possède un propriétaire, un statut, des références et une fonction ; liens valides ; manque explicite ; pas de nouvelle autorité technique ni approbation implicite. Installation applicative reste non vérifiée tant qu'elle n'existe pas.
- **Handoff** : incohérences → propriétaire/HQ ; index → toutes équipes ; guide d'installation exploitable → 14/18 au moment approprié.

## M0-TEAM-18 — QA / Testing / Release

- **Livrable propriétaire** : `documentation/quality/acceptance-test-matrix.md` ; compléter la stratégie existante sans en créer une copie concurrente.
- **Travail** : exigences → risques → tests unitaires/intégration/API/E2E ; scénarios nominaux, erreurs, droits et interactions ; régressions, installation vierge, backup/restore et charge ; conditions de release et de retour arrière.
- **Questions** : quel risque chaque test couvre-t-il ? Quelles dépendances empêchent son exécution ? Quel niveau de preuve est nécessaire avant ouverture du pilote ?
- **Entrées/dépendances** : 01/02/04/08/09/10/14/15 et 20/21.
- **Acceptation documentaire** : ID, exigence, préconditions, données fictives, action, résultat attendu, statut et emplacement de preuve pour chaque test critique ; aucun PASS de test applicatif inexécuté ; couverture manquante visible.
- **Handoff** : lacunes de spécification → propriétaires ; critères de release → HQ/14/21 ; cas exécutables futurs → 20.

## M0-TEAM-19 — Growth / Lancement / Communauté

- **Livrable propriétaire** : `documentation/growth/pilot-launch-plan.md`.
- **Travail** : hypothèses de recrutement, cohortes, besoins des premiers membres, animation, retours, assistance, moyens humains et critères d'arrêt/élargissement ; scénarios de pilote avec coûts indicatifs internes.
- **Questions** : pourquoi rejoindre une communauté encore petite ? Qui crée et modère les premiers contenus ? Quels retours mesurent la valeur au-delà des inscriptions ?
- **Entrées/dépendances** : 01/09/12/13/15/16 et budget HQ.
- **Acceptation documentaire** : profils et canaux proposés sans données personnelles réelles ; calendrier conditionnel aux capacités ; mesures et seuils proposés ; aucun contact, invitation ou campagne envoyés sans autorisation spécifique.
- **Handoff** : hypothèses pilote → HQ/01 ; recrutement et langues → 16/15 ; mesure → 13 ; capacité et calendrier → 09/14/18.

## M0-TEAM-20 — Code Source / Repository / Software Engineering

- **Livrable propriétaire** : `documentation/delivery/implementation-readiness.md`.
- **Travail** : vérifier l'organisation proposée dans la PR de fondation ; préparer une matrice des prérequis d'implémentation, responsabilités des modules, conventions de contribution, dépendances de contrats et futurs lots ; recenser les contrôles automatiques existants et manquants.
- **Questions** : quelle première tranche pourrait être codée une fois autorisée ? Quels contrats, permissions et migrations manquent ? Quels documents empêchent de dépendre des conversations ?
- **Entrées/dépendances** : 01/03/04/05/08/14/17/18/21 ; état réel du dépôt et décisions HQ.
- **Acceptation documentaire** : chaque lot a entrées, propriétaires, prérequis et critères de fin ; blocages visibles ; contrôles existants distingués des futurs ; aucun code applicatif, framework ou schéma DB introduit avant validation.
- **Handoff** : état prêt/bloqué et preuves → HQ/21 ; écarts documentaires → 17 ; contrats manquants → propriétaires ; vérifications → 18.

## M0-TEAM-21 — Intégration / Code Review

- **Livrable propriétaire** : `documentation/quality/integration-review.md`.
- **Travail** : revue indépendante de la PR de fondation sur un SHA exact ; cohérence nommage/liens/CI/tests/documentation ; identifier défauts, risques, preuves et correctifs. Préparer la grille de revue des futures contributions et règles de résolution de conflits.
- **Questions** : les contrôles prouvent-ils ce que leurs comptes rendus affirment ? Une modification contredit-elle un contrat ou une décision ? Quelles protections de branche sont réellement actives ?
- **Entrées/dépendances** : PR GitHub et commit examinés, conventions 20/17, stratégie 18, exigences 14 ; absence d'accès signalée immédiatement.
- **Acceptation documentaire** : SHA, fichiers examinés, commandes réellement exécutées, constats classés par gravité et verdict motivé ; distinguer absence de défaut observé et preuve complète ; aucun merge ni approbation de soi-même au nom d'une autre équipe.
- **Handoff** : défauts → 20/propriétaire ; risques sécurité → 14 ; résultat de revue → HQ avec recommandations de fusion ou demandes de correction ; publication et fusion restent vérifiées séparément.

## Convergence documentaire et critères de sortie M0

1. Chaque équipe fournit son premier inventaire et brouillon ; les dépendances absentes deviennent des questions identifiées, jamais une raison de supposer une décision approuvée.
2. HQ rassemble les propositions dans le registre, sans réécrire silencieusement les domaines spécialisés. Produit, Architecture, Sécurité/Privacy et QA confrontent les exigences, contrats et critères de validation.
3. Les équipes productrices et consommatrices examinent les points communs : accès, médias, suppression, blocage, modération, données de mesure, langues et exploitation. Toute contradiction conserve un propriétaire et un statut ouvert jusqu'à résolution.
4. Documentation normalise les deltas arbitrés et vérifie les références. Intégration revoit les PR concernées ; les tests documentaires exécutés sont joints avec leur SHA.
5. HQ peut proposer l'ouverture d'un lot d'implémentation seulement si son périmètre, ses contrats, ses permissions, ses données, ses critères d'acceptation, ses dépendances et les risques résiduels sont suffisamment définis et validés par les autorités concernées. Une quantité de fichiers ou de réponses n'est pas un critère de maturité.

Les chemins cibles en code dans ce document sont des emplacements proposés : ils ne prouvent pas l'existence des livrables. Tout changement de chemin doit conserver un propriétaire unique et mettre à jour l'index ; les décisions transversales restent dans le registre HQ et les décisions détaillées dans `documentation/decisions/`.
