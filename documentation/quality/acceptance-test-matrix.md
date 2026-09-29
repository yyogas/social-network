# Matrice d’acceptation — M0 / équipe 18

## Identification et statut

| Champ | Valeur |
| --- | --- |
| Objectif | Rendre le candidat pilote vérifiable : exigence → risque → cas → preuve → verdict |
| Propriétaire | 18 — QA / Testing / Release ; aucun reviewer humain GitHub affecté |
| Destinataires | 00/01/02/03/04/05/06/08/09/10/13/14/15/16/17/19/20/21 |
| Date / révision | 29 septembre 2026 — v0.1 du livrable propriétaire GitHub |
| Base consultée | `dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957`, branche `documentation/m0-team-coordination`, [PR nº 2](https://github.com/yyogas/social-network/pull/2) |
| Mandat | [M0-TEAM-18](../teams/work-orders.md#m0-team-18--qa--testing--release), DIR-010 et DIR-011 ; réponse à INT-0008 |
| Références | [Vision](../product/product-vision.md), [catalogue](../product/feature-catalog.md), [parcours](../product/user-journeys.md), [plan](../documentation-plan.md), [modèle](../teams/deliverable-template.md), [stratégie unique](test-strategy.md) |
| Statut | PROPOSÉ pour revue spécialisée ; aucune approbation de MVP, permission ou release |
| Périmètre | Les 31 AC-J du candidat pilote, 17 exigences QA transversales et les limites de couverture des 34 FEAT |
| Exclusions | Implémentation applicative, adoption de stack, définition unilatérale d’âge/rétention/permissions, tests offensifs sur production |
| Dépendances | INT-1801 à INT-1813 proposées ci-dessous ; l’absence d’un contrat bloque son cas, pas la rédaction M0 indépendante |
| État d’exécution | 48 cas définis, tous BLOCKED pour exécution applicative ; aucune preuve applicative disponible |

**CONFIRMÉ :** le mandat documentaire est reçu dans cette discussion ; les documents et le validateur de la base GitHub ont été lus. Le catalogue est proposé. **PROPOSÉ :** cas, priorités de test et gates ci-dessous. **À VÉRIFIER :** réponses spécialisées postérieures à la base, choix de client et valeurs contractuelles. **NON REÇU dans les entrées de ce lot :** contrats approuvés, artefact applicatif, environnement de test autorisé, fixtures implémentées et résultats applicatifs. Les sources déjà présentes sur d’autres branches ne sont pas réputées inexistantes.

Les deux notes QA antérieures de cette discussion (spécification générale v0.1 et Fondation M0 v0.1) servent de matériau de travail. Cette matrice les rapproche des références GitHub ; la stratégie de validation reste dans le fichier existant. Aucun export brut de conversation n’est ajouté au dépôt.

## Besoins, phases et couverture

Le besoin QA est de vérifier qu’un membre maîtrise ses publications et interactions, et que les opérateurs peuvent traiter un abus puis un recours avec des droits limités. Le catalogue conserve l’autorité des IDs et la phase proposée ; la priorité QA d’un test négatif peut être P0 même pour une FEAT P1.

Les tests 1832–1834 s’appliquent transversalement aux opérations effectivement retenues. Ils ne remplacent pas les tests nominaux ci-dessous. Couverture documentaire ne signifie ni couverture exhaustive ni résultat PASS.

| FEAT | Besoin / fonctionnalité | Phase proposée | Priorité catalogue | Cas ou limite de couverture |
| --- | --- | --- | --- | --- |
| FEAT-001 | Inscription et activation, méthode à décider | MVP | P0 | TEST-1801, TEST-1802, TEST-1842, TEST-1845 |
| FEAT-002 | Connexion, sessions, déconnexion et récupération | MVP | P0 | TEST-1803, TEST-1804, TEST-1834, TEST-1845, TEST-1846 |
| FEAT-003 | Profil, nom d'affichage, avatar et description | MVP | P0 | TEST-1848 |
| FEAT-004 | Confidentialité et contrôle de visibilité | MVP | P0 | TEST-1805, TEST-1808, TEST-1809, TEST-1811, TEST-1814, TEST-1826, TEST-1828 |
| FEAT-005 | Suivre et ne plus suivre une personne | MVP | P0 | TEST-1810, TEST-1812 |
| FEAT-006 | Publier, modifier et retirer du texte | MVP | P0 | TEST-1805, TEST-1807, TEST-1808, TEST-1809, TEST-1834, TEST-1838, TEST-1842, TEST-1843, TEST-1845 |
| FEAT-007 | Ajouter une image, texte alternatif et contrôler son traitement | MVP | P0 | TEST-1805, TEST-1806, TEST-1807, TEST-1808, TEST-1809, TEST-1827, TEST-1834, TEST-1835, TEST-1838, TEST-1842, TEST-1843 |
| FEAT-008 | Fil chronologique avec pagination et états vides | MVP | P0 | TEST-1810, TEST-1842, TEST-1843 |
| FEAT-009 | Réagir et retirer sa réaction | MVP | P1 | TEST-1812, TEST-1848 |
| FEAT-010 | Commenter et gérer ses commentaires | MVP | P1 | TEST-1811, TEST-1834, TEST-1848 |
| FEAT-011 | Notifications essentielles et préférences | MVP | P1 | TEST-1812, TEST-1814, TEST-1838 |
| FEAT-012 | Blocage et arrêt des interactions visées | MVP | P0 | TEST-1814, TEST-1815 |
| FEAT-013 | Signaler un contenu ou un compte | MVP | P0 | TEST-1816, TEST-1817, TEST-1818, TEST-1842, TEST-1845 |
| FEAT-014 | Examiner, restreindre et notifier une décision de modération | MVP | P0 | TEST-1819, TEST-1820, TEST-1821, TEST-1823, TEST-1838, TEST-1843, TEST-1847 |
| FEAT-015 | Contester une décision et recevoir un résultat | MVP | P0 | TEST-1822, TEST-1823, TEST-1834 |
| FEAT-016 | Demandes d'accès/export et suppression de compte | MVP | P0 | TEST-1824, TEST-1825, TEST-1826, TEST-1827, TEST-1834, TEST-1838 |
| FEAT-017 | Console minimale de modération et support | MVP | P0 | TEST-1817, TEST-1819, TEST-1820, TEST-1821, TEST-1822, TEST-1829, TEST-1842, TEST-1845, TEST-1846, TEST-1847 |
| FEAT-018 | Web responsive et accessibilité des parcours prioritaires | MVP | P0 | TEST-1813, TEST-1844 |
| FEAT-019 | Mesures minimales d'usage et de santé du pilote | MVP | P1 | TEST-1836, TEST-1847 |
| FEAT-020 | Communautés, membres, rôles et règles — INCLUSION À ARBITRER | MVP | P1 | TEST-1828, TEST-1829, TEST-1830, TEST-1831 |
| FEAT-021 | Langues du pilote et contenus multilingues | MVP | P0 | TEST-1837 |
| FEAT-022 | Respect du temps : commandes de lecture et préférences | MVP | P1 | TEST-1848 |
| FEAT-023 | Recherche de comptes, contenus et communautés accessibles | Phase 2 | P1 | Recherche : retrait/blocage dans résultats, extraits et accès direct ; cas détaillés avant ce lot. |
| FEAT-024 | Messagerie privée avec contrôles anti-abus | Phase 2 | P2 | Messagerie : adhésion, blocage, anti-abus, ordre/reconnexion et confidentialité ; modèle de sécurité attendu. |
| FEAT-025 | Applications mobiles natives et notifications associées | Phase 2 | P2 | TEST-1844 est un canevas conditionnel ; compléter permissions OS, stockage local, notifications, upgrade et appareils avant Phase 2. |
| FEAT-026 | Vidéo enregistrée, formats courts et outils de création | Phase 2 | P2 | Vidéo : upload repris, transcodage, variantes privées, retrait et coût ; TEST-1835 images ne suffit pas. |
| FEAT-027 | Outils créateurs : publication et statistiques compréhensibles | Phase 2 | P2 | Créateurs : accès à ses seuls rapports, définition et rapprochement des indicateurs avec 12/13. |
| FEAT-028 | Présence professionnelle et gestion à plusieurs | Phase 2 | P2 | Business : portée des rôles, retrait du gestionnaire, action attribuée et concurrence. |
| FEAT-029 | Recommandations facultatives et explication des suggestions | Phase 3 | P2 | IA : version modèle, fallback déterministe, désactivation, filtres d’accès, évaluation des biais et contrôles utilisateur. |
| FEAT-030 | Publicité transparente et gestion des campagnes | Phase 3 | P2 | Ads : étiquetage, diffusion autorisée, budget, fréquence, fraude et mesure ; contrats 11/15 requis. |
| FEAT-031 | Rémunération, abonnements et paiements aux créateurs | Phase 3 | P2 | Paiements : arrondis/devises, webhooks rejoués, ledger, litiges et absence de double versement. |
| FEAT-032 | Nouvelles régions, langues, écritures et opérations locales | International | P1 | Ouverture par marché : langues/écritures, fuseaux, support/modération et règles locales ; TEST-1837 pilote ne certifie pas l’expansion. |
| FEAT-033 | Direct vidéo et interactions en temps réel à grande audience | Long terme | P3 | Live : interruption d’abus, latence, incident et saturation ; aucune charge live démontrée. |
| FEAT-034 | Écosystème développeurs, intégrations et portabilité avancée | Long terme | P3 | Intégrations : scopes, révocation, versioning/quotas et portabilité ; revue propriétaire avant protocole détaillé. |

**FEAT-020 :** J07 reste conditionnel. Exclure les communautés est une option de MASTER/01, pas une suppression des cas. **FEAT-018/025 :** le web est candidat et le natif est Phase 2 dans le catalogue ; tout arbitrage mobile dès pilote impose une mise à jour coordonnée. Les langues du pilote (FEAT-021) se vérifient dès MVP ; elles sont distinctes de l’expansion International.

## Règles, états, erreurs et reprise à éprouver

| Famille | États et transitions candidats | Refus, erreurs et reprise à préciser par propriétaire |
| --- | --- | --- |
| Identité | non authentifié → activation en attente → actif ; session active/expirée/révoquée ; récupération | Activation consommée, preuve invalide, limitation ; aucun accès avant vérification. Compte limité/suspendu/supprimé a une matrice de droits distincte. |
| Profil et publication | initial/vide → édition → envoi → traitement → publié ; modification/retrait/restriction | Validation de champs, taille/type fichier, conflit de version, session perdue ; afficher état incertain si réponse perdue, puis réconcilier. |
| Lecture/interactions | vide/chargement/partiel/succès/indisponible ; suivi/réaction/commentaire → retrait | Ressource disparue/droits modifiés ; refus côté serveur ; ordre du fil et départage explicites ; pas de faux contenu pour combler le vide. |
| Signalement/modération | brouillon → reçu → trié → décision → effet appliqué/échec ; recours → résultat | Signalement ≠ blocage ≠ sanction ; dossier dupliqué, agent révoqué, conflit, preuve absente ; motif, décision, effet et notification séparés. |
| Données personnelles | demande vérifiée → en cours → export prêt/expiré ; suppression en cours → effets achevés selon catégorie | Erreur reprenable, exceptions et rétention décidées ; aucun effacement total instantané promis ; restauration revue avant réouverture. |
| Communautés | non-membre/en attente/membre/exclu ; rôle local retiré ; fermée | Perte du dernier responsable, départ et données restantes : attendus non définis par QA. |

Ces noms sont des labels de test, pas des enums API approuvés. Pour chaque erreur, 04/02 doivent fournir code stable, catégorie HTTP si pertinente, texte utilisateur localisé, état persistant, corrélation sans secret et reprise permise. La politique d’existence cachée (refus vs ressource introuvable), les délais de révocation et la conservation locale attendent 14/15. Pas de valeur de timeout ou de retry arbitrairement validée.

## Permissions, données et contrats

### Matrice de rôles de test

| Acteur synthétique | Actions / portée à examiner | Oracle de refus |
| --- | --- | --- |
| Visiteur anonyme | inscription/récupération, contenus autorisés aux visiteurs | aucun champ privé ; droit de lecture publique à décider |
| A propriétaire actif | son profil/publication/export ; interactions admissibles | aucune modification de B ; aucune extension d’audience interdite |
| B autorisé / C exclu | lecture détail/fil/original/variante/notification | même policy sur tous les chemins, y compris erreurs et métadonnées |
| Bloqueur / bloqué | lire/suivre/commenter/réagir selon effets décidés | matrice directionnelle testée ; pas d’invisibilité absolue supposée |
| Limité / suspendu / suppression en cours | action sociale vs appel/export/assistance | droits par action ; suspension ne supprime pas automatiquement accès au recours |
| Modérateur / réviseur / support | voir/créer/modifier/supprimer/exporter/approuver/escalader dossier | permissions distinctes, portée et justification ; pas de rôle omnipotent supposé |
| Rôle local / service de traitement | ressource communautaire ou tâche précise | aucune portée globale acquise par rôle local ; job réévalue droits/état selon contrat |

TEST-1832 instancie chaque couple acteur × opération × objet pertinente avec attendu autorisé/refusé fourni par 04/09/10/14/15. Tester ID substitué, propriété protégée, liste/compteur et session ouverte lors de retrait de droit. Masquer un bouton ne satisfait jamais le contrôle serveur. La validation de cette matrice demeure chez les propriétaires.

### Fixtures, données et cycle de vie

Données entièrement fictives : comptes A/B/C et agents M/R/S ; adresses de test sous example.invalid ; objets P1/P2, images bénignes I1/I2, dossiers R1/R2 et communautés G/H si retenues. Horloge contrôlée pour expiration, ordre et rétention ; contraintes et valeurs de frontière reçues des contrats. Aucun mot de passe/token réel ni contenu d’utilisateur copié.

| Catégorie | Origine / finalité / accès | Cycle de vie et preuve minimale |
| --- | --- | --- |
| Comptes/profils/relations | Fixtures locales ; propriétaire 01/04 ; tester audiences/roles | Initialiser isolément par run ; reset et suppression contrôlés ; aucun export réel |
| Texte/images/variantes | Génération synthétique ; propriétaire 01/08 | Capturer seulement ID/hash/état et résultat autorisation ; vérifier purge des dérivés ; seuils selon 08 |
| Dossiers/sanctions/recours | Scénarios fabriqués ; propriétaire 09/10 | Pièces visibles aux seuls rôles de test ; pas de texte sensible dans logs ; historique de décision vérifiable |
| Export/suppression/sauvegarde | Inventaire synthétique de 15/04/14 | État avant/après par catégorie ; restauration isolée ; retention et exceptions ne sont pas fixées par QA |
| Analytics/audit/traces | Capture autorisée des signaux de test ; propriétaire 13/14 | Canaris inertes pour détecter fuites ; séparer mesures agrégées, audit, finance future ; accès/retenue selon politique |
| Rapports/screenshots QA | Résultats expurgés du run ; propriétaire 18, support 14/15 | ACL et durée de conservation à décider ; dans Git : référence, hash et résumé sûr ; fichiers privés hors dépôt publicisable |

Les preuves ne doivent pas recopier payloads, sessions ni données supprimées par commodité. Une demande de suppression affectant une fixture/trace se traite selon le même registre de catégories ; la politique de conservation des preuves QA attend INT-1806. L’utilisation future de données de production demanderait une décision distincte, sans l’autoriser ici.

### Interfaces à recevoir et contrats de test

| Interface candidate | Producteur → consommateurs | Éléments nécessaires à l’oracle |
| --- | --- | --- |
| Identité/session/récupération | 04/14 → 05/06/10 | ID/version, auth, états, entrée/sortie, anti-énumération, révocation, expirations, limites, erreurs |
| Profil/contenu/feed/interactions | 04 → 05/06 | audiences/objets/champs, validation, pagination/départage, conflits/version, idempotence, API anciennes |
| Upload/traitement/diffusion/retrait | 08/04 → 05/06 | accès URL/original/variantes, tailles/formats, quotas, étapes, retry, annulation, purge et délais |
| Dossiers/modération/recours | 09/10/04 → 10/05 | droits dossier/action/preuve, séparation décisions/effets, concurrence, audit, notification |
| Export/suppression/jobs | 15/04 → 05/10/14 | vérification, contenu autorisé, liens/expiration, progression, délais par catégorie, backup et replay |
| Événements, observabilité, livraison | 04/13/14/20 → workers/clients/opérateurs | schema/version, identifiants corrélables, déduplication, ordre, retry borné, DLQ si retenue, santé et compatibilité |

Pour chacune : authn/authz, schémas complets et validation, timeout, politique retry, idempotence, concurrence, limites, audit/corrélation et compatibilité sont **NON REÇUS comme contrats approuvés** dans la base. Les valeurs restent chez les producteurs et consommateurs. QA prépare des injections de panne et attendus paramétrés ; aucun endpoint ni schéma DDL n’est créé ici.

### Dimensions à décliner sur chaque fonctionnalité retenue

Happy path ; donnée invalide et frontière ; droit insuffisant/anonyme/autre compte ; suspension/limitation ; ressource retirée ; chargement/état vide/erreur ; réseau lent ; hors ligne ; retry après réponse perdue ; concurrence ; charge. Une dimension sans sens doit être justifiée par le propriétaire dans le cas instancié, et ne devient pas PASS.

Profils réseau **proposés pour laboratoire** : normal de référence ; lent à 400 kbit/s descendant, 200 kbit/s montant, 400 ms RTT et 1 % de pertes ; coupure 30 s puis reprise ; hors ligne dès ouverture. Ce ne sont ni une promesse de service ni des SLO. 05/06/14 peuvent les ajuster aux pilotes avec preuve. Sous coupure, aucun cache privé ni file de mutations n’est implicitement autorisé ; le contrat définit ce qui est disponible et le risque de révocation sur données déjà téléchargées.

## Acceptation et vérification

### Lecture des fiches

Chaque ligne TEST est une définition unique. Les 31 AC-J conservent leur identifiant et leur statut documentaire PLANNED dans le document Produit ; les instances de test ici sont **BLOCKED** pour exécution faute de build/contrats/environnement. Tous les scénarios et résultats sont PROPOSÉS. PASS/FAIL n’existeront que dans un run séparé ; un expected non décidé reste bloquant, jamais évalué arbitrairement.

Les identifiants TEST-1801 à TEST-1848, REQ-1801 à REQ-1817 et INT-1801 à INT-1813 sont proposés dans le périmètre 18 ; unicité contrôlée contre la base seulement, à faire vérifier par 17 lors de l’intégration des autres branches.

**Preuve E(TEST-ID)** : emplacement futur `test-artifacts/<run-id>/<test-id>/` dans un espace d’artefacts à accès restreint, non créé par ce document. Chaque ligne référence explicitement E. Contenu attendu : version du test/contrat, SHA build et configuration, OS/client et dépendances, fixture/seed, horodatage, commande ou étapes manuelles, résultat réel, assertion par sous-cas, logs expurgés, hash des preuves et lien CI. Les scripts de ces tests applicatifs sont NON REÇUS ; aucune commande exécutable fictive n’est donnée.

**Blocage commun D-BUILD :** artefact applicatif, environnement/fixtures et contrat de lot approuvé absents des entrées ; complété par les dépendances indiquées ligne par ligne. R1–R9 désignent les familles de risque définies ci-dessous, pas de nouveaux risques officiels HQ.

### J01 — critères HQ

| Test / exigence / priorité / type | Risque ; dépendance | Préconditions et données fictives | Action | Résultat attendu | Statut / preuve |
| --- | --- | --- | --- | --- | --- |
| TEST-1801 ; AC-J01-01 ; FEAT-001 ; P0 ; API, intégration, E2E | R1 ; D-ID | Compte admissible selon règle reçue, alias membre-a@example.invalid, activation valide | Soumettre puis rejouer l’inscription/activation | Un seul compte dans l’état attendu ; aucun droit avant activation | BLOCKED ; E(TEST-1801) vide |
| TEST-1802 ; AC-J01-02 ; FEAT-001 ; P0 ; unitaire, API | R1 ; D-ID | Activation fictive expirée puis déjà consommée ; horloge contrôlée | Activer puis demander la reprise autorisée | Refus explicite et sûr ; aucune session accordée ; nouveau chemin d’activation conforme | BLOCKED ; E(TEST-1802) vide |
| TEST-1803 ; AC-J01-03 ; FEAT-002 ; P0 ; API, E2E | R1 ; D-ID | Session A active sur deux clients ; révocation confirmée | Relire puis écrire une ressource protégée après révocation et actualisation | Accès protégé refusé sur les deux clients ; pas d’écriture tardive autorisée | BLOCKED ; E(TEST-1803) vide |
| TEST-1804 ; AC-J01-04 ; FEAT-002 ; P0 ; API, sécurité | R1 ; D-ID | Comptes A/B et identifiant inexistant synthétique ; preuve de récupération invalide | Tenter récupération et lire le profil privé de B | Aucune donnée privée divulguée ni accès avant vérification ; réponses conformes à la politique anti-énumération | BLOCKED ; E(TEST-1804) vide |

### J02 — critères HQ

| Test / exigence / priorité / type | Risque ; dépendance | Préconditions et données fictives | Action | Résultat attendu | Statut / preuve |
| --- | --- | --- | --- | --- | --- |
| TEST-1805 ; AC-J02-01 ; FEAT-004, FEAT-006, FEAT-007 ; P0 ; API, intégration, E2E | R2 ; D-ACL, D-MEDIA | A auteur, B lecteur autorisé, C exclu ; texte et image synthétiques | Publier puis lire comme B et C via fil, détail et média | B voit les éléments autorisés ; C ne reçoit ni contenu ni variante interdite | BLOCKED ; E(TEST-1805) vide |
| TEST-1806 ; AC-J02-02 ; FEAT-007 ; P0 ; unitaire, intégration, E2E | R3 ; D-MEDIA | Fichier invalide et image dont le traitement échoue de façon contrôlée | Charger puis consulter l’état et tenter l’URL directe | Échec visible, aucun faux succès ni média publié avant validation ; reprise/nettoyage selon contrat | BLOCKED ; E(TEST-1806) vide |
| TEST-1807 ; AC-J02-03 ; FEAT-006, FEAT-007 ; P0 ; API, intégration | R3 ; D-API | Publication acceptée mais réponse réseau perdue ; même clé/logique de reprise | Répéter la soumission identique puis différente selon contrat | Une seule publication pour l’action initiale ; réutilisation incompatible refusée ou traitée explicitement | BLOCKED ; E(TEST-1807) vide |
| TEST-1808 ; AC-J02-04 ; FEAT-004, FEAT-006, FEAT-007 ; P0 ; API, sécurité | R2 ; D-ACL, D-MEDIA | A auteur ; C exclu possédant un identifiant et une URL copiés | Modifier en tant que C puis accéder aux originaux/variantes | Aucune modification ; aucun octet privé servi par accès direct ; refus sans métadonnées sensibles | BLOCKED ; E(TEST-1808) vide |
| TEST-1809 ; AC-J02-05 ; FEAT-004, FEAT-006, FEAT-007 ; P0 ; intégration, E2E | R2 ; D-ACL, D-MEDIA | Contenu déjà vu/caché, lien actif puis retrait/restriction confirmé | Relire fil, détail, aperçu, original et variantes après transition | Nouvelles lectures respectent la nouvelle règle dans son délai approuvé ; traces de purge/revocation corrélables | BLOCKED ; E(TEST-1809) vide |

### J03 — critères HQ

| Test / exigence / priorité / type | Risque ; dépendance | Préconditions et données fictives | Action | Résultat attendu | Statut / preuve |
| --- | --- | --- | --- | --- | --- |
| TEST-1810 ; AC-J03-01 ; FEAT-005, FEAT-008 ; P1 ; unitaire, API, E2E | R4 ; D-API, D-UX | Posts synthétiques dont deux timestamps égaux ; nouveaux posts et retrait pendant pagination | Charger plusieurs pages avec curseur contractuel | Ordre et départage définis ; pas de doublon ; omissions éventuelles conformes à la sémantique de snapshot | BLOCKED ; E(TEST-1810) vide |
| TEST-1811 ; AC-J03-02 ; FEAT-004, FEAT-010 ; P0 ; API, intégration | R2 ; D-ACL, D-API | Formulaire de commentaire ouvert ; droit retiré avant validation | Soumettre après retrait confirmé, puis forcer une course contrôlée | Aucune écriture non autorisée ; point de décision transactionnel documenté ; erreur récupérable | BLOCKED ; E(TEST-1811) vide |
| TEST-1812 ; AC-J03-03 ; FEAT-005, FEAT-009, FEAT-011 ; P1 ; API, E2E | R4 ; D-API, D-UX | A suit B, réaction existante, catégorie de notification modifiable | Se désabonner, retirer réaction, changer préférence, recharger sur second client | Relation, réaction et préférence durables conformes ; retry ne recrée pas l’état antérieur | BLOCKED ; E(TEST-1812) vide |
| TEST-1813 ; AC-J03-04 ; FEAT-018 ; P0 ; frontend, accessibilité, E2E | R5 ; D-UX | Parcours inscription/publication/signalement ; tailles et aides techniques retenues | Parcourir au clavier et lecteur d’écran, zoomer, changer taille | Actions essentielles atteignables, focus/labels/erreurs lisibles ; résultats manuels consignés | BLOCKED ; E(TEST-1813) vide |
| TEST-1814 ; AC-J03-05 ; FEAT-004, FEAT-011, FEAT-012 ; P0 ; intégration, E2E | R2 ; D-ACL, D-UX | Notification différée ; préférence modifiée et contenu retiré avant envoi | Déclencher le job puis ouvrir notification, aperçu et lien | Pas de contenu interdit ; préférence applicable respectée ; décision de modération distinguée du marketing | BLOCKED ; E(TEST-1814) vide |

### J04 — critères HQ

| Test / exigence / priorité / type | Risque ; dépendance | Préconditions et données fictives | Action | Résultat attendu | Statut / preuve |
| --- | --- | --- | --- | --- | --- |
| TEST-1815 ; AC-J04-01 ; FEAT-012 ; P0 ; API, E2E | R2 ; D-ACL, D-TS | A bloque B ; matrice des interactions interdite/autorisée fournie | Tester chaque interaction interdite dans les deux sens prévus, API et UI | Refus côté service conformément à la matrice ; blocage ne prétend pas garantir invisibilité absolue | BLOCKED ; E(TEST-1815) vide |
| TEST-1816 ; AC-J04-02 ; FEAT-013 ; P0 ; API, E2E | R6 ; D-TS, D-API | Signalement synthétique ; réponse reçue puis timeout sans accusé | Envoyer et reprendre avec la même identité de requête | Référence sur réception effective ; état incertain/erreur avant preuve ; dossier sans doublon illégitime | BLOCKED ; E(TEST-1816) vide |
| TEST-1817 ; AC-J04-03 ; FEAT-013, FEAT-017 ; P0 ; API, sécurité | R2 ; D-TS, D-ACL | Dossier R, déclarant A, cible B, note privée synthétique | Lire routes, notifications et exports accessibles à B | Identité du déclarant et note privée absentes des réponses destinées à B | BLOCKED ; E(TEST-1817) vide |
| TEST-1818 ; AC-J04-04 ; FEAT-013 ; P0 ; intégration, API | R6 ; D-TS, D-DATA | Cible supprimée pendant envoi ; dossier déjà reçu | Rejouer et traiter le signalement sur cible supprimée | Référence/état cohérents, données de preuve selon conservation approuvée ; erreur sans perte silencieuse | BLOCKED ; E(TEST-1818) vide |

### J05 — critères HQ

| Test / exigence / priorité / type | Risque ; dépendance | Préconditions et données fictives | Action | Résultat attendu | Statut / preuve |
| --- | --- | --- | --- | --- | --- |
| TEST-1819 ; AC-J05-01 ; FEAT-014, FEAT-017 ; P0 ; API, E2E | R2 ; D-ADMIN, D-ACL | Agent sans droit puis rôle révoqué pendant session | Lire dossier/preuve et soumettre sanction via route directe | Refus sur lecture et action ; session/MFA ne remplace pas l’habilitation de ressource | BLOCKED ; E(TEST-1819) vide |
| TEST-1820 ; AC-J05-02 ; FEAT-014, FEAT-017 ; P0 ; intégration | R6 ; D-TS, D-API | Deux agents autorisés traitent la même version de dossier | Soumettre simultanément décisions opposées | Transition cohérente unique ou conflit explicite ; aucun double effet ; auteurs et résultat auditables | BLOCKED ; E(TEST-1820) vide |
| TEST-1821 ; AC-J05-03 ; FEAT-014, FEAT-017 ; P0 ; intégration, E2E | R6 ; D-TS, D-OPS | Décision acceptée ; panne contrôlée d’application de sanction ou notification | Appliquer, observer statut et reprendre | Décision, effet et notification distincts ; jamais « appliquée » si effet échoué ; reprise traçable | BLOCKED ; E(TEST-1821) vide |
| TEST-1822 ; AC-J05-04 ; FEAT-015, FEAT-017 ; P0 ; API, E2E | R6 ; D-TS, D-ADMIN | Décision contestable ; demandeur A, tiers B, réviseur selon règle reçue | Déposer, consulter et traiter recours avec chaque rôle | Lien immuable vers décision ; A voit son état autorisé, B refusé, réexamen selon pouvoirs approuvés | BLOCKED ; E(TEST-1822) vide |
| TEST-1823 ; AC-J05-05 ; FEAT-014, FEAT-015 ; P0 ; intégration | R6 ; D-TS, D-DATA | Sanction annulable ; contenu aussi retiré pour un autre motif valide | Annuler décision et rejouer le job de restauration | Restaure uniquement effets autorisés ; autre retrait préservé ; correction tracée sans effacer l’historique | BLOCKED ; E(TEST-1823) vide |

### J06 — critères HQ

| Test / exigence / priorité / type | Risque ; dépendance | Préconditions et données fictives | Action | Résultat attendu | Statut / preuve |
| --- | --- | --- | --- | --- | --- |
| TEST-1824 ; AC-J06-01 ; FEAT-016 ; P0 ; API, sécurité | R2 ; D-DATA, D-ID | Export synthétique A prêt ; B différent ; lien expiré | Initier demande pour B puis télécharger comme B et via lien expiré | Création illégitime et téléchargement refusés ; export ne fuit pas par URL | BLOCKED ; E(TEST-1824) vide |
| TEST-1825 ; AC-J06-02 ; FEAT-016 ; P0 ; intégration, E2E | R7 ; D-DATA, D-API | Demande export/suppression en traitement, panne injectée | Interrompre, consulter, reprendre | État exact ; progression reprenable/idempotente selon contrat ; pas de succès complet mensonger | BLOCKED ; E(TEST-1825) vide |
| TEST-1826 ; AC-J06-03 ; FEAT-004, FEAT-016 ; P0 ; intégration, API | R7 ; D-DATA | Inventaire et délais approuvés ; compte A synthétique et catégories associées | Supprimer puis vérifier chaque catégorie et session au délai applicable | Traitements, rétention/exceptions et révocations conformes ; preuve de chaque catégorie sans exposition de données | BLOCKED ; E(TEST-1826) vide |
| TEST-1827 ; AC-J06-04 ; FEAT-007, FEAT-016 ; P0 ; restauration, intégration | R7 ; D-DATA, D-OPS | Sauvegarde synthétique avant suppression ; jobs en attente et médias dérivés | Supprimer puis rejouer jobs et restaurer isolément | Aucune résurrection publique de données interdites ; procédure de réapplication des suppressions démontrée avant réouverture | BLOCKED ; E(TEST-1827) vide |

### J07 — critères HQ

| Test / exigence / priorité / type | Risque ; dépendance | Préconditions et données fictives | Action | Résultat attendu | Statut / preuve |
| --- | --- | --- | --- | --- | --- |
| TEST-1828 ; AC-J07-01 ; FEAT-020, FEAT-004 ; P0 conditionnel ; API, E2E | R2 ; D-COM, D-ACL | Communauté G restreinte, membre A et non-membre B | Lister/lire texte et média comme chacun | Éléments autorisés seulement ; accès direct média aussi contrôlé | BLOCKED ; E(TEST-1828) vide |
| TEST-1829 ; AC-J07-02 ; FEAT-020, FEAT-017 ; P0 conditionnel ; API, sécurité | R2 ; D-COM, D-ADMIN | Responsable local G ; dossier global et autre communauté H | Consulter et gérer G, H et dossier global | Aucun dépassement de portée locale ; refus explicite et trace appropriée | BLOCKED ; E(TEST-1829) vide |
| TEST-1830 ; AC-J07-03 ; FEAT-020 ; P0 conditionnel ; intégration, E2E | R2 ; D-COM, D-ACL | Session de membre/responsable active ; départ, exclusion ou retrait de rôle | Confirmer transition puis lire/agir avec session ouverte | Droits actuels appliqués ; publications existantes suivent politique de départ décidée | BLOCKED ; E(TEST-1830) vide |
| TEST-1831 ; AC-J07-04 ; FEAT-020 ; P0 conditionnel ; intégration, E2E | R6 ; D-COM | Dernier responsable quitte ; fermeture prévue dans fixture | Déclencher chaque cas puis tenter lectures/actions | Procédure de relève/fermeture contractuelle, état visible, absence de communauté sans gouvernance non traitée | BLOCKED ; E(TEST-1831) vide |

### Contrôles transversaux et exploitation

Chaque REQ ci-dessous est proposée par QA : elle complète les AC sans les renuméroter. Pour TEST-1844, la partie FEAT-025 n’entre dans la release qu’après décision de surface ; le contrôle web retenu conserve sa couverture.

| Test / exigence / priorité / type | Risque ; dépendance | Préconditions et données fictives | Action | Résultat attendu | Statut / preuve |
| --- | --- | --- | --- | --- | --- |
| TEST-1832 ; REQ-1801 ; FEAT-001 à FEAT-022 selon inclusion ; P0 ; unitaire policy, API, sécurité | R2 ; D-ACL, D-API | Corpus rôles/objets du § permissions ; champs protégés | Paramétrer chaque opération retenue : voir/créer/modifier/supprimer/exporter/approuver/escalader ; modifier ID, champ et portée | Autorisation et refus suivent la matrice ; refus avant effet durable, sans fuite par erreurs/listes/compteurs | BLOCKED ; E(TEST-1832) vide |
| TEST-1833 ; REQ-1802 ; FEAT-001 à FEAT-022 selon inclusion ; P0 ; frontend, API, E2E | R3 ; D-UX, D-API | Profils réseau synthétiques ; mutations/lectures du § interfaces | Couper avant envoi, après réception serveur et pendant réponse ; reprendre deux fois, passer hors ligne | État incertain signalé, réconciliation sans doublon, pas de succès fictif ; cache/file hors ligne selon contrat approuvé | BLOCKED ; E(TEST-1833) vide |
| TEST-1834 ; REQ-1803 ; FEAT-002, FEAT-006, FEAT-007, FEAT-010, FEAT-015, FEAT-016 ; P0 ; API, concurrence, E2E | R2 ; D-ACL, D-TS, D-DATA | A suspendu/limité ; mutation prête à valider, appel/export demandés | Varier suspension avant requête, avant commit, après réponse ; rafraîchir cache | Actions interdites refusées au point défini ; appel et droits sur données testés séparément selon règles, sans blocage global supposé | BLOCKED ; E(TEST-1834) vide |
| TEST-1835 ; REQ-1804 ; FEAT-007 ; P0 ; unitaire, intégration, sécurité | R3 ; D-MEDIA | Images bénignes : MIME incohérent, GPS fictif, limites N-1/N/N+1, fichier corrompu | Uploader, annuler, retraiter, demander original/variantes avant validation | Type/taille/quotas contrôlés, métadonnées selon politique, isolation du traitement, aucun fichier refusé accessible publiquement | BLOCKED ; E(TEST-1835) vide |
| TEST-1836 ; REQ-1805 ; FEAT-019 ; P0 privacy / P1 mesure ; intégration, data | R7 ; D-DATA, D-OBS | Événements avec canaris de texte privé et secret fictif ; horloge fixée | Capturer événements/logs, rejouer doublons, refuser/retirer consentement si applicable | Champs permis seuls collectés ; canaris absents ; définitions/dédoublonnage conformes ; conditions de collecte respectées | BLOCKED ; E(TEST-1836) vide |
| TEST-1837 ; REQ-1806 ; FEAT-021 ; P1 ; frontend, API, localisation | R5 ; D-UX, D-DATA | Pays légal/résidence, communauté/origine/langue distincts ; Unicode long ; locales/fuseaux retenus | Parcourir inscription/signalement/recours ; afficher dates et basculer locale | Aucune confusion entre attributs ; actions accessibles ; formats/libellés et contenu utilisateur préservés | BLOCKED ; E(TEST-1837) vide |
| TEST-1838 ; REQ-1807 ; FEAT-006, FEAT-007, FEAT-011, FEAT-014, FEAT-016 ; P0 ; intégration, résilience | R4 ; D-API, D-OPS | Événement dupliqué, ancien, hors ordre ; worker interrompu | Rejouer, redémarrer, provoquer expiration des retries | Invariants conservés, pas de double effet ou restauration d’état ancien ; échec observable et reprise autorisée | BLOCKED ; E(TEST-1838) vide |
| TEST-1839 ; REQ-1808 ; Socle installation du MVP ; P0 ; installation | R8 ; D-OPS, D-BUILD | OS/CPU supportés décidés, machine vierge isolée, artefact identifié, secrets test hors dépôt | Suivre seulement le guide retenu, initialiser/migrer puis smoke ; répéter depuis une machine propre | Installation reproductible, versions/config documentées, aucune dépendance locale cachée ni compte dangereux par défaut ; commandes prouvées | BLOCKED ; E(TEST-1839) vide |
| TEST-1840 ; REQ-1809 ; Socle sauvegarde + FEAT-016 ; P0 ; restauration, intégration | R7 ; D-OPS, D-DATA | Backup synthétique DB/médias/config, clés test séparées, état attendu, RPO/RTO reçus | Restaurer isolément, contrôler intégrité/ACL, mesurer perte et durée ; backup corrompu/clé absente | Objectifs approuvés respectés ; défaut bloquant explicite ; aucune ouverture avant cohérence et réapplication des suppressions | BLOCKED ; E(TEST-1840) vide |
| TEST-1841 ; REQ-1810 ; Socle release du MVP ; P0 ; upgrade, rollback, intégration | R8 ; D-OPS, D-BUILD, D-API | Ancienne/nouvelle release, matrice client/API/DB, migration et plan de récupération reçus | Déployer progressivement, injecter échec, arrêter puis revenir/récupérer selon plan ; smoke des droits | Compatibilité pendant transition, données intactes ; retour impossible déclaré, pas d’inversion aveugle de migration destructive | BLOCKED ; E(TEST-1841) vide |
| TEST-1842 ; REQ-1811 ; FEAT-001, FEAT-006, FEAT-007, FEAT-008, FEAT-013, FEAT-017 ; P0 avant pilote ; performance, charge, sécurité | R9 ; D-LOAD, D-OPS | Volumes/tailles/caches/hotspots/régions du pilote décidés | Charge nominale, pointe, endurance puis saturation contrôlée en staging avec lectures interdites en parallèle | p50/p95/p99, erreurs, ressources, retard jobs et coût par parcours rapportés ; seuils respectés ou FAIL ; droits/intégrité préservés | BLOCKED ; E(TEST-1842) vide |
| TEST-1843 ; REQ-1812 ; FEAT-006, FEAT-007, FEAT-008, FEAT-014 ; P0 ; résilience, intégration | R8 ; D-OPS, D-API | Dépendances identifiées ; pannes DB/stockage/cache/worker injectables isolément | Couper chaque dépendance, observer, rétablir et réconcilier | Mode dégradé explicite ; échec fermé pour autorisation indécidable ; aucune perte/duplication silencieuse ; reprise et alertes | BLOCKED ; E(TEST-1843) vide |
| TEST-1844 ; REQ-1813 ; FEAT-018, FEAT-025 conditionnelle ; P1 ; compatibilité web/mobile, E2E | R5 ; D-UX, D-BUILD | Navigateurs/OS/appareils/API supportés décidés ; permission système refusée si client installé retenu | Parcours critiques sur matrice ; arrière-plan/reprise/rotation selon surface ; ancien client | Compatibilité et limites documentées ; aucune régression d’accès/données au changement de client | BLOCKED ; E(TEST-1844) vide |
| TEST-1845 ; REQ-1814 ; FEAT-001, FEAT-002, FEAT-006, FEAT-013, FEAT-017 ; P0 ; unitaire, API, sécurité | R1 ; D-ACL, D-API | Environnement autorisé ; limites reçues ; payloads inertes injection/CSRF, débit borné | Tester auth, validation/encodage, origine/session selon contrat, limites N-1/N/N+1 | Abus limités sans divulgation ; entrées non exécutées ; reprise après délai prévue ; contrôle serveur vérifié avec 14 | BLOCKED ; E(TEST-1845) vide |
| TEST-1846 ; REQ-1815 ; FEAT-017, FEAT-002 ; P0 ; API, E2E, sécurité | R2 ; D-ADMIN, D-ID | Agent support restreint, MFA/réauth si décidés, dossier non assigné, action sensible | Lire/exporter/escalader dossier, tenter récupération de compte/changement de rôle | Données minimales ; preuve renforcée si exigée ; aucun contournement de récupération ; audit des accès | BLOCKED ; E(TEST-1846) vide |
| TEST-1847 ; REQ-1816 ; FEAT-014, FEAT-017, FEAT-019 ; P0 ; intégration, observabilité | R6 ; D-OBS, D-ADMIN | IDs requête/job/dossier, panne audit, canari secret fictif, alerte test | Suivre action UI vers job, provoquer échec et alerte | Résultat/acteur/motif corrélables ; panne audit selon règle de 14 ; aucun secret ; alerte vers destination test autorisée/runbook | BLOCKED ; E(TEST-1847) vide |
| TEST-1848 ; REQ-1817 ; FEAT-003, FEAT-009, FEAT-010, FEAT-022 ; P1 ; P0 accès ; unitaire, API, frontend, E2E | R2 ; D-UX, D-API, D-ACL | Profils A/B, textes aux limites/Unicode ; fil vide puis rattrapé | Modifier profil/commentaire comme auteur puis tiers, retirer interaction, naviguer fin de fil/préférences | Validation/propriété appliquées ; erreurs/états vides compréhensibles ; choix de lecture/préférence persistants | BLOCKED ; E(TEST-1848) vide |

## Dépendances et transmissions ciblées

Tous les éléments ci-dessous sont **À TRANSMETTRE / réponse NON REÇUE dans ce lot**. Leur publication dans une PR ne prouve pas lecture ou accord des équipes. Le suivi courant demeure au [tableau HQ](../project-governance/coordination-board.md) ; ce lot ne le modifie pas à la place de MASTER.

| ID proposé / code de blocage | Émetteur → destinataire | Question et livrable exact attendu | Tests affectés / conséquence |
| --- | --- | --- | --- |
| INT-1801 / D-COM | 18 → 00/01, avis 09/19 | Ratifier inclusion FEAT, communautés oui/non, client pilote, pays/langues/âge ; décision DEC-0001/0002 avec exclusions | J07 et choix de suite bloqués ; la rédaction des J01–J06 continue |
| INT-1802 / D-ID | 18 → 04/14, avis 15 | Contrat activation/récupération/session : états, preuves, erreurs non divulgatrices, timeout/révocation, MFA interne si retenu | TEST-1801–1804, 1824, 1846 ; oracle identité manquant |
| INT-1803 / D-ACL | 18 → 04/14/15, avis 01/09 | Matrice acteur/action/objet/champ ; effets du blocage et suspension ; délais et point de concurrence des révocations, URLs déjà émises et caches locaux | Tests d’accès négatif et 1832/1834 bloqués ; risque de fuite |
| INT-1804 / D-API | 18 → 04/03, consommateurs 05/06/10 | Contrats versionnés entrée/sortie/erreurs, idempotence et conflits, pagination et départage, retries et événements | Tests API/concurrence/rejeu ; valeurs/commandes exécutables absentes |
| INT-1805 / D-MEDIA | 18 → 08/04, avis 14/15 | Cycle image original/variantes, formats/quotas/limites, scan/validation, métadonnées, purge et délai de révocation | TEST-1805–1809, 1835 ; accès direct et échecs non certifiables |
| INT-1806 / D-DATA | 18 → 15/04, avis 13/14/10 | Inventaire de données pilote ; export, suppression, exceptions/délais, restauration ; accès/rétention des artefacts QA | J06, 1834, 1836/1837, 1840 ; pas de durée juridique inventée |
| INT-1807 / D-TS | 18 → 09/10/15 | Motifs/états, double traitement, décision/effet/notification, recours et règle d’indépendance, capacité humaine/SLA | J04/J05, 1834 ; workflow et readiness humains manquants |
| INT-1808 / D-ADMIN | 18 → 10/14, avis 09/15 | Matrice console : lecture/preuve/action/export/escalade, portée, justification, réauth et révocation ; support récupération | TEST-1819, 1822, 1829, 1846/1847 ; droits opérateurs non approuvés |
| INT-1809 / D-UX | 18 → 02/05/06/16, avis 01 | Écrans/états et messages ; comportement offline/lecture locale ; matrice navigateurs/appareils/lecteurs d’écran/locales ; critères a11y retenus | 1810/1812–1814, 1833/1837/1844/1848 ; validation UX finale bloquée |
| INT-1810 / D-OPS | 18 → 14/03/04 | Staging isolé, guide OS/runtime, backup/restore/RPO/RTO, migrations et rollback, pannes et alertes de test autorisées | 1821/1827, 1838–1843 ; tests d’exploitation bloqués |
| INT-1811 / D-BUILD | 18 → 20/21 | Artefact immuable/commit, instructions et fixtures, manifestes/versions, jobs CI et preuves ; revue indépendante du delta QA | Tous tests applicatifs non exécutables ; revue documentaire peut commencer maintenant |
| INT-1812 / D-LOAD | 18 → 00/14/19/13, avis 03/08 | Profil chiffré pilote : débit/concurrence/mix, taille et nombre d’objets, hotspots, régions, durée ; SLO/coût et critères d’arrêt | TEST-1842 ; mesure possible seulement avec environnement, conformité impossible sans cible |
| INT-1813 / D-OBS | 18 → 13/14/04 | Dictionnaire événements, exclusions/consentement, définitions de cohorte, correlation/audit IDs, comportement sur perte d’audit et runbooks | TEST-1836/1847 ; collecte sûre et alerte à prouver |

## Risques et contradictions relevés

| Famille de test | Référence de risque | Impact / propriétaire | Mesure proposée |
| --- | --- | --- | --- |
| R1 — identité/abus | RISK-1801 proposé | accès indu, récupération ou énumération ; 04/14 | contrats, contrôles négatifs et limites testées |
| R2 — accès secondaires/révocation | RISK-1802 proposé ; lien RISK-0004 HQ | texte/image/dossier exposé ; 04/08/14/15 | mêmes oracles sur tous chemins ; arbitrer délai et copies déjà téléchargées |
| R3 — publication et retry | RISK-1803 proposé | double publication, média refusé visible ; 04/08 | idempotence, états exacts, tests de panne avant/après acceptation |
| R4 — ordre/cohérence | RISK-1804 proposé | contenu manquant/dupliqué, état ancien restauré ; 04/03 | pagination et versioning explicites, rejeu contrôlé |
| R5 — compatibilité/accessibilité | RISK-1805 proposé ; lien RISK-0003 HQ | utilisateurs pilotes exclus ; 02/05/06/16 | matrice réelle, essais clavier/lecteur d’écran et locales |
| R6 — modération/audit/recours | RISK-0002 HQ | abus non traité ou sanction erronée persistante ; 09/10/14 | effets observables, appels, triage humain et astreinte/support selon capacité |
| R7 — données et restauration | RISK-1806 proposé | fuite par export/log ou réintroduction après suppression ; 15/04/14 | inventaire, traces minimisées, restauration isolée avant ouverture |
| R8 — exploitation/release | RISK-1807 proposé | installation non reproductible, mise à jour non récupérable ; 14/20/21 | installation vierge, backups vérifiés et chemin de récupération testé |
| R9 — capacité | RISK-1808 proposé | service inutilisable sous charge du pilote ; 14/19/13/HQ | profil représentatif, seuils approuvés et saturation contrôlée |

Aucune probabilité chiffrée n’est inventée. Impact critique potentiel pour R1/R2/R6/R7/R8 ; ces risques de conception ne sont pas des bugs constatés.

### Écarts par rapport aux notes QA précédentes

| Références à rapprocher | Écart et traitement dans ce delta |
| --- | --- |
| Fondation QA v0.1 de cette discussion, dépendances « 07 Données / Analytics » ; index HQ M0 | Correction locale : Data = 13 ; IA = 07. Produit = 01, UX = 02. À transmettre à 17 pour éviter propagation. |
| Notes QA précédentes « repository/CI non reçus » ; PR nº 2 et stratégie au SHA source | Repository, workflow et validateur sont désormais consultés. Les tests de ce validateur sont distincts des tests applicatifs ; résultats du présent lot dans le rapport lié. |
| Ancienne formulation QA « toutes actions cessent immédiatement après suspension » ; J05/J06 et règles non approuvées | Généralisation retirée : matrice par action, contrat de concurrence/délai, accès au recours/export à décider. Le fichier présent ne promet pas effacement de copies déjà téléchargées. |
| Anciennes familles QA-M0-001…014 ; catalogue et AC-J du dépôt | Nouveaux tests liés aux FEAT/AC existants ; rapprochement ci-dessous. Les anciens IDs restent historiques, aucun PASS transféré. |
| Notes antérieures sur stack et phases ; catalogue HQ actuel | Pas de stack ratifiée déduite des briefs ; FEAT-025 Phase 2 et FEAT-029 Phase 3 restent des propositions. Arbitrage communautés et surface client encore ouvert. |

Rapprochement historique : QA-M0-001 → TEST-1801–1804 ; 002 → 1832/1848 ; 003 → 1805–1809/1835 ; 004 → 1805/1808/1809/1814 ; 005 → 1812 et 1828–1831 si communauté ; 006 → 1815 ; 007 → 1816–1818 ; 008 → 1819–1823 ; 009 → 1834 ; 010 → 1833 ; 011 → 1810 ; 012 → 1811/1812/1848 ; 013 → 1838 ; 014 → 1813/1837/1844.

### Fiche de proposition structurante — DEC-1801 (ID proposé)

| Champ | Proposition pour MASTER |
| --- | --- |
| Objectif | Définir la preuve minimale autorisant l’ouverture du pilote |
| Problème | Une CI documentaire verte peut être confondue avec une plateforme testée ; critères d’accès et récupération encore ouverts |
| Solution candidate | Adopter les gates de la [stratégie existante enrichie](test-strategy.md) : suite applicable figée avant candidat, P0 tous PASS sur artefact identifié, aucun S0/S1 ouvert, reprise et capacité vérifiées |
| Alternatives examinées | GO sur tests documentaires seuls : rejet recommandé, risque applicatif non mesuré. GO au pourcentage global de tests verts : rejet recommandé car masque un échec critique. Pilote réduit : option recevable si MASTER réduit explicitement le périmètre et si les parcours conservés satisfont leurs gates. Aucune alternative déclarée rejetée officiellement. |
| Dépendances | INT-1801 à INT-1813, contrats approuvés du lot et responsable GO nommé |
| Risques | Coût des tests/retard si périmètre trop large ; réduction de périmètre explicite plutôt que dérogation cachée ; propriétaire HQ/18/14/21 |
| Impact business | Fiabilité du pilote et capacité support ; effort QA à estimer après scope, aucun budget promis |
| Impact technique | Traçabilité, environnements isolés, suites négatives et restauration ; aucun choix de stack ou fournisseur |
| Priorité / phase | P0 — préparation MVP ; proposition à valider par HQ avec 14/15/09/21 selon portée |
| Statut / autorité | PROPOSÉ, aucune approbation ; ID à enregistrer/vérifier par HQ/17 avant usage canonique |
| Réexamen / delta | Changement de scope, client, permission, modèle de données ou migration : cibler tests affectés et invalider preuve obsolète. Ratification dans registre HQ puis lien de décision dans stratégie ; pas de changement silencieux. |

## Compte rendu de l’étape

1. **Décisions prises et à valider :** numérotation locale et rapprochement FEAT/AC réalisés ; DEC-1801 et oracles métier soumis à revue.
2. **Livrables :** ce fichier propriétaire ; delta à la stratégie unique ; [rapport de contrôles documentaires](qa-m0-validation.md). Références distantes établies dans la PR de publication.
3. **Tests :** 48 cas applicatifs BLOCKED, aucun exécuté ; contrôles réels distincts consignés dans le rapport. Aucune réussite héritée d’une ancienne conversation.
4. **Questions :** règles/valeurs manquantes et responsables définis dans INT-1801–1813 ; absence de réponse bloque seulement les cas dépendants.
5. **Dépendances :** demandes ciblées À TRANSMETTRE ; publication GitHub ≠ avis spécialisé reçu.
6. **Risques/limites :** couverture documentaire initiale, pas audit exhaustif ; 31 critères reliés ne prouvent ni produit complet ni conformité générale.
7. **Suite/HQ :** faire revoir ce delta par 01/04/09/14/15/17/21 ; intégrer les références livrées au tableau courant, arbitrer DEC-1801 et les décisions de périmètre, puis confier à 20 l’automatisation des seuls lots autorisés.

### Texte à transmettre

**À TRANSMETTRE — 18 → 00 MASTER, 17 et 21.** Réponse M0-TEAM-18 / INT-0008 : matrice de 48 cas proposée au chemin propriétaire, avec 31 liens AC-J, 17 exigences transversales, oracles manquants et preuves attendues. La stratégie existante est enrichie. Examiner le delta GitHub identifié par la PR, les numéros proposés DEC-1801 / INT-1801–1813 / RISK-1801–1808 et les collisions éventuelles entre branches. Aucune approbation de MVP ou preuve applicative ; les contrats et la release restent bloqués sur les dépendances explicites. Merci de transmettre seulement les lignes pertinentes aux propriétaires, puis consigner leurs réponses avec référence ; une publication n’est pas un accusé de réception.
