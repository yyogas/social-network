# agent04 — Relecture indépendante Privacy de Backend v0.3

Revue documentaire du 30 septembre 2026, distincte de la discussion 15. **Verdict proposé : À AMENDER ; P15-L1-05 et P15-L1-08 restent BLOQUANTS dans leur périmètre.** La v0.3 répond utilement aux demandes antérieures, mais ne fournit ni politique ratifiée ni preuve applicative. L1 reste BLOQUÉ POUR CODE. Aucun accord d’équipe, avis juridique externe ou changement distant n’est déclaré.

Sources lues via GitHub, dépôt `yyogas/social-network` :

- Backend, PR #28, `documentation/backend/api-contract-candidates.md`, commit `0a7fcd54b996cc292bfe98c61a835613837def32`, blob `770cbf3695aef8d6acdcf33b5c9dd59ec62f57fd` : sections **de convergence** C1, C6, C8, distinctes des règles communes homonymes.
- Privacy, `documentation/privacy/backend-l1-targeted-review.md`, commit `81063238cd32689c630aaa1e70633b7104a48042`, blob `4aef423112530ebd8061bb1370c2a8ef1ab743fa` : constats P15-L1-03 à 10, §§3–7. Cet avis portait sur Backend `1acf84fffcaa8131c0826d4874126e107a4cf978` ; ses acceptations ne deviennent pas des validations de v0.3.

C1 reconnaît désormais l’absence d’usage distinct démontré pour `account_ref`, maintient compte/profil séparés et supprime la déduction « email saisi → sujet observé ». C6 distingue fin d’autorisation, conservation et purge ; le contrôle B reçoit un plafond absolu candidat. C8 conserve honnêtement les dépendances. Toutefois, « dernière échéance des preuves » reste inexécutable si ces preuves, continuations et copies ne sont pas inventoriées. Une marge proposée de cinq minutes ne résout pas ce manque.

**Matrice minimale à compléter et ratifier.** Les nombres reproduisent uniquement C6 : préauth 30 min, challenge 15 min, IDLE 30 min, ABSOLUTE/racine B 12 h, reçu 10 min, marge `P=5 min`. Aucun n’est adopté ici.

| Objet et accès nécessaire | Départ / fin du pouvoir | Purge minimale et donnée manquante |
| --- | --- | --- |
| Préauth ; module auth | Création serveur / borne absolue | Liaison et payload à borne +P ; préciser horizon du marqueur d’admission, abandons compris. |
| Racine B ; auth uniquement | Création / plafond non renouvelable | Dissocier anciens comptes dès inutilité ; racine à borne +P ; démontrer reset sans réadmission. B reste conditionnel. |
| Challenge ; auth | Émission / consommation, échéance ou révocation | Secret/empreinte dès fin du besoin de comparaison ; marqueur anti-rejeu séparé jusqu’à horizon calculable. |
| K, empreinte, résultat ; opérations | Admission / clôture des replays autorisés | Empreinte sensible supprimée dès comparaison inutile ; marqueur/résultat minimaux selon horizon distinct ; rotation des clés coordonnée. |
| Session/révocation ; auth, diagnostic limité | Émission / IDLE, ABSOLUTE ou retrait autoritatif | Secret inutilisable éliminé ; marqueur/époque conservés selon dépendances explicites, sans historique illimité. |
| Reçu logout B ; contexte vérifié | Commit / minimum entre dix minutes et borne racine | Refus à échéance ; reçu/liaisons à +P ; aucune identité de compte dans réponse, audit séparé. |
| Cookies ; navigateur et auth | Émission / expiration absolue appropriée | Borne client vérifiée, sans renouvellement tardif ; nettoyage seulement sans effacer la session B. |
| Audit, diagnostic, refus ; habilitations distinctes | Événement / aucune durée fournie | Champs, finalité, durées, réexamen des exceptions et purge propres : NON REÇUS. |
| Backups, répliques, outbox/DLQ, email ; exploitants/prestataires habilités | Snapshot, commit ou envoi | Calendrier par destination et accès nommés : NON REÇUS ; restauration isolée avant réouverture. |

