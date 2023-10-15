from django.shortcuts import render,redirect
from user.models import *
from .models import *
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect('profilePage')
    return render(request,'index.html')

def search(request,id):
    if 'q' in request.GET and request.GET.get('q'):
        q = request.GET.get('q')
        print(q)
        search = Movie.objects.filter(title__contains = q)
    else:
        search = None

    profil = Profile.objects.get(id = id)
    profiller = request.user.profile_set.all()

    return render(request,'search.html',{
        'profil':profil,
        'profiller':profiller,
        'id':id,
        'search':search
    })



def filmler(request,id):
    if 'q' in request.GET and request.GET.get('q'):
        q = request.GET.get('q')
        print(q)
        search = Movie.objects.filter(title__contains = q)
    else:
        search = None

    profil = Profile.objects.get(id = id)
    profiller = request.user.profile_set.all()
    filmler = Movie.objects.all()

    # TURU KORKU OLAN FİLMLERİ FİLTRELEMEK İÇİN
    korku_id = Genre.objects.filter(title = 'Korku')[0].id
    korku_filmleri = Movie.objects.filter(genre = korku_id)
    
    return render(request,'filmler.html',{
        'profil':profil,
        'profiller':profiller,
        'id':id,
        'filmler':filmler,
        'korku':korku_filmleri,
        'search':search
    })



def movie(request,slug):
    movie = Movie.objects.get(slug = slug)
    return render(request,'movie.html',{
        'movie':movie
    })