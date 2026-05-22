from django import forms
from .models import Produit


class FormulaireProduit(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['categorie', 'nom', 'description', 'prix', 'etat', 'image', 'stock', 'disponible']
        labels = {
            'categorie': 'Catégorie',
            'nom': 'Nom du produit',
            'description': 'Description',
            'prix': 'Prix (FCFA)',
            'etat': 'État',
            'image': 'Image',
            'stock': 'Quantité en stock',
            'disponible': 'Disponible à la vente',
        }
        widgets = {
            'categorie': forms.Select(attrs={'class': 'form-select'}),
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du produit'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 4,
                'placeholder': 'Décrivez votre produit...',
            }),
            'prix': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Prix en FCFA'}),
            'etat': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
