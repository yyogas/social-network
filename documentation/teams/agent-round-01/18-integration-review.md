# Agent 18 — revue indépendante d’intégration des avis 01–12

Avis documentaire du 30 septembre 2026. Corpus : sorties locales 01–12 ; Backend PR #28, SHA `0a7fcd54b996cc292bfe98c61a835613837def32` ; Architecture PR #33, SHA `a7901fc87e79975d8963e909a89fc8150410e40a`. Les numéros de lignes ci-dessous désignent les copies dans `agent-round`. Aucun avis propriétaire remplacé, test runtime exécuté, mécanisme adopté ou statut distant modifié.

**Avis de publication : favorable à une PR documentaire après les corrections minimales ci-dessous, avec L1 toujours BLOQUÉ POUR CODE.** La rédaction peut avancer immédiatement ; la publication ne constitue ni ratification technique, ni acceptation produit, ni clôture des constats.

## 1. Élevée — clôture QA-A trop large

**Sources :** `outputs/05-qa.md:15,27,43` ; `outputs/01-backend.md:28,40–44` ; `outputs/10-data-model.md:30–32` ; `sources/backend-pr28-v03.md:571,576,622,628` ; `sources/architecture-pr33.md:57,92,208`.

QA propose de lever l’ambiguïté documentaire L1-BE-07 et d’annoncer « continuation F puis logout 204 ». Or, si la continuation avance T, le logout préparé à T ancien rencontre le refus C5. La cible immuable F empêche de viser B ; elle ne prouve pas que l’ancienne autorisation reste valable. Architecture exige elle aussi une version attendue, tout en proposant le succès après une transition gagnante. L’exception de reçu B ne résout rien ici : elle relit un résultat déjà acquis et n’autorise pas la première mutation de révocation.

**Impact :** clôturer QA-A en entier ou rendre 07-b déterminable autoriserait deux résultats incompatibles, 204 et 409, pour la même trace. Les progrès sur logout gagnant, nouvelle intention et login indépendant restent recevables séparément.

**Correction exacte :** remplacer la proposition de levée par « QA-A partiellement précisé ; continuation F/T encore À AMENDER ». Remplacer 07-b par « 204 conditionnel à une précondition terminale explicitée ; si T présenté est obsolète et aucune exception définie, appliquer C5 : 409 sans mutation ». Demander de préciser si la continuation avance T et, sinon, quelle version elle préserve ; si une exception est proposée, définir sa preuve, sa portée F et son expiration. Aucun reciblage vers B. Reporter ce statut dans la synthèse sans modifier les avis sources.

## 2. Élevée — recommandation A susceptible de devenir un défaut implicite

**Sources :** `outputs/02-security.md:39` ; `outputs/06-architecture.md:3,25,27` ; `outputs/03-web.md:5,14–18` ; `outputs/07-product.md:15–26` ; `sources/backend-pr28-v03.md:527–532` ; `sources/architecture-pr33.md:32,48`.

Les recommandations divergent réellement : A exige une nouvelle authentification après perte de vue, y compris reload ordinaire ; Web/Produit souhaitent une continuité vérifiée. Ce désaccord de politique n’invalide pas les invariants communs. Cependant, « appliquer A jusqu’à décision contraire », même dans un brouillon PROPOSÉ, pourrait être repris comme décision provisoire déjà effective. Différer le reçu B ne permet pas de différer automatiquement la continuité nécessaire au parcours retenu.

**Impact :** promesse UX amoindrie sans arbitrage, ou reprise privée indûment autorisée après disparition d’un logout jamais reçu. Aucune des deux positions ne prouve l’exclusivité entre racines indépendantes.

**Correction exacte :** « A est une option soumise à HQ ; aucune politique de reprise n’est modifiée par cette PR. » Présenter à HQ trois décisions séparées : reprise ordinaire et preuve de continuité ; maintien du verrou après sortie incertaine ; portée du dernier login. Documenter pour chaque alternative conséquence utilisateur, information requise et limite après perte totale. Si la continuité nécessaire n’est pas démontrable, laisser explicitement ouvert le choix entre coût de A et réduction de garantie ; ne choisir ni l’un ni l’autre dans la synthèse.

## 3. Moyenne — matrices de droits sûres en lecture complète, à rendre autonomes

**Sources :** `outputs/08-trust-safety.md:11,19–25,31–33` ; `outputs/09-support.md:13–21` ; `outputs/04-privacy.md:39–45` ; `outputs/12-localization-ux.md:17`.

Aucun export avant vérification ni récupération levant les restrictions n’est accordé par ces textes. La réception anonyme est distincte du suivi privé et de la livraison ; email déclaré, ticket et reçu logout ne prouvent pas la titularité. Les sanctions survivent à recovery, et Support ne restaure pas l’accès social. La ligne export 08, extraite seule, ne rappelle toutefois pas ces conditions.

**Impact :** risque de mauvaise reprise rédactionnelle, pas contournement démontré. **Correction minimale :** ajouter dans cette ligne « demande neutre recevable ; suivi privé et téléchargement uniquement après preuve du sujet et autorisation propre, revérifiées au téléchargement ». Ajouter « recovery ne modifie aucune restriction » dans la ligne compte. Garder P15-L1-05/QA-E ouverts : la matrice candidate ne crée pas un canal actif.

## 4. Faible — notation et portée des preuves

**Sources :** `outputs/05-qa.md:22` ; `outputs/10-data-model.md:32` ; `outputs/11-devops.md:25–29`. Uniformiser la déconnexion en Q ou `commit_logout`, réserver D à l’incarnation. Les 24 tests de dépôt rapportés par 11 ne prouvent aucun invariant applicatif. La PR peut publier les amendements, désaccords et besoins restants avec scénarios PLANNED ; elle ne doit annoncer ni READY, ni PASS runtime, ni adoption A/B, ni fermeture propriétaire.
