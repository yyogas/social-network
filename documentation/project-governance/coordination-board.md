# Pilotage des 21 équipes — Fondation / M0

Date : 29 septembre 2026. Responsable : 00 MASTER. Instruction source : « fait travailler toute les discussions, et bien construire la documentation, les grandes lignes, les fonctionnalités ».

## Ce qui est autorisé

Chaque équipe prépare maintenant sa contribution documentaire dans son domaine. Le HQ fournit une première proposition de vision, de catalogue et de parcours pour rendre les analyses concrètes. Ce travail préparatoire n'est ni une validation spécialisée ni une autorisation d'implémenter une architecture, un traitement de données ou une fonctionnalité non approuvés.

[Mandats individuels](../teams/work-orders.md) · [Plan documentaire](../documentation-plan.md) · [Modèle de livrable](../teams/deliverable-template.md) · [Catalogue](../product/feature-catalog.md) · [Roadmap](global-roadmap.md).

## Tableau de réception

Les mandats ci-dessous sont PRÉPARÉS / À TRANSMETTRE. Le présent tableau ne prouve pas leur réception par les autres discussions. Les éventuels travaux existants doivent être fournis avec référence, sans recommencer ce qui est déjà exploitable. Une équipe peut répondre par un delta ciblé à son document existant.

| Mandat | Équipe | Livrable spécialisé | Transmission | Réponse |
| --- | --- | --- | --- | --- |
| M0-TEAM-01 | 01 — Produit | Voir mandat 01 | À TRANSMETTRE | NON REÇU |
| M0-TEAM-02 | 02 — Design | Voir mandat 02 | À TRANSMETTRE | NON REÇU |
| M0-TEAM-03 | 03 — Architecture | Voir mandat 03 | À TRANSMETTRE | NON REÇU |
| M0-TEAM-04 | 04 — Backend / API | Voir mandat 04 | À TRANSMETTRE | NON REÇU |
| M0-TEAM-05 | 05 — Web | Voir mandat 05 | À TRANSMETTRE | NON REÇU |
| M0-TEAM-06 | 06 — Mobile | Voir mandat 06 | À TRANSMETTRE | NON REÇU |
| M0-TEAM-07 | 07 — IA / Recommandation | Voir mandat 07 | À TRANSMETTRE | NON REÇU |
| M0-TEAM-08 | 08 — Médias | Voir mandat 08 | À TRANSMETTRE | NON REÇU |
| M0-TEAM-09 | 09 — Trust & Safety | Voir mandat 09 | À TRANSMETTRE | NON REÇU |
| M0-TEAM-10 | 10 — Admin / Support | Voir mandat 10 | À TRANSMETTRE | NON REÇU |
| M0-TEAM-11 | 11 — Publicité | Voir mandat 11 | À TRANSMETTRE | NON REÇU |
| M0-TEAM-12 | 12 — Créateurs | Voir mandat 12 | À TRANSMETTRE | NON REÇU |
| M0-TEAM-13 | 13 — Data | Voir mandat 13 | À TRANSMETTRE | NON REÇU |
| M0-TEAM-14 | 14 — DevOps / Sécurité | Voir mandat 14 | À TRANSMETTRE | NON REÇU |
| M0-TEAM-15 | 15 — Privacy / Juridique | Voir mandat 15 | À TRANSMETTRE | NON REÇU |
| M0-TEAM-16 | 16 — International | Voir mandat 16 | À TRANSMETTRE | NON REÇU |
| M0-TEAM-17 | 17 — Documentation | Voir mandat 17 | À TRANSMETTRE | NON REÇU |
| M0-TEAM-18 | 18 — QA | Voir mandat 18 | À TRANSMETTRE | NON REÇU |
| M0-TEAM-19 | 19 — Growth | Voir mandat 19 | À TRANSMETTRE | NON REÇU |
| M0-TEAM-20 | 20 — Code Source | Voir mandat 20 | À TRANSMETTRE | NON REÇU |
| M0-TEAM-21 | 21 — Intégration / Revue | Voir mandat 21 | À TRANSMETTRE | NON REÇU |

## Convergence sans attente circulaire

