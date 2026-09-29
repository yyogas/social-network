# Exigences Juridique / Privacy / RGPD — M0

**Delta de positionnement — 30 septembre 2026 :** [DIR-012](../project-governance/decision-register.md) remplace l'ancienne audience de départ par un public universel et des priorités marketing mondiales. Correction documentaire par 21 sur instruction du porteur ; aucune nouvelle analyse juridique, validation pays ou modification de règles de données. L'option France/adultes de 15 ci-dessous reste une proposition à réexaminer.

## 1. Identification et statut

| Champ | Valeur |
| --- | --- |
| Objectif | Définir les exigences de données, de droits et de confidentialité du candidat pilote ; fournir les arbitrages au HQ avant implémentation |
| Propriétaire | 15 — Juridique / Privacy / RGPD ; aucun avocat, DPO ou reviewer humain désigné à ce jour dans les entrées reçues |
| Destinataires | HQ, 01/02/03/04/05/06/08/09/10/13/14/16/17/18 ; 07/11/12 pour les extensions |
| Date / révision | 30 septembre 2026 ; v0.3, delta de positionnement DIR-012 sur la consolidation Privacy v0.2 |
| Référence Git | PR #2, branche `documentation/m0-team-coordination`, SHA `dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957` |
| Mandat | M0-TEAM-15 et réponse à INT-0005 ; modèle de livrable spécialisé |
| Statut | PROPOSÉ — revue spécialisée et arbitrages HQ attendus ; aucune conformité générale proclamée |
| Classement | MVP candidat / Phase 2 / Phase 3 / International / Long terme, tous PROPOSÉS |
| Priorité | P0 pour confidentialité, droits et capacité juridique du lancement ; P1–P3 selon extensions |
| Périmètre | Compte, profil, relations, texte/image, visibilité, blocage, signalement, recours, mesure minimale et droits ; communautés conditionnelles |
| Blocages | DEC-0001 (public/pays), DEC-0002 (MVP), flux et fournisseurs réels, bases/rétention, revue juridique et preuves QA NON REÇUS |

Entrées : [mandat](../teams/work-orders.md), [modèle](../teams/deliverable-template.md), [plan](../documentation-plan.md), [vision](../product/product-vision.md), [catalogue](../product/feature-catalog.md), [parcours](../product/user-journeys.md), [registre HQ](../project-governance/decision-register.md), [gouvernance](../governance.md), [stratégie QA](../quality/test-strategy.md). Les propositions HQ ont été examinées comme entrées, sans approbation implicite.

Travaux réutilisés, lus localement : `SOCIAL-NETWORK-15-Privacy-Compliance-v0.1.md` (16 catégories D01–D16, LEGAL-01–07) et `SOCIAL-NETWORK-M0-Privacy-Pilot-v0.1.md` (PRIV-M0-01–12 et P01–P08). Leur publication Git antérieure n'est pas attestée. Le présent fichier rassemble les exigences utiles pour ne pas dépendre de ces pièces externes. Il ne remplace aucune décision approuvée. Les anciens IDs sont conservés ; les repères locaux H15/C15/R15 ci-dessous ne réservent aucun numéro DEC/INT/RISK global.

**CONFIRMÉ** : société déclarée en France, ambition internationale, travail documentaire et publication par PR autorisés. **PROPOSÉ** : tout comportement produit, durée candidate, permission, contrat et classement ci-dessous. **À VÉRIFIER** : qualification juridique, droit applicable à la date d'ouverture, bases légales et exceptions. **NON REÇU** : entité/contact exacts, avis d'avocat, inventaire déployé, contrats fournisseurs, AIPD, code et preuves applicatives. Une source légale consultée ne valide pas le produit.

## 2. Besoins, fonctionnalités et phases

Les douze exigences de sortie du brouillon M0 restent des propositions spécialisées. P0 signifie nécessaire avant ouverture de la fonction concernée, pas autorisation d'implémenter.

| Exigence conservée | FEAT / parcours | Acteur, besoin et résultat attendu | Phase / priorité | Précondition et succès observable |
| --- | --- | --- | --- | --- |
| PRIV-M0-01 | FEAT-001, FEAT-021 / J01 | Inscrit : comprendre finalités, responsable et textes ; distinguer CGU, notice et consentement | MVP / P0 | Entité et textes validés ; version présentée traçable, consentement facultatif séparé |
| PRIV-M0-02 | FEAT-002, FEAT-003 / J01 | Membre : profil minimisé ; email, sécurité et assurance d'âge restent privés | MVP / P0 | Schéma des champs validé ; réponses de tiers expurgées |
| PRIV-M0-03 | FEAT-004, FEAT-006–011 / J02–03 | Auteur/lecteur : audience comprise et contrôlée sur tous les chemins | MVP / P0 | Matrice d'audience approuvée ; accès direct interdit réellement refusé |
| PRIV-M0-04 | FEAT-007 / J02 | Auteur : traitement d'image et purge couvrant original et dérivés | MVP / P0 | Inventaire média ; EXIF sensibles absents des fichiers servis |
| PRIV-M0-05 | FEAT-005, FEAT-012, FEAT-020 / J04, J07 | Membre : blocage cohérent ; communauté seulement si retenue | MVP / P0 | Effets décidés par 01/09 ; absence de contournement sur surfaces maîtrisées |
| PRIV-M0-06 | FEAT-013–015, FEAT-017 / J04–05 | Signalant, cible, agent : dossier confidentiel, décision et recours distincts | MVP / P0 | Qualification DSA et rôles examinés ; pas de révélation ordinaire du signalant |
| PRIV-M0-07 | FEAT-003, FEAT-016 / J06 | Personne : accès, rectification, portabilité admissible, opposition et limitation | MVP / P0 | Identité proportionnée et inventaire ; réponse motivée et sécurisée |
| PRIV-M0-08 | FEAT-006, FEAT-007, FEAT-016 / J06 | Personne : retrait/suppression vérifiables sur toutes les copies maîtrisées | MVP / P0 | Rétention et exceptions arbitrées ; purge contrôlée et restauration sans republication |
| PRIV-M0-09 | FEAT-011, FEAT-019 | Visiteur/membre : choix de traceurs et absence de collecte facultative imposée | MVP / P0 si collecte | Inventaire terminal/serveur ; refus et retrait effectivement propagés |
| PRIV-M0-10 | FEAT-001, FEAT-004 / J01 | Candidat à l'inscription : admissibilité par politique datée, possibilité de contestation | MVP / P0 | DEC-0001 et assurance d'âge examinées ; aucun âge juridique universel codé |
| PRIV-M0-11 | FEAT-007, FEAT-016, FEAT-019 | Personne : destinataires/transferts connus, demandes propagées aux prestataires | MVP / P0 | Contrats et localisations vérifiés ; accusés des opérations conservés |
| PRIV-M0-12 | Transverse, FEAT-017 | Responsable : registre, rétention, incidents et responsabilités exploitables | MVP / P0 | Responsables nommés, revue de nécessité AIPD/DPO et exercices avant ouverture |

