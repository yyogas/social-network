# Sous-agent 17 — Traçabilité et publication réduite

**Avis documentaire proposé, 30 septembre 2026.** Relecture des douze annexes `01-backend.md` à `12-localization-ux.md`, de l’index documentaire, de `teams/README.md`, de la gouvernance et du statut projet. Références : HQ `4d3cd079e92217936af3292429a38f91f7b576ff` ; Backend v0.3 `0a7fcd54b996cc292bfe98c61a835613837def32`. Aucun contrat adopté, test exécuté, constat propriétaire clôturé ou changement distant effectué par cet avis.

## Corrections nécessaires avant synthèse

**Préserver les désaccords.** Les sous-agents 02/06 recommandent A ; 03/07/12 privilégient la continuité ordinaire vérifiée. Leur accord sur l’incertitude du logout ne constitue pas un consensus sur la reprise. Présenter ce choix à HQ/01/05/14, avec ses conséquences ; ne transformer aucune recommandation en comportement approuvé.

**Conditionner QA-A et L1-BE-07.** L’annexe 05 propose une levée d’ambiguïté documentaire, mais 01/10 identifient encore la continuation F avançant T : 204 annoncé contre 409 de contexte périmé. L’oracle 07-b et sa clôture restent conditionnels à la réponse 03/04/14. La correction du fence n’élimine pas cette question. Réserver D à l’incarnation d’admission et choisir une seule notation pour la déconnexion dans les textes concernés.

**Séparer les espaces d’identifiants.** « Sous-agent 01 » signifie Backend dans cette ronde ; « équipe 01 » signifie Produit. Employer partout `sous-agent NN — rôle` et `équipe NN — domaine`, sans créer de nouveaux M0-TEAM. Même collision pour sous-agent17/documentation : cette mission ne reçoit pas l’autorité de la discussion17. Aucun nouvel ID DEC/ADR/INT/TEST n’est réservé par les annexes.

**Rendre les références reproductibles.** Pour chaque source : chemin canonique, SHA, section, éventuellement PR. `backend-pr28-v03.md` cité par 09 est une copie de travail : référencer `documentation/backend/api-contract-candidates.md` au SHA Backend. Qualifier « sections de convergence C1–C9 » pour éviter les sections communes homonymes. Adapter les renvois `outputs/…` au répertoire final des annexes. Les avis propriétaires antérieurs sur v0.2 ne deviennent pas des avis sur v0.3.

Le résultat « 24 tests OK » rapporté par 11 reste sa vérification documentaire locale, avec ses limites ; ce n’est ni une exécution de cette revue, ni une CI du futur commit, ni un PASS applicatif.

## Publication minimale proposée

Modifier seulement trois entrées courantes : `documentation-index.md` pour la navigation ; `project-governance/project-status.md` pour l’état du lot ; `project-governance/coordination-board.md` pour le manifeste et les dépendances. Ajouter les vingt annexes dans un répertoire daté unique, sans dupliquer leur contenu dans les spécifications propriétaires.

Le manifeste contient numéro de mission, rôle, fichier, propriétaires concernés, source/SHA, état réellement constaté et décision attendue. L’index pointe vers ce manifeste ; le statut projet conserve **L1 BLOQUÉ POUR CODE**. Les anciennes sections sont déjà archivées : ne pas les réécrire comme état courant. La gouvernance DIR-010 et la liste canonique des équipes restent applicables ; aucun nouveau workflow n’est nécessaire.

| Dépendance préalable | Action suivante | Responsables canoniques |
| --- | --- | --- |
| Lecture des annexes et contrôle des références | Publier réception réelle, divergences et demandes ciblées | HQ/17/21 |
| Choix reprise et portée entre racines | Définir garantie utilisateur et conséquences acceptées | HQ/01/05/14/15 |
| Garantie retenue | Spécifier acquisition, F/T, admission et durabilité | 03/04/14 |
| Inventaire données et voies dédiées | Ratifier cycles, permissions, réceptionnaire et canal réel | 09/10/14/15 |
| Contrat amendé au SHA exact | Revoir seulement les constats affectés et leurs oracles | 05/14/15/18 |

## Vingt missions, vingt-et-une discussions

Les vingt missions déléguées sont des contributions temporaires de cette session. Les vingt-et-une discussions spécialisées et leurs propriétaires persistent ; leurs réponses historiques intégrées ne sont ni remplacées ni recomptées. Cette revue couvre 01–12 ; elle n’atteste pas l’achèvement des huit autres missions. Le manifeste final doit refléter leurs retours effectifs. Aucune écriture dans d’autres chats n’est effectuée ; les handoffs restent À TRANSMETTRE sans preuve d’envoi. Aucune poursuite asynchrone après réponse n’est promise.
