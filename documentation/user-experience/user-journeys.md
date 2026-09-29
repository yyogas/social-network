# Parcours UX, écrans et composants du candidat MVP

## Identification et statut

| Champ | Valeur |
| --- | --- |
| Référence / version | SN-UX-M0-001 / v0.2, adaptation GitHub du livrable v0.1 de cette équipe |
| Propriétaire | 02 — UX/UI / Design System ; personne GitHub responsable de revue NON REÇUE |
| Mandat | M0-TEAM-02 ; réponse à INT-0002 et à la campagne DIR-011 |
| Date / révision d'entrée | 29 septembre 2026 ; PR [#2](https://github.com/yyogas/social-network/pull/2), commit dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957 |
| Statut | PROPOSÉ — revue Produit, 05/06, 09/14/15/16/18 et HQ attendue |
| Priorité | P0 documentaire : rendre les parcours candidats estimables et vérifiables avant implémentation |
| Périmètre | Navigation, écrans, états, données affichées, besoins d'interface et acceptation UX |
| Exclusions | Code, choix de framework, endpoints définitifs, permissions approuvées, validation juridique, identité de marque |
| Blocages | DEC-0001/DEC-0002 ouverts ; règles d'audience, âge, session, suppression et modération non reçues |

Entrées lues : [mandat](../teams/work-orders.md), [modèle](../teams/deliverable-template.md), [plan documentaire](../documentation-plan.md), [vision](../product/product-vision.md), [catalogue](../product/feature-catalog.md), [parcours métier](../product/user-journeys.md), [gouvernance](../governance.md), [registre](../project-governance/decision-register.md), [conventions](../repository-conventions.md), [stratégie de tests](../quality/test-strategy.md).

**CONFIRMÉ :** mandat documentaire, responsabilité 02, réutilisation des identifiants FEAT/J/AC du dépôt et existence des documents d'entrée à ce SHA. **PROPOSÉ :** comportements UX et classement du catalogue repris ci-dessous. **À VÉRIFIER :** compréhension par les utilisateurs, faisabilité Web/Mobile, contrastes et comportement assistif. **NON REÇU :** décisions spécialisées finales et preuves d'implémentation. Aucun prototype, audit d'accessibilité ou test applicatif exécuté n'est revendiqué.

Ce fichier reprend les parcours, états et composants rédigés dans les deux travaux antérieurs de cette discussion (exploration UX/UI générale v0.1 et fondation SN-UX-M0-001 v0.1). Leur contenu utile est intégré ici : ces fichiers conversationnels ne sont pas des dépendances nécessaires pour comprendre la présente spécification. GitHub est la référence de revue. Les identifiants SN-UX-Sxx sont des écrans, pas des fonctionnalités concurrentes des FEAT.

## Besoin, fonctionnalités et parcours

### Classement et couverture

Toutes les phases et priorités ci-dessous restent **PROPOSÉES**. FEAT-020 est conditionnelle. FEAT-018 ne tranche pas à elle seule la surface de lancement.