| Fonctionnalité différée du catalogue | Phase proposée | Fondation Privacy nécessaire / raison du report |
| --- | --- | --- |
| FEAT-023 recherche | Phase 2 / P1 | ACL, extraits, index et retrait ; ne pas introduire un moteur de recherche au MVP par cette exigence |
| FEAT-024 messagerie | Phase 2 / P2 | Confidentialité des participants, modèle de chiffrement, signalement volontaire, copies et effacement à arbitrer |
| FEAT-025 mobile natif | Phase 2 / P2 | SDK, permissions appareil, push et caches locaux ; permissions OS distinctes du consentement juridique |
| FEAT-026 vidéo | Phase 2 / P2 | Droits musicaux/image, variantes, modération et rétention avant activation |
| FEAT-027 statistiques créateurs | Phase 2 / P2 | Agrégats, petits groupes et absence de révélation individuelle |
| FEAT-028 comptes professionnels | Phase 2 / P2 | Rôles des gestionnaires, révocation et qualification des responsabilités |
| FEAT-029 recommandation | Phase 3 / P2 | Base propre, contrôle utilisateur, profilage sensible et analyse des décisions automatisées |
| FEAT-030 publicité | Phase 3 / P2 | Contextuelle à comparer au profilage ; consentements, restrictions mineurs/sensible, transparence et responsabilités des acteurs ; aucune collecte anticipée de signaux ads proposée |
| FEAT-031 paiements | Phase 3 / P2 | Contrats créateurs, fiscalité, KYC selon qualification, prestataire et rétention financière distincte |
| FEAT-032 ouverture de régions | International / P1 | Fiche pays approuvée avant ouverture ; ce label ne reporte pas les obligations des pays réellement servis au pilote |
| FEAT-033 direct vidéo | Long terme / P3 | Droits territoriaux, arrêt de diffusion, capacité de traitement des abus |
| FEAT-034 intégrations/portabilité avancée | Long terme / P3 | Scopes, accès tiers, révocation ; les droits RGPD de FEAT-016 restent candidats MVP |
| D16 contacts, position précise, biométrie/AR | Long terme / P3, exploration hors catalogue actuel | Pas de collecte proposée au pilote ; besoin et éventuel nouvel ID à décider avec 01/HQ |

## 3. Parcours, états, erreurs et cas limites

### 3.1 Information et choix — PRIV-M0-01/09/10

Parcours : ouvrir le service → déterminer la politique admissible → afficher les notices dans une langue supportée → effectuer un choix par finalité facultative → enregistrer version et résultat → permettre consultation/retrait. CGU acceptées, notice consultée, réglage d'audience et consentement sont quatre objets distincts. Une notice ne demande pas un consentement global à tous les traitements.

États proposés : `UNSET`, `DENIED`, `GRANTED`, `WITHDRAWN`, `REVIEW_REQUIRED`. Seul `GRANTED` sur une finalité/version admissible ouvre son traitement. Une nouvelle finalité reste inactive jusqu'au choix requis ; elle n'hérite pas d'un accord ancien. Sans inventaire qualifiant l'exemption d'un traceur, ne pas le traiter comme nécessaire. Une mesure serveur doit aussi être examinée ; absence de cookie ne signifie pas absence de donnée personnelle. Sources S1/S4.

Échecs : politique absente ou conflit de règles → `POLICY_REVIEW_REQUIRED`, conserver les canaux de droits/support ; service de préférences indisponible → `CHOICE_NOT_SAVED`, aucun succès affiché. Pour un retrait, arrêt local immédiat des composants facultatifs, reprise de la propagation serveur avec alerte si échec. Concurrence entre appareils : numéro de version, refus d'une écriture périmée, relecture ; un ancien accord ne réactive pas un retrait plus récent. Toutes ces règles sont des propositions de contrat à revoir par 04/14.

UX : accepter/refuser au même niveau de simplicité, personnalisation lisible, aucun choix précoché, réglages accessibles au clavier, focus rendu au message d'erreur, état annoncé aux lecteurs d'écran. Les libellés d'âge ne doivent pas pousser à mentir. Les textes non traduits sont un blocage pour l'ouverture dans la langue concernée, à arbitrer avec 16.

### 3.2 Visibilité, blocage et médias — PRIV-M0-02 à 05

Proposition d'audience initiale restreinte, avec passage au public explicite ; les audiences exactes et leur défaut restent à décider par 01/09/14/HQ. Aucun droit ne découle du simple fait de connaître une URL.

Parcours : choisir audience → afficher résumé → contrôler l'autorisation lors de la publication et de chaque lecture → appliquer tout changement à profil, contenu, commentaire, média, aperçu, notification et cache. États : brouillon, traitement média, visible selon audience, restreint, retiré, purge en cours, purgé. Si une restriction n'est pas appliquée partout, l'interface indique le traitement en cours et le service refuse les accès concernés plutôt que d'annoncer une protection acquise.

Retrait de membre/rôle ou blocage pendant une lecture/écriture : revalider le droit avant livraison ou mutation ; les jobs déjà en file doivent vérifier l'état courant. Ne pas promettre l'effacement de captures ou de copies hors contrôle. Un contenu public peut être vu hors connexion : le blocage n'est pas une garantie d'invisibilité universelle. Aucun statut de blocage ni appartenance confidentielle ne doit être révélé par un code d'erreur trop précis.

Image : conserver séparément original privé et variantes autorisées ; suppression des EXIF sensibles avant diffusion, original non accessible par URL devinable ; inventaire de chaque variante et de sa purge. Si le traitement échoue, fichier non publié, reprise bornée et nettoyage des objets orphelins. Un retrait de sanction ne republie jamais un média dont l'auteur a demandé l'effacement.

### 3.3 Accès, portabilité, rectification, opposition et limitation — PRIV-M0-07

Canal authentifié et canal alternatif utilisable sans accès au compte, y compris pour non-membre ou personne suspendue. Réception horodatée → vérification proportionnée → qualification du droit → collecte limitée dans les systèmes → revue des tiers/exceptions → réponse → preuve minimale. La demande reçue commence son suivi avant la vérification ; ne pas remettre arbitrairement son horloge à zéro.

États : `RECEIVED` → `IDENTITY_CHECK` si doute → `QUALIFIED` → `IN_PROGRESS` → `REVIEW` → `ANSWERED` → `CLOSED`. Branches : `NEEDS_INFORMATION`, `PARTIAL`, `REFUSED_WITH_REASON`, `RETRY_PENDING`. Chaque refus/restriction exige un motif et les voies de contestation. Un statut d'export disponible n'est pas la clôture automatique de tous les droits du dossier.

