# Validation documentaire — équipe 16 / M0

Date : 29 septembre 2026. Propriétaire : 16 — International / Localisation.
Statut : compte rendu de contrôles documentaires ; aucune validation fonctionnelle ou approbation indépendante.

## Référence et périmètre

Entrée distante : PR [#2](https://github.com/yyogas/social-network/pull/2), commit `dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957`.
Le snapshot local de préparation porte le commit `107d13d7e972ef2457287be988716601f6018e17` : ce SHA local n'est pas présenté comme un commit GitHub.
Les blobs locaux des six entrées mandat, modèle, plan, vision, catalogue et parcours ont été comparés aux blobs lus via GitHub au SHA distant : six correspondances exactes.

Delta : [spécification v0.2](../international/localization-requirements.md), [index de domaine](../international/README.md) et ce rapport. Aucun code applicatif modifié.

## Contrôles

Environnement : Linux, Python 3.12.14. Exécution sur le snapshot local indiqué ci-dessus avec les trois fichiers du delta ajoutés à l'index. Le commit distant de livraison sera indiqué dans la PR ; il ne doit pas être confondu avec la référence d'entrée.

| Commande exécutée | Résultat observé |
| --- | --- |
| `python3 scripts/repository/validate_repository.py` | PASS : 45 fichiers suivis ; structure, nommage, liens locaux et règles de fichiers sensibles |
| `python3 -m unittest discover -s tests/repository -p 'test_*.py' -v` | PASS : 10 tests du validateur, aucun échec |
| `git diff --cached --check` | PASS : code de sortie 0, aucune erreur d'espacement |
| `python3 --version` | Python 3.12.14 |

Contrôle ponctuel supplémentaire exécuté avec `python3 -` : 13 identifiants REQ uniques et séquentiels, 18 AC uniques et séquentiels, toutes les références FEAT présentes dans le catalogue et 18 lignes de tests au statut PLANNED. Vérification des quatre heures d'exemple avec `datetime` et `zoneinfo` locaux : Paris 17:00, Alger 16:00, Toronto 11:00 et Londres 16:00 pour l'instant `2026-09-29T15:00:00Z`. Résultat : PASS documentaire, sans prétendre tester une application ni choisir la version de données de fuseaux de production.

## Limites

Les tests TEST-1601 à TEST-1618 sont PLANNED, sans application à exécuter. Aucun test E2E, API, sécurité, accessibilité ou humain de traduction n'a été exécuté. Le validateur du dépôt ne vérifie ni fragments Markdown, ni URL externes, ni conformité réglementaire et ne constitue pas un scanner complet de secrets. Les collisions avec les contributions des autres branches doivent encore être examinées par 17/21 lors de l'intégration.

## Revue et suite

Sources techniques primaires de la spécification consultées le 29 septembre 2026. Relecture locale : phases, états, droits, données, contrats candidats, glossaire, critères et handoffs présents ; aucun pays/langue déclaré ouvert. Avis 01/02/04/09/14/15/18/19 et revue indépendante 21 restent attendus. La publication du document n'atteste pas la réception par les discussions.
