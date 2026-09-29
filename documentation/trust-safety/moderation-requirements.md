# Exigences de modération du pilote — M0

## Identification et statut

| Champ | Valeur |
| --- | --- |
| Objectif | Permettre de protéger un membre, instruire un signalement, appliquer une mesure motivée et corriger une erreur par recours |
| Propriétaire | 09 — Trust & Safety ; aucun reviewer GitHub humain désigné |
| Destinataires | 00, 01, 02, 03, 04, 07, 08, 10, 13, 14, 15, 16, 17, 18, 19, 21 |
| Date / version | 29 septembre 2026 / 0.1 — première contribution spécialisée dans le dépôt |
| Référence de rédaction | PR [#2](https://github.com/yyogas/social-network/pull/2), branche `documentation/m0-team-coordination`, commit `dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957` |
| Mandat | M0-TEAM-09 et INT-0004 ; DIR-010 et DIR-011 pour publication et revue |
| Statut | PROPOSÉ — avis spécialisé, ni permission approuvée, ni autorisation d'implémentation |
| Phases / priorité | MVP candidat P0 : FEAT-012 à FEAT-015, besoins FEAT-017 ; extensions selon la matrice ci-dessous |
| Périmètre | Comptes, profils, texte, images, commentaires ; communautés conditionnelles ; opérations humaines et recours |
| Dépendances bloquantes | INT-0901 à INT-0906, selon le lot : périmètre, permissions, preuves, contrats et capacité |

Entrées lues : [mandat](../teams/work-orders.md), [plan](../documentation-plan.md), [modèle](../teams/deliverable-template.md), [vision](../product/product-vision.md), [catalogue](../product/feature-catalog.md), [parcours J04/J05 et J07](../product/user-journeys.md), [gouvernance](../governance.md), [conventions](../repository-conventions.md), [registre HQ](../project-governance/decision-register.md), [état](../project-governance/project-status.md) et [stratégie QA](../quality/test-strategy.md). Les propositions HQ ont été examinées comme entrées, sans les promouvoir en décisions.

Les brouillons de cette discussion `SOCIAL_NETWORK_09_Trust_Safety_v0.1.md` et `SOCIAL_NETWORK_09_Trust_Safety_M0_v0.1.md` sont réutilisés et consolidés ici. Ce fichier contient les éléments nécessaires à sa compréhension autonome ; les brouillons ne sont pas des dépendances normatives du dépôt. La version 0.1 désigne cette première livraison GitHub, pas une validation des brouillons.

| Nature | Éléments et preuve |
| --- | --- |
| CONFIRMÉ | Mandat reçu : protéger les personnes, proposer signalement, quatre niveaux de sanction, recours et audit ; travail documentaire autorisé |
| PROPOSÉ | Tous les comportements, rôles, délais, classifications et critères métier ci-dessous ; ils demandent les revues indiquées |
| À VÉRIFIER | Volumes, langues modérables, capacité humaine, effets du blocage, politique d'âge, exigences par marché |
| NON REÇU | Contrats API approuvés, politique privacy validée, staffing, avis spécialisés externes, résultats applicatifs ou déploiement |

## Besoin, fonctionnalités et parcours

### Contribution indispensable et classement

Le pilote a besoin d'un traitement réel des abus : parcours utilisateur, opérateurs habilités, responsable d'urgence, capacité de retrait effective et réparation. Une console disponible ne prouve pas qu'une équipe traite les dossiers. Les identifiants FEAT du catalogue sont conservés ; la mise en sourdine est une extension proposée de FEAT-012 à faire confirmer par 01/17, pas une nouvelle fonctionnalité numérotée arbitrairement.

| ID / capacité | Phase proposée | Priorité | Acteurs / besoin | Préconditions et résultat attendu |
| --- | --- | --- | --- | --- |
| FEAT-012 — blocage | MVP | P0 | Membre souhaitant interrompre une interaction | Matrice d'effets approuvée ; refus côté service et état consultable |
| FEAT-012 — mise en sourdine | MVP, extension à arbitrer | P1 | Lecteur souhaitant filtrer son fil sans sanctionner autrui | Préférence personnelle ; masque publications et notifications sociales de la cible selon matrice |
| FEAT-013 — signalement | MVP | P0 | Déclarant, victime ou témoin | Catégories publiées, collecte minimale ; accusé durable et confidentialité du déclarant |
| FEAT-014 — triage, décision et anti-abus simple | MVP | P0 | Modérateur, responsable d'urgence | Personnel et règles habilités ; décision explicable et état d'application observable |
| FEAT-015 — recours | MVP | P0 | Personne affectée et examinateur | Décision identifiable ; accès au recours malgré suspension et correction contrôlée |
| FEAT-017 — console / support | MVP | P0 | Opérateur interne | Besoins métier donnés à 10 ; permissions et audit examinés par 14/15 |
| FEAT-020 — pouvoirs locaux | MVP conditionnel | P1 | Responsable communautaire | Inclusion décidée ; périmètre local, voie plateforme et dernier responsable traités |
| FEAT-024 / FEAT-026 — messages / vidéo | Phase 2 | P2 | Membres et modérateurs | Définir preuves, signalement, accès et contrôles avant lancement de ces surfaces |
| FEAT-029 / FEAT-030 / FEAT-031 — recommandation, ads, revenus | Phase 3 | P2 | Membres, annonceurs, créateurs | Retrait propagé aux classements ; fraude, contestation économique et droits dédiés |
| FEAT-032 — extension locale | International | P1 | Public de chaque nouveau marché | Expertise linguistique et politique locale, capacité et analyse 15 avant ouverture |
| FEAT-033 / FEAT-034 — live / intégrations | Long terme | P3 | Diffuseurs et développeurs | Arrêt d'urgence, révocation et évaluation de charge ; étude avant ouverture |

Les langues du pilote FEAT-021 nécessitent déjà une couverture adéquate. La classe International ne diffère pas ce besoin. La détection IA de violations est étudiée avec 07 ; aucune sanction permanente fondée exclusivement sur un score n'est proposée au pilote. Les règles anti-spam déterministes et réversibles appartiennent au socle candidat FEAT-014.

### FEAT-012 — blocage et sourdine

User story : en tant que membre, je veux interrompre les interactions d'un compte ou masquer ses contenus, afin de contrôler mon expérience sans devoir obtenir une sanction préalable.

Parcours : depuis profil/contenu, choisir l'action ; lire son effet ; confirmer ; attendre l'accusé du service ; voir et gérer la liste dans les paramètres. Bloquer et signaler sont indépendants : l'échec du signalement ne doit pas annuler un blocage confirmé. Débloquer ne rétablit pas automatiquement les abonnements et interactions supprimés par le blocage.

| Surface | Blocage proposé | Sourdine proposée |
| --- | --- | --- |
| Abonnements | Supprimer les liens dans les deux sens ; interdire tout nouvel abonnement entre les comptes | Conserver les liens |
| Réactions, commentaires et mentions nouvelles | Refuser l'interaction directe entre les comptes ; contrôle transactionnel avant écriture | Autoriser, mais ne pas notifier le membre ayant mis en sourdine |
| Fil, profil et accès direct authentifié | Ne pas retourner le contenu de l'autre compte ; effet sur compteurs/extraits à aligner avec FEAT-004 | Filtre dans le fil personnel ; accès direct volontaire conservé |
| Notifications | Annuler les notifications sociales en attente entre comptes ; masquer leurs aperçus | Ne pas émettre les notifications sociales de la cible au membre concerné |
| Commentaires historiques | Masquer les commentaires réciproques pour les deux membres sans les effacer pour les tiers autorisés | Masquer les éléments de la cible dans l'expérience personnelle selon le choix validé |
| Signalement, décision, recours | Restent accessibles par une voie dédiée autorisée ; aucune identité de déclarant dévoilée | Restent accessibles ; les messages de service ne sont pas des notifications sociales |
| Communauté partagée | N'accorde aucun pouvoir sur l'adhésion d'autrui ; exception opérateur local à faire arbitrer | Préférence personnelle ; aucune sanction de groupe |

Limite à expliquer : un blocage entre comptes ne garantit pas l'invisibilité hors connexion, dans des copies déjà reçues ou face à un autre compte. La politique de contenus publics relève de 01/15. L'accès aux preuves par un modérateur utilise un rôle séparé et une justification ; il ne passe pas par un contournement du blocage dans son expérience personnelle.

États : `INACTIVE → PENDING → ACTIVE → REVOKE_PENDING → INACTIVE` ; une erreur conserve le dernier état serveur connu et affiche « état à confirmer » si l'issue est inconnue. Deux appareils doivent converger sur la version serveur. Rejouer la même commande ne crée pas deux relations. Une cible supprimée produit un résultat neutre, sans recréer de compte ni divulguer son historique.

### FEAT-013 — signaler

User story : en tant que victime ou témoin, je veux signaler un compte ou un contenu avec une référence de suivi, afin qu'une personne habilitée puisse examiner le problème sans exposer mon identité à la cible.

Cibles du noyau : profil/avatar, publication texte/image et commentaire ; communauté si retenue. La catégorie est obligatoire, le récit complémentaire facultatif. Ne pas exiger une qualification juridique de l'utilisateur. Un chemin externe pour victime sans compte ou sans accès est proposé via Support, avec vérification minimale et limites de débit à valider par 10/14/15.

| Code candidat | Libellé utilisateur | Orientation initiale ; aucun automatisme de culpabilité |
| --- | --- | --- |
| THREAT_HARASSMENT | Menace ou harcèlement | Urgence si danger crédible imminent, sinon contexte/répétition |
| HATE_TARGETING | Haine ou attaque ciblée | Examen linguistique et contexte : citation, critique et reportage distincts |
| PRIVACY_IMPERSONATION | Vie privée ou usurpation | Réduire l'exposition si risque actif ; vérifier la revendication sans révéler de données privées |
| SPAM_FRAUD_BOTS | Spam, fraude ou compte trompeur | Examiner comportement et preuves ; pseudonyme ou automatisation légitime ne suffisent pas à sanctionner |
| CHILD_SAFETY | Sécurité d'un mineur | File spécialisée ; protéger sans demander le renvoi de contenus sexuels impliquant des mineurs |
| OTHER_POLICY | Autre problème | Routage humain ; ne pas classer automatiquement sans suite |

La taxonomie détaillée du contenu interdit, ses exemples et exceptions est à approuver avec 01/15 ; un code n'est pas une définition juridique. Une preuve d'usurpation éventuelle passe par un espace vérifié par 15, pas par une pièce d'identité exigée par défaut.

Parcours : sélectionner la cible et le motif, ajouter contexte minimal, envoyer, recevoir `report_id`, consulter son statut synthétique, recevoir le résultat permis. La preuve interne référence une révision du contenu au moment du signalement si sa collecte est autorisée ; aucune copie intégrale systématique de tout compte. Au MVP, préférer références aux contenus de la plateforme ; téléchargement de pièces externes limité au canal spécialisé après revue 14/15.

États UI : formulaire vide, saisie, envoi, reçu, erreur récupérable, cible indisponible. Un timeout ne vaut pas réception : consulter le résultat avec la même clé de soumission avant une nouvelle création. Si la cible a disparu, permettre un dossier avec référence indisponible et éléments déjà autorisés, sans contourner un droit de lecture perdu. Plusieurs déclarants peuvent être reliés à un cas, mais leurs récits et identités restent cloisonnés.

### FEAT-014 — instruire et appliquer une mesure

User story : en tant que modérateur habilité, je veux examiner le contexte et appliquer une action limitée à mes pouvoirs, afin de protéger les personnes avec une décision motivée et traçable.

Parcours : prendre un dossier, confirmer son périmètre d'accès, examiner les preuves nécessaires, sélectionner règle/version et motif, choisir portée/durée, obtenir le second contrôle si requis, enregistrer la décision, suivre l'application et notifier. Les outils montrent distinctement dossier, décision, exécution technique et notification.

| Objet | Transitions candidates | Invariant et reprise |
| --- | --- | --- |
| Dossier | `RECEIVED → TRIAGED → IN_REVIEW → DECIDED → CLOSED` ; `ESCALATED` / `NEEDS_INFO` reviennent en revue | Une affectation ne vaut pas décision ; fermeture seulement si exécution résolue et notification livrée ou échec explicitement traité |
| Décision | `DRAFT → RECORDED → SUPERSEDED` | Décision enregistrée non écrasée ; correction par nouvelle décision liée |
| Mesure | `PENDING → APPLYING → APPLIED` ou `PARTIAL_FAILED` / `FAILED` ; puis `REVOKE_PENDING → REVOKED` ou `EXPIRED` | Ne pas annoncer l'application complète sans confirmations des surfaces concernées ; reprise idempotente |
| Notification | `PENDING → SENT → DELIVERED` ou `RETRY_PENDING` / `UNDELIVERABLE` | Distinguer envoi et réception lorsque cette preuve existe ; pas de suppression de la décision pour panne de notification |

Un dossier peut être rouvert sur preuve nouvelle ; un recours constitue son propre objet lié. Deux agents travaillent avec une version attendue : une décision concurrente obsolète est refusée et le dossier rechargé. Retrait de rôle pendant la session : vérifier les pouvoirs lors de la lecture sensible et de la mutation, pas seulement à la connexion.

| Niveau | Effets candidats | Décideur / limites proposés |
| --- | --- | --- |
| Avertissement | Motif et pédagogie ; retrait du contenu séparé si nécessaire | Modérateur habilité ; ne réduit pas secrètement la portée |
| Limitation | Restreindre une capacité identifiée pour une durée définie | Modérateur habilité ; restriction ciblée et contestable, avec début/fin |
| Suspension | Interrompre temporairement les capacités sociales du compte | Responsable habilité ; validation humaine et accès conservé au recours |
| Bannissement | Fermer durablement les capacités sociales | Deux personnes habilitées distinctes ; recours selon politique ; traitement des données séparé |

Pas d'escalade mécanique « trois infractions = bannissement ». Examiner gravité, préjudice, répétition établie, contexte et fiabilité des preuves. Une urgence peut justifier une mesure conservatoire avant décision finale ; elle possède une échéance et un responsable de réexamen. Aucune mesure temporaire ne devient permanente par oubli. Avant son échéance, alerter le responsable ; toute prolongation est une nouvelle décision motivée. Le comportement technique à l'échéance, notamment pour les cas graves, doit être testé et approuvé avec 14/15.

Retrait d'un contenu, restriction d'âge et mesure sur compte sont distincts. Le retrait bloque aussi original et dérivés d'image, URLs, cache, aperçu et éventuels index ; 08/04 doivent définir les garanties et délais mesurables. Une copie déjà téléchargée ne peut pas être rappelée. Retirer un post ne signifie pas purger les preuves ni supprimer immédiatement toutes les sauvegardes.

### Triage, délais candidats et capacité humaine

Les priorités opérationnelles U0–U3 ci-dessous évitent la confusion avec P0–P3 du backlog. Les délais sont des **cibles internes proposées**, pas des délais légaux ni un SLA public. Ils commencent à la réception durable serveur, en temps écoulé ; l'affectation, la première revue humaine et la décision finale sont mesurées séparément. Les cas incomplets conservent leur âge et sont revus à échéance ; demander un complément ne remet pas le compteur à zéro.

| Urgence | Situation indicative | Propriétaire candidat | Cible de première prise en charge / escalade |
| --- | --- | --- | --- |
| U0 | Danger crédible imminent ou exploitation potentielle d'un mineur | Astreinte formée + responsable T&S | Accusé humain ≤15 min ; examen initial ≤1 h ; repli vers suppléant si non pris à 15 min |
| U1 | Harcèlement coordonné, divulgation ou fraude à préjudice actif | Modérateur prioritaire + responsable | Examen ≤4 h ; alerte au responsable à dépassement |
| U2 | Violation ordinaire sans risque imminent établi | File générale avec compétence linguistique | Examen ≤24 h ; rééquilibrage de charge si dépassement |
| U3 | Ambiguïté, contexte manquant ou faible urgence | File contextuelle / expert langue | Examen ≤72 h ; ne pas laisser expirer sans résultat |
| Recours | Contestation d'une décision | Examinateur distinct pour sanctions graves | Première revue ≤48 h, objectif de résultat ≤7 jours ; urgence reclassée U0/U1 |

Aucune couverture 24/7 n'est confirmée. U0 en temps écoulé exige une astreinte réellement financée ou une autre organisation validée ; une simple mention d'horaires ouvrés ne résout pas un incident hors horaires. Si ces objectifs sont impossibles, MASTER doit réduire le périmètre/exposition ou financer la couverture avant ouverture. Aucune procédure de contact des autorités n'est improvisée : 15/14 valident qui contacte qui, critères, minimum de données, canal et conservation de preuve.

Rôles à nommer avant pilote : responsable de service, agents de triage, modérateurs par langue, expert mineurs/urgence, examinateur de recours et suppléants. Plusieurs fonctions peuvent être portées par les mêmes personnes sauf contrôle indépendant d'une même décision ; conflits d'intérêts et accès à son propre dossier imposent récusation. Accès aux médias sensibles limité et outils de protection du personnel, formation et relais de soutien prévus.

Dimensionnement à calculer avec 10/19 : heures de charge = `(signalements/jour × minutes de triage + cas/jour × minutes d'enquête + appels/jour × minutes de recours + minutes de QA)/60`. Diviser par les heures productives disponibles par agent, puis prévoir absences, pics, langues et couverture horaire séparément. Mesurer les entrées, doublons, temps par catégorie et stock avant de promettre un effectif ; aucune valeur de charge n'est mesurée ici.

### Anti-spam, faux comptes, fraude et abus de signalement

Pour FEAT-013/014 : quotas proportionnés, détection de répétitions, limitation temporaire d'actions et regroupement de cas candidats. Les seuils et signaux sont à examiner avec 07/14/15. Volume de signalements, IP commune, langue, nom, origine ou pseudonymat ne constituent pas seuls une preuve d'abus. Prévoir réseaux partagés et comptes légitimes automatisés. Un signalement classé sans violation n'est pas un signalement malveillant par défaut.

Une campagne coordonnée de faux signalements peut faire l'objet d'un cas distinct et d'une mesure motivée. Le rate limiting doit préserver une voie urgente et une voie Support accessible, elles-mêmes protégées. À seuil de modèle inconnu ou modèle indisponible, conserver file humaine et mesures techniques existantes ; pas d'auto-approbation ni de sanction globale de repli. Avant tout retrait automatique futur : jeu d'évaluation par langue/catégorie, faux positifs/négatifs, revue d'échantillons et rollback de règle/version. Les décisions humaines restent auditables et peuvent être erronées.

Classement complémentaire de l'automatisation, rattaché à FEAT-014 et à examiner avec 07 :

| Capacité | Phase proposée | Limite avant activation |
| --- | --- | --- |
| Règles déterministes de débit, regroupement et alertes | MVP | Seuils, exceptions, expiration et recours à valider ; pas de verdict au seul volume |
| Assistance IA au triage, à la traduction et au résumé | Phase 2 | Évaluation par langue, contrôle humain du contenu original, confidentialité et coût ; aucun texte signalé traité comme une instruction du système |
| Détection coordonnée avancée et suggestions de mesures | Phase 3 | Analyse des signaux autorisés, erreurs mesurées, justification et arrêt de la règle/version |
| Calibration et expertise par nouveau marché | International | Ne remplace pas la couverture linguistique indispensable dès le pilote |
| Automatisation de décisions lourdes | Long terme, étude uniquement | Aucune autorisation implicite ; nécessité et acceptabilité à réexaminer avec HQ/14/15, possibilité de rejet |

### FEAT-015 — recours, décision indépendante et réparation

User story : en tant que personne affectée, je veux comprendre et contester une mesure même si mon compte est suspendu, afin qu'une erreur soit corrigée.

Parcours : ouvrir notification/centre de décision, vérifier l'identité par le canal autorisé, choisir la décision, fournir le contexte, recevoir un identifiant, consulter l'état, recevoir confirmation/modification/annulation. États : `SUBMITTED → ELIGIBILITY_REVIEW → IN_REVIEW → UPHELD | MODIFIED | OVERTURNED → NOTIFIED`. Refus d'éligibilité motivé et traçable ; fenêtre d'appel et cas particuliers à définir par 15/09/HQ, jamais par le frontend. Le délai de recours doit tenir compte d'une notification non délivrée selon la règle validée.

Le décideur initial ne traite pas seul l'appel d'une suspension ou d'un bannissement. Support aide l'accès au canal, sans contourner l'authentification ni modifier le verdict. Une décision annulée retire uniquement ses propres effets : ne pas lever une seconde sanction valide, republier un contenu supprimé par l'auteur ni ouvrir une audience devenue privée. Si la preuve ou le média a été purgé conformément à la politique, documenter la limite de restauration et la réponse ; ne pas recréer un contenu. La version de droits et l'état actuel du compte sont revérifiés avant chaque réparation.

### États transverses, erreurs et accessibilité

| Raison candidate | Réponse à l'utilisateur / opérateur | Trace et récupération |
| --- | --- | --- |
| `VALIDATION_FAILED` | Champ à corriger, libellé localisé ; pas de succès | Code + champ, pas de récit sensible dans les logs généraux |
| `AUTH_REQUIRED` / `ACTION_FORBIDDEN` | Reprise d'accès ou action refusée | Audit de l'action sensible ; maintien de l'accès au recours par canal dédié |
| `TARGET_UNAVAILABLE` | Cible indisponible ; options de signalement encore autorisées | Ne pas distinguer absence et droit perdu si cela divulgue une donnée |
| `RATE_LIMITED` | Délai/reprise et voie urgente/Support autorisée | Compteur minimal, alerte de saturation ; pas d'identité publique du déclarant |
| `VERSION_CONFLICT` | Décision ou relation modifiée ; recharger avant confirmation | Versions et acteur, aucune écriture obsolète |
| `IDEMPOTENCY_CONFLICT` | Même clé avec contenu différent : nouvelle intention à confirmer | Aucun second effet ; ne pas retourner le résultat d'un autre acteur |
| `DEPENDENCY_UNAVAILABLE` / `APPLY_PARTIAL` | En attente ou application partielle, surfaces restantes identifiées | Retry contrôlé, alerte, propriétaire de réparation ; pas de clôture trompeuse |
| `NOTIFICATION_FAILED` | Statut de remise distinct ; centre de décision consultable | Nouvelle tentative sans doubler la sanction ; fallback autorisé |

Codes candidats à normaliser par 04 ; pas de codes HTTP imposés. Vide/chargement doivent être distincts, les échecs annoncés par lecteur d'écran, le focus rendu à la cible utile après modale et toutes les actions possibles au clavier. Libellés sans couleur comme seul indicateur ; texte simple et localisé, langues/écritures définies par 16. Ne pas exposer de preuve sensible dans notification push/email ou aperçu de liste.

## Permissions, données et contrats

### Matrice d'accès proposée — revue obligatoire 14/15/10

| Acteur | Autorisé sous condition | Refus / limite |
| --- | --- | --- |
| Anonyme / victime sans accès | Canal externe minimal vérifié selon contrat Support | Aucun accès aux dossiers privés ou preuves par identifiant deviné |
| Membre authentifié | Bloquer/sourdine pour soi, signaler cible admissible, lire son suivi synthétique | Ne lit pas le dossier interne, les autres déclarants, ni ne décide de sanction |
| Auteur / personne visée | Consulter sa décision, explication et recours | Pas d'identité ni de note privée du déclarant ; preuves expurgées si communiquées |
| Compte bloqué | Recours/signalement via voies autorisées | Ne contourne pas le blocage pour interagir ou retrouver du contenu protégé |
| Compte suspendu/banni | Consulter/contester ses décisions après vérification ; demandes privacy autorisées | Ne retrouve pas ses capacités sociales par la route de recours |
| Support | Suivi et aide de récupération selon habilitation | Pas de preuve brute, de bannissement ou d'usurpation de session par défaut |
| Modérateur plateforme | Dossiers affectés/périmètre habilité, décisions limitées | Aucun accès global implicite ; lecture preuve et action sont deux droits |
| Expert sensible / responsable | Accès sensible ou mesure lourde explicitement habilités | Pas d'export massif ni de double validation par la même personne |
| Examinateur de recours | Décision contestée et preuves nécessaires | Pas d'auto-revue d'une sanction grave ; limites identiques d'accès sensible |
| Responsable communautaire | Actions de son groupe approuvées ; transfert au niveau plateforme | Pas de dossiers globaux, d'identité du déclarant par défaut ou de bannissement plateforme |
| Service d'application | Appliquer/annuler une décision enregistrée dans son périmètre | Ne choisit pas de sanction ni ne lit tout le récit ; pas d'opération privilégiée générique |

Toute consultation sensible et toute mutation contrôlent les droits côté serveur. L'accès d'urgence, si retenu, exige motif, durée et revue ultérieure ; aucun rôle « administrateur » n'annule automatiquement ces règles. Une demande de rétention légale ou d'accès institutionnel suit un canal 15 distinct.

### Données et cycle de vie candidat

| Catégorie / origine | Champs, finalité, accès et propriétaire | Cycle à spécifier avec 15 |
| --- | --- | --- |
| Blocage/sourdine — membre | Acteur, cible, type, état, dates/version ; exécuter préférence ; 09/04 | Modifiable par membre ; export limité à ses relations autorisées ; purge après fin de finalité selon politique |
| Signalement — déclarant | Cible/révision, motif, récit facultatif, identité minimale, canal, date ; instruire ; 09 | Accès synthétique au déclarant, interne restreint ; correction additive ; durée après clôture et droits tiers à trancher |
| Preuve — contenu autorisé / canal sécurisé | Référence, capture minimale si justifiée, empreinte, provenance et date ; établir faits ; 09 avec 14 | Espace séparé proposé, accès journalisé ; export expurgé ; purge/gel motivés ; aucun envoi aux outils généraux |
| Dossier/décision/recours — opérateur/membre | Statuts, affectation, règle/version, justification, durée, liens décisions ; traitement et contestation ; 09/10 | Historique append-only logique proposé ; correction liée ; rétention compatible avec recours à décider |
| Exécution/notification — services | action_id, decision_id, versions, résultats par surface, erreurs, remise ; fiabilité ; 04/10 | Pas de corps de contenu dans métriques ; reprendre/purger selon politique |
| Audit — services et opérateurs | Qui/quand/quoi/pourquoi, rôle, corrélation, preuve référencée, version de règle/modèle ; responsabilité ; 14/09 | Intégrité vérifiable, accès contrôlé ; pas de secrets ni de récit brut ; durée/export spécifiques à décider |
| Signaux anti-abus — événements minimisés | Fréquence et similarité utiles, version de règle, explication ; 07/09/14 | Pas de collecte sensible ou fingerprinting par défaut ; chaque signal exige finalité et rétention validées |

Stockage transactionnel logique pour états, stockage de preuve isolé et journal protégé sont des propositions à examiner par 03/04/14/15 ; aucune table, migration ni fournisseur n'est imposé. Les suppressions de compte ne doivent ni effacer aveuglément une obligation de conservation établie ni justifier une conservation indéfinie de tous les signalements. 15 doit fournir durées chiffrées, point de départ, exceptions, responsables de gel/levée, traitement des sauvegardes et exports avant réalisation de ce lot.

La restauration d'une sauvegarde doit rejouer retraits, suppressions et décisions de purge avant exposition du service. Une restauration ne recrée pas l'accès aux preuves expirées ou à un contenu interdit. Les identifiants de tiers et l'identité du déclarant sont examinés avant tout export ou accès à une décision.

### Interfaces candidates — à contractualiser par 04/03

Les labels ci-dessous sont des opérations rattachées aux FEAT, version de travail 0.1 ; ce ne sont pas des endpoints ni des contrats API approuvés. Exemples uniquement synthétiques. Aucun timeout, quota ou délai de propagation numérique n'est présenté comme validé.

| Opération / FEAT | Producteur → consommateur ; droits | Entrée → sortie conceptuelles | Reprise / concurrence / vérification |
| --- | --- | --- | --- |
| `set-safety-relation` / FEAT-012 | 04 → 05/06 ; membre pour soi | target_id, block/mute, desired_state, expected_version, request_key → état, version, effets | Idempotence acteur+cible+clé ; conflit de version ; test AC-J04-01 |
| `submit-report` / FEAT-013 | 04 → 05/06/10 ; déclarant ou voie externe vérifiée | target_ref, category, contexte facultatif, request_key → report_id, received_at, statut synthétique | Rejouer sans nouveau dossier de la même soumission ; plusieurs déclarants restent distincts ; AC-J04-02/04 |
| `get-report-status` / FEAT-013 | 04 → membre/10 ; propriétaire du signalement | report_id → statut expurgé, résultat permis | Auth à chaque lecture ; limite/pagination pour listes ; aucun détail d'autres déclarants ; AC-J04-03 |
| `record-decision` / FEAT-014 | 04 → 10 ; opérateur habilité et second contrôle si requis | case_id, expected_version, policy_ref, reason, action, scope, expiry, request_key → decision_id, action_id, PENDING | Validation règle/portée/durée, journal durable ; aucun événement d'exécution sans décision durable ; AC-J05-01/02 |
| `apply-enforcement` / FEAT-014 | 04 → 08/fil/profil/commentaires/notifications, plus 07 et recherche FEAT-023 à leur ouverture ; service authentifié | decision_id, action_id, target/version, action → résultat par surface | Livraison au moins une fois candidate, déduplication action+cible+version ; résultat ancien ne remplace pas une annulation plus récente ; AC-J05-03 |
| `submit-appeal` / FEAT-015 | 04 → 05/06/10 ; personne affectée via canal autorisé | decision_id, contexte, request_key → appeal_id, statut | Vérifier admissibilité et identité ; même soumission rejouable ; AC-J05-04 |
| `resolve-appeal` / FEAT-015 | 04 → 10 ; examinateur habilité | appeal_id, expected_version, verdict, raison → nouvelle décision, réparation attendue | Annulation ciblée, pas de restauration contre droits actuels ; AC-J05-05 |
| `notify-decision` / FEAT-014/015 | 04 → canal choisi avec 10/02 | decision_id, destinataire autorisé, modèle/version → notification_id, état | Retry ne crée pas une seconde sanction ; contenu expurgé et centre de décision de repli |

Authentification : sessions membres pour les actions personnelles, authentification opérateur renforcée définie par 14, identité de service dédiée pour exécution ; un jeton seul ne dispense pas du contrôle d'autorisation de ressource. Les schémas imposeront taille/format, enum de motifs, bornes de récit et liste d'actions permises ; valeurs à recevoir de 04/14/15. Chaque opération porte une corrélation et des versions de données/politique.

Timeout, nombre de retries, backoff et durée de rétention des clés doivent être fournis par 04/14 avant implémentation. Invariants proposés : timeout = issue inconnue, lecture d'état avant répétition ; retries bornés pour pannes transitoires ; aucun retry automatique sur validation/droits ; file de réparation visible si épuisement. L'annulation utilise une commande nouvelle liée, pas une réutilisation ambiguë de la clé initiale. Événements avec IDs et transitions seulement, sans récit/preuve sensible. Évolution additive compatible autant que possible ; valeur de sanction inconnue refusée côté opérateur et affichée prudemment côté client. Une rupture de schéma nécessite version et coordination des consommateurs.

## Acceptation et vérification

Les critères HQ existants sont conservés ; les extensions AC-TS-* et TEST-09xx sont proposés pour l'équipe 18, unicité à vérifier à l'intégration. Tous sont **PLANNED** et aucun n'est un résultat applicatif. Leur exécution dépend des décisions et de l'implémentation ; les essais d'application sont actuellement non exécutables.

| Critère | FEAT | Précondition, action et résultat observable | Test proposé / type | Statut / blocage |
| --- | --- | --- | --- | --- |
| AC-J04-01 | FEAT-012 | Blocage confirmé ; tentative d'abonnement/commentaire/réaction via API ; refus sans écriture ni notification | TEST-0901 API/E2E | PLANNED ; matrice approuvée + code |
| AC-J04-02 | FEAT-013 | Perte réseau après réception serveur ; même soumission rejouée ; une référence stable, aucun faux accusé client | TEST-0902 intégration | PLANNED ; contrat idempotence |
| AC-J04-03 | FEAT-013 | Cible ou tiers demande dossier/notification/export ; aucune identité du déclarant ni note privée accessible | TEST-0903 permissions | PLANNED ; accès/exports validés |
| AC-J04-04 | FEAT-013 | Cible retirée pendant l'envoi ; résultat documenté et preuve autorisée seulement ; aucun objet recréé | TEST-0904 concurrence | PLANNED ; cycle de preuve |
| AC-J05-01 | FEAT-014/017 | Rôle révoqué après ouverture de console ; lecture sensible et action suivantes refusées et auditées | TEST-0905 sécurité | PLANNED ; contrat de révocation |
| AC-J05-02 | FEAT-014 | Deux opérateurs décident depuis la même version ; une écriture admise, autre conflit visible ; aucune double sanction | TEST-0906 intégration | PLANNED ; versionnement |
| AC-J05-03 | FEAT-014 | Retrait accepté mais média indisponible ; statut partiel visible, alerte et reprise ; pas de succès global annoncé | TEST-0907 panne | PLANNED ; confirmations par surface |
| AC-J05-04 | FEAT-015 | Compte suspendu vérifié ; dépôt d'appel ; suivi accessible sans rétablir capacité de publication | TEST-0908 E2E | PLANNED ; canal dédié |
| AC-J05-05 | FEAT-015 | Appel accepté alors qu'une autre sanction demeure et que l'auteur a supprimé le post ; seule mesure visée levée, post non republié | TEST-0909 intégration | PLANNED ; règles de réparation |
| AC-TS-01 | FEAT-012 | Sourdine active ; publications/notifications sociales masquées ; accès direct volontaire et décisions de service conservés | TEST-0910 E2E | PLANNED ; extension à arbitrer |
| AC-TS-02 | FEAT-014 | Notification échoue après mesure appliquée ; reprise de remise sans double mesure et décision consultable | TEST-0911 panne | PLANNED ; modèle de notification |
| AC-TS-03 | FEAT-014 | Événement d'application retardé après annulation ; refus de réappliquer une version obsolète | TEST-0912 concurrence | PLANNED ; protocole d'ordonnancement |
| AC-TS-04 | FEAT-013/014 | Plusieurs comptes coordonnés signalent le même contenu permis ; volume seul n'entraîne aucune sanction | TEST-0913 abus | PLANNED ; fixtures synthétiques et règle |
| AC-TS-05 | FEAT-014 | Cas mineur/urgence détecté hors horaires ; relais affecté, accès restreint et délais réels mesurés | TEST-0914 exercice | PLANNED ; astreinte non reçue |
| AC-TS-06 | FEAT-014/015 | Même personne tente double validation ou appel grave de sa décision ; refus et attribution indépendante | TEST-0915 permissions | PLANNED ; rôles validés |
| AC-TS-07 | FEAT-013/015 | Clavier/lecteur d'écran et langues retenues ; signalement, erreur, confirmation et recours compréhensibles | TEST-0916 accessibilité | PLANNED ; écrans/locale |
| AC-TS-08 | FEAT-014/016 | Restauration après purge/retrait ; rejeu des décisions avant remise en ligne, aucune réexposition | TEST-0917 reprise | PLANNED ; politique rétention et runbook |
| AC-J07-02 | FEAT-020/017 | Modérateur local tente dossier hors groupe ou global ; refus sans exposition d'identité | TEST-0918 permissions | PLANNED ; communautés conditionnelles |

Mesures proposées avec 13/15 : latence réception→première revue et →décision en médiane/p95, stock/âge par urgence et langue, taux de décisions annulées parmi les recours résolus, réouvertures, faux positifs/faux négatifs sur échantillons revus, coût/temps par cas, temps de réparation et exposition avant retrait. Ne pas déduire la justesse de toutes les décisions du seul taux d'appel ; les personnes n'appelant pas peuvent aussi subir une erreur. Pas de texte brut ni identifiant de victime dans les tableaux agrégés.

## Décisions importantes à soumettre

Ces fiches alimentent DEC-0001/DEC-0002 encore attendues au registre ; aucun nouvel ID DEC global n'est réservé ici. Le rejet d'une alternative reste proposé.

| Champ | Socle opérationnel et politique d'âge | Étendue du blocage et automatisation |
| --- | --- | --- |
| Objectif / problème | Pilote exploitable malgré abus et recours ; couverture et âge non arrêtés | Contrôle utilisateur sans fausse promesse d'invisibilité ni sanction arbitraire |
| Solution candidate | Socle FEAT-012 à FEAT-015 avec FEAT-017 ; articulation avec FEAT-016 propriété de 15 ; périmètre proportionné à la capacité ; procédure mineurs même si pilote adultes | Matrice FEAT-012 ci-dessus ; décisions lourdes humaines ; règles anti-spam réversibles |
| Alternatives | Pilote réservé aux adultes, ou ouvert à des mineurs avec protections et opérations adaptées ; réserver aux adultes ne prouve pas absence de mineurs. Ouvrir sans équipe : rejet recommandé | Masquer seulement dans le fil : moins complexe mais protection moindre. Tout automatiser : réduit la charge apparente mais erreurs et recours accrus |
| Dépendances | 00/01/10/14/15/16/19 ; admissibilité, règles, budget et horaires | 01/03/04/07/08/14/15 ; audience, caches, signalement et droits |
| Impact business | Coût humain, périmètre et date de lancement ; confiance et prévention du préjudice | Friction d'usage, coût de modération et contestation ; effets possibles sur croissance |
| Impact technique | Console, audit, canal d'appel sous suspension, preuves sensibles et escalades | Contrôles de lecture/écriture cohérents, versions, propagation, réparation |
| Risques / prévention | Couverture fictive : exercice prouvé ; âge mal géré : revue 15/09 avant ouverture | Surblocage et faux positifs : tests ciblés, transparence et réparation |
| Phase / priorité / validation | MVP / P0 ; MASTER avec 01/09/10/14/15 ; engagements significatifs au porteur de projet | MVP / P0, sourdine P1 ; MASTER avec 01/09/14/15 et faisabilité 03/04 |
| Réexamen / delta | À chaque ouverture de marché/surface ou saturation ; alimenter décisions, produit et opérations | À changement d'audience, nouvelle surface ou dérive d'erreurs ; compléter FEAT-012 et contrats |

## Dépendances, risques et transmission

### Écarts avec les brouillons et questions ciblées

Le catalogue donne FEAT-033 au Long terme : les mentions antérieures de live/vidéo dans la vision T&S ne valent donc pas engagement MVP. La sourdine figurait au mandat mais n'était pas détaillée dans FEAT-012 : demander à 01 de confirmer son rattachement et sa phase. La formule antérieure « restaurer le contenu après appel » est restreinte ici aux droits et données encore valides, conformément à AC-J05-05. La notion antérieure de « mesure réversible » est un objectif : une purge exécutée ou une copie déjà vue ne se répare pas intégralement. Aucun conflit avec une décision spécialisée approuvée n'est établi dans les entrées reçues.

Pour les mineurs, ne pas décider seul âge minimum, vérification, défauts de visibilité ou publicité : 15/01 doivent proposer options à MASTER, 09 instruit les risques. Le pilote sans messages ni live réduit certaines surfaces d'abus mais n'exclut ni harcèlement via commentaires ni sollicitation via profil/image.

### Demandes inter-équipes

IDs INT-0901 à INT-0908 proposés, à harmoniser par 00/17 ; ils complètent INT-0004. Émetteur pour toutes les lignes : 09. **À TRANSMETTRE** ; publication GitHub ne prouve pas réception par les discussions.

| ID | Destinataire | Question et livrable attendu ; delta de cette spécification | Blocage réel |
| --- | --- | --- | --- |
| INT-0901 | 00/01/16/19 | Confirmer surfaces, publics/âge, pays, langues et communautés ; comparer capacité proposée aux ambitions ; décision DEC-0001/0002 | Lot de permissions et lancement ; rédaction indépendante possible |
| INT-0902 | 14/15 | Examiner matrice d'accès, preuve/cycle et mineurs ; fournir politique de rétention chiffrée, droits/export, canal urgent et pouvoirs | Implémentation données sensibles et ouverture |
| INT-0903 | 03/04/08 | Formaliser huit opérations candidates, versions, délais de propagation, retries/quotas et révocation original/dérivés/cache ; retour ciblé sections interfaces et états | Implémentation des mesures et du blocage |
| INT-0904 | 10/00/19 | Nommer opérateurs/suppléants, estimer charge/budget ; accepter ou ajuster cibles U0–U3 et recours ; produire planning et exercice | Lancement ; aucune couverture supposée |
| INT-0905 | 02/05/06/16 | Écrans et libellés blocage/sourdine, signalement, décision, appel sous suspension, langues et accessibilité ; phase sourdine à confirmer par 01 | Implémentation des clients retenus |
| INT-0906 | 18/21 | Reprendre 18 critères et tests, inspecter cas partiels/permissions ; fournir plan d'exécution et revue indépendante | Validation du lot ; pas d'implémentation à tester encore |
| INT-0907 | 07/13/15 | Évaluer règles simples sans modèle ; proposer métriques minimales, calibration et limites de données | Non bloquant pour rédaction ; instrumentation à valider avant collecte |
| INT-0908 | 17/00 | Intégrer chemin propriétaire, contrôler IDs proposés et inscrire la référence examinée au tableau de coordination ; ne pas actualiser l'index historique des mandats | Intégration documentaire et traçabilité |

### Risques

RISK-0002 (absence de traitement opérationnel), RISK-0003 (ouverture internationale prématurée) et RISK-0004 (contrats non alignés) restent applicables. Extensions locales proposées, probabilités non mesurées :

| ID | Risque / impact | Propriétaire et mesure | État |
| --- | --- | --- | --- |
| RISK-0901 | Mesure enregistrée mais image/cache encore diffusé : préjudice persistant | 04/08/14 ; confirmations par surface, alerte et essais de panne | OPEN — proposé |
| RISK-0902 | Brigading ou biais linguistique : suppression injustifiée | 09/07/16 ; contexte, pas de verdict au volume, revue multilingue et recours | OPEN — proposé |
| RISK-0903 | Divulgation de déclarant ou preuve mineur : dommage grave | 14/15/09 ; accès minimal, journal et export expurgé | OPEN — proposé |
| RISK-0904 | Appel inaccessible sous suspension ou auto-revue : erreur durable | 10/04/09 ; canal dédié, examinateur distinct et tests | OPEN — proposé |
| RISK-0905 | Réparation tardive écrase une autre sanction/audience : réexposition | 03/04/09 ; version attendue et annulation ciblée | OPEN — proposé |

## Compte rendu de fin d'étape

1. **Décisions prises / à valider :** structuration locale selon le mandat, conservation des FEAT ; règles, permissions, délais, âge et budget restent PROPOSÉS. Autorités et options dans les fiches ci-dessus.
2. **Livrables :** ce fichier et le README du domaine ; contribution à publier par PR depuis le SHA de référence. Les liens de commit/PR et preuves d'exécution sont portés dans la PR de livraison ; cette phrase ne prétend pas qu'une publication a déjà eu lieu.
3. **Vérification :** revue documentaire de cohérence avec FEAT-012–015/017 et J04/J05 ; contrôles dépôt à consigner dans la PR. Aucun test applicatif exécuté ; 18 scénarios PLANNED, exécution bloquée par contrats/implémentation.
4. **Questions ouvertes :** périmètre/âge/pays/langues (00/01/15/16), effet exact du blocage et sourdine (01/14/15), durée des sanctions/recours/preuves (09/15/00), moyens/cibles (10/00/19), garanties de propagation (03/04/08).
5. **Dépendances :** INT-0901 à INT-0908 ci-dessus, toutes À TRANSMETTRE ; aucune réponse externe présumée reçue.
6. **Risques / limites :** rédaction spécialisée proposée, pas un audit juridique ni une preuve de capacité ; RISK-0002–0004 et RISK-0901–0905 à instruire. Les cibles de délai ne sont ni promises ni mesurées.
7. **Suite / HQ :** faire examiner ce delta par 10/14/15 et 01 ; arbitrer le socle du pilote et la capacité avant ouverture ; 04/08 définissent les garanties, 02 les parcours, 18 les tests, 17 la consolidation et 21 la revue de PR. Fusion après revue selon la gouvernance ; la fusion documentaire ne vaut pas approbation métier.
