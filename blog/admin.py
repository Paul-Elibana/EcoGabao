from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'publie', 'vues', 'date_creation')
    list_filter = ('publie', 'date_creation')
    search_fields = ('titre', 'contenu', 'auteur__username')
    raw_id_fields = ('auteur',)
    readonly_fields = ('vues', 'date_creation', 'date_modification')
