from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = _('Catégorie')
        verbose_name_plural = _('Catégories')

    def __str__(self):
        return self.nom


class Produit(models.Model):
    ETAT_CHOICES = [
        ('neuf', _('Neuf')),
        ('bon_etat', _('Bon état')),
        ('usage', _('Usagé')),
    ]

    vendeur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='produits')
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, related_name='produits')
    titre = models.CharField(max_length=200)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=0)
    etat = models.CharField(max_length=20, choices=ETAT_CHOICES, default='bon_etat')
    disponible = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Produit')
        verbose_name_plural = _('Produits')
        ordering = ['-date_creation']

    def __str__(self):
        return self.titre


class ImageProduit(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='produits/')
    principale = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Image produit')
        verbose_name_plural = _('Images produit')
