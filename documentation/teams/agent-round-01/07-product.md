# Avis sous-agent 07 — arbitrages Produit pour L1

**30 septembre 2026 — PROPOSITION, sans adoption.** Cet avis indépendant ne remplace pas la contribution du propriétaire 01. Sources : Produit, dossier M0 et registre HQ au snapshot `4d3cd079e92217936af3292429a38f91f7b576ff` ; Backend #28 v0.3 `0a7fcd54b996cc292bfe98c61a835613837def32`, C1–C7 ; Architecture #33 `a7901fc87e79975d8963e909a89fc8150410e40a`, §§2–6/8–9 ; avis sous-agents 03 Web et 06 Architecture.

**Recommandation : conserver la reprise ordinaire comme objectif L1, demander une continuité minimale démontrable, et limiter explicitement « dernier login » à une lignée établie.** La reprise stricte devient le comportement en cas de continuité invérifiable ; elle ne devient pas automatiquement le parcours de chaque rechargement. Ce paquet réduit la portée sans prétendre résoudre le protocole.

DIR-012 confirme un réseau universel dès sa conception, peuple kabyle inclus. Les marchés prioritaires ne fixent aucun pays ouvert ni aucune langue disponible. Le MVP, DEC-0001/0002, A/B et les contrats restent non approuvés.

## Matrice : texte courant et exigence proposée

« Courant » désigne les propositions documentées, sans leur attribuer une approbation.

| Sujet | Exigence courante / manque | Exigence proposée à arbitrer |
| --- | --- | --- |
| Rechargement ordinaire | FEAT-002/J01 prévoient sessions et reprise ; aucune reconnexion systématique adoptée. A l’exigerait après toute perte de vue. | Une session valide reprend après vérification serveur de sa continuité autorisée. Écran neutre pendant cette vérification. Continuité absente, expirée ou invérifiable : authentification explicite ; panne : indisponibilité. |
| Logout incertain | C2 masque la vue et arrête ses mutations ; maintien après reload non résolu. | Maintenir le verrou lors des reprises ordinaires dans la portée contractualisée. Une commande jamais reçue reste non confirmée. Si l’information nécessaire manque, aucune reprise privée automatique. |
| « Dernier login » | C3 ordonne les transitions d’une racine connue ; C1/C2 indépendants peuvent rester valides. Garantie globale ouverte. | Dans une lignée établie, seule l’intention gagnante selon l’ordre serveur autorise la nouvelle vue ; une réponse ancienne ne restaure pas l’identité précédente. Aucune exclusivité globale entre racines indépendantes promise. |
| Usage partagé | Protection des sessions résiduelles identifiée ; « appareil partagé » non défini. | Couvrir plusieurs personnes utilisant successivement un même profil de navigateur et plusieurs onglets. Afficher clairement le compte actif. Ne pas présenter un changement de compte comme une fermeture de toutes les sessions du navigateur. |
| Connexion sans réponse | C1 interdit d’attribuer le succès avec 049 ou l’email saisi. | Afficher un résultat inconnu et proposer une nouvelle démarche explicite. Aucun deuxième login automatique ; aucune déclaration de succès de l’ancienne intention. |
| Sortie et récupération | Logout candidat : famille ciblée et continuations. Récupération : anciennes sessions du compte invalidées, portée à ratifier. | Libeller la sortie « Se déconnecter de cette session ». Distinguer sa confirmation de toute fermeture globale. Après remplacement vérifié du moyen d’accès, invalider les anciennes sessions du compte puis demander une nouvelle connexion. |

## Périmètre minimal cohérent

Retenir l’authentification, l’attribution fiable de chaque vue/action, la révocation ciblée, la récupération et la reprise ordinaire vérifiée. Différer le reçu consultable après logout et l’exclusivité entre amorçages indépendants, **sous acceptation explicite de leur conséquence**. Le reçu est facultatif ; la continuité nécessaire au parcours retenu ne l’est pas. Aucune méthode d’identité, bibliothèque, durée ou nouvelle donnée n’est sélectionnée ici.

Le contrat doit définir ce qui conserve le verrou de sortie et ce qui permet la reprise, leur portée entre onglets, leur expiration et le comportement après effacement de stockage. Une session simplement observée ne prouve pas l’absence d’un logout perdu. Si 03/04/14/15 ne peuvent démontrer cette distinction, HQ doit arbitrer à nouveau entre le coût de A et une garantie de sortie réduite ; le sous-agent ne choisit pas implicitement cette réduction.

## Impact utilisateur et clôture attendue

La reprise ordinaire évite de multiplier les authentifications et interruptions de lecture. Aucun gain de rétention ou taux d’abandon n’est établi. Le verrou protège la sortie malgré une connexion instable, mais peut imposer une reconnexion. Le texte doit dire « Déconnexion non confirmée » ; une authentification fraîche ne confirme pas rétroactivement la sortie.

Sur navigateur partagé, une ancienne paire cohérente indépendante peut rester autorisée. Le périmètre proposé ne garantit donc pas la remise du navigateur à une autre personne sans accès résiduel. Si cette garantie est indispensable au pilote, l’exclusivité globale demeure bloquante. Le partage volontaire d’identifiants ne crée aucun rôle collaboratif dans ce lot.

HQ/01 arbitrent ce paquet avec 05/14 ; 03/04 spécifient la continuité, 15 ses données, 02 les états et 18 les preuves : reload normal, logout jamais envoyé puis reload, ancienne paire cohérente, permutations de réponses et changement A→B. Livrable : cet avis uniquement. Aucun test applicatif exécuté, aucune acceptation propriétaire transférée, aucun constat fermé ; L1 reste bloqué pour code.
