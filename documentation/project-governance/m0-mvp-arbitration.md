# Dossier d'arbitrage du pilote et du MVP — M0

## 1. Identification et statut

| Champ | Valeur |
| --- | --- |
| Référence / version | SN-INT-M0-ARB-001 — v0.4 |
| Date | 30 septembre 2026, Europe/Paris |
| Auteur | 21 — Intégration / Code Review ; préparation du dossier, sans substitution aux propriétaires |
| Autorité attendue | 00 — MASTER / HQ avec 01 Produit, 09 Safety, 15 Privacy et les propriétaires des arbitrages concernés |
| Demande | Poursuivre après consolidation des 21 contributions ; rendre les décisions suivantes concrètes et traçables |
| Base examinée | `main` au SHA `ba26729aa10dc497338a960ae78ba904a72216b2`, arbre `1da7b576c427cff1a45924f446cb4f94404ae58b` |
| Statut | **DIR-012 CONFIRMÉ par le porteur** pour le public universel/marketing ; modalités du pilote et MVP **PROPOSÉS — À ARBITRER** |
| Priorité / classe | Préparation MVP, P0 ; phases futures conservées dans le tableau de périmètre |
| Portée | Options de pilote, contrat de portée candidat, dépendances et ordre de réalisation conditionnel |
| Limites | Pas de nouvelle validation juridique, choix de stack/fournisseur, permission définitive, coût ou calendrier engagé |

**Actualisation du 30 septembre 2026 :** [DIR-012](decision-register.md) remplace le ciblage communautaire initial et confirme le public universel, peuple kabyle inclus, avec les priorités marketing listées dans la [vision](../product/product-vision.md). A1 et C1 ne sont plus recommandés par défaut ; ils restent des options non approuvées à comparer dans ce nouveau cadre. Le choix de groupes FEAT-020 reste distinct.

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

**Positionnement CONFIRMÉ — DIR-012 :** réseau pour tout le monde, peuple kabyle inclus. Les priorités marketing mondiales sont des entrées de recherche et de préparation ; elles ne définissent pas encore le périmètre disponible du pilote. **Travail PROPOSÉ :** comparer les options ci-dessous avec des segments d'usage et besoins communs. Aucun champ d'origine ni déduction d'origine depuis la langue n'est introduit. Un lien d'invitation ne prouve ni âge, ni résidence, ni droit de lire un contenu.

| Option | Bénéfice attendu | Coût / risque / condition |
| --- | --- | --- |
| A1 — Pilote France adultes, sur invitation — option antérieure, à réexaminer | Périmètre opérationnel et recrutement bornés ; reprend la proposition Privacy et l'option d'accès fermé de Growth | Cohorte non représentative ; admission/âge, personnes hors cible et cas transfrontières à instruire avec 15/14 ; seuil, méthode et données d'admissibilité à contractualiser |
| A2 — Pilote dans plusieurs pays | Observe plusieurs usages et marchés prioritaires du public mondial | Requiert pour chaque pays les avis, textes, support et modération adaptés ; charge et délais non chiffrés |
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

**Surface PROPOSÉE :** web responsive pour le pilote. **Langues À ARBITRER :** comparer les besoins des cohortes issues des marchés prioritaires DIR-012 avec les moyens de traduction, support et modération. La recommandation antérieure français puis français/kabyle est retirée comme défaut ; aucune langue principale n'est décidée par ce changement de positionnement.

| Option | Intérêt | Condition / alternative |
| --- | --- | --- |
| C1 — Web responsive, une langue d'interface à choisir | Une surface et moins de chaînes à qualifier ; français/anglais sont des exemples à comparer | 01/19 démontrent la compréhension ; 09/10 couvrent les contenus et recours ; 02/16/18 vérifient les parcours, Unicode et accessibilité |
| C2 — Web responsive, plusieurs langues sélectionnées | Sert des cohortes complémentaires sans paire linguistique prédéfinie | Glossaires, relecteurs, textes sensibles, QA et support pour chaque langue ; périmètre à arbitrer |
| C3 — Natif mobile et/ou large couverture linguistique dès pilote | Couverture plus large des usages | Besoin, budget, compétences et maintenance à démontrer ; FEAT-025 reste Phase 2 candidate, extension linguistique selon FEAT-032 |

Les contenus de toutes les langues, dont le kabyle, sont inclus dans la conception du socle Unicode ; compréhension, traduction et capacité de modération restent à démontrer pour la disponibilité annoncée. Un texte dans une langue non couverte suit le parcours de réception/escalade de 09/10/16, sans modération réussie simulée. Installation PWA, notifications push et synchronisation offline ne sont pas incluses automatiquement.

