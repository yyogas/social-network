# Vision produit et cadre du pilote

Date : 30 septembre 2026. Version : 0.2. Statut : **POSITIONNEMENT DIR-012 CONFIRMÉ PAR LE PORTEUR ; MVP ET CONTRATS EN PROPOSITION**. Delta de positionnement intégré par 21, sans nouvelle validation spécialisée.

Propriétaire attendu : 01 Produit. Ce document prépare son travail ; il ne constitue ni sa réponse ni une approbation du périmètre, de la roadmap ou des permissions.

## 1. Ce que le porteur du projet a confirmé

- Société basée en France.
- Public : tout le monde, partout sur la planète, y compris le peuple kabyle. Le ciblage de départ d'une seule communauté est remplacé par DIR-012, instruction du porteur du 30 septembre 2026.
- Ambition : réseau social universel dès sa conception, moderne, positif, respectueux de la vie privée et économiquement viable.
- Principes : contrôle utilisateur, respect du temps, communautés fortes, rémunération des créateurs, publicité transparente et outils professionnels.
- GitHub conserve les spécifications, décisions, code et preuves. Une idée n'est pas une décision approuvée.

### Priorités marketing confirmées — DIR-012

| Périmètre | Priorités communiquées par le porteur |
| --- | --- |
| Pays | États-Unis, Canada, Inde, France, Allemagne, Royaume-Uni, Japon, Chine, Brésil, Argentine, Colombie, Mexique, Algérie, Maroc, Afrique du Sud, Espagne et Australie |
| Régions ou ensembles | Kabylie, monde arabe et Asie |
| Portée générale | Toute la planète ; aucune exclusion des pays et publics non cités |

Ces priorités orientent la préparation marketing ; elles ne fixent ni ordre de lancement, ni budget, ni pays ouverts, ni langues disponibles. Kabylie, monde arabe et Asie ne sont pas assimilés à des pays ou à des attributs individuels. Les segments de recherche sont fondés sur les usages et centres d'intérêt. [Décision et transmissions DIR-012](../project-governance/decision-register.md).

## 2. Promesse proposée à tester

« Retrouver les personnes et les communautés qui comptent, partager simplement et choisir ce que l'on voit et ce que l'on partage. »

Le pilote doit vérifier qu'un petit groupe trouve une utilité récurrente à publier, lire et échanger. Concurrencer toutes les grandes plateformes constitue une ambition de long terme ; cette ambition ne justifie pas de reproduire immédiatement tous leurs formats et outils.

## 3. Publics et besoins hypothétiques

| Public | Besoin à confirmer par entretien | Parcours proposé | Équipe responsable |
| --- | --- | --- | --- |
| Personne souhaitant suivre ses proches, des créateurs ou ses centres d'intérêt | Maintenir des liens et découvrir des échanges pertinents malgré la distance | Profil, abonnements, fil, publication | 01 + 19 |
| Animateur associatif ou communautaire | Faire vivre un espace et modérer les échanges | Communauté candidate, règles, signalement | 01 + 09 + 19 |
| Créateur | Construire une audience, comprendre sa diffusion et obtenir une rémunération claire | Publication au pilote ; outils et revenus dans des phases ultérieures | 12 + 13 |
| Lecteur occasionnel | Comprendre rapidement l'intérêt du service sans pression à rester | Fil lisible, repère de lecture, notifications maîtrisées | 02 + 01 |
| Modérateur / support | Traiter les incidents avec des permissions limitées et une trace de décision | File de signalements, décision, recours | 09 + 10 + 14 |
| Professionnel | Présenter une activité et gérer sa présence | Outils professionnels proposés hors pilote | 01 + 11 + 12 |

Ces besoins n'ont pas encore été validés par une étude utilisateur. Aucun volume d'utilisateurs ni taux de rétention n'est annoncé comme acquis.

## 4. Proposition de périmètre

Le [catalogue fonctionnel](feature-catalog.md) porte les identifiants et classifications. Les [parcours](user-journeys.md) décrivent les critères d'acceptation à reprendre par QA.

### Candidat MVP

- Comptes, sessions, récupération, profils et paramètres de confidentialité.
- Publication texte/image, abonnements, fil chronologique, réactions et commentaires.
- Contrôles de lecture et de notification pour respecter le temps utilisateur.
- Blocage, signalement, modération, notification de décision et recours.
- Demande d'accès/export et suppression de compte, avec cycle documenté.
- Surface web responsive proposée pour le pilote, accessibilité, instrumentation minimale et opérations de support.

Tout accès direct à un contenu doit appliquer les mêmes permissions que l'interface. Les médias, liens partagés et notifications font partie du périmètre de protection à spécifier.

### Arbitrages explicites