| Fonctionnalités | Acteur / problème et résultat attendu | Phase / priorité | Parcours / écrans | Conditions et dépendances |
| --- | --- | --- | --- | --- |
| FEAT-001, FEAT-002 | Visiteur/membre : accéder et reprendre accès sans confusion | MVP / P0 | J01 ; S01/S02/S12 | 04/14/15 : admissibilité, activation, sessions et récupération |
| FEAT-003, FEAT-004 | Membre : se présenter et comprendre qui voit quoi | MVP / P0 | J01/J02/J06 ; S03/S06/S11 | 01/15 : champs, audiences, valeurs initiales |
| FEAT-005 | Membre : choisir ses sources | MVP / P0 | J03 ; S03/S04/S05 | 01/04/09 : suivi et effet du blocage |
| FEAT-006, FEAT-007 | Auteur : publier/corriger/retirer texte et image accessibles | MVP / P0 | J02 ; S06/S07 | 04/08/15 : limites, traitement, audience et brouillons |
| FEAT-008 | Lecteur : lire dans un ordre prévisible | MVP / P0 | J03 ; S05 | 04 : curseur, départage, invalidation |
| FEAT-009, FEAT-010 | Membre : réagir/commenter sans doublon ni faux succès | MVP / P1 | J03 ; S07 | 01/04/09 : règles de modification/retrait |
| FEAT-011, FEAT-022 | Lecteur : maîtriser alertes et fin de session | MVP / P1 | J03 ; S05/S11/S13 | 01/04/15 : catégories/canaux et synchronisation |
| FEAT-012, FEAT-013 | Personne exposée à un abus : protéger et transmettre | MVP / P0 | J04 ; S08/S11 | 09/14/15 : portée, motifs et confidentialité |
| FEAT-014, FEAT-015, FEAT-017 | Agent et personne concernée : décision et recours compréhensibles | MVP / P0 | J05 ; S09/S10 | 09/10/14/15 : rôles, preuves, réexamen et capacité |
| FEAT-016 | Titulaire : consulter ses demandes de données et suppression | MVP / P0 | J06 ; S11/S14 | 04/15 : cycle, vérification, exceptions et sauvegardes |
| FEAT-018, FEAT-021 | Tous : utiliser petits écrans et langues retenues | MVP / P0 | J01–J07 ; tous écrans | 05/06/16/18 : surface, locales et tests |
| FEAT-019 | Équipe pilote : comprendre l'utilité avec mesure minimale | MVP / P1 | Transversal | 13/15 : protocole, finalité ; aucune instrumentation définie ici |
| FEAT-020 | Membre/responsable local : échanger dans un espace délimité | MVP conditionnel / P1 | J07 ; S15 | Arbitrage HQ ; 01/09/04/15 |
| FEAT-023 | Membre : rechercher comptes/contenus/communautés | Phase 2 / P1 | Extension future S04 | Aucun moteur de recherche complet supposé au pilote |
| FEAT-024 à FEAT-028 | Messagerie, mobile natif, vidéo, studio créateur, présence professionnelle | Phase 2 / P2 | Parcours détaillés ultérieurs | 01/04/06/08/09/12/14/15 |
| FEAT-029 à FEAT-031 | Recommandations, publicité, rémunération | Phase 3 / P2 | Parcours détaillés ultérieurs | HQ et propriétaires économiques/privacy |
| FEAT-032 | Nouvelles régions/langues/opérations | International / P1 | Adaptation des parcours | 16/09/15 ; couverture humaine à prouver |
| FEAT-033, FEAT-034 | Live, écosystème développeurs | Long terme / P3 | Parcours ultérieurs | 03/04/08/09/14/15 |

Stories, événements et marketplace figuraient dans l'exploration initiale mais n'ont pas d'ID distinct dans le catalogue reçu. Proposition de classement **Phase 3, P3 à examiner** ; 01/HQ doit décider création d'ID, rattachement ou retrait. Aucun écran correspondant n'est imposé au candidat pilote.

### Navigation proposée et contrôle du temps

Sur petit écran : **Accueil**, action **Créer**, accès **Profil/paramètres**, et **Notifications** clairement accessible. Accès aux premiers profils via liens d'invitation ou sélection de comptes pilotes à examiner avec 01/19 ; pas d'obligation d'importer les contacts. S04 désigne cette sélection, pas FEAT-023. Desktop : mêmes objets dans un rail/en-tête ; colonne de lecture bornée ; pas d'information essentielle uniquement en colonne secondaire. Les outils internes ouvrent un contexte explicitement nommé, avec sortie visible.

FEAT-022 : afficher « Publications des comptes suivis, des plus récentes aux plus anciennes » lorsque ce modèle est retenu. Après consommation du curseur disponible, afficher « Vous avez vu les publications disponibles » ; ne pas annoncer avoir tout lu si des pages sont en erreur. Préférer une action « Charger la suite » à un défilement sans fin au pilote. Les nouveaux posts produisent une commande de rafraîchissement, sans déplacement automatique de la lecture. Revenir d'un détail restaure position et repère ; si le contenu a disparu, utiliser le voisin disponible. Aucun compteur de série, relance culpabilisante ou ajout automatique de sources.

La sauvegarde du repère de lecture entre sessions/appareils est **À VÉRIFIER** avec 04/15. Une conservation en mémoire de la session de navigation suffit à la proposition UX initiale ; aucun stockage durable implicite.

### Carte parcours → écrans → critères existants

