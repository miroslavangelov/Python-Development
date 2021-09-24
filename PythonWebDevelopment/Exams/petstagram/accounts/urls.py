from django.urls import path

from accounts.views import register, login_user, logout_user, profile_details

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile_details, name='profile_details'),
]