- **Communautés** : candidate MVP à arbitrer. Option A : pilote fondé sur les abonnements ; option B : communautés dès le pilote avec membres, rôles, règles et modération. La valeur communautaire attendue doit être comparée au coût de gouvernance et d'implémentation.
- **Web ou mobile d'abord** : web responsive proposé ; aucune priorité de plateforme n'est approuvée. Une application native exigerait une révision du périmètre et des dépendances.
- **Langues et pays d'ouverture** : sélectionner un périmètre testable ; le support technique des contenus multilingues doit être distingué des langues d'interface réellement traduites et modérées.
- **Âge d'accès et visibilité** : décisions à examiner avec 09, 14 et 15 avant les contrats. Aucun seuil ni défaut de visibilité ne sont fixés ici.

### Hors candidat MVP

Messagerie privée, diffusion vidéo avancée, direct, classement personnalisé du fil, publicité, paiements aux créateurs et abonnements payants. Leur classification demeure proposée et figure au catalogue ; exclusion du candidat MVP ne signifie pas abandon.

## 5. Hypothèses de valeur et mesures

Statut de toutes les mesures : **PROPOSÉ — COLLECTE NON IMPLÉMENTÉE**. Les définitions, la minimisation des événements, les durées de conservation et les conditions de collecte sont à revoir avec 13 et 15 avant instrumentation.

| Hypothèse | Mesure proposée et dénominateur | Décision qu'elle doit éclairer |
| --- | --- | --- |
| L'inscription conduit à un premier usage utile | Part des comptes de cohorte ayant accompli une action choisie : suivre, publier ou commenter ; fenêtre à fixer | Corriger l'accueil ou clarifier la promesse |
| Le réseau rend utile un retour volontaire | Part des comptes de cohorte ayant une action utile durant une fenêtre de retour définie ; exclure comptes de test selon règle documentée | Confirmer l'utilité au-delà de la première visite |
| Les publications suscitent un échange | Part des publications admissibles recevant une réponse d'un autre compte ; fenêtre et exclusions à fixer | Comprendre la densité sociale, sans encourager le spam |
| Les personnes comprennent leur audience | Réussite observée d'une tâche de réglage et de vérification de visibilité | Simplifier les contrôles avant lancement |
| La sécurité opérationnelle est soutenable | Délais médian et p95 de prise en charge, stock de dossiers, réouvertures et décisions de recours | Adapter outils, règles et moyens de modération |
| Le service respecte le temps | Réussite des tâches, contrôle perçu et satisfaction déclarée ; aucune maximisation de durée de session | Vérifier la cohérence avec la promesse |
| Le pilote reste finançable | Coût mensuel observé, coût médias, coût de support/modération et scénario de croissance | Déterminer une limite de pilote et réviser les phases |

Les objectifs chiffrés seront proposés après définition de cohorte, capacité opérationnelle et protocole de mesure. Une absence de signalement n'est pas une preuve de sécurité ; une hausse de temps passé n'est pas automatiquement une réussite.

## 6. Conditions de passage au développement

1. 01 décrit le problème pilote, le public choisi et le périmètre inclus/exclu.
2. 02 précise les parcours, erreurs, états vides et accès sur les surfaces retenues.
3. 09, 14 et 15 examinent sécurité, permissions, abus, données et opérations sensibles.
4. 03 et 04 proposent les contrats et impacts de capacité ; aucun choix de stack n'est imposé ici.
5. 18 traduit les critères en plan de validation avec preuves attendues.
6. MASTER enregistre les arbitrages, dépendances, responsables et autorisation d'implémentation dans GitHub.

## 7. Questions prioritaires à soumettre au MASTER

| Question | Responsable de proposition | Contribution requise |
| --- | --- | --- |
| Quelle utilité centrale et quel groupe pilote concret ? | 01 | 19, entretiens et protocole pilote |
| Quelles surfaces et langues dès le pilote ? | 01 | 02, 05, 06, 16, 09 |
| Communautés incluses ou différées ? | 01 | 09, 04, 19, coût et parcours comparés |
| Quelles politiques d'accès, âge, visibilité et suppression ? | 15 + 09 + 14 | 01, contrats et analyse ciblée |
| Quel budget et quelle disponibilité de modération/support ? | MASTER | 10, 14, 19 |
| Quelle stratégie économique explorer après preuve de valeur ? | MASTER | 11, 12, 13, 15 |

## Compte rendu de préparation

1. Décisions : rédaction d'un cadre proposé ; aucune validation de MVP ou stack.
2. Livrable : ce document et ses deux documents liés, à publier par la PR HQ.
3. Tests : aucun test applicatif exécuté par cette rédaction ; critères du parcours au statut PLANNED.
4. Questions : tableau ci-dessus.
5. Dépendances : contributions spécialisées identifiées, non supposées reçues.
6. Risques : surdimensionnement du pilote, ambiguïté des permissions, modération sous-financée et confusion entre audience et pays ouverts.
7. Suite / HQ : faire examiner ces propositions, enregistrer les arbitrages puis figer une première référence produit.