| Parcours métier | Besoin et enchaînement proposé | Résultat observable | Critères métier réutilisés |
| --- | --- | --- | --- |
| J01 | S01 entrée → S02 activation → S03 profil → S11 résumé audience → S05 ; S12 pour récupération | Accès confirmé, étapes facultatives sautables, retour au lien initial si autorisé | AC-J01-01 à AC-J01-04 |
| J02 | S06 texte/image/description/audience → aperçu → envoi → S07 ; modifier ou retirer | Aucune annonce « publié » avant réponse confirmée ; portée visible avant soumission | AC-J02-01 à AC-J02-05 |
| J03 | S03/S04 suivre → S05 lire → S07 réagir/commenter → S13/S11 préférences | Fil stable, interaction confirmée ou explicitement en échec, réglage relu | AC-J03-01 à AC-J03-05 |
| J04 | S07/S03 options → S08 signalement et/ou blocage → accusé → S11 blocages | Actions distinctes ; référence si reçu, aucune promesse de sanction | AC-J04-01 à AC-J04-04 |
| J05 | S10 dossier → décision → S09 information → recours → S10 réexamen → S09 résultat | Décision, application et notification distinguées ; état du recours consultable | AC-J05-01 à AC-J05-05 |
| J06 | S11 données → S14 export ou suppression → vérification → suivi | Conséquences exactes et états réels ; résultat inaccessible à un tiers | AC-J06-01 à AC-J06-04 |
| J07 conditionnel | S15 présentation/règles → adhésion → fil → contribution → départ | Statut membre et pouvoirs locaux explicités ; refus compréhensible | AC-J07-01 à AC-J07-04 |

### Écrans et états

Les écrans S01–S11 reprennent le travail M0 antérieur, avec les corrections de périmètre ci-dessus. Tous appliquent les états communs décrits ensuite.

| Écran | Objectif / éléments et actions visibles | Navigation, mobile et desktop | États particuliers et accès |
| --- | --- | --- | --- |
| SN-UX-S01 | Présenter valeur, langue, connexion/inscription et aperçu autorisé | Entrée publique/lien profond ; colonne unique mobile | Aucun aperçu privé ; contenu absent n'empêche pas l'accès au compte |
| SN-UX-S02 | Formulaire d'accès, activation, étapes facultatives, retour | Étapes courtes ; clavier adapté ; formulaire borné desktop | Activation expirée/consommée, envoi impossible, restriction ; messages anti-énumération validés par 14 |
| SN-UX-S03 | Nom, avatar, bio, posts autorisés ; suivre, éditer, options | Profil depuis fil/lien ; retour au même contexte | Nouveau profil, auteur absent, blocage ; édition réservée au titulaire selon contrat |
| SN-UX-S04 | Trouver une première source via profils pilotes proposés ou lien | Depuis fil vide ; pas d'onglet recherche globale requis | Aucun profil proposé : expliquer et revenir ; n'exposer que profils découvrables |
| SN-UX-S05 | Fil chronologique, auteur/date/audience, interactions, fin et rafraîchissement | Carte mobile, lecture centrale desktop ; position conservée | Aucune source, aucune publication, page échouée, fin distincts ; filtre d'accès serveur |
| SN-UX-S06 | Texte, image/description, destination, audience, aperçu ; publier/abandonner | Page mobile ; aperçu élargi desktop | Upload/traitement/publication distincts ; audience manquante bloque ; brouillon selon contrat privacy |
| SN-UX-S07 | Publication, réactions et commentaires ; corriger/retirer, signaler | Détail puis retour ; champ de commentaire visible avec clavier | Sans commentaires, contenu retiré, édition concurrente, refus d'interaction |
| SN-UX-S08 | Motif/explication et effets du blocage ; confirmer/annuler | Page/panneau mobile, dialogue court desktop | Double envoi, objet supprimé, refus, référence après accusé ; identité signalant protégée |
| SN-UX-S09 | Décision, motif communicable, portée/durée, recours et statut | Depuis notification et chemin d'aide accessible selon politique de suspension | Recours indisponible avec raison ; aucune fausse promesse de délai ou d'annulation |
| SN-UX-S10 | File, dossier, preuves autorisées, action/motif/confirmation, réexamen | Desktop proposé ; triage mobile à valider ; filtres conservés | File vide, dossier concurrent, rôle révoqué, échec partiel ; pouvoirs séparés |
| SN-UX-S11 | Audience, blocages, langues/thème, notifications, données, aide | Avatar → sections ; empilé mobile, sommaire desktop | Réglage non sauvegardé indiqué ; portée et état des interrupteurs explicites |
| SN-UX-S12 | Connexion, récupération, nouvelle vérification, déconnexion | Depuis S02/aide ; retour après succès autorisé | Jeton expiré/consommé, trop de tentatives ; ne jamais conserver le secret dans brouillon |
| SN-UX-S13 | Boîte des notifications essentielles, objet/date/état lu et préférences | En-tête → boîte → objet ; plein écran mobile | Vide, objet inaccessible, données en retard ; aperçu recalculé selon autorisation actuelle |
| SN-UX-S14 | Export et suppression : conséquences, vérification, statut, accès au résultat | S11 → demande → suivi ; actions dangereuses séparées | Export expiré, demande déjà en cours, job interrompu ; annulation seulement si contrat l'autorise |
| SN-UX-S15 | Communauté conditionnelle : règles, visibilité, membres, adhésion, fil | Présentation → adhésion → fil ; entrée dédiée à arbitrer | En attente/refus/exclusion/fermeture/dernier responsable ; publication et adhésion séparées |

