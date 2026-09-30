# Social Network — Direction / HQ

**Version :** 0.8 — 30 septembre 2026
**Statut :** orientations du porteur confirmées, dont DIR-012 ; périmètre pilote et contrats spécialisés encore à arbitrer
**Propriétaire :** Direction / HQ
**Nom du projet :** Social Network

## 1. Vision et mandat

Construire, depuis une société basée en France, un réseau social universel et économiquement viable, destiné à tout le monde dès sa conception, y compris au peuple kabyle. Le produit doit donner davantage de contrôle aux personnes sur leurs données, leur temps et leur expérience, offrir des communautés solides, mieux servir les créateurs, rendre la publicité intelligible et proposer des outils professionnels utiles.

DIR-012 remplace le ciblage initial d'une seule communauté par une audience universelle et des priorités marketing géographiques explicites. Les pays effectivement disponibles, les langues prises en charge et le rythme d'ouverture restent à décider séparément ; aucun public n'est présenté comme une extension tardive de l'identité du produit.

**Règle de gouvernance :** HQ tranche les arbitrages transversaux après avis des propriétaires concernés. Une proposition d'équipe ne devient pas une décision validée sans inscription explicite dans ce registre. Les engagements juridiques, financiers, de sécurité et de calendrier exigent une validation adaptée avant exécution.

## 2. Périmètre par étape — proposition de travail

| Étape | Portée proposée | Critère de sortie |
| --- | --- | --- |
| MVP | Comptes et profils ; publications texte/photo ; fil chronologique avec contrôle simple ; abonnements ; communautés et modération de base ; signalement/blocage ; paramètres de confidentialité ; notifications essentielles ; interface mobile web ; instrumentation sobre et consentement adapté. | Une communauté pilote peut publier, découvrir, interagir et gérer les abus avec une fiabilité mesurée. |
| Phase 2 | Vidéo courte et hébergement média renforcé ; messagerie privée sous réserve de ses contrats de sécurité ; outils de créateurs et de communautés ; recherche et découverte améliorées. | Usage et coûts du MVP justifient ces investissements. |
| Phase 3 | Monétisation des créateurs, outils professionnels avancés, publicité transparente avec contrôles explicites, vidéo longue selon la demande. | Économie unitaire et exigences de confiance démontrées. |
| International | Localisation, accessibilité linguistique, déploiement et modération régionale, conformité par marché, moyens de paiement locaux lorsqu'ils deviennent nécessaires. | Ouverture marché par marché après préparation opérationnelle. |
| Long terme | Fédération ou interopérabilité éventuelle, formats et expériences supplémentaires, écosystème de développeurs, outils avancés d'aide à la création. | Décisions fondées sur des besoins et contraintes documentés. |

Ces affectations sont **des propositions**, pas des spécifications validées. Les principes de confidentialité, accessibilité et sécurité s'appliquent à toutes les étapes ; le rang « International » désigne l'expansion, pas un report de leur conception.

## 3. Structure de travail suggérée

| Domaine | Responsable de décision attendu | Livrables attendus |
| --- | --- | --- |
| Produit et recherche | Produit / UX | publics, besoins, parcours, indicateurs, MVP |
| Design et accessibilité | Design System | parcours et composants, mobile, langues, accessibilité |
| Architecture et ingénierie | Architecture / développement | limites de domaines, contrats, choix techniques, coût et livraison |
| Confiance, sécurité et modération | Trust & Safety | politiques, signalements, recours, protection contre les abus |
| Vie privée et juridique | Privacy / Legal | données, consentement, conservation, marchés, obligations applicables |
| Communautés et croissance | Community / Growth | pilotes, acquisition, animation, rétention saine |
| Créateurs et économie | Creator / Business | rémunération, publicité, outils professionnels, économie unitaire |
| Qualité et exploitation | QA / SRE | tests, disponibilité, incidents, métriques, support |

Les noms des discussions, responsables humains et mandats détaillés restent à désigner. Chaque équipe transmet à HQ ses décisions proposées, dépendances, preuves, risques et points bloquants. HQ renvoie un arbitrage daté et un statut ; aucun échange automatique entre discussions n'est présumé.

## 4. Décisions validées par le brief

| ID | Décision | Portée |
| --- | --- | --- |
| DIR-001 | Société basée en France. | Gouvernance et préparation du lancement. |
| DIR-002 | Orientation historique de première audience communautaire — **REMPLACÉE par DIR-012 le 30 septembre 2026**. | Conservée pour traçabilité ; ne détermine plus le public ni le recrutement. |
| DIR-003 | Ambition universelle, précisée par DIR-012 : public mondial dès la conception. | Préparation et disponibilité opérationnelles à décider ; marque universelle. |
| DIR-004 | Principes : expérience positive et moderne, vie privée, contrôle utilisateur, respect du temps, communautés, créateurs, publicité transparente, outils professionnels et viabilité économique. | Critères d'arbitrage produit. |
| DIR-005 | HQ maintient priorités, roadmap, arbitrages, cohérence, risques et registre des décisions. | Gouvernance de ce document. |
| DIR-012 | Réseau pour tout le monde, peuple kabyle inclus ; priorités marketing mondiales ci-dessous. | **CONFIRMÉ par instruction explicite du porteur**, 30 septembre 2026 ; remplace DIR-002. |

