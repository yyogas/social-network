# agent08 — Matrice proposée : restriction, suspension, suppression

Contribution documentaire du 30 septembre 2026, indépendante de la discussion 09. **PROPOSÉ, relecture 09/10/14/15 puis 04/05/18 requise ; P15-L1-05 reste BLOQUANT.** Cette matrice ne fournit aucune permission adoptée ni canal opérationnel.

Références : snapshot HQ `4d3cd079e92217936af3292429a38f91f7b576ff`, exigences `documentation/trust-safety/moderation-requirements.md` (FEAT-015, permissions, AC-J05-04/05), `administration/administration-support-requirements.md` (rétablissement, demandes de données, matrice), `privacy/privacy-requirements.md` (§§3.3–3.5, 4). Backend PR #28, `0a7fcd54b996cc292bfe98c61a835613837def32`, sections de convergence C1/C6/C8 ; complément indépendant [avis sous-agent 04](04-privacy.md).

## États et séparation des pouvoirs

`restricted` est une projection auth minimale, sans motif sensible. La limitation cible des capacités ; la suspension interrompt temporairement les capacités sociales ; le bannissement les ferme durablement, sans signifier effacement. `deleted` désigne ici le compte après retrait d’accès, pas une valeur adoptée du DTO : purge, sauvegardes et exceptions ont leurs états propres. Profil absent et session perdue constituent d’autres axes.

Une session valide établit une identité, pas l’ensemble de ses permissions. À chaque opération, le service vérifie sujet, ressource, habilitation et restrictions courantes. Une récupération ne lève aucune sanction. Capacités vides/inconnues n’accordent rien ; elles ne doivent pas masquer le canal de réception alternatif.

## Matrice minimale à ratifier

« Dédié » signifie capacité propre, contrôle serveur et canal approuvé ; aucun code ou endpoint fixé ici. « À définir » conserve le blocage concerné.

| Opération propre | Limitation / projection `restricted` | Suspension ou bannissement | Compte supprimé / accès retiré |
| --- | --- | --- | --- |
| Compte : accès, paramètres, récupération | Auth distincte ; recovery ne modifie aucune restriction ; paramètres autorisés à définir | Accès limité dédié ; récupération sans capacités sociales | Aucun rétablissement implicite ; suivi hors session |
| Profil : lire ou modifier | Selon capacité précise ; rectification via dossier si nécessaire | Lecture/édition sociale à définir ; rectification dédiée possible | Aucun profil requis pour une demande ; aucune recréation |
| Publication : créer, éditer, interagir | Refus des capacités visées ; autres permissions explicites | Capacités sociales refusées | Refus ; ancien job/retry ne recrée rien |
| Export : demander, suivre, télécharger | Demande neutre recevable ; suivi privé et téléchargement après preuve du sujet et autorisation propre, revérifiées au téléchargement ; tiers occultés | Même voie, indépendante de publication/profil | Demande sur données résiduelles examinée ; aucune archive purgée recréée |
| Suppression : demander, suivre | Voie privacy dédiée avec confirmation appropriée | Même voie ; sanction distincte des exceptions de conservation | Suivi purge/exception ; demande répétée sans second effet destructif |
| Décision et recours : consulter, déposer, suivre | Décision propre ; admissibilité selon politique | Accès dédié conservé après vérification | Canal alternatif ; décision conservée et admissibilité à vérifier |
| Support : recevoir, suivre, escalader | Ticket minimal ; aucune permission sociale requise | Idem, sans modification du verdict | Réception possible sans nouvelle session sociale |

Retrait de publication, suppression de compte et effacement restent distincts. Un recours accepté ne republie pas un objet supprimé par l’auteur et ne lève pas une autre sanction. Après effacement confirmé, génération/export sont annulés ou révoqués selon Privacy ; données résiduelles via circuit dédié.

## Identité, canaux et erreurs

**Proposition de raccordement :** session propre validée lorsque disponible ; contrôle renforcé proportionné pour export/suppression ; vérification du propriétaire à chaque téléchargement. En cas de session perdue, compromise ou de facteur inaccessible, réception hors session horodatée, puis procédure 14/15 précisant preuves strictement nécessaires, accès et purge. Aucune pièce d’identité par défaut. Le ticket, identifiant opaque, email saisi ou reçu de logout ne constitue pas une preuve suffisante. Support ne collecte ni mot de passe ni code MFA, ne change pas directement l’adresse de récupération et n’usurpe aucune session.

Avant vérification, réponse neutre sans confirmer existence, suppression ou sanction du compte ; aucun dossier privé par référence devinée. Après vérification, expliquer refus et recours propres sans signalant, notes internes ou catégories sensibles. Panne d’autorité : aucun contenu privé, réception alternative conservée. Un timeout indique une issue inconnue ; le suivi conserve son horodatage initial.

## Questions, propriétaires et acceptation

**Conflits à résoudre :** refus auth global contre voies dédiées ; `restricted` contre sanction détaillée ; suppression contre preuve conservée ; visibilité UI contre autorisation serveur. Aucun choix arbitraire ne résout ces tensions.

09 définit admissibilité, fenêtres, indépendance et réparation ; 15 définit droits, exceptions et preuve minimale ; 14 approuve vérification et habilitations ; 10 nomme réceptionnaire, suppléant et coordonnées réelles. 04 contractualise ; 05 rend le parcours accessible ; 18 vérifie.

**Acceptation documentaire :** matrice ratifiée, dictionnaire de permissions, procédure de preuve, canal réel et responsabilités nommées/versionnées. **Preuves futures :** propriétaire versus tiers ; compte suspendu sans profil ; capacités inconnues ; session perdue ; panne ; suppression concurrente avec export ; recours sans publication ni restauration interdite. Raccorder TEST-0908/0909, TEST-0413/0415 et TEST-PRIV-M0-06/10/18, tous PLANNED. Aucun test applicatif exécuté, aucune fermeture de constat ni conclusion juridique nouvelle.
