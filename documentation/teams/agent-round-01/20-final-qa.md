# Sous-agent 20 — contrôle final des revendications et preuves

**Revue indépendante, 30 septembre 2026. Verdict : favorable à la publication documentaire du contenu relu.** Les réserves de cohérence identifiées sont corrigées dans la copie intégrée ; aucun blocage rédactionnel résiduel n’est relevé dans le périmètre contrôlé. Ce verdict n’adopte aucun contrat, ne ferme aucun constat propriétaire et n’autorise ni code ni pilote.

Périmètre : contributions 01–19, comparaison avec leurs copies intégrées dans `documentation/teams/agent-round-01`, manifeste README, fiche `quality/agent-round-01-validation.md`, ajouts à l’index, au statut projet, au tableau de coordination et au registre DIR-013. Ce contrôle constitue la vingtième contribution. Aucun test, appel applicatif ou changement distant exécuté par cette revue.

## Corrections vérifiées

**F/T et QA-A.** La première version de l’avis 05 proposait une levée trop large et donnait 204 après continuation F. Les avis 01/10/17/18 relevaient une précondition manquante : si cette continuation avance T, le logout préparé à l’ancienne version rencontre le 409 de C5. La copie Backend confirme la tension entre C3 et C5. La version intégrée de 05 maintient désormais QA-A/L1-BE-07 partiellement ouvert ; 07-b est conditionnel à une précondition terminale ratifiée. Sans exception définie, T obsolète produit 409 sans mutation. Le reçu B ne résout pas la première révocation et la commande ne se recible pas vers B. Le manifeste reprend correctement cette réserve. Q distingue la déconnexion de l’incarnation D ; la correction du contrat propriétaire reste proposée.

**A et reprise ordinaire.** Les avis 02/06 privilégient A après perte de vue, tandis que 03/07/12 visent une continuité vérifiée au reload ordinaire. Le manifeste conserve ce désaccord. L’avis 06 corrigé soumet A à HQ et précise qu’aucune politique n’est modifiée par cette PR. Différer le reçu B ne décide pas du sort de la continuité. Reprise, maintien du verrou après sortie incertaine et portée du dernier login restent des arbitrages distincts. Aucune exclusivité entre racines indépendantes n’est acquise ; l’ancienne paire cohérente demeure le contre-exemple explicite.

**Droits et responsabilité.** L’avis 08 corrigé exige preuve du sujet et autorisation propre avant suivi privé ou téléchargement, revérifiées au téléchargement ; recovery ne change aucune restriction. Les avis 08/09 ne créent ni canal actif ni destinataire humain. P15-L1-05/08 et QA-E restent ouverts. Les matrices, durées et parcours demeurent des propositions.

## Autorité, sources et preuves

Le manifeste distingue correctement **vingt missions nouvelles** et **vingt-et-une discussions spécialisées**. Les numéros de sous-agents ne désignent pas les équipes homonymes. DIR-013 organise la coordination ; il ne transforme pas ces contributions en avis signés des propriétaires historiques. Aucune écriture dans d’autres conversations ni poursuite permanente après la session n’est déclarée. Les anciennes transmissions non établies restent identifiées comme telles.

Les références structurantes sont séparées : HQ `4d3cd079e92217936af3292429a38f91f7b576ff`, Backend v0.3 `0a7fcd54b996cc292bfe98c61a835613837def32`, Architecture `a7901fc87e79975d8963e909a89fc8150410e40a`. Le manifeste rattache les copies temporaires aux chemins canoniques et les renvois `outputs/…` aux annexes. Il précise que les avis propriétaires historiques portent sur Backend v0.2 ; leur autorité n’est pas transférée à v0.3. La présente revue contrôle cette traçabilité interne, sans refaire les lectures GitHub du HQ.

Les **24 tests documentaires existants** rapportés par 11 restent sa vérification locale. La fiche de validation distingue cette preuve, la CI Backend au SHA examiné et les contrôles finaux du nouveau paquet encore prévus. Aucun résultat futur n’est anticipé. L’application est absente ; sécurité applicative, concurrence, restauration, purge, accessibilité et charge restent PLANNED/BLOCKED. **L1 demeure BLOQUÉ POUR CODE.** Les contrôles de publication du HQ pourront être consignés après copie de ce verdict final, sans modifier sa portée documentaire.