### D — Comparaison du pilote international après DIR-012

**Complément v0.4, 30 septembre 2026 — auteur 21, recommandation de coordination PROPOSÉE aux propriétaires 01/16/19 et au HQ.** Entrée examinée : PR #27 au SHA `e8d8a56f49d487d78a00af8df9847696b138e7a6`. Cette comparaison utilise les scénarios déjà rédigés par Growth et les exigences de Localisation ; elle ne constitue ni étude de marché, ni nouvel avis pays, ni approbation de ces équipes. Les repères IP1–IP3 sont locaux et ne réservent pas de nouvelle DEC/ADR.

**CONFIRMÉ :** positionnement et priorités marketing DIR-012. **PROPOSÉ :** variantes, langues candidates et dimensionnement ci-dessous. **À VÉRIFIER :** besoins, compréhension, coûts et capacité par cohorte/marché. **NON REÇU :** sélection des pays ouverts, responsables disponibles, budget complet, ressources linguistiques validées et preuves applicatives. Les 17 pays, la Kabylie, le monde arabe, l'Asie et l'ensemble de la planète restent dans le cadre de la [vision](../product/product-vision.md) ; aucun classement entre ces priorités n'est introduit.

| Variante candidate | Composition proposée | Ce qu'elle permet d'apprendre | Coût de préparation / risque | Avis de 21, soumis au HQ |
| --- | --- | --- | --- | --- |
| IP1 — Une langue, plusieurs marchés si prêts | Web responsive ; une langue choisie après qualification, anglais comme exemple à examiner ; périmètre d'admission borné | Boucle sociale et exploitation dans plusieurs marchés sans comparer deux interfaces | Un ensemble de textes critiques à qualifier ; participants exclus du test si incompréhension, sans extrapoler leurs besoins aux autres publics | Alternative de test limité si une seule couverture linguistique est démontrée ; ne valide pas un produit multilingue |
| IP2 — Deux langues, plusieurs marchés si prêts | Web responsive ; anglais/français comme paire candidate à examiner ; deux cercles d'intérêt issus du scénario Growth S1 | Cohérence des mêmes parcours dans deux langues, choix/changement de locale, support et échanges entre cohortes | Deux ensembles de textes et de ressources critiques, relectures et couverture humaine correspondantes ; surcoût non chiffré | **Recommandation de préparation** : produire le dossier de faisabilité IP2, puis confirmer ou remplacer les langues selon la recherche et les moyens |
| IP3 — Couverture linguistique large dès le pilote | Plusieurs langues et marchés du périmètre marketing préparés ensemble ; liste exacte encore ouverte | Expérience plus diversifiée dès l'ouverture | Autant de parcours, textes, compétences et preuves à préparer que de combinaisons retenues ; aucun budget ou effectif démontré | Garder comme option ; ne pas engager cette portée avant comparaison de capacité et coût |

La paire anglais/français est une **hypothèse de travail**, destinée à rendre IP2 comparable ; elle n'est pas réputée optimale ni comprise par les habitants des pays cités. Une autre paire ou un autre ensemble doit la remplacer si les cohortes le justifient. Les langues du contenu, de l'interface, du support et du recours sont qualifiées séparément. L'anglais ne donne pas accès à un pays par défaut ; une langue de contenu non retenue pour l'interface n'est pas automatiquement interdite. Sa réception et son escalade suivent les contrats 09/10/16.

#### Dimensionnement candidat : réutiliser S1, sans multiplier les plafonds

Pour comparer IP1/IP2, reprendre comme **hypothèse** le scénario [Growth S1](../growth/pilot-launch-plan.md) : 40 comptes au total, dont 8 fondateurs/animateurs et 32 autres participants, deux cercles d'intérêt, admission par vagues d'au plus 20. Ce sont des nombres proposés dans Growth, pas une capacité technique vérifiée. Ils ne deviennent ni 40 comptes par pays ni 40 par langue ; les fondateurs restent séparés dans la mesure.

Pour exercer réellement le caractère international, **viser une cohorte dans au moins deux pays préparés**, sans quotas de nationalité ni d'origine. La répartition des 40 comptes dépend des besoins et des capacités ; elle n'est pas fixée à parts égales. Si un seul pays est prêt, présenter au HQ le choix entre un test limité explicitement nommé et le report de la comparaison internationale. L'élargissement ne se déclenche pas automatiquement après une vague réussie. Pays, âge et invitation restent des paramètres à décider, sans déduire une admission de DIR-012.

