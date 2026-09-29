# Parcours utilisateurs et critères d'acceptation proposés

Date : 29 septembre 2026. Version : 0.1. Statut : **PROPOSITION HQ — REVUE PRODUIT, DESIGN, SÉCURITÉ, PRIVACY ET QA ATTENDUE**.

Les parcours décrivent le comportement attendu, sans imposer de stack, de mécanisme d'authentification, de modèle de permission ou de délai réglementaire. Références : [vision produit](product-vision.md), [catalogue fonctionnel](feature-catalog.md).

Tous les critères `AC-Jxx-xx` ci-dessous ont le statut **PLANNED**. Ils ne sont ni des tests exécutés ni une preuve de fonctionnement. QA attribuera ses identifiants de test et précisera données, environnement, commandes, preuve et résultat. Les décisions manquantes sont des préconditions à lever avant exécution concluante.

## J01 — Créer un compte et reprendre l'accès

**Capacités :** FEAT-001, FEAT-002, FEAT-003, FEAT-004, FEAT-021. **Propriétaires :** 01/04 ; revues 02/14/15/18.

**But :** disposer d'un compte et comprendre les premiers réglages. **Préconditions :** politique d'admissibilité, méthode d'activation et de récupération, informations présentées et défauts de visibilité approuvés.

**Parcours nominal :** la personne choisit sa langue parmi celles disponibles ; prend connaissance des informations utiles ; soumet les données prévues au contrat ; accomplit l'activation retenue ; complète les champs facultatifs de profil ; voit un résumé de visibilité ; accède à l'accueil. Une connexion ultérieure crée une session ; la déconnexion la ferme. En cas de perte d'accès, une procédure dédiée remplace la réutilisation de secrets anciens.

**Erreurs et reprise :** entrée invalide, activation expirée ou consommée, envoi impossible, interruption réseau, tentative trop fréquente. Les messages restent compréhensibles et ne révèlent pas inutilement l'existence d'un compte. La reprise ne crée pas deux comptes ni deux validations.

**Permissions :** une personne non authentifiée ne reçoit aucune donnée privée de compte. L'état d'activation et l'admissibilité sont contrôlés côté service, pas uniquement dans l'interface. La récupération ne donne aucun droit avant sa vérification.

| Critère | Vérification à préparer | Statut |
| --- | --- | --- |
| AC-J01-01 | Données valides et activation recevable conduisent à un seul compte dans l'état attendu | PLANNED |
| AC-J01-02 | Activation expirée ou déjà consommée est refusée avec une reprise autorisée | PLANNED |
| AC-J01-03 | Une session révoquée échoue sur une route protégée, y compris après actualisation | PLANNED |
| AC-J01-04 | Récupération et erreurs ne permettent pas d'obtenir les informations privées d'un autre compte | PLANNED |

## J02 — Publier un texte et une image pour une audience choisie

**Capacités :** FEAT-004, FEAT-006, FEAT-007. **Propriétaires :** 01/08/04 ; revues 02/14/15/18.

**But :** partager en comprenant qui peut accéder au résultat. **Préconditions :** audiences possibles, défaut de visibilité, limites de texte/fichier, règles de traitement et modification approuvés.

**Parcours nominal :** l'auteur saisit le texte ; ajoute éventuellement une image et sa description ; consulte l'audience ; soumet ; voit l'état de traitement puis le résultat. L'interface n'annonce pas une publication visible avant confirmation du service. L'auteur peut ensuite modifier ou retirer sa publication suivant le contrat approuvé.

**Erreurs et reprise :** fichier incorrect ou dépassant les limites, échec du traitement, réseau interrompu, session expirée ou action interdite. Le statut doit distinguer brouillon, en cours, publié et échec selon le modèle retenu. Les reprises ne doivent pas créer de doublon accidentel. La persistance de brouillons sur l'appareil reste à spécifier avec Privacy.

