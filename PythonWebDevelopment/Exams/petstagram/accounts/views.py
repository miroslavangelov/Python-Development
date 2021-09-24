from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import SignUpForm, SignInForm, ProfileForm
from accounts.models import Profile
from pets.models import Pet


def register(request):
    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('common:landing_page')

    else:
        form = SignUpForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/register.html', context)


def login_user(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('common:landing_page')
    form = SignInForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('common:landing_page')


@login_required(login_url='accounts:login')
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    user_pets = Pet.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('common:landing_page')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
        'pets': user_pets,
    }

    return render(request, 'accounts/user_profile.html', context)
