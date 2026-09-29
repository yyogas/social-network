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

## Delta ciblé L1 v0.2 — 30 septembre 2026

**Portée :** réponse 04 dans le [document Backend](../backend/api-contract-candidates.md), GAP-L1-01 à 04 uniquement, et présent rapport. Mandat HQ `206b1804df5cb602140729613fa85080fea32c7c` ; base PR #27 actualisée `85319286222559c22f943f4c94838840c23dae97`. La lecture de contenu est limitée au mandat, candidat L1 et contrats directs ; copie mécanique des 86 fichiers pour exécuter les contrôles existants, sans réaudit du corpus. Aucun script, test, workflow ou fichier d'un autre propriétaire modifié.

Instantané local d'entrée distinct de l'historique distant : son arbre `39bbac81875877aa51bd36f2ba4d7411835802b4` est identique à l'arbre GitHub de la référence. Le SHA publié et la CI de ce delta sont consignés dans sa PR ; aucun succès de #27 n'est réutilisé comme preuve du nouveau delta.

Environnement local : Linux, Python 3.12.14. Commandes exécutées :

```sh
python3 scripts/repository/validate_repository.py
python3 -m unittest discover -s tests/repository -p 'test_*.py' -v
git diff --check
git diff --cached --check
```

Résultats : **86 fichiers PASS ; 24 tests du validateur/contrôle whitespace PASS ; espaces PASS**. Ces tests vérifient l'outillage du dépôt, pas les sessions de l'application.

Contrôle ponctuel Python : quatre sections GAP propriétaires présentes ; onze critères locaux L1-BE ; 48 lignes historiques du catalogue préservées ; références TEST-18xx/14xx/WEB explicites du delta résolues dans les trois sources QA/Sécurité/Web ; les deux fixtures JSON d'identité sont syntaxiquement valides. Recherche Git dans la base : API-BE-049 absent, donc identifiant proposé sans collision observée dans cette référence ; nouvelles contributions simultanées à vérifier lors de l'intégration.

**Échec de contrôle puis correction :** la première assertion comptait les mentions API des nouveaux tableaux comme de nouvelles définitions du catalogue historique. Elle a échoué ; le contrôle a été borné à la portion antérieure au titre « Delta propriétaire L1 », puis réussi. Aucune réussite applicative déduite de cette correction du contrôle textuel.

Relecture locale : distinction clé K/preuve/contexte ; preuve expirée versus reçu historique ; mutation en cours et réponse perdue ; extension logout et changement de génération ; identité compte/profil séparée ; absence de Set-Cookie de suppression tardive ; issue de reconnexion si un ancien cookie invalide écrase B ; récupération contre login ancien ; données et paramètres proposés/ouverts. Cette relecture du producteur ne vaut pas revue indépendante de 21 ni avis 05/14/15/18.

Aucun test applicatif, API, navigateur réel, CSRF, anti-énumération mesurée, cryptographie, concurrence DB, restauration, charge ou migration exécuté. Les scénarios S03a–h/S04a–h et L1-BE-01…11 sont PLANNED ; leurs preuves runtime restent manquantes. Les contrôles documentaires ne ferment aucun GAP. Avis ciblés préparés, À TRANSMETTRE / NON REÇUS. **L1 BLOQUÉ POUR CODE**, aucune fusion.
