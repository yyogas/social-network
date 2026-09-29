# Validation de la campagne documentaire M0

Date : 29 septembre 2026. Portée : documents préparés au HQ pour les 21 discussions. Environnement local : Linux, Python 3.12.14. Base distante : `8590a095d76965880e94614328a8eafbe09b93cb`, PR nº 1. La nouvelle PR cible sa branche de travail afin de séparer les changements ; elle dépend de sa revue et de sa fusion ultérieure. Les SHA publiés et résultats de CI sont attachés à la nouvelle PR.

## Vérifications reproductibles

```sh
python3 scripts/repository/validate_repository.py
python3 -m unittest discover -s tests/repository -p 'test_*.py' -v
git diff --cached --check
```

Exécution locale effectuée : PASS sur 42 fichiers suivis ; 10 tests du validateur réussis ; contrôle des espaces réussi. Le contrôle ciblé des identifiants a confirmé 21 mandats et lignes de réception, 34 fonctionnalités uniques, 7 parcours, 31 critères PLANNED uniques et aucune référence fonctionnelle orpheline dans ces parcours.

Ces commandes vérifient les documents suivis et le validateur existant. Le résultat exécuté pour ce lot est consigné dans le corps de PR avec le commit distant ; ne pas assimiler ces contrôles à des tests du réseau social.

## Revue documentaire ciblée

La revue du plan, des mandats, du catalogue et de la roadmap a relevé une divergence de phase sur les notifications et les médias. La roadmap a été alignée sur le catalogue avant publication. Le tableau de réception est la référence unique des états de transmission ; les mandats contiennent les instructions et un index statique.

Contrôles de contenu à la préparation : unicité et présence des 21 mandats, correspondance du tableau de réception, unicité des IDs fonctionnels et des critères de parcours, absence de références fonctionnelles orphelines dans les parcours. Résultats réellement exécutés dans la PR. Ces vérifications sont une revue de cohérence HQ, pas les avis attendus des discussions spécialisées.

## Limites

- Le contrôle de liens couvre les chemins locaux inline, pas les ancres ou l'accès aux liens externes.
- Aucun test applicatif, sécurité du produit, installation applicative, performance ni restauration n'est exécuté pour cette rédaction.
- Les exemples d'acceptation sont PLANNED ; aucune fonctionnalité n'est déclarée réalisée.
- Aucun mandat n'est déclaré transmis ou reçu sur la seule base de sa présence dans GitHub.
- Les cibles documentaires futures des mandats sont écrites en code pour les distinguer des liens vers des livrables présents.
- La revue des PR avant fusion et les décisions produit/techniques restent requises ; une CI verte ne les remplace pas.
