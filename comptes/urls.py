from django.urls import path
from .views import InscriptionView, ProfilView

app_name = 'comptes'

urlpatterns = [
    path('inscription/', InscriptionView.as_view(), name='inscription'),
    path('profil/', ProfilView.as_view(), name='profil'),
]
