# Options Créateurs / Monétisation — M0

## Identification et statut

| Champ | Valeur |
| --- | --- |
| Objectif | Définir la valeur créateur avant paiement et comparer les modèles économiques futurs avec leurs prérequis |
| Propriétaire | 12 — Créateurs / Monétisation ; aucune personne GitHub désignée comme approbateur |
| Destinataires | 00, 01, 02, 04, 08, 09, 10, 11, 13, 14, 15, 16, 17, 18, 19, 21 ; 05/06 pour surfaces futures |
| Date / version | 29 septembre 2026 / v0.1 du livrable propriétaire GitHub |
| Révision d'entrée | PR #2, branche documentation/m0-team-coordination, commit dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957 |
| Statut | PROPOSÉ — revue spécialisée et arbitrage HQ attendus ; aucune autorisation d'implémentation |
| Classement | MVP : besoins créateurs via socle commun ; Phase 2 : FEAT-027 ; Phase 3 : FEAT-031 ; International et Long terme décrits séparément |
| Priorité | P0 : clarifier frontières et accès ; P2 : outils et modèles économiques futurs, selon catalogue |
| Périmètre | Publication, audience, communauté, outils professionnels, comparaison économique, accès payant, états et risques |
| Exclusions | Choix PSP, taux adopté, politique juridique finale, code applicatif, schéma DB, collecte activée, contrats API exécutables, paiements réels |

Références lues : [mandat M0-TEAM-12](../teams/work-orders.md), [plan documentaire](../documentation-plan.md), [modèle](../teams/deliverable-template.md), [vision](../product/product-vision.md), [catalogue](../product/feature-catalog.md), [parcours](../product/user-journeys.md), [gouvernance](../governance.md), [registre HQ](../project-governance/decision-register.md), [statut](../project-governance/project-status.md), [stratégie de tests](../quality/test-strategy.md). Les propositions HQ sont examinées comme entrées, pas comme validations des spécialistes.

### État des preuves et réutilisation

| Nature | Fait ou proposition | Conséquence |
| --- | --- | --- |
| CONFIRMÉ | Mandat documentaire M0-TEAM-12 reçu ; publication par branche/PR autorisée par le porteur | Rédaction et soumission autorisées |
| CONFIRMÉ | Le catalogue lu classe FEAT-027 en Phase 2 et FEAT-031 en Phase 3 | Ce sont des classements HQ proposés, pas une roadmap approuvée |
| PROPOSÉ | Créateur au pilote = membre auteur, utilisant FEAT-003 à FEAT-010 et contrôles communs, sans rôle privilégié implicite | Soumettre à 01/14/HQ ; pas de Studio financier au pilote |
| PROPOSÉ | Tester la valeur de l'audience avant la vente ; étudier ensuite l'abonnement puis l'achat unitaire | Séquence à arbitrer, aucune promesse de revenus |
| À VÉRIFIER | Demande réelle, volonté de payer, coûts, pays/âge éligibles, traitement fiscal, règles des stores | Propriétaires 19/13/15/14, 05/06 et HQ |
| NON REÇU | MVP approuvé, contrats applicatifs, avis juridiques spécialisés, fournisseur retenu, devis, résultats utilisateur, preuve d'implémentation | Bloquants du lot concerné, pas de toute la rédaction |

Travaux antérieurs de cette discussion réutilisés : « SOCIAL-NETWORK-12-CREATEURS-MONETISATION-v0.1 » (exploration générale) et « SOCIAL-NETWORK-M0-12-CREATEURS-MONETISATION-v0.1 » (cadrage gratuit). Leur substance utile est intégrée ici pour que GitHub soit autonome. Le premier proposait un MVP web monétisé, 10 % de commission, 25 € de seuil et 30 jours de réserve : **aucun de ces choix n'a été validé**. Le second proposait des métriques légères au pilote ; le catalogue place le Studio FEAT-027 en Phase 2 et la mesure interne FEAT-019 au MVP. Le présent document distingue ces deux surfaces ; une statistique visible par le créateur au MVP reste un arbitrage, pas une extension implicite de FEAT-019.

## Besoin, fonctionnalités et parcours

### Matrice fonctionnelle et phases proposées