### Transitions, reprise et erreurs

Les raisons ci-dessous sont des catégories UX provisoires, **pas des codes API approuvés**. 04 fournit leur mapping ; 09/14/15 valident les messages sensibles.

| Déclencheur / précondition | Transition et effet visible | Erreur / récupération / annulation |
| --- | --- | --- |
| Ouverture de vue autorisée | Initial → chargement → contenu ou vide confirmé | Réseau/service : réessai local ; état vide jamais déduit d'une panne |
| Soumission de saisie valide | Édition → envoi → succès confirmé | Validation : erreurs près des champs, saisie conservée ; annuler avant envoi |
| Délai dépassé après mutation | Envoi → résultat indéterminé | Consulter statut ou réessayer avec même clé logique si contrat l'autorise ; pas de nouvelle création aveugle |
| Session expirée | Action → réauthentification requise | Sauvegarde non sensible seulement selon règle validée ; reprendre après vérification |
| Accès refusé/rôle révoqué | Donnée/action retirée → explication sobre | Ne pas répéter automatiquement ; pas de titre privé dans erreur ou toast |
| Ressource retirée/modifiée | Détail → indisponible/conflit | Recharger ; proposer comparaison du texte propre si possible, aucun écrasement silencieux |
| Limite d'usage atteinte | Refus avec explication et reprise autorisée | Afficher délai seulement si fourni ; pas de boucle de retries |
| Upload interrompu | Progression → interruption | Reprendre si protocole compatible, sinon recommencer le fichier en conservant le texte autorisé |
| Compte suspendu | Actions limitées → explication/recours permis | Aucun accès général implicite ; chemin de contestation selon règles 09/14/15 |
| Décision appliquée mais notification échouée | Deux statuts distincts dans S10 | Reprendre notification sans rejouer la sanction |
| Suppression confirmée | Demande → traitement → état final attesté | Aucun « tout effacé » avant achèvement selon contrat ; exceptions et sauvegardes expliquées |

Journalisation UX proposée : référence de requête corrélable et catégorie d'échec, sans secret, texte de publication, motif libre ni contenu d'export. Collecte et durée relèvent de 13/14/15. Hors ligne : afficher l'état connu comme tel ; aucune mutation en arrière-plan promise. Le stockage local de contenus privés et la purge lors de déconnexion doivent être arbitrés, y compris sur appareil partagé.

### Accessibilité, contenu et composants nécessaires

Propositions vérifiables : tabulation logique, activation clavier, focus visible et restauré après dialogue, libellé persistant, erreur associée au champ et résumé focalisable, état sélectionné annoncé, absence de piège clavier. Les listes dynamiques annoncent sobrement le chargement sans relire tout le fil. Les dialogues nommés ont une fermeture accessible ; les confirmations sensibles expliquent ressource et portée. Le zoom, l'agrandissement du texte, le clavier virtuel et les petites largeurs ne cachent pas les actions essentielles. Aucun geste, survol, couleur ou animation n'est l'unique moyen de comprendre/agir.

Image : description proposée dans le composer ; avatar et image décorative distingués ; le caractère obligatoire et les limites du texte alternatif sont à décider avec 01/08/18. Date complète disponible en complément du temps relatif. Tester accents, noms longs, tifinagh et chaînes RTL avec 16 ; langue d'interface, langue du contenu, résidence et origine ne sont pas confondues. Réduction du mouvement et absence d'autoplay sonore constituent des propositions UX.

