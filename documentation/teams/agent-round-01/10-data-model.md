# Agent 10 — Modèle de données et atomicité : avis sous-agent

**La cohérence est formulable, mais la continuation F/T empêche encore un oracle unique.** Cet avis documentaire ne représente ni la discussion 03 ni la discussion 04 et n’adopte aucun mécanisme. Sources : Backend #28, SHA `0a7fcd54b996cc292bfe98c61a835613837def32`, convergence C1–C7 ; Architecture #33, SHA `a7901fc87e79975d8963e909a89fc8150410e40a`, §§3–6/8–9 ; `documentation/architecture/architecture-proposal.md` ; avis locaux 01, 02, 05 et 06. Aucun code, test runtime ou changement distant.

## Entités et invariants minimaux

Les symboles décrivent des responsabilités logiques ; ils n’imposent ni table, service, DDL ni framework.

| Élément | Invariant à conserver |
| --- | --- |
| Compte / E | E appartient au compte. Le reset avance E ; sessions, challenges et vérifications antérieurs ne retrouvent aucun droit par rejeu. |
| R / T | R borne une lignée connue ; T ordonne ses transitions. T ne devient pas un identifiant immuable d’opération. |
| F / session | F garde une identité stable à travers ses continuations ; une famille indépendante F2 reste distincte, même sous le même compte ou R. |
| I / W | I lie admission, opération, R/T et preuve attendue ; W atteste la liaison de vue. Aucun identifiant seul n’autorise le privé. |
| K / résultat | L’unicité porte sur scope, opération et K. Empreinte versionnée et résultat minimal durable empêchent une nouvelle exécution ; K n’est ni I ni un credential. |
| D / scope | D délimite les admissions encore acceptables après perte/restauration. Son retrait doit rendre les anciennes capacités inutilisables. |

Le reçu optionnel B est une lecture autorisée d’un résultat immuable. Il ne conserve pas les droits sociaux et ne bloque pas l’avancement de T. Audit et outbox ont des finalités distinctes du registre K ; leur présence ne remplace pas l’autorité d’admission.

## Transaction candidate, sans adoption

Une proposition examinable serait une autorité transactionnelle commune. Après les précontrôles et le calcul coûteux éventuel, acquérir les protections dans un ordre total : garde D/scope, comptes concernés, racines, familles, preuves/intention, puis emplacement logique K. Trier les identifiants à chaque niveau. Toute opération concurrente touchant ces invariants suivrait le même ordre ; une dépendance découverte tard exige relâchement et reprise, sans inversion. Cet ordre candidat ne modifie pas les priorités d’erreurs C5.

À L, après toute attente, revalider admission, preuve, R/T, F, E, droits et horloge. L’absence de K doit elle-même être protégée contre deux insertions concurrentes. Effectuer ensemble mutation, consommation, résultat K, audit obligatoire et intention outbox ; garder les protections jusqu’au commit durable. Aucun appel réseau dans cette section. Un reset peut invalider logiquement les sessions par E, sans imposer leur réécriture exhaustive, à condition que chaque autorisation contrôle cette époque.

Le retrait de D doit exclure aussi les transactions déjà admises : attendre leur issue ou les empêcher de committer avant réouverture. Un contrôle de D effectué seulement avant transaction ne suffit pas. La coordination concrète de cette garde avec une barrière extérieure au rollback reste à concevoir ; cet avis ne la déclare pas disponible.

## Traces qui départagent les interprétations

À partir de R/T=8, F active, logout Q préparé contre F/T=8 : une continuation de F committe et avance T à 9. Q atteint ensuite L. C3 annonce 204 avec révocation des continuations ; C5 impose 409 pour T obsolète. L’identité stable F ne prouve pas, seule, que l’ancienne preuve autorise encore cette commande terminale. Deux options restent ouvertes : continuation sans changement de T pertinent, ou capacité terminale ciblant F autorisée malgré ce changement. Chacune demande une définition et des oracles propriétaires.

Remplacer la continuation par un login indépendant B à T=9 interdit de recibler Q vers B. Sans exception ratifiée, l’avis 01 recommande d’appliquer le refus général 409. L’oracle 07-b de l’avis 05 reste donc conditionnel. Renommer immédiatement la déconnexion Q dans C7 réserve D à l’incarnation.

L décide l’éligibilité ; le commit durable décide l’effet acquis et permet le succès serveur. Si Q valide à L puis avorte, aucun fence avancé n’est acquis. Si Q committe, le login préparé à l’ancien T échoue ; une réponse Q perdue laisse seulement le client incertain. L valide avant échéance autorise, dans la proposition actuelle, un commit ultérieur sous budget borné : aucune garantie « zéro commit après échéance » n’est établie.

## Preuve d’absence et minimum prouvable

K absent ne signifie neuf qu’avec lecture autoritative, unicité atomique, intégrité du scope et conservation jusqu’à fermeture de tous ses droits de replay. Deux histoires — jamais exécuté, ou exécuté puis historique perdu — produisent autrement la même absence. Cache vide et ticket restauré non consommé ne les distinguent pas. Retrait connu : 409 ; autorité/intégrité invérifiable : 503. D restauré dans la même sauvegarde n’apporte aucune preuve indépendante.

**Prêts à rédaction :** séparer I/K/reçu/T, distinguer L/commit/acquittement, corriger D/Q et rendre l’oracle continuation conditionnel. **Non ratifiés :** primitive, ordre effectif des verrous, exception terminale F, budget, durabilité, conservation et procédure D. Le minimum actuellement prouvable est la cohérence documentaire de certaines courses sous hypothèses explicites, jamais leur exécution, l’exclusivité entre racines indépendantes ou READY. Architecture 06 propose A ; ce choix de reprise ne résout aucun de ces besoins transactionnels.