Les sous-options de FEAT-031 ne reçoivent pas de nouveaux FEAT : Produit décidera s'il faut scinder le catalogue. P0/P1/P2/P3 expriment une priorité candidate, pas une adoption.

| Référence | Acteur et besoin | Résultat / préconditions | Classe / priorité | Critère de succès à instruire |
| --- | --- | --- | --- | --- |
| FEAT-003/004/006/007 | Auteur : présenter son activité et publier pour la bonne audience | Profil et texte/image ; compte admissible, droits et limites définis | MVP / P0 | Réussite observée de publication et compréhension de visibilité |
| FEAT-005/008/009/010 | Auteur/lecteur : retrouver et discuter les publications | Suivi gratuit et fil chronologique ; règles de blocage applicables | MVP / P0–P1 | Part de publications recevant une réponse utile d'un autre compte |
| FEAT-020 | Animateur : fédérer une communauté | Adhésion et pouvoirs locaux si communauté retenue | MVP conditionnel / P1 | Participation et capacité de modération, sans confondre rôle local et rôle plateforme |
| FEAT-019 | Équipes pilote : mesurer la valeur | Indicateurs internes minimisés et autorisés | MVP / P1 | Décisions de produit étayées, sans activer un Studio par défaut |
| FEAT-027 | Auteur : gérer ses contenus et comprendre ses statistiques | Liste de contenus, mesures définies, filtres et export agrégé permis | Phase 2 / P2 | Tâches accomplies et interprétation correcte des indicateurs |
| FEAT-027, extension à examiner | Auteur : newsletter gratuite et planification | Consentements/délivrabilité et politique de brouillons à définir | Phase 2 / P2 | Envois voulus, désabonnement effectif, pas de divulgation d'e-mails |
| FEAT-028 | Équipe professionnelle : gérer une présence à plusieurs | Délégations explicites et révocables, hors pouvoirs du compte personnel | Phase 2 / P2 | Révocation effective sur chaque accès |
| FEAT-031 | Créateur : abonnement, contenu/newsletter premium, achat unitaire | Modèle vendeur, droits, paiement, taxe, litiges et coûts revus | Phase 3 / P2 | Net compréhensible, droits cohérents, marge contributive viable |
| FEAT-031, options | Créateur : tips et événements payants | Qualification de produit, fraude, délivrance et annulation instruites séparément | Phase 3 / P2 | Paiements et droits/restitutions réconciliés |
| FEAT-030/031 | Créateur/marque : partenariat et partage publicitaire | Règles de transparence, mesure et inventaire éligible validés avec 11/15/09 | Phase 3 / P2 | Revenu calculable et contenu sponsorisé identifiable |
| FEAT-031, extension à examiner | Vendeur : marketplace de biens/services | Nouveau contrat vendeur, logistique et litiges ; périmètre distinct à créer par 01 | Long terme / P3 | Fourniture et remboursement prouvables |
| FEAT-032 + FEAT-031 | Créateur international : recevoir son revenu | Matrice pays/devise/canal/support validée, pas d'ouverture déduite du public universel ou des priorités marketing | International / P1 pour l'ouverture concernée | Flux et support validés pour chaque marché ouvert |

### Parcours P1 — Publier et construire une audience gratuite

User story : « En tant qu'auteur, je veux publier et comprendre qui peut me lire, afin de construire une audience en gardant le contrôle. » Préconditions : FEAT-001/002/004 et limites média validés. Le profil n'accorde aucun droit commercial ni badge d'identité par simple choix du mot créateur.

Nominal : compléter profil → rédiger texte/image et texte alternatif → choisir audience → soumettre → recevoir confirmation → consulter publication et interactions → modifier ou retirer. Le lecteur suit/ne suit plus et interagit selon J02/J03 ; la communauté suit J07 si retenue. Le signalement et le recours reprennent J04/J05 sans circuit privilégié pour auteur populaire.

