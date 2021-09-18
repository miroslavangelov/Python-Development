from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from common.forms import CommentForm
from core.decorators import can_like, can_delete_or_edit
from pets.forms import PetCreateForm, EditPetForm
from pets.models import Pet, Like


def get_all(request):
    context = {
        'pets': Pet.objects.all(),
    }
    return render(request, "pets_list.html", context)


@login_required(login_url='accounts:login')
def pet_details(request, pet_id):
    current_pet = Pet.objects.get(pk=pet_id)
    current_pet.likes_count = current_pet.like_set.count()
    is_owner = current_pet.user == request.user
    is_liked_by_user = current_pet.like_set.filter(user_id=request.user.id).exists()

    context = {
        'pet': current_pet,
        'is_owner': is_owner,
        'is_liked': is_liked_by_user,
        'comment_form': CommentForm(
            initial={
                'pet_id': pet_id,
            }),
        'comments': current_pet.comment_set.all(),
    }

    return render(request, 'pet_details.html', context)


@can_like(Pet)
def like_pet(request, pet_id):
    current_pet = Pet.objects.get(pk=pet_id)
    is_liked_by_user = current_pet.like_set.filter(user_id=request.user.id).first()

    if is_liked_by_user:
        is_liked_by_user.delete()
    else:
        like = Like(pet=current_pet, user=request.user)
        like.save()

    return redirect('pets:pet_details', pet_id)


@login_required(login_url='accounts:login')
def create(request):
    pet = Pet()
    return persist(request, pet, "pet_create.html")


@can_delete_or_edit(Pet)
def edit(request, pet_id):
    pet = Pet.objects.get(pk=pet_id)
    EditPetForm(request.POST, request.FILES, instance=pet)
    return persist(request, pet, "pet_edit.html")


@can_delete_or_edit(Pet)
def delete(request, pet_id):
    pet = Pet.objects.get(pk=pet_id)
    if request.method == "GET":
        return render(request, "pet_delete.html", {'pet': pet})
    else:
        pet.delete()
        return redirect("pets:pets_list")


@login_required(login_url='accounts:login')
def comment_pet(request, pet_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()

    return redirect("pets:pet_details", pet_id)


def persist(request, pet, template, form=None):
    if request.method == "GET":
        form = PetCreateForm(instance=pet)
        return render(request, template, {'form': form})
    else:
        if not form:
            form = PetCreateForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()

            return redirect('pets:pet_details', pet.id)

        return render(request, template, {'form': form})
