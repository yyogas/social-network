# Rapport de contrôles — livraison QA M0

## Identification et périmètre

- Date : 29 septembre 2026 ; session de contrôle locale autour de 19:29 UTC (21:29 Europe/Paris).
- Propriétaire : 18 QA ; revue indépendante de 21 NON REÇUE.
- Base distante : `dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957`, [PR nº 2](https://github.com/yyogas/social-network/pull/2).
- Lecture de main à la préparation : `46a4f36ba827b978bba57acf72ed9282ecb48b8a`. Publication prévue en PR empilée sur `documentation/m0-team-coordination` pour isoler le delta QA.
- Environnement réellement utilisé : Linux 6.18.44 x86_64, Python 3.12.14, Git 2.51.1.
- Les 42 fichiers texte de la base ont été lus par l’accès GitHub et matérialisés dans un espace isolé. Leurs SHA de blobs Git ont été recalculés : 42 concordances. Un historique Git local de préparation a été créé pour exécuter le validateur ; il n’est pas l’historique distant et ne doit pas être poussé.
- Aucun AGENTS.md présent dans l’arbre de la base consultée. Conventions et CONTRIBUTING lus.
- Delta : [matrice d’acceptation](acceptance-test-matrix.md) nouvelle, [stratégie existante](test-strategy.md) enrichie, présent rapport nouveau. Aucun code applicatif, workflow, registre HQ ou catalogue produit modifié.

## Résultats réellement obtenus

| Contrôle | Commande / résultat |
| --- | --- |
| Validation du dépôt | `python3 scripts/repository/validate_repository.py` — PASS : 44 fichiers suivis, organisation, noms, liens locaux et règles de fichiers sensibles du validateur |
| Tests existants du validateur | `python3 -m unittest discover -s tests/repository -p 'test_*.py' -v` — 10 tests, OK |
| Espaces du delta | `git diff --cached --check` après `git add documentation/quality` — code 0, aucune sortie |
| Traçabilité QA | Commande Python ci-dessous — PASS : 48 IDs de test uniques, 31/31 AC reliés, 34 phases/priorités FEAT conservées, 13 dépendances résolues |
| Revue documentaire par l’auteur | États, refus, fixtures, phases, transmission, limites et anciennes références rapprochés ; ce n’est pas une revue indépendante |
| Tests applicatifs | 0 exécuté ; 48 définis avec statut BLOCKED. Installation, charge, rollback et restauration applicatifs non exécutés |
| CI distante du commit QA | État à consulter dans la PR ; aucune réussite distante n’est déduite des contrôles locaux |

Sorties locales pertinentes :

```text
PASS: 44 tracked files; required layout, names, local file links, sensitive-file rules
Scope: inline Markdown file links only; no fragment/external URL check; not a complete secret scanner.
test_ambiguous_name_is_rejected (test_repository_validation.RepositoryValidationTests.test_ambiguous_name_is_rejected) ... ok
test_broken_link_is_rejected (test_repository_validation.RepositoryValidationTests.test_broken_link_is_rejected) ... ok
test_environment_example_is_allowed (test_repository_validation.RepositoryValidationTests.test_environment_example_is_allowed) ... ok
test_environment_file_is_rejected (test_repository_validation.RepositoryValidationTests.test_environment_file_is_rejected) ... ok
test_external_link_does_not_need_network (test_repository_validation.RepositoryValidationTests.test_external_link_does_not_need_network) ... ok
test_fenced_example_is_not_a_link_requirement (test_repository_validation.RepositoryValidationTests.test_fenced_example_is_not_a_link_requirement) ... ok
test_link_escape_is_rejected (test_repository_validation.RepositoryValidationTests.test_link_escape_is_rejected) ... ok
test_missing_layout_is_rejected (test_repository_validation.RepositoryValidationTests.test_missing_layout_is_rejected) ... ok
test_private_key_marker_is_rejected_without_disclosing_value (test_repository_validation.RepositoryValidationTests.test_private_key_marker_is_rejected_without_disclosing_value) ... ok
test_valid_local_link_and_standard_names (test_repository_validation.RepositoryValidationTests.test_valid_local_link_and_standard_names) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.004s

OK
PASS: 48 unique cases BLOCKED; 31/31 AC mapped; 34 FEAT phases/priorities preserved; 13 dependencies resolved.
```

## Commande exacte du contrôle de traçabilité

Exécuter depuis la racine du dépôt ; ce contrôle vérifie la structure documentaire et n’exécute aucun comportement produit.

```sh
python3 - <<'PY_QA'
import re
from pathlib import Path
q = Path('documentation/quality/acceptance-test-matrix.md').read_text()
j = Path('documentation/product/user-journeys.md').read_text()
c = Path('documentation/product/feature-catalog.md').read_text()
rows = re.findall(r'^\| (TEST-18\d{2}) ; ([^|]+)\|([^\n]+)', q, re.M)
assert len(rows) == len({r[0] for r in rows}) == 48
assert {r[0] for r in rows} == {f'TEST-{i}' for i in range(1801,1849)}
ac = re.findall(r'^\| (AC-J\d{2}-\d{2}) \|', j, re.M)
mapped = [re.search(r'AC-J\d{2}-\d{2}',r[1]).group() for r in rows if 'AC-J' in r[1]]
assert len(ac) == len(mapped) == 31 and set(ac) == set(mapped)
for ident, req, rest in rows:
    assert 'BLOCKED' in rest and f'E({ident}) vide' in rest
    assert 'D-' in rest and re.search(r'R[1-9]',rest)
    assert not re.search(r'\| (?:PASS|FAIL|READY|RUNNING) ;',rest)
assert len(re.findall(r'^\| FEAT-\d{3} \|',q,re.M)) == 34
cat = {r[0]:(r[2],r[3]) for r in (line.strip('|').split(' | ') for line in c.splitlines() if line.startswith('| FEAT-'))}
qat = {r[0]:(r[2],r[3]) for r in (line.strip('|').split(' | ') for line in q.splitlines() if line.startswith('| FEAT-'))}
assert cat == qat, 'phase or catalog priority mismatch'
declared = set(re.findall(r'^\| INT-18\d{2} / (D-[A-Z]+)',q,re.M))
used = set(re.findall(r'D-[A-Z]+',' '.join(r[2] for r in rows)))
assert used <= declared, used-declared
assert len(declared) == 13
print('PASS: 48 unique cases BLOCKED; 31/31 AC mapped; 34 FEAT phases/priorities preserved; 13 dependencies resolved.')
PY_QA
```

## Empreintes des documents vérifiés

```text
034ad991fef3f460ba86549659c2a4e9463c3b9dad4e8004bb9313bfdf60923e  documentation/quality/acceptance-test-matrix.md
119d4b32b06c73474f117656320bcf12dbd1cf282fa5e0e31aa8edf649ccc186  documentation/quality/test-strategy.md
```

Ces empreintes SHA-256 portent sur les octets locaux vérifiés. Le commit distant et le lien de PR seront indiqués dans le compte rendu de publication ; ne pas substituer un commit local préparatoire. Le rapport décrit son propre lot sans se prétendre preuve d’une application fonctionnelle.

## Limites et suite

Le validateur ne teste que les liens Markdown inline de fichiers, sans fragments ni URLs externes ; il ne constitue pas un scan de secrets complet. Le contrôle de traçabilité ne prouve pas l’exhaustivité fonctionnelle, la pertinence de toutes les assertions ni l’absence de collision d’IDs sur d’autres branches. La couverture 31/31 désigne un mapping documentaire. Les contrôles système du futur produit sont décrits, pas réalisés.

Revue attendue de 17/21 et des propriétaires ciblés. Les demandes INT-1801 à INT-1813 et la proposition DEC-1801 restent À TRANSMETTRE ; leur publication ne vaut pas réception. Après fusion des PR parentes, retargeter la PR QA vers la branche d’intégration désignée par HQ et contrôler à nouveau son diff/CI. Revenir sur ce delta documentaire par revert ciblé après examen des contributions ultérieures ; aucune migration runtime.