| État / transition | Règle et effet observable | Échec / reprise |
| --- | --- | --- |
| Vide → saisie → soumission | Vide propose « publier » ; chargement n'est pas un succès | Brouillon local persistant seulement si 15/02 le retiennent |
| Soumission → publié ou échec | Confirmation serveur obligatoire ; média non traité ne doit pas sembler publié | Réseau interrompu : vérifier le résultat de la requête avant répétition selon contrat 04 |
| Publié → modifié/restreint/retiré | Vérifier auteur et version ; propager visibilité aux médias/caches | Conflit concurrent : conserver l'édition, demander de recharger avant écrasement |
| Publié → masqué par modération | État et motif autorisés, lien vers recours | Échec notification distinct de l'application de la décision |
| Compte suspendu/supprimé | Actions selon matrice commune, pas de nouvelle publication si interdite | Recours/export via parcours 09/15, pas de contournement par Studio |

Cas limites : autre auteur, image invalide, session expirée, contenu supprimé entre deux écrans, changement de visibilité pendant commentaire, retrait de rôle communautaire. UX : états textuels annoncés aux lecteurs d'écran, focus sur erreur/action, ordre clavier et libellés traduisibles ; aucune information essentielle seulement en couleur. Erreurs sémantiques candidates : NON_AUTHENTIFIE, NON_AUTORISE, CONTENU_INDISPONIBLE, VALIDATION, CONFLIT_VERSION, LIMITE_ATTEINTE, INDISPONIBILITE_TEMPORAIRE ; codes HTTP et masquage de l'existence d'une ressource à définir par 04/14/15. Journaliser catégorie, résultat et corrélation sans texte privé ni secret.

### Parcours P2 — Creator Studio et statistiques, Phase 2

User story : « En tant qu'auteur, je veux comprendre mes publications et leur réception, afin d'améliorer leur utilité sans dépendre du temps passé. » Préconditions : protocole 13/15 et droit de consultation 14, FEAT-027 arbitré. Nominal : ouvrir ses contenus → filtrer une période → lire métriques et définitions → consulter le détail d'un contenu → exporter un agrégat autorisé.

États : chargement ; disponible avec date de fraîcheur ; aucun contenu ; aucune donnée ; données insuffisantes/masquées ; recalcul ; indisponibilité. Distinguer zéro mesuré, mesure absente et donnée masquée. En cas de panne, afficher indisponibilité ou dernier agrégat autorisé daté, jamais zéro inventé. Modification de filtre crée une nouvelle lecture, pas une nouvelle collecte implicite. Retrait d'un contenu ou changement de droits exige une nouvelle autorisation, même sur export différé. Une délégation retirée bloque lectures futures et liens d'export selon le contrat ; les copies déjà téléchargées ne peuvent être promises effacées.

| Indicateur candidat | Définition / dénominateur | Limite et décision utile |
| --- | --- | --- |
| Audience gratuite | Nombre de relations de suivi actives à l'instant observé | Ni acheteurs ni portée ; exclusions de comptes à valider par 13 |
| Publications suscitant un échange | Publications éligibles avec au moins une réponse d'un autre compte / publications éligibles de la cohorte | Fenêtre, robots et auto-interactions à préciser ; denominator zéro = non calculable |
| Engagement | Interactions qualifiées / impressions éligibles sur même période | À définir avec 13, pas de promesse d'unicité des personnes ni d'équivalence entre actions |
| Conversion future | Premiers achats confirmés / visiteurs éligibles d'offre sur fenêtre et attribution documentées | Phase 3 ; consentement, déduplication et attribution non reçus |
| Revenus futurs | Brut, taxes, frais, commission, remboursements, réserve, disponible et versé séparés | Proviennent des écritures de paiement réconciliées, jamais seulement d'analytics |

Newsletter : consentement éditorial et messages transactionnels distincts à instruire ; désabonnement accessible ; erreurs de délivrance, doublons et rebonds gérés ; aucune adresse lecteur exposée au créateur par défaut. Outils professionnels : délégation FEAT-028 exige identité de l'acteur réel, périmètre et révocation ; pas de partage de mot de passe proposé.

### Parcours P3 — Acheter et recevoir un revenu, Phase 3 exploratoire

User story : « En tant que créateur, je veux connaître ce que chaque vente me rapporte et pourquoi un montant est retenu, afin de gérer mon activité. » Aucun flux ci-dessous n'est autorisé à l'implémentation par ce document.

Nominal proposé : admissibilité pays/âge/statut → vérification adaptée → offre et conditions → prix final et périodicité → confirmation prestataire vérifiée → droit d'accès → écriture financière → réconciliation → solde disponible → versement → relevé. Le choix entre plateforme vendeuse, marketplace et autre modèle contractuel appartient à HQ/15 avec avis financier ; il conditionne taxes, factures et responsabilité des remboursements.