### DIR-012 — Positionnement universel et priorités marketing

**Autorité et preuve :** instruction directe du porteur du projet reçue le 30 septembre 2026 à 00:45 Europe/Paris dans la discussion 21 ; intégration documentaire par 21 dans la PR #27. Révision d'entrée : `f779bf728a8a77fbd1003158c78473109ce71d54`. **Statut : CONFIRMÉ pour le positionnement et les priorités marketing.** Cette trace ne vaut pas avis spécialisé des autres équipes.

- **Décision :** le réseau est destiné à tout le monde, y compris au peuple kabyle. Le ciblage initial exclusif ou privilégié d'une communauté kabyle est retiré. L'identité universelle s'applique dès la conception du produit.
- **Priorités marketing confirmées — pays :** États-Unis, Canada, Inde, France, Allemagne, Royaume-Uni, Japon, Chine, Brésil, Argentine, Colombie, Mexique, Algérie, Maroc, Afrique du Sud, Espagne et Australie.
- **Priorités marketing confirmées — régions ou ensembles :** Kabylie, monde arabe et Asie. Ces libellés sont des périmètres marketing, pas des codes de pays, une résidence ni une origine à attribuer aux personnes.
- **Portée mondiale :** toute la planète reste concernée ; les pays ou publics non cités restent inclus dans l'ambition. L'ordre de la liste ne fixe ni un classement, ni un budget, ni une vague de déploiement.
- **Effet sur les propositions antérieures :** A1 France/adultes/invitation et C1 français ne sont pas validés par ce message et perdent leur statut de recommandation par défaut ; cohorte, pays servis, langues, âge et admission sont à réexaminer dans ce cadre mondial. L'inclusion de la fonctionnalité générique de groupes/communautés FEAT-020 reste un arbitrage distinct.
- **Limites :** aucune campagne, dépense, collecte d'origine, ouverture de pays, traduction, modification d'ACL ou autorisation d'implémentation n'est déclenchée. La liste marketing du réseau ne modifie pas la phase candidate de la publicité intégrée au produit.
- **Classement :** orientation de produit et préparation marketing applicables dès M0/MVP ; fonctionnalités MVP / Phase 2 / Phase 3 / International / Long terme inchangées. « International » décrit la préparation des marchés et langues, pas une future ouverture du public à d'autres peuples.

| Transmission ciblée — toutes À TRANSMETTRE | Livrable attendu / blocage |
| --- | --- |
| 01/19 : remplacer les segments fondés sur une origine par des usages, centres d'intérêt et besoins | Fiche de cohorte candidate et plan marketing par marché ; bloque le recrutement effectif, pas cette correction de positionnement |
| 16 + 09/10/15 : rapprocher pays servis, langues d'interface/contenu/support et capacités humaines | Matrice de préparation par marché et options de langues ; bloque annonce de disponibilité et ouverture |
| 03/04/05/14/18/20 : reprendre les entrées de L1 touchées, sans inventer pays, locale ou origine depuis un segment marketing | Contrats d'admission/locale/permissions et critères de test après arbitrage ; bloque le code dépendant |
| HQ/17 : normaliser ce delta ciblé et les références A/C, OPEN-001/004, SYN-002 | Traçabilité et arbitrage DEC-0001/0002 restant ouvert ; aucune demande de réaudit des 21 contributions |

**Acceptation documentaire :** README, vision, Produit, Growth, Localisation et dossier HQ portent une audience universelle ; tous les territoires demandés sont présents ; aucune mention historique du premier ciblage n'est présentée comme active ; priorités marketing, langues et disponibilité restent distinctes. Contrôles Git/CI au SHA publié dans la PR ; aucun test applicatif ou avis pays nouvellement exécuté.

## 5. Décisions ouvertes prioritaires

Chaque fiche suit le même format. Les solutions proposées ci-dessous ne valent pas validation.

### OUV-001 — Promesse et public pilote

- **Objectif :** définir une promesse que le premier groupe d'utilisateurs peut vérifier.
- **Problème résolu :** éviter un produit trop général et un MVP dispersé.
- **Solution proposée :** tester une expérience centrée sur les communautés, les publications et le contrôle du fil auprès d'un ou deux segments d'usage définis par leurs besoins et centres d'intérêt dans le cadre universel DIR-012.
- **Alternatives rejetées :** aucune à ce stade ; les options « vidéo d'abord » et « réseau professionnel d'abord » restent à comparer.
- **Dépendances :** recherche utilisateur, recrutement de pilotes, positionnement de marque.
- **Risques :** échantillon non représentatif ; confusion entre cohorte de test et public universel du réseau.
- **Impact business :** acquisition et rétention initiales ; coût des opérations communautaires.
- **Impact technique :** priorise profils, graphe social, communautés et fil.
- **Priorité :** P0 ; **classement :** MVP ; **statut :** OUVERT.

