from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    auteur = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'auteur', 'titre', 'contenu', 'image_couverture',
                  'vues', 'date_creation', 'date_modification')
        read_only_fields = ('id', 'auteur', 'vues', 'date_creation', 'date_modification')
