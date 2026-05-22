from django.db import models
from django.contrib.auth.models import User


class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Catégorie'


class Produit(models.Model):
    NEUF = 'neuf'
    BON_ETAT = 'bon_etat'
    USAGE = 'usage'
    ETATS = [(NEUF, 'Neuf'), (BON_ETAT, 'Bon état'), (USAGE, 'Usagé')]

    vendeur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='produits')
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, related_name='produits')
    nom = models.CharField(max_length=200)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=0)
    etat = models.CharField(max_length=20, choices=ETATS, default=NEUF)
    image = models.ImageField(upload_to='produits/', blank=True)
    stock = models.PositiveIntegerField(default=1)
    disponible = models.BooleanField(default=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['-date_ajout']
