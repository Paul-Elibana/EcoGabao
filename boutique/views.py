from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Produit, Categorie
from .forms import FormulaireProduit


def accueil(request):
    produits = Produit.objects.filter(disponible=True)[:8]
    return render(request, 'boutique/accueil.html', {'produits': produits})


def liste_produits(request):
    categories = Categorie.objects.all()
    produits = Produit.objects.filter(disponible=True)
    categorie_selectionnee = None

    categorie_pk = request.GET.get('categorie')
    if categorie_pk:
        categorie_selectionnee = get_object_or_404(Categorie, pk=categorie_pk)
        produits = produits.filter(categorie=categorie_selectionnee)

    return render(request, 'boutique/liste_produits.html', {
        'produits': produits,
        'categories': categories,
        'categorie_selectionnee': categorie_selectionnee,
    })


def detail_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk, disponible=True)
    return render(request, 'boutique/detail_produit.html', {'produit': produit})


@login_required
def mes_produits(request):
    produits = Produit.objects.filter(vendeur=request.user)
    return render(request, 'boutique/mes_produits.html', {'produits': produits})


@login_required
def ajouter_produit(request):
    try:
        profil = request.user.profil
        if not profil.est_vendeur():
            messages.error(request, 'Seuls les vendeurs peuvent ajouter des produits.')
            return redirect('accueil')
    except Exception:
        messages.error(request, 'Vous devez être vendeur pour ajouter un produit.')
        return redirect('accueil')

    if request.method == 'POST':
        form = FormulaireProduit(request.POST, request.FILES)
        if form.is_valid():
            produit = form.save(commit=False)
            produit.vendeur = request.user
            produit.save()
            messages.success(request, 'Produit ajouté avec succès.')
            return redirect('mes_produits')
        else:
            messages.error(request, 'Veuillez corriger les erreurs.')
    else:
        form = FormulaireProduit()

    return render(request, 'boutique/formulaire_produit.html', {'form': form, 'action': 'Ajouter'})


@login_required
def modifier_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk, vendeur=request.user)

    if request.method == 'POST':
        form = FormulaireProduit(request.POST, request.FILES, instance=produit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produit modifié avec succès.')
            return redirect('mes_produits')
        else:
            messages.error(request, 'Veuillez corriger les erreurs.')
    else:
        form = FormulaireProduit(instance=produit)

    return render(request, 'boutique/formulaire_produit.html', {'form': form, 'action': 'Modifier', 'produit': produit})


@login_required
def supprimer_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk, vendeur=request.user)

    if request.method == 'POST':
        produit.delete()
        messages.success(request, 'Produit supprimé.')
        return redirect('mes_produits')

    return render(request, 'boutique/confirmer_suppression.html', {'produit': produit})