1. Tous démarrent par un inventaire des besoins, contraintes, preuves existantes et inconnues dans leur domaine. Les dépendances absentes deviennent des hypothèses explicites, sans bloquer l'ensemble du document.
2. Produit, Safety, Privacy, International et Growth préparent le cadre du pilote. Design et les équipes techniques travaillent sur les parcours candidats en signalant les variantes affectées par les questions ouvertes.
3. Architecture organise une proposition de contrats avec Backend, Web, Mobile, Médias, Admin, Data et DevOps. Ces équipes exposent les désaccords ; aucune n'impose seule ses interfaces.
4. Documentation vérifie la couverture et les liens ; QA rend les critères testables ; Code Source prépare la réalisation ; Intégration relève les conflits et les pièces manquantes.
5. MASTER arbitre chaque question sur un dossier suffisant. Une dépendance future non pertinente ne bloque pas un lot autonome. Les dépendances critiques de sécurité, droits ou données doivent être résolues avant l'implémentation concernée.

## Arbitrages ouverts

| ID de suivi | Question | Porteurs des options | Preuve attendue avant décision |
| --- | --- | --- | --- |
| OPEN-001 | Public et pays effectivement ouverts au pilote | 01, 15, 16, 19 | Besoins, contraintes, support et capacité de modération par marché |
| OPEN-002 | Web, mobile natif ou séquence combinée | 01, 02, 05, 06, 03 | Parcours, accès au public, coûts et charge de maintenance |
| OPEN-003 | Communautés dès le MVP ou après | 01, 09, 10, 19 | Valeur différenciante, permissions et charge de modération |
| OPEN-004 | Langues, écritures et politique d'âge du pilote | 15, 16, 09, 02 | Analyse spécialisée, support réel et états UX nécessaires |
| OPEN-005 | Stack, frontières, données et contrats | 03, 04, 14, 20 | Comparaison motivée et avis des consommateurs |
| OPEN-006 | Budget disponible et mode de financement du pilote | 00, 11, 12, 14, 19 | Hypothèses de dépenses et revenus, sans budget réputé accepté |
| OPEN-007 | Visibilité des contenus, droits d'accès et cycle de suppression | 01, 04, 09, 14, 15 | Matrice de permissions et cycle de données cohérents |
| OPEN-008 | Responsable humain et comptes GitHub des reviewers | 00, 20, 21 | Identités confirmées, accès et règle de revue applicable |

Ces IDs suivent les questions ; ils ne remplacent pas les décisions DEC ou ADR. DEC-0001 et DEC-0002 restent réservées au public pilote et au contrat MVP après examen.

## Dépendances et risques

- Produit ↔ Safety / Privacy : visibilité, blocage, suspension, suppression et recours doivent former un parcours cohérent.
- Backend ↔ interfaces ↔ médias : mêmes états, erreurs, permissions et règles de reprise.
- Ads / Créateurs ↔ Privacy / Data : documenter les besoins futurs et les restrictions avant toute collecte ou monétisation.
- International ↔ Design / Safety / Support : traduire l'interface ne suffit pas à rendre un marché opérationnel.
- QA ↔ tous les propriétaires : chaque exigence critique doit avoir un critère et une méthode de preuve.

RISK-0001 à RISK-0004 restent actifs dans le [registre](decision-register.md). Risques additionnels de coordination : fausse attribution d'une validation, duplication des spécifications, contrats divergents et documentation volumineuse non exploitable. Mesures : un propriétaire canonique, un statut par document, revue ciblée des deltas et références de commit.

## Traitement des retours

Pour chaque réponse : consigner équipe, mandat, date, chemin, branche/PR/commit, exigences affectées, questions et preuves. Marquer REÇU seulement après lecture du livrable ; EN REVUE pendant examen ; APPROUVÉ seulement avec autorité et périmètre explicites. Une PR fusionnée peut contenir des propositions : la fusion n'approuve pas automatiquement leur contenu produit.

En cas de conflit : conserver les deux positions avec leurs références, nommer les propriétaires, ouvrir une question HQ et suspendre uniquement le changement dépendant. Ne pas renommer silencieusement une exigence ou supprimer la position d'une autre équipe.

## Prochaines actions

Transmettre le [message commun](../teams/kickoff-message.md) à chaque discussion 01–21, recevoir les premiers livrables, puis consolider les décisions pilote et MVP. Aucune date de livraison d'équipe n'est promise sans capacité confirmée. La préparation locale par des agents assistants ne constitue pas une réponse des discussions spécialisées.