### OUV-002 — Contrat du MVP et indicateurs de passage

- **Objectif :** figer une portée réalisable et des critères de succès.
- **Problème résolu :** accumulation de fonctions imitant plusieurs réseaux à la fois.
- **Solution proposée :** retenir le périmètre MVP du tableau, puis fixer des seuils de qualité, rétention, sécurité et coût avec les équipes.
- **Alternatives rejetées :** aucune ; un MVP vidéo ou messagerie peut être évalué avec données utilisateur.
- **Dépendances :** OUV-001, étude technique, modération, capacité de l'équipe.
- **Risques :** sous-estimation des abus, stockage média et support.
- **Impact business :** délai de lancement et capital requis.
- **Impact technique :** séquencement des services, tests et instrumentation.
- **Priorité :** P0 ; **classement :** MVP ; **statut :** OUVERT.

### OUV-003 — Règles de confidentialité et d'identité

- **Objectif :** permettre une participation sûre et maîtrisée dans plusieurs pays.
- **Problème résolu :** incertitude sur visibilité, identité publique, mineurs, données et consentement.
- **Solution proposée :** définir une matrice de visibilité, règles d'âge et d'accès, politique de conservation et parcours de suppression avant conception détaillée.
- **Alternatives rejetées :** aucune ; les degrés de pseudonymat et de visibilité demandent arbitrage.
- **Dépendances :** Privacy / Legal, sécurité, Trust & Safety, marchés pilotes.
- **Risques :** exposition des personnes, coûts de modération, obligations variables selon les marchés.
- **Impact business :** confiance et coût de conformité.
- **Impact technique :** modèle de données, permissions, journaux et suppression.
- **Priorité :** P0 ; **classement :** MVP ; **statut :** OUVERT.

### OUV-004 — Modération, recours et gouvernance communautaire

- **Objectif :** assurer la sécurité et une application prévisible des règles.
- **Problème résolu :** contenus nuisibles, harcèlement, spam et décisions opaques.
- **Solution proposée :** politiques publiées, signalement, blocage, modération humaine proportionnée et voie de recours dès le pilote.
- **Alternatives rejetées :** aucune ; le degré d'automatisation et les droits des administrateurs de communauté restent ouverts.
- **Dépendances :** juridique, produit, support, sécurité, outils internes.
- **Risques :** volume de traitement, biais, atteintes à la liberté d'expression.
- **Impact business :** confiance, coût opérationnel, rétention.
- **Impact technique :** workflows, preuves, contrôles d'accès, audit.
- **Priorité :** P0 ; **classement :** MVP ; **statut :** OUVERT.

### OUV-005 — Modèle économique et créateurs

- **Objectif :** financer durablement le service et définir une rémunération crédible.
- **Problème résolu :** promesse de meilleure rémunération sans mécanisme ni économie validés.
- **Solution proposée :** mesurer les coûts et usages au MVP ; comparer abonnements, services professionnels et publicité contrôlable avant de fixer les offres.
- **Alternatives rejetées :** aucune ; tarifs, partage de revenus et publicité ciblée ne sont pas décidés.
- **Dépendances :** finance, Creator / Business, Privacy / Legal, paiements, lutte contre la fraude.
- **Risques :** coûts média, incitations au contenu nocif, fraude et complexité fiscale.
- **Impact business :** revenus, marge et attractivité des créateurs.
- **Impact technique :** facturation, comptabilité, attribution, transparence publicitaire.
- **Priorité :** P1 pour le modèle ; **classement :** Phase 3 pour le déploiement ; **statut :** OUVERT.

### OUV-006 — Marchés, langues et ordre d'ouverture

- **Objectif :** rendre le lancement international exploitable.
- **Problème résolu :** huit pays cités ne signifient pas huit lancements opérationnels simultanés.
- **Solution proposée :** choisir un pilote restreint, puis ouvrir par vagues selon langues, support, modération et préparation juridique.
- **Alternatives rejetées :** aucune ; déploiement simultané et vagues restent à comparer.
- **Dépendances :** OUV-001, Privacy / Legal, infrastructure, support.
- **Risques :** promesse de disponibilité excessive et expérience linguistique inégale.
- **Impact business :** taille du marché accessible et coût d'expansion.
- **Impact technique :** localisation, distribution, stockage et exploitation.
- **Priorité :** P0 pour le choix du pilote ; **classement :** MVP puis International ; **statut :** OUVERT.

## 6. Risques majeurs

