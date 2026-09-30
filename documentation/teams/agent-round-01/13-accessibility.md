# Avis sous-agent13 — accessibilité opérationnelle de L1

**PROPOSÉ, 30 septembre 2026.** Aucun test applicatif, adoption ou clôture L1. Références : HQ `4d3cd079e92217936af3292429a38f91f7b576ff` ; Backend `0a7fcd54b996cc292bfe98c61a835613837def32`, via l’avis Web. Complément W01/W03/W04 et TEST-1813.

Sources lues : `documentation/user-experience/user-journeys.md`, `documentation/web-application/web-requirements.md`, `documentation/international/localization-requirements.md`, `documentation/quality/acceptance-test-matrix.md` et [avis sous-agent 03](03-web.md). Avis 12 non livré à la lecture.

**Critère transversal :** intitulé visible et nom accessible cohérents, explication persistante, commandes clavier. Les annonces décrivent le résultat établi sans secret. Le chargement ne vole pas le focus ; une vue supprimée entraîne son déplacement vers un repère sûr nommé.

| État L1 | Focus et annonce attendus | Nom accessible, clavier et action sûre | Preuve future ciblée |
| --- | --- | --- | --- |
| Connexion : validation refusée | Focus au résumé d’erreurs ; champs invalides reliés à leur explication ; annonce unique. | Libellés persistants ; liens du résumé vers les champs ; soumission clavier. Message sensible conforme à l’anti-énumération. | Parcours clavier et lecteur d’écran avec identifiant fictif existant/inexistant ; aucune distinction interdite. |
| Connexion : réponse perdue | Focus conservé ; « Résultat de connexion inconnu », sans annoncer réussite ou échec. | Action nommée selon la reprise contractuelle ; aucun deuxième login automatique. Observer B ne confirme pas l’intention A. | Perdre la réponse puis recevoir un résultat tardif ; vérifier texte, annonce et absence de double soumission. |
| Ouverture, reload, restauration | État neutre « Vérification de la session » ; repère stable ; panne annoncée comme indisponibilité. | « Réessayer la vérification » accessible ; reprise privée après continuité autorisée seulement. Reload ordinaire ne signifie pas expiration. | Reload, retour navigateur et restauration : aucune apparition privée avant vérification ; focus utile après résolution. |
| Session expirée ou liaison invérifiable | Retirer le privé ; focus sur « Connexion nécessaire » ; annoncer la reprise requise. | « Se reconnecter » et aide au clavier ; retour interne permis ; aucune reprise automatique de mutation. | Expiration pendant saisie et lecture ; vérifier disparition du contenu et destination après réauthentification. |
| Déconnexion demandée, résultat incertain | Retrait privé immédiat ; focus vers notice neutre ; « Déconnexion non confirmée ». | Commandes nommées de reprise autorisée ; ni timeout, ni 401, ni session anonyme observée ne deviennent preuve de révocation. | Perte avant/après réception serveur, reload : masque maintenu selon portée contractuelle ; aucune annonce trompeuse. |
| Changement de compte A→B | Retirer A avant B ; si cible focalisée supprimée, rejoindre le titre sûr de la nouvelle vue. | Navigation et noms sans données de A ; résultat tardif A sans effet sur B. | Lecture continue, recherche dans l’arbre accessible et réponses inversées ; aucun canari de A présent. |
| Compte restreint | Titre et motif communicable ; focus conservé si possible, déplacé hors commande retirée sinon. | Recours, aide et droits sur données seulement selon matrice approuvée ; libellés explicites, aucune publication rétablie. | Retrait de droit pendant interaction ; parcours clavier séparés pour refus, recours et données. |
| Limitation temporaire | Motif et délai serveur éventuel persistants ; éviter annonce répétée chaque seconde. | Action indisponible avec raison accessible ; aide atteignable ; réessai explicite quand permis. | Horloge contrôlée : compréhension sans couleur seule, aucun réessai prématuré ni boucle. |

Le retrait couvre aussi l’arbre accessible : noms, descriptions, textes alternatifs, dialogues, annonces et titres sans contenu privé retiré. Un masque visuel ne prouve jamais le refus serveur ; vérifier séparément affichage, arbre accessible et autorisation des lectures/mutations.

Les messages restent consultables sans prolonger une session expirée ni retarder sa révocation. Aucun délai chiffré inventé. Langue déclarée, secours approuvé, textes longs et mixtes préservent lecture et commandes.

Avant gel : 02/05/16 fixent comportements/messages ; 04/14/15 les reprises/protections ; 18 consigne navigateur/aide technique, étapes, focus, annonces, captures expurgées et résultat. Preuves **PLANNED/BLOCKED** selon dépendances.
