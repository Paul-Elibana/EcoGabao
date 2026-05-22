from django.urls import path
from . import views

urlpatterns = [
    path('panier/', views.panier, name='panier'),
    path('panier/ajouter/<int:produit_pk>/', views.ajouter_panier, name='ajouter_panier'),
    path('panier/retirer/<int:produit_pk>/', views.retirer_panier, name='retirer_panier'),
    path('commander/', views.passer_commande, name='passer_commande'),
    path('mes-commandes/', views.mes_commandes, name='mes_commandes'),
]
