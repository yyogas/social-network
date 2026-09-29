# Revue indépendante d'intégration — Fondation / M0

## Identification et statut

| Champ | Valeur |
| --- | --- |
| Référence / version | SN-INT-M0-001 v0.2 — réponse spécialisée à M0-TEAM-21 et INT-0007 |
| Objectif | Vérifier la fondation documentaire et ses contrôles, puis préparer la revue des futurs lots |
| Propriétaire | 21 — Intégration / Code Review ; auteur de ce rapport, distinct du mandat producteur 20 |
| Destinataires | 00 HQ, 20 Code Source, 17 Documentation, 18 QA, 14 DevOps/Security ; propriétaires métier concernés |
| Date | 29 septembre 2026 ; vérifications effectuées à partir de 19:17 UTC |
| Statut documentaire | PROPOSÉ — réponse de l'équipe 21, à examiner ; aucune auto-approbation de cette contribution |
| Classe / priorité | Fondation nécessaire au MVP ; P0 pour preuve/revue, P1 pour fiabilité du contrôle des espaces |
| Périmètre | PR #1 sur SHA identifié ; contrôles hérités et delta documentaire de PR #2 ; grille des futurs changements |
| Exclusions | Audit sécurité exhaustif, validation juridique, prix fournisseurs, benchmark, implémentation applicative, merge et déploiement |
| Verdict PR #1 | CHANGES REQUIRED — contrôle des espaces à corriger ; décision HQ/14 sur protection et revue à formaliser |
| Verdict PR #2 | BLOCKED pour intégration de la pile tant que la fondation n'est pas corrigée/revue ; delta documentaire exploitable pour poursuivre M0 |
| Readiness produit | NOT READY — contrats et implémentation non reçus sur les SHA examinés ; aucune release évaluée |

La revue est indépendante de la rédaction de CODE SOURCE dans le mandat de cette discussion. Elle ne vaut pas approbation d'un reviewer humain nommé, ni review GitHub APPROVE. Le compte technique qui publie une contribution n'est pas assimilé à une autre équipe. OPEN-008 reste à résoudre par HQ.

### Références examinées et état des preuves

