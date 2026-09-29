# Catalogue fonctionnel proposé

Date : 29 septembre 2026. Version : 0.1. Statut global : **PROPOSÉ — NON APPROUVÉ POUR IMPLÉMENTATION**.

Propriétaire : 01 Produit, coordination MASTER. Les 34 identifiants sont stables ; un retrait conserve son identifiant et sa justification. Les phases sont des propositions de classement, pas un engagement de date. P0 = candidat nécessaire au lancement ; P1 = important ; P2 = évolution ; P3 = exploration. P0 ne prouve pas que la fonctionnalité est approuvée.

Les propriétaires ci-dessous sont les discussions attendues, pas des personnes GitHub désignées. « Dépendances » nomme à la fois les capacités produit et les avis indispensables. Aucun test indiqué n'a encore été exécuté pour l'application.

## Capacités candidates au pilote

| ID | Fonctionnalité et limite proposée | Classe | Priorité | Propriétaire | Dépendances | Exemple d'acceptation vérifiable |
| --- | --- | --- | --- | --- | --- | --- |
| FEAT-001 | Inscription et activation, méthode à décider | MVP | P0 | 04 Backend | 01, 14, 15 ; politiques d'âge et d'accès | Une activation expirée est refusée ; un compte non admissible n'accède pas à une action réservée |
| FEAT-002 | Connexion, sessions, déconnexion et récupération | MVP | P0 | 04 Backend | FEAT-001 ; 14 | Une session révoquée ne permet plus une action protégée ; récupération sans divulgation inutile de compte |
| FEAT-003 | Profil, nom d'affichage, avatar et description | MVP | P0 | 01 Produit | FEAT-001, FEAT-007, FEAT-021 ; 02, 15 | Un tiers ne peut modifier le profil ; les champs privés sont absents de sa réponse API |
| FEAT-004 | Confidentialité et contrôle de visibilité | MVP | P0 | 15 Privacy | 01, 04, 09, 14 ; matrice de permissions à décider | Un lecteur non autorisé ne reçoit ni contenu ni média par accès direct |
| FEAT-005 | Suivre et ne plus suivre une personne | MVP | P0 | 01 Produit | FEAT-003, FEAT-004, FEAT-012 ; 04 | Répéter une demande n'ajoute pas de doublon ; un blocage applique la règle approuvée |
| FEAT-006 | Publier, modifier et retirer du texte | MVP | P0 | 01 Produit | FEAT-004, FEAT-014 ; 04, 05 | Un non-auteur ne peut modifier le texte ; la modification respecte validation et audience |
| FEAT-007 | Ajouter une image, texte alternatif et contrôler son traitement | MVP | P0 | 08 Média | FEAT-004, FEAT-006 ; 14, 15 | Fichier invalide ou trop volumineux refusé selon limites approuvées ; média privé non servi à un tiers |
| FEAT-008 | Fil chronologique avec pagination et états vides | MVP | P0 | 01 Produit | FEAT-004 à FEAT-007, FEAT-012, FEAT-014 ; 04, 05 | Ordre stable documenté, aucun doublon sur pagination et aucun contenu devenu interdit après blocage |
| FEAT-009 | Réagir et retirer sa réaction | MVP | P1 | 01 Produit | FEAT-004, FEAT-006, FEAT-012 ; 04 | Nouvelle tentative réseau ne double pas la réaction ; aucune interaction sur un contenu inaccessible |
| FEAT-010 | Commenter et gérer ses commentaires | MVP | P1 | 01 Produit | FEAT-004, FEAT-006, FEAT-012, FEAT-014 ; 09 | Le refus de permission s'applique aussi par API ; un retrait garde le fil dans un état compréhensible |
| FEAT-011 | Notifications essentielles et préférences | MVP | P1 | 01 Produit | FEAT-004, FEAT-012 ; 02, 04, 15 | Désactiver une catégorie arrête sa diffusion selon le contrat ; aperçu sans contenu non autorisé |
| FEAT-012 | Blocage et arrêt des interactions visées | MVP | P0 | 09 Trust & Safety | FEAT-004 ; 01, 04, 14 | Le compte bloqué ne contourne pas les restrictions approuvées via URL, API ou notification |
| FEAT-013 | Signaler un contenu ou un compte | MVP | P0 | 09 Trust & Safety | FEAT-006, FEAT-017 ; 10, 15 | Accusé de réception, catégorie et référence de dossier ; identité du signalant non exposée à la cible |
| FEAT-014 | Examiner, restreindre et notifier une décision de modération | MVP | P0 | 09 Trust & Safety | FEAT-013, FEAT-017 ; 10, 14, 15 | Seul un rôle habilité agit ; motif, acteur et résultat sont traçables avec accès limité |
| FEAT-015 | Contester une décision et recevoir un résultat | MVP | P0 | 09 Trust & Safety | FEAT-014, FEAT-017 ; 10, 15 | Un recours reste rattaché à sa décision et conserve un état consultable ; règle de réexamen définie |
| FEAT-016 | Demandes d'accès/export et suppression de compte | MVP | P0 | 15 Privacy | FEAT-001, FEAT-002 ; 04, 14, 10 | Un tiers ne peut initier ou télécharger l'export ; la suppression suit les états, délais et exceptions approuvés |
| FEAT-017 | Console minimale de modération et support | MVP | P0 | 10 Admin | FEAT-013 à FEAT-016 ; 09, 14 | Rôle sans habilitation refusé ; accès sensibles et décisions auditables sans exposer de secrets |
| FEAT-018 | Web responsive et accessibilité des parcours prioritaires | MVP | P0 | 05 Web | 01, 02, 18 ; choix de surface à arbitrer | Inscription, publication et signalement utilisables au clavier et sur les tailles d'écran retenues |
| FEAT-019 | Mesures minimales d'usage et de santé du pilote | MVP | P1 | 13 Data | 01, 14, 15 ; protocole de mesure | Un événement documenté n'inclut pas texte privé ni secret ; définitions de cohorte reproductibles |
| FEAT-020 | Communautés, membres, rôles et règles — INCLUSION À ARBITRER | MVP | P1 | 01 Produit | FEAT-004, FEAT-013 à FEAT-017 ; 09, 19, 04 | Un non-membre n'accède pas à une communauté restreinte ; un responsable ne dépasse pas ses pouvoirs |
| FEAT-021 | Langues du pilote et contenus multilingues | MVP | P0 | 16 International | 01, 02, 09 ; langues à décider | Chaque parcours pilote dispose de ses libellés, erreurs et contenus de support dans les langues retenues |
| FEAT-022 | Respect du temps : commandes de lecture et préférences | MVP | P1 | 02 Design | FEAT-008, FEAT-011 ; 01 | L'utilisateur retrouve la commande des notifications et comprend l'état de fin/rattrapage du fil |

