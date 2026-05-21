from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _
from .models import Produit, Categorie
from .serializers import ProduitSerializer, CategorieSerializer


class CategorieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    permission_classes = (permissions.AllowAny,)


class ProduitViewSet(viewsets.ModelViewSet):
    serializer_class = ProduitSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.action in ('update', 'partial_update', 'destroy'):
                return Produit.objects.filter(vendeur=self.request.user)
        return Produit.objects.filter(disponible=True).select_related('vendeur', 'categorie').prefetch_related('images')

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(vendeur=self.request.user)
