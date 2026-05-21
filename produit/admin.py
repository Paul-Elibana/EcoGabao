from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Categorie, Produit, ImageProduit


class ImageProduitInline(admin.TabularInline):
    model = ImageProduit
    extra = 1


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('titre', 'vendeur', 'categorie', 'prix', 'etat', 'disponible', 'date_creation')
    list_filter = ('etat', 'disponible', 'categorie')
    search_fields = ('titre', 'description', 'vendeur__username')
    raw_id_fields = ('vendeur',)
    readonly_fields = ('date_creation', 'date_modification')
    inlines = (ImageProduitInline,)