S1 prévoit 128 heures sur quatre semaines d'ouverture et une valorisation humaine illustrative de 6 400 €, réserve comprise. **Ce calcul n'est pas le devis d'IP2** : les heures de support ne prouvent aucune couverture linguistique, territoriale ou horaire. 19/09/10/16/14 doivent reprendre le calcul en détaillant préparation, traduction/relecture, QA, support/modération, exploitation et suppléance ; éviter de compter deux fois les heures déjà incluses. Ajouter les coûts externes et hypothèses de réserve sans inventer de montant. Si un poste manque, le total reste **INCOMPLET**, même si l'ancien S1 est chiffré. Aucune dépense autorisée ici.

#### Choisir les marchés sur preuves, sans score de rentabilité inventé

Les mêmes critères s'appliquent à chaque marché candidat de DIR-012 et à toute autre proposition motivée. 19/16 préparent une fiche par pays de service envisagé ; Kabylie, monde arabe et Asie restent des périmètres marketing distincts, à préciser quand une campagne ou un service concret est étudié. Aucun pays n'est classé facile, rentable, conforme ou techniquement accessible par ce dossier.

| Preuve attendue dans la fiche de marché | Responsable / sortie observable | Effet de l'absence |
| --- | --- | --- |
| Besoin et cohorte : usage, raison de revenir, relais volontaires et compréhension des parcours | 01/19/16 : synthèse de recherche sans coordonnées ou origine inférée dans Git | Comparaison de valeur et recrutement non prêts |
| Langues et textes : interface, contenu, aide, sécurité, signalement, décision, recours et droits sur les données | 02/16/09/10/15 : versions relues, manques explicites et responsable de chaque langue | Disponibilité annoncée non prête ; une page d'accueil traduite ne suffit pas |
| Analyse du périmètre de service et admission | 15/14/01 : avis daté sur le service envisagé, âge/cas limites, données et textes ; contrat consommable par 04/05 | Ouverture du marché et implémentation dépendante bloquées ; aucune conclusion juridique nouvelle ici |
| Capacité humaine et reprise | 09/10/14/19 : planning, titulaires/suppléants, délais annoncés, escalade et autorité de suspension/reprise | Vague concernée non prête ; aucune disponibilité 24/7 supposée |
| Faisabilité, accès et qualité | 03/04/05/14/18 : environnement, accès au service depuis la cible, limites et résultats des parcours critiques | Aucun PASS technique ni ouverture déduit de la seule documentation |
| Coût, plafond et autorité | HQ/19/14/16 : postes estimés, incertitudes, budget, plafond total, décision et preuve de sortie | Engagement de moyens ou acquisition non autorisé par cette proposition |

Reprendre le cycle existant de 16 : **NON ÉTUDIÉ → EN REVUE → PRÊT À ARBITRER → OUVERT**, puis **SUSPENDU** si décision motivée. Une priorité marketing ne fait avancer aucun de ces états. Les avis et la preuve HQ conditionnent le passage ; aucune matrice d'ouverture remplie n'a été reçue. Après suspension d'acquisition, les voies de recours, de droits et de support existantes restent traitées selon leurs contrats ; ne pas désactiver indistinctement tous les accès.

Entre dossiers suffisamment préparés, proposer l'ordre au HQ selon besoin observé, relais disponibles, couverture humaine et coût estimé. Garder les réserves visibles ; un critère de sécurité ou de préparation manquant n'est pas compensé par une promesse de croissance. À ce stade, les pièces disponibles ne permettent pas de nommer honnêtement les premiers pays ouverts.

#### Impacts et acceptation de la variante retenue