Composants candidats : shell/navigation, bouton et bouton icône nommé, champ et résumé d'erreur, sélection d'audience avec explication, carte de publication, commentaire, upload/progression, menu d'options, dialogue, toast, bannière, état vide/erreur, pagination, statut de dossier et tableau de modération. Pour chacun : default, focus, pressed, selected, disabled, loading, success, error selon pertinence. Les tokens sémantiques couvrent surfaces/textes/actions/bordures/focus/états, espaces, typographie, clair/sombre et mouvement réduit. **Palette, police, breakpoints et framework ne sont pas approuvés.** Les deux thèmes restent proposés ; leur priorité de livraison doit être décidée par 01/HQ.

## Permissions, données et contrats

### Matrice de permissions candidate

| Acteur | Action / ressource / portée | Autorisation attendue à confirmer | Refus UX |
| --- | --- | --- | --- |
| Anonyme | Lire profil/publication via lien | Seulement audience publique si retenue | Connexion ou indisponible sans fuite |
| Authentifié autre que propriétaire | Lire/réagir/commenter/suivre | Audience actuelle, admissibilité, blocages et restrictions évalués serveur | Aucune interaction confirmée ; explication minimale |
| Propriétaire | Éditer/retirer profil, post/commentaire | Propriété + état de ressource et du compte | Saisie conservée si permis ; conflit/accès refusé |
| Bloqué / bloqueur | Accès et interactions croisées | Matrice de portée 09/14/15 NON REÇUE | Effet exact expliqué ; pas de promesse d'invisibilité absolue |
| Suspendu | Consultation décision/recours/données | Exceptions et authentification 09/14/15 NON REÇUES | Restrictions visibles, aide autorisée |
| Titulaire de données | Demander/télécharger export, supprimer compte | Vérification renforcée selon 14/15 | Refus d'identité/lien expiré ; aucun export tiers |
| Opérateur interne | Lire preuves, statuer, réexaminer | Permissions séparées + portée + audit ; 10/14 | Accès retiré immédiatement visible, pas de nouvelle action |
| Responsable communautaire | Gérer membres/contenus locaux | FEAT-020 approuvée et matrice locale | Aucun pouvoir global déduit |

Masquer un bouton ne remplace jamais le contrôle serveur ; mêmes règles pour API, médias directs, aperçus, notifications et cache. L'UX n'approuve aucune permission.

### Données et cycle de vie

| Catégorie / origine et champs minimum proposés | Finalité / visibilité / propriétaire métier | Stockage et accès proposés à examiner | Modification, export, suppression, conservation et sauvegardes |
| --- | --- | --- | --- |
| Compte saisi : identifiant d'accès selon méthode, langue, statut ; secrets seulement en transit vers flux prévu | Authentifier ; titulaire et opérateurs limités ; 04/14/15 | Source serveur ; aucun secret en logs/brouillons | 04/15 définissent rétention, export et suppression ; 14 purge sessions et politique sauvegarde |
| Profil saisi : nom, avatar, bio facultative, audience autorisée | Présentation ; selon visibilité ; 01/15 | Source serveur, aperçu client limité | Édition propriétaire ; purge variantes/caches ; inclusion export et restauration à définir |
| Publication/commentaire : texte, image, description, auteur, date, audience, état/version | Partage ; audience autorisée ; 01/08/09 | Source serveur et cache contrôlé ; brouillon persistant non décidé | Correction/retrait propagés ; délais, traces et sauvegardes à définir par 04/08/15 |
| Relations/préférences : suivi, blocage, catégories notifications | Fil et protection ; visibilité séparée ; 01/09/15 | Serveur, représentation client limitée | Désabonnement/déblocage/réglage ; audit minimal et rétention/export à définir |
| Dossier : objet, catégorie, note éventuelle, référence, état, décision/recours | Protection ; demandeur et agents habilités ; 09/10/15 | Preuves dans stockage contrôlé, pas analytics | Correction/recours ; conservation, exceptions d'effacement et restauration à définir |
| Export/suppression : ID demande, état, dates, référence de téléchargement temporaire | Droits du titulaire ; 15/04 | Accès authentifié ; pas de lien secret en journal | Expiration et purge ; états d'erreur/reprise ; effet des sauvegardes explicitement NON REÇU |
| Repère de lecture/mesures : position temporaire, événements strictement nécessaires si approuvés | Retour de navigation et mesure ; 02/13/15 | Mémoire de session proposée ; aucun SDK choisi | Pas de durée inventée ; consentement/base, agrégation, export et purge à décider si collecte |

Aucune durée légale ni schéma de base de données n'est arrêté ici. Les aperçus et fichiers dérivés font partie de la propagation des restrictions. Aucun exemple ne contient de données réelles.

### Besoins d'interface transmis à 04

