from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profil


class FormulaireInscription(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='Adresse e-mail',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'votre@email.com'}),
    )
    role = forms.ChoiceField(
        choices=Profil.ROLES,
        label='Vous êtes',
        widget=forms.RadioSelect,
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Profil.objects.create(user=user, role=self.cleaned_data['role'])
        return user


class FormulaireConnexion(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Mot de passe'})


class FormulaireProfilField(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['telephone', 'ville', 'photo']
        labels = {
            'telephone': 'Téléphone',
            'ville': 'Ville',
            'photo': 'Photo de profil',
        }
        widgets = {
            'telephone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex : +241 07 00 00 00',
            }),
            'ville': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex : Libreville',
            }),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
