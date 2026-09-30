# Avis Privacy ciblé — Backend L1 GAP-L1-01 à 04

## 1. Identification, mandat et verdict

| Champ | Valeur |
| --- | --- |
| Référence locale | PRIV-L1-REVIEW-01, v0.1 ; équipe 15 — Juridique / Privacy / RGPD |
| Date | 30 septembre 2026, Europe/Paris |
| Objet | Avis spécialisé sur nécessité des données, projections, contextes/reçus, conservation et accès aux droits après restriction |
| Delta examiné | [PR #28](https://github.com/yyogas/social-network/pull/28), SHA exact `1acf84fffcaa8131c0826d4874126e107a4cf978` |
| Document propriétaire | [api-contract-candidates.md au SHA examiné](https://github.com/yyogas/social-network/blob/1acf84fffcaa8131c0826d4874126e107a4cf978/documentation/backend/api-contract-candidates.md), lignes 305–505 ; blob `2bfcfeed3ffd853e6b9fbef700720d8dcedfe6e9` |
| Raccordements bornés | [préparation L1 §4, notamment GAP-05/06/08](https://github.com/yyogas/social-network/blob/1acf84fffcaa8131c0826d4874126e107a4cf978/documentation/quality/first-lot-contract-readiness.md), blob `5c29e66679d182dc25cc8c1920405dc9638464f0` ; [Privacy §§3.3–3.4 et P01/P02/P08](https://github.com/yyogas/social-network/blob/1acf84fffcaa8131c0826d4874126e107a4cf978/documentation/privacy/privacy-requirements.md), blob `7db8aaae76417c79b4979057c4796d05d52af1a3` |
| Statut | Avis documentaire de 15 rendu sur cette seule révision ; corrections ci-dessous PROPOSÉES aux propriétaires, non intégrées au Backend |
| Phase | MVP candidat, L1 ; aucune modification des phases ultérieures |
| Verdict global | **À AMENDER ; deux dépendances BLOQUANTES pour validation Privacy du contrat concerné. L1 demeure BLOQUÉ POUR CODE.** |
| Autorité | 15 formule l'avis Privacy ; 04 modifie son contrat, 09 définit les restrictions/recours, 14/03 valident la sécurité/architecture, HQ arbitre les décisions structurantes |

**CONFIRMÉ** : lecture du delta exact, existence des propositions et paramètres explicitement ouverts. **PROPOSÉ** : corrections, matrices et critères de levée de cet avis. **À VÉRIFIER** : nécessité finale, bases/durées, qualification des cookies, schémas et preuves futures. **NON REÇU dans cette revue** : accords des autres équipes, protocole approuvé, implémentation et tests applicatifs. Aucun audit général du corpus ni approbation du protocole de session.

DIR-012 est préservé : public universel ; les priorités marketing ne fixent ni origine personnelle, ni résidence, ni pays servi, ni âge. Aucun retour à l'ancienne hypothèse communautaire ou à un pilote France/adultes par cet avis.

Sens des verdicts :
- **ACCEPTÉ AU NIVEAU DOCUMENTAIRE** : principe suffisamment clair pour ce point Privacy, sans preuve d'implémentation ni approbation transverse.
- **À AMENDER** : précision/correction propriétaire requise avant gel de l'élément concerné.
- **BLOQUANT** : absence déjà identifiée empêchant la validation Privacy du raccordement/lot concerné ; pas une vulnérabilité runtime démontrée ni une interdiction de poursuivre la rédaction.
- **HORS MANDAT** : 15 ne prononce pas la validation technique ou métier ; propriétaire explicitement nommé.

## 2. Matrice des constats et corrections attendues

Les repères P15-L1 sont locaux à cet avis et ne réservent pas de nouveaux IDs globaux. Les numéros de ligne visent uniquement le SHA ci-dessus.

| Repère / point | Preuve Backend | Verdict | Justification Privacy / correction attendue / destinataire |
| --- | --- | --- | --- |
| P15-L1-01 — identité et admission | GAP-01, L319–324, L335–343, L452 | ACCEPTÉ AU NIVEAU DOCUMENTAIRE | La preuve email est distincte d'identité civile/âge/résidence et les réponses initiales sont neutres. Préserver cette séparation et l'absence de pays marketing. Le choix password/passkey/fédération et les preuves techniques restent 03/14/HQ ; champs d'admission GAP-06 non validés ici. |
| P15-L1-02 — projection anonyme et séparation compte/profil | GAP-03, L375–379, L382, L387–398 | ACCEPTÉ AU NIVEAU DOCUMENTAIRE | Variante anonyme sans viewer, profil nullable, absence d'email/motif/âge et distinction panne/anonyme réduisent les divulgations. Préserver les DTO sans créer automatiquement un profil. L'exposition des références et la qualification restricted font l'objet des points 03–05. |
| P15-L1-03 — account_ref et profile_ref obligatoires | GAP-03, L377–378, L402 | À AMENDER | Identifiants opaques mais corrélables. Séparation des domaines justifiée ; nécessité d'envoyer les deux références à chaque lecture non démontrée par un usage consommateur précis. 04/05 doivent nommer pour chaque champ l'écran/action qui le consomme et comparer une lecture du profil propre sans identifiant de compte exposé. Garder deux champs seulement si besoin distinct documenté ; ne pas les fusionner silencieusement. Voir §3. |
| P15-L1-04 — état et capacités | GAP-03, L379–380, L394 ; GAP-04 L430 | À AMENDER | Projection coarse active/restricted et allowlist sont de bonnes limites ; la liste peut toutefois révéler indirectement une sanction ou un statut sensible. 09/04/14/15 doivent fixer mapping et codes minimaux, sans rôle global ni détail d'enquête. Séparer décisions/recours privés du contexte. Pas de pouvoir dérivé du DTO. Voir §3. |
| P15-L1-05 — droits après restriction ou perte d'accès | GAP-03 L382/L394 ; L459 ; demande 09/15 L487 | BLOQUANT | Le tableau reconnaît que capacités et canal alternatif sont indéfinis. La fixture restricted avec liste vide n'est pas en elle-même un défaut, mais ne prouve aucun accès aux droits. Fermer le raccordement opération × état × preuve × canal avec 09/10/04/14/05 ; voie hors session utilisable et responsable nommé, sans exiger réactivation ni levée de sanction. Voir §5. Bloque l'autorisation dépendante, pas toute la rédaction L1. |
| P15-L1-06 — empreinte K et entrée secrète | GAP-02 L347–365 ; L454 | À AMENDER | K seul ne donne aucun droit, reçu expurgé et absence de secret brut sont acceptables comme principes. La conservation d'une empreinte des secrets reste une surface sensible. 04/14 doivent comparer nécessité de l'empreinte secrète et liaison à une transaction validée ; préciser champs inclus, clé/rotation, TTL, destinataires et suppression. 15 ne choisit pas l'algorithme et ne valide pas sa résistance. Ne jamais conserver le corps complet sous prétexte d'idempotence. |
| P15-L1-07 — finalité des contextes navigateur | L334/L347 ; L419, L433/L437 ; L445 | À AMENDER | La liaison peut servir la déduplication et l'isolation A/B ; elle ne doit pas devenir un identifiant durable de navigateur/utilisateur multi-compte. 04/14/03 précisent bornes de vie, dissociation des comptes anciens, reset et nécessité d'un secret post-logout ; 15 examine finalité/base/régime terminal. Aucun réemploi en analytics, ads ou suivi inter-appareils dans ce lot. Voir §4. |
| P15-L1-08 — durée de validité versus conservation | L365 ; L443–448 ; L453–457 | BLOQUANT | Les TTL proposés limitent des autorisations ; rétention après usage, refus, tombstones et sauvegardes restent explicitement ouverts. Aucun calendrier de purge exécutable ni plafond du contexte réutilisé n'est établi. 04/14/15 complètent §4 : événements déclencheurs, bornes, marge de purge, archives/exceptions et preuves de restauration. Pas d'adoption des 90 jours ou 7 jours historiques. Bloque le gel du cycle de données correspondant. |
| P15-L1-09 — reçu logout minimal | L422–424, L433, L456 | ACCEPTÉ AU NIVEAU DOCUMENTAIRE | Résultat sans ID de compte, limité à l'opération/contextes vérifiés, distinct d'un droit social et d'un simple état anonyme : finalité compréhensible. Acceptation du principe de minimisation seulement ; nécessité du mécanisme et durée de 10 min non ratifiées (07/08), sûreté de liaison HORS validation 15. |
| P15-L1-10 — cookie invalide conservé après logout | L398, L435, L443 | À AMENDER | Éviter qu'une réponse tardive efface B est une justification pertinente ; cela n'autorise pas une conservation sans borne du résidu. 04/05/14 définissent borne client réelle, non-renouvellement sur erreur/lecture, devenir du cookie de contrôle et nettoyage sûr. Ne pas imposer un Set-Cookie d'effacement sur logout tardif, qui contredirait le scénario examiné. Voir §4. |
| P15-L1-11 — minimisation de lecture, traces et restauration | L386/L393/L396, L428–431, L444/L457 | ACCEPTÉ AU NIVEAU DOCUMENTAIRE | Lecture sans prolongation et diagnostic sans DTO/secret, distinction audit/diagnostic, restrictions conservées après recovery, refus de réactivation après restauration : invariants utiles. Préserver ; rétention et canaux droits restent 05/08, audit de sécurité et preuve navigateur 03/14/18. |
| P15-L1-12 — choix de protocole et validation QA complète | GAP-01/02/04 ; L1-BE-01 à 11 | HORS MANDAT | 15 ne ratifie ni CSRF/SameSite, résistance à la fixation, epoch/atomicité, entropie, hash, absence de refresh, valeurs de timeout ni mapping exhaustif des tests. 03/14/05/18 rendent ces avis ; §6 fournit seulement les oracles de confidentialité et cycle de données. |

Bilan : **4 ACCEPTÉ AU NIVEAU DOCUMENTAIRE, 5 À AMENDER, 2 BLOQUANT, 1 HORS MANDAT**.

## 3. Nécessité et projection minimale à faire ratifier

Ce tableau est un avis de schéma, pas une nouvelle API. Le Backend conserve API-BE-049 et son schéma tant qu'un amendement propriétaire n'est pas adopté.

| Donnée / projection | Usage candidat légitime dans L1 | Limite proposée et condition de validation |
| --- | --- | --- |
| identity/email et preuve de vérification | Connexion, activation, récupération | Module auth et prestataire de livraison strictement nécessaires ; pas dans API-BE-049, télémétrie ou paramètres d'URL. Base candidate contrat/mesures précontractuelles à qualifier ; sécurité/anti-abus à analyser séparément. |
| password, challenge, CSRF et cookies | Preuve de possession et protection d'opération | Secrets jamais dans DTO courant, logs, export téléchargeable ou archive d'audit ; empreintes techniques encore sensibles. Pas de collecte d'identité civile par déduction de cette finalité. |
| authentication / viewer nullable | Savoir si la vue privée peut être chargée | N'expose ni existence d'un compte donné ni motif d'expiration. État de panne non assimilé à anonymous. |
| account_ref | Éventuellement distinguer le sujet courant et ses changements côté client | 05 doit démontrer son usage distinct d'un indicateur de génération/contexte déjà prévu. Proposition : référence de sujet opaque, limitée au client autorisé si nécessaire ; ne pas exposer automatiquement la clé interne DB. Aucun ID public de rapprochement, aucun consentement implicite à l'analytics. |
| profile_ref | Éventuellement charger le profil associé | Null accepté ; pas d'obligation de profil pour exercer un droit. Vérifier si lecture du profil propre peut éviter cette donnée dans le contexte. Un profil public n'autorise pas à publier sa liaison avec un compte privé. |
| account_state | Séparer expérience active/restreinte | Deux valeurs candidates sans sous-code de sanction, gravité, motif, identité d'agent, plainte, minorité ou statut d'enquête. La notice de décision utile reste dans son parcours dédié avec droits propres. |
| allowed_capabilities | Indiquer les seules actions d'interface autorisées | Liste fermée nécessaire au client, scope sujet courant ; pas de rôles internes, de wildcard, d'historique ni code révélant la catégorie de sanction. Enum inconnue = aucun nouveau droit ; canal alternatif visible indépendamment de l'enum. |
| request_id, classe de résultat, latence | Diagnostic d'une requête | Corrélation technique bornée, pas clé de suivi durable. Exclure corps DTO et identifiants auth des crash reports/replay de session/outils de support, pas seulement des logs serveur. |
| last_interactive_at / epoch / génération | Expiration et ordre des opérations | Métadonnées internes de contrôle ; pas d'historique de navigation ni mesure de temps d'engagement. Mise à jour de l'activité sur liste approuvée ; ne pas ajouter un attribut comportemental « humain ». |

Les identifiants opaques/empreintes et leurs liaisons ne sont pas réputés anonymes. Base légale candidate ne vaut pas approbation : finalité, nécessité, accès, durée et texte d'information doivent être raccordés à P01/P02/P08 par 15 avec 04/14. Le fondement d'un traitement serveur et la qualification d'un dépôt/lecture de cookie sont deux analyses distinctes. Aucun consentement facultatif de mesure ne doit conditionner l'accès aux droits.

## 4. Conservation : delta demandé, sans inventer un délai légal

Les valeurs **30 min préauth, 15 min challenge, 30 min IDLE, 12 h ABSOLUTE et 10 min reçu logout** sont des propositions Backend. Avis 15 : elles peuvent servir aux scénarios de revue ; **aucune n'est ratifiée comme durée de conservation ou délai légal**. Besoin, accessibilité et menace à justifier avec 05/14.

Modèle de fiche demandé pour chaque objet : finalité/base candidate ; champs et liens réellement nécessaires ; propriétaire et destinataires ; création/début de compteur ; fin de validité ; déclencheur de purge et borne maximale du retard de purge ; archives/exceptions motivées ; sauvegardes ; comportement en panne/restauration ; critère de vérification. Pas de conservation définie seulement par « jusqu'à suppression ultérieure » ou « pour sécurité ».

| Objet du delta | Usage/durée actuellement proposés | Amendement de cycle attendu / propriétaire |
| --- | --- | --- |
| Contexte préauth sans compte | 30 min à compter d'un début à préciser ; aucun prolongement par retry | Fixer origin/time authority ; fin de recevabilité puis purge bornée de liaison et opérations expirées. Contextes abandonnés, compte inexistant ou inscription non aboutie inclus. Quotas sans garder indéfiniment une empreinte individuelle. 04/14/15. |
| Contexte de contrôle navigateur réutilisé | Pendant session puis fenêtre de reçu ; plafond général non établi | Distinguer la durée du contexte et celle de chaque génération/session. Un renouvellement de login ne justifie pas une identité de navigateur perpétuelle. Définir borne absolue du contexte, réinitialisation sûre et purge des associations A/B anciennes après besoin de réconciliation ; ne pas sélectionner un mécanisme cryptographique dans l'avis. 03/04/14/15. |
| Challenge et consommation | Validité candidate 15 min ; tombstone anti-rejeu | Distinguer secret/empreinte, reçu de résultat et preuve de consommation minimale. Purger ce qui n'est plus nécessaire sans permettre réusage ; justifier la période couvrant messages retardés, reprise et backups. Les tentatives/rejets ont leur propre durée. 04/14. |
| K et empreinte d'entrée protégée | Reçu borné au contexte | Aucune extension par polling ; supprimer l'empreinte des champs secrets dès fin de sa nécessité de comparaison, avec borne validée. Invariants métier de non-réexécution indépendants de la présence de K. Ne pas dupliquer tout le reçu et l'entrée dans outbox, journaux ou DLQ. 04/14/15. |
| Session et états de révocation | IDLE/ABSOLUTE bornent autorisation | Révocation = fin de droit, pas nécessairement purge de toute preuve. Supprimer le matériel inutilisable et garder uniquement les éléments anti-réactivation nécessaires selon durée explicite ; clés/epochs ne doivent pas reculer à la restauration. 03/04/14/15. |
| Reçu logout | 10 min candidates après un instant à préciser | Définir départ sur commit de révocation ou autre événement motivé, pas dernier retry ; limiter lien session/compte, état/instant et accès au besoin de confirmation. Après fenêtre : plus de lecture du reçu, purge bornée distincte ; jamais recréation de session. Audit éventuel séparé et justifié. 04/14/15. |
| Cookie de session invalidé et cookie de contrôle | Cookie session annoncé borné à ABSOLUTE ; contrôle distinct | Décrire expiry client réelle, non-renouvellement sur anonymous/erreur/GET, réception très tardive, fermeture/restauration navigateur, résidus de comptes précédents ; traiter séparément le cookie de contrôle et sa fenêtre. Nettoyage sûr respectant B et absence d'accès A ; aucun effacement global tardif imposé. 05/04/14. |
| Audit, diagnostic et refus | Rétention ouverte | Accès sécurité/Privacy selon dossier, support limité ; justification et durée propres, pas corps/secret/email/K brut. Si IP ou User-Agent ajoutés ultérieurement : nécessité et durée à examiner, aucune autorisation implicite par ce delta. 14/15. |
| Sauvegardes, répliques, outbox/DLQ, fournisseur email | Rétention ouverte et anti-résurrection demandé | Inventaire limité à ces données auth ; cycles d'expiration, ordre purge/restore, restrictions d'accès et destinataires. Mesure de retard de purge et alerte sur panne ; restauration n'expose pas de reçu expiré ni de session révoquée. 03/04/14. |

Qualification terminal à documenter : cookie de session, préauth, contrôle post-logout, stockage de génération et K côté client ; pour chacun, nécessité pour le service expressément demandé et durée. Le simple libellé « sécurité » ne valide pas une exemption de consentement. Comparer le reçu borné à l'alternative « résultat incertain + reprise explicite » déjà donnée par 04 ; arbitrer sur utilité et moindre collecte, sans en déduire que l'alternative est automatiquement meilleure.

Ne pas exiger la suppression immédiate de marqueurs anti-rejeu avant d'avoir établi comment le système rejette d'anciennes preuves. Inversement, la protection de restauration ne justifie pas la conservation perpétuelle des historiques de comptes d'un même navigateur. Le calendrier et la garantie anti-résurrection doivent être examinés ensemble.

## 5. Accès aux droits après restriction — dépendance Trust & Safety

Avis P15-L1-05 : **BLOQUANT au raccordement GAP-L1-05**, déjà ouvert dans l'entrée. Il n'est pas demandé d'implémenter immédiatement tous les lots de modération/droits ; il faut définir maintenant les frontières pour éviter une session qui bloque ces parcours futurs.

| État / situation | Exigence Privacy candidate | Réponse attendue de 09/04/14/10/05 |
| --- | --- | --- |
| Compte authenticated/restricted | Le statut social ne supprime pas automatiquement la possibilité de demander un droit | Matrice des actions de demande/suivi et vérification de propriété ; actions sociales interdites restent interdites |
| Capabilities vide ou code inconnu | Aucun privilège supposé ; voie alternative identifiable malgré l'absence de bouton autorisé | Lien/coordonnées d'un canal hors session, collecte minimale, responsable de réception et suivi ; ne pas inventer un token de contournement |
| Profil absent ou retiré | La titularité du compte est distincte de l'existence d'un profil public | Demande possible sans créer/rendre public un profil et sans disclosure à un tiers |
| Recovery réussie | Restrictions conservées, authentification et droits distincts | Reconnexion/voie de droits sans levée de sanction ; anti-fraude propre sans refus global automatique |
| Session compromise, compte fermé ou ancien membre | Vérification proportionnée et réponse possible sans session sociale valide | Circuit manuel ou dédié approuvé par 10/14/15 ; pas d'envoi d'archive avant vérification, pas de pièce civile systématique |
| Autorité de droits indisponible | Aucun accès privé accordé par défaut ; demande de droit ne doit pas disparaître | Canal de réception alternatif, accusé et horodatage réel ; reprise sans remise à zéro arbitraire du délai |
| Recours de modération | Parcours distinct d'une demande de droit RGPD | 09 décide recevabilité/réexamen et motifs communiqués ; 15 examine occultation des tiers et conservation, sans déterminer la sanction |

Questions **à transmettre à 09 (INT-0403 avec 10/14/15)** :
1. Quels états internes se projettent en restricted et lesquels exigent un accès hors session ? Fournir mapping sans révéler les motifs dans API-BE-049.
2. Quelles capacités minimales et notifications permettent de demander/suivre un droit et de contester une décision, sans rétablir publication/interactions ?
3. Qui traite la voie alternative si le compte/profil ne peut être rouvert, et quelles preuves proportionnées sont admissibles ?
4. Quels éléments des dossiers de sanction doivent être occultés pour préserver les tiers lors d'une demande d'accès ? Réponse ciblée seulement, pas réaudit de toute la politique de modération.

L'accès aux droits ne signifie pas accès libre à tous les dossiers ni effacement de toute sanction. Ne pas réutiliser un reçu logout ou un cookie de contrôle comme justificatif suffisant pour télécharger un export.

## 6. Critères Privacy proposés à QA — aucun test exécuté

Repères locaux V15, sans nouveaux TEST globaux. Ils complètent seulement l'oracle Privacy ; 18 reste propriétaire de la couverture complète des onze L1-BE et de leurs correspondances existantes. Tous **PLANNED** ; exécution impossible sans application et contrats approuvés.

| Critère local / rattachement | Précondition → action → résultat observable demandé | Preuve future |
| --- | --- | --- |
| V15-01 / L1-BE-03 | A anonyme/actif/restreint, profil présent/null → lire 049 → schéma autorisé uniquement, sans email, âge, motif, secret ni rôles ; aucun profil créé ; nécessité des refs documentée | Fixtures + réponses expurgées, validation serveur/client et liste champs attendus |
| V15-02 / L1-BE-03/04, GAP-05 | Titulaire restreint avec capacités vides/inconnues, puis profil supprimé → demander/suivre un droit par voie autorisée → réception vérifiable sans accès social, tiers refusé | Parcours/API + dossier fictif et horodatage ; matrice 09 préalable |
| V15-03 / L1-BE-01/02 | Opération committée, réponse perdue, K seul ou contexte tiers → replay → aucun reçu privé divulgué ni donnée précédente dans erreur ; contexte validé dans fenêtre reçoit seulement résultat minimal | Traces synthétiques et contrôle du contenu des erreurs |
| V15-04 / L1-BE-02/10 | Horloge avant/à/après chaque validité puis date de purge approuvée → replay et inspection des stores → refus à expiration, élimination selon calendrier, aucune nouvelle mutation par purge K | Horloge contrôlée, captures stores/DLQ/backup autorisées, preuves de purge sans secrets |
| V15-05 / L1-BE-05/08 | A puis B, ordre de réponses inversé, multi-onglets, retour historique → aucune vue/DTO/cache A rendu à B ; résidus cookies sans accès A et échéances vérifiées | Navigateur réel, stockage/historique/service worker, cookies et en-têtes avec valeurs masquées |
| V15-06 / L1-BE-06/08 | Logout A incertain puis login B ; reçu A rejoué avant/après fenêtre → pas d'identité A exposée, pas d'accès social par reçu, pas d'effacement B ; ancien reçu inaccessible après fenêtre | Réseau contrôlé, réponses/états et échéances ; corrélations fictives |
| V15-07 / L1-BE-09 | Recovery d'un compte restreint puis tentative d'accès aux droits → aucune sanction levée, voie de droits encore utilisable, aucune archive envoyée sans contrôle de titulaire | Sessions fictives multi-appareils et parcours de droits |
| V15-08 / L1-BE-10 | Purge/expiration réalisées puis restauration d'un backup ancien → absence de réactivation, de reçu expiré servi et de liens A/B inutilement reconstitués en service | Restore isolé, procédure et vérification avant ouverture ; rétention préalable définie |
| V15-09 / L1-BE-10/11 | Canaris fictifs secrets/email/DTO → erreurs et replay → canaris absents logs, audit, crash reporting, analytics ; seuls champs approuvés persistent | Inspection multi-destinations, aucune donnée réelle dans GitHub |

Les seules correspondances ci-dessus sont des propositions locales ; aucun mapping QA global n'est déclaré validé. Les preuves navigateur de L1-BE-08 ne peuvent être remplacées par une lecture Markdown ni par un test de DTO.

## 7. Questions, dépendances et critères de levée

| Repère | Destinataire / référence existante | Delta à fournir | État / effet |
| --- | --- | --- | --- |
| H15-L1-01 | 04/05, INT-0405/0407 | Usage consommateur par champ de 049, projection et exemples expurgés ; amendements 03/04 | À TRANSMETTRE ; gel projection concernée |
| H15-L1-02 | 04/14/03 avec 15, INT-0402/0404/0405 | Fiches de rétention §4, plafond contexte, séparation secret/reçu/audit, cookies et preuves de purge | À TRANSMETTRE ; blocage P15-L1-08 |
| H15-L1-03 | 09/10/04/14/05, INT-0403/0405 | Matrice restriction/capacités/voies de droits §5, rôle opérateur et réception en panne | À TRANSMETTRE ; blocage P15-L1-05 |
| H15-L1-04 | 18, INT-0408 | Intégrer ou amender V15-01–09 dans les TEST existants, préciser snapshots runtime et environnement | À TRANSMETTRE ; aucun PASS applicatif |
| H15-L1-05 | HQ/21/20 | Enregistrer avis 15 rendu sur SHA exact ; garder GAP ouverts et gate L1 ; vérifier futur delta sans refaire le corpus | Publication via PR ; réception/accord des discussions non attestés |

Levée proposée : 04 publie un delta ciblé citant chaque constat ; 05 justifie les consommateurs et parcours ; 09/10/14 fixent accès après restriction ; 04/14/15 arrêtent finalités/cycles motivés, avec conseil juridique si nécessaire ; 15 revoit uniquement ces changements puis 21 vérifie raccordements. Les valeurs techniques ne sont pas décidées par 15 seul. La validation documentaire éventuelle ne remplace pas les preuves d'implémentation ultérieures.

Risques ouverts : RISK-0403 (droits inaccessibles sous restriction), RISK-0404 (données/révocations restaurées), RISK-0405 (document pris pour protocole validé). Compléments locaux : corrélation multi-compte durable par contexte ; refs compte/profil reprises dans télémétrie ; TTL confondu avec effacement. Impacts de confidentialité élevés mais aucune exploitation ou probabilité mesurée.

## 8. Appuis juridiques limités et vérification documentaire

Sources officielles consultées le 30 septembre 2026 (Europe/Paris), sans revue de nouveaux pays/âges :
- [CNIL — RGPD chapitre II, articles 5 et 6](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre2) : nécessité/minimisation, limitation de finalité/conservation et choix du fondement selon opération. Ne prescrit pas les TTL Backend.
- [CNIL — RGPD chapitre III, article 12 et droits associés](https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre3) : faciliter l'exercice des droits et vérification d'identité adaptée. La matrice de canal restreint est une traduction produit proposée, pas un protocole légal imposé.
- [CNIL — cookies et autres traceurs](https://www.cnil.fr/fr/cookies-et-autres-traceurs/que-dit-la-loi) : examiner finalité des dépôts/lectures et conditions des exemptions. Aucun cookie du protocole proposé n'est déclaré exempt sur son seul nom.

Contrôles de cet avis : exactitude des références au SHA, présence des douze verdicts et de leurs propriétaires/corrections, neuf critères PLANNED, contenu ajouté isolé des travaux existants. Les commandes et résultats réellement obtenus, les blobs relus et la CI éventuelle sont consignés dans la PR de publication. Aucun code applicatif, test session/API/navigateur/sécurité/restore ou avis d'avocat n'a été exécuté/obtenu dans cette passe. Une CI documentaire réussie ne valide pas le protocole.

## 9. Compte rendu — sept rubriques

1. **Décisions** : avis 15 rendu ; 4 acceptations documentaires ciblées, 5 amendements, 2 blocages et 1 point hors mandat. Aucun choix de protocole, durée ou permission approuvé au nom des autres propriétaires.
2. **Livrable** : ce fichier, réponse indépendante au delta Backend SHA `1acf84fffcaa8131c0826d4874126e107a4cf978`, publié par PR séparée empilée sur #28 ; références de publication dans la PR.
3. **Tests exécutés** : contrôles documentaires de cette pièce uniquement selon compte rendu de publication ; V15 et L1-BE restent PLANNED, aucun test applicatif.
4. **Questions** : nécessité de deux refs côté client, mapping restricted/capacités, plafond des contextes, cycles de purge et voie de droits hors session.
5. **Dépendances** : H15-L1-01–05 ; demande Trust & Safety ciblée §5, sans avis 09 présumé.
6. **Risques** : droits bloqués, surconservation/corrélation, résidus cookies et réapparition après backup ; propositions ne valent ni conformité ni sécurité démontrées.
7. **Prochaines étapes / HQ** : transmettre les corrections aux propriétaires, recevoir deltas puis revue ciblée et convergence 21 ; L1 demeure BLOQUÉ POUR CODE. Aucun merge. Inter-discussions **À TRANSMETTRE**, même après publication GitHub.
