# Gouvernance des contributions

## Autorité

MASTER tient le registre des décisions transversales, de la roadmap, des risques et des dépendances. Les équipes spécialisées possèdent leurs analyses, contrats et livrables dans leur domaine. Les changements majeurs d'architecture globale, stack, modèle économique, sécurité, données personnelles, permissions ou roadmap sont proposés à MASTER avec les avis des propriétaires concernés.

Une discussion n'écrit pas automatiquement dans une autre. Un `HANDOFF` est **À TRANSMETTRE**, puis **ENVOYÉ**, puis **REÇU** seulement si chaque étape a réellement eu lieu.

## Statuts

- **CONFIRMÉ** : preuve ou instruction explicite reçue.
- **PROPOSÉ** : option documentée en attente de décision.
- **À VÉRIFIER** : information plausible sans preuve suffisante.
- **NON REÇU** : livrable ou réponse absent du dossier MASTER.
- **APPROUVÉ** : décision enregistrée avec date et autorité.

## Changement

1. L'équipe propriétaire rédige le problème, les options et impacts.
2. Les équipes touchées commentent leurs dépendances et risques.
3. MASTER arbitre ou présente les options au porteur du projet.
4. La décision, ses références et son statut sont enregistrés dans `documentation/decisions/` et le registre HQ.
5. Les équipes touchées reçoivent un `SYNC PACKET` ciblé.
6. Documentation, code et tests sont mis en cohérence avant de marquer le travail terminé.

Les décisions sont identifiées `DEC-XXXX`, les décisions d'architecture `ADR-XXXX`, les demandes inter-équipes `INT-XXXX`, les risques `RISK-XXXX`. Les anciens `DIR-001` à `DIR-008` sont préservés dans le registre historique.

## Fin de travail important

Chaque propriétaire rend : 1. décisions prises ; 2. livrables produits ; 3. questions ouvertes ; 4. dépendances ; 5. risques ; 6. prochaines étapes ; 7. informations à transmettre au HQ. Une fonctionnalité n'est déclarée terminée qu'après les revues et preuves adaptées à son risque.

## Exigences de qualité — DIR-010

Les décisions et livrables indispensables sont enregistrés dans GitHub. Chaque changement passe par une branche et une PR avec revue avant fusion. Les preuves de validation associent commandes, environnement, SHA et résultat consultable. Le format courant de fin d'étape est : 1. décisions prises et à valider ; 2. livrables et références GitHub ; 3. tests exécutés et résultats ; 4. questions ouvertes ; 5. dépendances ; 6. risques et limites ; 7. prochaines étapes et informations HQ.
