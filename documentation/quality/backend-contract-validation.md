# Vérification documentaire — contrats Backend M0

Date : 29 septembre 2026. Propriétaire : 04 Backend. Portée : [contrats candidats](../backend/api-contract-candidates.md) et [index Backend](../backend/README.md), référence d'entrée GitHub `dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957` de la PR nº 2.

La copie locale de référence contient 42 fichiers ; les blobs des six documents demandés (mandat, modèle, plan, vision, catalogue, parcours) ont été comparés aux lectures GitHub du SHA de référence : identiques. Son commit local de préparation est distinct du commit publié ; aucun faux SHA distant n'est utilisé. Le SHA publié et les résultats de CI sont consignés dans la PR de contribution.

## Contrôles exécutés

Exécution locale le 29 septembre 2026, Linux / Python 3.12.14, base locale `bfc0d4f` et delta des trois fichiers de cette contribution. La base locale est un instantané de préparation, pas le SHA GitHub. Commandes exécutées :

```sh
python3 scripts/repository/validate_repository.py
python3 -m unittest discover -s tests/repository -p 'test_*.py' -v
git diff --cached --check
```

Résultats : validateur PASS (45 fichiers suivis) ; 10 tests du validateur PASS ; contrôle des espaces PASS. Contrôle ponctuel Python exécuté : 48 définitions API-BE uniques, 18 AC-BE uniques, 18 TEST uniques ; chacune des 48 opérations référence un AC-BE ; toutes les références FEAT/AC-J explicites appartiennent aux sources ; aucun ID proposé TEST-04xx, INT-04xx, RISK-04xx, API-BE ou AC-BE ne préexiste dans les documents de la base locale. Contrôle des six blobs effectué avec `git hash-object` et comparaison aux SHA retournés par GitHub. Ces vérifications de texte ne prouvent pas la justesse fonctionnelle.

Delta : trois ajouts uniquement (contrats, index Backend, présent rapport). Relecture spécialisée locale : reprise anonyme à préciser, liste des blocages/préférences/file des recours encore à contractualiser, événements organisés historiques absents du catalogue HQ ; ces limites sont désormais explicites. Aucun fichier HQ modifié. CI distante non encore vérifiée à la rédaction ; son statut doit être consulté sur le commit publié et ne se déduit pas des contrôles locaux.

## Limites

Aucun test applicatif, API runtime, sécurité, permission, performance, migration ou restauration exécuté. Les exemples sont conceptuels et fictifs ; aucun schéma OpenAPI exécutable n'est revendiqué. Le validateur du dépôt vérifie nommage, fichiers, liens Markdown inline et règles limitées sur données sensibles ; il ne valide pas la sémantique des contrats, les ancres, les URL externes ou l'absence générale de secrets. Une vérification locale ne vaut ni revue indépendante ni validation des politiques proposées.

## Transmission

Revue de cette seule contribution à demander à 03/05/06/08/09/10/14/15/18/21 selon leur domaine. Statut : À TRANSMETTRE aux discussions. Les arbitrages OPEN-003/005/007 restent ouverts.