| ID | Risque | Niveau initial | Première réponse |
| --- | --- | --- | --- |
| R-001 | MVP trop large pour les moyens disponibles | Élevé | Contrat de portée et critères de sortie. |
| R-002 | Harcèlement, spam, manipulation ou conflits entre communautés | Élevé | Modération et recours avant ouverture. |
| R-003 | Exposition de données personnelles à travers plusieurs juridictions | Élevé | Analyse juridique et conception privacy dès l'origine. |
| R-004 | Coût du stockage et de la diffusion vidéo | Élevé | Déployer la vidéo selon validation de la demande et des coûts. |
| R-005 | Faible rétention malgré acquisition initiale | Élevé | Entretiens et pilote mesuré. |
| R-006 | Promesse de rémunération des créateurs non soutenable | Élevé | Modèle économique chiffré avant engagement public. |

## 7. Dépendances inter-équipes

| Décision ou livrable | Équipes liées | Condition avant arbitrage |
| --- | --- | --- |
| MVP et parcours | Produit, Design, Ingénierie, Trust & Safety | Segments pilotes et capacité. |
| Confidentialité et identité | Produit, Privacy / Legal, Sécurité, Données | Matrice de visibilité et marchés pilotes. |
| Fil et découverte | Produit, Données, Trust & Safety, UX | Contrôle utilisateur, risques de manipulation, mesures. |
| Vidéo et créateurs | Produit, Infrastructure, Finance, Creator / Business | Coûts et usage mesurés. |
| Ouverture pays par pays | Legal, Community, Localisation, SRE | Support, langues, modération, conformité. |

## 8. Prochaines actions

1. Désigner les discussions ou responsables de chaque domaine et leur mandat exact.
2. Lancer une courte recherche auprès des premiers publics ; formuler trois besoins principaux et une promesse testable.
3. Faire chiffrer la capacité de l'équipe, le budget et la date cible pour cadrer le MVP.
4. Produire ensemble les premières versions de la matrice de confidentialité, des règles de modération et des parcours clés.
5. Arbitrer OUV-001, OUV-002 et OUV-006 ; dater et inscrire les décisions retenues.
6. Établir ensuite un calendrier avec jalons et critères d'entrée/sortie, sans annoncer de date non étayée.

## 9. Protocole de mise à jour

Pour chaque nouvelle idée : attribuer un ID, l'affecter à MVP, Phase 2, Phase 3, International ou Long terme, nommer un responsable et noter les dépendances. Pour toute décision majeure : enregistrer objectif, problème, solution, alternatives réellement évaluées, dépendances, risques, impacts business et technique, priorité, statut, date et auteur de validation. Mettre à jour les listes validées, ouvertes, risques, dépendances et prochaines actions. Une correction conserve l'historique de la décision remplacée.

## 10. Règle commune de coordination — DIR-006

**Statut : VALIDÉ par instruction du porteur de projet le 29 septembre 2026.** Cette règle s'applique à chaque discussion spécialisée du projet. Son inscription ici ne prouve pas qu'elle a déjà été transmise dans les autres fils.

Chaque équipe fait partie d'un projet global. Elle ne décide pas seule d'un changement majeur de l'architecture globale, du modèle économique, de la sécurité, des données personnelles, des permissions, de la roadmap ou de la stack technologique. Elle formule une proposition argumentée et la transmet à HQ / Architecture pour arbitrage, avec les avis des propriétaires concernés. Elle peut poursuivre les décisions locales dans son mandat qui ne modifient pas ces domaines. Une proposition n'est pas une décision validée.

À la fin de chaque travail important, l'équipe fournit systématiquement :

1. Décisions prises — en distinguant les décisions locales des propositions à arbitrer.
2. Livrables produits — avec leurs références et versions.
3. Questions ouvertes.
4. Dépendances avec les autres équipes.
5. Risques.
6. Prochaines étapes.
7. Informations à transmettre au HQ — notamment arbitrages, conflits et changements de portée.

La priorité commune est un produit cohérent et documenté, avec traçabilité des décisions et des transferts entre équipes.

### Message canonique à diffuser

> **RÈGLE COMMUNE — COORDINATION DU PROJET SOCIAL NETWORK**
> Tu fais partie d'un projet global comportant plusieurs équipes spécialisées. Ne prends pas seul une décision qui modifie fortement l'architecture globale, le business model, la sécurité, les données personnelles, les permissions, la roadmap ou la stack technologique. Dans ce cas, prépare une proposition motivée à transmettre à **00 — DIRECTION / HQ / CHEF D'ORCHESTRE** et, pour l'architecture, à l'équipe propriétaire concernée. Distingue toujours une proposition d'une décision validée.
> À la fin de chaque travail important, fournis : **1. Décisions prises ; 2. Livrables produits ; 3. Questions ouvertes ; 4. Dépendances avec les autres équipes ; 5. Risques ; 6. Prochaines étapes ; 7. Informations à transmettre au HQ.**
> Notre priorité est de construire un produit cohérent et documenté, pas simplement d'accumuler des fonctionnalités.

## 11. Mandat MASTER reçu — DIR-007

**Source :** document transmis « 00 — MASTER / DIRECTION GÉNÉRALE / ORCHESTRATION DU PROJET », 29 septembre 2026. **Statut :** mandat de gouvernance adopté pour cette discussion. La longue liste de capacités du document est une vision de périmètre progressif ; elle ne valide ni la présence de ces fonctions dans le MVP, ni leur implémentation, ni leur ordre de livraison.