| Référence | SHA / preuve | État |
| --- | --- | --- |
| [PR #1 — fondation](https://github.com/yyogas/social-network/pull/1) | Head `8590a095d76965880e94614328a8eafbe09b93cb`, base `46a4f36ba827b978bba57acf72ed9282ecb48b8a` | CONFIRMÉ : ouverte, non fusionnée au moment de la consultation |
| [PR #2 — coordination](https://github.com/yyogas/social-network/pull/2) | Head `dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957`, base = head de #1 | CONFIRMÉ : ouverte, non fusionnée ; 15 fichiers dans le delta |
| Mandat | [M0-TEAM-21](../teams/work-orders.md), [plan](../documentation-plan.md), [modèle](../teams/deliverable-template.md) | CONFIRMÉ : sources lues ; leurs propositions métier restent PROPOSÉES |
| Gouvernance | [contribution](../../CONTRIBUTING.md), [conventions](../repository-conventions.md), [registre HQ](../project-governance/decision-register.md), [statut](../project-governance/project-status.md) | CONFIRMÉ : DIR-010/011 autorisent ce travail documentaire |
| Produit | [vision](../product/product-vision.md), [catalogue](../product/feature-catalog.md), [parcours](../product/user-journeys.md), [roadmap](../project-governance/global-roadmap.md) | PROPOSÉ : 34 FEAT, 7 parcours et 31 critères PLANNED ; pas un MVP validé |
| Historique local de 21 | Registre SN-INT-M0-001 v0.1, produit dans cette discussion avant accès au dépôt | Réutilisé par delta ; n'est pas une baseline GitHub |
| Contrats/API/permissions | Livrables spécialistes de 03/04/09/10/14/15 aux SHA examinés | NON REÇU dans ce périmètre ; ne préjuge pas des travaux d'autres branches/discussions |
| Règles détaillées de protection | API de protection : 403 ; API rulesets : 403 avec restriction d'offre | À VÉRIFIER administrativement ; la réponse de branche indique `protected: false` |
| Code applicatif | Inventaires des arbres : 32 puis 42 fichiers ; Python limité au validateur et à ses tests | CONFIRMÉ : aucune application dans ces instantanés |

Les commandes ont été exécutées sur deux exports des fichiers GitHub, puis indexés dans deux dépôts locaux temporaires pour fournir `git ls-files`. Les empreintes Git blob de chacun des 32 et 42 fichiers correspondent à leur arbre distant. Les commits locaux de ces exports ne sont pas les commits GitHub ; aucun test d'historique distant n'est déduit d'une commande sur l'historique local.

### Delta par rapport à v0.1

- Conservation de la matrice des frontières, des scénarios négatifs et de l'exigence de preuves.
- Remplacement du statut « repository non reçu » par les preuves réelles de #1/#2.
- La stack était décrite dans v0.1 comme « annoncée », sans preuve d'implémentation. Ici OPEN-005 reste explicitement ouvert : aucune stack définitive n'est ratifiée.
- Les FEAT du catalogue sont réutilisés ; les anciens numéros SN-INT-M0-01 à 10 ne deviennent pas des identifiants de fonctionnalité concurrents.
- Le Mobile natif, la vidéo enregistrée et les outils créateurs suivent désormais les propositions Phase 2 du catalogue ; le direct suit Long terme ; la monétisation Phase 3. La classification indicative de v0.1 ne prévaut pas.
- Ajout explicite des notifications, de l'export/suppression, de l'accessibilité, des langues et du respect du temps déjà présents au catalogue HQ.
- Les noms FIND-21-* et AC-INT-21-* ci-dessous sont des repères locaux de revue proposés. Aucun DEC/ADR/RISK/TEST global n'est attribué au nom d'un autre propriétaire.

## CODE REVIEW REPORT

**PR / Change ID :** #1 et delta #2, aux SHA ci-dessus.
**Équipe productrice :** fondation et coordination préparées au HQ ; responsabilités futures 20/17, sans leur attribuer une réponse spécialisée inexistante.
**Fonctionnalité :** organisation, gouvernance, contrôle documentaire et préparation de M0.
**Références MASTER :** DIR-010, DIR-011, INT-0007 ; OPEN-005/008.
**Références ADR :** aucune ADR technique approuvée reçue dans le périmètre.

### Résumé et points positifs

La réorganisation et les liens locaux des instantanés passent le validateur existant. Les tests du validateur passent localement et dans les runs GitHub consultés. La CI a des permissions `contents: read`, un délai de cinq minutes, une action checkout référencée par SHA et `persist-credentials: false`. Les documents distinguent correctement propositions, tests prévus et preuves applicatives absentes. Le catalogue et les parcours portent des IDs réutilisables.

Ces éléments constituent une fondation documentaire utile. Ils ne prouvent ni l'application des règles de revue par GitHub, ni la justesse des contrats métier futurs.

### Constats classés et demandes de correction

| ID / sévérité | Constat et preuve | Effet | Correction demandée / propriétaire / condition de clôture |
| --- | --- | --- | --- |
| FIND-21-01 — Medium, bloquant pour validation de ce contrôle | [Workflow](https://github.com/yyogas/social-network/blob/8590a095d76965880e94614328a8eafbe09b93cb/.github/workflows/repository-quality.yml#L26-L27) : `git show --format= --check HEAD`. Les logs prouvent un checkout du merge synthétique de PR. La reproduction ci-dessous renvoie 0 avec une erreur de whitespace dans la branche candidate ; le diff base/head renvoie 2. | Le check peut être vert sans couvrir le delta de la PR. Aucun défaut de whitespace actuel n'est affirmé ; le défaut concerne le garde-fou. | 20 + 14 : vérifier un diff explicite couvrant le changement, récupérer les objets requis malgré le checkout peu profond, traiter séparément PR et push. Ajouter une non-régression avec erreur sur une branche fusionnée. Clôture : ce cas échoue, le cas propre passe, le run du nouveau SHA est vérifié. |
| FIND-21-02 — High, décision de gouvernance avant merge | GET branche main : `protected: false`, `protection.enabled: false`, aucun check requis dans la réponse. Lecture dédiée : 403 « Resource not accessible by integration ». Rulesets : 403 « Upgrade to GitHub Pro or make this repository public to enable this feature ». | La présence de la CI ne rend pas obligatoires ses résultats ni une revue. Les droits détaillés de contournement ne sont pas vérifiables avec cet accès. | HQ + 14 + 20 : désigner les reviewers (OPEN-008), choisir une solution de protection compatible avec le dépôt privé, ou documenter temporairement contrôle manuel, responsable, portée et réexamen. Ne pas rendre public le dépôt pour contourner cette limite. Pas de réglage changé par cette revue. |
| FIND-21-03 — Low, preuve documentaire à actualiser | [Rapport de fondation](https://github.com/yyogas/social-network/blob/8590a095d76965880e94614328a8eafbe09b93cb/documentation/quality/validation-report.md#L11) : CI « En attente d'exécution », alors que run 36615257604 terminé avec succès et corps #1 mis à jour. | La lecture du document seul donne un statut ancien ; le commit de branche et le merge synthétique sont insuffisamment distingués. | 17/20 : ajouter une observation datée avec head, SHA effectivement checkout, lien run/job et limites ; préserver les résultats historiques. Ne pas prétendre avoir exécuté le futur commit qui ajoute la preuve. |
| FIND-21-04 — Low, amélioration locale du validateur | [Validateur](https://github.com/yyogas/social-network/blob/8590a095d76965880e94614328a8eafbe09b93cb/scripts/repository/validate_repository.py#L65-L69) vérifie l'existence physique de la destination, pas son inclusion dans les fichiers suivis. Sonde : README suivi vers un fichier local non suivi, résultat `[]`. | Un contrôle local peut réussir et le checkout propre échouer. Aucun lien actuel de ce type détecté sur l'export vérifié. | 20/18 : soit contrôler la présence dans les chemins suivis (avec règle explicite pour répertoires), soit imposer/documenter le contrôle sur checkout propre. Ajouter une non-régression pertinente si modification du validateur. Non bloquant documentaire. |
| FIND-21-05 — Low, suivi de maintenance | Les logs des deux jobs signalent l'action checkout ciblant Node 20 et forcée sur Node 24. Les jobs ont réussi. | Avertissement réel de dépendance à instruire ; pas une panne ni une vulnérabilité démontrée. | 14/20 : examiner une mise à jour compatible du SHA d'action, avec preuve et test. Version à retenir non décidée ici. |

Les constats sont OPEN à la publication de ce rapport. La correction des scripts et du workflow relève d'une PR de 20/14 ; ce livrable de revue ne modifie pas les éléments qu'il évalue.

### Sécurité, privacy, performance et données

- Sécurité : la revue porte sur le workflow et les contrôles documentaires visibles. Les permissions minimales observées sont positives ; le marqueur de clé privée n'est pas un scanner complet de secrets. Aucun test d'authentification, d'autorisation runtime ou d'isolation n'a été exécuté.
- Privacy : aucun jeu de données utilisateur réel n'a été créé pour cette revue. Les scénarios utilisent des acteurs synthétiques. Les champs, durées, finalités et exceptions des futurs traitements sont à valider par 15.
- Performance : aucun benchmark. Les coûts et capacités du comparatif d'hébergement sont des propositions ; leurs prix externes et disponibilité n'ont pas été revérifiés dans cette revue. Aucun avis d'achat ni validation de dimensionnement.
- Données/migrations runtime : sans objet pour ce delta documentaire. Les migrations futures doivent distinguer rollback applicatif, données transformées, reprise des jobs et restauration ; une sauvegarde seule ne prouve pas la réversibilité.

### Documentation, compatibilité, breaking changes et rollback

PR #1 renomme les chemins historiques `apps/docs/infra/packages` vers les dossiers documentés. Le diff GitHub énumère 30 fichiers changés et la table des conventions conserve les correspondances. Les liens actifs locaux passent sur les instantanés examinés ; les liens externes et ancres ne sont pas validés automatiquement.

**BREAKING CHANGE REPORT — chemins documentaires :** consommateurs potentiels = liens de conversations, scripts externes ou bookmarks vers les anciens chemins ; consommateurs effectifs NON REÇUS. Migration = utiliser les nouveaux chemins et conserver la table de correspondance. Compatibilité temporaire par redirection : non fournie et non décidée. Feature flag : sans objet. Rollback : revert ciblé avec revue des contributions suivantes, sans écraser les livrables des autres équipes. HQ/17/20 doivent vérifier les références externes utiles ; aucun breaking change d'API applicative ne peut être déduit de ce dépôt.

Aucun conflit métier établi entre contrats implémentés : ils ne sont pas fournis. Les questions du pilote restent ouvertes. Les dépendances circulaires de cadrage entre publication, signalement et modération ne prouvent pas une boucle de services : Architecture doit distinguer dépendance de décision, dépendance de conception et appel runtime.

### Décision et actions avant merge

- **PR #1 : CHANGES REQUIRED.** Corriger FIND-21-01 et montrer sa non-régression ; formaliser avec HQ/14 le traitement de FIND-21-02 ; actualiser la preuve FIND-21-03.
- **PR #2 : BLOCKED pour intégration de la pile.** Poursuivre la rédaction M0 est autorisé. Après résolution de #1, réexaminer seulement les deltas affectés, retargeter selon la stratégie du mainteneur puis relancer les checks. La réussite ancienne de #2 ne valide pas un nouveau SHA ou une nouvelle base.
- Les points Low indépendants peuvent être suivis avec responsable et échéance de réexamen ; toute dette volontaire doit être documentée avec raison, impact, solution, priorité et propriétaire.
- Aucun APPROVE, merge, activation de protection ni déploiement n'est effectué par ce rapport. La contribution présente demande elle-même une revue avant intégration.

## Besoin, fonctionnalités et parcours d'intégration candidats

Les phases et priorités ci-dessous reprennent le catalogue HQ au SHA examiné et restent **PROPOSÉES**. P0 ne signifie pas approuvé. Chaque groupe conserve ses FEAT ; il ne crée pas un second catalogue.

| FEAT / classe / priorité | Acteurs, résultat et préconditions | Parcours et états conceptuels à confronter aux contrats | Frontières, erreurs et preuve requise |
| --- | --- | --- | --- |
| FEAT-001 à FEAT-003 — MVP P0 | Visiteur puis titulaire ; créer un compte, accéder à un profil. Admissibilité, activation et récupération décidées par 01/14/15. | Saisie → activation attendue → accès ; profil vide/complet ; session active/expirée/révoquée ; suspension distincte. | Web/API/profil, média avatar ; entrée invalide, activation consommée, transport incertain. Même demande ne crée pas deux comptes ; session révoquée refusée. J01. |
| FEAT-004 — MVP P0 | Titulaire/lecteur ; comprendre et appliquer son audience. Matrice d'accès validée. | Audience choisie → modification confirmée → nouvelles lectures conformes ; refus et ressource indisponible. | API, fil, fichiers et dérivés, caches, notifications ; course avec changement de droit. Vérifier chaque accès secondaire ; un contenu déjà téléchargé ne peut être repris à un tiers par simple révocation serveur. J02/J06. |
| FEAT-005 et FEAT-008 — MVP P0 | Membre ; suivre puis lire un fil explicable. Règle de suivi, ordre et pagination décidés. | Suivre/ne plus suivre ; fil vide/chargement/partiel/prêt/échec ; nouvelles publications pendant lecture. | Graphe/API/fil/client ; répéter la requête, supprimer un objet entre deux pages, bloquer entre lecture et action. Ordre, départage et contrat de curseur nécessaires. J03. |
| FEAT-006 et FEAT-007 — MVP P0 | Auteur ; publier/retirer texte et image. Audience, formats, limites et validation décidés. | Préparation → traitement → publication ; rejet/échec ; retrait → purge selon politique ; brouillon persistant non présumé. | Web/API/média/stockage ; upload interrompu, fichier interdit, traitement tardif après retrait, doublon. Aucun succès affiché avant confirmation ; original et dérivés contrôlés. J02. |
| FEAT-009 et FEAT-010 — MVP P1 | Lecteur autorisé/auteur ; réagir ou commenter. Accès au post et règle de modification définis. | Soumission incertaine → confirmée/refusée ; retrait ; parent supprimé. | API/post/interactions/compteurs ; retry, concurrence, permission révoquée ; pas d'écriture interdite ni double effet. J03. |
| FEAT-011 et FEAT-022 — MVP P1 | Membre ; lire sans perdre le contrôle des notifications. Catégories, canaux et règles de diffusion fixés. | Préférence enregistrée ; événement en attente/envoyé/échoué/supprimé selon contrat ; fil vide/rattrapé. | Préférence/API/job/interface ; vérification de droits au moment pertinent, aperçu périmé, livraison répétée. Pas de fuite ni faux accusé. J03 ; notification de sanction à distinguer des préférences sociales. |
| FEAT-012 et FEAT-013 — MVP P0 | Membre/signalant/cible ; arrêter certaines interactions et déclarer un abus. Étendue du blocage et preuve admise définies. | Blocage confirmé/révoqué ; signalement saisi/en attente d'accusé/reçu/échec ; cible supprimée. | API/fil/média/notifications/modération ; double soumission, réseau perdu ; référence uniquement après réception, identité du signalant inaccessible à la cible. J04. |
| FEAT-014, FEAT-015 et FEAT-017 — MVP P0 | Opérateur habilité et personne concernée ; décision justifiée puis recours. Rôles, indépendance de réexamen et capacité humaine approuvés. | Dossier ouvert → examen → décision ; effet appliqué/en échec ; notification suivie séparément ; recours reçu/examiné/résolu. | Admin/API/dossier/audit/média/jobs ; rôle retiré, double décision, effet partiel, recours sur objet disparu. Pas de succès masquant une sanction non appliquée. J05. |
| FEAT-016 — MVP P0 | Titulaire ; exporter/supprimer selon politique. Vérification d'identité, catégories et exceptions définies par 15. | Demande vérifiée → traitement → résultat/échec ; export disponible/expiré ; suppression partielle/achevée selon contrat. | API/jobs/média/sessions/sauvegardes ; export inter-compte refusé, reprise idempotente, restauration sans réintroduction non autorisée. J06. |
| FEAT-018 et FEAT-021 — MVP P0 | Membres et opérateurs ; parcours utilisables sur surface et langues retenues. Matrices 02/05/16 approuvées. | Chargement, vide, validation, erreur, accès refusé, focus après changement d'état. | UI/API/messages traduits ; clavier, lecture assistée, réseau lent et contenu multilingue. Surface responsive proposée ; aucun navigateur ou langue marqué testé. J01/J03 et parcours critiques. |
| FEAT-019 — MVP P1 | Opérateurs du pilote ; mesurer usage et santé avec minimisation. Événements/finalités définis par 13/15. | Collecte admise/refusée ; événement reçu/rejeté/dupliqué ; instrumentation indisponible. | App/collecteur/observabilité ; pas de contenu privé ni secret ; événement dupliqué ne gonfle pas une mesure ; panne analytics n'empêche pas une action métier sauf contrat contraire motivé. |
| FEAT-020 — MVP P1 conditionnel | Membre/responsable local ; espace gouverné. OPEN-003 résolu avant contrat dépendant. | Adhésion attendue/acceptée/refusée, départ/exclusion, rôle retiré, fermeture/perte du dernier responsable. | Communauté/API/média/modération ; périmètre local distinct du global, départ et audience cohérents. J07. Aucune inclusion implicite. |
| FEAT-023 — Phase 2 P1 ; FEAT-024 à FEAT-028 — Phase 2 P2 | Recherche, messagerie, natif, vidéo enregistrée, outils créateurs, présence professionnelle. | Définition différée ; M0 relève seulement les dépendances aux droits, versions clients et cycle média. | Pas de donnée anticipée ni de nouvelle stack imposée ; vérifier plus tard recherche après retrait, appareils anciens, abus et révocation du gestionnaire. |
| FEAT-029 à FEAT-031 — Phase 3 P2 | Recommandations, publicité, revenus/paiements. | Contrats de consentement/contrôle, diffusion, état financier et déduplication à définir avant la phase. | 07/11/12/13/15/14 ; aucun événement marketing ou paiement créé au MVP par anticipation. |
| FEAT-032 — International P1 | Publics et opérations des nouveaux marchés. | Ouverture conditionnée à langues, support, modération et revue locale. | 16/09/15/14 ; contenus multilingues du pilote restent couverts par FEAT-021. |
| FEAT-033 et FEAT-034 — Long terme P3 | Direct à grande audience et intégrations développeurs. | États et contrats différés. | Arrêt d'urgence, charge, scopes, révocation, quotas et portabilité à instruire avant lancement de ces capacités. |

Les états de ce tableau sont des candidats sémantiques, pas des noms de champs ou enums d'API adoptés. Les codes d'erreur, timeouts, quotas et délais chiffrés sont NON REÇUS ; 04, 08 et 14 proposent les valeurs, les consommateurs les examinent. Une interface doit distinguer « refus définitif », « résultat inconnu après transport » et « reprise autorisée » ; un retry ne doit jamais être supposé sûr.

## Permissions, données et contrats

### Permissions à contrôler sur chaque frontière

| Acteur | Action / portée | Règle candidate et refus attendu | Autorité attendue |
| --- | --- | --- | --- |
| Anonyme | Lire profil/contenu, créer/récupérer compte | Seulement ce qu'autorise la politique publique ; absence d'information privée ou d'énumération inutile | 01/04/14/15 |
| Authentifié non propriétaire | Lire/interagir avec ressource accessible | Vérification service à chaque opération ; état du compte et audience courants | 04/14 + métier |
| Propriétaire | Modifier/retirer son objet ; demander son export | Propriété ne contourne pas suspension, modération ou autres interdictions ; vérification renforcée des actions sensibles à décider | 01/09/14/15 |
| Compte bloqué ou suspendu | Lire/interagir selon matrice | Pas d'hypothèse « tout interdit » : étendue exacte définie par 09 ; tester API, caches, fichiers et notifications concernés | 09/14/15 |
| Modérateur/support | Lire dossier, agir, voir preuve, réexaminer | Permissions distinctes ; rôle retiré effectif côté serveur ; support sans accès général implicite | 09/10/14/15 |
| Responsable communautaire | Gérer l'espace autorisé | Aucun pouvoir global déduit du rôle local ; dépend de FEAT-020 | 01/09/10/14 |

Pour un objet inexistant ou inaccessible, 04/14/15 décident la politique d'erreur (dont révélation d'existence). Aucun choix automatique de 403/404 ni permission nouvelle n'est validé par 21.

### Données et cycle de vie à relier aux preuves

| Catégorie / origine / finalité | Données conceptuelles minimales et visibilité | Propriétaire / stockage / accès interne | Cycle et cas de revue |
| --- | --- | --- | --- |
| Compte/profil — membre ; accès et présentation | Identifiant stable, état, champs approuvés ; privé/public par champ | 01/04/14/15 ; stockage et rôles NON REÇUS | Modification, export, révocation, suppression ; aucune durée inventée |
| Graphe/contenus/médias — membre ; échange | Référence auteur, audience, texte/image, références de dérivés, état | 01/04/08 ; accès interne à minimiser | Restriction/retrait sur original, dérivés, index/cache et jobs ; purge/sauvegardes selon 15 |
| Interactions/notifications — membre/service ; réponse et information | Référence acteur/objet, état et préférence applicable | 01/04 ; rôle de diffusion borné | Déduplication, suppression, destinataire autorisé, contenu d'aperçu minimal |
| Signalements/décisions/recours — signalant/opérateur ; traitement | Références, motif, état, action effective, acteur habilité | 09/10/15 ; preuves sensibles à accès distinct | Accès/export excluant données tierces non autorisées ; rétention et exceptions NON REÇUES |
| Événements/logs — service ; diagnostic/mesure | Schéma versionné, corrélation et champs nécessaires | 13/14/15 ; accès et stockage NON REÇUS | Secrets exclus ; minimisation, rétention/purge et séparation logs/analytics à examiner |
| Sauvegardes — exploitation ; reprise | Catégories couvertes, version et règles de restauration | 14/04/15 ; clés, accès, rétention NON REÇUS | Réappliquer les décisions de suppression et vérifier les droits lors de restauration |

Une suppression logique, un retrait de visibilité et une purge physique sont des transitions différentes. Leur ordre, délai, preuve et exception restent aux propriétaires. Les données de test devront être synthétiques ; aucun secret ou export utilisateur n'accompagne une preuve de PR.

### Fiche d'interface attendue avant implémentation du lot

Chaque API/événement/job doit recevoir de 04/03 un ID et une version canoniques ; 21 ne les attribue pas ici. La fiche comprend : producteur, consommateurs, authentification, autorisation, entrée/sortie, champs obligatoires/facultatifs, types, nullabilité, états, validation, erreurs, délai, retry, idempotence, concurrence, quotas, corrélation, audit, compatibilité, dépréciation et tests.

| Groupe de contrats candidats | Producteur → consommateurs | Défaillance / reprise à définir | Contrôle de compatibilité attendu |
| --- | --- | --- | --- |
| Compte/session/profil | 04 → 05/10 ; 06 si retenu | Activation expirée, session révoquée, résultat incertain ; pas de compte doublon | Champs identiques, erreurs non divulgatrices, ancienne version supportée |
| Publication/média/visibilité | 04/08 → 05/10 ; 06 si retenu | Traitement différé, upload orphelin, retrait concurrent ; reprise sans rendre visible un fichier interdit | Audience identique pour texte, original et dérivés |
| Fil/interactions/blocage | 04 → 05 ; 06 si retenu | Curseur invalidé, droit changé, double soumission | Ordre et départage documentés ; contrôle de droits au moment d'écrire |
| Signalement/modération/recours | 04/09/10 → 05/10, média et diffusion | Décision concurrente, sanction partielle, notification en échec | Séparer décision, effet et notification ; audit attribuable |
| Export/suppression | 04/14 selon architecture → 05/10/08 | Traitement partiel, lien expiré, restauration | Isolement par demandeur ; reprise sans résurrection des données |
| Mesure/observabilité | Applications retenues → 13/14 | Doublon, retard, panne collecteur, changement de schéma | Version et minimisation ; compatibilité des consommateurs |

La topologie de service, le transport synchrone/asynchrone et l'usage de Redis/OpenSearch ne sont pas inférés de cette table.

## Acceptation et vérification

### Exécutions réalisées, et seulement celles-ci

Environnement local : Linux x86_64, Python 3.12.14, Git 2.51.1. Sources obtenues via API au SHA, hashes des fichiers vérifiés avant contrôles. Aucun commit GitHub n'a été recréé localement.

| Preuve locale | Commande / méthode | Résultat observé |
| --- | --- | --- |
| Identité des exports #1 et #2 | SHA-1 Git blob = SHA-1 de `blob <taille>\0<octets>`, comparé à chaque entrée des arbres distants | PASS : 32/32 et 42/42 fichiers identiques |
| Structure, noms et liens inline | `python3 scripts/repository/validate_repository.py` dans chaque export indexé | PASS : 32 puis 42 fichiers |
| Tests du validateur | `python3 -m unittest discover -s tests/repository -p 'test_*.py' -v` | PASS : 10 tests dans chacun des deux exports, aucune erreur |
| Whitespace des instantanés locaux | `git show --format= --check HEAD` sur le commit racine local de chaque export | PASS : tous les fichiers de l'instantané ; ne teste pas la sémantique merge du workflow |
| Identifiants documentaires #2 | Expressions ancrées sur lignes du catalogue, titres des parcours/mandats et tables des AC ; vérification des références FEAT explicites | PASS : 34 FEAT uniques, 21 mandats, 7 parcours, 31 AC uniques ; aucune référence FEAT explicite orpheline |
| Sonde du check sur merge | Reproduction isolée ci-dessous, mêmes commandes Git que le workflow | Défaut confirmé : commande actuelle exit 0 ; diff base/head exit 2 |
| Sonde lien non suivi | Appel `inspect(root, ['README.md'], require_layout=False)` avec cible locale existante non incluse dans la liste | Limite confirmée : aucune erreur retournée |
| Tests applicatifs/API/E2E/sécurité/charge/install/restore | Aucune application/infra validée dans ces instantanés | NON EXÉCUTÉS ; exécution applicative BLOCKED, scénarios futurs PLANNED |

Les références FEAT sous forme d'intervalle ont été relues comme intervalles du catalogue ; le contrôle regex ne constitue pas une preuve sémantique des dépendances. La cohérence du futur contrat doit être revue par ses producteurs et consommateurs.

Les dix tests existants vérifient noms/liens valides, lien cassé, lien externe, exemple fenced, fichier environnement interdit, exemple environnement autorisé, marqueur de clé sans divulgation, sortie du dépôt, nom ambigu et layout manquant. Ils ne couvrent pas les deux sondes nouvelles ci-dessus.

### CI distante consultée, sans la confondre avec le head

| PR / head associé | Run / job | SHA réellement checkout dans le log | Résultat |
| --- | --- | --- | --- |
| #1 / `8590a095d76965880e94614328a8eafbe09b93cb` | [36615257604](https://github.com/yyogas/social-network/actions/runs/36615257604), job 109566513206 | `bdb6f3b14caa257c533a64ee4a40dbddeee701e5` — merge synthétique de #1 | completed/success ; 32 fichiers, 10 tests ; Python 3.12.3 |
| #2 / `dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957` | [36617243179](https://github.com/yyogas/social-network/actions/runs/36617243179), job 109573301675 | `06128a6ff19fe613170bca5599fd9176f1e09fd7` — merge synthétique de #2 | completed/success ; 42 fichiers, 10 tests ; Python 3.12.3 |

Les logs de checkout, validation, tests et whitespace ont été consultés. Leurs succès sont réels pour leur portée ; FIND-21-01 limite la conclusion du check whitespace. Les résultats de la PR publiant le présent rapport doivent être consignés dans son corps avec son propre SHA, sans modifier rétroactivement cette observation des sources.

### Reproduction du défaut FIND-21-01

Exécuter dans un dossier temporaire, indépendant du dépôt projet. Cette sonde ne pousse rien et n'implémente aucune fonctionnalité du réseau social.

```sh
python3 - <<'PY'
import subprocess
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory(prefix="sn-review-") as folder:
    def git(*args):
        return subprocess.run(
            ["git", "-C", folder, *args], capture_output=True, text=True
        )

    def ok(*args):
        result = git(*args)
        if result.returncode:
            raise RuntimeError(result.stderr)
        return result.stdout.strip()

    ok("init", "-q", "-b", "main")
    ok("config", "user.name", "Synthetic review")
    ok("config", "user.email", "review@example.invalid")
    (Path(folder) / "README.md").write_text("# Base\n")
    ok("add", ".")
    ok("commit", "-qm", "base")
    base = ok("rev-parse", "HEAD")
    ok("switch", "-qc", "candidate")
    (Path(folder) / "guide.md").write_text("# Candidate   \n")
    ok("add", ".")
    ok("commit", "-qm", "candidate with whitespace")
    head = ok("rev-parse", "HEAD")
    ok("switch", "-q", "main")
    ok("merge", "--no-ff", "-m", "Synthetic PR merge", "candidate")
    current = git("show", "--format=", "--check", "HEAD")
    explicit = git("diff", "--check", base, head)
    print("current:", current.returncode, "explicit:", explicit.returncode)
    print(explicit.stdout)
    assert current.returncode == 0 and explicit.returncode != 0
PY
```

Résultat observé : `current: 0 explicit: 2`, avec `guide.md:1: trailing whitespace.`. Cette reproduction confirme la faille du contrôle ; elle ne constitue pas un correctif. 20/14 doivent définir les refs du workflow réel et gérer leur récupération avant d'utiliser un diff explicite.

### Critères d'intégration à transmettre à QA

Tous les critères ci-dessous sont **PLANNED** ; les IDs de tests canoniques sont **NON REÇUS — attribution 18**. Les données seront fictives : deux membres A/B, un opérateur habilité puis révoqué, un média original avec dérivé et une publication à audience restreinte. QA précise fixtures, environnement et méthodes avant exécution.

| Critère local | FEAT / parcours | Étant donné / lorsque / alors | Type futur / propriétaire / blocage |
| --- | --- | --- | --- |
| AC-INT-21-01 | 001–003 / AC-J01-01 à 04 | Activation consommée ou session révoquée ; répéter l'accès ; aucun compte supplémentaire ni opération protégée réussie | API/contrat/E2E — 04/14/18 ; activation et sessions ouvertes |
| AC-INT-21-02 | 004/006/007 / AC-J02-01,04,05 | B a perdu l'audience ; ouvrir détail, fil, original, dérivé et aperçu ; aucune nouvelle réponse ne livre un contenu interdit suivant le contrat de propagation | API/intégration — 04/08/14/15/18 ; audience et délais ouverts |
| AC-INT-21-03 | 006/007 / AC-J02-02,03 | Réponse perdue après soumission ou traitement média en échec ; reprendre ; un seul effet et un état exact, sans publication prématurée | Intégration — 04/08/18 ; contrat de reprise ouvert |
| AC-INT-21-04 | 005/008 / AC-J03-01,03 | Nouvelles publications/suppression pendant pagination ; charger la suite ; ordre/départage et absence de doublon respectent le contrat | API/concurrence — 04/05/18 ; curseur et cohérence ouverts |
| AC-INT-21-05 | 009/010/012 / AC-J03-02, AC-J04-01 | Droits révoqués entre lecture et réaction/commentaire ; envoyer directement l'API ; refus et aucune écriture interdite | API/intégration — 04/09/18 ; matrice d'accès ouverte |
| AC-INT-21-06 | 011/022 / AC-J03-05 | Notification en attente puis contenu retiré/préférence changée ; diffuser ; aucune fuite, règle de catégorie respectée, état utilisateur compréhensible | Intégration/E2E — 01/02/04/15/18 ; catégories et notification obligatoire à distinguer |
| AC-INT-21-07 | 013 / AC-J04-02 à 04 | Cible supprimée ou envoi répété ; transmettre le signalement ; dossier cohérent et identité du signalant protégée | API/E2E — 09/10/15/18 ; preuve et rétention ouvertes |
| AC-INT-21-08 | 014/015/017 / AC-J05-01 à 05 | Deux opérateurs ou rôle retiré ; décider puis contester ; un état autorisé cohérent, audit et reprise des effets partiels | Intégration/concurrence — 09/10/14/18 ; rôles et transitions ouverts |
| AC-INT-21-09 | 016 / AC-J06-01 à 04 | Export ou suppression de A ; B tente l'accès, un job reprend et une sauvegarde est restaurée ; isolement et cycle approuvés restent respectés | API/jobs/restore — 04/14/15/18 ; politique et procédure absentes |
| AC-INT-21-10 | 018/021 / AC-J03-04 | Clavier/lecture assistée/langue retenue et réseau lent ; parcourir accès/publication/signalement ; états compréhensibles, focus et messages utilisables | E2E/accessibilité — 02/05/16/18 ; matrice de support absente |
| AC-INT-21-11 | 019 | Événement synthétique répété ou collecteur indisponible ; mesurer ; déduplication et minimisation conformes, action métier selon contrat | Contrat/intégration — 13/14/15/18 ; schémas et finalités ouverts |
| AC-INT-21-12 | 020 / AC-J07-01 à 04 | Non-membre, responsable local révoqué ou dernier responsable absent ; lire/agir ; scope et fermeture conformes | API/E2E — 01/04/09/18 ; inclusion OPEN-003 non décidée |

Les clauses AC-J existantes restent la référence Produit/QA ; ces critères les précisent aux frontières, sans les déclarer approuvées.

## Grille de revue des prochaines contributions

| Domaine de revue | Pièces et contrôle | Motif de blocage du lot concerné |
| --- | --- | --- |
| Contexte et architecture | FEAT, décision applicable, ADR, modules/propriétaires et delta | Changement structurant sans autorité ou dépendance critique ouverte |
| API/événements | Producteur/consommateurs, schémas, erreurs, pagination, versions, contrats de test | Rupture silencieuse, type renommé non propagé, retry non sûr |
| Données/migrations | Contraintes, anciens enregistrements, concurrence, durée/locks, forward, reprise et rollback | Perte/altération non contrôlée ou retour arrière supposé |
| UI/UX/clients | Design référencé, loading/vide/erreur/refus, accessibilité, API compatible | Succès faux, autorisation seulement dans UI, client supporté cassé |
| Sécurité/privacy | Droits serveur, secrets, sessions, audit, finalité et cycle données | Exposition de données, élévation de droits, traitement non examiné |
| Performance/dépendances | Budget mesurable, requêtes/payloads, version/licence/maintenance et vulnérabilités connues | Capacité promise sans mesure nécessaire ou dépendance incompatible |
| Tests/observabilité | Critères/tests liés, résultats sur SHA, logs minimisés, échecs partiels et alertes utiles | Preuve absente pour un risque critique ou régression inexpliquée |
| Feature flags | Défaut, état désactivé, scope, activation progressive pertinente, audit et retrait | Flag qui contourne un droit ou arrêt qui ne traite pas les jobs/données en vol |
| Documentation/release | Guide et configuration alignés ; bugs connus ; migrations ; surveillance et rollback | Procédure non vérifiée présentée comme opérationnelle |

**Processus proposé :** soumission → identification base/head et du delta → contrôle des pièces → revue → statut motivé → corrections/preuves → relecture du delta → décision du mainteneur. Une révision nouvelle invalide seulement les conclusions qu'elle affecte, sauf changement de périmètre. Une fonction reportée et indépendante ne bloque pas les documents M0.

Statuts de revue : APPROVED ; APPROVED WITH MINOR CHANGES (aucune réserve critique, liste explicite) ; CHANGES REQUIRED ; BLOCKED ; NEEDS MASTER DECISION ; SECURITY REVIEW REQUIRED ; PRIVACY REVIEW REQUIRED. En cas de plusieurs causes, indiquer un statut principal et toutes les conditions restantes. APPROVED ne vaut pas décision de release ; READY/NOT READY/CONDITIONAL sont utilisés séparément sur version/artefact identifiés.

Pour tout breaking change : ancien/nouveau comportement, consommateurs et versions affectés, transition, feature flag si utile, migration, rollback, risques, décision HQ nécessaire. Pour toute migration : volume représentatif, locks/durée, compatibilité application ancienne/nouvelle, sauvegarde/restauration, reprise après échec et stratégie de déploiement. Aucun outil de contract testing ni framework n'est adopté par cette grille.

## Fiche de décision importante à soumettre

**Référence existante : OPEN-008 / DIR-010 ; DEC à attribuer par HQ si nécessaire. Statut : PROPOSÉ.**

| Champ | Proposition |
| --- | --- |
| Objectif / problème | Rendre vérifiable et effective la revue avant merge alors que main est déclarée non protégée |
| Solution recommandée | 14/HQ vérifient les capacités du dépôt privé et proposent une protection imposant revue indépendante et checks adaptés ; désigner les comptes autorisés |
| Alternatives | Contrôle manuel temporaire avec responsable nommé, vérification explicite des SHA/checks et date de réexamen ; différer la fusion. Aucun rejet définitif décidé ici |
| Option non recommandée | Rendre public le dépôt uniquement pour débloquer les protections : changement d'exposition sans justification produit |
| Dépendances | OPEN-008, identité des reviewers, droits administratifs, restrictions d'offre, avis 14 et budget HQ si nécessaire |
| Impact business | Éventuel coût de l'offre et disponibilité d'un reviewer ; réduction des erreurs d'intégration |
| Impact technique | Réglages GitHub, checks requis et politique de contournement à définir ; pas de stack runtime changée |
| Risques | Contrôle manuel contournable ; fausse confiance dans une CI qui a ses propres limites |
| Priorité / phase | P0 pour gouvernance de fusion M0/MVP |
| Autorité / réexamen | HQ avec 14/20/21 ; avant prochain merge et à tout changement de droits ou d'offre |

## Conflits, dépendances et transmissions

### INTEGRATION CONFLICT — portée de la stack et du noyau

**Références :** v0.1 de 21, OPEN-002/003/005/007, catalogue et vision au SHA #2. **Sujet :** une stack annoncée ou une liste de fonctions candidate peut être interprétée comme contrat acquis. **État :** clarification dans ce livrable ; aucune contradiction entre contrats approuvés démontrée. **Recommandation :** conserver les phases HQ proposées et attendre les décisions produit/Architecture pertinentes avant code. **Impact bloquant :** seulement les lots dépendants. **Décision HQ nécessaire :** périmètre, clients, communautés, permissions et stack ; pas une décision de 21.

### Règle de résolution proposée

Documenter les deux positions avec chemins/SHA, comportement attendu, consommateurs affectés, options, recommandation, autorité et test de résolution. Ne pas renommer un champ, écarter une position ou fermer un conflit sans preuve. La réponse du propriétaire et la décision HQ sont distinctes. Après arbitrage, mettre à jour contrats, clients, docs et tests dans des PR liées ; 21 contrôle le delta.

| Référence de suivi | Émetteur → destinataire | Question/action et pièce attendue | Blocage / état réel |
| --- | --- | --- | --- |
| INT-0007, FIND-21-01 | 21 → 20/14/18 | Corriger uniquement le check whitespace et fournir non-régression + run du SHA corrigé | Validation du contrôle/fusion #1 ; À TRANSMETTRE |
| OPEN-008, FIND-21-02 | 21 → HQ/14/20 | Vérification administrative et décision documentée sur revue/protection sans changer la visibilité du dépôt | Gouvernance avant merge ; À TRANSMETTRE |
| INT-0010, FIND-21-03 | 21 → 17/20 | Actualiser seulement la ligne CI du rapport historique, avec les deux SHA et le run | Traçabilité ; À TRANSMETTRE |
| INT-0003, OPEN-005 | 21 → 03/04 | Contrats et frontières prioritaires, distinction décision/conception/runtime | Implémentation du lot concerné ; À TRANSMETTRE |
| INT-0001, OPEN-002/003 | 21 → 01/HQ/05/06/19 | Décisions clients/communautés et exclusions ; aucune fonction ajoutée par la revue | Contrats des variantes ; À TRANSMETTRE |
| INT-0004/0005, OPEN-007 | 21 → 09/10/14/15/08 | Matrice de droits et propagation retrait/blocage/recours/export ; délais et exceptions explicités | Lots sensibles et pilote ; À TRANSMETTRE |
| INT-0008 | 21 → 18 | Relier les 12 critères locaux aux AC-J et tests canoniques ; compléter environnement et preuves | Tests applicatifs futurs ; À TRANSMETTRE |
| INT-0009 | 21 → 16/02/05 | Matrice langues/surfaces et accessibilité des parcours critiques | Validation du pilote ; À TRANSMETTRE |

Le mandat de travail a bien été reçu par cette discussion via le message du porteur du projet. La publication GitHub de sa réponse ne prouve ni lecture ni réception par les autres discussions. Le tableau de coordination HQ reste à mettre à jour par son propriétaire sur preuve ; aucune autre équipe n'est marquée REÇU ici.

## Risques et limites

- **FIND-21-01 :** faux vert du contrôle whitespace ; mesure = correctif ciblé et cas de non-régression. Défaut reproduit, sans panne de l'application.
- **FIND-21-02 :** fusion sans garde-fou technique ; mesure = décision de gouvernance et preuve des réglages/contrôles retenus.
- **RISK-0004 existant :** contrats divergents ; mesure = grille producteur/consommateurs et tests de contrat, sans création d'API unilatérale.
- **RISK-0001 existant :** propositions transformées en engagement MVP ; mesure = phase/statut et décision explicites par FEAT.
- **RISK-0002 existant :** modération ou recours inopérants ; mesure = états, droits, capacité humaine et preuve de bout en bout avant ouverture.
- Privacy/visibilité : retrait sans propagation aux médias, caches ou notifications ; mesure proposée = AC-INT-21-02/06/09 et revue 14/15. Risque à intégrer au registre par HQ, pas incident constaté.
- Les contrôles locaux ne couvrent ni ancres Markdown, ni liens externes, ni tous les secrets, ni sémantique métier complète. Les prix et garanties de fournisseurs n'ont pas été revérifiés.
- Les preuves décrivent les SHA indiqués. Toute évolution parallèle du dépôt demande un examen du delta avant intégration, sans généraliser ce verdict.

## Compte rendu et MASTER HANDOFF — INTEGRATION

1. **Décisions prises / à valider :** revue locale motivée CHANGES REQUIRED pour #1, BLOCKED pour intégration de #2 ; aucune décision produit/stack/permission. HQ/14 doivent arbitrer OPEN-008 et le contrôle avant merge. Les autres OPEN restent aux propriétaires.
2. **Livrable :** ce fichier à son chemin canonique `documentation/quality/integration-review.md`, SN-INT-M0-001 v0.2 ; reprend v0.1 avec preuves GitHub et matrice FEAT. La PR qui le publie porte son SHA et ses checks ; sa fusion ne vaut pas approbation spécialisée de toutes les propositions.
3. **Tests :** 32/42 fichiers hash-vérifiés ; validateur PASS sur les deux exports ; 10 tests PASS sur chacun ; 34 FEAT/21 mandats/7 parcours/31 AC contrôlés ; défaut whitespace et limite lien non suivi reproduits. CI source consultée avec SHA de merge effectifs. Aucun test applicatif exécuté.
4. **Questions ouvertes :** protection/reviewers (HQ/14/20), correction du gate (20/14/18), clients/communautés (01/HQ), contrats (03/04), accès/données/modération (09/10/14/15), langues (16).
5. **Dépendances :** tableau ci-dessus, à transmettre. Aucun acquittement d'une autre discussion inventé.
6. **Risques :** cinq constats locaux, dont contrôle CI incomplet et protection absente dans la réponse de branche ; preuves limitées au documentaire ; aucune readiness du pilote.
7. **Suite/HQ :** publier et faire examiner cette contribution ; transmettre les corrections ciblées à 20/14/17 ; obtenir arbitrage OPEN-008 ; corriger puis revoir #1 ; traiter la base et les checks de #2 ; consolider ensuite les contrats des lots retenus et les cas QA. Éviter une réanalyse générale des documents déjà lus sans delta justifié.

**Security review :** requise pour la décision de protection et les futurs contrôles d'accès, sans prétendre à une approbation 14. **Privacy review :** requise pour les traitements produit futurs ; ce rapport ne les met pas en œuvre. **QA :** demandé pour non-régression du gate et critères futurs. **Documentation :** delta ciblé FIND-21-03 et intégration des décisions seulement après arbitrage.