États distincts : vérification NON_COMMENCEE/EN_COURS/ACTION_REQUISE/VERIFIEE/RESTREINTE ; commande CREEE/EN_ATTENTE/CONFIRMEE/ECHEC/ANNULEE ; droit EN_ATTENTE/ACTIF/EXPIRE/REVOQUE ; versement EN_ATTENTE/ELIGIBLE/EN_COURS/VERSE/ECHEC. Remboursement et litige ont leurs propres objets/états : une commande peut être partiellement remboursée puis contestée. Ne pas définir une unique machine qui mélange commande, droit et banque.

Règles candidates : un écran de retour paiement ne vaut pas confirmation ; événement signé et dédupliqué ; répétition ne double ni droit ni versement ; événements désordonnés réconciliés ; changement de prix jamais rétroactif silencieux ; annulation du renouvellement distincte du remboursement ; restauration d'achat mobile à instruire par canal. Timeout = état inconnu à vérifier, pas nouvel encaissement immédiat. Échec de versement n'efface pas le solde. Retenue motivée, portée limitée et réexamen ; pas de confiscation automatique après sanction. Seuil/délai de versement et période de grâce restent à déterminer. Les droits après refund, litige, retrait de contenu ou suspension doivent être définis par produit avant vente.

## Comparaison économique et décision importante

### Options comparées

| Option | Valeur | Coûts / risques à étudier | Données supplémentaires | Avis 12 |
| --- | --- | --- | --- | --- |
| Abonnement créateur | Soutien récurrent et accès continu | Churn, défaut de paiement, support, engagements de publication et coûts de canal | Offre, période, droit, preuve paiement, annulation | Candidat prioritaire à étudier en Phase 3, pas adopté |
| Accès payant unitaire | Achat ponctuel lisible | Faibles paniers, fraude, remboursement, accès après retrait | Commande, objet acquis, droit, preuve de fourniture | Comparer au récurrent avant choix |
| Tips / soutien | Paiement facultatif sans contrepartie annoncée | Coût fixe dominant, auto-achats, fraude, qualification juridique | Montant, bénéficiaire, provenance/preuve restreinte | Étude séparée ; ne pas promettre de déductibilité fiscale |
| Partage publicitaire | Gratuité du contenu pour lecteur | Revenu variable, fraude d'audience, mesure, modération marques, coût commercial | Inventaire éligible et revenu attribuable validés par 11/13/15 | Dépend du produit publicitaire ; aucune rémunération par vue promise |

Le partage publicitaire ne se calcule pas avec un taux annoncé sans définir l'assiette : revenus réellement encaissés éligibles, ajustements, trafic invalide, coûts déduits et période de clôture. Les dons/tips ne sont pas assimilés à un achat ou à un don défiscalisé sans analyse 15. Les partenariats directs demandent d'instruire transparence, contrat, droits de contenu et responsabilité même si la plateforme ne traite pas le paiement. Événements payants : capacité, contrôle d'accès, annulation/report, no-show et reversement après événement à définir séparément.

### Simulation de sensibilité — valeurs fictives, hors taxes, web uniquement

But : rendre visible le coût du support et des médias avant fixation d'un taux. Aucun tarif PSP réel, budget, revenu prévisionnel ou conseil fiscal n'est affirmé. Variables : panier P ; commission candidate c ; frais F ; coût plateforme variable S (média/support/modération) ; perte attendue R. Hypothèse de scénario : frais F à la charge du créateur, S et R à la charge de la plateforme. Net créateur = P × (1 − c) − F. Contribution plateforme = P × c − S − R, avant coûts fixes. Répartition des remboursements/pertes à négocier ; elle change ces résultats.

| Scénario fictif | P | c | F | S | R | Net créateur | Contribution plateforme |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Micro-paiement | 2,00 € | 10 % | 0,30 € | 0,20 € | 0,10 € | 1,50 € | −0,10 € |
| Offre médiane | 10,00 € | 10 % | 0,50 € | 0,60 € | 0,20 € | 8,50 € | 0,20 € |
| Média/support élevé | 10,00 € | 10 % | 0,50 € | 1,10 € | 0,20 € | 8,50 € | −0,30 € |