Accès et portabilité diffèrent : l'accès porte sur les données personnelles et les informations dues ; la portabilité vise son périmètre admissible de données fournies, traitement automatisé et base contrat/consentement. Un export JSON/CSV accompagné d'une notice lisible est proposé. Ne pas appliquer le seul filtre de portabilité à une demande d'accès. Protéger les tiers par examen/occultation, sans refus global automatique. Sources S2.

Rectification : modification directe des champs éditables, vérification d'un nouvel email selon 14, dossier pour données non éditables, propagation aux destinataires lorsque requise. Opposition : distinguer prospection et autres traitements ; décision motivée sur chaque finalité. Limitation : suspendre les usages concernés, conserver sous accès restreint ; notifier la reprise lorsque requise. Le retrait d'un consentement n'efface pas automatiquement toutes les preuves d'un traitement passé.

Échecs : `IDENTITY_UNRESOLVED` → demande d'éléments strictement nécessaires, pas de pièce d'identité par défaut ; `EXPORT_EXPIRED` → renouvellement sécurisé ; `DEPENDENCY_UNAVAILABLE` → reprise sans export incomplet annoncé comme complet. Demandes répétées liées au même dossier sans les supprimer ni les qualifier abusives automatiquement. Support chargé de répondre même si l'automatisation échoue.

Délai RGPD : réponse en principe sous un mois à réception ; prolongation de deux mois supplémentaires possible selon les conditions de l'article 12, avec motifs notifiés dans le premier mois. Proposition opérationnelle : alerte au responsable à J+7 sans qualification et J+21 sans réponse prévue ; ces alertes ne sont pas des délais légaux. Calcul calendaire à valider par 15/04, jamais remplacé silencieusement par 30 jours. Source S2.

Export : préparation → contrôle → disponible → expiré/révoqué. Téléchargement authentifié avec vérification du propriétaire à chaque accès ; URL expirante seule insuffisante. Durée proposée 7 jours, à approuver ; révocation si suppression confirmée. Ne pas envoyer l'archive en pièce jointe d'email. Journaux sans contenu de l'export ni jeton de téléchargement.

### 3.4 Suppression, exceptions et restauration — PRIV-M0-08

Distinguer retrait d'un contenu, suppression du compte et effacement au titre d'un droit. Parcours compte proposé : expliquer conséquences → authentification renforcée proportionnée → confirmation → retrait d'accès/publication et révocation des sessions → purge par système → vérification → réponse détaillée → suivi des sauvegardes/exceptions.

États : `REQUESTED`, `VERIFIED`, `ACCESS_REMOVED`, `PURGING`, `PARTIAL_RETRY`, `LIVE_PURGED`, `BACKUP_PENDING`, `COMPLETE`. Exceptions justifiées suivies dans un registre parallèle `HOLD_ACTIVE` avec objet, motif, base, périmètre, décideur, échéance/réexamen et accès. Ni exception générale « anti-fraude » ni conservation illimitée par défaut. Ne pas marquer `COMPLETE` si une copie reste légalement conservée : afficher un résultat avec réserves et périmètre exact. Source S2 pour le caractère non absolu de l'effacement ; workflow proposé par 15.

Chaque système répond par objet/version : purgé, absent, exception autorisée ou erreur. La suppression déjà exécutée est idempotente ; une erreur CDN ne relance pas la création d'un compte. Les objets reçus tardivement et les retries d'anciens jobs ne doivent pas recréer le contenu ; utiliser un marqueur minimal de suppression dont la durée couvre les copies restaurables, sous réserve de la politique de rétention.

Les sauvegardes restent hors usage courant, avec expiration planifiée et droits restreints. Après restauration : environnement isolé → réapplication des suppressions/restrictions depuis une source protégée non reculée au même point de restauration → vérification → remise en service. Si le registre manque, pas de réouverture avant résolution. Définir séparément le retrait visible, la purge active et la disparition des sauvegardes ; les valeurs sont NON REÇUES, et 30 jours du brouillon n'est pas un délai légal ni un engagement validé.

Course export/effacement : une fois effacement confirmé, révoquer l'archive et annuler sa génération ; informer la personne et proposer le canal alternatif pour les données résiduelles auxquelles elle a droit. Une purge irréversible n'a pas de bouton d'annulation fictif. Retrait d'une demande avant purge : décision contrôlée et nouvel état audité, pas de restauration silencieuse.

### 3.5 Modération, recours, textes et incidents — PRIV-M0-06/12

Signalement reçu → triage → examen habilité → décision motivée → notification → recours éventuel → décision de réexamen. Les permissions de lecture, décision, conservation de preuve et recours sont distinctes. Les délais et critères métier relèvent de 09 ; ne pas confondre recours de modération et demande RGPD. Protéger les tiers dans les notifications ; toute communication légale exceptionnelle du signalant relève d'une analyse individualisée, pas d'une promesse d'anonymat absolu.

L'applicabilité détaillée du DSA, notamment les dispositions dépendant de la qualification, de la taille et des exceptions, reste à valider par avocat. Aucun statut VLOP, aucune exemption de petite entreprise n'est présumé. Les exigences produit de recours restent proposées même si une exemption légale est ensuite applicable. Source S7, contrôle du texte consolidé requis (S9).

