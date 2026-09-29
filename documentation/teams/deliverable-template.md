# Modèle de livrable spécialisé

Ce modèle est proposé pour les travaux M0 et les évolutions suivantes. Copier les sections utiles dans un fichier nommé selon sa responsabilité, sans recopier le modèle dans chaque conversation. Pour une petite modification, un delta précis suffit. Un champ non applicable doit expliquer pourquoi ; un champ inconnu reste ouvert avec un propriétaire.

## Identification et statut

| Champ | Valeur à renseigner |
| --- | --- |
| Titre et objectif du livrable | Résultat concret attendu |
| Propriétaire | Numéro et nom de l'équipe ; personne GitHub si confirmée |
| Contributeurs et destinataires | Équipes réellement concernées |
| Date / révision | Date et SHA de référence ; pas de faux SHA |
| Références d'entrée | Documents, décisions, issue et PR existants |
| Statut du document | PROPOSÉ / EN REVUE / APPROUVÉ, avec autorité et preuve pour l'approbation |
| Nature de chaque affirmation | CONFIRMÉ / PROPOSÉ / À VÉRIFIER ; preuve ou hypothèse associée |
| Classement | MVP / Phase 2 / Phase 3 / International / Long terme ; classement proposé ou approuvé |
| Priorité | P0 / P1 / P2 / P3 avec justification |
| Périmètre | Ce qui est traité et explicitement exclu |
| Dépendances bloquantes | ID, propriétaire, réponse attendue et conséquence |

Une pièce produite n'est pas automatiquement approuvée ; une spécification approuvée n'est pas automatiquement implémentée ou vérifiée. Marquer séparément ces états avec leurs preuves. Réutiliser les identifiants existants. Si aucun n'existe, proposer un ID stable selon le [plan documentaire](../documentation-plan.md), puis vérifier son unicité lors de l'intégration.

## Besoin, fonctionnalités et parcours

Pour chaque besoin ou fonctionnalité : ID, utilisateur/acteur concerné, problème, résultat attendu, phase, priorité, préconditions et critères de succès. Distinguer les demandes du porteur du projet des hypothèses de l'équipe.

| Élément | Description attendue |
| --- | --- |
| Parcours normal | Étapes et résultat observable |
| États | Initial, vide, chargement, succès, erreur, indisponible, supprimé ou suspendu si applicables |
| Transitions | Déclencheur, précondition, effet, annulation et reprise |
| Erreurs | Code/raison, réponse utilisateur, journalisation et récupération |
| Cas limites | Doublon, concurrence, réseau lent/interrompu, ressource supprimée, changement de droits |
| UX et accessibilité | Navigation, libellés, clavier, focus, lecture assistée et adaptation aux langues |
| Hors périmètre | Comportements non pris en charge et effet pour l'utilisateur |

## Permissions, données et contrats

### Permissions

Décrire acteur/rôle, action, ressource, portée, règle d'autorisation et refus attendu. Inclure les états anonyme, authentifié, propriétaire, autre utilisateur, bloqué/suspendu et opérateur interne lorsque pertinents. La présence d'un bouton masqué ne constitue pas un contrôle d'accès. Les propositions structurantes sont à faire examiner par 14, les propriétaires métier et le HQ.

### Données et cycle de vie

Pour chaque catégorie : origine, champs nécessaires, finalité, visibilité, propriétaire métier, stockage proposé, accès internes, événements/journaux, conservation, modification, export, suppression et effet des sauvegardes. Ne pas inventer une durée légale ni déposer de données réelles. Les choix privacy restent à valider par 15 avec une analyse adaptée au périmètre et datée.

### Interfaces

Pour chaque API, événement ou tâche : ID/version, producteur, consommateur, authentification, autorisation, schémas entrée/sortie, validation, erreurs, timeout, retry, idempotence, concurrence, limites, corrélation/audit, compatibilité et tests. Décrire l'effet d'une défaillance de la dépendance et la récupération. Ne pas déduire une stack définitive de cet inventaire.

## Acceptation et vérification

