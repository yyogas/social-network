# Rapport de validation M0

Date : 29 septembre 2026. Portée : conventions, documentation et validateur du dépôt. Les résultats de CI sont ceux du commit de la pull request, consultables dans GitHub Actions.

| Vérification | Commande / preuve | Statut |
| --- | --- | --- |
| Dépôt et liens Markdown locaux | `python3 scripts/repository/validate_repository.py` | PASS — exécuté localement |
| Cas de non-régression du validateur | `python3 -m unittest discover -s tests/repository -p 'test_*.py' -v` | PASS — exécuté localement |
| Espaces et fins de lignes | `git diff --cached --check` | PASS — exécuté localement |
| Checkout propre | Clone local isolé puis mêmes commandes | PASS — 32 fichiers, 10 tests |
| GitHub Actions — exécution historique #1 | [Run 36615257604](https://github.com/yyogas/social-network/actions/runs/36615257604), job 109566513206 | PASS observé ; portée limitée ci-dessous |
| Installation applicative sur OS vierge | Aucune application installable dans M0 | BLOCKED |
| API, permissions et end-to-end du produit | Implémentation non reçue | BLOCKED |
| Charge et restauration applicatives | Infra et contrats non validés | BLOCKED |

Le contrôle de secrets détecte des noms de fichiers interdits et marqueurs de clés privées ; il ne détecte pas toutes les données personnelles ou formes de credentials. Le vérificateur de liens couvre les fichiers des liens Markdown inline, pas les ancres, liens de référence ou disponibilités HTTP. Le checkout propre ne remplace pas une installation sur machine vierge.

Exécution locale : Linux, Python 3.12.14 ; 32 fichiers contrôlés ; 10 tests du validateur réussis. Le premier contrôle des espaces a détecté une fin de ligne avec espaces dans le registre ; correction appliquée et contrôle relancé avant commit.

Checkout propre testé : commit local `6a10b8d`, créé uniquement à partir des fichiers versionnés ; `git clone --no-local` dans un nouveau dossier, mêmes commandes et `git show --format= --check HEAD` exécutés avec succès. La publication API GitHub peut avoir un autre SHA pour le même contenu ; le run CI de la PR est la preuve attachée au commit distant. Les mises à jour de ce rapport ajoutent uniquement les résultats.


## Observation historique corrigée — FIND-21-03

Logs GitHub relus le 29 septembre 2026 : head proposé `8590a095d76965880e94614328a8eafbe09b93cb`, base `46a4f36ba827b978bba57acf72ed9282ecb48b8a`, merge synthétique réellement checkout `bdb6f3b14caa257c533a64ee4a40dbddeee701e5`. Le run ci-dessus a réussi avec 10 tests du validateur. Son succès est historique : il ne valide ni un correctif ultérieur ni l'absence de défaut du contrôle des espaces. FIND-21-01 décrit précisément la limite de ce contrôle sur un commit de merge.

Le [correctif de validation](foundation-validation-fix.md) ajoute les preuves de non-régression et sépare les constats traités des décisions de gouvernance restant ouvertes.
