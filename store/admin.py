from django.contrib import admin
from .models import Movie,Person,Reporter,POINT_DE_RETRAIT,AGENT_DESTINY,CLIENT,LIVREUR,PRESTATAIRE,MARQUE,CATEGORIE
from .models import SOUS_CATEGORIE,PANIER,EVENEMENT,RETOUR,COMMANDE,ARTICLE,CARACTERISTIQUE,DETAIL_COMMANDE,LIVRAISON
from .models import NOTIFICATION,VERSEMENT,FACTURE
# Register your models here.

admin.site.register(Movie)
admin.site.register(Person)
# admin.site.register(Article)
admin.site.register(Reporter)
admin.site.register(POINT_DE_RETRAIT)
admin.site.register(AGENT_DESTINY)
admin.site.register(CLIENT)
admin.site.register(LIVREUR)
admin.site.register(PRESTATAIRE)
admin.site.register(MARQUE)
admin.site.register(CATEGORIE)
admin.site.register(SOUS_CATEGORIE)
admin.site.register(PANIER)
admin.site.register(EVENEMENT)
admin.site.register(RETOUR)
admin.site.register(COMMANDE)
admin.site.register(ARTICLE)
admin.site.register(CARACTERISTIQUE)
admin.site.register(DETAIL_COMMANDE)
admin.site.register(LIVRAISON)
admin.site.register(NOTIFICATION)
admin.site.register(VERSEMENT)
admin.site.register(FACTURE)

