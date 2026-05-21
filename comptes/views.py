from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .models import Profil
from .serializers import InscriptionSerializer, ProfilSerializer


class InscriptionView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = InscriptionSerializer
    permission_classes = (permissions.AllowAny,)


class ProfilView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfilSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user.profil
