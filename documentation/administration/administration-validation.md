# Vérification documentaire — équipe 10

Date : 29 septembre 2026. Propriétaire : 10 ; revue indépendante attendue de 21. Périmètre : [spécification FEAT-017](administration-support-requirements.md) et index de domaine.

## Provenance et portée

Référence GitHub d'entrée : PR #2, commit `dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957`. Les 42 blobs de cette révision ont été récupérés via GitHub et vérifiés par leur empreinte Git SHA-1 avant contrôle. Le clone réseau direct était indisponible ; le dépôt local sert uniquement de copie de validation. Son commit local `928b9d2` n'est pas un commit GitHub et ne doit pas être publié comme historique du projet.

Delta prévu : trois fichiers Markdown dans ce domaine. Aucune modification applicative, de politique approuvée, du catalogue ou du registre HQ. Les résultats et empreintes du delta publié sont consignés dans la PR ; ils ne sont pas attribués au SHA d'entrée.

## Résultats

Environnement : Linux, Python 3.12.14 ; copie locale de la révision d'entrée, plus les trois fichiers de ce delta. Contrôles exécutés le 29 septembre 2026 après mise à l'index des documents :

| Commande | Résultat observé |
| --- | --- |
| `python3 scripts/repository/validate_repository.py` | PASS : 45 fichiers suivis ; structure, nommage, liens locaux et règles limitées de fichiers sensibles |
| `python3 -m unittest discover -s tests/repository -p 'test_*.py' -v` | OK : 10 tests du validateur exécutés, aucun échec |
| `git diff --cached --check` | Code retour 0, aucune erreur d'espacement |

Contrôle Python ciblé exécuté via entrée standard : toutes les références FEAT appartiennent au catalogue ; 15 critères AC-ADMIN uniques sont PLANNED ; aucun identifiant candidat INT/RISK/TEST de ce lot ne figure dans les Markdown du snapshot d'entrée ; colonnes des tableaux cohérentes. Relecture de la matrice et des parcours : les propositions ne sont pas marquées approuvées ; décisions, exécutions, notifications et réparations sont distinguées. Ce contrôle d'IDs ne réserve pas les numéros contre des contributions concurrentes ultérieures.

Aucun test applicatif exécuté. Les 15 scénarios de la spécification restent PLANNED. Le SHA GitHub du delta est enregistré dans la PR après publication ; il doit être contrôlé avant d'attribuer ces résultats à une autre révision.

## Limites et suite

Le validateur contrôle noms, présence de fichiers, liens Markdown inline et certaines règles de fichiers sensibles. Il ne vérifie ni ancres, ni URLs externes, ni exhaustivité de détection des secrets. Les tests du validateur ne sont pas des tests du réseau social. La cohérence documentaire ne valide pas une permission, une politique métier ou la conformité juridique.

Revue 21 et avis ciblés 09/14/15/04 attendus avant fusion ou adoption. Rollback documentaire : revert du delta après contrôle des contributions suivantes ; aucune migration ni action de données à annuler.
