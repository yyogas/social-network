# Avis 14 — Frontière identité/profil/avatar et accès aux médias

Avis documentaire d’un nouveau sous-agent, distinct de l’équipe 08 ; aucune adoption ni preuve runtime. Références : snapshot HQ `4d3cd079e92217936af3292429a38f91f7b576ff`, contrat Backend v0.1 HQ et proposition PR #28 v0.3 au SHA exact `0a7fcd54b996cc292bfe98c61a835613837def32`. Les options A/B et les garanties entre racines navigateur indépendantes restent ouvertes.

**Périmètre contractuel L1.** `implementation-readiness.md` (§3, lots L1/L2) inclut compte, session révoquable, profil minimal à visibilité définie, ainsi que les effets contractuels du blocage et de la suspension. L’identité du compte et celle du profil restent distinctes ; les champs privés sont filtrés selon le lecteur. L’avatar de FEAT-003 dépend explicitement de L2 : le différer ou contractualiser cette dépendance demeure un arbitrage, pas une autorisation d’upload implicite. L1 ne couvre donc pas, par sa seule livraison, admission de fichiers, traitement, dérivés, distribution ou purge média. Aucun fournisseur, format supplémentaire ou fonctionnalité média n’est proposé ici.

Une vue privée liée au cookie ne protège **pas automatiquement une URL média autonome**. Le contrat d’acquisition v0.3 C1/C2 sécurise une projection et sa liaison ; il ne démontre pas un contrôle d’accès courant sur chaque chemin servant des octets. De même, `no-store`, un identifiant opaque ou une URL signée courte ne constituent pas une autorisation actuelle.

**Six assertions et preuves futures attendues — toutes PLANNED :**

1. **Identités cohérentes.** Après A→B, une réponse tardive contenant profil ou référence d’avatar A ne doit pas alimenter la vue B. Preuve : chronologie des intentions, réponses et rendus sous changement de compte, restauration de page et profil absent. `profile_ref=null` ne déclenche aucune création ; nécessité de `account_ref/profile_ref` encore à justifier selon v0.3 C1.

2. **Lecture directe soumise au droit courant.** Chaque dérivé protégé doit dépendre du parent profil ou contenu autorisé, de l’état du compte et des restrictions applicables ; aucun original ni chemin d’origine ne contourne ce contrôle. Preuve : requêtes directes avec ancienne URL, autre compte, absence de session et parent interdit, y compris variantes. Sources : Media, matrice et MEDIA-API-05 ; Privacy §3.2.

3. **Cache sans pouvoir d’autorisation.** Un cache chaud ne restitue pas un objet après perte du droit ; autorité invérifiable implique refus contrôlé. Preuve : mêmes lectures avant/après restriction avec cache chaud, panne d’autorité, historique et restauration navigateur. Distinguer cache objet interne, cache partagé et mémoire client ; vérifier le comportement réel au-delà du header. Sources : Backend C6 historique, v0.3 C6.

4. **Révocation correctement bornée.** Logout retire la famille F et ses continuations ; recovery vise les anciennes sessions du compte selon la proposition à ratifier. Les lectures de fichiers protégés ne réutilisent pas une autorisation périmée ; les assets ne prolongent pas IDLE. Preuve : ancienne session, continuation, session indépendante témoin et récupération, avec instant autoritatif tracé. Aucun effet global entre racines indépendantes n’est acquis.

5. **Remplacement et retrait sans résurrection.** Ancien avatar, anciennes générations et jobs tardifs respectent retrait et tombstone ; annuler une sanction ne restaure pas un fichier supprimé. Preuve : remplacement concurrent avec suppression, traitement retardé et réessai ; anciennes URLs restent interdites selon la politique retenue. Source : Media, transitions et cycle des données.

6. **Suppression vérifiable par système.** Compte supprimé entraîne retrait des avatars historiques, variantes et accès associés ; purge partielle reste visible comme telle. Preuve : accusés par objet/version, panne de purge et restauration isolée réappliquant restrictions depuis une source non reculée. Conservation justifiée demeure cloisonnée ; copies déjà reçues non récupérables. Source : Privacy §3.4.

**Dépendances propriétaires.** 04/08 contractualisent chaque chemin de lecture et la propagation ; 03/14 démontrent contrôle autoritatif, caches et révocation ; 01/09/15 fixent audiences, restrictions, exceptions et rétention ; 05/06 traitent références périmées ; 18 définit les preuves. Le délai média évoqué par Backend v0.1 doit être concilié avec le refus des nouvelles lectures dès confirmation proposé par Media. La convergence auth v0.3 ne tranche pas cet écart. HQ arbitre le périmètre ; L1 seul ne vaut pas ouverture du pilote.
