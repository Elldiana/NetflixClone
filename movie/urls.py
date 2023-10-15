from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='indexPage'),
    path('filmler/<int:id>',filmler,name='filmlerPage'),
    path('search/<int:id>',search,name='searchPage'),
    path('movie/<slug:slug>',movie,name='moviePage'),
]