À c constant, la viabilité dépend de coûts et pertes. Exemple médian : 1 000 € de coûts fixes mensuels fictifs demanderaient 5 000 transactions de même contribution pour couvrir ces seuls coûts, sans démontrer demande ou capacité. Les stores nécessitent une formule séparée selon qui facture, les frais et les taxes ; aucune extrapolation des 8,50 € au mobile. Chiffrage réel attendu de 08/13/14/15/HQ, puis analyse par pays, panier, refund, chargeback et canal. L'ancien triplet 10 % / 25 € / 30 jours reste non adopté.

### Proposition de décision à enregistrer par HQ

ID canonique DEC-XXXX : **à attribuer par HQ**, sans réserver arbitrairement un numéro global. Libellé local : « Séquence de valeur créateur et ouverture de la monétisation ». Statut : PROPOSÉ.

| Champ | Contenu |
| --- | --- |
| Objectif / problème | Apprendre la valeur créateur sans que l'infrastructure financière conditionne le premier pilote social |
| Solution candidate | Socle commun MVP ; outils FEAT-027 Phase 2 ; options FEAT-031 Phase 3 après revue économique et juridique |
| Alternatives, rejet seulement proposé | Paiements dès MVP : ajoute coûts/contrats sans demande prouvée ; tips d'abord : simplicité UX mais pas nécessairement financière ; publicité d'abord : dépend d'inventaire et d'annonceurs |
| Dépendances | 01/19 valeur pilote ; 13 mesure ; 08 coûts ; 11 publicité ; 14/15 sécurité, données et exigences de marché ; 04 contrats |
| Risques | Retard de rémunération pouvant réduire l'intérêt créateur ; tester cette hypothèse auprès de candidats, sans promettre une date |
| Impact business | Besoin de financer le pilote gratuit ; budget maximal et condition d'arrêt à fixer par HQ ; aucune rentabilité déduite de la simulation |
| Impact technique | Pas de PSP/ledger ajouté au socle par anticipation ; futur domaine financier à concevoir avec 03/04 après choix commercial |
| Priorité / phase | P0 pour arbitrage du périmètre M0 ; fonctionnalités selon phases ci-dessus |
| Réexamen / delta | Revoir après retours 19, coût 08/13 et avis 15 ; 01/HQ mettent à jour catalogue/DEC-0002 seulement après arbitrage |

## Permissions, données et contrats

### Permissions candidates à revoir par 14/15 et propriétaires métier

| Acteur | Action / portée | Règle proposée / refus |
| --- | --- | --- |
| Anonyme | Lire profil/contenu | Seulement si politique publique autorise ; aucune métrique privée ni donnée de vente |
| Membre tiers | Lire, suivre, interagir | Droits FEAT-004/012 et modération ; aucune modification de contenu d'autrui |
| Auteur propriétaire | Modifier/retirer son contenu, consulter ses mesures futures | Propriété contrôlée serveur ; rôle créateur n'accorde pas de droit d'export des données lecteurs |
| Membre bloqué/suspendu | Lire/interagir suivant portée de sanction | Appliquer décision approuvée à API/média/export, sans inventer une invisibilité absolue |
| Responsable communautaire | Modérer dans sa communauté | Aucun accès aux finances, données privées ou rôles plateforme par héritage |
| Gestionnaire délégué futur | Outils FEAT-028 limités au périmètre confié | Révocation vérifiée à chaque action ; pouvoirs financiers distincts |
| Support / Finance / modérateur | Dossiers nécessaires au rôle | Support ne modifie pas un compte bancaire ; Finance ne lit pas librement contenu privé ; séparation et actions sensibles à faire revoir |

L'UI masquée ne remplace jamais le contrôle serveur. Pour les futurs exports et paiements, appliquer également le contrôle au démarrage du job et au téléchargement/versement, avec politique précise d'échec en cas de révocation.

### Données et cycle de vie proposés

