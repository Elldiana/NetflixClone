from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login_request,name='loginPage'),
    path('register/',register_request,name='registerPage'),
    path('profile/',profile,name='profilePage'),
    path('profile-manage/<slug:slug>',profile_manage,name='managePage'),
    path('logout',logout_request,name='logoutPage'),
    path('hesap/<int:id>',hesap,name='hesap'),
    path('change-password/',changePass,name='changePass'),
]
