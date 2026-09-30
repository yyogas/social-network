# Sous-agent09 — Canal de support, recours et droits hors session

**Avis de sous-agent, pas validation de l’équipe 10.** Proposition documentaire du 30 septembre 2026 pour `yyogas/social-network`. Aucun canal actif, fournisseur, destinataire, accord spécialisé ou résultat applicatif n’est établi. **P15-L1-05 / QA-E / GAP-05 restent ouverts.**

Sources : au snapshot HQ `4d3cd079e92217936af3292429a38f91f7b576ff`, `documentation/administration/administration-support-requirements.md` (§§ Recours, Rétablissement, Données, Interfaces), `documentation/privacy/privacy-requirements.md` (§§3.3, 4, 5), `documentation/trust-safety/moderation-requirements.md` (§§ Anti-spam, FEAT-015) ; Backend `0a7fcd54b996cc292bfe98c61a835613837def32`, `documentation/backend/api-contract-candidates.md` au SHA Backend précité, convergence C6/C8 ; avis indépendant [avis sous-agent 04](04-privacy.md). Le besoin est établi ; sa réalisation opérationnelle manque.

## Parcours minimal candidat

Proposer **un formulaire web public de première partie**, accessible avant connexion et depuis les écrans de refus, suspension, fermeture, profil absent ou capacités inconnues. Il reçoit trois catégories séparées : aide d’accès, recours de modération, droits sur les données. Ce choix réduit la dépendance à un prestataire externe ; il reste à adopter et n’invente aucune adresse.

1. Afficher une notice courte, les langues effectivement couvertes et les informations de traitement ratifiées. Ne demander ni inscription ni réactivation sociale. Le blocage interpersonnel ne ferme pas les droits propres.
2. Recueillir catégorie, langue, moyen de réponse choisi, description limitée et référence de décision/dossier si disponible. Une référence inconnue ou perdue n’empêche pas la réception ; aucune pièce jointe au socle candidat. Les justificatifs éventuellement nécessaires suivent un circuit spécialisé ultérieur.
3. Enregistrer durablement la demande et son horodatage initial ; donner un reçu opaque attestant seulement cette réception. L’existence d’un compte, d’une sanction ou d’un dossier antérieur n’est jamais confirmée publiquement. La réception ne signifie ni identité vérifiée ni recours recevable.
4. Router vers une file assignée. Commencer le suivi dès réception ; vérification, transfert ou panne ne remettent pas arbitrairement son horloge à zéro. L’opérateur distingue attente d’informations, examen, réponse et clôture.
5. Après vérification adaptée, fournir un suivi limité au dossier propre et une réponse protégée. Recours : décision, notification et réparation restent distinctes. Droits : livraison éventuelle des données par accès vérifié séparé ; aucun export obtenu par simple numéro de reçu.

## Identité, abus et minimisation

La maîtrise du moyen de réponse déclaré prouve seulement cette maîtrise, pas la titularité du compte. Une référence de décision, un pseudonyme public ou un reçu logout ne suffisent pas. 14/15 doivent choisir une preuve admissible liée au sujet et proportionnée à l’action ; 09 précise celle du recours. Si les facteurs habituels sont perdus ou compromis, réception maintenue puis examen humain selon procédure définie, sans divulgation préalable.

Ne demander ni mot de passe, ni code MFA à l’agent, ni pièce d’identité systématique. Support ne modifie pas directement l’identité et ne restaure pas l’accès social. Un contexte de suivi spécialisé éventuel possède permissions, expiration et révocation propres, sans pouvoir social ou opérateur.

Prévoir limites de taille et débit, protections contre soumissions forgées, rejeu et énumération, avec reprise accessible. IP commune ou répétition seules ne prouvent pas l’abus. Le chemin de réception alternatif, utilisable si ces protections bloquent injustement ou si l’autorité est indisponible, doit être réellement désigné. Aucune solution de repli n’est attestée aujourd’hui. Champs, preuves, traces, copies et exceptions demandent des durées opérables validées ; aucune durée candidate existante n’est adoptée ici.

## Opérateurs et audit

Support reçoit les seules métadonnées nécessaires dans sa file ; Privacy qualifie les droits ; le réviseur habilité traite le recours indépendamment du décideur initial. Identités nominatives, MFA personnel, contrôle serveur du scope à chaque consultation/action et révocation effective sont requis dans la proposition. Notes internes et réponses restent séparées ; transfert de file ne transmet pas automatiquement les preuves.

Tracer réception, assignation, contrôle d’identité, consultation sensible, transfert, décision et livraison avec acteur, dossier, résultat, horodatage et version de règle. Exclure secrets, justificatifs bruts et récit intégral des journaux généraux. Une panne d’audit bloque l’action sensible ; elle ne justifie pas la disparition silencieuse d’une demande reçue.

## Critères futurs et décision manquante

04 doit contractualiser les statuts HTTP : succès seulement après réception durable ; validation et limitation distinguées ; indisponibilité sans faux reçu. Timeout signifie résultat inconnu ; reprise dédupliquée sans second dossier ni perte. Lecture privée refusée sans vérification, réponses anti-énumération cohérentes, caches exclus des réponses sensibles. UI : aucune boucle connexion, clavier/lecteur d’écran utilisables, états reçu/à vérifier/indisponible distincts. Vérifications futures : suspension, compte fermé, capacités vides, perte de facteurs, panne, doublons et accès au dossier d’autrui ; **PLANNED uniquement**.

Décision attendue de HQ avec 10/09/14/15 : adopter ou remplacer ce formulaire, nommer son emplacement public réel, responsable humain et suppléant, couverture/langues, circuit de réponse et repli effectifs, preuves acceptées, scopes et rétention. Ensuite seulement 04/05 raccordent le contrat et l’interface, puis 18 constate les preuves. Cette fiche ciblée complète C6 et INT-1001 à 1006 sans nouvelle spécification générale ni levée de blocage.
