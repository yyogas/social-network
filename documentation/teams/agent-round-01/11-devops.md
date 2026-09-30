# Agent 11 — Exploitation, restauration et CI

Avis documentaire indépendant du 30 septembre 2026, distinct d’une validation des équipes propriétaires. Périmètre : snapshot HQ fourni au SHA `4d3cd079e92217936af3292429a38f91f7b576ff`, workflow, scripts/tests, `operations-readiness.md`, `hosting-comparison.md`, `m0-branch-integration-status.md` ; Backend v0.3, PR #28 au SHA `0a7fcd54b996cc292bfe98c61a835613837def32`, C3/C4/C6/C7 ; avis sous-agents `02-security.md` et `04-privacy.md`. Les copies raw présentes à la racine de `sources` ne sont pas assimilées à des fichiers du dépôt. **Proposition seulement : aucun mécanisme adopté, aucun GO code ou pilote.**

## Constat utile

Le document exploitation pose correctement sauvegarde isolée, intégrité, droits, preuve horodatée et RPO/RTO mesurés. Il manque le raccordement exécutable aux sessions : une sauvegarde correcte peut restaurer un challenge consommé, une session révoquée ou un effacement disparu. Backend C4 exige donc le retrait de l’incarnation D avant réouverture ; restaurer D avec la base annulerait cette protection. Les avis sécurité et privacy maintiennent respectivement l’intégrité/admission et le calendrier des copies comme dépendances bloquantes.

Les objectifs hébergement — pilote 24 h/8 h, intermédiaire 1 h/4 h, premium 15 min/1 h — restent proposés et non mesurés. Ils ne prouvent ni continuité des révocations ni capacité RPO zéro. Les prix ne sont pas réévalués par cette mission.

## Runbook minimal proposé à 03/14/15/18

1. **Préparer une fixture synthétique datée.** Sauvegarder à t0 ; ensuite révoquer une famille F, effectuer un recovery avançant E, consommer un challenge/K, supprimer un compte et un média, puis relever les effets durables. Conserver les références minimales de révocation/effacement dans une autorité protégée du rollback, avec accès et rétention approuvés. Inclure une session indépendante témoin. Capturer les anciennes capacités uniquement dans le banc de test, jamais dans le rapport.
2. **Fermer et isoler.** Couper admissions et accès applicatifs, arrêter workers/outbox et les envois externes. Enregistrer l’incident, le point de restauration et les périmètres affectés ; clôturer les scopes et retirer D ancienne par une barrière indépendante de la sauvegarde. Si l’autorité ou cette clôture est invérifiable, rester fermé, conformément au 503 candidat. Une perte partielle silencieuse reste hors garantie tant que sa détection/prévention n’est pas démontrée.
3. **Restaurer sans exposer.** Restaurer base, objets et configuration dans un environnement isolé. Vérifier manifestes, intégrité et migrations. Établir D nouvelle avec un mécanisme que 03/14 doivent choisir : sa valeur et son autorité ne doivent pas reculer lors du retour à t0. Faire confirmer cette incarnation par chaque serveur, worker et chemin d’autorisation ; aucun cache ou réplica ancien ne peut accorder un accès.
4. **Réconcilier avant réouverture.** Réappliquer les révocations, restrictions et effacements postérieurs à t0 depuis le registre indépendant ; purger projections, caches, objets et files concernés. D nouvelle interdit les anciennes capacités, mais ne retire pas à elle seule un contenu effacé de la base restaurée. Une lacune du registre d’effacement impose de maintenir le périmètre fermé. Documenter séparément les copies encore conservées et leur échéance, sans prétendre à un effacement physique total.
5. **Prouver puis ouvrir.** Rejouer anciennes sessions, preuves recovery, K, reçus expirés et messages tardifs : aucun accès, second effet, réenvoi logique ou réapparition de données supprimées. Vérifier une authentification fraîche autorisée et un compte témoin selon la portée ratifiée. Mesurer RPO/RTO et retard de purge ; réouverture seulement après contrôles signés par propriétaires. Toute anomalie ramène à l’état fermé.

## Journal et preuves attendus

Le dossier d’exercice conserve SHA/contrat, identifiant de sauvegarde, heures serveur, aliases D avant/après, ordre clôture–restauration–réconciliation–ouverture, compteurs d’effets et résultats expurgés. Distinguer audit obligatoire lié au commit durable et diagnostic d’exploitation ; tester les crashs avant/après commit sans interpréter un timeout comme rollback. Exclure corps, email, K brut, cookies et secrets. Accès, durées et purge du journal restent à ratifier. TEST-1840 couvre le raccordement restauration proposé ; l’extension auth de TEST-1847 reste à adopter par QA.

## Vérifiable maintenant / futur

**Exécuté localement :** `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests/repository -p 'test_*.py' -v` : **24 tests OK**, exit 0. Le dossier fourni n’est pas un checkout Git ; aucun PASS du validateur global ou du delta réel n’est revendiqué.

**CI constatée dans le fichier :** pull_request et push main ; Ubuntu 24.04, timeout 5 minutes ; checkout épinglé `11d5960a326750d5838078e36cf38b85af677262`, credentials désactivés, historique complet ; commandes `validate_repository.py`, unittest puis `check_whitespace.py`. Portée : structure/liens locaux/fichiers sensibles et whitespace, sans ancres/URL externes ni tests applicatifs. Permissions inchangées : `contents: read`.

**Toujours ouverts :** FIND-21-02 protection de branche ; FIND-21-05 dépréciation Node20 du checkout, sans recommandation de version non vérifiée. Les anciens runs du bilan restent historiques. Restauration, barrière D, audit runtime, purge, charge et objectifs de reprise restent futurs, non exécutés.
