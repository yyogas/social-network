# Hébergement — trois scénarios de préparation

**Date du chiffrage : 29 septembre 2026. Statut : PROPOSÉ, capacités NON BENCHMARKÉES.** Propriétaires : 14 DevOps, 03 Architecture, 08 Media, 13 Data ; arbitrage budget et fournisseur par MASTER. Aucun service n'est commandé et aucune configuration n'est un minimum garanti du produit.

## Hypothèses et limites

Application sociale texte/images, fil chronologique, backend et PostgreSQL. Les jeux de charge ci-dessous sont des objectifs de benchmark, pas le nombre d'utilisateurs garanti par une machine. Un compte inscrit ne correspond pas à une connexion simultanée. Mix de référence à tester : 90 % lectures / 10 % écritures, utilisateurs authentifiés, droits contrôlés, pagination et jeux de données croissants. Les requêtes média ne passent pas toutes par l'application.

| Dimension proposée | Minimum : pilote | Intermédiaire : croissance | Premium : charge / disponibilité |
| --- | --- | --- | --- |
| Population de test | 1 000 comptes, 100 actifs/jour | 10 000 comptes, 2 000 actifs/jour | 100 000 comptes, 20 000 actifs/jour |
| Pointe à tester | 20 sessions actives, 10 req/s API | 200 sessions, 100 req/s | 2 000 sessions, 1 000 req/s |
| Ressources applicatives | 1 × 4 vCPU partagés / 8 Go | 2 × 4 vCPU partagés / 8 Go | 3 × 4 vCPU dédiés / 16 Go |
| PostgreSQL | Sur le même hôte ; budget DB initial 20 Go | 1 × 4 vCPU dédiés / 16 Go ; budget DB 80 Go | 2 × 8 vCPU dédiés / 32 Go ; budget DB 120 Go par copie |
| Disques de calcul de référence | 160 Go sur l'hôte unique | 160 Go par hôte app et DB, 80 Go worker | 160 Go par hôte app, 240 Go par DB, 160 Go par worker |
| Workers / cache | Dans l'hôte pilote, sous limites | 1 × 2 vCPU / 4 Go ; cache si validé | 2 × 4 vCPU / 8 Go ; redondance à concevoir |
| Médias stockés en moyenne | 100 Go | 1 000 Go | 10 000 Go |
| Trafic sortant mensuel estimé | API 50 Go ; images 0,2 To | API 0,5 To ; images 2 To | API 5 To ; images 20 To |
| Sauvegardes | Quotidiennes hors hôte, rétention proposée 7 jours | Base + journaux de transactions, rétention proposée 14 jours | Base + journaux, copie indépendante, rétention proposée 30 jours |
| Cibles de reprise à valider | RPO 24 h / RTO 8 h | RPO 1 h / RTO 4 h | RPO 15 min / RTO 1 h |
| Supervision | Uptime externe, erreurs, ressources, disque, backup | Latences, DB, jobs et alertes de saturation | Traces échantillonnées, SLO, exercices de panne et astreinte |
| Limites | Hôte unique ; une panne arrête le pilote | DB unique ; deux apps ne suffisent pas à assurer la haute disponibilité | Répartition des domaines de panne, quorum et failover à valider ; pas de SLA promis |

Premium requiert une revue spécifique de la réplication PostgreSQL, du point d'entrée réseau, des jobs et du cache. Deux bases sans quorum/fencing maîtrisé peuvent créer une perte de données ou un split-brain. Le budget ci-dessous ne certifie pas une topologie multi-zone ni un service managé. Les rétentions et RPO/RTO sont des propositions à ratifier avec Privacy et Produit.

## Références publiques de prix

Repères Hetzner Allemagne/Finlande, prix mensuels en euros hors TVA et IPv4, consultés le 29 septembre 2026 : CPX22 19,49 €, CPX32 35,49 €, CCX23 85,99 €, CCX33 138,49 €. Source : [ajustement officiel du 15 juin 2026](https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/).