Chaque ligne réutilise un FEAT comme ancrage ; **ID/version API définitifs NON REÇUS**. Ce tableau propose des besoins de données UI, pas des endpoints ou schémas exécutables.

| Ancrage | Producteur → consommateur / entrée candidate | Sortie candidate / validation / défaillance |
| --- | --- | --- |
| FEAT-001/002 | 04 → clients 05/06 ; preuve d'accès selon méthode | État compte/session et étape suivante ; expiration/limite/refus ; reprise J01 |
| FEAT-004/006/007 | 04/08 → composer ; texte, média, description, audience, version attendue, clé logique | ID/état/version et erreurs de champ ; limites serveur ; upload et publication distingués |
| FEAT-005/008 | 04 → fil/profil ; relation voulue, curseur opaque | État relation, éléments autorisés, prochain curseur, fin fiable ; invalidation et doublons |
| FEAT-009/010/011 | 04 → détail/notifications ; action voulue, texte ou préférence et version | État confirmé, compteur autorisé ; conflit/retrait ; pas de replay créant doublon |
| FEAT-012/013 | 04/09 → S08 ; cible, action, catégorie, note permise | Référence et état reçu ; doublon/cible retirée selon contrat ; confidentialité |
| FEAT-014/015/017 | 04/10 → console/recours ; dossier/version/action/motif | Décision, application, notification, recours séparés ; conflit et échec partiel |
| FEAT-016 | 04 → S14 ; type de demande, vérification, ID | États et moyen d'accès autorisé ; expiration/échec/reprise ; aucune suppression supposée synchrone |

Pour **chaque** interface : authentification et autorisation côté serveur par 04/14 ; validation des champs et limites par propriétaire ; timeout chiffré NON REÇU ; délai dépassé traité comme résultat inconnu pour une mutation ; retry borné/idempotence/concurrence définis par 04 ; aucune mutation rejouée sans garantie. Version attendue ou équivalent à décider pour édition/décision. Correlation ID sans secret ; audit des actions sensibles par 14/10. Compatibilité : champ/état inconnu → message sûr et rafraîchissement, jamais succès par défaut. Dépréciation, quotas, mécanisme d'authentification et tests de contrat restent à fournir. Une défaillance média ne doit pas devenir une fausse publication réussie.

## Acceptation et vérification

Les critères AC-J existants restent la référence métier ; compléments ci-dessous ont des identifiants locaux de revue UX à faire intégrer par 18/17. Tous les tests applicatifs sont **PLANNED** ; leurs IDs canoniques, environnement et preuves sont NON REÇUS.

