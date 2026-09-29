# Exigences de localisation — Fondation M0

**Delta DIR-012 — 30 septembre 2026 :** correction de positionnement intégrée par 21 sur instruction du porteur. Le public est universel ; les marchés marketing et langues ci-dessous ne sont pas des ouvertures ou traductions approuvées. Les exigences spécialisées restent proposées ; le rapport de validation v0.2 conserve sa portée historique.

## Identification et statut

| Champ | Valeur |
| --- | --- |
| Objectif | Rendre FEAT-021 spécifiable et testable pour le pilote ; préparer FEAT-032 sans ouvrir de marché par défaut |
| Propriétaire | 16 — International / Localisation ; aucun reviewer humain désigné |
| Destinataires | HQ, 01, 02, 03, 04, 05, 06, 09, 10, 13, 14, 15, 17, 18, 19 |
| Date / version | 30 septembre 2026 / v0.3 ; delta DIR-012 sur la contribution de 16 v0.2 |
| Référence Git | PR [#2](https://github.com/yyogas/social-network/pull/2), branche `documentation/m0-team-coordination`, commit `dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957` |
| Entrées | [Mandat M0-TEAM-16](../teams/work-orders.md), [modèle](../teams/deliverable-template.md), [plan](../documentation-plan.md), [vision](../product/product-vision.md), [catalogue](../product/feature-catalog.md), [parcours J01–J07](../product/user-journeys.md), [registre HQ](../project-governance/decision-register.md), [gouvernance](../governance.md) |
| Travail réutilisé | Cadrage de cette discussion du 29 septembre 2026, livrable `SOCIAL-NETWORK-INTERNATIONAL-M0-v0.1.md` ; pas de SHA Git antérieur attribué à cette pièce |
| Statut documentaire | PROPOSÉ — soumis à revue spécialisée et arbitrage HQ ; aucune approbation reçue |
| Implémentation / vérification produit | NON REÇUES ; aucun résultat fonctionnel revendiqué |
| Classement et priorité | FEAT-021 : candidat MVP / P0 ; FEAT-032 : International / P1 ; autres sous-exigences rattachées aux FEAT existantes ci-dessous |
| Périmètre | Langues, écritures, formats, traduction, données et interfaces candidates, disponibilité par pays, support/modération linguistiques et acceptation |
| Dépendances bloquantes | INT-1601 à INT-1606 ci-dessous, selon le lot concerné ; elles n'empêchent pas la rédaction indépendante |

Les identifiants FEAT existants sont conservés. REQ-1601–REQ-1613, AC-1601–AC-1618, TEST-1601–TEST-1618, INT-1601–INT-1608 et RISK-1601–RISK-1603 sont des identifiants **proposés**, à contrôler par 17/HQ lors de l'intégration des branches concurrentes. Les contrôles documentaires sont consignés dans le [rapport du lot](../quality/localization-documentation-validation.md).

## 1. Faits, propositions et preuves manquantes

| Nature | Éléments et portée |
| --- | --- |
| CONFIRMÉ | DIR-001 : société basée en France ; DIR-012 remplace DIR-002 : public universel, peuple kabyle inclus, et priorités marketing mondiales ; DIR-003 précisé. Le mandat direct de l'équipe impose la séparation pays légal / résidence / communauté / origine / langues. Le noyau pilote reste une hypothèse. |
| PROPOSÉ | Combinaisons pays/langues à comparer avec les priorités marketing ; aucune langue principale ou paire français/kabyle présélectionnée ; prise en charge technique de contenus Unicode et mixtes dès le pilote. Aucun classement n'autorise l'implémentation. |
| À VÉRIFIER | Compréhension des langues candidates dans les cohortes ; besoins d'interface et de support des marchés prioritaires ; choix d'écriture ; couverture des polices et technologies d'assistance ; capacités humaines et analyse pays de 15. |
| NON REÇU | DEC-0001/DEC-0002 approuvées, pays ouverts, âge d'accès, glossaires validés des langues retenues, relecteurs, horaires de support/modération, contrats 04, permissions 14/15, implémentation et tests applicatifs. |

Contribution indispensable : garantir la compréhension des actions et des droits dans le périmètre retenu, préserver les textes et identités linguistiques, et fournir à HQ les conditions d'ouverture réellement démontrables. Une langue lisible techniquement n'est pas une interface traduite ni une capacité de modération opérationnelle.

## 2. Pays de recrutement et disponibilité effective

Les priorités marketing ci-dessous sont **CONFIRMÉES par DIR-012**. La disponibilité effective et les langues d'interface restent **NON DÉCIDÉES**. Une campagne dans une région ne prouve ni résidence, ni origine, ni langue individuelle.

| Périmètre marketing | Priorités reçues | Travail de 16/19/15/09/10 avant ouverture |
| --- | --- | --- |
| Pays | États-Unis, Canada, Inde, France, Allemagne, Royaume-Uni, Japon, Chine, Brésil, Argentine, Colombie, Mexique, Algérie, Maroc, Afrique du Sud, Espagne et Australie | Qualifier par marché les besoins linguistiques, textes, support/modération, contraintes et preuves de préparation |
| Régions ou ensembles | Kabylie, monde arabe et Asie | Décomposer les périmètres utiles à la campagne et au service ; ne pas les coder comme pays ou origine utilisateur |
| Monde entier | Tous les autres publics restent inclus | Prioriser la préparation sans promettre une couverture opérationnelle immédiate |

La liste n'est pas un inventaire des langues nationales. Les besoins doivent être établis avec les cohortes et locuteurs concernés. Ni pays de l'entreprise, ni email, ni langue de l'appareil ne prouve la résidence. L'analyse par pays appartient à 15 ; aucun nouvel avis juridique n'est fourni par ce delta.

Pour chaque combinaison **pays × fonction × langue d'interface**, le registre proposé conserve : version, public/âge approuvés, documents utilisateurs, support, modération/recours, avis 15/14, tests 18, décision HQ et procédure de suspension. États : NON ÉTUDIÉ → EN REVUE → PRÊT À ARBITRER → OUVERT, puis SUSPENDU si décision motivée. Le passage à OUVERT exige des preuves nommées ; aucune absence de réponse ne vaut accord. Une suspension d'acquisition ou de publication ne supprime pas automatiquement l'accès aux recours, droits et support des comptes existants.

## 3. Matrice langue / écriture / interface / support / modération

| Candidate | Interface proposée | Contenus utilisateurs | Support | Modération et recours | Preuve actuelle |
| --- | --- | --- | --- | --- | --- |
| Français `fr` ; formats `fr-FR`, `fr-CA` si nécessaires | MVP si retenu pour la cohorte ; sinon International | Unicode ; avec règles communes d'accès | Couverture humaine à nommer | Capacité et procédure à fournir par 09/10 | Aucun parcours complet validé |
| Kabyle `kab`, écriture latine candidate | MVP si retenu pour la cohorte ; sinon International / FEAT-032 | Contenus inclus dans le socle Unicode ; diacritiques conservés | Locuteurs qualifiés à identifier | Expertise du contexte kabyle requise ; réponse NON REÇUE | Aucun glossaire ni relecteur confirmé |
| Écriture tifinagh, corpus à valider avec locuteurs | International ; variante de contenu à examiner dès M0 | Vérification de rendu/édition et assistive ; pas de translittération automatique | À vérifier | Compétence linguistique à établir | Aucun texte d'interface approuvé |
| Anglais `en` ; variantes de format selon besoin | MVP si retenu pour la cohorte ; sinon International | Texte lisible techniquement ; capacité opérationnelle distincte | NON REÇU | NON REÇUE | Candidature seulement |
| Arabe `ar` ; autres variétés sur validation des locuteurs | MVP si retenu avec RTL complet ; sinon International | Texte RTL et mixte à tester dès MVP | NON REÇU | NON REÇUE ; pas d'assimilation des variétés | Candidature seulement |
| Allemand, espagnol, portugais, japonais, chinois (écritures à qualifier), langues des cohortes en Inde et autres marchés | MVP pour les langues effectivement retenues et préparées ; sinon International | Socle Unicode commun | NON REÇU | NON REÇUE | Aucun engagement de support |

Les tags décrivent la langue du contenu ou un réglage, pas la citoyenneté, l'origine ou la résidence. L'orthographe, les variantes et les autonymes du sélecteur exigent une revue humaine dans chaque langue retenue, dont le kabyle s'il est choisi. La langue ne sera pas représentée uniquement par un drapeau.

**Options réexaminées après DIR-012 pour DEC-0001 / DEC-0002 — aucune adoptée :**

| Option | Valeur / coût | Risque et condition |
| --- | --- | --- |
| A — Une langue d'interface choisie selon la cohorte | Moins de chaînes à qualifier ; français ou anglais sont des exemples à comparer, sans choix par défaut | Compréhension de tous les parcours critiques à démontrer ; support/modération des contenus réellement accueillis |
| B — Plusieurs langues ciblées dès le pilote | Couverture de cohortes ou marchés complémentaires ; aucune paire prédéfinie | Glossaires, relecteurs, QA, accessibilité et moyens humains pour chaque langue ; ensemble exact à arbitrer |
| C — Large couverture linguistique et territoriale dès le pilote | Couverture plus vaste conforme à l'ambition mondiale | Charge et coût non démontrés ; capacité réelle, textes, corpus et avis nécessaires avant engagement |

**Recommandation de méthode PROPOSÉE :** 01/19 établissent les besoins dans les marchés prioritaires ; 16 compare A/B/C avec 09/10/15 et propose un ensemble testable au HQ. La recommandation antérieure français puis français/kabyle est retirée comme défaut. Une cohorte sans langue de service compréhensible ne devient pas admissible faute de moyens. Le public universel n'impose pas une interface unique ni une langue à une personne.

## 4. Fonctionnalités, règles et parcours détaillés

Toutes les lignes sont PROPOSÉES. Les exigences sont des subdivisions des FEAT existantes, pas de nouvelles fonctionnalités inscrites au catalogue.

| Exigence / rattachement | Phase / priorité | Acteur, problème et préconditions | Parcours normal et résultat observable |
| --- | --- | --- | --- |
| REQ-1601 / FEAT-021, J01 | MVP / P0 | Visiteur ou membre ; comprendre le service ; catalogue de langues publiées et langue de secours approuvés | Ouvrir le sélecteur accessible avant inscription → choisir → prévisualiser → appliquer ; aucune modification automatique de résidence/origine/communautés |
| REQ-1602 / FEAT-021, FEAT-011, J01/J04/J05/J06 | MVP / P0 | Membre ou agent ; libellés de sécurité compréhensibles ; messages approuvés | Afficher formulaire, validation, erreur, accusé et décision dans la langue disponible ; conserver la référence de dossier et les liens utiles lors d'un changement de langue |
| REQ-1603 / FEAT-003/006/007/010/021, J02/J03 | MVP / P0 | Auteur/lecteur ; préserver textes, noms et texte alternatif ; limites de contenu à définir par 01/04 | Saisir → prévisualiser → publier → lire/copier/modifier du kabyle latin, français, RTL et texte mixte sans corruption ni réécriture linguistique silencieuse |
| REQ-1604 / FEAT-021, FEAT-008/011, J03/J05 | MVP / P0 | Membre/agent ; interpréter heure et échéance ; fuseau connu ou explicitement inconnu | Choisir fuseau et format → afficher heure localisée avec détail absolu ; l'ordre du fil dépend de l'instant serveur, pas de la chaîne affichée |
| REQ-1605 / FEAT-021, FEAT-013/014/015/017, J04/J05 | MVP / P0 | Signalant, personne sanctionnée, opérateur ; comprendre et contester ; procédure Safety approuvée | Signalement dans sa langue → reçu réel → routage par compétence → examen → motif compréhensible et recours ; traduction de travail clairement marquée |
| REQ-1606 / FEAT-021, FEAT-004/016, J01/J06 | MVP / P0 | Membre ; préférences indépendantes et minimales ; règles Privacy validées | Choisir langue sans devoir déclarer origine ; consulter/modifier/exporter ses préférences selon contrat ; suppression intègre préférences et copies dérivées |
| REQ-1607 / FEAT-021, FEAT-018 | MVP / P0 | Membre utilisant clavier, lecteur d'écran ou zoom ; ressources et composants adaptés | Langue et direction du document déclarées ; passages de langues connus balisés ; navigation et focus maintenus après changement ; noms/URLs mixtes isolés |
| REQ-1608 / FEAT-023, socle FEAT-021 | Phase 2 / P1 ; préparation Unicode MVP | Lecteur ; retrouver du contenu accessible malgré formes Unicode équivalentes ; moteur et droits à définir par 04 | Requête → normalisation de comparaison → résultats autorisés → extrait fidèle à l'original ; pas de translittération ni suppression générale des accents par défaut |
| REQ-1609 / FEAT-032, avec 07 | International / P1 | Lecteur/auteur ; comprendre une autre langue ; prestataire, droits et Privacy approuvés | Demander traduction → attendre → lire résultat marqué automatique → voir original → signaler erreur ; modification/retrait de l'original invalide les dérivés |
| REQ-1610 / FEAT-032 | International / P1 | Membre d'une nouvelle cohorte ; interface RTL complète et opérations locales | Qualification linguistique/UX/Safety/Privacy/QA → décision HQ → activation contrôlée → suivi ; fermeture ciblée et reprise documentées |
| REQ-1611 / FEAT-030/031, extension FEAT-032 | Phase 3 / P2 ; extension International | Client/créateur/annonceur ; comprendre montant/frais ; modèle économique approuvé | Afficher devise et total réellement débités, frais et conversion éventuelle avant confirmation ; codes monétaires explicites ; devise locale ne prouve ni résidence ni admissibilité |
| REQ-1612 / FEAT-020/032, avec 19 | International / P1 ; communautés MVP conditionnelles | Membre/animateur ; trouver contenu local choisi ; FEAT-020 à arbitrer | Choisir communautés/intérêts et préférences de contenu ; quitter ou réinitialiser ; aucune adhésion imposée à partir du pays ou de l'origine |
| REQ-1613 / FEAT-032, avec 07/08 | Long terme / P3 | Créateur/lecteur ; traduction audio/vidéo et variantes avancées | Besoin, benchmark humain et coûts avant proposition de pipeline ; aucun service, fournisseur ni modèle décidé ici |

**Notifications et formats de message :** ressources complètes avec paramètres typés, pluriels et contexte ; éviter la concaténation de fragments. Une valeur fournie par un utilisateur reste du texte échappé, jamais une clé de traduction ou du balisage exécutable. Les codes métier restent stables et ne sont pas traduits par le serveur à la place de leur identifiant. Choix du format et de la bibliothèque par 03/04/05/06.

**Traductions absentes :** préférence explicite valide → variante compatible validée → langue de secours approuvée et annoncée. Ne pas tronquer arbitrairement un tag ni afficher une clé technique. Avant activation d'une locale, 100 % des chaînes des parcours critiques doivent être revues humainement et les éléments non critiques manquants listés. Si un message critique manque à l'exécution, utiliser une version humaine approuvée disponible, indiquer sa langue et maintenir l'accès au support/recours ; ne pas fabriquer une traduction juridique. Un défaut de traduction n'annule pas un signalement reçu. Les variantes signées/versionnées des documents utilisateurs restent rattachées à leur version source.

## 5. États, transitions, erreurs et limites

Les codes ci-dessous sont des raisons candidates à normaliser par 04, pas des codes HTTP approuvés. Les durées et quotas des contrats restent à recevoir ; aucun délai de recours n'est fixé ici.

| Cas / exigences | Transition et comportement | Reprise, annulation et trace minimale |
| --- | --- | --- |
| Initial / préférences absentes — 1601/1606 | Suggestion de langue de l'appareil, explicite et corrigeable ; aucun profil géographique créé | Annuler garde la langue active ; stockage visiteur à arbitrer 15 |
| LOCALE_UNAVAILABLE — 1601/1602 | Langue demandée non publiée ou retirée → choix disponibles et secours annoncé | Ne pas promettre l'activation ; journal technique code/version, sans origine personnelle |
| LANGUAGE_SAVE_FAILED — 1601/1606 | Sélection → enregistrement → échec réseau : distinguer aperçu local et préférence confirmée | Réessayer sans doublon ; annuler restaure la valeur confirmée ; indicateur de sauvegarde seulement après reçu |
| PREFERENCE_CONFLICT — 1601/1606 | Deux appareils modifient la même révision → conflit explicite, valeur courante relue | Choisir et soumettre à nouveau ; pas d'écrasement silencieux |
| RESOURCE_LOAD_FAILED — 1602/1607 | Chargement de catalogue → échec : paquet de secours compatible si disponible | Sinon écran minimal approuvé avec reprise et support ; ne pas exposer une pile d'erreur |
| MESSAGE_MISSING / stale — 1602 | Texte absent ou version incompatible → repli approuvé et diagnostic | Événement clé/version/locale sans payload de contenu ni secret ; correction éditoriale versionnée |
| TEXT_INVALID / TEXT_TOO_LONG — 1603 | Entrée illisible ou hors limites → refus précis ; texte valide conservé dans l'éditeur selon politique de brouillon | Distinguer budget en octets côté service et longueur perceptible côté UI ; valeurs numériques à décider par 01/04 |
| TIMEZONE_INVALID — 1604 | Identifiant de zone invalide → proposition de correction ; sans zone fiable afficher UTC explicitement | Ne pas convertir un décalage fixe en pays ; heure absolue disponible même si affichage relatif |
| CONTENT_UNAVAILABLE — 1608/1609 | Source retirée, accès perdu, blocage ou sanction → refus d'extrait/traduction | Invalidation et recontrôle d'accès côté service ; aucune résurrection par cache |
| TRANSLATION_FAILED / UNSUPPORTED — 1609 | Attente → erreur : original disponible seulement si encore autorisé | Réessayer sur action explicite ; ne pas remplacer l'original ; annulation d'affichage n'implique pas effacement fournisseur |
| LANGUAGE_REVIEW_REQUIRED — 1605 | Langue inconnue/mixte ou compétence indisponible → escalade, état de traitement exact | Conserver accusé et dossier ; pas de rejet automatique des alertes graves ; 09 fixe le délai/escalade et son effet sur l'ouverture |
| UNAUTHENTICATED / FORBIDDEN — transversal | Session expirée, suspension ou rôle retiré → action refusée selon sa portée | Langue ne confère aucun droit ; les chemins de recours/récupération définis par 09/14/15 restent accessibles |

Réseau lent : montrer attente et possibilité d'annulation sans annoncer de succès. Libellé long : retour à la ligne et focus visible, jamais masquage de l'action critique. Unicode : pas de compteur supposant qu'un octet ou un point de code équivaut à un caractère perçu ; ne pas couper une séquence combinée/emoji. Formes NFC équivalentes utilisables pour la comparaison sans réécrire le contenu source à l'insu de l'auteur. Pas d'assimilation automatique des homographes entre écritures ; l'unicité des identifiants et la défense contre l'usurpation appartiennent à 14/04.

RTL : isoler le sens des contenus et noms dans une interface LTR ; tester chiffres, ponctuation, URL et boutons adjacents. Une interface RTL complète relève de REQ-1610, mais le contenu RTL ne doit pas casser les actions MVP. Les contrôles bidi suspects doivent être signalés ou présentés de manière sûre aux agents selon revue 14, sans bannissement général des langues qui utilisent des marques directionnelles.

## 6. Exemples synthétiques et glossaire initial

| Exemple | Usage / attendu proposé |
| --- | --- |
| `é` (U+00E9) et `e` + U+0301 | Comparaison NFC équivalente ; affichage correct ; source et politique de normalisation documentées |
| `ḍ ḥ ṛ ṣ ṭ ẓ č ǧ ɣ ɛ` | Jeu de caractères de test pour écriture latine kabyle, non alphabet exhaustif approuvé ; aucun glyphe manquant |
| `ⴰ ⵣ ⵢ` | Échantillon graphique tifinagh ; pas une traduction validée |
| `مرحبا — profil 123` | Sens et ponctuation isolés ; aucun déplacement trompeur du bouton de signalement |
| `👩🏽‍💻` | Édition et troncature respectant la séquence ; limites techniques distinctes et explicites |
| `2026-09-29T15:00:00Z` | Même instant : Paris 17:00, Alger 16:00, Toronto 11:00, Londres 16:00 selon données de zone consultables ; zone incluse au détail |
| `2026-10-25 02:30 Europe/Paris` | Exemple futur de saisie locale ambiguë : demander l'occurrence/décalage ; jamais utilisé seul comme instant de décision |
| `1 234,50` / `1,234.50` | Formats français/anglais illustratifs d'une même valeur ; données numériques non stockées sous forme de texte localisé |
| `12,00 EUR` / `12.00 USD` | Montants fictifs, distincts ; aucun taux, prix ni devise de paiement adopté |

Fuseaux proposés : identifiants de zones IANA et instant UTC pour événements horodatés ; une date civile (par exemple une date de naissance si 15 en valide la collecte) conserve sa nature de date sans conversion automatique en minuit UTC. Les événements futurs récurrents, s'ils sont retenus plus tard, nécessiteront un contrat séparé. Versions de données de fuseaux et de formats à fixer par 03/04 et actualiser de manière testée.

| Terme français source | Sens produit à conserver | Risque / propriétaire de validation |
| --- | --- | --- |
| Suivre | S'abonner aux publications selon droits applicables | Différent d'un abonnement payant ; 01 |
| Communauté | Espace d'échange à adhésion volontaire | Ni nationalité ni origine supposée ; 01/09 |
| Bloquer | Appliquer les restrictions définies au compte visé | Ne pas promettre invisibilité absolue ; 09 |
| Signaler | Transmettre un incident à examiner | Ne signifie pas que le contenu est supprimé ; 09 |
| Contester une décision | Ouvrir la voie de recours prévue | Motif et référence conservés ; 09/15 |
| Public / audience | Personnes autorisées à accéder au contenu | « Public » ne signifie pas propriété publique ; 01/15 |
| Pays de résidence | Pays où la personne déclare résider | Ni pays légal du service ni origine ; 15/16 |
| Région d'origine | Indication culturelle facultative si retenue | Collecte non autorisée par ce glossaire ; 15 |
| Langue de l'interface | Langue des commandes et messages du produit | Indépendante des contenus ; 02/16 |
| Traduction automatique | Version générée, susceptible d'erreurs | Original et signalement accessibles ; 07/16 |
| Retirer une publication / supprimer un compte | Deux opérations et cycles distincts | Effacement immédiat non promis ; 01/15 |

Les traductions kabyles, arabes et autres du glossaire sont **NON REÇUES**. Le livrable définit les sens à traduire ; il ne publie pas de terminologie inventée. Chaque entrée traduite devra porter langue/écriture, contexte, version source, traducteur habilité, relecteur et date. Une chaîne critique modifiée revient en revue. Le travail automatisé peut proposer un brouillon, jamais attester la validation humaine.

## 7. Permissions, données et cycle de vie

### Matrice d'autorisation candidate

| Acteur | Action et portée | Contrôle / refus attendu |
| --- | --- | --- |
| Anonyme | Lire catalogue public de langues et documents publiés ; choisir une langue locale | Pas d'accès à une préférence de compte ni au registre interne des pays |
| Membre propriétaire | Lire/modifier ses préférences autorisées | Contrôle de sujet côté service ; validation de valeurs et révision |
| Autre membre, y compris bloqué | Lire uniquement les champs rendus visibles par la politique du profil | Pas de fuite d'origine, résidence ou préférences privées ; langue d'affichage sans effet sur ACL |
| Compte suspendu | Comprendre la décision et utiliser les voies permises de recours/droits | Adapter la langue du parcours sans rétablir le droit de publier ; règle exacte à revoir 09/14/15 |
| Traducteur / relecteur | Travailler sur ressources produit autorisées | Aucun accès aux messages privés ni aux dossiers de modération par simple rôle linguistique |
| Modérateur / support | Accéder à un dossier et aux éléments nécessaires selon habilitation | Compétence linguistique ne confère pas une permission ; retrait de rôle prend effet côté service |
| Responsable publication linguistique | Publier/revenir à un paquet approuvé | Permission et audit à valider par 14 ; pas d'auto-approbation implicite d'un texte juridique |
| Responsable ouverture territoriale | Activer une combinaison approuvée | Preuve de décision HQ et contrôles métier ; pas de pouvoir implicite du traducteur |

### Données minimales proposées

| Catégorie / origine | Champs candidats et finalité | Visibilité, accès et propriétaire | Cycle de vie à contractualiser |
| --- | --- | --- | --- |
| Préférences explicites | Langue UI, locales de format si distinctes, fuseau, langue de communication, langues de contenu optionnelles, révision | Privées par défaut proposé ; compte propriétaire ; 01/04, revue 15 | Modifier séparément ; export et suppression avec compte ; historique non justifié par défaut ; session visiteur/persistance à arbitrer |
| Pays légal du service | Entité contractante et version d'offre/règles | Configuration de service, pas champ culturel du profil ; 15/HQ | Historique requis pour documents/transactions uniquement selon analyse 15 ; pas de duplication par utilisateur sans nécessité |
| Résidence / origine | Résidence déclarée seulement si finalité démontrée ; origine non collectée au pilote recommandée | Séparation conceptuelle confirmée, collecte PROPOSÉE/À VALIDER ; 15/01 | Ne pas créer de champs persistants « au cas où » ; effacement/export/rectification si retenus ; accès et rétention explicités par 15 |
| Communautés | Identifiants et état d'adhésion si FEAT-020 retenue | Politique de visibilité propre à la communauté ; 01/09 | Départ, suppression et visibilité sans déduction ethnique ; jamais alias du pays |
| Contenu source | Texte/texte alternatif et éventuelle langue déclarée ; langue inconnue/mixte admise | Audience de l'objet ; 01/08/04 | Aucun contenu brut dans métriques de locale ; correction auteur ; suppression et caches alignés sur source |
| Ressources éditoriales | Clé, langue, direction, paramètres, version source/cible, validation, périmètre et secours | Publiées ou internes selon rôle ; 02/16 avec 09/15 pour textes sensibles | Historique versionné, remplacement et rollback ; preuve de qui a relu ; pas de données d'utilisateur |
| Dossier Safety / traduction future | Référence de source/révision, langue, accès, provenance humaine/automatique et état | Accès du dossier ou du contenu ; 09/15/07 | Version dérivée invalidée si source change ou droits retirés ; contrat fournisseur et suppression à définir avant appel |
| Diagnostics | Code d'erreur, clé de ressource, version, locale technique, corrélation restreinte si nécessaire | Exploitation limitée ; 14/13/15 | Pas de texte privé, IP ou origine ajoutés au diagnostic de traduction ; rétention chiffrée NON REÇUE, condition avant instrumentation |

Recommandation de minimisation à arbitrer : conserver au pilote les réglages nécessaires au service, sans demander la région d'origine pour accéder au réseau. Les brouillons, caches de traduction, index et sauvegardes doivent suivre les règles d'effacement de leurs objets ; une restauration ne doit pas réintroduire une donnée supprimée. Aucune durée légale ou technique n'est décidée par 16. Les préférences ne deviennent pas automatiquement des signaux publicitaires, d'identité ou de recommandation.

## 8. Interfaces candidates à remettre à 04

Inventaire sémantique, version de proposition 0.1. Aucun endpoint, table, migration ou bibliothèque n'est imposé. Le contrat de 04 doit fixer tailles maximales, timeouts numériques, quotas et codes HTTP avant implémentation ; les valeurs sont **NON REÇUES**, propriétaire 04 avec 14. Pas de nouvelle famille d'API canonique : références locales C-LANG, C-PREF et C-NOTIF rattachées à FEAT-021.

| Élément | C-LANG — capacités linguistiques publiées | C-PREF — préférences personnelles | C-NOTIF — message localisé métier |
| --- | --- | --- | --- |
| Producteur → consommateur | Ressources validées de 02/16 via service 04 → 05/06/10 | Client 05/06 → service 04 ; état confirmé → client | Événement métier 04/09 → notifications 04 → membre/agent autorisé |
| Authentification / autorisation | Lecture publique d'un sous-ensemble publiable ; écriture interne habilitée | Session et sujet authentifiés ; protections CSRF selon transport ; état suspendu selon matrice | Producteur interne authentifié ; permissions du destinataire et visibilité revérifiées |
| Entrée minimale | Version connue, locale demandée facultative | Lecture : soi ; écriture : champs explicitement modifiés et révision attendue | Référence/version de l'événement, clé stable, paramètres typés minimaux, destinataire autorisé, référence de source |
| Sortie minimale | Version, locales sélectionnables, direction, secours validés, état de disponibilité | Valeurs effectives et nouvelle révision ; absence distincte de null/effacement | État de livraison, référence et langue/version rendue ; succès métier distinct du succès de notification |
| Validation | Tags connus et combinaisons publiées ; aucune origine/résidence | Liste de locales, zone valide, limites de liste/tailles, refus de champs inattendus | Paramètres attendus, clé/version valide, audience, échappement, pas de HTML utilisateur |
| Erreurs | LOCALE_UNAVAILABLE, RESOURCE_LOAD_FAILED | UNAUTHENTICATED, FORBIDDEN, TIMEZONE_INVALID, PREFERENCE_CONFLICT, erreur de validation/réseau | MESSAGE_MISSING, contenu inaccessible, destinataire invalide, échec de livraison |
| Timeout / reprise | Deadline finie ; dernier catalogue compatible ou secours embarqué ; aucun retry infini | Timeout : état incertain, relire la révision ; écriture conditionnelle ; pas de retry aveugle après conflit | Retry borné avec déduplication ; file d'échec à opérateur ; pas de sanction réappliquée pour renvoyer le message |
| Idempotence / concurrence | Lecture idempotente, version du paquet cohérente ; cache par version/locale | Révision attendue évite l'écrasement ; repetition détectable ou conflit explicite suivi d'une relecture | Clé de déduplication événement/destinataire/canal ; politique de locale figée par tentative, à fixer par 04 |
| Limites / audit | Réponse publique sans notes internes ; quotas 04/14 à fixer ; trace de publication | Aucun champ privé dans cache partagé ; audit minimal de modification selon 14/15 | Pas de corps sensible dans logs ; corrélation au dossier avec accès limité |
| Compatibilité / rollback | Ajouter une locale sans changer sa sémantique ; retirer avec secours ; clients anciens tolèrent métadonnées additives | Version de schéma explicite ; pas de conversion de résidence en locale ; ancien client conserve les champs non modifiés | Templates compatibles avec paramètres ; changement incompatible versionné ; traduction obsolète repasse en revue |
| Tests prévus | TEST-1601/1602/1614/1615 | TEST-1603/1604/1609/1610/1617 | TEST-1602/1608/1616 |

C-PREF ne doit pas devenir un contrat de géolocalisation. C-NOTIF consomme la langue de communication retenue ; changer la langue ne renvoie pas tous les anciens messages. Aucun envoi de contenu privé à un service de traduction au MVP : éventuelle exception à proposer séparément à 07/14/15 et HQ avec finalité, flux et protections.

## 9. Acceptation et vérification à préparer avec 18

Tous les tests fonctionnels suivants sont **PLANNED** ; aucune exécution applicative n'a eu lieu. QA confirme les IDs avant intégration. Préconditions générales : périmètre HQ, rôles et contrats approuvés, implementation testable et corpus humain revu. Les types sont proposés et les observations demandées, pas des preuves déjà disponibles.

| Critère | Besoin | Étant donné / lorsque / alors | Test / type | Statut ; responsable ou blocage |
| --- | --- | --- | --- | --- |
| AC-1601 | REQ-1601 | Langue publiée ; le visiteur la choisit ; commandes changent sans affecter pays/origine/communauté | TEST-1601 / E2E | PLANNED ; 02/05/18, locales non décidées |
| AC-1602 | REQ-1602 | Chaîne critique manquante ; parcours sécurité ouvert ; secours humain annoncé, dossier et recours accessibles, aucune clé brute | TEST-1602 / intégration + UX | PLANNED ; 09/10/15/18, contenus non reçus |
| AC-1603 | REQ-1601/1606 | Sauvegarde interrompue ; reprise ; état local distingué du confirmé et une valeur effective après relecture | TEST-1603 / API/E2E réseau | PLANNED ; 04/05/18, contrat ouvert |
| AC-1604 | REQ-1606 | Deux appareils même révision ; écritures concurrentes ; conflit explicite sans écrasement silencieux | TEST-1604 / API concurrence | PLANNED ; 04/18 |
| AC-1605 | REQ-1603/1607 | Corpus combiné/diacritiques/emoji/RTL ; publication/édition ; texte lisible, pas de glyphe manquant ni troncature interne de séquence | TEST-1605 / E2E manuel + unités | PLANNED ; 02/04/05/06/18, corpus humain requis |
| AC-1606 | REQ-1604 | Même instant dans Paris/Alger/Toronto ; changement de fuseau ; ordre chrono inchangé et absolu correct | TEST-1606 / unités/intégration | PLANNED ; 04/18, versions de zones à fixer |
| AC-1607 | REQ-1604 | Zone invalide ou absente ; affichage ; correction ou UTC explicitement indiqué, aucune résidence inférée | TEST-1607 / API/E2E | PLANNED ; 04/05/18 |
| AC-1608 | REQ-1605 | Dossier en langue inconnue ; signalement reçu ; référence conservée et escalade réelle sans succès d'examen fictif | TEST-1608 / intégration + exercice humain | PLANNED ; 09/10/18, capacité NON REÇUE |
| AC-1609 | REQ-1606 | Un tiers appelle C-PREF ; lecture/écriture ; refus et absence de préférences privées | TEST-1609 / API permissions | PLANNED ; 04/14/15/18 |
| AC-1610 | REQ-1606 | Compte exporté/supprimé selon politique ; traitement et restauration ; préférences incluses et pas de réintroduction interdite | TEST-1610 / intégration/recovery | PLANNED ; 04/14/15/18, politique non reçue |
| AC-1611 | REQ-1607 | Lecteur d'écran/clavier/zoom ; changement de langue ; langue annoncée, focus conservé et actions critiques accessibles | TEST-1611 / accessibilité manuelle | PLANNED ; 02/05/06/18, appareils/AT à sélectionner |
| AC-1612 | REQ-1608 | Formes Unicode équivalentes et texte devenu privé ; recherche ; comparaison prévue et aucun résultat/extrait non autorisé | TEST-1612 / API recherche | PLANNED ; Phase 2, 04/14/18 |
| AC-1613 | REQ-1609 | Traduction en cache ; original supprimé ou accès retiré ; résultat dérivé interdit et original non divulgué | TEST-1613 / intégration permissions | PLANNED ; International, 04/07/15/18 |
| AC-1614 | REQ-1610 | Locale candidate sans revue ; tentative d'ouverture ; activation refusée avec condition manquante | TEST-1614 / release + exercice | PLANNED ; 14/16/18/HQ |
| AC-1615 | REQ-1602/1607 | Changement critique après approbation de ressource ; publication ; nouvelle version non considérée relue automatiquement | TEST-1615 / workflow documentaire | PLANNED ; 02/16/17/18 |
| AC-1616 | REQ-1602/1605 | Compte suspendu ou droit agent révoqué ; UI dans autre langue ; recours autorisé conservé, opération privilégiée refusée | TEST-1616 / API/E2E permissions | PLANNED ; 04/09/14/15/18 |
| AC-1617 | REQ-1606/1612 | Profil sans origine ni langue de contenu ; inscription/adhésion ; ni champ obligatoire caché ni affectation communautaire automatique | TEST-1617 / E2E | PLANNED ; 01/04/15/18, communautés conditionnelles |
| AC-1618 | REQ-1611 | Offre future en devise définie ; confirmation ; total/frais/devise réellement facturés explicites, sans conversion silencieuse | TEST-1618 / E2E finance | PLANNED ; Phase 3, 11/12/15/18 |

REQ-1613 reste une étude Long terme, sans critère d'exécution adopté : livrable requis avant toute implémentation = comparaison besoin/coût/qualité et risques, approuvée par propriétaires. La recherche publique FEAT-023 n'est pas promue au MVP par les tests Unicode ; au MVP on vérifie saisie, stockage, affichage et éventuelles recherches internes déjà retenues.

## 10. Arbitrages, contradictions et delta du cadrage précédent

| Sujet | Constat et références | Proposition / autorité / lot affecté |
| --- | --- | --- |
| Séparation des dimensions | Le brief l'impose ; la réponse précédente la qualifiait entièrement de proposition | Corriger : séparation CONFIRMÉE, collecte et schéma encore PROPOSÉS ; 03/04/15 ; bloque le modèle de profil tant que champs/finalités non décidés |
| Origine facultative « privée par défaut » dans v0.1 | Une possibilité de champ pouvait être lue comme autorisation de collecte | Recommander aucune collecte au pilote sans finalité validée ; option de champ déclaré seulement après arbitrage 15/HQ ; pas de nouveau champ dans ce lot |
| Recherche multilingue | V0.1 évoquait Post-MVP ; catalogue affecte FEAT-023 à Phase 2 | Garder Phase 2 ; qualifier Unicode au MVP. Pas de moteur de recherche imposé ; 01/04/HQ |
| Locale vs ouverture pays | Langues et pays cités dans les deux cadrages ne portent aucune preuve d'ouverture | Conserver cette concordance ; deux matrices distinctes, activation à décider pour DEC-0001/DEC-0002 |
| DIR-012 et anciennes options linguistiques | Le public universel remplace l'hypothèse d'un premier public communautaire ; ni français ni couple français/kabyle ne sont des défauts approuvés | Refaire seulement la comparaison des langues/cohortes A/B/C sur les besoins et capacités ; OPEN-004, 01/16/19/09/10/15 |
| Statut des transmissions | Tableau HQ au SHA source indique M0-TEAM-16 NON REÇU | Le mandat a été reçu dans cette discussion ; publier cette réponse fournit une pièce. 00/17 mettront le tableau à jour sur preuve ; réception des autres équipes toujours NON REÇUE |

**Fiche de proposition liée à DEC-0001/DEC-0002 et OPEN-001/OPEN-004 :** objectif = pilote compréhensible et opérable ; problème = couverture des langues et territoires sans preuve ; solution candidate = option A ou B conditionnelle et registre d'ouverture ; alternatives = C et lancement mondial simultané, report recommandé mais non rejet définitif ; dépendances = INT-1601/1602/1603 ; priorité P0 pour le pilote. Impact business : coûts de traduction/support/recrutement et représentativité de la cohorte, montants NON REÇUS. Impact technique : versionner ressources, préférences et tests, sans imposer stack. Risques : exclusion linguistique, sous-modération et collecte excessive. Réexamen : besoins observés, capacité humaine disponible, nouvelle région/offre, changement de règle ou incident linguistique. Autorité : HQ avec 01/09/15/16/19, avis 02/03/04/14 selon delta. Les décisions finales iront au registre HQ ; aucune nouvelle DEC concurrente créée ici.

## 11. Dépendances et transmissions ciblées

Toutes les demandes ci-dessous sont **À TRANSMETTRE**, réponses NON REÇUES. Une PR rend la pièce disponible ; elle ne prouve pas que les discussions l'ont reçue. Aucun envoi d'invitation, de campagne ni de demande de revue à une personne non identifiée n'est effectué.

| ID | Émetteur → destinataire | Question et livrable attendu ; section à examiner | Bloquant pour |
| --- | --- | --- | --- |
| INT-0009 | HQ → 16 | Demande existante traitée par ce document ; réponse soumise à HQ | Arbitrages pays/langues encore ouverts |
| INT-1601 | 16 → 00/01/19/15 | Quelle cohorte comprend quelles langues, dans quels pays effectivement ouverts ? Fiche cohorte agrégée, avis 15 et décision DEC-0001/0002 ; sections 2–3/10 | Annonce et lancement, pas rédaction |
| INT-1602 | 16 → 09/10/19 | Pour chaque langue de contenu envisagée et les contenus mixtes, qui examine, à quelles plages, avec quel secours ? Matrice de compétence, capacité, escalade/recours ; sections 3/5 | Ouverture d'une cohorte linguistique |
| INT-1603 | 16 → 15/14/01 | Quels réglages sont nécessaires, privés, conservés et exportés ? Avis sur non-collecte de l'origine, suspension et données de diagnostic ; section 7 | Collecte, permissions et instrumentation |
| INT-1604 | 16 → 02/05/06 | Quels écrans/chaînes critiques, polices, locales et technologies d'assistance ? Inventaire de ressources, prototype d'états et relecteurs ; sections 3–6 | Validation d'une langue d'interface |
| INT-1605 | 16 → 03/04/05/06 | Quels contrats remplacent C-LANG/C-PREF/C-NOTIF ; quelles bornes, erreurs et versions ? Contrats producteurs/consommateurs ; section 8 | Implémentation du lot FEAT-021 |
| INT-1606 | 16 → 18 | Quels corpus/appareils et preuves pour TEST-1601–1618 ? Matrice de tests intégrée et critères release ; section 9 | Vérification avant pilote |
| INT-1607 | 16 → 17/00/21 | Intégrer référence, contrôler collisions d'IDs et revoir delta ; actualiser coordination sur preuve ; sections 1/10/11 | Fusion documentaire après revue |
| INT-1608 | 16 → 07/08/11/12/13/15 | Pour phases futures, quels besoins réels de traduction, paiement et métriques de langue ? Deltas ciblés, flux et finalités ; REQ-1609/1611/1613 | Fonctions futures seulement |

## 12. Risques et mesures

| ID / état | Impact et propriétaire | Mesure proposée et limite |
| --- | --- | --- |
| RISK-0001 / rappel ouvert | Gonfler MVP avec langues, recherche et traduction ; 00/01/16 | Respect FEAT-021 vs FEAT-023/032 ; pas de traduction automatique promise au pilote |
| RISK-0002 / rappel ouvert | Abuse mal traité faute de compétence linguistique ; 09/10/16 | Matrice humaine et escalade avant ouverture ; un taux faible de signalement ne démontre rien |
| RISK-0003 / rappel ouvert | Pays annoncé sans capacité locale ; 15/16/19 | Séparer recrutement/disponibilité, avis spécialisé et arrêt ciblé |
| RISK-0004 / rappel ouvert | Clients divergent sur locale, cache ou droits ; 03/04/05/06 | Contrats et fixtures communs avant implémentation |
| RISK-1601 / proposé ouvert | Origine ou communauté inférée et réutilisée ; 15/14/16 | Pas de collecte d'origine par défaut, pas d'inférence ; revue de finalité et autorisations |
| RISK-1602 / proposé ouvert | Corruption Unicode, homographes ou bidi trompeur ; 04/14/16 | Corpus mixte, séparation source/comparaison, revue sécurité des identifiants et affichage |
| RISK-1603 / proposé ouvert | Message critique erroné et perte de recours ; 09/15/16 | Glossaire validé, version source, revue humaine, secours et voies de recours ; aucun substitut à avis juridique |

## 13. Sources techniques et portée

Sources primaires consultées le 29 septembre 2026 ; elles justifient les conventions proposées, pas une validation de stack ni de conformité générale. Pas d'avis juridique fourni par cette équipe.

- [IETF RFC 5646 / BCP 47](https://www.rfc-editor.org/rfc/rfc5646) : tags de langue distincts des attributs d'identité ; variantes d'écriture et de format à qualifier.
- [Unicode UAX #15](https://www.unicode.org/reports/tr15/) : formes de normalisation ; proposition de comparaison NFC et conservation du texte source.
- [W3C — direction du texte HTML](https://www.w3.org/International/questions/qa-html-dir) : direction et contenu mixte ; choix d'implémentation à 05/06.
- [IANA — Time Zone Database](https://www.iana.org/time-zones) : zones et changements de règles ; versions utilisées à fixer par les équipes techniques.

## Compte rendu de fin d'étape

1. **Décisions prises et à valider** : chemin du mandat, réemploi des FEAT et détail local de spécification ; pays, langues, collecte, permissions et contrats restent proposés. Arbitrages liés à DEC-0001/DEC-0002, aucune décision transversale approuvée ici.
2. **Livrables et références** : ce document v0.3 avec delta DIR-012, README propriétaire et rapport de contrôle historique v0.2 ; référence d'entrée PR #2 / SHA ci-dessus. La PR de livraison porte la preuve du commit publié ; pas de fusion ni d'approbation implicite.
3. **Tests exécutés** : voir [rapport documentaire](../quality/localization-documentation-validation.md) et checks de la PR. Aucun test applicatif exécuté ; TEST-1601–1618 restent PLANNED.
4. **Questions ouvertes** : langues comprises dans les cohortes mondiales candidates, couverture humaine, pays/âge, données réellement nécessaires, bornes des contrats, locales/écritures et corpus ; propriétaires dans INT-1601–1608.
5. **Dépendances** : réponses ciblées attendues ; état À TRANSMETTRE aux discussions, pas de réception inventée.
6. **Risques et limites** : sections 10/12 ; revue au SHA source, pas examen de toutes les branches concurrentes ni conformité pays attestée.
7. **Suite / HQ** : recevoir les avis 01/09/15/19, arbitrer pays et options de langues, obtenir contrats/ressources/corpus, actualiser registre et tableau de coordination via 17, revue 21 avant fusion ; lancement/implémentation suivent leurs autorisations propres. Lecture ciblée de ce delta suffisante, pas de réanalyse générale demandée.
