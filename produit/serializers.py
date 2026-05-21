from rest_framework import serializers
from .models import Categorie, Produit, ImageProduit


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ('id', 'nom', 'description')


class ImageProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProduit
        fields = ('id', 'image', 'principale')


class ProduitSerializer(serializers.ModelSerializer):
    images = ImageProduitSerializer(many=True, read_only=True)
    vendeur = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Produit
        fields = ('id', 'vendeur', 'categorie', 'titre', 'description', 'prix',
                  'etat', 'disponible', 'images', 'date_creation', 'date_modification')
        read_only_fields = ('id', 'vendeur', 'date_creation', 'date_modification')