| Élément / phase | Règle ou scénario vérifiable proposé | Références et état réel |
| --- | --- | --- |
| Admission et paramètres — FEAT-001/004/021, MVP | Personne admissible selon la politique reçue ; choisir une langue disponible, vérifier/activer puis reprendre après coupure. Le choix ne change pas pays déclaré, droits ou origine ; aucun succès avant confirmation. | GAP-L1-01/02/03/06/07 ; TEST-1801/1833/1837 et TEST-1601/1603/1604 ; applicatif BLOCKED/PLANNED |
| Boucle sociale — FEAT-003/005–010/018/021, MVP | Même capacité à publier/lire/répondre dans les langues retenues ; Unicode préservé, erreurs compréhensibles, navigation clavier/lecteur d'écran. Changer de langue ne rétablit pas un contenu interdit. | TEST-1832/1837/1844/1848 et TEST-1605/1611 ; applicatif BLOCKED/PLANNED |
| Protection et droits — FEAT-013–017/021, MVP | Signalement dans une langue non couverte : reçu conservé et escalade réelle ; décision, recours et droits restent accessibles selon contrat. Aucun examen humain annoncé comme réussi sans preuve. | TEST-1602/1608/1614, TEST-1914/1917 et J04–J06 de 18 ; applicatif BLOCKED/PLANNED |
| Croissance et coût — préparation MVP | Total des sous-cohortes respecte le plafond global ; fondateurs/tests exclus des indicateurs concernés, fenêtres matures et petites cellules protégées ; coûts inconnus restent affichés comme inconnus. | TEST-1910/1912/1915/1918 ; PLANNED, contrat 13/15 et données NON REÇUS |
| Évolutions | Natif, messagerie et recherche restent Phase 2 candidats ; recommandation/publicité/paiements Phase 3 ; extension de langues/marchés International ; expérimentations Long terme selon catalogue. Aucune collecte anticipée n'est ajoutée. | FEAT et phases existants, inchangés ; choix linguistiques du pilote traités dès le MVP concerné |

Les profils, états de session et permissions détaillés restent dans les contrats propriétaires et le rapport L1. Ce complément ne crée ni endpoint, ni champ d'origine, ni règle de géolocalisation, ni migration. Les données de recherche et les contacts éventuels demandent leurs finalités/accès/rétention ; la publication de ce dossier ne lance pas leur collecte.

#### Demandes ciblées à transmettre et arbitrage proposé

| Destinataire / suivi existant | Demande précise | Livrable et blocage |
| --- | --- | --- |
| 01/19 — INT-1901, SYN-002 | IP2 et S1 testent-ils le besoin de deux cercles d'intérêt sans groupes obligatoires ? Proposer les cohortes d'usage et l'ordre de préparation des marchés, sans supposer un public lié à une origine. | Fiches de cohortes et hypothèses réfutables ; bloque choix du pilote, pas le travail contractuel indépendant |
| 16 avec 02/09/10/15 — INT-1601/1602/1604, INT-1902/1903 | Anglais/français convient-il aux cohortes proposées ? Nommer la couverture de chaque parcours/langue, l'alternative si nécessaire et les avis manquants. | Comparatif des langues, ressources, couverture et fiches de marché ; bloque promesse de disponibilité et ouverture |
| 19/14/16 + HQ — INT-1907, OPEN-006 | Recalculer S1 pour la variante choisie : postes supplémentaires, doublons, suppléance et coûts externes. | Estimation complète avec incertitudes puis budget HQ ; bloque engagement de moyens |
| 04/05/14/18/20 — GAP-L1 et INT-0407/0408 | Relier admission/locale/états/reprise au contrat L1 retenu et affecter les scénarios ci-dessus aux preuves existantes. | Schémas, erreurs, droits et oracles relus ; bloque code dépendant et verdict applicatif |

**Toutes ces demandes sont À TRANSMETTRE.** Aucun avis de 01/16/19, contact, campagne ou budget n'est créé par la rédaction de 21. HQ peut choisir IP1/IP2/IP3, demander une autre variante ou demander des compléments ; consigner la variante, les langues, les pays de service, l'âge/admission, les plafonds, les responsables, le budget et les réserves dans DEC-0001/0002 selon leur portée. **Recommandation actuelle : instruire IP2 avec anglais/français candidats et le plafond S1 global ; ne pas annoncer de pays ouverts avant les preuves.** Elle ne remplace pas DIR-012 ni les gates du §6.

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

