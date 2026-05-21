from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Profil(models.Model):
    ROLE_CHOICES = [
        ('acheteur', _('Acheteur')),
        ('vendeur', _('Vendeur')),
        ('admin', _('Admin')),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='acheteur')
    telephone = models.CharField(max_length=20, blank=True)
    adresse = models.TextField(blank=True)
    ville = models.CharField(max_length=100, blank=True)
    photo_profil = models.ImageField(upload_to='profils/', blank=True)
    biographie = models.TextField(blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    actif = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Profil')
        verbose_name_plural = _('Profils')
        ordering = ['-date_creation']

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} - {self.role}"
