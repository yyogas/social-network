# Publicité et Ads Manager — options de fondation M0

## Identification et statut

| Champ | Valeur |
| --- | --- |
| Objectif | Permettre au MASTER de décider quand et sous quelles conditions explorer des revenus publicitaires sans surveillance invasive. |
| Propriétaire | 11 — Publicité / Ads Manager ; aucun reviewer humain GitHub désigné. |
| Révision | v0.1 — 29 septembre 2026. |
| Référence GitHub | PR [#2](https://github.com/yyogas/social-network/pull/2), branche `documentation/m0-team-coordination`, commit d'entrée `dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957`. |
| Mandat / modèle | [M0-TEAM-11](../teams/work-orders.md), [modèle de livrable](../teams/deliverable-template.md), [plan documentaire](../documentation-plan.md). |
| Entrées produit | [Vision](../product/product-vision.md), [catalogue FEAT](../product/feature-catalog.md), [parcours J01–J07](../product/user-journeys.md), [roadmap proposée](../project-governance/global-roadmap.md). |
| Gouvernance | [Registre HQ](../project-governance/decision-register.md) : DIR-004, DIR-010, DIR-011, OUV-005 ; contribution à DEC-0002 encore à créer/arbitrer par HQ. |
| Statut | PROPOSÉ — revue métier/transversale attendue ; ni autorisation d'implémentation ni validation juridique. |
| Phase / priorité | Analyse M0 maintenant ; contraintes du MVP candidat ; FEAT-030 en Phase 3 / P2 proposé. L'étude du financement est P1 selon OUV-005. |
| Périmètre | Absence de publicité au pilote, expérimentation contextuelle ultérieure, produit Ads complet, coût/revenu, données, permissions et critères. |
| Hors périmètre | Code applicatif, intégration de régie, fournisseur de paiement, prix commercial adopté, contrat légal final, modèle prédictif implémenté. |
| Dépendances critiques | INT-1101 (périmètre/économie), INT-1102 (privacy), INT-1103 (safety), INT-1104 (mesure), INT-1105 (sécurité), avant lancement Ads ; aucune ne bloque la rédaction M0. |

### Faits et hypothèses

| Nature | Énoncé et preuve / limite |
| --- | --- |
| CONFIRMÉ | Mandat de l'équipe 11 et accès en lecture aux références ci-dessus ; publicité transparente et respect de la vie privée demandés par le porteur. |
| CONFIRMÉ | Le catalogue reçu classe FEAT-030 en Phase 3 / P2 **proposée**. La vision HQ exclut Ads de son candidat MVP ; ce n'est pas une décision MVP approuvée. |
| PROPOSÉ | Aucun service Ads ni collecte publicitaire dans le pilote ; première expérimentation payante contextuelle en Phase 3, soumise à un gate distinct. |
| PROPOSÉ | Pas de publicité aux mineurs ou aux utilisateurs d'âge incertain dans cette première expérimentation ; pas de ciblage ethnique, politique, de santé, ni de membres de communautés sensibles. |
| À VÉRIFIER | Budget pilote, demande des annonceurs, prix accepté, volumes adultes admissibles, capacité de revue, moyens de paiement, règles locales et bases juridiques. |
| NON REÇU | Avis spécialisés de 09/13/14/15, contrats économiques, contrat d'âge, rétention, modèle financier, preuve d'une implémentation Ads, tests applicatifs ou déploiement. |

Les propositions de protection ci-dessous sont des choix de produit soumis à 09/14/15 ; elles ne prétendent pas énoncer des obligations légales universelles. L'équipe 15 doit produire l'analyse datée des marchés réellement retenus avant ouverture.

## Besoin, fonctionnalités et parcours

### Réemploi et divergences à traiter

Les deux brouillons déjà rédigés dans la discussion 11 sont des entrées historiques : `Social_Network_Ads_Manager_Spec_v0.1.md` et `Social_Network_ADS_M0_Fondation_v0.1.md`. Ce livrable réintègre leur substance nécessaire et n'exige pas leur accès pour être compris.

- Le « MVP Ads » du premier brouillon désignait une première version du produit publicitaire. Il ne signifie pas inclusion au MVP social. Ici FEAT-030 reste Phase 3 proposée, conformément au catalogue reçu ; toute expérimentation anticipée demanderait un changement de roadmap explicite.
- Les anciens identifiants locaux ADS-01 à ADS-10 ne sont pas une deuxième numérotation FEAT. Les capacités ci-dessous sont toutes rattachées à FEAT-030 ; FEAT-028 reste une présence professionnelle distincte, propriétaire 01, en Phase 2 proposée.
- Les plafonds précédemment illustrés (2 vues par annonceur/24 h, 6 publicités par personne/24 h) ne sont pas validés. Ils deviennent des paramètres à tester avec 01/02/13/15 ; aucun compteur n'est demandé au MVP.
- Le recours possible à Redis, PostgreSQL ou un moteur séparé évoqué dans le brouillon ne fige pas la stack. 03/04 décideront du mécanisme de cohérence après arbitrage ; aucune migration ou service Ads n'est requis en M0.
- Le ciblage par « communauté » est ambigu : espace de diffusion contextuel et appartenance des membres sont distincts. Recommandation : ne jamais convertir automatiquement une appartenance communautaire, une langue ou un périmètre marketing de DIR-012 en segment ethnique.

### Options comparées

| Option | Phase proposée | Valeur / coûts | Données requises | Limites et recommandation |
| --- | --- | --- | --- | --- |
| A — Pilote sans publicité | MVP | Revenus Ads = 0 ; pas de revue, vente ou facturation Ads ; le fonctionnement social reste à financer. | Aucune donnée collectée pour Ads. Mesure du pilote FEAT-019 avec finalités propres. | Recommandée au MVP ; financement à décider par HQ. |
| B — Expérimentation contextuelle limitée, vendue directement | Phase 3, sous-lot initial de FEAT-030 | Teste demande et prix ; revue humaine et traitement administratif peuvent dominer le coût à faible volume. | Entité annonceur/payeur, création, catégorie du placement, pays/langue autorisés, agrégats de diffusion ; état minimal d'éligibilité et compteur de fréquence validé. | Recommandée comme première exploration commerciale ; aucun suivi intersites, aucune preuve de demande aujourd'hui. |
| C — Ads Manager complet en libre-service | Phase 3, après B | Plus d'autonomie ; coûts d'ingénierie, paiement, fraude, support et modération accrus. | B + membres Business, budgets, versions, transactions, ledger, préférences si autorisées. | Conditionné à la demande observée et à une économie soutenable ; pas de revenu garanti. |
| D — Régie externe | Phase 3, alternative | Peut apporter une demande ; marge, maîtrise des contenus et données dépendent du contrat. | Dépend du fournisseur ; tout SDK/partage exigerait inventaire et revue préalable. | Non recommandée au départ ; aucune régie évaluée/intégrée, alternative non rejetée officiellement. |
| Extension par marchés | International | Support, politiques, taxes, factures, monnaie et modération à préparer pays par pays. | Strict nécessaire local documenté par 15/16. | L'audience mondiale envisagée ne constitue pas une autorisation commerciale mondiale. |

Phase 2 : FEAT-028 peut préparer la présence professionnelle ; elle n'active ni rôle de payeur ni compte annonceur par défaut. Long terme : optimisation automatique, achats programmatiques et formats supplémentaires uniquement après réexamen de leur utilité et de leurs risques. Aucun ciblage invasif n'est accepté par ce classement.

### Capacités de FEAT-030

Toutes les lignes sont PROPOSÉES ; les priorités P1/P2 concernent le lot Ads, pas une nécessité de lancement du MVP social.

| Capacité | User story et résultat | Classe / priorité | Préconditions et règles |
| --- | --- | --- | --- |
| Annonceur / Business Manager | En tant que professionnel, je veux identifier mon entreprise et mon équipe afin de gérer une responsabilité publicitaire claire. | Phase 3 / P1 | Entité et payeur déclarés, vérification, habilitations examinées par 10/14/15 ; pas d'accès automatique depuis FEAT-028. |
| Campagne / groupes | En tant que gestionnaire, je veux définir période, objectif et plafond afin de maîtriser la diffusion et la dépense. | Phase 3 / P1 | Compte admissible, politique validée ; chaque groupe respecte budget campagne et solde ; dates/fuseau explicites. |
| Création / destination | En tant qu'annonceur, je veux prévisualiser une version afin de publier une annonce identifiable et accessible. | Phase 3 / P1 | Texte/image d'abord ; annonceur/payeur, CTA, description alternative, destination contrôlée ; droits sur médias attestés. |
| Ciblage contextuel | En tant qu'annonceur, je veux choisir des contextes autorisés afin de rejoindre un public pertinent sans dossier comportemental. | Phase 3 / P1 | Taxonomie non sensible, pays/langue sans localisation précise ; pas d'extension automatique d'audience. |
| Revue / recours | En tant qu'annonceur, je veux recevoir un motif et contester un refus afin de corriger ou faire réexaminer ma création. | Phase 3 / P1 | Catégories interdites, capacité humaine, séparation des rôles et preuves définies avec 09/10/15. |
| Livraison / budget | En tant qu'annonceur, je veux respecter mon plafond afin d'éviter une dépense non autorisée. | Phase 3 / P1 | Modération, visibilité, âge, préférence, fréquence et budget vérifiés avant choix ; aucun montant arbitraire débité. |
| Enchères | En tant qu'annonceur, je veux comprendre la tarification afin de comparer mon coût avec les résultats. | Phase 3 / P2 | B : CPM convenu et allocation simple proposés ; C : enchère CPM à règle publiée après expérimentation. Pas de mélange CPC/CPA sans attribution validée. |
| Transparence / contrôle | En tant qu'utilisateur, je veux identifier, masquer ou signaler une annonce afin de contrôler mon expérience. | Phase 3 / P1 | Libellé permanent, payeur, principaux critères, fréquence plafonnée ; signalement ne promet pas retrait instantané. |
| Reporting | En tant qu'annonceur, je veux des agrégats définis afin d'évaluer une campagne sans identifier les personnes exposées. | Phase 3 / P1 | Définitions, trafic invalide, latence de finalisation, fenêtres et seuils anti-réidentification approuvés. |
| Facturation | En tant que payeur habilité, je veux rapprocher débit, facture et correction afin de comprendre ma dépense. | Phase 3 / P1 | Prépayé candidat, prestataire/Finance à choisir, taxes/devise, réservations et réconciliation ; pas de double débit. |
| Vidéo et conversions externes | En tant qu'annonceur, je veux évaluer un format ou des ventes attribuées afin de tester leur valeur. | Phase 3 / P2, sous-lot ultérieur | FEAT-026 pour vidéo ; protocole distinct Privacy/Data avant mesure externe ; indisponible dans B. |
| Automatisation avancée | En tant qu'annonceur, je veux une aide explicable au pilotage afin de réduire le travail manuel. | Long terme / P3 | Volumes et qualité démontrés, contrôle humain, garde-fous de biais, alternative déterministe. |

### Parcours nominaux et erreurs

**Annonceur :** identification → vérification → compte et habilitations → brouillon campagne/groupe/création → contrôles → soumission → revue motivée → approbation et programmation → diffusion admissible → pause/fin → rapport et facture. B peut recourir à une saisie par un opérateur habilité, toujours versionnée et revue ; la vente manuelle ne dispense d'aucun contrôle.

**Utilisateur :** voit « Publicité » et provenance sans ouvrir le menu → consulte « Pourquoi cette publicité ? » (critères effectivement utilisés, contexte et principaux facteurs) → masque l'annonce ou l'annonceur, ajuste les choix autorisés ou signale → confirmation seulement après accusé de réception. En cas d'échec, message accessible et possibilité de reprendre ; masque local temporaire clairement distingué d'un choix enregistré.

**Revue :** examinateur consulte la version et sa destination → applique une politique versionnée → motive et approuve/refuse → auteur reçoit l'état → recours rattaché, examiné selon règle d'indépendance. Une modification de texte, média, destination ou ciblage rouvre la revue. Une nouvelle menace peut suspendre une version approuvée.

**Paiement :** intention de recharge → confirmation serveur vérifiée → inscription unique au ledger → réservation pour diffusion → constat d'événement facturable → capture ou libération → réconciliation → facture/correction. Une réussite affichée par le navigateur seul n'est pas une preuve de paiement. Aucun paiement réel exécuté dans ce travail.

### États et transitions proposés

| Objet | États | Déclencheur, reprise et limite |
| --- | --- | --- |
| Annonceur | Brouillon, vérification en cours, actif, refusé, suspendu, fermé | Seul le rôle habilité active ; suspension bloque campagnes ; fermeture n'efface pas automatiquement les obligations de conservation validées. |
| Création | Brouillon, soumise, en revue, approuvée, refusée, suspendue, archivée | Approbation porte sur une version ; modification crée nouvelle version ; recours ne réactive pas l'annonce automatiquement. |
| Campagne / groupe | Brouillon, programmée, active, en pause, terminée, suspendue | « Active » seulement si la création est approuvée et les autres conditions satisfaites ; pause/révocation arrête les nouvelles admissions ; événements antérieurs traités selon règle comptable. |
| Budget réservé | Réservé, capturé, libéré, expiré | Capture atomique une fois ; échéance contractuelle ; événement tardif après libération non facturé sans preuve d'une réservation valide. |
| Rapport | Vide, en préparation, provisoire, finalisé, corrigé, indisponible | Source ou fraude en retard rend le rapport provisoire ; correction conserve trace et période ; aucun zéro inventé lors d'une panne. |
| Facture / paiement | En attente, confirmé, échoué ; facture émise, corrigée par avoir ; remboursement demandé/confirmé/échoué | États distincts pour argent et pièce comptable ; double webhook idempotent ; défaillance rejouable sans réécriture du passé. |
| Interface | Vide, chargement, succès, erreur, accès refusé, suspendu | Messages compréhensibles, focus et annonces de statut ; aucune action disponible ne remplace l'autorisation serveur. |

| Motif d'erreur candidat | Réponse et récupération | Trace minimale |
| --- | --- | --- |
| `NOT_AUTHORIZED` / `ACCOUNT_SUSPENDED` | Refus sans révéler d'autre compte ; restaurer l'accès seulement via procédure habilitée. | Acteur, ressource opaque, règle, corrélation. |
| `CREATIVE_NOT_APPROVED` / `CONTEXT_UNSAFE` | Aucune diffusion ; expliquer au gestionnaire ce qui est corrigeable. | Version/politique, motif, décision. |
| `ELIGIBILITY_UNKNOWN` / `PREFERENCE_UNAVAILABLE` | Contenu organique ; ne pas déduire l'âge ni créer un profil de remplacement. | Code minimal sans données sensibles. |
| `BUDGET_UNAVAILABLE` / `INSUFFICIENT_FUNDS` | Aucune nouvelle réservation ; reprise après confirmation fiable. | Réservation et état comptable. |
| `VERSION_CONFLICT` | Demander de recharger, ne pas écraser une modification concurrente. | Versions attendue/observée. |
| `EVENT_DUPLICATE` / `EVENT_TOO_LATE` | Accusé idempotent ou rejet documenté ; pas de double facturation. | ID d'événement et résultat. |
| `REPORT_SUPPRESSED` / `REPORT_NOT_READY` | « Volume insuffisant » / « Données provisoires » ; aucune cellule permettant d'isoler un individu. | Fenêtre, règle d'agrégation. |
| `DEPENDENCY_TIMEOUT` | Diffusion organique, tâche de gestion reprenable ; pas de retry illimité. | Dépendance, corrélation, tentative. |

Cas limites : deux groupes consomment le dernier budget, droits retirés pendant édition, âge/choix modifié entre décision et rendu, média retiré du CDN, destination changeant après revue, facture en devise différente, signalement sans réseau, campagne supprimée avec facture conservée. Les délais de révocation, fréquence et validité des tickets doivent être approuvés puis testés ; leur absence bloque Ads, pas le pilote sans Ads.

Accessibilité : parcours au clavier, focus explicite après erreur, erreurs associées aux champs, pas de statut transmis uniquement par couleur, formats pays/monnaie/fuseau lisibles, libellés localisés, texte alternatif et commandes de masquage/signalement utilisables sur petits écrans. Les cibles de conformité relèvent de 02/18/16.

## Permissions, données et contrats

### Permissions candidates — revue 10/14/15 requise

| Acteur | Action / portée | Condition et refus |
| --- | --- | --- |
| Anonyme | Lire une éventuelle notice publique de transparence | Aucune gestion ni donnée annonceur privée ; pas d'annonce expérimentale si éligibilité inconnue. |
| Membre authentifié | Voir provenance, masquer, préférences propres, signaler | Pas d'accès aux budgets ni à l'équipe de l'annonceur ; contrôle de ses seules préférences. |
| Gestionnaire du Business | Inviter/révoquer dans son Business | MFA/validation renforcée proposées ; aucun rôle interne Safety accordé par invitation. |
| Campaign Manager | CRUD/soumission/pause des campagnes autorisées | Tenant et compte vérifiés à chaque opération ; pas de paiement ni d'auto-approbation. |
| Creative Editor | Créer/modifier un brouillon du compte habilité | Ne modifie pas une version déjà approuvée ni le payeur. |
| Analyste annonceur | Lire/exporter des agrégats du compte | Seuils et mêmes restrictions dans export ; jamais liste des exposés/cliqueurs. |
| Billing Manager | Moyen de paiement, factures et solde du compte | Pas de revue publicitaire ; données carte détenues par prestataire retenu, pas de secret carte dans nos logs. |
| Autre annonceur / ancien membre | Aucune action sur le compte visé | Refus serveur même avec URL/API directe ; caches et sessions ne conservent pas les droits retirés. |
| Compte bloqué/suspendu | Consultation limitée des motifs/recours selon politique | Aucune nouvelle diffusion ni écriture réservée ; blocage utilisateur doit exclure les annonces liées selon règle 09 à définir. |
| Reviewer interne | Examiner, approuver/refuser/suspendre le dossier habilité | Séparation des fonctions ; pas de modification silencieuse d'une création ni de validation de son propre compte. |
| Finance interne / support | Correction financière / consultation minimale de dossier | Permissions séparées, justification, MFA récent et double contrôle selon risque ; aucun accès général aux profils. |

### Données et cycle de vie

Stockage et durées non approuvés. Les noms suivants désignent des catégories conceptuelles, pas des tables à créer. 04/03 produisent le modèle, 13 la mesure, 15 la rétention/export/suppression, 14 les accès et la restauration.

| Catégorie / origine / finalité | Champs minimaux candidats | Visibilité et responsable | Cycle de vie proposé |
| --- | --- | --- | --- |
| Annonceur/payeur, fourni par entreprise | Référence entité, pays, nom public, contact professionnel, bénéficiaire/payeur, état de vérification | 11/Finance ; public uniquement pour identité de transparence validée ; justificatifs restreints | Modifier avec historique, réexaminer changement d'entité ; durée/export/effacement définis par 15. |
| Membres et droits, invitations | Acteur, Business, rôle, portée, validité | 10/14 ; entreprise autorisée et audit restreint | Révocation effective ; pas d'accès aux autres tenants ; audit séparé du profil supprimable. |
| Campagne/création, saisie et revue | IDs/versions, objectif, dates, contexte, budget, média, destination, décision/politique | 11/09/08 ; création publiée identifiable, brouillons privés | Nouvelle version après modification ; retrait médias/caches coordonné ; archivage et registre selon 15. |
| Éligibilité/préférences, domaine Privacy | Résultat admissible oui/non/inconnu, choix autorisés, version/expiration | 15/14 ; moteur reçoit minimum nécessaire, annonceur aucun détail | Pas de date de naissance ni pièce d'identité dans Ads ; retrait invalide usage/cache selon contrat ; pas de collecte au MVP pour Ads. |
| Fréquence/diffusion, événement technique | Jeton interne limité si autorisé, campagne, horodatage, compteur, contexte non sensible | 13/14/15 ; jamais export individuel annonceur | Fenêtre et durée courtes à déterminer ; clés non réutilisées intersites ; absence de compteur fiable = pas d'annonce. |
| Événements et rapports | ID unique, ticket/version, impression/clic valide, période, coût ; agrégats | 13/11 ; annonceur agrégats uniquement | Déduplication, correction fraude, suppression des petites cellules et protection contre différenciation par filtres/export ; durées brutes et agrégées distinctes. |
| Fraude et recours | Motif, preuve limitée, score/évaluation, acteur, horodatage | 09/14 ; accès restreint, pas de ciblage secondaire | Droit de correction/contestation selon politique ; rétention limitée par finalité ; IP éventuelle réservée sécurité, jamais fingerprinting publicitaire. |
| Transactions/factures | Réf PSP, devise, unité monétaire, réservation, débit/avoir, statut et payeur | Finance/04 ; compte habilité | Écritures correctrices, pas d'effacement arbitraire ; durées/obligations locales à définir, même après fermeture du compte. |

Aucune réutilisation automatique des messages, du graphe social, des lectures, des intérêts du moteur de recommandation ou des communautés pour Ads. Les intérêts déclarés eux-mêmes restent hors expérimentation B tant que 15/01 n'ont pas accepté une finalité et des choix distincts. La taxonomie contextuelle exclut les catégories/proxys sensibles ; un contexte public n'autorise pas à révéler un profil privé.

Sauvegardes : suppression et retrait doivent survivre à une restauration via le mécanisme défini par 14/15 ; les annonces retirées ne redémarrent pas automatiquement. Aucun délai légal ni méthode technique de purge n'est inventé ici. Les données réelles restent absentes de ce dépôt.

### Interfaces candidates (contrats exécutables NON REÇUS)

Ces libellés locaux sont des repères de FEAT-030, pas de nouveaux endpoints approuvés. Version de description v0.1, compatibilité future à négocier avec 03/04 ; seuils, timeout chiffré, retry maximal, conservation de clé et quotas **À VÉRIFIER avant implémentation**.

| Interface / producteur → consommateur | Entrée → sortie / validation | Contrôles et défaillance |
| --- | --- | --- |
| Gestion campagne v0.1 / 04 → 05/10 | Compte, version, dates, budget, contexte/création → état, nouvelle version, motifs | Session authentifiée et portée tenant ; idempotence création, concurrence optimiste ; `VERSION_CONFLICT`/`NOT_AUTHORIZED`. Retry borné même clé uniquement ; audit acteur/référence. |
| Revue v0.1 / 09/10 → 04/11 | Version immuable, politique, motif → décision versionnée | Identité interne et rôle ; pas d'auto-approbation ; action unique par clé, comparaison de version ; indisponibilité maintient hors diffusion. |
| Éligibilité v0.1 / 15 via 04 → diffusion | Contexte courant et référence interne minimale → admissible/non/inconnu, version/expiration | Authentification de service à définir par 14 ; aucun identifiant annonceur côté profil ; défaut fermé, pas de retry synchrone sans borne. |
| Sélection/réservation v0.1 / domaine Ads/04 → client autorisé | Placement, contexte autorisé, éligibilité actuelle → aucune annonce ou ticket opaque, création/version, notice | Budget campagne/groupe/compte atomique ; clé par opportunité ; ticket authentifié, expirant et non rejouable hors portée ; échec = organique, jamais débit sur simple sélection. |
| Événement v0.1 / client validé par 04 → 13/Finance | ID événement, ticket, type, timestamp → reçu/rejeté/dupliqué | Ticket lié à version/placement, données client non considérées vraies sans validation ; rafales limitées ; capture une seule fois ; désordre et retard contractuels. |
| Paiement/réconciliation v0.1 / PSP futur via 04 → Finance/Ads | ID PSP, montant, devise, état vérifié → écriture/état | Signature/authentification serveur, replay contrôlé, comparaison montant attendu ; aucun secret carte ; retry borné, file d'échecs et reprise humaine autorisée. |
| Rapport v0.1 / 13 → Ads Manager | Compte, période, filtres autorisés → agrégats, devise/fuseau, état, date de finalisation | Tenant, quotas d'export, suppression de cellules et requêtes permettant différence ; retry lecture, pas de zéro substitué à une panne. |
| Retrait/masquage v0.1 / utilisateur ou 09 via 04 → diffusion/08/13 | Acteur, portée, version/reason → accusé et état appliqué | Droits propres ou internes distincts ; idempotence, invalidation propagée et audit ; nouvelles admissions interdites dès retrait connu ; rendu ancien géré selon délai validé. |

Pour chaque interface, corrélation pseudonyme limitée, ID de campagne/version et journal minimal ; aucun token complet ni contenu privé dans logs. La proposition exige authentification et autorisation côté service pour tous les appels internes comme externes. Une panne d'audit financier ou de compteur critique doit arrêter les nouvelles admissions ; une panne de reporting garde les opérations dans un état exact. Évolution compatible par version explicite ; retrait d'un champ après accord des consommateurs et délai à définir, jamais silencieusement.

### Livraison et protection

Ordre proposé : éligibilité et sécurité → admissibilité du contexte/placement → annonceur/création actifs → dates/choix/blocage/fréquence → allocation ou classement → réservation de budget → rendu → événement vérifié → capture/réconciliation. Une offre financière élevée ne contourne pas un veto Safety. Si aucune annonce n'est admissible, le fil organique fonctionne normalement.

Facturation B proposée : CPM sur impressions visibles valides ; définition de visibilité par format à approuver avec 13/18 avant vente, distincte des réponses « servies ». Les clics restent une mesure et non une autre facture. Pas de promesse de dépense intégrale ni de résultat. Écriture en unités monétaires définies avec Finance (précision et arrondis explicites) ; somme des réservations et débits bornée par plafond et solde, même en concurrence.

Brand safety : contrôles sur création et contexte à chaque admission, recontrôle de la destination contre redirections/cloaking, retrait rapide des versions signalées selon politique ; pas de publicité dans messages privés, recours ou paramètres sensibles. Politique candidate : exclure escroqueries, malware, offres illégales/trompeuses, publicité politique et catégories réglementées non revues. 09/15 spécifieront le catalogue et les exceptions pays ; aucune permission d'achat ne vaut approbation de contenu.

Fraude : déduplication, cohérence entre ticket/rendu/clic, vitesses anormales, sources suspectes, quarantaine avant finalisation, procédure d'appel contre faux positifs, correction par crédit traçable. Pas de fingerprinting pour compenser l'absence de suivi. Les protections ne doivent pas produire un export de personnes pour l'annonceur.

## Économie et métriques — hypothèses, pas prévisions

Revenu hypothétique mensuel = adultes actifs admissibles × jours actifs/mois × opportunités/jour × taux de remplissage × part valide × CPM / 1 000. Les opportunités sont un plafond d'inventaire utilisé pour le calcul, pas un objectif d'exposition. L'inventaire adulte admissible peut être nul ; les personnes d'âge inconnu ne sont pas assimilées à des adultes.

Les valeurs suivantes sont **fictives pour comparer la sensibilité**, sans donnée de marché, devis, mesure d'audience ou revenu observé. La part valide exclut le trafic invalidé avant facturation. Aucun volume d'utilisateurs n'est acquis.

| Scénario | Adultes admissibles | Jours × opportunités | Remplissage / part valide | Impressions valides | CPM hypothétique | Revenu brut hypothétique |
| --- | ---: | --- | --- | ---: | ---: | ---: |
| Faible | 10 000 | 10 × 2 | 40 % / 95 % | 76 000 | 4 EUR | 304 EUR/mois |
| Intermédiaire | 50 000 | 10 × 2 | 60 % / 95 % | 570 000 | 6 EUR | 3 420 EUR/mois |
| Élevé | 200 000 | 12 × 2 | 70 % / 95 % | 3 192 000 | 8 EUR | 25 536 EUR/mois |

Coûts Ads à chiffrer séparément : commercialisation, revue/modération et appels, support, fraude/remboursements, frais de paiement, diffusion/mesure, ingénierie et sécurité/privacy. À titre d'illustration uniquement, des enveloppes mensuelles Ads de 1 600 / 4 500 / 14 000 EUR produiraient des contributions de **−1 296 / −1 080 / +11 536 EUR** respectivement, avant coûts sociaux communs, amortissement de développement, fiscalité et éventuel partage créateurs. Ces enveloppes ne sont ni un budget ni des devis ; la contribution positive ne prouve pas la rentabilité globale.

Critère de réexamen proposé : demande annonceur réelle, coût opérationnel observé, protection utilisateur et contribution soutenable. À faible volume, une expérimentation peut être assumée comme coût d'apprentissage seulement après budget explicite. Aucun seuil d'utilisateurs déclenchant automatiquement Ads.

| KPI | Définition candidate / disponibilité |
| --- | --- |
| Impressions | Impressions visibles valides selon règle approuvée, dédupliquées ; servies et visibles rapportées séparément. |
| Clics | Clics volontaires valides ; type de clic précisé ; pas de faux clic après chargement. |
| CTR | Clics valides / impressions valides × 100 ; convention de clic et fenêtre stable. |
| CPM / CPC effectifs | Dépense média hors taxes / impressions valides × 1 000 ; dépense / clics valides. Le CPC n'est pas un mode de facturation de B. |
| Conversions / CPA | Événement et attribution explicitement définis ; dépense / conversions attribuées. « Non mesuré » tant que contrat non validé ; B ne collecte pas de conversion externe. |
| ROAS | Revenu attribué net des corrections définies / dépense média ; indisponible si attribution/revenus absents. Ne jamais remplacer une vente par un clic. |
| Qualité économique | Revenu net de crédits/remboursements, coûts directs, contribution, coût du support et délai de paiement. |
| Qualité utilisateur | Masquages/signalements pour 1 000 impressions, répétition, compréhension du libellé, satisfaction et rétention ; pas de maximisation du temps passé. |

Dénominateur nul → « non calculable » ; données absentes → « non mesuré » ; données retardées → « provisoire ». Attribution n'est pas causalité/incrémentalité. Pas de ROAS comparé entre fenêtres incompatibles, pas de mélange de devises ni de taxes, pas de prix recommandé présenté comme tarif officiel.

## Acceptation et vérification

Les IDs AC-ADS ci-dessous sont des critères locaux de FEAT-030, sans nouvelle fonctionnalité FEAT. QA attribuera les IDs TEST. Tous les scénarios applicatifs sont **PLANNED**, aucun n'est exécuté ; absence de contrat/implémentation est le blocage d'exécution, pas une raison de simuler un PASS.

| Critère ID | Besoin / scénario observable | Test prévu / propriétaire | Statut et précondition |
| --- | --- | --- | --- |
| AC-ADS-01 | Étant donné le pilote sans Ads, lorsque le fil FEAT-008 est chargé sans aucun service Ads, alors publication, pagination et lecture restent utilisables sans événement publicitaire. | E2E + inspection réseau / 18, 05, 04 | PLANNED ; DEC-0002 et implémentation requis. |
| AC-ADS-02 | Étant donné une création approuvée, lorsqu'elle est rendue, alors libellé, payeur et critères effectivement utilisés sont consultables au clavier et lecteur d'écran. | E2E/accessibilité / 02, 18 | PLANNED ; UX et transparence validées. |
| AC-ADS-03 | Étant donné mineur, âge inconnu ou service d'éligibilité indisponible, lorsqu'une opportunité survient, alors aucune publicité expérimentale ni collecte Ads associée n'a lieu. | API/E2E/privacy / 15, 18 | PLANNED ; politique et contrat d'âge. |
| AC-ADS-04 | Étant donné un masquage confirmé ou un blocage applicable, lorsqu'une nouvelle sélection est demandée, alors l'annonce/annonceur est exclu ; erreur de sauvegarde n'affiche pas « enregistré ». | Intégration/E2E / 09, 18 | PLANNED ; portée et propagation définies. |
| AC-ADS-05 | Étant donné un contexte sensible/privé ou création refusée, lorsque son offre est la plus élevée, alors aucune diffusion n'est admise. | API/sécurité / 09, 14, 18 | PLANNED ; taxonomie et droits. |
| AC-ADS-06 | Étant donné un plafond commun presque épuisé, lorsque deux groupes réservent simultanément, alors réservations + débits ne dépassent pas le plafond ni le solde. | Concurrence / 04, 18 | PLANNED ; mécanisme atomique et arrondis. |
| AC-ADS-07 | Étant donné un événement déjà traité, lorsqu'il est rejoué ou reçu dans le désordre, alors compteur et facture restent cohérents sans double débit ; ticket expiré suit le refus défini. | Intégration / 04, 13, 18 | PLANNED ; idempotence et lateness. |
| AC-ADS-08 | Étant donné une annonce modifiée/suspendue après approbation, lorsqu'une admission utilise une version périmée, alors elle est refusée et la nouvelle version exige revue. | API/intégration / 09, 18 | PLANNED ; invalidation/expiration. |
| AC-ADS-09 | Étant donné un autre tenant ou un rôle révoqué, lorsqu'un rapport, une facture ou une campagne est appelé directement, alors l'accès est refusé sans contenu privé. | API/permissions / 14, 18 | PLANNED ; matrice d'accès. |
| AC-ADS-10 | Étant donné un trafic invalidé, lorsque rapport/facture sont finalisés ou corrigés, alors exclusion/crédit est traçable et le montant n'est pas compté deux fois. | Intégration Finance / 13, 18 | PLANNED ; fraude et corrections. |
| AC-ADS-11 | Étant donné une petite cellule ou des filtres par différence, lorsqu'un rapport/export est demandé, alors aucune audience individuelle ne peut être extraite selon règles approuvées. | Privacy/API / 13, 15, 18 | PLANNED ; seuils/protection cumulée. |
| AC-ADS-12 | Étant donné une panne budget/fréquence ou audit financier, lorsqu'une opportunité arrive, alors le fil continue organiquement et aucun budget n'est débité. | Résilience / 14, 18 | PLANNED ; contrats de panne. |
| AC-ADS-13 | Étant donné un paiement navigateur réussi mais non confirmé serveur, lorsque le solde est consulté, alors il n'est pas crédité ; double confirmation serveur n'inscrit qu'une recharge. | Intégration / 04, Finance, 18 | PLANNED ; PSP et ledger. |
| AC-ADS-14 | Étant donné un compte fermé et une sauvegarde restaurée, lorsque le système reprend, alors préférences/retraits restent appliqués et aucune campagne arrêtée ne redémarre automatiquement. | Restauration/privacy / 14, 15, 18 | PLANNED ; rétention/restauration. |
| AC-ADS-15 | Étant donné un refus contesté, lorsque le recours est examiné, alors demandeur, décision et motif restent liés ; aucun reviewer ne s'auto-approuve un compte. | E2E/permissions / 09, 10, 18 | PLANNED ; indépendance et recours. |

Les contrôles documentaires effectivement exécutés sont décrits dans le [rapport de validation Ads](../quality/advertising-validation.md). Ils ne prouvent aucun comportement de cette matrice.

## Fiche de décision importante — contribution à OUV-005 / futur DEC-0002

Aucun nouvel ID DEC n'est réservé par cette équipe ; HQ rattache cette proposition à ses décisions existantes ou attribue l'ID final. Statut : **PROPOSÉ**, autorité attendue HQ avec 01/03/09/13/14/15 et responsable Finance à désigner.

| Champ | Proposition |
| --- | --- |
| Objectif | Tester la valeur sociale du pilote, puis financer une publicité compatible avec contrôle utilisateur et vie privée. |
| Problème | Revenus et demande non mesurés ; construire le produit publicitaire complet peut retarder le pilote et générer des coûts sans revenu suffisant. |
| Solution candidate | Option A au MVP ; étude B en Phase 3 après gate, puis C si demande et capacité prouvées. |
| Alternatives et motifs | Ads dès MVP : revenu potentiel plus tôt mais coûts/risques non couverts. Régie externe : demande potentielle contre dépendance et partage de données. Abonnements/services : à comparer avec 12/01, aucune alternative officiellement rejetée. |
| Dépendances | Questions INT-1101 à INT-1108 ci-dessous ; contrats d'âge, contexte, reporting, paiement, permissions et modération avant Ads. |
| Risques | Recettes nulles au pilote, faible volume, coût humain, fraude, proxies sensibles ; financement explicite, garde-fous et seuils expérimentaux. |
| Impact business | Report de recettes Ads ; réduction de complexité pilote ; mesurer disposition à payer et coût d'acquisition annonceur avant libre-service. |
| Impact technique | Aucun SDK, service, table ou compteur Ads au MVP ; autonomie du fil ; interfaces ultérieures versionnées sans imposer maintenant une abstraction spéculative. |
| Priorité / phase | P1 pour l'étude économique M0 ; FEAT-030 Phase 3 / P2 proposé. |
| Réexamen / acceptation | Budget pilote acté ; intérêt annonceur documenté ; collecte/droits/modération revus ; coûts estimés puis mesurés ; tests Ads exécutés avant ouverture. |
| Delta HQ demandé | Confirmer ou amender exclusion Ads dans DEC-0002, rattacher ce document à OUV-005 et réception M0-TEAM-11 ; aucune modification autonome du registre par 11. |

## Dépendances, risques et transmission

Les IDs INT-1101–INT-1108 et RISK-1101–RISK-1105 sont **proposés**, absents des références d'entrée examinées ; 00/17 doivent vérifier les collisions avec les autres contributions avant intégration. Émetteur : 11. Toutes les demandes restent **À TRANSMETTRE** aux discussions ; publier la PR ne prouve pas leur réception.

| Demande | Destinataire | Question ciblée / livrable attendu | Effet bloquant |
| --- | --- | --- | --- |
| INT-1101 | 00/01, Finance à désigner | DEC-0002 exclut-il Ads ? Quel financement sans recettes Ads ? Revoir options et hypothèses économiques uniquement. | Arbitrage du périmètre et financement pilote ; non bloquant rédaction. |
| INT-1102 | 15 avec 16/09 | Pour B : admissibilité, pays/langue/contexte, mineurs/âge inconnu, cookies/compteurs, rétention/export/registre et taxonomie sensible ; fournir analyse datée et conditions. | Toute collecte/diffusion Ads. |
| INT-1103 | 09/10 | Catalogue interdit, examen de destination, recours, rôles et capacité humaine ; livrer workflow et matrice de pouvoirs ciblés Ads. | Ouverture B/C, pas pilote sans Ads. |
| INT-1104 | 13 avec 15/18 | Définir impression visible, clic valide, agrégats/seuils et fenêtres, anti-différenciation ; distinguer FEAT-019 et Ads. | Facturation/mesure Ads, pas mesure sociale indépendante. |
| INT-1105 | 14 avec 04/03 | Menaces fraude/tenant/PSP, contrôle des tickets, budget concurrent et arrêt sûr ; fournir avis et invariants avant choix d'implémentation. | Production Ads payante. |
| INT-1106 | 03/04 avec 05/06/08 | Confirmer autonomie du fil ; proposer contrats futurs sur versions, révocation, éligibilité, budget et média sans code Ads M0. | Contrats du futur lot Ads ; aucune infrastructure Ads préalable au MVP. |
| INT-1107 | 12/01 et Finance à désigner | Comparer publicité, abonnements et services ; préciser frontière FEAT-028/030/031 et éventuel partage créateurs sans inventer taux. | Modèle économique Ads, pas publication sociale. |
| INT-1108 | 02/16/18, consolidation 17 | Revoir libellés, provenance, contrôle utilisateur, critères AC-ADS et index ; proposer tests/langues avant expérimentation. | Expérience Ads et ouverture pays ; indexation indépendante possible maintenant. |

| Risque | Impact / propriétaire | Mesure proposée / état |
| --- | --- | --- |
| RISK-1101 | Glissement d'Ads au pilote, retard et financement incohérent — 00/01/11 ; lien RISK-0001 | Phase explicite et décision de périmètre ; OUVERT. |
| RISK-1102 | Ciblage communautaire/langue utilisé comme proxy sensible, exposition de personnes — 15/09/11 | Pas de segment membre/origine ; contexte non sensible et revue des combinaisons ; OUVERT, critique avant ciblage. |
| RISK-1103 | Surfacturation, faux trafic, chargebacks — 14/04/Finance/11 | Budget atomique, événements vérifiés, réconciliation, correction et plafonds ; OUVERT, critique avant vente. |
| RISK-1104 | Collecte préventive ou réidentification par exports — 13/15/11 | Aucune collecte Ads au MVP ; finalités distinctes, agrégation et protection contre requêtes combinées ; OUVERT. |
| RISK-1105 | Recettes surévaluées et sous-capacité de revue — 00/09/10/11 | Ne pas budgéter les simulations comme revenus ; mesurer demande/coûts et capacité avant B ; OUVERT. |

### Handoff HQ — à transmettre

Objet : réponse spécialisée M0-TEAM-11, FEAT-030 et OUV-005. Delta : revue indépendante du cadrage publicitaire HQ, comparaison A/B/C/D, réconciliation des brouillons Ads avec Phase 3, scénarios économiques fictifs et contrats/risques à instruire. Pièces : ce document et son rapport de validation, PR/commit de publication à citer dans la transmission. Arbitrages : Ads hors MVP, financement pilote, gate Phase 3, propriétaire Finance, examen Privacy/Safety du ciblage contextuel. Aucun tarif, périmètre pays, permission ou architecture nouvelle approuvé.

## Compte rendu de fin d'étape

1. **Décisions prises/à valider :** consolidation documentaire locale, réemploi de FEAT-030 ; recommandation option A puis B/C et contraintes restent PROPOSÉES. Aucun DEC/ADR approuvé.
2. **Livrables et références :** ce fichier propriétaire v0.1, README du domaine et rapport documentaire ; base PR #2 / `dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957`. La PR de contribution fournit le SHA effectif de publication, distinct du snapshot local de validation.
3. **Tests réels :** voir rapport versionné ; aucun test applicatif Ads exécuté ; AC-ADS-01 à AC-ADS-15 PLANNED.
4. **Questions ouvertes :** financement/périmètre 00/01 ; protection et pays 15/16 ; capacité/recours 09/10 ; métriques 13 ; sécurité/contrats 14/03/04 ; partage éventuel 12.
5. **Dépendances :** INT-1101–1108 proposées, À TRANSMETTRE ; aucun avis d'équipe présumé reçu.
6. **Risques/limites :** hypothèses économiques illustratives, contrat non exécutable, revue juridique non réalisée ici, fonctionnement non implémenté ; risques identifiés ci-dessus.
7. **Suite/HQ :** revue ciblée par propriétaires, arbitrage MASTER, intégration par 17/21 après contrôles ; aucune fusion automatique. La publication du document n'autorise pas Ads dans le pilote.
