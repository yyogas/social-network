# Sous-agent 15 — Preuves et observation minimales

Avis indépendant du 30 septembre 2026, **PROPOSÉ**, distinct des validations des équipes 13/14/15. Sources : Backend PR #28 v0.3, SHA `0a7fcd54b996cc292bfe98c61a835613837def32`, sections de convergence C3–C7 ; `measurement-plan.md` ; `security-operations-requirements.md`, REQ-1409 ; `privacy-requirements.md`, §5 ; avis indépendants `04-privacy.md` et `11-devops.md`. Aucun schéma adopté, délai légal, accord propriétaire ou résultat runtime n’est établi.

## Trois finalités séparées

| Canal | Contenu minimal et accès proposés |
| --- | --- |
| Audit obligatoire | Faits sensibles durables : autorisation finale, effet, consommation, révocation, reprise et ouverture après restauration. Security habilité ; Privacy sur dossier ; lecture/export eux-mêmes audités. |
| Diagnostic | Route normalisée, code contrôlé, latence, composant, état d’autorité, profondeur/âge de file et perte de télémétrie. Exploitation ; échantillonnage et cardinalité bornés. |
| Analytics | Agrégats approuvés, finalité/version propres. Aucun recyclage des événements d’authentification, références de session, K ou recovery en suivi comportemental. |

L’audit ne remplace ni le registre autoritatif K, ni le registre d’effacements/restrictions survivant au rollback. Les données pseudonymisées restent personnelles ; l’accès technique n’autorise pas une jointure métier.

## Enveloppe conceptuelle fermée

Champs candidats communs : identifiant d’événement généré serveur, type/version, producteur, environnement, finalité, date serveur, version du contrat et résultat/motif énumérés. Pour l’audit seulement, ajouter référence opaque d’opération, attestation de commit et référence d’ordre autoritatif si nécessaires. SHA et paramètres figurent dans le dossier d’exercice ; aucune répétition obligatoire par trace.

Corrélation limitée à une opération et ses reprises, ou à un exercice synthétique. Une référence de cible exceptionnellement nécessaire reste dans une zone restreinte, avec justification, accès et échéance propres. Aucun identifiant durable commun aux comptes, navigateurs et finalités ; aucun rapprochement email saisi/session observée. Les alias F/E/T/D du rapport sont locaux au scénario, sans capacité d’accès ni table de correspondance exportée.

Interdits : mots de passe, challenges, cookies, jetons CSRF, témoins de vue, K brut, empreintes sensibles de requête, corps, emails, URL signées, texte libre et données privées. IP brute, fingerprint et identifiants utilisateurs sont exclus des labels ordinaires. Les champs inconnus sont rejetés avant stockage, y compris quarantaine, DLQ et crash-report.

## Preuve de L, du commit et de restauration

Un événement candidat `auth_transition_committed` relie opération, type d’effet, contrôles effectués à L, références d’ordre et résultat durable. L’attestation doit provenir de l’autorité transactionnelle ; juxtaposer deux timestamps ou écrire « validé » ne prouve ni protection jusqu’au commit ni atomicité. Le mécanisme et son intégrité restent à choisir par 03/04/14.

Dans les fixtures : comparer login/logout et login/recovery par même domaine de conflit, alias locaux avant/après, ordre démontré et compteurs d’effets. Distinguer admission, refus, commit et replay exact : celui-ci référence le fait original sans nouvelle consommation ni émission logique. Un timeout conserve le résultat inconnu ; l’arrivée HTTP n’établit pas l’ordre L.

Pour restauration, dossier par exercice : sauvegarde, fermeture, retrait de D ancienne par autorité hors rollback, D nouvelle, réconciliation des révocations/effacements, vérifications, puis décision d’ouverture. Résultats attendus : anciennes capacités refusées, données effacées absentes, aucun second effet, compte témoin inchangé. Compteurs et alias synthétiques suffisent au rapport ; aucun graphe multi-compte de production n’est requis.

## Bornes et pannes à contractualiser

Choisir séparément durée active, archivage, sauvegardes, exports, files et retard maximal de purge ; départ depuis événement/commit, jamais dernier replay. Fixer propriétaire, nécessité, échéance calculable et réexamen des exceptions. Les marqueurs anti-rejeu couvrent les admissions/continuations encore possibles ; leur empreinte sensible cesse plus tôt si inutile. Aucun report automatique des hypothèses 90 jours/7 jours.

Si la preuve obligatoire ne peut être rendue durable avec l’effet, refuser avant effet ; après résultat incertain, réconcilier sans annoncer un rollback. Une panne diagnostic/analytics n’interrompt pas indistinctement le service : tampon borné, retries au même identifiant, déduplication, alertes perte/backlog et données déclarées partielles. Intégrité d’autorité ou réconciliation invérifiable : admissions/périmètre fermé. Aucun test exécuté ici.