| Catégorie / origine | Champs minimaux / finalité / visibilité | Stockage et accès proposés | Modification, rétention, export, suppression / sauvegardes |
| --- | --- | --- | --- |
| Profil/contenu, saisis par membre | Référence auteur, texte/image, visibilité, état/version ; publication autorisée | Système commun 04/08, pas de copie créateur ; opérateurs habilités | FEAT-016 et 15 définissent durées, exceptions et restauration ; ne pas réintroduire un objet supprimé |
| Relation de suivi, action membre | Références des comptes et état ; alimentation du fil | Domaine social 04 ; visibilité liste/compteurs à arbitrer par 15 | Suppression et effet blocage définis par 01/09/15 ; export ne révèle pas de données interdites de tiers |
| Agrégats, calcul 13 | Contenu auteur, période, définition/version, valeur, fraîcheur/masquage | Projection 13 ; propriétaire et rôles autorisés, pas d'identité de lecteur | Rétention/agrégation à décider avant collecte ; recalcul/retrait selon 15 ; exports agrégés contrôlés |
| Newsletter, action lecteur | Adresse nécessaire à délivrance, préférence et preuve de choix | Domaine d'envoi futur ; adresse masquée par défaut au créateur | Désabonnement arrête l'usage éditorial concerné ; preuves et sauvegardes selon politique 15 |
| Vérification financière, futur partenaire | Référence et statut nécessaires ; éléments d'identité/fiscaux seulement selon exigence instruite | Stockage spécialisé à étudier, pas de pièce brute dans logs ni analytics ; accès minimisé | Durées et droits par catégorie à vérifier par 15 ; export/suppression ne doivent pas effacer obligations applicables sans examen |
| Transactions et relevés futurs | Montant/devise, frais, taxe, références externes, états, corrections ; explication du net | Source financière 04 à concevoir ; auteur ses relevés, Finance habilitée | Écritures correctives, rapprochement, délais légaux à déterminer ; sauvegardes et reprise testables |

Aucune durée légale, base juridique, catégorie mineur admissible ou donnée obligatoire n'est déclarée validée. 15 doit établir une analyse datée par modèle/pays/canal pour fiscalité, rétractation, déclaration de plateforme, vérification et transferts. Le document reste une demande d'étude, pas une qualification juridique.

### Interfaces : besoins à contractualiser, aucun endpoint officiel créé

Le catalogue ne fournit pas d'ID/version d'API : **NON REÇU**, attribution par 04. Les noms ci-dessous sont des usages, pas un contrat adopté. Aucune stack supplémentaire n'est imposée.

| Interface | Producteur → consommateur ; entrée / sortie candidates | Autorisation / validation / erreurs | Reprise, limites, audit, tests |
| --- | --- | --- | --- |
| Publication commune | 04/08 → 05/06 ; texte, référence média, audience, clé de requête/version → ID, état, version | Session ; auteur et droits courants ; limites 01/08 ; erreurs de P1 | Timeout à fixer ; mutation non répétée aveuglément ; idempotence et concurrence par 04 ; corrélation sans contenu privé ; AC-J02-03/04/05 |
| Lecture mesures, Phase 2 | 13/04 → Studio ; auteur autorisé, fenêtre, métriques permises → valeurs, fraîcheur, masquage | Session et périmètre ; bornes de fenêtre/export à fixer ; refus homogène et absence de fuite | Lecture répétable, backoff borné si temporaire ; quotas/délais à fixer ; version de définition ; test TEST-CRE-0002 proposé |
| Export agrégats, Phase 2 | Studio → job 04/13 → auteur ; filtres → référence/état puis accès sécurisé | Autorisation au lancement et retrait ; liens non permanents ; refus en cas de révocation | Idempotence requête, expiration, nombre simultané à fixer ; reprise sans nouvel export dupliqué ; TEST-CRE-0003 |
| Notifications de paiement, Phase 3 | Fournisseur choisi → domaine financier 04 → droits/relevés | Référence événement/transaction, statut, montant/devise selon contrat futur ; origine vérifiée et correspondance commande obligatoire | Doublons/désordre/retard, réconciliation, retries bornés + revue erreurs ; pas de timeout = échec bancaire ; TEST-CRE-0004/05 |

Compatibilité : évolution versionnée des schémas, définitions métriques et états ; consommateurs n'interprètent pas un état inconnu comme succès. Timeouts, retries, quotas, authentification technique et délai d'invalidation restent des champs ouverts à 04/14 ; l'implémentation de l'interface concernée reste bloquée jusqu'au contrat suffisant. L'export et le paiement ne doivent pas reprendre aveuglément après retrait d'un droit. Défaillance analytics ne bloque pas la publication du socle.

