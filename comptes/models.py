from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
    VENDEUR = 'vendeur'
    ACHETEUR = 'acheteur'
    ROLES = [
        (VENDEUR, 'Vendeur'),
        (ACHETEUR, 'Acheteur'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil')
    role = models.CharField(max_length=20, choices=ROLES, default=ACHETEUR)
    telephone = models.CharField(max_length=20, blank=True)
    ville = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='profils/', blank=True)

    def __str__(self):
        return f"Profil de {self.user.username}"

    def est_vendeur(self):
        return self.role == self.VENDEUR

    class Meta:
        verbose_name = 'Profil'