### Autorité et traçabilité

- `00 — MASTER` tient les arbitrages et l'état décisionnel central ; les équipes spécialisées conservent la conception et l'exécution dans leur domaine. `03 — Architecture technique / CTO` instruit les décisions architecturales, et MASTER arbitre leurs impacts transversaux. Les choix sensibles impliquant budget, identité, cadre juridique ou compromis stratégiques sont soumis au porteur de projet avec options et recommandation.
- Les conversations séparées ne se synchronisent pas automatiquement. Une transmission n'est marquée **ENVOYÉE** que si elle a réellement été envoyée ; une réponse n'est marquée **REÇUE** que si elle a été fournie. Statuts de preuve : **confirmé, proposé, à vérifier, non reçu, en attente**.
- Le registre HQ est le relevé des décisions de coordination. La documentation validée détaille les contrats ; le repository et les environnements montrent ce qui est implémenté et déployé. Les divergences entre ces états sont consignées et résolues, sans présenter une intention comme du code livré.
- Pour toute décision importante, utiliser `DEC-XXXX` avec état `PROPOSED`, `UNDER REVIEW`, `APPROVED`, `REJECTED`, `SUPERSEDED` ou `DEPRECATED`. Conserver les identifiants `DIR-001` à `DIR-007` comme identifiants historiques et créer une correspondance lors d'une consolidation plutôt que de les réattribuer silencieusement.
- Autres registres à ouvrir au besoin : `ADR`, `EPIC`, `FEAT`, `RISK`, `BUG`, `SEC`, `PRIV`, `DEP`, `INT`, `CR`, `TECH-DEBT`, `REL`, `INC`. Aucun ID de ces registres n'est créé pour un travail non effectué.

### Équipes reconnues dans le mandat

| Numéros | Domaines |
| --- | --- |
| 00–04 | MASTER ; Produit ; UX/UI / Design System ; Architecture technique / CTO ; Backend / API |
| 05–10 | Web ; Mobile ; IA / Recommandation / Hub ; Média ; Trust & Safety ; Admin / Support |
| 11–16 | Publicité ; Créateurs ; Data ; DevOps / SRE ; Juridique / Privacy ; International |
| 17–21 | Documentation ; QA / Release ; Growth ; Code Source / Repository ; Intégration / Code Review |

Cette liste décrit l'organisation annoncée. Elle n'établit pas que chaque équipe a déjà livré ou approuvé ses contrats.

### Registres et flux de décision

MASTER maintient : `Decision Register`, état du projet, carte des composants et de leurs propriétaires, `Dependency Register`, `Risk Register`, dette technique, demandes inter-équipes, change requests, releases et incidents. Chaque entrée doit avoir un propriétaire, un statut, des références et, si pertinent, une échéance et des critères de clôture.

Flux : **idée → analyse par propriétaire → proposition → avis des équipes touchées → arbitrage MASTER ou humain → spécification → réalisation → revue indépendante → QA / sécurité / privacy proportionnées au risque → documentation → validation de release → production → mesure**. Les décisions sont redistribuées via un `SYNC PACKET` ciblé ; les travaux importants reviennent avec un `MASTER HANDOFF`. Le niveau de formalisme dépend du risque.

### Priorisation et gates

- Les nouvelles initiatives sont classées `MVP`, `Post-MVP`, `Phase 2`, `Phase 3`, `International`, `Long terme`, `Expérimental` ou `Abandonné`, avec priorité `P0` à `P3`. Les cinq classes initiales du registre restent compatibles ; les classes supplémentaires permettent de distinguer une transition, une exploration et un abandon.
- La roadmap de travail distingue Fondation, MVP, Engagement, Monétisation, Scale et International. Elle ne fixe pas encore de dates, de budgets ou de contenu de release approuvé. La sécurité, la confidentialité, l'accessibilité et l'internationalisation sont prises en compte dès la fondation.
- `Ready` : besoin, portée, règles métier, design suffisant, contrats, permissions, dépendances, critères d'acceptation et risques principaux. `Done` : intégration, revue du code, tests, documentation et validations adaptées au risque ; une fonctionnalité écrite mais non vérifiée reste en cours.
- L'équipe 21 peut signaler un blocage d'intégration sur compatibilité, migration, permission, sécurité ou tests critiques. MASTER arbitre avec les responsables concernés et ne marque pas une release prête tant qu'un blocage critique est ouvert.

### État initial selon les éléments reçus

| Champ | État probant |
| --- | --- |
| Phase | Fondation / cadrage ; à confirmer avec les équipes |
| Produit ou repository livré | Non confirmé dans ce fil |
| Contrats architecture, API, permissions et données | Non reçus dans ce fil |
| MVP, calendrier et budget officiels | En attente d'arbitrage |
| Tests, release, production | Non confirmés dans ce fil |
| Prochaine priorité | Consolider l'état réel des équipes 01, 03, 15, 09, 18, 20 et 21, puis figer le premier jalon de Fondation |

