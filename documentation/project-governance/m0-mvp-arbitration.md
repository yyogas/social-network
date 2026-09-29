# Dossier d'arbitrage du pilote et du MVP — M0

## 1. Identification et statut

| Champ | Valeur |
| --- | --- |
| Référence / version | SN-INT-M0-ARB-001 — v0.1 |
| Date | 30 septembre 2026, Europe/Paris |
| Auteur | 21 — Intégration / Code Review ; préparation du dossier, sans substitution aux propriétaires |
| Autorité attendue | 00 — MASTER / HQ avec 01 Produit, 09 Safety, 15 Privacy et les propriétaires des arbitrages concernés |
| Demande | Poursuivre après consolidation des 21 contributions ; rendre les décisions suivantes concrètes et traçables |
| Base examinée | `main` au SHA `ba26729aa10dc497338a960ae78ba904a72216b2`, arbre `1da7b576c427cff1a45924f446cb4f94404ae58b` |
| Statut | **PROPOSÉ — À ARBITRER** ; aucune décision structurante approuvée par ce document |
| Priorité / classe | Préparation MVP, P0 ; phases futures conservées dans le tableau de périmètre |
| Portée | Options de pilote, contrat de portée candidat, dépendances et ordre de réalisation conditionnel |
| Limites | Pas de nouvelle validation juridique, choix de stack/fournisseur, permission définitive, coût ou calendrier engagé |

Les repères de ce dossier sont locaux. **DEC-0001 et DEC-0002 restent des décisions attendues**, à rédiger et inscrire par HQ après arbitrage explicite. Les dossiers SYN-001..007, FEAT et critères existants sont réutilisés. La publication ou la fusion de cette proposition ne constitue pas leur approbation.

### Éléments probants et inconnues

