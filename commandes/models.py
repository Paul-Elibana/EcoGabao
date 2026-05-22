from django.db import models
from django.contrib.auth.models import User
from boutique.models import Produit


class Commande(models.Model):
    EN_ATTENTE = 'en_attente'
    CONFIRMEE = 'confirmee'
    LIVREE = 'livree'
    ANNULEE = 'annulee'
    STATUTS = [
        (EN_ATTENTE, 'En attente'),
        (CONFIRMEE, 'Confirmée'),
        (LIVREE, 'Livrée'),
        (ANNULEE, 'Annulée'),
    ]

    acheteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commandes')
    statut = models.CharField(max_length=20, choices=STATUTS, default=EN_ATTENTE)
    date = models.DateTimeField(auto_now_add=True)
    adresse_livraison = models.TextField()

    def total(self):
        return sum(ligne.sous_total() for ligne in self.lignes.all())

    def __str__(self):
        return f"Commande #{self.pk} - {self.acheteur.username}"

    class Meta:
        ordering = ['-date']


class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='lignes')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=0)

    def sous_total(self):
        return self.quantite * self.prix_unitaire