### Modèles de sortie

Chaque travail important se clôt par les sept rubriques de `DIR-006`. Pour MASTER, ajouter un `PROJECT STATUS` concis : phase et objectif ; faits accomplis ; en cours ; blocages ; décisions et change requests en attente ; risques et dépendances critiques ; sécurité/privacy et tests à revoir ; prochaine priorité ; équipes à synchroniser. Employer **« non reçu »** et **« à vérifier »** quand les preuves manquent.

## 12. Démarrage opérationnel — DIR-008

**Date :** 29 septembre 2026. **Origine :** instruction du porteur de projet « commence le projet ». **Statut : APPROVED pour l'ouverture de la phase Fondation ; aucun périmètre fonctionnel, budget, délai ni architecture détaillée n'est approuvé par cette décision.**

### M0 — Premier jalon de Fondation

**Objectif :** obtenir un dossier de démarrage cohérent permettant de décider le MVP et de préparer son exécution. **Sortie attendue :** une fiche de public pilote et de promesse, un parcours utilisateur principal, une liste priorisée des capacités, une architecture de principe et ses frontières, un modèle initial de données et de permissions, les exigences de sécurité/modération/privacy, des critères d'acceptation et une estimation de capacité/coûts. Chaque élément a un propriétaire, un statut et une preuve. M0 se termine seulement après arbitrage explicite du MVP par MASTER et validation humaine des engagements significatifs.

**État au démarrage :** brief stratégique et mandats d'équipes reçus ; livrables spécialisés consolidés **non reçus** ; repository, implémentation, QA et déploiement **non vérifiés** dans cette discussion. Aucune date de fin de M0 n'est annoncée sans capacité et dépendances confirmées.

### Hypothèse produit à instruire — MVP-001 (PROPOSED)

Une personne rejoint le pilote, crée un profil, suit des personnes ou rejoint une communauté, publie du texte et une image, découvre un fil chronologique, réagit et commente, contrôle la visibilité de ses publications et peut bloquer ou signaler un abus. Les modérateurs disposent des actions minimales traçables pour traiter les signalements et recours. Le parcours doit fonctionner sur web responsive et être évalué pour mobile ; la décision sur une application native dès le MVP reste ouverte.

**Bornes provisoires :** vidéo, stories, live, messagerie, appels, publicité, paiements, marketplace, recommandation personnalisée avancée et Creator Studio complet sont candidats aux étapes suivantes. Ce classement est provisoire ; Produit peut proposer un autre noyau si la recherche utilisateur le justifie. Un fil chronologique reste toujours disponible selon le mandat de l'équipe IA reçu dans le projet.

**Critères à préciser avant validation :** groupe pilote et besoins, langues de lancement, règles d'identité et d'âge, visibilité, politiques de modération, ergonomie et accessibilité, qualité réseau, capacité de support, métriques de valeur et seuils de fiabilité, coûts média et exploitation.

### Vague 1 — demandes ciblées aux propriétaires

| Demande | Destinataire | Livrable exact | Dépendance / statut |
| --- | --- | --- | --- |
| INT-0001 | 01 — Produit | Deux segments pilotes possibles, problème central, promesse, parcours principal, proposition MVP et exclusions, critères d'acceptation, options et questions à HQ. | OUV-001/002 ; **À TRANSMETTRE** |
| INT-0002 | 02 — UX/UI | Parcours onboarding → communauté/personne → publication → fil → interaction → contrôle/signalement ; états d'erreur, accessibilité et langues ; points à arbitrer. | INT-0001 ; **À TRANSMETTRE** |
| INT-0003 | 03 — Architecture | Carte des domaines et frontières, contrats prioritaires, flux de données, options de déploiement simples, risques et ADR proposés ; vérifier la stack annoncée par les équipes sans la modifier seul. | INT-0001/0004/0005 ; **À TRANSMETTRE** |
| INT-0004 | 09 — Trust & Safety | Règles du pilote, signalement, blocage, modération, recours, protection des mineurs, besoins back-office et capacité humaine. | INT-0001/0005 ; **À TRANSMETTRE** |
| INT-0005 | 15 — Juridique / Privacy | Matrice initiale des données, visibilité, âge, conservation, suppression, pays pilotes, points nécessitant avocat ; ne pas tenir une hypothèse juridique pour une validation. | INT-0001/0009 ; **À TRANSMETTRE** |
| INT-0006 | 20 — Code Source | État probant du repository, conventions existantes, inventaire du code et des tests ; proposition de squelette seulement si le contrat de Fondation le requiert. | INT-0003 ; **À TRANSMETTRE** |
| INT-0007 | 21 — Intégration / Code Review | Critères minimaux de revue et d'intégration pour M0/MVP, risques de conflit entre équipes et pièces nécessaires avant première revue. | INT-0003/0006 ; **À TRANSMETTRE** |
| INT-0008 | 18 — QA | Matrice de tests du parcours pilote, permissions, abus, réseau lent, accessibilité et critères de release ; aucun test marqué PASS sans exécution. | INT-0001/0004/0005 ; **À TRANSMETTRE** |
| INT-0009 | 16 — International | Proposition de pays et langues du pilote, séparation pays légal/résidence/origine/communauté/langue, besoins de support local. | INT-0001/0005 ; **À TRANSMETTRE** |
| INT-0010 | 17 — Documentation | Index des spécifications M0, conventions de statut et liens vers preuves ; consolider les décisions approuvées, sans transformer des propositions en faits. | Tous les livrables ; **À TRANSMETTRE** |