Caractéristiques de référence : [CPX22 : 2 vCPU / 4 Go / 80 Go ; CPX32 : 4 / 8 / 160](https://www.hetzner.com/cloud/regular-performance/) ; [CCX23 : 4 / 16 / 160 ; CCX33 : 8 / 32 / 240, CPU dédiés](https://www.hetzner.com/cloud/general-purpose/). Les pages consultées affichent des mentions d'indisponibilité : vérifier stock, région et devis avant toute décision. Ce sont des repères de calcul, pas une recommandation d'achat immédiat.

Repère Cloudflare R2 Standard : 0,015 USD/Go-mois, 4,50 USD/million d'opérations A, 0,36 USD/million B ; sortie directe R2 sans frais de transfert. Source : [tarification officielle R2](https://developers.cloudflare.com/r2/pricing/), consultée le 29 septembre 2026. Les calculs ci-dessous ignorent volontairement le quota gratuit et les arrondis restent visibles à la facture. Les frais de transformation, Workers, autres services CDN et services vidéo ne sont pas inclus dans le stockage R2.

## Modèle budgétaire mensuel reproductible

| Poste | Pilote | Intermédiaire | Premium |
| --- | --- | --- | --- |
| Calcul / DB / workers | 1 × 35,49 = **35,49 €** | 2 × 35,49 + 85,99 + 19,49 = **176,46 €** | 3 × 85,99 + 2 × 138,49 + 2 × 35,49 = **605,93 €** |
| Provision sauvegardes | 10–25 € | 25–75 € | 100–300 € |
| Provision monitoring | 0–20 € | 15–50 € | 75–200 € |
| Provision réseau, IPv4, point d'entrée, email et marge | 20–55 € | 60–175 € | 225–700 € |
| **Enveloppe EUR hors médias** | **65,49–135,49 €** | **276,46–476,46 €** | **1 005,93–1 805,93 €** |
| Médias R2 : stockage + A + B | 100 Go + 1 M A + 10 M B | 1 000 Go + 5 M A + 100 M B | 10 000 Go + 20 M A + 1 000 M B |
| **Enveloppe USD médias** | 1,50 + 4,50 + 3,60 = **9,60 USD** | 15 + 22,50 + 36 = **73,50 USD** | 150 + 90 + 360 = **600 USD** |

Les provisions sont des hypothèses budgétaires internes, pas des devis fournisseurs. Elles doivent couvrir aussi les lectures/écritures des sauvegardes et les frais inter-régions éventuels. Elles seront remplacées par des devis et consommations mesurées. Les ressources de staging, le CI payant, l'astreinte, le support humain, la modération, l'IA, les taxes, le change EUR/USD et un éventuel onboarding prestataire restent à budgéter séparément. Aucun total artificiel mélangeant EUR et USD n'est fourni.

## Vidéo et médias : budget séparé

La vidéo n'est pas validée dans le MVP. La projection est : stockage des originaux + renditions + miniatures + transcriptions ; CPU/GPU ou minutes de transcodage ; requêtes de lecture ; diffusion ; modération ; sauvegardes. Exemple de volume, sans estimation de coût validée : 10 000 heures regardées à 2 Mbit/s produisent environ 9 To de trafic decimal (`heures × 3 600 × débit / 8`). Ajouter renditions, trafic d'upload et taux de cache. Un prix de stockage ne finance pas à lui seul une plateforme vidéo. L'équipe 08 doit produire les profils de codec, les tests et le coût par minute avant adoption.

## Critères d'évolution proposés

Établir d'abord les objectifs produit de latence et de disponibilité. Déclencher une revue si, pendant une charge représentative, CPU > 70 % pendant 15 minutes, mémoire disponible < 20 %, disque > 70 %, p95 dépasse l'objectif, jobs en retard ou connexions DB saturées. Ces seuils sont des alarmes initiales à ajuster aux mesures, pas des capacités garanties. Déplacer les médias hors des disques applicatifs ; étudier requêtes lentes, index et contention avant d'ajouter des serveurs. Vérifier toute évolution par charge et restauration : benchmark → coût mesuré → décision d'architecture → déploiement.