FEAT-020 reste dans la classe candidate MVP pour rendre visible l'arbitrage, mais ne peut être inclus dans un engagement de livraison avant décision. FEAT-018 ne tranche pas le débat web/mobile. Les limites d'upload, catégories de notification, délais d'effacement et règles de visibilité restent des contrats à examiner.

## Évolutions proposées

| ID | Fonctionnalité et limite proposée | Classe | Priorité | Propriétaire | Dépendances | Exemple d'acceptation vérifiable |
| --- | --- | --- | --- | --- | --- | --- |
| FEAT-023 | Recherche de comptes, contenus et communautés accessibles | Phase 2 | P1 | 01 Produit | FEAT-004, FEAT-012, FEAT-014 ; 04, 15 | Un résultat retiré ou inaccessible ne réapparaît pas par recherche ni extrait |
| FEAT-024 | Messagerie privée avec contrôles anti-abus | Phase 2 | P2 | 01 Produit | FEAT-002, FEAT-004, FEAT-012, FEAT-013 ; 09, 14, 15 | Un expéditeur bloqué est refusé ; modèles de sécurité et de signalement explicités avant lancement |
| FEAT-025 | Applications mobiles natives et notifications associées | Phase 2 | P2 | 06 Mobile | Contrats 04, FEAT-004, FEAT-011 ; 02, 14, 18 | Révocation de session et confidentialité respectées sur appareil et notifications |
| FEAT-026 | Vidéo enregistrée, formats courts et outils de création | Phase 2 | P2 | 08 Média | FEAT-004, FEAT-013, FEAT-014 ; 14, 09, budget médias | Upload repris ou erreur récupérable, accès contrôlé, traitement et coût mesurés |
| FEAT-027 | Outils créateurs : publication et statistiques compréhensibles | Phase 2 | P2 | 12 Créateurs | FEAT-006, FEAT-019 ; 13, 15 | Un créateur n'accède qu'à ses mesures autorisées ; chaque indicateur a une définition |
| FEAT-028 | Présence professionnelle et gestion à plusieurs | Phase 2 | P2 | 01 Produit | FEAT-003, FEAT-004, FEAT-017 ; 11, 12, 14 | Retirer un gestionnaire révoque ses pouvoirs ; actions attribuées à un acteur |
| FEAT-029 | Recommandations facultatives et explication des suggestions | Phase 3 | P2 | 07 IA | FEAT-004, FEAT-008, FEAT-019 ; 13, 15, 09 | Désactiver la personnalisation conserve un fil utilisable ; filtres d'accès appliqués à chaque suggestion |
| FEAT-030 | Publicité transparente et gestion des campagnes | Phase 3 | P2 | 11 Publicité | Modèle économique, FEAT-019 ; 15, 09, 13 | Une publicité est identifiée, sa provenance consultable et ses règles de diffusion vérifiables |
| FEAT-031 | Rémunération, abonnements et paiements aux créateurs | Phase 3 | P2 | 12 Créateurs | Modèle économique ; 11, 15, 14, 04 | Montant, frais, statut et contestation sont explicites ; double événement de paiement ne crée pas de double versement |
| FEAT-032 | Nouvelles régions, langues, écritures et opérations locales | International | P1 | 16 International | FEAT-021 ; 15, 09, 14, 19 | Chaque ouverture dispose d'une revue linguistique, support et modération, avec scénarios de lecture adaptés |
| FEAT-033 | Direct vidéo et interactions en temps réel à grande audience | Long terme | P3 | 08 Média | FEAT-026 ; 09, 14, 12, budget et tests de charge | Procédure d'arrêt, gestion d'incident, capacité et latence démontrées avant ouverture |
| FEAT-034 | Écosystème développeurs, intégrations et portabilité avancée | Long terme | P3 | 03 Architecture | FEAT-004, FEAT-016 ; 04, 14, 15 | Permissions explicites, révocation, quotas, contrat versionné et journal d'accès vérifiés |

