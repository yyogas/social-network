# Vérification documentaire du plan Growth

**Portée historique :** contrôles de la contribution Growth v0.2 à la révision ci-dessous. Le delta de positionnement DIR-012 du 30 septembre 2026 produit la v0.3 du plan ; les résultats et le hash ci-dessous ne lui sont pas attribués. Ses contrôles courants sont consignés dans la PR #27.

Date : 29 septembre 2026. Propriétaire : 19 — Growth. Statut : contrôles documentaires locaux exécutés et réussis ; revue indépendante attendue. Aucun test applicatif.

Référence source : dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957, PR #2. Les 42 fichiers de cet instantané ont été récupérés avec le connecteur GitHub et leurs SHA de blob ont été recalculés localement : 42 identiques, aucun écart. Le commit de préparation local est distinct du commit distant et n'est pas poussé.

## Périmètre et environnement

Périmètre du delta : [plan pilote](pilot-launch-plan.md), [index Growth](README.md) et ce rapport. Les scénarios AC-G19-01 à AC-G19-18 restent PLANNED.

- Environnement : Linux 6.18.44 x86_64 ; Python 3.12.14 ; Git 2.51.1.
- Corpus : 42 fichiers source + 3 fichiers Growth, soit 45 fichiers suivis dans l'instantané local.
- Identification du plan effectivement contrôlé : SHA-256 `f0ac91cf45ac3cc09297f22a10fc02ad5fc8a3016029aa6dbb936331879d4236`.
- Le SHA Git publié figure dans la PR de contribution. Les SHA de blob et d'arbre servent à vérifier que les fichiers distants correspondent aux fichiers préparés ; un commit local de reconstitution n'est pas assimilé à un commit GitHub.

## Commandes réellement exécutées

Depuis la racine du dépôt reconstitué :

```sh
git add documentation/growth
python3 scripts/repository/validate_repository.py
python3 -m unittest discover -s tests/repository -p 'test_*.py' -v
git diff --cached --check
```

| Contrôle | Résultat observé |
| --- | --- |
| Validateur du dépôt | PASS : 45 fichiers ; arborescence requise, noms, liens locaux de fichiers et règles de fichiers sensibles |
| Tests existants du validateur | 10 tests exécutés, 10 réussis, sortie OK ; aucun test applicatif |
| Espaces / diff indexé | Code de sortie 0, aucune erreur |
| Vérification des 42 blobs source | 42 identiques aux SHA du tree GitHub de référence, zéro écart |

Contrôle ponctuel ciblé également exécuté, sans ajout de script au produit :

```sh
python3 - <<'PY'
from pathlib import Path
import re, hashlib
p=Path('documentation/growth/pilot-launch-plan.md')
s=p.read_text()
refs={f'FEAT-{n:03d}' for n in range(1,35)}
used=set(re.findall(r'FEAT-\d{3}',s))
assert not used-refs, used-refs
for label, count in [('AC-G19',18),('TEST',18)]:
 pattern=r'^\| (AC-G19-\d{2}) \|' if label=='AC-G19' else r'\| (TEST-19\d{2}) /'
 ids=re.findall(pattern,s,re.M)
 assert len(ids)==count and len(set(ids))==count, (label,ids)
rows=[line for line in s.splitlines() if line.startswith('| AC-G19-')]
assert all('PLANNED' in line for line in rows)
assert len(re.findall(r'^\| REQ-19\d{2} ',s,re.M))==11
assert len(re.findall(r'^\| INT-19\d{2} ',s,re.M))==9
assert len(re.findall(r'^\| RISK-19\d{2} ',s,re.M))==6
for line in s.splitlines():
 if line.startswith('|'):
  assert line.endswith('|'),line
assert (24+4*26)*40*1.25==6400
assert (36+4*52)*40*1.25==12200
print('PASS: 11 besoins, 9 demandes, 6 risques, 18 critères et 18 tests proposés uniques ; critères PLANNED ; références FEAT explicites dans 001–034 ; calculs S1/S2 cohérents.')
print('SHA256 plan:',hashlib.sha256(p.read_bytes()).hexdigest())
print('Limites: références abrégées FEAT, pertinence métier, permissions et conformité exigent une revue humaine ; contrôle de structure seulement.')
PY
```

Résultat : code de sortie 0 ; comptages et calculs attendus confirmés ; empreinte ci-dessus obtenue. Les propositions d'IDs ont aussi été recherchées dans le corpus source : aucune occurrence préexistante pour les préfixes locaux 19 concernés. Les collisions avec les contributions d'autres branches restent à contrôler par 17/HQ avant intégration.

## Relecture ciblée et limites

Relecture de l'auteur : audience initiale alignée sur DIR-002 ; option communautés toujours conditionnelle ; invitations et pages publiques identifiées comme contrats manquants ; S1/S2 séparés d'un devis ; cohorte immature non présentée comme R30 ; comptes fondateurs et interventions d'équipe distingués ; aucun statut applicatif PASS ; transmissions inter-discussions toujours À TRANSMETTRE. Cette relecture n'est pas une revue indépendante.

Les contrôles automatiques ne vérifient pas les ancres Markdown, URLs externes, règles de droit, sécurité effective, pertinence des seuils, capacité humaine ni exactitude exhaustive des références FEAT abrégées. Le validateur n'est pas un scanner complet de secrets. Aucun entretien, recrutement, benchmark, contrôle d'installation, test E2E, campagne ou test de charge exécuté.

Les résultats CI distants et le SHA exact de publication doivent être consultés dans la PR ; aucun résultat CI n'est supposé sur la seule base de cette vérification locale. Réexécuter les contrôles sur tout delta et après changement de branche de base.
