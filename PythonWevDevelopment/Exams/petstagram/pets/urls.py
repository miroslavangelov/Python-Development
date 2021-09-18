from django.urls import path

from pets.views import get_all, pet_details, like_pet, create, edit, delete, comment_pet

urlpatterns = [
    path('', get_all, name='pets_list'),
    path('details/<int:pet_id>/', pet_details, name='pet_details'),
    path('like/<int:pet_id>/', like_pet, name='like_pet'),
    path('create/', create, name='create'),
    path('edit/<int:pet_id>', edit, name='edit'),
    path('delete/<int:pet_id>', delete, name='delete'),
    path('comment/<int:pet_id>', comment_pet, name='comment_pet'),
]
