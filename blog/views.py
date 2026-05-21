from rest_framework import viewsets, permissions, mixins
from .models import Post
from .serializers import PostSerializer


class PostViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(publie=True).select_related('auteur')

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(auteur=self.request.user)