| Critère local / ancrage | Précondition → action → résultat observable | Type prévu / propriétaire | Statut / blocage |
| --- | --- | --- | --- |
| UX-AC-01 / AC-J01-02 | Activation expirée → ouvrir lien → erreur nommée, action de reprise, aucun succès | E2E / 04/18 | PLANNED ; méthode d'accès |
| UX-AC-02 / AC-J01-04 | Récupération → saisie valide/inconnue → réponse ne révélant pas données privées ; focus sur étape suivante | UX/API / 14/18 | PLANNED ; messages |
| UX-AC-03 / AC-J02-01 | Audience définie → aperçu puis publier → même audience nommée avant et après confirmation | UX/E2E / 02/18 | PLANNED ; matrice audiences |
| UX-AC-04 / AC-J02-02 | Upload échoué → soumettre → aucun post marqué publié, texte récupérable selon contrat | E2E / 08/18 | PLANNED ; brouillons |
| UX-AC-05 / AC-J02-03 | Réponse perdue → réessai autorisé → un seul objet confirmé et état compréhensible | Intégration/E2E / 04/18 | PLANNED ; idempotence |
| UX-AC-06 / AC-J03-01 | Nouvelles publications pendant lecture → arriver → bouton rafraîchir, aucun saut de position | E2E / 05/18 | PLANNED ; pagination |
| UX-AC-07 / FEAT-022 | Dernière page confirmée → terminer → fin réelle ; page échouée → réessai, pas « tout vu » | UX/E2E / 02/18 | PLANNED ; signal de fin |
| UX-AC-08 / AC-J03-02 | Droits retirés → commenter → refus, pas de commentaire confirmé ni aperçu privé | API/E2E / 04/18 | PLANNED ; permissions |
| UX-AC-09 / AC-J03-03 | Préférence sauvegardée → recharger → même état ; échec → « non enregistré » | E2E / 04/18 | PLANNED ; catégories/canaux |
| UX-AC-10 / AC-J04-02 | Réseau coupé → signaler → aucun accusé reçu fictif ; référence après reprise confirmée | E2E / 09/18 | PLANNED ; contrat dossiers |
| UX-AC-11 / AC-J04-01 | Bloquer confirmé → afficher explication → seules conséquences de la matrice promises | UX/API / 09/18 | PLANNED ; portée |
| UX-AC-12 / AC-J05-02 | Dossier traité ailleurs → confirmer → conflit, rafraîchissement et aucune seconde sanction | Intégration/E2E / 10/18 | PLANNED ; concurrence |
| UX-AC-13 / AC-J05-03 | Sanction appliquée, notification échouée → consulter → deux états distincts, reprise notification seule | E2E / 10/18 | PLANNED ; états métier |
| UX-AC-14 / AC-J05-04 | Compte restreint → chemin autorisé → décision et recours accessibles selon exceptions validées | E2E / 09/14/18 | PLANNED ; politique suspension |
| UX-AC-15 / AC-J06-01 | Export expiré ou autre titulaire → ouvrir → refus et voie légitime de nouvelle demande | API/E2E / 15/18 | PLANNED ; cycle export |
| UX-AC-16 / AC-J06-03 | Suppression en cours → consulter → état réel et limites approuvées, pas d'effacement instantané annoncé | UX/E2E / 15/18 | PLANNED ; cycle/sauvegardes |
| UX-AC-17 / AC-J07-03 | Rôle communauté retiré → action locale → refus et commandes mises à jour | API/E2E / 01/18 | PLANNED ; inclusion FEAT-020 |
| UX-AC-18 / AC-J03-04 | Clavier seul → J01/J02/J04/J06 → toutes actions réalisables, focus visible/restauré, aucune impasse | Manuel assistif / 02/18 | PLANNED ; prototype/application |
| UX-AC-19 / FEAT-018/021 | Petite largeur, zoom et chaîne longue → écran → actions, erreurs et ordre de lecture restent accessibles | Manuel responsive / 05/16/18 | PLANNED ; tailles/locales |
| UX-AC-20 / FEAT-022 | Lecture terminée → quitter puis retour navigation → aucun contenu injecté ni relance contraignante | UX / 02/18 | PLANNED ; protocole pilote |

Aucun seuil de réussite d'étude utilisateur n'est inventé. Protocole proposé : tâches de compréhension d'audience, reprise d'erreur, signalement et fin de lecture ; noter réussite sans aide, erreur critique et verbatim anonymisé seulement selon consentement/protocole 13/15. Taille d'échantillon, recrutement, modalités assistives et conservation à définir avec 19/18/15.

## Fiche de décision importante et contradictions

**Décision de référence : DEC-0002, ouverte au HQ.** Contribution UX, aucune nouvelle décision globale attribuée.

| Champ | Proposition |
| --- | --- |
| Objectif / problème | Un premier fil utile sans complexité excessive ; population et sources pilotes encore hypothétiques |
| Solution candidate | Pilote fondé sur suivi de personnes, entrée aux profils pilotes, fil chronologique et contrôle de fin ; FEAT-020 examinée séparément |
| Alternatives non rejetées | Communautés dès pilote : valeur possible pour groupes constitués, coût supplémentaire rôles/modération ; les deux modèles : couverture plus large mais risque de périmètre |
| Dépendances | 01/19 pour recrutement/valeur ; 09/10 pour capacité ; 04 pour modèle ; 15 pour visibilité |
| Risques | Fil vide, confusion audience, modération insuffisante ; RISK-0001/0002/0004 |
| Impact business | Onboarding plus court proposé ; besoin de contenus initiaux ; aucune estimation chiffrée validée |
| Impact technique | Moins de contextes d'adhésion si communautés différées ; le choix exact relève de 03/04 |
| Priorité / phase | P0 arbitrage / MVP candidat |
| Réexamen / delta | Retours pilote ou recrutement fondé sur groupes ; modifier catalogue/parcours après décision HQ, sans changer silencieusement leurs phases |