**Permissions :** l'autorisation porte sur le texte, les fichiers, leurs variantes et leur accès direct. Un non-auteur ne modifie pas la publication. Le traitement d'un changement d'audience ou d'un retrait inclut caches, médias et liens selon un contrat cohérent ; aucun délai n'est inventé ici.

| Critère | Vérification à préparer | Statut |
| --- | --- | --- |
| AC-J02-01 | Publication valide consultable par le public autorisé et absente pour le public exclu | PLANNED |
| AC-J02-02 | Fichier interdit ou échec de traitement n'est pas affiché comme une publication réussie | PLANNED |
| AC-J02-03 | Répétition de la même soumission réseau ne crée pas deux publications selon le contrat de reprise | PLANNED |
| AC-J02-04 | Un non-auteur ne modifie pas l'objet ; un lecteur interdit n'obtient pas le fichier par URL directe | PLANNED |
| AC-J02-05 | Retrait ou restriction d'audience rend les accès texte et médias conformes à la nouvelle règle | PLANNED |

## J03 — Suivre, lire le fil et interagir sans perdre le contrôle

**Capacités :** FEAT-005, FEAT-008 à FEAT-012, FEAT-022. **Propriétaires :** 01/02/05 ; revues 04/09/18.

**But :** retrouver les publications choisies et gérer son attention. **Préconditions :** règle d'abonnement, ordre chronologique et départage, pagination, catégories de notification et effet du blocage approuvés.

**Parcours nominal :** la personne ouvre un profil accessible et s'abonne ; revient au fil ; lit les publications dans l'ordre affiché ; charge la suite ; réagit ou commente ; retire sa réaction si souhaité ; ajuste ses notifications ; peut se désabonner. Le fil vide explique ce qui manque et propose une action pertinente sans suggérer de faux contenu.

**Erreurs et reprise :** contenu supprimé entre lecture et commentaire, permission modifiée, chargement partiel, réseau perdu. Une nouvelle tentative d'interaction ne doit pas multiplier la même action. La position de lecture et l'indication de rattrapage sont définies par Design avant implémentation.

**Permissions :** une publication devenue inaccessible disparaît des réponses de fil, du détail et des aperçus sensibles. Les compteurs ne doivent pas révéler plus que la politique approuvée. Les commentaires et réactions appliquent les mêmes interdictions d'interaction.

| Critère | Vérification à préparer | Statut |
| --- | --- | --- |
| AC-J03-01 | Le fil respecte l'ordre défini et sa pagination n'introduit pas de doublon sous les scénarios concurrents prévus | PLANNED |
| AC-J03-02 | Retrait de visibilité avant commentaire produit un refus contrôlé sans écriture non autorisée | PLANNED |
| AC-J03-03 | Désabonnement, retrait de réaction et préférences restent cohérents après rechargement | PLANNED |
| AC-J03-04 | Le parcours essentiel est utilisable au clavier et sur les tailles d'écran approuvées | PLANNED |
| AC-J03-05 | Une notification ne révèle pas un contenu interdit et respecte la préférence applicable | PLANNED |

## J04 — Bloquer et signaler une situation indésirable

**Capacités :** FEAT-012, FEAT-013. **Propriétaires :** 09/10 ; revues 01/04/14/15/18.

**But :** interrompre les interactions prévues par la politique et transmettre un incident. **Préconditions :** effet exact du blocage, catégories, données de preuve admises et règles contre l'abus de signalement approuvés.

**Parcours nominal :** la personne ouvre les options d'un compte ou contenu ; choisit de bloquer, de signaler, ou les deux ; reçoit l'explication de chaque action ; fournit le minimum requis ; obtient confirmation et référence de signalement. Le blocage ne signifie pas automatiquement sanction de l'autre compte.

**Erreurs et reprise :** cible supprimée, signalement déjà transmis, pièce jointe refusée, réseau absent. L'interface ne prétend pas que le signalement est reçu avant accusé de réception. Les règles de conservation de preuve pour un objet supprimé restent à examiner avec Privacy.

