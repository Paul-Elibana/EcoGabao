from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import FormulaireInscription, FormulaireConnexion, FormulaireProfilField


def inscription(request):
    if request.user.is_authenticated:
        return redirect('accueil')

    if request.method == 'POST':
        form = FormulaireInscription(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte a été créé avec succès. Vous pouvez maintenant vous connecter.')
            return redirect('connexion')
        else:
            messages.error(request, 'Veuillez corriger les erreurs ci-dessous.')
    else:
        form = FormulaireInscription()

    return render(request, 'comptes/inscription.html', {'form': form})


def connexion(request):
    if request.user.is_authenticated:
        return redirect('accueil')

    if request.method == 'POST':
        form = FormulaireConnexion(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Bienvenue, {user.username} !')
            next_url = request.GET.get('next', 'accueil')
            return redirect(next_url)
        else:
            messages.error(request, 'Identifiant ou mot de passe incorrect.')
    else:
        form = FormulaireConnexion(request)

    return render(request, 'comptes/connexion.html', {'form': form})


def deconnexion(request):
    logout(request)
    messages.info(request, 'Vous avez été déconnecté.')
    return redirect('accueil')


@login_required
def profil(request):
    try:
        profil_obj = request.user.profil
    except Exception:
        from .models import Profil
        profil_obj = Profil.objects.create(user=request.user)

    if request.method == 'POST':
        form = FormulaireProfilField(request.POST, request.FILES, instance=profil_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre profil a été mis à jour.')
            return redirect('profil')
        else:
            messages.error(request, 'Veuillez corriger les erreurs.')
    else:
        form = FormulaireProfilField(instance=profil_obj)

    return render(request, 'comptes/profil.html', {'form': form, 'profil': profil_obj})