Chaque critère doit être vérifiable, par exemple « Étant donné [précondition], lorsque [action], alors [résultat observable] ». Couvrir succès, erreurs, droits insuffisants et interactions entre modules.

| Critère ID | Besoin/fonctionnalité | Scénario et résultat attendu | Test ID / type | Statut | Preuve ou blocage |
| --- | --- | --- | --- | --- | --- |
| À attribuer | ID existant | Précondition, action, résultat | ID, unitaire/intégration/API/E2E/autre | PLANNED | Propriétaire et étape suivante |

Statuts de test : `PLANNED`, `READY`, `RUNNING`, `PASS`, `FAIL`, `BLOCKED`. Pour chaque exécution, consigner date, environnement et versions, SHA, commande exacte, résultat observé et logs/rapport consultables expurgés. Un test prévu ou une simple relecture n'est jamais un `PASS` de fonctionnalité. Une revue documentaire peut être décrite comme telle, sans la transformer en test applicatif. Un correctif comprend la non-régression pertinente.

## Fiche de décision importante

ID : reprendre `DEC-XXXX` ou `ADR-XXXX` selon la gouvernance, sans collision. Statut : PROPOSÉ / APPROUVÉ / REJETÉ / REMPLACÉ avec date, autorité et référence. Ne remplir « approuvé » qu'après décision explicite.

| Champ obligatoire | Contenu |
| --- | --- |
| Objectif | Résultat recherché |
| Problème résolu | Situation et conséquences observées ou hypothèses |
| Solution retenue | Proposition candidate tant que la décision n'est pas approuvée |
| Alternatives rejetées | Options et raisons ; préciser si le rejet est seulement proposé |
| Dépendances | Équipes, contrats, données et décisions nécessaires |
| Risques | Probabilité/impact si évalués, prévention, réponse et propriétaire |
| Impact business | Valeur, coût, revenus, expérience et exploitation |
| Impact technique | Architecture, maintenance, sécurité, performances et migration |
| Priorité | P0–P3 et justification |

Ajouter les preuves utilisées, le classement de phase, les critères de réexamen et le delta à appliquer aux références. Toute décision touchant fortement architecture, stack, sécurité, permissions, données personnelles, modèle économique ou roadmap requiert le HQ et les propriétaires concernés.

## Dépendances, risques et transmission

Pour chaque dépendance : ID existant ou proposé `INT-XXXX`, émetteur, destinataire, question/action précise, référence et delta, impact bloquant ou non, statut et preuve. Pour chaque risque : `RISK-XXXX`, description, impact, propriétaire, mesure proposée et état. Ne pas annoncer qu'une autre équipe a accepté une dépendance sans réponse référencée.

Transmission : **À TRANSMETTRE → ENVOYÉ → REÇU** selon les faits. Une réponse reçue peut rester non approuvée. Ne pas envoyer de demande générale de réanalyse quand une lecture ciblée des fichiers modifiés suffit.

## Compte rendu obligatoire de fin d'étape

1. **Décisions prises et restant à valider** : IDs, statut, autorité, impacts et arbitrages demandés.
2. **Livrables produits et références GitHub** : chemins, liens de PR/commit et SHA réellement vérifiés ; sinon écrire « préparé localement — publication restante ».
3. **Tests exécutés et résultats** : commandes, environnement, SHA, résultats consultables ; distinguer prévu, réussi, échoué et bloqué. Dire explicitement si aucun test applicatif n'a été exécuté.
4. **Questions ouvertes** : réponse attendue, propriétaire et conséquence de l'absence de réponse.
5. **Dépendances avec les autres équipes** : IDs et état réel des transmissions.
6. **Risques et limites connus** : portée des conclusions, hypothèses, incohérences et mesures proposées.
7. **Prochaines étapes et informations à transmettre au HQ** : actions concrètes, responsables, conditions de démarrage et décision demandée.

Le compte rendu contient le delta utile, pas une déclaration générale d'achèvement du projet. Une absence d'accès GitHub, une publication non réalisée ou une revue manquante reste visible.
