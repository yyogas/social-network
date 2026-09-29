# Vérification du livrable M0-TEAM-17

## Vérification d'intégration v0.2 — périmètre courant

Complément de 21, 29 septembre 2026. Le tableau courant de l'index contient les 21 mandats, leurs chemins versionnés et les PR/SHA de réception. Les preuves locales de composition et la CI de synchronisation sont consignées dans la PR #17 ; aucune exécution applicative revendiquée. La revue du second agent distinct de l'auteur ne constitue pas une approbation humaine ni un avis spécialisé de 17/18/20.

Contrôle ponctuel courant reproductible depuis la racine du dépôt versionné :

```python
import pathlib, re, subprocess
root = pathlib.Path.cwd()
tracked = set(subprocess.check_output(["git", "ls-files"], text=True).splitlines())
orders = (root / "documentation/teams/work-orders.md").read_text()
targets = re.findall(r"\*\*Livrable propriétaire\*\* : `([^`]+)`", orders)
index = (root / "documentation/documentation-index.md").read_text().split("## Archive — index v0.1")[0]
assert len(targets) == len(set(targets)) == 21
for number, target in enumerate(targets, 1):
    assert target in tracked and (root / target).is_file(), target
    row = next(line for line in index.splitlines() if line.startswith(f"| M0-TEAM-{number:02} |"))
    assert f"[{target}]" in row and "REÇU ; PROPOSÉ" in row, row
print("PASS: 21/21 mandats reçus, liés et versionnés ; adoption métier non déduite")
```

## Archive — validation v0.1 et script de l'ancien instantané

Les résultats 44 fichiers / 10 tests et le script ci-dessous appartiennent exclusivement à l'ancien snapshot de la v0.1. Ce script suppose que seul le livrable 17 existe ; **ne pas l'exécuter comme contrôle du dépôt consolidé**. Les commandes, résultats et limites historiques restent inchangés pour audit.

Date : 29 septembre 2026. Propriétaire : 17 — Documentation. Destinataires : 18 QA, 20 Code Source, 21 Intégration et 00 MASTER. Statut : compte rendu de contrôles documentaires ; revue indépendante NON REÇUE.

## Références et méthode

- Référence GitHub : [PR #2](https://github.com/yyogas/social-network/pull/2), base `dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957` sur `documentation/m0-team-coordination`.
- Arbre Git source : `6f31f4b0559a7de490baf4bf730f415b66828d50`. Les 42 blobs téléchargés par le connecteur ont été comparés à leurs SHA Git ; aucun écart. L'arbre local avant modification est identique à l'arbre source. Le commit local de préparation n'est pas un commit distant et n'est pas poussé.
- Environnement des contrôles locaux : Linux 6.18.44, Python 3.12.14, bibliothèque standard ; copie intégrale des 42 fichiers, index Git local alimenté avec les changements documentaires.
- Delta : [index](../documentation-index.md), lien d'entrée dans [README](../../README.md), renvoi dans [plan](../documentation-plan.md), présent rapport. Aucun script, test ou paramètre CI modifié.
- Le SHA final de publication et les résultats CI éventuels sont liés par la PR de cette contribution. Les résultats ci-dessous concernent le contenu local dérivé de la base citée ; ils ne prétendent pas qu'une CI distante les a exécutés.

## Contrôles exécutés

| Contrôle | Commande ou méthode exacte | Résultat |
| --- | --- | --- |
| Identité du snapshot | Calcul SHA-1 Git de chaque blob et `git rev-parse HEAD^{tree}` avant delta | PASS : 42 blobs identiques et arbre source identique |
| Dépôt documentaire | `python3 scripts/repository/validate_repository.py` | PASS : 44 fichiers suivis ; disposition, noms, liens locaux et règles limitées de fichiers sensibles |
| Non-régression du validateur existant | `python3 -m unittest discover -s tests/repository -p 'test_*.py' -v` | PASS : 10 tests, 0 échec, 0 erreur |
| Espaces du delta | `git diff --cached --check` | PASS : sortie vide, code 0 |
| Couverture de l'index | `python3 ../verify-doc17.py` — script ponctuel reproduit ci-dessous | PASS : 39 fichiers Markdown reliés, 21 cibles, 34 FEAT / 5 phases, 31 références AC |

## Relecture de cohérence effectuée

- Installation, exploitation et contrats restent explicitement non vérifiés pour l'application ; un contrôle Python réussi ne devient pas une preuve applicative.
- Les classements des 34 FEAT sont repris comme propositions ; communautés conditionnelles et choix de surface non tranchés.
- Les 31 AC restent PLANNED ; aucune nouvelle identité TEST n'est attribuée à QA.
- Le tableau HQ demeure l'unique registre de transmission ; les handoffs de l'index sont À TRANSMETTRE.
- Les manques sont évalués au SHA source, pas sur toutes les branches ou discussions. Chaque cible absente est affichée en code, sans lien fictif.
- Les contradictions et ambiguïtés sont rattachées à des propriétaires et à un delta, sans demander de réanalyse complète.

## Limites et suites

Aucun test applicatif, E2E utilisateur, test de charge, déploiement, installation applicative, restauration ou exercice de gestion des droits n'a été exécuté. Les tests de procédure futurs AC-DOC17-04/05/07/08 restent PLANNED ; les vérifications ponctuelles de références ne les remplacent pas.

Le validateur existant couvre les chemins de liens Markdown inline, pas les fragments ni les URL externes ; sa règle de fichiers sensibles n'est pas un scanner complet de secrets. Les liens GitHub de référence ont été consultés par le connecteur ; aucune certification juridique ou d'accessibilité n'est déduite de leur présence. La revue de l'auteur ne vaut pas revue indépendante de 21.

Avant fusion : revue du delta par les owners concernés et 21, décision HQ si nécessaire, vérification des checks de la PR. Contribution empilée sur #2 ; après évolution de la base ou fusion de #2, vérifier le diff, retargeter si nécessaire et réexécuter les contrôles utiles. Rollback documentaire : revert ciblé en préservant les contributions postérieures et en vérifiant les liens ; aucune migration applicative concernée.

## Reproduire le contrôle ponctuel de couverture

Le script ci-dessous a été exécuté depuis la racine du snapshot Git indexé. Il est reproduit pour audit, sans ajout d’un nouveau contrôle CI ni modification des outils du dépôt. Le chemin `../verify-doc17.py` désigne le fichier temporaire utilisé durant cette exécution ; copier le bloc dans un fichier temporaire pour le rejouer.

```python
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re, subprocess

root = Path.cwd()
index = root / "documentation/documentation-index.md"
body = index.read_text()
tracked = subprocess.check_output(["git", "ls-files"], text=True).splitlines()
links = set()
for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", body):
    url = urlsplit(target)
    if not url.scheme and not url.netloc and url.path:
        links.add((index.parent / unquote(url.path)).resolve().relative_to(root).as_posix())
missing = sorted({p for p in tracked if p.endswith(".md")} - links)
assert not missing, missing
orders = (root / "documentation/teams/work-orders.md").read_text()
targets = re.findall(r"\*\*Livrable propriétaire\*\* : `([^`]+)`", orders)
assert len(targets) == 21 and len(set(targets)) == 21
for number, target in enumerate(targets, 1):
    row = next(l for l in body.splitlines() if l.startswith(f"| M0-TEAM-{number:02} "))
    assert f"`{target}`" in row
    assert ("AJOUTÉ" in row) == (number == 17)
    assert (root / target).exists() == (number == 17)
catalog = (root / "documentation/product/feature-catalog.md").read_text()
features = set(re.findall(r"^\| (FEAT-\d{3}) \|", catalog, re.M))
assert len(features) == 34
mentions = set(re.findall(r"FEAT-\d{3}", body))
for a, b in re.findall(r"FEAT-(\d{3}) à FEAT-(\d{3})", body):
    mentions |= {f"FEAT-{i:03}" for i in range(int(a), int(b) + 1)}
assert mentions == features, (mentions-features, features-mentions)
journeys = (root / "documentation/product/user-journeys.md").read_text()
criteria = set(re.findall(r"^\| (AC-J\d{2}-\d{2}) \|", journeys, re.M))
refs = set(re.findall(r"AC-J\d{2}-\d{2}", body))
for j, a, k, b in re.findall(r"AC-J(\d{2})-(\d{2}) à AC-J(\d{2})-(\d{2})", body):
    assert j == k
    refs |= {f"AC-J{j}-{i:02}" for i in range(int(a), int(b) + 1)}
assert len(criteria) == 31 and refs == criteria
expected = [("MVP",1,22),("Phase 2",23,28),("Phase 3",29,31),
            ("International",32,32),("Long terme",33,34)]
for phase, a, b in expected:
    for i in range(a,b+1):
        row=next(l for l in catalog.splitlines() if l.startswith(f"| FEAT-{i:03} "))
        assert row.split("|")[3].strip() == phase
assert "FEAT-020 reste conditionnelle" in body
print(f"PASS: {len([p for p in tracked if p.endswith('.md')])} Markdown files linked; "
      "21 owner targets; 34 FEAT/5 phases; 31 AC references.")
```