**Permissions :** identité et commentaires privés du signalant ne sont pas exposés à la cible. Les règles du blocage doivent être testées sur tous les accès concernés ; son étendue doit être expliquée sans promettre un anonymat ou une invisibilité absolus.

| Critère | Vérification à préparer | Statut |
| --- | --- | --- |
| AC-J04-01 | Après blocage confirmé, chaque interaction interdite par la matrice est refusée par le service | PLANNED |
| AC-J04-02 | Un signalement reçu possède une référence ; une erreur de transport n'est pas présentée comme un succès | PLANNED |
| AC-J04-03 | La cible n'obtient ni identité du signalant ni note privée en consultant les routes accessibles | PLANNED |
| AC-J04-04 | Cible supprimée ou envoi répété produit le comportement documenté sans dossier incohérent | PLANNED |

## J05 — Modérer et traiter un recours

**Capacités :** FEAT-014, FEAT-015, FEAT-017. **Propriétaires :** 09/10 ; revues 04/14/15/18.

**But :** résoudre un dossier avec une décision justifiée et contestable selon les règles retenues. **Préconditions :** rôles, motifs, pouvoirs, règle de réexamen, modèle de notification et données consultables approuvés.

**Parcours nominal :** un agent habilité ouvre un dossier ; consulte les seules informations nécessaires ; choisit une action prévue ; consigne le motif ; confirme ; le service applique et journalise le résultat. La personne concernée reçoit l'information autorisée et peut déposer un recours. Le recours est rattaché à la décision et examiné selon la règle d'indépendance à décider. Son résultat confirme, modifie ou annule la décision avec traçabilité.

**Erreurs et reprise :** habilitation retirée pendant la session, dossier traité simultanément, action partiellement échouée, notification non délivrée. Aucun succès ne doit masquer une sanction non appliquée. La reprise suit un contrat défini et évite une double sanction.

**Permissions :** lecture du dossier, action, accès aux preuves et réexamen sont des permissions distinctes à spécifier. Les rôles communautaires éventuels n'obtiennent pas automatiquement des pouvoirs globaux. La journalisation ne contient pas de secrets.

| Critère | Vérification à préparer | Statut |
| --- | --- | --- |
| AC-J05-01 | Agent sans habilitation refusé sur lecture et action, y compris après retrait de rôle | PLANNED |
| AC-J05-02 | Deux traitements concurrents produisent l'état cohérent défini et des traces attribuables | PLANNED |
| AC-J05-03 | Décision, motif, action effective et notification restent distinguables en cas d'échec partiel | PLANNED |
| AC-J05-04 | Recours rattaché à sa décision, consultable par son demandeur et traité par un rôle autorisé | PLANNED |
| AC-J05-05 | Annulation d'une décision restaure uniquement ce que le contrat prévoit et conserve la trace de correction | PLANNED |

## J06 — Consulter ses paramètres, demander un export et supprimer son compte

**Capacités :** FEAT-004, FEAT-016. **Propriétaires :** 15/04 ; revues 02/10/14/18.

**But :** comprendre ses données et agir sur son compte. **Préconditions :** inventaire de données, méthode de vérification de la demande, délais, rétention, exceptions, cycle de suppression et traitement des sauvegardes documentés et examinés.

**Parcours nominal :** la personne ouvre les paramètres ; consulte visibilité et informations ; demande un export ; reçoit un état puis un moyen sécurisé d'accès au résultat. Pour la suppression, elle voit les conséquences et limites réellement applicables ; confirme selon la procédure retenue ; reçoit un état de suivi. Les effets sur sessions, profil, publications, médias et traitements différés suivent le contrat approuvé.

**Erreurs et reprise :** vérification échouée, export expiré, traitement interrompu, compte déjà en cours de suppression. L'interface expose un état exact ; elle ne promet pas l'effacement instantané de tous les systèmes. Les données concernant des tiers sont examinées avant définition du contenu de l'export.