Les ordres 0–4 ci-dessous regroupent les travaux ; les identifiants L0–L7 de [20](../delivery/implementation-readiness.md) restent la référence des lots. Le complément [préparation contractuelle L1 v0.4](../quality/first-lot-contract-readiness.md) rapproche les onze API candidates et les besoins Web, précise huit demandes avec propriétaires et réutilise les tests existants. Il détaille les candidats identité courante GAP-L1-03 et cycle de session GAP-L1-04, dont pertes de réponse, révocation et cookies tardifs, avec sous-cas S03a–h/S04a–h ; ses contrats restent à compléter et à approuver par leurs propriétaires. DIR-012 actualise les entrées de cohorte et de langues des options A/C sans les approuver.

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
| SYN-002 ; HQ/15/16/19/01, avis 09/10/14 | Quels pays, cohortes et langues sont préparables après DIR-012, sans présélection A1/C1 ? Fiche cohorte, couverture des contenus/langues, âge/admission et réserves | Inscription et ouverture ; pas rédaction des options | §2A/C et propositions existantes Privacy/International |
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
| Public / priorités marketing DIR-012 | CONFIRMÉS par le porteur le 30 septembre 2026 ; ancien ciblage DIR-002 remplacé |
| Option A1/A2/A3 et conditions ; pays/âge/admission effectivement disponibles | NON DÉCIDÉ ; recommandations antérieures à réexaminer |
| Option B1/B2 et traitement de FEAT-020/J07 | NON DÉCIDÉ |
| Option C1/C2/C3, langues réellement couvertes | NON DÉCIDÉ |
| Autorité et date de positionnement ; avis sur ouverture/contrats | Portée DIR-012 : porteur, 30 septembre 2026 ; avis spécialisés d'ouverture et contrats NON REÇUS |
| Décisions DEC-0001/0002 et deltas au registre/catalogue/roadmap/QA | À PRODUIRE APRÈS ARBITRAGE |
| GO de réalisation d'un premier lot / GO de lancement | NON REÇUS ; deux autorisations de portée distincte |

Risques principaux : cohorte choisie sans besoin vérifié ; exclusion linguistique ; confusion suivi/groupe privé ; politique de données choisie par défaut ; périmètre apparemment petit mais moyens de modération absents ; confusion CI documentaire/qualité produit. Réponses proposées : conditions A/B/C explicites, interfaces et gates du dossier, arbitrages par finalité et conservation des conflits SYN. Les protections GitHub restent ouvertes ; une publication ne les configure pas.

Rollback de ce delta documentaire : retrait ou remplacement ciblé du dossier et de ses liens après examen des contributions suivantes ; conserver l'historique et l'éventuel arbitrage qui l'aurait cité. Aucun schéma, runtime ou migration à annuler.

## 9. Vérification et compte rendu à HQ

La base de départ a été reconstruite à partir des fichiers versionnés et son arbre comparé à celui de main : 84 fichiers, arbre identique `1da7b576c427cff1a45924f446cb4f94404ae58b`. Cette copie de contenu locale n'est pas un checkout de l'historique distant.

Contrôles de publication à consigner avec leur résultat effectif dans la PR : `python3 scripts/repository/validate_repository.py`, `git diff --cached --check`, puis workflow Repository quality au SHA publié, avec job et checkout réellement testés. Aucun nouveau test applicatif, audit juridique, benchmark ou exercice d'exploitation n'est exécuté par ce dossier.

1. **Décisions prises / à valider :** synthèse locale et organisation du dossier ; positionnement universel DIR-012 confirmé ; B1 reste proposé ; A/C et les autres arbitrages de pilote restent ouverts.
2. **Livrables :** présent dossier v0.4, comparaison internationale IP1–IP3 au §2D, complément L1 v0.4 et liens depuis l'index, le statut et la coordination ; mise à jour de la PR #27 existante sur la branche HQ, distincte du bilan #24 déjà fusionné.
3. **Tests :** résultats du delta et de la CI dans la PR ; historiques séparés de l'exécution présente, aucun PASS applicatif.
4. **Questions :** public/admission, groupes, langues/surface puis données, architecture et capacité selon SYN-001..007.
5. **Dépendances :** demandes ciblées du §7, toutes À TRANSMETTRE tant qu'aucun envoi n'est établi.
6. **Risques :** §8 ; statuts et gates évitent de transformer une proposition en autorisation.
7. **Suite :** obtenir les choix A/B/C et avis nécessaires, les inscrire via HQ dans DEC-0001/0002, puis finaliser les contrats du premier lot avant code. La revue et la fusion de cette PR documentaire suivent leur propre autorisation et ne valent pas GO produit.

## 10. Reprise HQ — demande ciblée au propriétaire Backend

**30 septembre 2026 — organisation du travail par HQ, sans approbation des options.** Référence de reprise : PR #27 au SHA `9ce0118d2a6072347f4d8c07d37a149f4d161894`. Les PR #1 à #26 sont vérifiées fusionnées ; #27 est la seule PR ouverte lors de cette reprise. Son workflow Repository quality est completed/success, run 36644587422. Ces preuves concernent la révision reçue ; le présent complément doit recevoir ses propres contrôles.

Le dossier v0.4 est **REÇU HQ pour instruction**. Ce statut n'est ni une revue spécialisée favorable ni une approbation de B1, IP2, des langues, des pays, du budget ou du schéma d'identité. Les huit GAP restent ouverts. Le positionnement confirmé DIR-012 est conservé.

