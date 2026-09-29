# Scripts

`repository/validate_repository.py` contrôle les fichiers versionnés : présence des références requises, organisation, fichiers interdits, marqueurs de clés privées et liens Markdown locaux. Il fonctionne avec Python 3.10+ et Git. Ce contrôle ciblé ne remplace pas un scanner complet de secrets ni une revue de sécurité.


`repository/check_whitespace.py` vérifie le delta Git fourni par l'événement GitHub : merge-base → head pour une PR ; before → after pour un push ; arbre vide → after pour création de branche. Le checkout conserve l'historique complet. Une référence absente, un SHA malformé ou un événement non pris en charge échoue explicitement. Le workflow reste limité à pull_request et push main ; aucun déploiement ni secret applicatif.

Les liens Markdown locaux doivent viser un fichier suivi, ou un répertoire contenant au moins un fichier suivi. L'existence d'un brouillon local non versionné ne suffit plus. Les liens symboliques sont refusés dans tous les composants du chemin, avant résolution, même si leur cible est suivie. Les chemins relatifs ordinaires (`./`, `../`) restent admis dans le dépôt. Les ancres et disponibilités HTTP restent hors du contrôle.