**Note de synchronisation :** ces demandes sont rédigées ici, mais ne sont pas envoyées automatiquement aux autres discussions. MASTER les marque ENVOYÉES à mesure que les transmissions ont réellement lieu. Les équipes 04–08, 10–14 et 19 reçoivent un handoff ciblé dès que le parcours et les contrats correspondants sont assez précis ; elles peuvent signaler dès maintenant des contraintes bloquantes sans concevoir tout le périmètre long terme.

### Séquence et critères de décision

1. `01` et `16` définissent le pilote ; `09` et `15` exposent les contraintes critiques en parallèle.
2. `02` illustre le parcours ; `03` propose les frontières et contrats ; HQ compare valeur, coût, risques et capacité.
3. `20` et `21` établissent l'état technique réel et les gates ; `18` formalise les preuves nécessaires ; `17` consolide les références.
4. MASTER produit `DEC-0001` sur le public pilote et `DEC-0002` sur le MVP seulement après réception des avis. Il publie les sync packets aux équipes impactées.

### Risques et blocages de démarrage

| ID | Point | Responsable de l'instruction | Mesure |
| --- | --- | --- | --- |
| RISK-0001 | Explosion du MVP par assimilation de la vision à une liste de livraison | 00/01 | Exclusions explicites et critères de changement. |
| RISK-0002 | Absence de traitement opérationnel des abus au lancement | 09/10/15 | Parcours de signalement, recours, équipe et permissions avant ouverture. |
| RISK-0003 | Disponibilité annoncée dans plusieurs pays sans préparation locale | 15/16/19 | Pilote circonscrit, matrice par marché et support. |
| RISK-0004 | Contrats techniques non alignés entre web, mobile, backend et admin | 03/04/20/21 | Carte des domaines, contrats, intégration et revue. |

**Prochaine décision attendue :** `DEC-0001 — public et pays pilotes`, puis `DEC-0002 — contrat du MVP`. Les demandes INT-0001, INT-0004 et INT-0005 sont prioritaires pour débloquer ces décisions.

## 13. Dépôt GitHub — DIR-009

**État courant : GITHUB LINKED — dépôt privé créé, structure publiée sur `main` et vérifiée.** Les paragraphes suivants conservent le contexte préparatoire, puis la décision exécutée.

**Date :** 29 septembre 2026. **Décision :** préparer une structure de dépôt dédiée à Social Network, sous le contrôle de 20 — Code Source et 21 — Intégration, avec les documents M0 versionnés. **Statut :** structure et premier commit local créés ; connexion à un dépôt GitHub **EN ATTENTE**.

Le dépôt local `social-network-repository` contient le registre HQ, l'état du projet, la gouvernance, les index des domaines et des emplacements pour applications, services, packages, infrastructure et tests. Premier commit local : `14c215e` (`docs: establish Social Network M0 foundation`). Aucune application ni release n'y figure. Le compte GitHub accessible ne montre actuellement aucun dépôt dédié à Social Network ; le seul dépôt modifiable découvert, `yyogas/kbwds`, n'est pas utilisé.

**Décision initialement ouverte, désormais résolue :** destination GitHub et visibilité. Recommandation provisoire : un nouveau dépôt privé dédié, dont l'URL et les accès sont à confirmer avant publication. Les protections de branche, reviewers et conventions sont à instruire avec 20 et 21. Ne pas marquer `GITHUB LINKED` avant qu'un remote ait été configuré et que le commit soit visible dans le dépôt cible.


### Mise à jour GitHub — 29 septembre 2026

Le dépôt `https://github.com/yyogas/social-network` est créé et sa visibilité **privée** est vérifiée. L’utilisateur a confirmé l’installation automatique de Mend Bolt. Le connecteur dispose des droits de lecture et d’écriture. Le remote local `origin` pointe vers ce dépôt. La publication initiale utilise les API GitHub ; les deux commits locaux préparatoires restent un historique de préparation et ne sont pas présentés comme des commits distants. Les références de publication sont consultables dans l’historique GitHub.

GitHub devient la référence versionnée pour les fichiers de ce dépôt. La précédente archive et la copie autonome du registre constituent des instantanés historiques ; les prochaines évolutions de ces fichiers passent par le dépôt. Les autres livrables d’équipes devront être intégrés avec leur statut et leurs preuves. Les protections de branche et reviewers restent à définir avec les équipes 20 et 21.


## DIR-010 — Développement rigoureux et GitHub central