| Nature | Élément | Portée de la preuve |
| --- | --- | --- |
| CONFIRMÉ | 21 contributions spécialisées et bilan HQ intégrés ; 26 PR fusionnées, aucune ouverte à la lecture de départ ; 27 branches conservées | [Clôture #24](https://github.com/yyogas/social-network/pull/24), au SHA de base ci-dessus ; une nouvelle PR documentaire fera évoluer le nombre de PR ouvertes |
| CONFIRMÉ | 84 fichiers dans la base ; dernier push avec 24 tests du dépôt réussis | [Run 36637992529](https://github.com/yyogas/social-network/actions/runs/36637992529), job 109643243563 ; preuve documentaire, aucune preuve applicative |
| CONFIRMÉ | FIND-21-01/03/04 corrigés et vérifiés ; FIND-21-02/05 ouverts ; main non protégée lors de la lecture | [Revue du correctif](../quality/foundation-fix-review.md), [bilan](m0-reception-report.md) ; aucun paramètre GitHub modifié ici |
| PROPOSÉ | Pilote restreint autour du suivi de personnes, interface web responsive, noyau texte/image et protection des utilisateurs | Synthèse des options Produit, Growth, Architecture, International et Privacy ; recommandations ci-dessous |
| À VÉRIFIER | Besoin réel sans groupes, compréhension linguistique, admissibilité, moyens humains, coûts, contrats et capacité | Avis ciblés et preuves attendus des propriétaires ; réception de leurs documents ne vaut pas réception de ces validations |
| NON REÇU | Cohorte concrète, disponibilité des opérateurs, budget/plafond, décisions de scope, ADR adoptée, matrice de permissions approuvée, durées par finalité, application et preuves de lancement | Ces manques bloquent uniquement les décisions/lots qui en dépendent ; aucun participant ou responsable humain n'est inventé |

### Sources réutilisées

Lecture ciblée des sections de recommandations et interfaces, sans nouvel audit exhaustif des 21 contributions : [spécification Produit](../product/mvp-specification.md), [options Growth](../growth/pilot-launch-plan.md), [Privacy](../privacy/privacy-requirements.md), [langues et marchés](../international/localization-requirements.md), [Architecture](../architecture/architecture-proposal.md), [mesure](../analytics/measurement-plan.md), [recommandation](../artificial-intelligence/recommendation-options.md), [QA](../quality/acceptance-test-matrix.md) et [conflits SYN-001..007](m0-reception-report.md). Les règles détaillées restent dans ces sources propriétaires.

## 2. Trois arbitrages prioritaires

### A — Public et accès au pilote : préparation de DEC-0001 / SYN-002

**Recommandation PROPOSÉE :** préparer un pilote sur invitation, destiné aux adultes en France, auprès du segment de personnes suivant des proches ou créateurs décrit par Produit. Le ciblage communautaire n'introduit aucun champ obligatoire d'origine ni une déduction d'origine à partir de la langue. Un lien d'invitation ne prouve ni âge, ni résidence, ni droit de lire un contenu.

| Option | Bénéfice attendu | Coût / risque / condition |
| --- | --- | --- |
| A1 — Pilote France adultes, sur invitation — recommandé pour examen | Périmètre opérationnel et recrutement bornés ; reprend la proposition Privacy et l'option d'accès fermé de Growth | Cohorte non représentative ; admission/âge, personnes hors cible et cas transfrontières à instruire avec 15/14 ; seuil, méthode et données d'admissibilité à contractualiser |
| A2 — Pilote dans plusieurs pays | Observe plus directement la diversité de la diaspora | Requiert pour chaque pays les avis, textes, support et modération adaptés ; charge et délais non chiffrés |
| A3 — Ouverture publique dès le départ | Accès plus large et moins de traitement des invitations | Capacité d'anti-abus, support, coûts et procédure d'arrêt à démontrer ; pas de plafond ou de budget reçu |

**Autorité / entrée indispensable :** HQ avec 01/15/16/19, avis 09/10/14. Attendu : fiche cohorte sans données personnelles dans Git, pays effectivement servis, critère d'âge du pilote, admission, traitement de l'âge inconnu et des exclusions contestées. La proposition « adultes » n'est ni une analyse du droit applicable ni une preuve d'exclusion technique des mineurs.

**Impact et réexamen :** l'option retenue détermine notices, inscription, assistance et coûts humains. La décision peut autoriser la préparation des contrats ; l'ouverture exige ensuite les preuves du §6. Aucun participant ne sera contacté par ce dossier.

### B — Suivi de personnes ou communautés : préparation de DEC-0002 / SYN-001

**Recommandation PROPOSÉE :** retenir le suivi de personnes pour la première boucle d'usage et reporter FEAT-020 en **Phase 2 candidate**. Cette recommandation reprend Produit et Growth ; le catalogue conserve actuellement FEAT-020 « MVP conditionnel ». Aucune modification silencieuse du catalogue n'est effectuée.

| Option | Produit et valeur | Coût / risque / condition |
| --- | --- | --- |
| B1 — Personnes suivies, sans groupes structurés — recommandé | Compte/profil → suivre → publier/lire → réagir/commenter → revenir à une réponse utile | Pas d'espace collectif privé ni de gestion des membres ; accueil éditorial/manual à préparer ; ne pas promettre une communauté fermée par le suivi |
| B2 — Communautés dès le pilote | Adhésion et espace collectif utiles aux associations | Ajoute J07, rôles locaux, dernier responsable, départ/exclusion/fermeture et articulation de modération ; exige contrats et critères dédiés |

**Condition décisive :** si 01/19 établissent que l'espace collectif fermé est le besoin indispensable de la cohorte, B1 ne répond pas à ce besoin. HQ doit alors retenir B2 avec ses moyens ou revoir la cohorte. Le manque de moyens ne transforme pas B1 en substitut à des permissions de groupe.

**Delta après arbitrage :** 01/17 rapprochent catalogue, roadmap, spécification et index ; 18 rend J07 et TEST-1828..1831 conditionnels à la décision, sans supprimer leur historique ni les déclarer PASS. Les cas transversaux restent applicables aux objets effectivement retenus.

### C — Surface et langues : DEC-0001/0002, SYN-002/003

**Recommandation PROPOSÉE :** une interface **web responsive** pour le pilote ; interface française si la compréhension de tous les parcours critiques est démontrée pour la cohorte, avec contenus français/kabyles et capacité humaine correspondante. L'option bilingue français/kabyle doit être retenue ou le pilote différé si le français ne suffit pas et que les moyens nécessaires sont disponibles ou à constituer.

| Option | Intérêt | Condition / alternative |
| --- | --- | --- |
| C1 — Web responsive, interface française — recommandation conditionnelle | Une surface et moins de chaînes à qualifier | 01/19 démontrent la compréhension ; 09/10 couvrent les contenus et recours ; 02/16/18 vérifient les parcours, Unicode et accessibilité |
| C2 — Web responsive, interfaces française et kabyle | Réduit l'exclusion linguistique | Glossaire, relecteurs, textes sensibles, QA et support à fournir ; la disponibilité réelle prime sur une traduction annoncée |
| C3 — Natif mobile et/ou quatre langues dès pilote | Couverture plus large des usages | Besoin, budget, compétences et maintenance à démontrer ; FEAT-025 reste Phase 2 candidate, extension linguistique selon FEAT-032 |

Une interface française ne signifie ni interdiction du kabyle dans les contenus ni capacité universelle de modération. Un texte dans une langue non couverte reste soumis au parcours de réception/escalade défini par 09/10/16 ; aucune modération réussie n'est simulée. Installation PWA, notifications push et synchronisation offline ne sont pas incluses automatiquement.

## 3. Périmètre candidat complet et phases

Les 34 lignes suivantes reprennent la spécification Produit de la base. Seule la présentation de FEAT-020 explicite la recommandation de report de ce dossier. **Toutes les classes restent proposées.** MVP désigne le périmètre candidat du pilote, pas un premier sprint monolithique ni une autorisation de réaliser toute la ligne sans contrat.

| ID | Capacité | Classe candidate PROPOSÉE | Priorité source | Justification / limite |
| --- | --- | --- | --- | --- |
| FEAT-001 | Inscription et activation | MVP | P0 | Accès admissible ; méthode non fixée |
| FEAT-002 | Sessions, déconnexion et récupération | MVP | P0 | Protection et reprise d'accès |
| FEAT-003 | Profil minimal | MVP | P0 | Identité publique compréhensible ; champs facultatifs limités |
| FEAT-004 | Audience et confidentialité | MVP | P0 | Contrôler lecture et accès directs |
| FEAT-005 | Suivre / ne plus suivre | MVP | P0 | Source du fil ; abonnement social, sans paiement |
| FEAT-006 | Texte : créer, modifier, retirer | MVP | P0 | Boucle de création ; règle d'édition ouverte |
| FEAT-007 | Image et texte alternatif | MVP | P0 | Média simple ; ni vidéo ni caméra avancée |
| FEAT-008 | Fil chronologique | MVP | P0 | Ordre explicite et pagination ; pas de classement personnalisé |
| FEAT-009 | Réaction réversible | MVP | P1 | Conversation simple ; type unique proposé |
| FEAT-010 | Commentaires | MVP | P1 | Retour utile ; réponses profondes différées |
| FEAT-011 | Notifications essentielles | MVP | P1 | Centre interne proposé ; push et campagnes de réengagement exclus |
| FEAT-012 | Blocage | MVP | P0 | Arrêt des interactions définies ; pas promesse d'invisibilité absolue |
| FEAT-013 | Signalement | MVP | P0 | Réception traçable, protection du déclarant |
| FEAT-014 | Décision de modération | MVP | P0 | Mesures effectives, information et audit |
| FEAT-015 | Recours | MVP | P0 | Réexamen opérable, y compris compte suspendu |
| FEAT-016 | Accès/export et suppression de compte | MVP | P0 | Sortie du service et droits ; délais et exceptions à décider |
| FEAT-017 | Console de modération/support | MVP | P0 | Exploitation minimale avant ouverture UGC |
| FEAT-018 | Surface web responsive accessible | MVP | P0 | Proposition de première surface ; OPEN-002 non tranché |
| FEAT-019 | Mesures et santé minimales | MVP | P1 | Mesurer valeur et coût sans collecte excessive |
| FEAT-020 | Communautés | Phase 2 recommandée ; MVP conditionnel au catalogue, arbitrage ouvert | P1 | Arbitrage OPEN-003 ; jamais réputée incluse avant DEC-0002 |
| FEAT-021 | Langues du pilote | MVP | P0 | Interface, erreurs et modération dans les langues retenues |
| FEAT-022 | Respect du temps et commandes de lecture | MVP | P1 | Fin/rattrapage et préférences, sans maximiser durée |
| FEAT-023 | Recherche | Phase 2 | P1 | Liens de profil comme alternative pilote ; filtrage d'accès futur |
| FEAT-024 | Messages privés | Phase 2 | P2 | Modèle de sécurité, rétention et anti-abus à instruire |
| FEAT-025 | Applications mobiles natives | Phase 2 | P2 | Coût/valeur à comparer avec responsive/PWA par 06 |
| FEAT-026 | Vidéo et outils courts | Phase 2 | P2 | Coût, traitement, retrait et modération spécialisés |
| FEAT-027 | Outils et statistiques créateurs | Phase 2 | P2 | Dépend de mesures compréhensibles et minimisées |
| FEAT-028 | Pages professionnelles multi-gestionnaires | Phase 2 | P2 | Rôles délégués et usurpation à instruire |
| FEAT-029 | Recommandations facultatives | Phase 3 | P2 | Fil chronologique conservé ; contrôle et explicabilité |
| FEAT-030 | Publicité | Phase 3 | P2 | Économie, données, transparence et fraude avant ouverture |
| FEAT-031 | Revenus, abonnements payants et paiements créateurs | Phase 3 | P2 | Distinct du suivi FEAT-005 ; économie et litiges à décider |
| FEAT-032 | Expansion et opérations locales | International | P1 | Langue, pays et capacité humaine distincts |
| FEAT-033 | Live grande audience | Long terme | P3 | Procédure d'arrêt, capacité et modération démontrées |
| FEAT-034 | Intégrations et portabilité avancée | Long terme | P3 | Permissions, révocation et contrats versionnés |

La boucle candidat comprend également notifications internes essentielles, langues/accessibilité, droits et sortie du service, support/modération/recours, mesure sobre et respect du temps. Ces prérequis ne disparaissent pas lorsque le résumé parle simplement de « texte/image et fil ». Stories et expériences non identifiées au catalogue ne sont pas ajoutées : 01 doit d'abord préciser besoin, phase et rattachement avant toute inscription.

## 4. Règles et contrats qui doivent rester explicites

Les règles ci-dessous résument des exigences candidates des propriétaires. Elles ne définissent pas seules les audiences, codes API, délais, limites ni durées définitives.

| Famille / FEAT | Nominal et états à couvrir | Erreur / concurrence / reprise | Permission, donnée et preuve attendue |
| --- | --- | --- | --- |
| Admission, compte, profil / 001–004 | Invitation si retenue → admission → activation → compte actif ; session expirée/révoquée ; profil minimal | Invitation expirée/révoquée/réutilisée ; récupération interrompue ; compte suspendu ; aucun succès avant enregistrement | Invitation, compte et lecture distincts ; identifiant privé séparé du profil ; schémas/champs/anti-abus/assurance d'âge par 04/14/15 |
| Publication texte/image / 004,006,007 | Brouillon → validation → publié ; image en traitement/prête/rejetée ; retrait et purge distingués | Réponse perdue après écriture, retry, conflit de révision, image refusée ; reprendre sans doublon ni média non validé publié | Auteur sur son contenu ; traitement média et métadonnées ; audience recontrôlée sur original, variantes, aperçu, accès direct et cache |
| Suivi, fil, interactions / 005,008–011,022 | Suivi absent/présent ; fil vide/chargement/page/fin ; réaction réversible ; commentaire visible/retiré | Pagination stable ; droit changé pendant lecture/écriture ; notification en attente/échec ; panne annoncée, pas de faux résultat | Suivre ne confère pas une audience privée ; filtrage serveur ; notification et commentaire héritent des restrictions requises |
| Blocage, signalement, décision, recours / 012–015,017 | Blocage actif/inactif ; dossier reçu/en examen ; décision distincte de son effet ; recours accessible selon politique même en suspension | Signalement doublé, rôle opérateur retiré, conflit de dossier, sanction appliquée mais notification échouée | Membre, auteur, signalant, personne sanctionnée et opérateur ont des pouvoirs distincts ; identité du signalant protégée ; motif, acteur et résultat audités |
| Droits et sortie / 004,016 | Demande reçue/vérifiée/en cours ; export disponible/expiré ; suppression partielle/complète selon périmètre | Dépendance indisponible, preuve insuffisante, effacement concurrent à un job, restauration d'une sauvegarde | Accès aux droits/support à préserver ; export sécurisé ; purge, exceptions et sauvegardes selon politique validée, sans promesse d'effacement instantané universel |
| Langues, lecture et mesure / 018,019,021,022 | Erreurs compréhensibles, clavier/focus ; langue/écriture distinctes de résidence ; indicateur absent/immature/non calculable | Chaîne sensible manquante ; langue non couverte ; dénominateur nul ; panne de mesure sans panne sociale | Préférences minimisées ; aucune origine inférée ; finalités, accès et durées examinés par 13/14/15/16 |

### Matrice d'autorisation à recevoir — SYN-006

Le livrable de 04/09/10/14/15 doit couvrir : anonyme, membre actif, auteur, personne bloquée, compte suspendu, opérateur habilité et opérateur révoqué ; actions créer/lire/modifier/retirer, lire un média direct, notifier, signaler, modérer, contester, exporter et supprimer. Une combinaison non applicable doit être justifiée. Une audience ne sera pas choisie implicitement par l'équipe 21 : valeurs, défaut, évolution, effet du blocage et délai de révocation sont des champs de contrat encore ouverts.

Pour chaque interface retenue : producteur/consommateur, version, authentification/autorisation, entrée/sortie, erreurs stables et textes associés, timeout/retry, idempotence, concurrence, quotas, corrélation/audit, compatibilité et tests. Les contrats candidats [Backend](../backend/api-contract-candidates.md), [Médias](../media/media-lifecycle.md), [Safety](../trust-safety/moderation-requirements.md) et [Administration](../administration/administration-support-requirements.md) sont les points de départ, sans nouvelle API imposée ici.

### Données et mesure — SYN-004

Les propositions divergent : Data propose 45 jours bruts et 13 mois agrégés ; IA propose au plus 7 jours bruts et 90 jours agrégés pour la mesure. Data signale déjà que le churn à 60 jours n'est pas calculable directement sur 45 jours bruts sans autre conception. **Aucune durée n'est retenue ici.**

Recommandation de travail : différer M12 (churn 60 jours) du pilote candidat ; choisir les indicateurs utiles, puis leur finalité et leur donnée minimale avant les durées. 13/07/15 doivent rendre un tableau unique : catégorie/champs, finalité, source, base/choix requis à qualifier, accès, durée, agrégation, export/effacement et reprise après restauration. Un agrégat n'est pas réputé anonyme par son nom. Les journaux de sécurité ont leur finalité propre ; cette proposition ne les supprime pas. Aucune collecte pour de futures recommandations ou annonces n'est autorisée par ce dossier.

### Architecture et exploitation — SYN-003/005

La proposition 03 de monolithe modulaire/API/workers constitue une option cohérente à examiner avec le pilote web. L'application intégrée reste une alternative ; les microservices initiaux demandent une justification. **Aucune stack, base de données, fournisseur ou version n'est adoptée.** La comparaison existante Next.js/NestJS, application intégrée et alternatives Laravel/Django reste à instruire par 03/04/05/14/20 selon compétences, opérations et coût total. Aucun benchmark nouveau n'a été réalisé.

Pour la reprise, les propositions 24 h/8 h et 1 h/4 h doivent être rapprochées par 14/03 en nommant RPO et RTO, perte acceptable, périmètre, coût et exercice attendu. Ne pas prendre automatiquement les valeurs les plus exigeantes ni un fournisseur comme déjà sélectionné. FIND-21-02 (protections/reviewers) et FIND-21-05 (maintenance checkout) restent suivis séparément avec 14/20.

## 5. Ordre de réalisation proposé après décisions

Les lots suivants sont un séquencement candidat, pas une nouvelle roadmap approuvée. Des travaux documentaires indépendants peuvent continuer immédiatement ; le démarrage du code d'un lot exige ses contrats et une autorisation de réalisation suffisants.

| Ordre | Livrable borné | Condition d'entrée | Preuve de sortie / limite |
| --- | --- | --- | --- |
| 0 — Décisions et contrats | DEC-0001/0002 ; arbitrages d'architecture ; matrice acteurs/états/données ; limites et erreurs du premier lot | Dossier présent, avis ciblés et réponse HQ ; pas besoin de relancer les 21 équipes | Décisions datées et liées à un SHA ; contrats propriétaires relus ; budgets et capacités explicites |
| 1 — Identité, profil minimal et autorisation | Tranche FEAT-001..004/021, contrats de sessions et admission si retenue | Scope, âge/admission, données minimales, architecture et contrats de droits approuvés | Scénarios QA d'identité, révocation et accès exécutables puis résultats sur un commit ; ne permet pas à elle seule un pilote UGC |
| 2 — Publication, médias et lecture | FEAT-005..008, droits et traitement média, révocation/retrait | Lot 1 et contrats 04/08/14/15 ; limites texte/image et panne/reprise définies | Publication et lecture réelles, négatifs d'accès et média, idempotence et concurrence vérifiés |
| 3 — Interactions, protection, opérations et sortie | FEAT-009..017/019/022 avec parcours de support, recours, export/suppression | Contrats 09/10/13/14/15 et moyens opérateurs ; peut être préparé en parallèle du lot 2 | Boucle J01..J06 et critères transversaux couverts ; reprise et procédures humaines éprouvées |
| 4 — Ouverture limitée | Cohorte et capacité approuvées, puis observation du pilote | Gates du §6 satisfaites et GO explicite du responsable désigné par HQ | Ouverture limitée documentée ; décision poursuivre/corriger/suspendre, sans extension automatique |

Modération, recours, droits et sécurité restent des critères d'ouverture même si leur implémentation est répartie en lots. Aucun lancement intermédiaire n'est déduit du passage du lot 1 ou 2.

## 6. Critères d'acceptation et preuves manquantes

Les références de test restent celles de 18 ; aucun test applicatif n'est ajouté, exécuté ou déclaré PASS par cette préparation.

| Gate candidat | Scénario / résultat observable attendu | Référence et statut actuel | Responsable de la preuve |
| --- | --- | --- | --- |
| G0 — Décision traçable | HQ choisit une option ; date, portée, avis, réserves et SHA sont enregistrés ; toute condition non satisfaite demeure visible | DEC-0001/0002 attendues ; aucun accord de scope reçu | HQ + propriétaires |
| G1 — Admission et compréhension | Candidat admissible comprend les parcours critiques ; cas hors cible, invitation invalide et âge inconnu suivent une réponse explicite | TEST-1801..1804, 1837, 1844..1846 selon périmètre ; BLOCKED pour l'application | 01/04/14/15/16/18/19 |
| G2 — Boucle utile | Membre suit, publie une image/texte autorisé, lit dans le bon ordre, reçoit une réponse et peut arrêter/quitter | J01..J03, TEST-1805..1816 et 1848 selon mapping QA ; BLOCKED | 01/02/04/05/08/18/19 |
| G3 — Droits effectifs | Droit retiré/blocage/suspension empêche les opérations interdites sur API/média/cache/notification ; recours et droits autorisés restent disponibles | TEST-1817..1827, 1832..1835, 1838 selon mapping ; BLOCKED | 04/08/09/10/14/15/18 |
| G4 — Exploitation prête | Opérateur révoqué refusé ; incident, purge, sauvegarde/restauration et reprise démontrés sur environnement autorisé | TEST-1838..1847 selon mapping ; BLOCKED ; responsables humains NON REÇUS | 09/10/14/15/18 |
| G5 — Mesure interprétable | Compte technique exclu ; métrique sans dénominateur ou fenêtre complète correctement qualifiée ; collecte conforme au contrat adopté | TEST-1836 et sources 13 ; BLOCKED ; définitions/seuils de succès ouverts | 13/15/18/19/HQ |

Ces regroupements facilitent la lecture : ils ne remplacent pas le mapping détaillé de la [matrice QA](../quality/acceptance-test-matrix.md). 18 doit revoir les cas affectés par les décisions retenues, notamment J07 si les communautés sont reportées. L'absence de signalement n'est pas une preuve de sécurité ; aucune rétention, capacité ou qualité linguistique n'est démontrée par la CI documentaire.

## 7. Dépendances et transmissions ciblées

Tous les messages de ce tableau sont **À TRANSMETTRE** ; publication GitHub ne signifie pas réception d'une nouvelle demande par une autre discussion. Relire seulement les sections indiquées et les sources affectées ; aucune demande générale de réaudit des 21 dossiers.

| Suivi existant / destinataires | Question ciblée et livrable attendu | Bloquant pour | Portée de lecture |
| --- | --- | --- | --- |
| SYN-001 ; HQ/01/19/09/10 | B1 suffit-il au besoin central ? Avis oui/non motivé, alternative B2 et coût humain ; proposition DEC-0002 | Scope et contrats de groupes ; pas le dossier présent | §2B et fiche Produit/Growth correspondante |
| SYN-002 ; HQ/15/16/19/01, avis 09/10/14 | A1/C1 sont-ils admissibles et compréhensibles ? Fiche cohorte, couverture des contenus/langues, âge/admission et réserves | Inscription et ouverture ; pas rédaction des options | §2A/C et propositions existantes Privacy/International |
| SYN-003 ; 03/04/05/06/14/20 | Quel premier lot et quelle option d'architecture/stack répondent au pilote retenu ? Dossier ADR avec compétences, opérations et coût | Code du lot concerné | §4 Architecture et §5 ; ADR-0301..0307 candidats existants |
| SYN-004 ; 13/07/15 | Quelles mesures justifient quelles données et durées ? Tableau unique ; sort de M12 explicitement décidé | Instrumentation concernée | §4 Données et divergence documentée |
| SYN-005 ; HQ/14/03 | Quel budget et quels objectifs RPO/RTO ? Scénarios comparables, perte acceptable, preuve de restauration attendue | Exploitation et ouverture | §4 Reprise et options d'hébergement existantes |
| SYN-006 ; 04/08/09/10/14/15 + 18 | Quelles audiences, droits, erreurs, limites et révocations ? Contrat commun et critères QA affectés | Lots d'identité/contenu/modération correspondants | §4 et §6 ; interfaces candidates propriétaires |
| SYN-007 ; HQ/19/09/10/14 | Qui opère, quand, avec quel plafond et quelle règle d'arrêt ? Plan nominatif opérationnel conservé hors Git si données personnelles ; synthèse de rôles/capacité dans Git | GO pilote | §5/6 et plan Growth existant |
| FIND-21-02/05 ; HQ/14/20 | Quelle solution durable de protection/revue et quel correctif de maintenance checkout séparé ? Décision et preuve d'application | Fin du dispositif transitoire ; maintenance distincte | Constats déjà intégrés, sans réouvrir FIND-21-01/03/04 |

Budget, plafond, disponibilité et seuils de réussite ne sont pas inventés pour remplir un tableau. Leur propriétaire doit fournir valeur, hypothèse et méthode d'observation avant le GO correspondant.

## 8. Enregistrement des arbitrages et prévention des erreurs

Cycle proposé du dossier : PROPOSÉ → AVIS CIBLÉS REÇUS → PRÊT À ARBITRER → choix explicite HQ ; une option est ensuite APPROUVÉE, REJETÉE ou À COMPLÉTER avec preuve. L'absence d'avis reste NON REÇUE. Un simple « document reçu », un succès CI ou une fusion ne fait pas passer une option à APPROUVÉE. Une réponse ambiguë doit être rattachée aux options exactes avant de modifier une référence officielle.

| Trace à enregistrer par HQ | Valeur actuelle |
| --- | --- |
| Option A1/A2/A3 et conditions ; pays/âge/admission | NON DÉCIDÉ |
| Option B1/B2 et traitement de FEAT-020/J07 | NON DÉCIDÉ |
| Option C1/C2/C3, langues réellement couvertes | NON DÉCIDÉ |
| Autorité, date, avis propriétaires, réserves, SHA du dossier décidé | NON REÇUS |
| Décisions DEC-0001/0002 et deltas au registre/catalogue/roadmap/QA | À PRODUIRE APRÈS ARBITRAGE |
| GO de réalisation d'un premier lot / GO de lancement | NON REÇUS ; deux autorisations de portée distincte |

Risques principaux : cohorte choisie sans besoin vérifié ; exclusion linguistique ; confusion suivi/groupe privé ; politique de données choisie par défaut ; périmètre apparemment petit mais moyens de modération absents ; confusion CI documentaire/qualité produit. Réponses proposées : conditions A/B/C explicites, interfaces et gates du dossier, arbitrages par finalité et conservation des conflits SYN. Les protections GitHub restent ouvertes ; une publication ne les configure pas.

Rollback de ce delta documentaire : retrait ou remplacement ciblé du dossier et de ses liens après examen des contributions suivantes ; conserver l'historique et l'éventuel arbitrage qui l'aurait cité. Aucun schéma, runtime ou migration à annuler.

## 9. Vérification et compte rendu à HQ

La base de départ a été reconstruite à partir des fichiers versionnés et son arbre comparé à celui de main : 84 fichiers, arbre identique `1da7b576c427cff1a45924f446cb4f94404ae58b`. Cette copie de contenu locale n'est pas un checkout de l'historique distant.

Contrôles de publication à consigner avec leur résultat effectif dans la PR : `python3 scripts/repository/validate_repository.py`, `git diff --cached --check`, puis workflow Repository quality au SHA publié, avec job et checkout réellement testés. Aucun nouveau test applicatif, audit juridique, benchmark ou exercice d'exploitation n'est exécuté par ce dossier.

1. **Décisions prises / à valider :** synthèse locale et organisation du dossier ; A1/B1/C1 conditionnel recommandés, arbitrages structurants ouverts.
2. **Livrables :** présent dossier v0.1, liens depuis l'index, le statut et la coordination ; publication sur la branche HQ existante avec nouvelle PR distincte du bilan #24 déjà fusionné.
3. **Tests :** résultats du delta et de la CI dans la PR ; historiques séparés de l'exécution présente, aucun PASS applicatif.
4. **Questions :** public/admission, groupes, langues/surface puis données, architecture et capacité selon SYN-001..007.
5. **Dépendances :** demandes ciblées du §7, toutes À TRANSMETTRE tant qu'aucun envoi n'est établi.
6. **Risques :** §8 ; statuts et gates évitent de transformer une proposition en autorisation.
7. **Suite :** obtenir les choix A/B/C et avis nécessaires, les inscrire via HQ dans DEC-0001/0002, puis finaliser les contrats du premier lot avant code. La revue et la fusion de cette PR documentaire suivent leur propre autorisation et ne valent pas GO produit.