## Acceptation et vérification

Reprendre AC-J02-01 à AC-J02-05, AC-J03-02/03/05, AC-J04-03 et AC-J05-04 pour le parcours créateur commun ; ils restent PLANNED, sans doublon d'ID. Les nouveaux identifiants TEST-CRE ci-dessous sont proposés dans le périmètre équipe 12, unicité à consolider par 17/18.

| Critère | FEAT | Scénario et résultat attendu | Test / type | Statut / blocage |
| --- | --- | --- | --- | --- |
| AC-CRE-01 | FEAT-005/031 | Étant donné un suivi gratuit, consulter le profil ne crée ni dette, ni commande, ni droit payant | TEST-CRE-0001 / API + E2E | PLANNED ; contrat social et produit requis |
| AC-CRE-02 | FEAT-027/019 | Étant donné données absentes ou masquées, ouvrir Studio affiche cet état et jamais un zéro présenté comme mesure | TEST-CRE-0002 / intégration + UI | PLANNED ; définitions 13/15 |
| AC-CRE-03 | FEAT-027/028 | Étant donné un export en attente, retirer la délégation puis demander le fichier refuse l'accès, même par URL directe | TEST-CRE-0003 / API + job | PLANNED ; autorisation et contrat export |
| AC-CRE-04 | FEAT-031 | Étant donné un événement confirmé déjà traité, répéter sa réception ne crée ni double droit ni double somme | TEST-CRE-0004 / intégration financière | PLANNED ; fournisseur/ledger/contrat absents |
| AC-CRE-05 | FEAT-031 | Étant donné une panne après débit inconnu et événements désordonnés, réconcilier produit un état explicable sans nouveau débit aveugle | TEST-CRE-0005 / panne + intégration | PLANNED ; machine d'état et réconciliation |
| AC-CRE-06 | FEAT-031 | Étant donné un remboursement après reversement, une correction et la répartition de perte selon contrat sont visibles sans réécrire la transaction | TEST-CRE-0006 / intégration | PLANNED ; règles financières non approuvées |
| AC-CRE-07 | FEAT-027 | Étant donné un clavier et une lecture assistée, filtrer les mesures et lire une erreur conserve focus et libellés compréhensibles | TEST-CRE-0007 / accessibilité | PLANNED ; design puis application |
| AC-CRE-08 | FEAT-031 | Étant donné une sanction ou annulation, droits, renouvellement et solde suivent chacun leur politique et restent distingués | TEST-CRE-0008 / E2E | PLANNED ; 09/15/04 doivent définir ces règles |

Preuves applicatives : **aucune**, code et environnement non fournis dans ce mandat. Les contrôles du dépôt et calculs de cette contribution sont documentaires ; commandes, résultats et commit publié sont consignés dans la PR. Ils ne prouvent ni sécurité runtime ni conformité financière.

## Dépendances, risques et transmission

IDs globaux INT-XXXX et RISK-XXXX à attribuer/consolider par HQ/17 : les repères T12-D et T12-R ci-dessous sont locaux et ne remplacent pas ces registres.

