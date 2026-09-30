# Avis sous-agent12 — UX et localisation des états d’accès

Avis documentaire du 30 septembre 2026, **PROPOSÉ**, sans validation des équipes 02/16/18. Sources : HQ `4d3cd079e92217936af3292429a38f91f7b576ff`, localisation, parcours UX/Produit et exigences Web ; Backend v0.3 `0a7fcd54b996cc292bfe98c61a835613837def32`, C1–C7 ; `03-web.md`. Ce sous-agent ne représente aucune discussion antérieure.

Le positionnement est universel, mondial, peuple kabyle inclus. Priorités marketing ≠ pays de lancement. Le français sert ici à la revue : **ni français par défaut, ni couple EN/FR IP2, ni langue pilote adoptés**. La méthode d’authentification demeure ouverte.

| État observable | Message FR candidat | Action sûre / reprise |
| --- | --- | --- |
| 1. Vérification initiale, reload ou retour | « Vérification de votre accès… » ; si panne : « Impossible de vérifier votre accès pour le moment. » | Masquer le privé ; reprendre une lecture bornée. Une panne ne signifie pas déconnexion. |
| 2. Connexion refusée : `AUTH_INVALID` | « Connexion impossible avec les informations fournies. » | Corriger puis soumettre explicitement ; proposer la récupération sans confirmer l’existence du compte. |
| 3. Résultat de connexion inconnu | « Nous ne pouvons pas confirmer cette connexion. » | Aucun second login automatique. Réconcilier selon contrat ; observer un autre compte ne prouve pas cette tentative. |
| 4. Contexte courant expiré ou changé | « Votre accès doit être vérifié à nouveau. » | Arrêter l’ancienne intention ; vérifier puis proposer une reprise explicite. Ne pas reconstruire sa commande sous une autre identité. |
| 5. Déconnexion demandée, réponse absente | « Déconnexion non confirmée. Le contenu privé reste masqué dans cette page. » | Masquer dès le clic, suspendre les mutations ; reprise uniquement dans la portée autorisée, sinon conserver l’incertitude. |
| 6. Déconnexion confirmée et attribuable | « Déconnexion confirmée pour cette session. » | Retour à l’entrée publique. Expliquer la portée ratifiée ; ne pas annoncer la fermeture de toutes les sessions du compte. |
| 7. Demande de récupération reçue | « Si les informations fournies permettent une récupération, vous recevrez les instructions prévues. » | Message neutre ; ne confirmer ni compte, ni adresse de destination, ni délivrance effective. Aucun renvoi agressif. |
| 8. Preuve de récupération refusée | « Cette procédure ne peut pas être poursuivie. Vous pouvez demander de nouvelles instructions. » | Nouvelle procédure explicite. Expiration, consommation et remplacement suivent leurs codes authentifiés ; « consommé » ne signifie pas récupération réussie. |
| 9. Récupération effectivement confirmée | « Votre moyen d’accès a été mis à jour. Vous pouvez vous connecter. » | Connexion explicite ; aucune levée de restriction ni connexion automatique. La demande d’instructions seule ne révoque aucune session. |
| 10. Accès restreint vérifié | « Certaines actions ne sont pas disponibles. Consultez les informations et démarches accessibles. » | Afficher uniquement les voies réellement autorisées ; ne déduire aucun motif sensible des capacités absentes. |

Les libellés n’exposent ni email même masqué, nom, avatar, référence de compte/profil, motif confidentiel, ni identité d’un signalant. Diagnostics : famille d’état, clé/version de ressource et locale technique seulement selon validation ; exclure secrets, cookies, CSRF, clés d’idempotence, preuves, URL de récupération, corps et historique multi-compte. La locale n’infère ni origine, résidence ou admissibilité.

Au rechargement, viser la continuité d’une session après vérification autorisée : l’option A n’est pas adoptée par défaut. Après déconnexion jamais reçue puis perte totale d’intention, une session active observée ne résout pas B03. Focus, restauration/bfcache, réveil et retour réseau imposent masque puis acquisition cohérente. Une ancienne réponse A ne modifie pas B. Aucun secret ou DTO par canal inter-onglets. Hors ligne, aucun succès supposé ni mutation mise en attente automatiquement ; aucune révocation immédiate mondiale promise. `CONTEXT_MAX_AGE` reste à ratifier.

Pour 429, afficher seulement le délai serveur reçu ; au-delà du budget, arrêter. 503 en mutation signifie résultat inconnu. Les chiffres C6 restent candidats. Changer de langue conserve le sens et les références autorisées, sans rejouer une action. Chaînes complètes, erreurs associées aux champs, focus conservé, annonces accessibles, textes longs et RTL sont à vérifier. Toute chaîne critique exige revue humaine ; secours approuvé annoncé, jamais clé brute ni traduction improvisée.

Critères de sortie pour les droits sous restriction, tous **PLANNED** :

- 09/10/15/14 définissent, par opération et état, preuve, permission, canal et responsable : décision, dépôt/suivi de recours, demande/suivi privacy.
- Profil absent et capacités vides n’empêchent pas les voies autorisées ; aucune garde globale ne boucle vers une connexion impossible.
- Sans session, un canal réel permet réception et suivi après vérification proportionnée, sans réactivation sociale ; aucun contact fictif.
- Vérifier accès au seul dossier propre, refus tiers, panne, langue manquante et reprise ; accusé uniquement après réception, aucun délai inventé.

Aucun code, test runtime, modification distante ou fermeture de blocage effectué.