## Règles de changement

1. Ajouter une idée avec identifiant, problème utilisateur, classe parmi MVP / Phase 2 / Phase 3 / International / Long terme, propriétaire, dépendances et exemple d'acceptation.
2. Toute modification de phase ou de permission produit une proposition au MASTER et aux équipes touchées.
3. Documenter les options, risques, impact business/technique et priorité dans le registre de décisions avant approbation.
4. Rattacher spécification, contrat, test, implémentation et revue à l'identifiant FEAT ; ne pas remplacer l'identifiant par un titre mouvant.
5. Marquer une fonctionnalité implémentée et vérifiée uniquement sur preuve ; la présence dans ce tableau ne vaut ni réalisation ni validation.

## Compte rendu de préparation

1. Décisions : classement proposé de 34 capacités, aucune nouvelle fonctionnalité approuvée.
2. Livrables : catalogue et liens vers [vision](product-vision.md) et [parcours](user-journeys.md).
3. Tests : exemples d'acceptation rédigés, tests applicatifs non exécutés.
4. Questions : communautés, surfaces, langues, âge, visibilité, économie et capacités opérationnelles.
5. Dépendances : propriétaires et consultations inscrits par ligne ; avis spécialisés non reçus dans ce document.
6. Risques : convertir involontairement une classification proposée en engagement de livraison ; propagation des permissions aux médias et notifications.
7. Suite / HQ : demander les revues ciblées, enregistrer les arbitrages et ouvrir les issues après fixation du périmètre.