### Première réponse attendue : 04 — Backend / API

**Mandat borné :** produire un delta documentaire propriétaire sur GAP-L1-01 à 04 à partir de la [préparation L1, sections 3 à 4.1](../quality/first-lot-contract-readiness.md). Réutiliser API-BE-001 à 007 et C1–C8 ; ne pas refaire le catalogue complet et ne pas lancer le code applicatif.

| Sujet | Réponse concrète attendue de 04 | Avis nécessaires avant gel |
| --- | --- | --- |
| Identité et transport, GAP-01 | Comparaison des options pertinentes pour le client candidat ; recommandation motivée, preuve d'identité, stockage client, contrôle d'origine/CSRF, paramètres encore ouverts et effets sur le modèle de données | 03/05/14/15 ; HQ pour les décisions structurantes |
| Idempotence préauthentifiée, GAP-02 | Tableau même clé/même entrée, entrée différente, clé différente, preuve consommée, expiration, mutation en cours et réponse perdue ; résultat observable, erreur et confidentialité pour chaque cas | 14 et consommation 05 ; oracles 18 |
| Identité courante, GAP-03 | Avis accepté/amendé/rejeté sur chaque champ et chaque règle du candidat §4.1 ; option lecture/bootstrap, anonymous/restricted/unavailable, mapping d'erreurs et responsabilités d'invalidation | 05/14, projection 09/15 ; aucune route imposée par HQ |
| Cycle de session, GAP-04 | Table connexion/rotation concurrente/révocation/récupération/expiration/déconnexion répétée ; portée, instant d'effet proposé, résultat inconnu et convergence après réponse perdue | 05/14/15 ; paramètres motivés et encore proposés jusqu'à décision |

Chaque réponse doit indiquer : règle proposée, état nominal, erreur, données, permission, producteur/consommateur, dépendances, références QA existantes, décision attendue et preuve de validation future. Un paramètre inconnu reste explicitement ouvert avec propriétaire et impact ; ne pas le remplacer silencieusement par une valeur. Si une option dépend de la stack ou du pilote, rendre la branche conditionnelle et avancer sur la sémantique indépendante.

**Emplacements :** mettre à jour le document Backend propriétaire existant ; proposer seulement les ajustements nécessaires au complément L1 de 21. Conserver les repères GAP existants ; ne pas marquer VERIFIED un contrat seulement rédigé. Les pays et langues ne sont ni fixés ni déduits des priorités marketing. Les autres GAP et SYN continuent d'exister ; cette priorité de réponse ne change pas la roadmap.

### Passage aux avis et critères de retour HQ

1. 04 produit son delta et fournit le SHA, le diff, les questions résiduelles et les vérifications réellement exécutées.
2. 05 examine les comportements consommateur et 14 les hypothèses de session/autorisation ; 09/15 examinent uniquement les projections et données touchées.
3. 18 rattache les oracles aux tests existants, y compris S03a–h ; aucune exécution applicative n'est revendiquée.
4. HQ rapproche les réponses et tranche uniquement les choix relevant de son autorité ; 21 revoit ensuite la cohérence du delta avant intégration.

Critère de réception : les quatre lignes ci-dessus ont chacune une réponse explicite, des alternatives et des dépendances attribuées. Critère de fermeture d'un GAP : réponse propriétaire, accords nécessaires et décision traçable ; un simple document publié ne suffit pas. Les avis non reçus sont conservés comme tels.

**État historique à la préparation du §10 : À TRANSMETTRE à la discussion 04 ; remplacé par la réception vérifiée au §11.** Ce mandat préparé dans GitHub ne déclenche pas l'autre discussion. Les demandes 05/14/18 sont séquencées après le delta 04 pour éviter des contrats parallèles contradictoires ; leurs contributions indépendantes restent possibles. Aucun envoi individuel, aucune réception ni aucun avis n'est revendiqué ici.

**Compte rendu HQ :** organisation de cette réponse ciblée seulement ; livrable présent §10 dans la PR #27 existante ; contrôles de ce complément à vérifier au nouveau SHA ; questions de fond et protections FIND-21-02/05 ouvertes ; risque principal de substituer une proposition HQ aux autorités de domaine ; prochaine étape : recevoir le delta 04 puis les avis bornés. L1 reste BLOQUÉ POUR CODE et aucun GO de lancement n'est donné.

## 11. Réception HQ des avis L1 et convergence des corrections