Documents avant ouverture : notice à couches (entité/contact, finalités/bases, destinataires, transferts, durées/critères, droits), CGU (compte, règles, licence limitée d'hébergement/diffusion, retrait, résiliation, recours), politique cookies/SDK, règles communautaires et canal droit d'auteur. Une licence UGC ne vaut pas autorisation générale pour musique, image de tiers ou entraînement IA. 15/avocat examinent les textes ; 02/16 leur accessibilité/traduction ; 17 normalise les versions. Les textes publics définitifs restent NON REÇUS car leurs données d'entrée ne sont pas fixées.

Incident de données : qualifier et documenter avec 14 ; horodatage de connaissance, personnes/données, risque, mesures, notifications et décision du responsable. Le RGPD prévoit notification à l'autorité sauf absence probable de risque, si possible sous 72 h après connaissance ; risque élevé : information des personnes sous réserve des exceptions. Source S3. Exercice proposé avant pilote, aucune simulation exécutée ici.

## 4. Permissions candidates

Toutes les lignes attendent revue 14, métiers et HQ. Contrôle serveur et refus sans divulgation ; tout accès interne sensible comporte acteur, motif, dossier et horodatage.

| Acteur | Action / ressource / portée | Autorisation candidate | Refus / limite |
| --- | --- | --- | --- |
| Anonyme | Notices, choix locaux, demande de droit alternative | Public ; aucune donnée privée renvoyée avant vérification | Pas d'accès à un export par connaissance du numéro |
| Membre propriétaire | Paramètres, droits, contenu et audience propres | Session valide ; contrôle renforcé proportionné pour export/suppression | Aucune cible fournie par le client ne permet d'agir sur un tiers |
| Autre membre | Lecture/interactions | Audience et blocages courants, ressource active | Refus cohérent détail/API/média/cache/notifications |
| Bloqué | Contenu/interactions de la relation concernée | Matrice 09/01 à fixer ; droits sur ses propres données conservés | Pas de levée du blocage via URL ou rôle ordinaire |
| Suspendu / ancien membre | Droits et recours propres | Canal sécurisé conservé, sans réactiver les fonctions sociales | Suspension ne supprime pas le canal de droits |
| Responsable de communauté | Modération locale si FEAT-020 retenue | Portée communauté et pouvoirs explicitement accordés | Ni export de membres, ni données privées globales par défaut |
| Support 10 | Recevoir/suivre un dossier | Métadonnées nécessaires, périmètre assigné | Pas de téléchargement systématique d'archives ni lecture libre des preuves |
| Privacy habilité | Qualifier droits et exceptions | Accès au dossier nécessaire ; export/revue attribuables | Pas d'accès analytique réutilisable à tous les contenus |
| Modérateur 09 | Preuves nécessaires au dossier | Accès limité, contrôlé à chaque consultation | Pas de collecte globale de profils ou signalants |
| Sécurité/SRE 14 | Journaux, incident/restauration | Accès temporaire justifié, journalisé et révocable | Pas d'usage métier des données de sauvegarde |
| Worker / sous-traitant | Exécuter tâche autorisée | Identité de service, finalité/objets bornés, version valide | Aucun jeton global transmis dans une tâche ou un journal |

## 5. Données et cycle de vie

### 5.1 Règles communes et registre candidat

Les emplacements sont logiques : aucun moteur DB, prestataire ni région n'est adopté. Pour chaque ligne : chiffrement transit, stockage et sauvegardes proposé, clés séparées et accès au moindre privilège ; cela ne signifie pas chiffrement de bout en bout. Mots de passe hachés, secrets récupérables dans un coffre. Les preuves/exports ne sont pas copiés dans l'analytics. Les données pseudonymisées restent traitées comme personnelles.

`A/R/E/L/P` : accès, rectification, effacement, limitation, portabilité selon son périmètre légal ; opposition pour base intérêt légitime, retrait pour consentement. Ces droits sont instruits selon le cas, sans garantir l'effacement inconditionnel. Les bases ci-dessous sont des hypothèses à tester au regard de la nécessité de chaque opération, pas une liste dans laquelle l'implémentation choisit librement. Contrat : article 6(1)(b) ; intérêt légitime : 6(1)(f), avec analyse de mise en balance ; obligation : texte précis requis. Source S1.

| ID / anciens D | Origine et données minimales / finalité | Base envisagée / responsable métier | Stockage, accès, partage possibles | Conservation candidate, modification, export et effacement |
| --- | --- | --- | --- | --- |
| P01 / D01,D14 | Formulaire : identifiant privé, pseudo, preuve minimale d'admissibilité ; compte/âge | Contrat pour compte ; âge à qualifier séparément / 01,04,15 | Compte privé ; résultat d'âge séparé ; support limité, prestataire d'identité/âge éventuel NON CHOISI | Tant que nécessaire au compte ; demandes non activées et preuves d'âge : délai à fixer ; A/R/E/L/P, correction d'âge contrôlée ; pièces supprimées au plus tôt après contrôle justifié |
| P02 / D02,D12 | Authentification : empreinte du secret, sessions, événements IP strictement nécessaires ; sécurité | Contrat pour authentification, intérêt légitime sécurité à analyser / 14,04 | Auth/coffre/journal séparés ; sécurité ; hébergeur potentiel | Sessions jusqu'à expiration/révocation ; logs 90 j issus du brouillon, PROPOSÉ à réévaluer ; pas de secrets dans export ; données personnelles de logs examinées via accès ; purge des tokens à clôture |
| P03 / D03 | Utilisateur : bio/avatar, follows, communauté éventuelle ; présence/relations | Contrat pour fonction demandée ; art. 9 à examiner si données sensibles / 01 | Profil et graphe logiques ; audience choisie ; hébergeur/CDN pour avatar | Tant que nécessaire à fonction ; historique inutile non accumulé ; A/R/E/L/P selon portée ; dissocier relations et invalider caches à suppression |
| P04 / D04 | Auteur/tiers : texte, image, commentaires, réactions, métadonnées limitées ; publication | Contrat candidat pour auteur ; données de tiers et sensibles : analyse séparée / 01,08 | Objets privés avant diffusion, variantes autorisées ; audience et modérateur par dossier ; processeur média/CDN | Jusqu'au retrait/fin de finalité ; original/variante/orphelin chacun avec purge ; export des données admissibles et protection des tiers ; éventuelle preuve en P06 séparée |
| P05 / D08 | Réglages utilisateur : visibilité, blocage, catégories de notification ; appliquer choix | Contrat ; mesures de protection spécifiques à qualifier / 01,09 | Autorisation/préférences ; services autorisés ; opérateur limité | État courant tant qu'utile ; historique minimal si justification ; A/R/E/L/P selon cas ; retirer jetons push et jobs facultatifs au retrait applicable |
| P06 / D11,D13 | Signalant/cible/support : faits, objet, preuve, décision, recours ; dossiers | Obligation identifiée ou intérêt légitime selon catégorie, art. 9/10 à examiner / 09,10,15 | Dossiers/probatoire isolés ; modérateurs/Privacy habilités ; fournisseur support potentiel | 12 mois après clôture dans brouillon, PROPOSÉ sans valeur légale ; réexamen selon recours/litige ; accès occulté des tiers ; correction annotée, purge preuves et pièces superflues |
| P07 / D07 | Événements minimaux, compteur, version du schéma ; mesure utile du pilote | Base par événement à définir ; consentement traceurs distinct de base RGPD ; exemption à démontrer / 13,15 | Mesure séparée ; analystes habilités ; fournisseur analytics éventuel NON CHOISI | Bruts 90 j dans brouillon, PROPOSÉ à réduire selon besoin ; anonymisation à démontrer ; pas de texte/image/ethnicité ; suppression des identifiants et dérivés, droits selon base |
| P08 / D08,D15 | Personne/opérateur : finalité, choix, version, date, dossier de droit, preuve et export ; exécuter/prouver | Obligation pour droits ; justification de preuve distincte / 15,10 | Registre/exports temporaires privés ; Privacy, demandeur pour archive ; mail minimal chez prestataire | Archive 7 j PROPOSÉS ; preuve à durée motivée NON REÇUE ; pièces d'identité non accumulées ; A/R/E/L avec examen des obligations résiduelles ; révocation des liens |

Chaque ligne attend : durée active chiffrée ou critère opérable, déclencheur, durée d'archive et sauvegarde, motif d'exception, destinataires nommés, région et support distant, propriétaire opérationnel, test de purge et approbation. Un chiffre candidat non validé ne peut être injecté comme valeur par défaut de production.

Couverture différée des anciennes catégories : D05 messages → FEAT-024 ; D06 signaux de recommandation → FEAT-029 ; D09 publicité → FEAT-030 ; D10 paiements → FEAT-031 ; D16 capteurs/biométrie → exploration Long terme. Registres propres avant activation, pas de collecte au nom de futures fonctionnalités.

### 5.2 Point sensible propre au projet

Le positionnement universel est CONFIRMÉ par DIR-012 ; les priorités marketing géographiques ne constituent pas des attributs d'origine à attribuer aux utilisateurs. Analyse 15 : communautés, textes et affinités pourraient révéler origine ethnique, opinions ou croyances ; leur qualification dépend du traitement. L'article 9 impose un examen distinct de l'article 6 pour les catégories particulières. Une publication accessible ne donne pas une autorisation générale de profilage. Source S1.

Proposition P0 : aucun champ obligatoire d'ethnicité, aucune inférence depuis langue/nom/relations ni segment ads/analytics ethnique. Traitement des données sensibles volontairement publiées et données d'infractions dans les signalements à examiner avec avocat (LEGAL-01/07). Ne pas censurer automatiquement toute discussion culturelle : limiter les usages et contrôler la nécessité. À transmettre à 01/07/09/11/13/HQ avant schéma ou instrumentation.

### 5.3 Sous-traitants et transferts

Inventaire NON REÇU : hébergeur DB/objets/backups, CDN, emails transactionnels, authentification/âge, support/modération, analytics et observabilité. Un service potentiel n'est pas un fournisseur sélectionné. Fiche attendue de 14/03 : entité juridique, rôle responsable/sous-traitant/conjoint, données/finalités, régions de stockage et support, sous-traitants ultérieurs, contrat, accès, effacement/restitution, incident et preuve des transferts.

Hébergement européen ne suffit pas à exclure tout transfert. Examiner destinataires et accès distants ; documenter adéquation applicable ou garanties appropriées et analyses complémentaires nécessaires. Aucun mécanisme spécifique, pays adéquat ou fournisseur certifié n'est présumé. Source S5. Échec de purge fournisseur : dossier partiel, relance/escalade, pas de clôture fictive.

## 6. Interfaces conceptuelles à formaliser par 04/03/14

Ces identifiants locaux décrivent des besoins v0.1, pas des endpoints/API approuvés. Schémas logiques seulement ; aucune migration ni implémentation.

| Repère | Producteur → consommateur | Entrée minimale → sortie | Validation / erreurs / dépendance |
| --- | --- | --- | --- |
| PRIV-IF-01 choix | Web/mobile → préférences → collecteurs | sujet vérifié ou navigateur, finalité, choix, version notice, version attendue → version reçue, état, date | Finalité/version connues ; conflit version, indisponibilité ; arrêt/reprise §3.1 |
| PRIV-IF-02 droits | Personne/canal support → gestionnaire droits | type de droit, périmètre, moyen de réponse, preuve de vérification référencée → dossier, reçu, échéance, état | Pas de secret/pièce brute dans événement ; identité insuffisante, dossier inexistant masqué |
| PRIV-IF-03 export | Gestionnaire → stores → remise sécurisée | dossier, sujet, périmètre juridique, version inventaire → manifeste des catégories, occultations/motifs, archive privée expirante | Vérifier habilitation au lancement et téléchargement ; pas de succès si un store manque |
| PRIV-IF-04 purge | Gestionnaire → DB/média/cache/mesure/fournisseurs | dossier, sujet/objets, génération, exceptions validées, échéances → accusé par store/objet/version | Purge/absent/hold/échec ; notification partielle ; aucune nouvelle donnée créée par retry |
| PRIV-IF-05 visibilité | Service d'autorisation → lecteurs/jobs/médias | ressource, acteur, version politique, état → autorisé/refus + version | Contrôle courant avant réponse ; pas de fallback permissif sur panne |
| PRIV-IF-06 politique | Politique approuvée → inscription/consentement/traitements | pays/contextes, tranche ou résultat d'âge, opération → policy_id/version, règles, statut de revue | Entrée inconnue/conflit → revue, pas d'ouverture automatique ; canal droits préservé |

Enveloppe commune proposée : `request_id`, `correlation_id`, `actor_ref`, `subject_ref`, `purpose`, `policy_version`, `received_at`, `idempotency_key` et version d'objet. Authentification de session ou de service, autorisation par action/périmètre ; aucune confiance dans un subject_id envoyé par client. Audit des décisions, transitions et erreurs sans secrets ni contenus personnels bruts.

Proposition à négocier : accusé synchrone sous 10 s, tâche asynchrone au-delà ; trois retries techniques maximum avec temporisation progressive (1/5/15 minutes) pour pannes transitoires, puis file opérateur et alerte. Aucun retry automatique sur défaut d'autorisation ou requête invalide. Ces budgets ne repoussent jamais une échéance juridique ; gestionnaire alerte avant échéance et maintient une voie manuelle. 04/14 peuvent proposer d'autres budgets avec justification.

Idempotence par dossier/opération/objet/génération ; répétition identique retourne le résultat existant, contenu différent pour la même clé → conflit. Reprise au dernier accusé vérifié, pas au début destructif de tout le lot. Verrou/version optimiste pour choix et dossiers ; effacement confirmé prévaut sur vieux jobs/export. Limites de taille et quotas NON REÇUS (04/14) ; ils ne doivent pas rendre les droits inexerçables et nécessitent canal alternatif. Compatibilité : version explicite, champs nouveaux optionnels seulement sans rupture ; changement de finalité exige revue, migration et tests. Tests §9.

## 7. Pays, mineurs et décisions structurantes

### 7.1 Politique versionnée

Le moteur proposé dans v0.1 devient ici une table de politiques et des contrats conceptuels ; aucun service architectural supplémentaire imposé. Séparer établissement, pays effectivement servis, résidence déclarée, langue, lieu d'hébergement et contexte d'âge. Ni langue kabyle ni IP ne prouve origine, résidence ou âge. Le RGPD ne cesse pas de s'appliquer automatiquement aux utilisateurs hors UE d'un responsable établi en France (analyse territoriale à confirmer).

| Marché mentionné dans la vision | Statut / phase | Validation attendue de 15/16/avocat |
| --- | --- | --- |
| France | Option pilote MVP, PROPOSÉE | Âge/assurance, textes, RGPD/traceurs, qualification plateforme, capacité support |
| Belgique, Allemagne | International ; possible pilote seulement après arbitrage | Variantes nationales mineurs/traceurs, langue, obligations locales et recours |
| Algérie | International, ouverture NON APPROUVÉE | Droit des données, conditions locales, transferts et modération ; conseil local |
| Canada | International, ouverture NON APPROUVÉE | Niveau fédéral/provincial applicable, mineurs, langues, données/transferts |
| États-Unis | International, ouverture NON APPROUVÉE | Régimes fédéraux/étatiques, enfants, droits d'auteur, publicité |
| Suisse, Royaume-Uni | International, ouverture NON APPROUVÉE | Règles nationales, jeunesse, plateforme, traceurs et transferts |

Pour chaque politique : autorité, avis, version/date d'effet, pays/public, finalités, textes, âge, méthode proportionnée, fonctions, rétention, droits, transferts, tests et procédure de retrait. En cas de conflit, suspendre la fonction concernée et faire arbitrer ; une règle simplement « la plus restrictive » ne résout pas tous les conflits de droit. La décision d'ouverture du marché appartient au HQ. Les voyages, pays inconnu et contestations de classement restent des cas à documenter avec 16.

Mineurs : la CNIL distingue le consentement aux traitements en ligne, avec accompagnement parental avant 15 ans en France ; ce n'est pas un âge d'inscription universel. Source S6. **L'état consolidé du régime français d'inscription, ses mesures d'application et les éventuelles évolutions de 2026 ne sont pas établis dans cette revue** : consultation directe Légifrance bloquée, LEGAL-02 maintenu ouvert. Un pilote annoncé adultes doit malgré tout prévoir les mineurs détectés et une assurance d'âge proportionnée, sans collecte systématique de pièce.

### 7.2 Fiches soumises au HQ

| Champ | Contribution à DEC-0001 — public/pays | Contribution à DEC-0002 — contrat MVP |
| --- | --- | --- |
| Statut/autorité | PROPOSÉ ; HQ avec 01/09/14/15/16 | PROPOSÉ ; HQ avec propriétaires |
| Objectif/problème | Pilote exploitable sans supposer couverture juridique internationale ni parcours mineurs disponible | Rendre visibilité/droits/retrait cohérents avant implémentation |
| Solution candidate | Pilote France adultes, sous revue des cas transfrontières et moyens d'assurance d'âge | FEAT-004/016 et PRIV-M0-01–12 dans critères d'ouverture ; instrumentation minimale qualifiée |
| Alternatives | Plusieurs pays adultes ; mineurs avec protections dédiées ; aucune rejetée officiellement | Réduire fonctionnalités/mesure pour réduire les traitements ; aucune option de suppression de façade recommandée |
| Dépendances | Avis LEGAL-02/06, public cible 01/19, support/modération 09/10/16 | Flux 03/04/08/13/14, textes/rétention 15, tests 18 |
| Risques/mesures | Couverture réduite par rapport au public mondial et contournement ; expliquer périmètre, vérifier contrôles proportionnés | Surcoût purge/exports ; architecture simple et inventaire exhaustif des stores |
| Impact business | Recrutement restreint, apprentissage plus limité ; coût juridique/support réduit comme hypothèse non chiffrée | Coût initial droits/modération, réduction du risque de perte de confiance |
| Impact technique | Politiques versionnées, assurance d'âge, voie de contestation ; pas de stack fixée | Contrats d'accès, suppression et restauration transverses, événements minimisés |
| Priorité/réexamen | P0 avant inscription ; réexaminer à chaque pays/public nouveau | P0 avant lot concerné ; réexaminer à nouveau store/fournisseur/finalité |
| Delta au registre | Enregistrer la décision réelle et ses limites ; aucune approbation par ce fichier | Référencer exigences, preuves attendues et exceptions acceptées explicitement |

## 8. Contradictions, validations juridiques et dépendances

### 8.1 Deltas par rapport aux brouillons

| Repère | Constat / preuve | Traitement proposé / propriétaire |
| --- | --- | --- |
| C15-01 | Brouillon pilote v0.1 groupait live avec Phase 2 ; catalogue FEAT-033 = Long terme | Alignement de ce livrable sur classement proposé HQ ; 01/HQ arbitre, aucun engagement nouveau |
| C15-02 | Référentiel v0.1 nommait ClickHouse en D07 sans décision de stack reçue | Retirer cette présupposition ici ; emplacement analytics logique ; 03/HQ propriétaire du choix |
| C15-03 | Valeurs 30 j/90 j/12 mois/7 j des brouillons pourraient être interprétées comme délais légaux | Durées candidates seulement, paramètres production bloqués sans justification ; 15/14/09/13 |
| C15-04 | France adultes proposé par 15 vs public universel et priorités marketing DIR-012 | Arbitrage DEC-0001 ; différence de périmètre proposée, pas décision contradictoire déjà approuvée |
| C15-05 | Portabilité avancée FEAT-034 différée | Ne pas différer les droits légaux de FEAT-016 ; 01/04/18 |
| C15-06 | Pays UE/EEE groupés trop largement dans premier référentiel | Pas d'extension automatique du DSA à tout pays EEE sans qualification ; revue marché par marché |

### 8.2 Avis d'avocat spécialisé requis

| ID conservé | Question précise / preuve attendue | Effet bloquant |
| --- | --- | --- |
| LEGAL-01 | Entité et responsabilités, bases P01–P08, mise en balance, art. 9/10 et nécessité DPO ; avis daté | Traitements réels avant ouverture |
| LEGAL-02 | Régime français d'inscription à la date de lancement, âge/contrôle parental et assurance proportionnée ; texte consolidé et applicabilité | Contrat d'admissibilité, y compris pilote adultes |
| LEGAL-03 | Traceurs/exemptions et futures ads ; rôles annonceur/plateforme, profilage mineurs/sensible et champ DSA | Collecte facultative du pilote ; publicité avant sa phase |
| LEGAL-04 | Durées par finalité, obligations particulières des hébergeurs/services, preuves et litiges ; calendrier documenté | Purge et promesses aux personnes |
| LEGAL-05 | Qualification DSA/droit d'auteur, CGU/licence, droit à l'image, notifications/recours et exceptions ; revue des textes | Publication texte/image ; réexamen vidéo/live plus tard |
| LEGAL-06 | Pays servis, contrats fournisseurs/transferts, autorités et contacts ; matrice documentée | Chaque ouverture et externalisation concernée |
| LEGAL-07 | Décision motivée sur AIPD et analyse des données sensibles/profilage/mineurs ; risques résiduels et éventuelle consultation | Avant traitement à risque élevé ; aucune AIPD prétendue terminée |

Ces gates sont une recommandation de gouvernance du projet, pas une affirmation que tout traitement exige légalement une consultation d'avocat.

### 8.3 Handoffs ciblés

Tous **À TRANSMETTRE** aux discussions ; publier une PR ne prouve ni réception ni validation spécialisée. HQ attribue les numéros INT globaux ; ne pas envoyer une demande de réanalyse générale.

| Repère / émetteur 15 | Destinataire | Question / livrable attendu | Blocage / delta |
| --- | --- | --- | --- |
| H15-01 (INT-0005) | HQ/01/19/16 | Quelles fonctions, pays réellement servis, âges, canaux et langues ? Décisions DEC-0001/0002 | Avant contrats d'accès et textes ; §§2,7 |
| H15-02 | 03/04 | Carte des stores, sources et destinataires ; contrats versionnés droits/visibilité/purge et calcul d'échéance | Lot FEAT-004/016 ; §§3,6 |
| H15-03 | 08/14 | Original/variantes/CDN, révocation, EXIF, backups et source de tombstones après restauration | Images et effacement avant ouverture ; §§3.2,3.4 |
| H15-04 | 09/10 | Données nécessaires aux dossiers, accès, recours, gel probatoire et échéances motivées | Modération/support avant ouverture ; P06, §4 |
| H15-05 | 13/07/11 | Dictionnaire événements/finalités ; confirmer absence d'inférence ethnique et collecte anticipée ads | Avant instrumentation concernée ; P07, §5.2 |
| H15-06 | 14/03 | Fournisseurs, régions/support, contrats, mécanismes de transferts et incidents | Externalisation avant ouverture ; §5.3 |
| H15-07 | 02/05/06/16 | Maquettes droits/refus/retrait, notice, erreur, clavier et inventaire SDK par surface retenue | Parcours réellement livrés ; §3.1–3.3 |
| H15-08 | 18 | Reprendre matrice §9, fixtures fictives, contrats et preuves d'exécution | Validation du lot puis ouverture ; aucun PASS applicatif ici |
| H15-09 | 17/21 | Indexer ce fichier, vérifier IDs et revue ciblée du delta ; préserver les statuts | Intégration documentaire, non bloquant pour poursuivre analyse |
| H15-10 | HQ/avocat | Désigner responsable Privacy/conseil, instruire LEGAL-01–07 | Lancement et traitements concernés |
| H15-11 | 11/12 | Confirmer option sans ads/paiements au pilote ; sinon delta de périmètre et flux | Non bloquant si différés ; bloque activation sinon |

## 9. Acceptation et vérification

Tous les tests applicatifs ci-dessous sont **PLANNED**, proposés à 18 ; aucun n'a été exécuté. Préconditions communes : environnement isolé, données fictives A/B/C et rôles sans privilège, versions d'API/politique et durées approuvées. Absence d'application/contrats approuvés bloque leur exécution. Les IDs TEST-PRIV-M0 sont locaux proposés ; 17/18 contrôlent l'unicité lors d'intégration. AC-J existants restent conservés.

| Critère / test proposé | Exigence / lien existant | Étant donné… lorsque… alors… | Type / statut |
| --- | --- | --- | --- |
| AC-PRIV-01 / TEST-PRIV-M0-01 | PRIV-M0-01/09 | Visiteur sans choix, ouverture puis refus : aucun dépôt/lecture soumis au consentement, refus enregistré séparément des CGU | E2E + trafic / PLANNED |
| AC-PRIV-02 / TEST-PRIV-M0-02 | PRIV-M0-02, AC-J01-04 | A consulte B : email, preuve d'âge, secrets et paramètres internes absents du profil/API | API négatif / PLANNED |
| AC-PRIV-03 / TEST-PRIV-M0-03 | PRIV-M0-03, AC-J03-02/05 | Audience de A retirée à B pendant un job : B ne reçoit plus contenu, aperçu, commentaire ni média direct | Intégration concurrence / PLANNED |
| AC-PRIV-04 / TEST-PRIV-M0-04 | PRIV-M0-04 | Image fictive avec GPS EXIF : variante publiée sans EXIF sensible, original privé refusé à tiers ; panne transformation reste non publiée | Média/API / PLANNED |
| AC-PRIV-05 / TEST-PRIV-M0-05 | PRIV-M0-05, AC-J04-01, AC-J07-01/03 | Blocage ou départ communauté confirmé : droits révoqués selon matrice, y compris sessions/cache déjà actifs | E2E/API / PLANNED |
| AC-PRIV-06 / TEST-PRIV-M0-06 | PRIV-M0-06, AC-J04-03, AC-J05-01/04 | Cible consulte dossier puis export : identité privée du signalant occultée ; rôle agent révoqué ne lit plus les preuves ; recours propre accessible | API / PLANNED |
| AC-PRIV-07 / TEST-PRIV-M0-07 | PRIV-M0-07, AC-J06-01 | Export A prêt : B, lien expiré et session révoquée sont refusés ; A reçoit périmètre qualifié et informations/occultations | API + revue métier / PLANNED |
| AC-PRIV-08 / TEST-PRIV-M0-08 | PRIV-M0-07, AC-J06-02 | Store indisponible et demande répétée : dossier unique/relié, état partiel visible, reprise sans données manquantes prétendues complètes | Intégration panne / PLANNED |
| AC-PRIV-09 / TEST-PRIV-M0-09 | PRIV-M0-07 | Rectification/opposition/limitation recevable : donnée et usages concernés corrigés/restreints, destinataires notifiés selon cas, preuve minimale | Intégration / PLANNED |
| AC-PRIV-10 / TEST-PRIV-M0-10 | PRIV-M0-08, AC-J06-03 | Suppression confirmée pendant export et purge CDN en échec : sessions/archive révoquées, état partiel, retry idempotent sans recréation | Intégration concurrence/panne / PLANNED |
| AC-PRIV-11 / TEST-PRIV-M0-11 | PRIV-M0-08, AC-J06-04 | Backup ancien restauré : marqueurs récents réappliqués avant ouverture ; registre indisponible empêche réouverture | Restauration / PLANNED |
| AC-PRIV-12 / TEST-PRIV-M0-12 | PRIV-M0-08/12 | Preuve sous hold justifié : copie limitée isolée, pas de succès global trompeur ; échéance déclenche revue puis purge autorisée | Intégration + revue / PLANNED |
| AC-PRIV-13 / TEST-PRIV-M0-13 | PRIV-M0-09 | Consentement retiré sur A puis ancien accord rejoué depuis B : pas de réactivation ; finalité nouvelle reste inactive | Concurrence/E2E / PLANNED |
| AC-PRIV-14 / TEST-PRIV-M0-14 | PRIV-M0-10 | Politique pays/âge inconnue, mineur détecté ou erreur de classement : revue et parcours de contestation, sans pièce systématique ni ouverture automatique | E2E + revue juridique / PLANNED |
| AC-PRIV-15 / TEST-PRIV-M0-15 | PRIV-M0-11 | Fournisseur sans fiche ou sans garantie documentée : activation concernée bloquée par gate ; purge sans accusé reste partielle | Revue + intégration / PLANNED |
| AC-PRIV-16 / TEST-PRIV-M0-16 | PRIV-M0-12 | Demande reçue en fin de mois et incident simulé : échéances calendaires contrôlées, escalades distinctes droits/violation, notifications motivées | Horloge contrôlée + exercice / PLANNED |
| AC-PRIV-17 / TEST-PRIV-M0-17 | PRIV-M0-09/12, §5.2 | Schéma analytics candidat contient texte privé ou attribut ethnique : collecte refusée à la revue, aucun signal équivalent dérivé implicitement | Revue schéma / PLANNED |
| AC-PRIV-18 / TEST-PRIV-M0-18 | PRIV-M0-01/07/09 | Personne sans souris, compte suspendu, langue retenue : notices/refus/droits restent lisibles et utilisables avec erreurs annoncées | Accessibilité/E2E / PLANNED |

Preuve attendue à chaque exécution : date, environnement, SHA applicatif et version politique, commande/protocole exact, données fictives, résultat, logs expurgés et propriétaire. La relecture de ce document ne vaut aucun des PASS ci-dessus.

## 10. Risques et séquence

| Repère local | Risque / impact | Propriétaire proposé / mesure / état |
| --- | --- | --- |
| R15-01 | Profilage ethnique involontaire, exposition de communauté ou opinion ; impact élevé | 15/13/07 : minimisation et analyse art. 9 ; OPEN, probabilité non mesurée |
| R15-02 | France adultes interprété comme contrôle déjà effectif ; mineurs/pays non couverts | HQ/01/16/09 : décider et tester assurance/cas limites ; OPEN |
| R15-03 | Effacement de façade ou retour après backup, divulgation durable | 04/08/14 : inventaire, accusés, restore isolé ; OPEN |
| R15-04 | Bases/durées hypothétiques devenues paramètres de production | 15/14/13/09 : fiches approuvées avant activation ; OPEN |
| R15-05 | SDK, support distant ou prestataire non inventorié | 14/05/06 : flux/contrats/transferts, contrôle trafic ; OPEN |
| R15-06 | Export/support permettant l'exfiltration des données de tiers | 04/10/14 : séparation rôles, authentification, revue/occultation ; OPEN |
| R15-07 | Mauvaise qualification DSA/droit d'auteur ou textes inexacts | 15/09/avocat : LEGAL-05 et textes adaptés aux flux ; OPEN |

Ordre proposé : (1) HQ reçoit cette réponse et décide public/MVP ; (2) propriétaires fournissent les deltas H15 ; (3) 15/avocat qualifient traitements, bases, rétention et applicabilité ; (4) 03/04/14 et métiers fixent contrats/permissions puis 02 les parcours ; (5) 18 prépare et, après implémentation autorisée, exécute les scénarios ; (6) revue des preuves et textes avant ouverture. Les recherches Phase 2/3 continuent indépendamment, sans activation de collecte.

## 11. Sources officielles et limites de vérification

Consultation datée du **29 septembre 2026**. Les analyses produit sont des propositions de l'équipe ; les sources documentent uniquement le cadre juridique cité. Vérification ponctuelle, pas veille exhaustive ni avis juridique sur droit futur.

| Source | Référence officielle / portée et état |
| --- | --- |
| S1 | [CNIL — RGPD chapitre II](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre2), articles 5–10 : principes, bases, consentement et catégories sensibles ; page consultée |
| S2 | [CNIL — RGPD chapitre III](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre3), articles 12–22 : droits, délais, portée et exceptions ; page consultée |
| S3 | [CNIL — RGPD chapitre IV](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre4), articles 25/28/30/32–37 : gouvernance, sécurité, violations, AIPD/DPO ; page consultée ; applicabilité à analyser |
| S4 | [CNIL — FAQ cookies](https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies/FAQ), page consultée, résultat indexé daté 29 avril 2026 ; [cadre traceurs](https://www.cnil.fr/fr/cookies-et-autres-traceurs/que-dit-la-loi), consentement et exemptions à qualifier |
| S5 | [CNIL — RGPD chapitre V](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre5), articles 44–49 : transferts ; page consultée ; aucun fournisseur/mécanisme concret validé |
| S6 | [CNIL — droits numériques des mineurs](https://www.cnil.fr/fr/enjeux-numeriques/les-droits-numeriques-des-mineurs), recommandation 4, résultat officiel consulté ; pas preuve d'un régime d'inscription consolidé en 2026 |
| S7 | [Commission — effets du DSA](https://digital-strategy.ec.europa.eu/en/policies/dsa-impact-platforms), résultat officiel daté 19 mai 2026 ; [protection des mineurs](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-protection-minors), 14 juillet 2025 ; portée détaillée à vérifier par avocat |
| S8 | [Légifrance — article 45](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000037823135) et [loi 2023-566](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047799533) : références du brouillon ; accès direct 403 durant cette passe, état consolidé NON VÉRIFIÉ |
| S9 | [EUR-Lex — DSA 2022/2065](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32022R2065) : accès direct limité par vérification JavaScript ; pas de nouvelle validation du texte consolidé dans cette passe |

## 12. Compte rendu et informations HQ

1. **Décisions prises / à valider** : consolidation locale, conservation PRIV-M0-01–12 et liens FEAT/J ; aucune décision structurante adoptée. DEC-0001/0002 et LEGAL-01–07 ouverts.
2. **Livrable** : ce fichier v0.3, delta DIR-012 sur la réponse M0-TEAM-15/INT-0005 ; publication par branche/PR, référence exacte et preuves dans le compte rendu de PR. Le README Privacy pointe sur cette proposition ; aucun avis spécialisé supplémentaire n'est prétendu.
3. **Tests** : 18 scénarios applicatifs PLANNED, aucun exécuté. Contrôles documentaires réellement exécutés rapportés séparément avec commandes, environnement et SHA ; ils ne prouvent pas conformité ou fonctionnement.
4. **Questions** : âge/pays/MVP (HQ/01), bases et durées (15/avocat/métiers), flux et suppression (03/04/08/14), mesure (13), recours (09/10).
5. **Dépendances** : H15-01–11, toutes à transmettre et sans accord présumé ; blocages limités au lot concerné.
6. **Risques** : R15-01–07, notamment données sensibles communautaires, effacement/restauration et politique d'âge non vérifiée.
7. **Suite / HQ** : intégrer cette contribution comme PROPOSÉE, faire arbitrer les deux fiches §7.2, attribuer les IDs globaux nécessaires, solliciter seulement les revues ciblées §§3–9. Publication GitHub et transmission aux discussions sont deux faits distincts ; HANDOFF inter-discussions **À TRANSMETTRE**.