| Contradiction / lacune | Références | Traitement de cette contribution / question ciblée |
| --- | --- | --- |
| Recherche et messagerie initialement proposées MVP | Exploration UX générale v0.1 vs FEAT-023/024 Phase 2 | Alignement documentaire sur classement HQ proposé ; S04 limité aux premières sources ; 01 valide cette limite |
| Mobile et vidéo trop larges dans exploration | Ancienne v0.1 vs FEAT-025/026 | Phase 2 reprise comme proposition ; responsive décrit, aucune priorité de surface approuvée |
| Quatre parcours anciens ne couvraient pas récupération/export/suppression | Fondation v0.1 vs J01/J06 | S12/S14 et critères ajoutés ; 14/15 définissent règles |
| Thèmes et recherche non nécessaires à figer M0 | Palette/menus anciens vs absence de validation | Tokens et navigation proposés, pas de framework ni palette canonique |
| Communautés restent indécises | FEAT-020 et J07 | S15 conditionnel, aucun rôle communautaire accordé par design |

## Dépendances, risques et transmission

Réutiliser les INT du registre ; les demandes détaillées ci-dessous sont des deltas de INT-0002. Les destinataires n'ont pas encore répondu dans cette contribution. **À TRANSMETTRE** pour chaque ligne ; publication d'une PR ne vaut pas réception par une discussion.

| Référence | Destinataire | Question / livrable attendu | Blocage concret |
| --- | --- | --- | --- |
| INT-0002 lié à INT-0001 | 01/HQ/19 | Personnes/communautés ? Première source sans FEAT-023 ? Décision et cohorte pilote | Navigation et validation de J03/J07 ; wireframes indépendants possibles |
| INT-0002 lié à INT-0004 | 09/10 | Portée blocage, motifs, états et recours du compte suspendu ; matrice et textes | S08–S10 finalisés |
| INT-0002 lié à INT-0005 | 15/14 | Audiences par défaut, persistance brouillons, export/suppression et accès restreint | S02/S06/S14 finalisés |
| INT-0002 lié à INT-0003 | 03/04/08 | Mapping erreurs, états média, résultat inconnu, version et reprise | Contrats UI implémentables |
| INT-0002 lié à INT-0009 | 16 | Locales, scripts, textes de sécurité et repli ; corpus synthétique | Recette linguistique |
| INT-0002 | 05/06 | Contraintes lien profond, clavier, cache, offline et surface retenue | Estimation et états finaux par plateforme |
| INT-0002 lié à INT-0008 | 18 | Reprendre AC-J et UX-AC ; protocole assistif et preuves | Tests exécutables et preuve release |
| INT-0002 lié à INT-0010/0006/0007 | 17/20/21 | Indexer ce chemin, revue des IDs/liens et composants après validation | Intégration documentaire ; pas de code avant contrats |

Risques rattachés au registre : **RISK-0001** (surcroît MVP via recherche/communautés), **RISK-0002** (signalement/recours sans capacité), **RISK-0003** (langues affichées sans support), **RISK-0004** (états UI différents du serveur). Risque UX spécifique à examiner par 15/14 : divulgation par audience ambiguë ou brouillon sur appareil partagé ; mitigation proposée : audience explicite, politique de persistance, purge et tests négatifs. Statut OUVERT ; gravité finale et nouveau RISK éventuel à attribuer par HQ. Aucun conflit n'est déclaré résolu par une équipe tierce.

## Compte rendu de fin d'étape

1. **Décisions prises / à valider :** adoption locale du chemin et des IDs existants ; 15 écrans et 20 compléments d'acceptation proposés. Arbitrages DEC-0001/0002, permissions et données restent ouverts.
2. **Livrable :** ce fichier SN-UX-M0-001 v0.2 ; delta spécialisé sur la PR #2, base exacte indiquée en tête. Référence de commit/PR de publication à consulter dans la PR qui ajoute le fichier.
3. **Vérification :** contrôles documentaires à exécuter avant publication et à consigner dans la PR avec commandes/résultats. Aucun test applicatif, test utilisateur ou audit d'accessibilité exécuté.
4. **Questions :** première source, communautés, surface, audiences, brouillons, suppression, suspension/recours, langues ; propriétaires et blocages au tableau.
5. **Dépendances :** INT-0002 et liens ci-dessus ; handoffs À TRANSMETTRE, aucun avis externe supposé reçu.
6. **Risques :** périmètre, confidentialité, capacité humaine, localisation et contrats ; aucune fonctionnalité déclarée implémentée.
7. **Suite / HQ :** recueillir les réponses ciblées ; arbitrer DEC-0002 ; normaliser avec 17 ; demander revue 21 et revues métier ; produire wireframes/prototype du lot validé. Fusion documentaire éventuelle ne vaut pas autorisation d'implémentation.