**30 septembre 2026 — réception vérifiée, pas approbation du protocole.** La réponse Backend [#28](https://github.com/yyogas/social-network/pull/28), SHA `1acf84fffcaa8131c0826d4874126e107a4cf978`, et les quatre avis ci-dessous sont reçus HQ. Ces avis portent tous sur ce même SHA Backend. Le statut NON REÇU antérieur est historique pour ces quatre avis seulement ; les accords sur corrections, l'avis Architecture et les réponses Safety restent non reçus.

| Propriétaire | PR ouverte | Source versionnée reçue | CI du SHA de l'avis |
| --- | --- | --- | --- |
| 05 Web | [#29](https://github.com/yyogas/social-network/pull/29) | [Avis au SHA exact](https://github.com/yyogas/social-network/blob/e363e751d4b797cceb6c6ab3ec79745d6e54e380/documentation/web-application/backend-l1-web-review.md) | [success](https://github.com/yyogas/social-network/actions/runs/36648382675) |
| 14 Sécurité | [#30](https://github.com/yyogas/social-network/pull/30) | [Avis au SHA exact](https://github.com/yyogas/social-network/blob/3221f762b5f98a552a3600fc24118fbe99b7a003/documentation/security/backend-l1-security-review.md) | [success](https://github.com/yyogas/social-network/actions/runs/36648436925) |
| 15 Privacy | [#31](https://github.com/yyogas/social-network/pull/31) | [Avis au SHA exact](https://github.com/yyogas/social-network/blob/81063238cd32689c630aaa1e70633b7104a48042/documentation/privacy/backend-l1-targeted-review.md) | [success](https://github.com/yyogas/social-network/actions/runs/36648452400) |
| 18 QA | [#32](https://github.com/yyogas/social-network/pull/32) | [Avis au SHA exact](https://github.com/yyogas/social-network/blob/cada61a7b6391a1119bfdf70b4ddc7b04ab13dbb/documentation/quality/backend-l1-qa-review.md) | [success](https://github.com/yyogas/social-network/actions/runs/36649149045) |

Les quatre CI sont completed/success lors de cette consultation. HQ a lu les pièces, les verdicts et les demandes : ce n'est ni une exécution de tests applicatifs ni une nouvelle revue spécialisée. Les acceptations documentaires sont locales ; aucun GAP n'est fermé. Les quatre avis contiennent **onze constats bloquants au total, avec recouvrements** : Web 4, Sécurité 3, Privacy 2, QA 2. Ne pas les présenter comme onze bugs runtime ni additionner leurs tests d'outillage pour annoncer une couverture produit.

### Corrections regroupées, sans nouvel identifiant concurrent

| Groupe de travail | Constats sources à conserver | Livrable de convergence attendu | Responsables et contrôle |
| --- | --- | --- | --- |
| Liaison navigateur et acquisition cohérente | Web B01/B04 ; S14-L1-05 ; QA L1-BE-08 / QA-B | Table identité/version/CSRF/cookies et intention ; deux bootstraps concurrents, cookies tardifs/perdus/remplacés, réveil d'onglet ; résultat HTTP, effet durable et état UI pour chaque ordre ; refus des combinaisons incohérentes | 03 propose primitives/hypothèses ; 04 amende le contrat ; 05/14 revoient ; 18 vérifie les oracles |
| Attribution du login et ordre logout/login | Web B02 ; S14-L1-13 ; QA L1-BE-07 / QA-A | Distinguer login préparé avant logout mais committé après, nouvelle intention explicite après logout, récupération concurrente et réponse login perdue ; point de sérialisation et attribution du résultat à l'intention, sans lookup privé | 03/04, avis 14/05 et minimisation 15 ; ni nom de DB ni protocole choisis par HQ |
| Déconnexion incertaine après reload | Web B03 ; amendements QA L1-BE-06 / QA-D | Portée et fin du verrou, reload/historique/restauration/nouvel onglet, stockage indisponible/perdu ; mécanisme minimal ou limite de reprise explicite ; ne pas réafficher le privé par simple relecture d'une session encore active | 04/05/14/15 ; paramètres et persistance à ratifier, aucun stockage de secret implicitement autorisé |
| Historique K absent, perdu ou purgé | S14-L1-09 ; QA-C | Distinguer première opération autorisée et historique perdu ; garanties de durabilité/admission ou invalidation de génération ; pas de mutation doublée sur miss cache ; lien avec rotation d'empreinte, tombstones et purge | 03/04/14, cycle 15, oracle 18 |
| Conservation après validité | P15-L1-08 ; QA-C/QA-F | Compléter les neuf objets du tableau Privacy : finalité, accès, début/fin de validité, déclencheur et borne de conservation, marge de purge, exceptions/backups, preuve de restauration ; borner le contexte multi-compte | 04 décrit les besoins ; 14/15 valident les contraintes ; aucune durée déduite d'un TTL ou d'un ancien chiffre analytics |
| Accès aux droits sous restriction | P15-L1-05 ; QA-E ; questions Web sur reprise | Matrice opération × état × preuve × canal, y compris hors session ; voies recours/privacy et responsable opérationnel ; distinguer restriction, authentification et panne | 09/10/15/14 définissent avec 04 ; 05 consomme ; dépendance GAP-05 déjà ouverte, pas de réaudit de la modération entière |

**Amendements non bloquants à ne pas perdre :** chaque ligne À AMENDER des quatre sources doit aussi recevoir une réponse motivée : priorité des erreurs, allowlist d'activité, bornes et budgets, rotation d'empreinte, challenges après recovery, projection compte/profil/capacités, paramètres, messages et preuves navigateur. Le tableau ci-dessus priorise les blocages sans supprimer les autres verdicts. Conserver les repères des propriétaires dans la réponse.

### Mandat de correction et ordre de travail

- **03 Architecture :** instruire les primitives nécessaires aux quatre premiers groupes avec les contraintes des avis ; proposer une option et ses alternatives, hypothèses, atomicité/durabilité, modes panne et coût de complexité. Réutiliser les ADR candidats ; aucune stack, table ou durée ne devient approuvée par défaut. Une option plus simple avec reprise utilisateur explicite doit être comparée aux contextes/reçus supplémentaires avant toute sophistication.
- **04 Backend :** compléter la PR #28 existante, après lecture des quatre avis ; produire une table source → réponse → section amendée → dépendance → preuve attendue. Avancer sur les corrections indépendantes ; conserver les choix Architecture, Privacy et Safety explicitement ouverts jusqu'à leur réponse. Ne pas marquer les avis clos sur sa seule auto-évaluation.
- **05/14/15/18 :** revoir ensuite uniquement le delta qui répond à leurs constats au nouveau SHA, sans recommencer la revue historique. 09/10 interviennent uniquement sur le raccordement des droits ; leurs avis ne sont pas présumés reçus.
- **21 :** vérifier la cohérence et les raccordements après amendements et avis ; HQ arbitre les décisions transversales sur options concrètes. Le contrôle technique n'adopte pas le périmètre produit.

Critère de réception du correctif : les onze constats bloquants et chaque amendement ont une réponse traçable, même si certaines restent BLOQUÉES avec propriétaire. Critère de levée : correction au SHA exact et avis favorable du propriétaire concerné ; les tests runtime restent à réaliser après autorisation du lot. Aucune fusion de #27–32 ni GO code/pilote dans cette réception.

### Branches, preuves et compte rendu

#28 est empilée sur #27 ; #29–32 sont empilées sur #28. Après modification d'une base, vérifier le diff propre à chaque contribution et sa CI ; les avis restent ancrés au SHA initial et ne valent pas approbation automatique du nouveau Backend. Ne pas supprimer les branches ni recopier les quatre rapports dans le contrat : les liens immuables ci-dessus sont les pièces de référence.

Ce delta HQ met à jour le dossier existant sur la branche de #27. Sa vérification documentaire et sa CI sont à consigner dans la PR au nouveau SHA ; les CI ci-dessus concernent uniquement les avis reçus. Aucun test applicatif, navigateur, sécurité ou restauration exécuté par cette consolidation.

1. **Décision :** réception des quatre avis et organisation des corrections ; aucune option technique adoptée.
2. **Livrable :** présent §11, sources versionnées et demandes groupées ; §10 conservé comme historique du mandat.
3. **Vérifications :** SHA/PR/fichiers et quatre CI relus ; tests runtime toujours non exécutés.
4. **Questions :** primitives 03, contrats amendés 04, cycles 15 et droits 09/10 ; durées et options toujours ouvertes.
5. **Dépendances :** matrice ci-dessus ; nouvelles demandes 03/04 **À TRANSMETTRE**, leur publication n'est pas une réception interdiscussion.
6. **Risques :** accepter un protocole par simple CI verte, divergence des réponses aux mêmes courses, surconservation ou accès aux droits absent ; aucune faille applicative reproduite.
7. **Suite HQ :** transmettre le mandat à 03 et 04 ; recevoir leurs deltas et solliciter la relecture ciblée des propriétaires. L1 demeure BLOQUÉ POUR CODE.