Chaque ligne exige propriétaire, champs/liens autorisés, horloge, événement terminal, retard maximal, exceptions motivées, destinataires et preuve d’élimination. L’interdiction d’accès malgré une panne de purge reste distincte de l’effacement. Les marqueurs anti-rejeu ne doivent disparaître qu’après fermeture des voies anciennes ; cette nécessité n’autorise pas une conservation indéfinie. Finalités/bases et qualification terminal des cookies, générations et K restent à documenter selon l’avis source ; aucun réemploi analytics ni exemption présumée.

**Corrections exactes proposées au propriétaire Backend :**

1. À la ligne K de C6, remplacer « puis +P purge entrée sensible » par : « L’empreinte sensible est supprimée dès la fin démontrée du besoin de comparaison, avec retard maximal approuvé. La conservation du marqueur, du résultat minimal et du matériel de vérification possède des échéances distinctes. Aucun corps secret n’est conservé pour attendre la purge du marqueur. »
2. Après le tableau des cycles, ajouter : « Pour chaque horizon dépendant, énumérer preuves, admissions, continuations et copies concernées ; calculer leur dernière échéance depuis des événements serveur. Si cet horizon reste indéterminé, le cycle reste NON READY. Les durées du support des époques, des audits et des copies secondaires doivent être renseignées avant levée de P15-L1-08. »
3. En C1, après la minimisation, ajouter : « Pour chaque champ de projection retenu, documenter écran/action consommateur, nécessité distincte, destinataires et alternative moins identifiante. Le bundle AuthView entre dans le même inventaire ; aucune référence sensible dans télémétrie, crash-report, historique ou échange inter-onglets. »
4. En C8, conserver les deux blocages et ajouter à leurs preuves : « Référence de décision, propriétaire, version effective et pièces de vérification requises ; réponse documentaire fournie ne signifie pas constat levé. »

**Raccordement minimal pour P15-L1-05.** Le tableau C6 reste une demande de définition ; il faut le remplacer ou compléter par des lignes opérationnelles :

| Situation / opération | Contrôle et canal à faire approuver |
| --- | --- |
| Compte restreint : demander/suivre un droit | Titularité vérifiée, capacités dédiées et périmètre propre ; aucune permission sociale requise. |
| Décision/recours | Accès à sa décision et dépôt/suivi séparés du droit privacy ; occultation des tiers selon 09/15. |
| Profil absent ou capacités vides/inconnues | Aucun profil public exigé ; canal alternatif visible sans dépendre d’une capacité reconnue. |
| Session compromise/perdue, compte fermé | Vérification proportionnée par circuit dédié, responsable nommé et suivi ; aucun export délivré sur reçu logout. |
| Recovery ou panne d’autorité | Restrictions préservées ; réception alternative horodatée, reprise sans perte de demande ni remise à zéro arbitraire du suivi. |

09/10/14/15 doivent fournir permissions, preuves admissibles, coordonnées réelles, habilitations opérateur et responsabilité de réception ; 05 fournit le parcours utilisable, 04 le raccordement. Le canal alternatif ne doit pas dépendre de la création d’une nouvelle session sociale.

**Preuves futures et limites.** Reprendre V15-03/05/06 : connexion A perdue puis B visible, réponses inversées, reçu avant/après échéance, aucune identité A divulguée ni effacement B. Ajouter inspection des destinations de traces, horloges aux bornes et restauration d’anciennes copies sans session réactivée ni reçu expiré servi, selon V15-04/08/09. Lier chaque résultat au SHA, scénario, paramètres, ordre serveur et observations expurgées. Ces preuves restent PLANNED ; aucun test navigateur, sécurité ou restauration n’a été exécuté. Les exigences utilisées sont celles de l’avis existant ; aucune nouvelle conclusion juridique ni durée légale n’est formulée.