| Repère local | Destinataire / demande ciblée et pièce attendue | Blocage | État |
| --- | --- | --- | --- |
| T12-D1 | 00/01 : avis sur MVP sans paiements, FEAT-020 et phases FEAT-027/031 ; décision de périmètre | Pilote détaillé ; rédaction indépendante possible | À TRANSMETTRE |
| T12-D2 | 19/01 : entretiens créateurs sur valeur du pilote gratuit et besoins prioritaires ; synthèse anonymisée, sans recrutement automatique | Validation de valeur, pas cadrage documentaire | À TRANSMETTRE |
| T12-D3 | 13/15 : distinguer mesure interne FEAT-019 et données affichées FEAT-027 ; dictionnaire, agrégation, droits, durées | Instrumentation/Studio concernés | À TRANSMETTRE |
| T12-D4 | 08/13/14 : coûts variables par image/vidéo et charge support ; hypothèses et plage de sensibilité | Choix économique futur | À TRANSMETTRE |
| T12-D5 | 11 : assiette partage publicitaire, fraude, partenariats directs ; avis sur tableau d'options seulement | Publicité/partage Phase 3 | À TRANSMETTRE |
| T12-D6 | 15/HQ : modèle vendeur, pays/âge, taxes, déclarations, remboursements et vérification ; matrice juridique datée et propriétaire financier | Toute vente, pas pilote gratuit | À TRANSMETTRE |
| T12-D7 | 14/04/03 : matrice permissions, droits commerciaux futurs, événements/réconciliation ; contrats avant implémentation concernée | Lot technique correspondant | À TRANSMETTRE |
| T12-D8 | 02/05/06 : vocabulaire suivre/payer, états Studio et modèle d'achat par canal ; parcours et contraintes stores à examiner | UI future ; pas décision mobile ici | À TRANSMETTRE |
| T12-D9 | 09/10 : effet sanction/recours sur publication puis offre, renouvellement et solde ; politique et capacité humaine | Pilote pour recours ; commerce ultérieur pour finances | À TRANSMETTRE |
| T12-D10 | 16/15 : matrice d'ouverture pays/devise/langue/support, distinguée des pays d'audience | International commercial | À TRANSMETTRE |
| T12-D11 | 17/18/21 : indexer ce chemin, consolider IDs et reprendre critères, revue indépendante de la PR | Intégration et preuve | À TRANSMETTRE |

| Risque local | Impact / propriétaire | Mesure proposée / état |
| --- | --- | --- |
| T12-R1, lié RISK-0001 | Paiements confondus avec MVP ; 00/01 | Phases explicites, arbitrage séparé ; OUVERT |
| T12-R2 | Coût support/média > commission et solde négatif après fraude ; 00/12/14 | Scénarios puis coûts observés, politique pertes/réserve ; OUVERT |
| T12-R3 | Fuite de contenu/identité par mesure, cache ou export ; 04/13/14/15 | Contrôles cohérents et minimisation ; OUVERT |
| T12-R4 | Dépendance pays/store/PSP rend vente promise impossible ; 15/05/06 | Avis par marché/canal avant activation ; OUVERT |
| T12-R5 | Créateurs peu intéressés par pilote gratuit ; 19/12 | Entretiens et proposition de valeur sans promesse de rémunération ; OUVERT |
| T12-R6 | Suppression/sanction mal conciliée avec finances et recours ; 09/10/15 | États et politiques séparés avant commerce ; OUVERT |

Conflits à arbitrer : première exploration web monétisée vs catalogue Phase 3 ; mini-statistiques créateur MVP proposées antérieurement vs FEAT-027 Phase 2. Aucun conflit entre propriétaires n'est déclaré résolu par cette rédaction. Recommandation : conserver le socle commun au MVP, réserver le Studio à Phase 2 et l'étude commerciale à Phase 3, sans modifier silencieusement catalogue ni registre HQ.

## Compte rendu de fin d'étape

1. **Décisions prises/à valider** : rédaction selon M0-TEAM-12 ; aucun fournisseur, taux, périmètre MVP ou permission adopté. Proposition de séquence et deux écarts soumis au HQ.
2. **Livrables** : ce document et son README propriétaire, publication par branche et PR ; références de commit et URL dans le compte rendu GitHub de la contribution.
3. **Tests** : critères applicatifs PLANNED uniquement. Vérifications documentaires et de calcul exécutées avec résultats dans la PR ; aucune preuve de comportement de l'application.
4. **Questions** : périmètre créateur, métriques visibles, intérêt pilote gratuit, modèle vendeur, coûts et financement ; responsables dans T12-D1 à D10.
5. **Dépendances** : demandes ciblées ci-dessus, toutes À TRANSMETTRE aux discussions ; publication GitHub ne prouve pas leur réception.
6. **Risques** : coûts, fraude, confidentialité, accès et capacité opérationnelle ; simulations fictives et absence de revue spécialisée limitent les conclusions.
7. **Suite/HQ** : examiner les deux écarts, arbitrer phases et collecte avec propriétaires ; 17 indexe, 18 reprend critères, 21 revoit la PR ; 19 prépare validation de valeur avant toute décision commerciale. Aucun merge ni lancement demandé.