**Permissions :** aucune demande ou pièce d'export accessible à un autre membre ; l'assistance n'obtient que ses pouvoirs documentés. Les accès sensibles et les reprises font l'objet de vérifications et d'une traçabilité adaptée.

| Critère | Vérification à préparer | Statut |
| --- | --- | --- |
| AC-J06-01 | Le demandeur accède uniquement à son export ; lien expiré ou identité différente refusés | PLANNED |
| AC-J06-02 | Erreur de traitement laisse un état compréhensible et permet la reprise documentée | PLANNED |
| AC-J06-03 | Suppression applique les effets attendus à chaque catégorie de données selon délais et exceptions approuvés | PLANNED |
| AC-J06-04 | La vérification de suppression comprend médias, jobs et risque de réintroduction lors d'une restauration | PLANNED |

## J07 — Rejoindre et utiliser une communauté, si retenue au MVP

**Capacités :** FEAT-020, FEAT-004, FEAT-013 à FEAT-017. **Propriétaires :** 01/19 ; revues 09/04/02/15/18.

**Statut du parcours :** PROPOSÉ, CONDITIONNÉ À L'ARBITRAGE COMMUNAUTÉS. **But :** échanger dans un espace dont les règles et les responsables sont identifiables.

**Préconditions :** inclusion dans le périmètre, types de communautés, adhésion, rôles, pouvoirs, visibilité et articulation avec modération globale approuvés.

**Parcours nominal :** une personne consulte la présentation accessible ; prend connaissance des règles ; demande à rejoindre ou rejoint selon le type retenu ; voit son état d'adhésion ; publie si son rôle le permet ; signale un incident ; peut quitter l'espace. Un responsable gère l'adhésion et les règles uniquement dans la limite de ses pouvoirs.

**Erreurs et reprise :** demande en attente, refus, exclusion, perte du dernier responsable, communauté fermée ou contenu devenu inaccessible. Le traitement de ces états ne doit pas être inventé par l'implémentation.

**Permissions :** un rôle local ne permet aucune action hors de sa communauté. Les informations accessibles aux non-membres et l'effet d'un départ sur les publications sont à décider. Les politiques globales restent applicables selon la hiérarchie à documenter.

| Critère | Vérification à préparer | Statut |
| --- | --- | --- |
| AC-J07-01 | Non-membre et membre voient uniquement ce que leur statut autorise, y compris par API et média direct | PLANNED |
| AC-J07-02 | Responsable local ne peut consulter ni gérer les dossiers réservés au niveau global | PLANNED |
| AC-J07-03 | Retrait de rôle, départ ou exclusion modifie effectivement les actions autorisées | PLANNED |
| AC-J07-04 | Perte du dernier responsable et fermeture suivent une procédure définie et observable | PLANNED |

## Couverture et suites attendues

Les 31 critères couvrent des parcours du candidat pilote ; ils ne constituent pas une stratégie exhaustive. Restent à détailler : concurrence avancée, limites/rate limiting, charge, accessibilité complète, localisation, opérations de support, panne et restauration, installation, mises à jour et sécurité spécialisée. Les parcours vidéo, mobile natif, publicité et rémunération seront documentés avant les phases concernées.

## Compte rendu de préparation

1. Décisions : sept parcours proposés ; communautés conditionnelles, aucune permission approuvée ici.
2. Livrables : ce document, catalogue FEAT et cadre de vision.
3. Tests : 31 critères PLANNED ; aucun test applicatif exécuté dans ce travail.
4. Questions : contrats de visibilité, récupération, suppression, recours et communautés à trancher.
5. Dépendances : 01 et 02 formalisent l'expérience ; 04 les contrats ; 09/14/15 les règles ; 18 les cas et preuves.
6. Risques : critères partiellement exécutables avant décisions manquantes, échecs partiels et fuites par accès secondaires.
7. Suite / HQ : demander les revues et compléter les préconditions avant d'autoriser les issues d'implémentation.
