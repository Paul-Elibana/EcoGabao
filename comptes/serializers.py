from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from .models import Profil


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('id',)


class ProfilSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profil
        fields = ('id', 'user', 'role', 'telephone', 'adresse', 'ville',
                  'photo_profil', 'biographie', 'date_creation', 'date_modification', 'actif')
        read_only_fields = ('id', 'date_creation', 'date_modification')

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        for attr, value in user_data.items():
            setattr(instance.user, attr, value)
        instance.user.save()
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class InscriptionSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, label=_('Mot de passe'))
    role = serializers.ChoiceField(choices=Profil.ROLE_CHOICES, default='acheteur', label=_('Rôle'))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'role')

    def create(self, validated_data):
        role = validated_data.pop('role', 'acheteur')
        user = User.objects.create_user(**validated_data)
        Profil.objects.create(user=user, role=role)
        return user
