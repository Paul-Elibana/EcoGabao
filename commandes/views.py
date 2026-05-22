from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from boutique.models import Produit
from .models import Commande, LigneCommande


def _get_panier(request):
    """Retourne le panier depuis la session sous forme de dict {produit_pk: quantite}."""
    return request.session.get('panier', {})


def _sauvegarder_panier(request, panier):
    request.session['panier'] = panier
    request.session.modified = True


def panier(request):
    panier_session = _get_panier(request)
    articles = []
    total = 0

    for pk_str, quantite in panier_session.items():
        try:
            produit = Produit.objects.get(pk=int(pk_str), disponible=True)
            sous_total = produit.prix * quantite
            total += sous_total
            articles.append({
                'produit': produit,
                'quantite': quantite,
                'sous_total': sous_total,
            })
        except Produit.DoesNotExist:
            pass

    return render(request, 'commandes/panier.html', {
        'articles': articles,
        'total': total,
    })


def ajouter_panier(request, produit_pk):
    produit = get_object_or_404(Produit, pk=produit_pk, disponible=True)
    panier_session = _get_panier(request)
    pk_str = str(produit_pk)

    if pk_str in panier_session:
        panier_session[pk_str] += 1
    else:
        panier_session[pk_str] = 1

    _sauvegarder_panier(request, panier_session)
    messages.success(request, f'"{produit.nom}" ajouté au panier.')
    return redirect('panier')


def retirer_panier(request, produit_pk):
    panier_session = _get_panier(request)
    pk_str = str(produit_pk)

    if pk_str in panier_session:
        del panier_session[pk_str]
        _sauvegarder_panier(request, panier_session)
        messages.info(request, 'Article retiré du panier.')

    return redirect('panier')


@login_required
def passer_commande(request):
    panier_session = _get_panier(request)

    if not panier_session:
        messages.error(request, 'Votre panier est vide.')
        return redirect('panier')

    if request.method == 'POST':
        adresse = request.POST.get('adresse_livraison', '').strip()
        if not adresse:
            messages.error(request, 'Veuillez saisir une adresse de livraison.')
            return render(request, 'commandes/passer_commande.html')

        commande = Commande.objects.create(
            acheteur=request.user,
            adresse_livraison=adresse,
        )

        for pk_str, quantite in panier_session.items():
            try:
                produit = Produit.objects.get(pk=int(pk_str))
                LigneCommande.objects.create(
                    commande=commande,
                    produit=produit,
                    quantite=quantite,
                    prix_unitaire=produit.prix,
                )
            except Produit.DoesNotExist:
                pass

        _sauvegarder_panier(request, {})
        messages.success(request, f'Commande #{commande.pk} passée avec succès !')
        return redirect('mes_commandes')

    return render(request, 'commandes/passer_commande.html')


@login_required
def mes_commandes(request):
    commandes = Commande.objects.filter(acheteur=request.user)
    return render(request, 'commandes/mes_commandes.html', {'commandes': commandes})
