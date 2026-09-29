# Validation documentaire — équipe 11 Publicité / Ads Manager

Date : 29 septembre 2026. Portée : contribution M0-TEAM-11, version documentaire 0.1.

## Référence et limites

- Entrée distante : PR [#2](https://github.com/yyogas/social-network/pull/2), commit `dd7db8c7aec3ea9779e3fb9a9aadec7b3a732957`.
- Les 42 fichiers de ce commit ont été récupérés via le connecteur GitHub dans un snapshot local isolé. Son historique Git local est un support de validation, pas l'historique distant et ne sera pas poussé.
- Delta : `documentation/advertising/README.md`, [options publicitaires](../advertising/advertising-options.md), ce rapport.
- Aucun fichier applicatif, migration, intégration fournisseur ou modification des registres HQ.
- Les contrôles portent sur les fichiers de cette contribution ; le SHA distant de publication sera indiqué dans la PR. Les critères AC-ADS-01 à AC-ADS-15 restent PLANNED, tests applicatifs non exécutés.

## Commandes et résultats

Environnement local : Linux 6.18.44 x86_64, Python 3.12.14. Exécution le 29 septembre 2026, terminée à 19:24 UTC avant publication ; entrée SHA ci-dessus plus le delta documentaire. Les 42 blobs d'entrée correspondent aux SHA Git distants, contrôle `git hash-object` fichier par fichier réussi.

| Commande / contrôle réel | Résultat observé |
| --- | --- |
| `python3 scripts/repository/validate_repository.py` | PASS : 45 fichiers suivis ; structure, noms, liens Markdown locaux et règles limitées de fichiers sensibles. |
| `python3 -m unittest discover -s tests/repository -p 'test_*.py' -v` | PASS : 10 tests du validateur, 0 erreur/échec, exécution initiale 0,005 s. |
| `git diff --cached --check` | PASS : sortie vide, code 0. |
| Contrôle Python ciblé des critères / références / arithmétique / tables | PASS : 15 AC-ADS uniques, séquentiels et PLANNED ; références FEAT présentes au catalogue ; trois scénarios et contributions exacts ; largeur des tables cohérente. |

Sortie conservée du validateur :

```text
PASS: 45 tracked files; required layout, names, local file links, sensitive-file rules
Scope: inline Markdown file links only; no fragment/external URL check; not a complete secret scanner.
```

Les contrôles ne vérifient pas les ancres ou URLs externes, ni la conformité juridique, ni les comportements Ads. Aucun test applicatif n'a été exécuté ; la CI distante sera consultée sur le commit publié et rapportée dans la PR sans être présumée réussie ici.

Empreintes SHA-256 des documents métier contrôlés :

```text
999c69662b5ca99f1005c4b944d70b5ad729a27b41121b0004c93cb7d8d550ee  documentation/advertising/README.md
b3fbfae7e8ecf0c62ba0f3a8ae6b9f8e0c020449eb63613904b403cda36ba6ed  documentation/advertising/advertising-options.md
```

Le rapport est complété après ces exécutions, puis les liens et espaces du delta final sont recontrôlés avant publication. L'identité du contenu publié sera vérifiée contre les fichiers locaux ; aucun historique local de préparation n'est poussé.

## Revue documentaire ciblée

- Mandat M0-TEAM-11, plan, modèle, vision, catalogue et parcours lus au commit d'entrée.
- FEAT-030 conservé en Phase 3 proposée ; ambiguïté « MVP Ads » des brouillons précédents explicitée.
- Options, 15 critères, hypothèses de coût/revenu et 8 transmissions ciblées rédigés.
- INT-1101–INT-1108 et RISK-1101–RISK-1105 sont des IDs proposés : unicité à recontrôler par HQ/17 à l'intégration avec les contributions concurrentes.
- Aucune conformité juridique, revue indépendante, performance runtime ou recette financière réelle attestée par ce rapport.

## Publication et retour arrière

Branche de contribution ciblant `documentation/m0-team-coordination` pour isoler le delta par rapport à PR #2. Revue avant fusion selon CONTRIBUTING. Après fusion de #2, vérifier la base et le diff avant de recibler la PR si nécessaire. Retour arrière documentaire : revert du commit de contribution après examen des références ultérieures ; aucune migration runtime.
