# Correctif ciblé des contrôles de fondation

Date : 29 septembre 2026. Proposé par HQ pour revue 20/14/18/21. Référence : [revue #19](https://github.com/yyogas/social-network/pull/19), findings FIND-21-01 à 05. Périmètre : CI et validateur du dépôt, aucune fonctionnalité applicative.

## Complément du 29 septembre — consolidation sur la PR existante

Après la revue [#26](https://github.com/yyogas/social-network/pull/26), le porteur a demandé de poursuivre la consolidation sans multiplier les branches. Le complément est proposé dans **#25**, sur la base vérifiée `786da003111f5ac985b521a4c872c7c3251dc00b`. Le texte ci-dessous conserve la preuve historique de la première version.

- FIND-21-01/03 : corrections vérifiées par la revue indépendante #26 sur cette base ; scripts whitespace et preuve historique inchangés dans ce complément.
- FIND-21-04 : rejet explicite des liens symboliques dans chaque composant du chemin avant `resolve()`, y compris les alias de répertoire, les chemins avec `..` et les caractères encodés dans l'URL. Les chemins de fichiers suivis conservent leur identité lexicale. Le contrôle de confinement dans le dépôt reste actif ; les liens relatifs ordinaires et répertoires avec contenu suivi restent acceptés.
- Auteur de ce complément : équipe 21, sur instruction du porteur. Cette équipe devient donc auteur du delta : **ses tests ne constituent pas une revue indépendante de sa propre correction**. Relecture ciblée par 20/18 attendue avant clôture complète du constat. FIND-21-02 reste à arbitrer par HQ/14/20 ; FIND-21-05 reste séparé.

Validation locale effectuée dans un export isolé : 35/35 hashes Git blob comparés à l'arbre GitHub de la base, Linux x86_64, Python 3.12.14, Git 2.51.1. Aucun commit racine local n'est présenté comme un commit distant.

| Vérification | Résultat réellement observé |
| --- | --- |
| Quatre nouvelles méthodes de test ajoutées, avant modification du validateur | 24 tests exécutés, 6 échecs d'assertion dans 3 méthodes, dont 4 sous-cas d'alias de répertoire ; défaut reproduit |
| Même suite après correction | 24 tests PASS, dont la non-régression du merge synthétique et les cas PR/push |
| Alias fichier vers cible suivie, puis suppression de l'alias | Refus avec alias ; lien cassé après suppression |
| Alias répertoire direct, descendant, composant avant `..`, nom encodé | Refus dans les 4 sous-cas |
| Fichier déclaré suivi traversant un répertoire symbolique | Refus |
| Liens ordinaires `./`, `../`, répertoire suivi et racine | Acceptés |
| `python3 scripts/repository/validate_repository.py` | PASS, 35 fichiers |
| `git diff --check` | PASS sur le delta local |

Le SHA publié et la CI de ce complément sont consignés dans le corps de #25 après publication et consultation des logs. Les commandes de suite sont celles de la section historique ci-dessous. Aucun test applicatif, fusion, changement de protection ou suppression de branche effectué.

Demande **À TRANSMETTRE** à 20/18 : relire uniquement le delta alias et ses quatre nouvelles méthodes de test. Demande **À TRANSMETTRE** à HQ/14/20 : enregistrer le choix de protection et les reviewers avant intégration. Le présent complément ne désigne aucun reviewer humain à leur place.

## Changements et statut

- FIND-21-01 : correction proposée. La CI appelle un script Python sur le delta explicite PR/push ; checkout avec `fetch-depth: 0`. SHA validés avant appel Git, sans interpolation shell de métadonnées de PR. Référence absente ou événement inattendu : échec, aucun vert par omission.
- FIND-21-03 : rapport historique corrigé avec head, merge synthétique, run/job et limites. Le futur commit publiant cette correction n'est pas présenté comme couvert par l'ancien run.
- FIND-21-04 : correction proposée. Un lien vers fichier non suivi est refusé ; un lien vers répertoire exige un descendant suivi.
- FIND-21-02 : OUVERT. Aucun réglage de permissions, protection, abonnement ou visibilité modifié. La revue indépendante avant fusion reste requise selon les règles du projet ; les reviewers et le mécanisme de protection sont à formaliser.
- FIND-21-05 : OUVERT. Le SHA checkout existant est conservé. Son avertissement de runtime reste un suivi séparé à examiner par 14/20 ; pas de vulnérabilité déduite de cet avertissement.

## Reproduction et vérifications

Environnement : Linux, Python 3.12.14, dépôts Git éphémères à données synthétiques. Commande :

```sh
python3 -m unittest discover -s tests/repository -p 'test_*.py' -v
python3 scripts/repository/validate_repository.py
git diff --cached --check
```

20 tests exécutés avec succès localement : les 10 cas existants, 2 cas liens suivis et 8 cas de contrôle du delta Git. Les suites utilisent les vrais exécutables Git/Python ; aucun résultat simulé n'est présenté comme une exécution CI.

La non-régression `test_dirty_pr_on_synthetic_merge_fails_when_old_check_passes` crée une branche avec espace final puis un merge synthétique. Elle confirme l'ancien retour 0 et le nouveau retour 2. Autres cas : PR propre ; changement fautif de base exclu du delta PR ; faute dans un premier commit de push malgré dernier commit propre ; push propre ; création de branche ; objet manquant ; SHA invalide et événement non pris en charge.

Le contrôle vise le delta net de la PR ou du push, pas les commits intermédiaires dont un défaut serait déjà corrigé dans le résultat final. Les règles d'espacement sont fixées explicitement. L'historique complet augmente le volume de checkout ; acceptable pour la fondation, à mesurer si le dépôt grandit. Pour un before de push devenu introuvable, le contrôle échoue plutôt que de réduire silencieusement sa portée.

La CI distante et le commit effectivement contrôlé sont référencés dans le corps de PR après exécution. Les tests applicatifs, permissions runtime, installation et charge ne sont pas exécutés.

## Branches et intégration

Inventaire initial de cette intervention : 25 branches dont main, 24 PR ouvertes. #1 cible main ; #2 cible #1 ; #3–24 ciblent la branche de #2. La revue #19 bloque l'intégration de cette pile tant que la correction du contrôle et le traitement de la gouvernance ne sont pas examinés.

Le présent correctif cible la branche de #1 sur sa base exacte. Les branches spécialisées sont conservées ; aucune suppression, aucun force-push et aucune fusion effectués. Après revue favorable du correctif, traitement de FIND-21-02 et intégration autorisée dans #1 : revérifier #1, puis #2 sur la nouvelle base, puis retargeter progressivement les contributions documentaires revues. Revoir les conflits README/plan/stratégie sans écraser les autres propositions.

## Handoff ciblé

20/14 : vérifier le choix des bornes Git, l'historique récupéré et les cas push. 18 : vérifier la reproduction réelle et les cas propres/fautifs. 21 : examiner seulement ce delta contre FIND-21-01/03/04 ; le statut « corrigé proposé » ne clôt pas la revue. 17 : conserver les observations historiques et liens du rapport. Ces demandes sont préparées, pas réputées envoyées aux discussions.

## Compte rendu

1. Décisions : correctif technique limité aux contrôles existants ; gouvernance inchangée.
2. Livrables : workflow, script de delta, tests, validateur et documentation de preuve ; PR distincte.
3. Tests : 20 tests locaux réussis ; commandes ci-dessus ; CI distante consignée après exécution.
4. Questions : avis 21, protection/reviewers, maintenance checkout.
5. Dépendances : 20/14/18/21 et base de #1 ; aucune modification des branches d'équipes.
6. Risques : coût checkout complet, refs indisponibles provoquant échec explicite ; contrôle documentaire ne valide pas le produit.
7. Suite : revue ciblée, statut des findings à mettre à jour par propriétaire sur preuve, puis intégration de la pile dans l'ordre ; rollback par revert ciblé du correctif après revue.