Date : 29 septembre 2026. Origine : exigences explicites du porteur de projet. Statut : APPROVED pour les exigences ; mise en œuvre dans une pull request à revoir. Objectif : rendre le projet maintenable et vérifiable hors des conversations. Problème : livrables dispersés, nommage ambigu et validations non traçables. Solution retenue : fichiers indispensables versionnés, noms explicites respectant les standards, revue par PR, tests prouvés, documentation installation/exploitation et chiffrage d'hébergement daté. Alternatives rejetées : décisions indispensables uniquement en chat ; publication de secrets ; déclarations de réussite sans preuve.

Dépendances : 17 Documentation, 20 Code Source, 21 Intégration, 18 QA, 14 DevOps, 03 Architecture et 15 Privacy. Risques : faux sentiment de sécurité d'un gate documentaire, divergence des liens lors des renommages, promesses de capacité non testées. Impact business : estimations distinguées des devis et budgets à arbitrer. Impact technique : arborescence explicite, CI documentaire et modèle de contribution ; aucune stack runtime nouvelle. Priorité : P0 pour la traçabilité ; P1 pour les propositions de dimensionnement.

Les réponses importantes suivent désormais sept rubriques : décisions prises/restantes ; livrables et références GitHub ; tests exécutés/résultats ; questions ouvertes ; dépendances ; risques/limites ; prochaines étapes et informations HQ. Les anciennes rubriques restent historiques. La fusion de cette proposition exige une revue ; aucune fusion n'est déclarée à sa création.


## DIR-011 — Mobilisation documentaire de toutes les équipes

Date : 29 septembre 2026. Autorité : instruction explicite du porteur de projet. Statut : APPROVED pour lancer les contributions documentaires des équipes 01–21 ; propositions détaillées soumises à revue.

- Objectif : construire des grandes lignes et fonctionnalités cohérentes, documentées et vérifiables avant réalisation.
- Problème résolu : préparation limitée à quelques équipes, risques de silos et manque de contrats communs.
- Solution retenue : un mandat par équipe, un modèle commun, un catalogue proposé, des parcours et un tableau de réception dans GitHub ; transmission réelle à suivre.
- Alternatives rejetées : attendre séquentiellement toutes les équipes avant de commencer une analyse ; assimiler un brouillon HQ à une validation spécialisée ; développer toutes les ambitions simultanément.
- Dépendances : 01–21, accès GitHub et revue de la PR nº 1 qui fournit les conventions utilisées.
- Risques : contributions contradictoires, inflation documentaire et absence de retours effectifs. Le propriétaire canonique et les revues ciblées limitent ces risques.
- Impact business : rend visibles le périmètre, les coûts à instruire et les arbitrages ; aucun budget ni modèle économique nouveau n'est adopté.
- Impact technique : documentation et coordination ; aucune stack ou permission runtime nouvellement approuvée.
- Priorité : P0 pour le cadre documentaire M0. Classification : préparation du MVP ; fonctionnalités ultérieures classées dans le catalogue.

Le [tableau de coordination](coordination-board.md) et les [mandats](../teams/work-orders.md) étendent la séquence initiale INT-0001 à INT-0010 : toutes les équipes commencent leur analyse documentaire, avec convergence progressive. Les anciennes demandes restent traçables et ne constituent pas une preuve d'envoi. Les réponses spécialisées de cette nouvelle campagne sont NON REÇUES à sa préparation.

## DIR-013 — Délégation à vingt sous-agents et coordination centralisée

Date : 30 septembre 2026. Autorité : demande explicite du porteur de lancer vingt agents pour gérer les contributions et avancer plus vite, avec ses instructions centralisées auprès du HQ. **Statut : APPROUVÉ pour l’organisation du travail.**

Le HQ répartit vingt missions bornées en vagues, avec six sous-agents actifs simultanément au maximum, confronte leurs livrables et publie les résultats revus dans GitHub. Le [dossier de ronde 01](../teams/agent-round-01/README.md) consigne les missions effectivement lancées, les pièces reçues, les contradictions corrigées et les prochaines actions. La publication passe par la branche et la PR HQ existantes, sans vingt nouvelles branches.

Ces exécutants sont nouveaux et distincts des discussions M0 01–21. Leur travail ne signe pas un avis au nom des anciens propriétaires et ne permet pas d’écrire directement dans les autres conversations. Le porteur n’a plus à transmettre manuellement les consignes de cette ronde. Les anciennes mentions À TRANSMETTRE restent historiques lorsqu’aucun envoi réel n’a eu lieu. La délégation est exécutée dans la session et ne promet pas de processus permanent après sa fin.

Cette décision organise la rédaction, la revue et la consolidation ; elle n’adopte pas les propositions de session A/B, une nouvelle stack, des permissions, des durées de conservation, un budget ou un lancement. DIR-010 conserve la revue et les preuves avant fusion ; les gates applicables au premier code restent en vigueur. Le HQ poursuit la coordination des deltas ciblés au lieu de demander vingt-et-un nouveaux relais manuels.
