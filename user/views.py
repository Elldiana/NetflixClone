from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout,update_session_auth_hash
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def login_request(request):
    if request.user.is_authenticated:
        return redirect('profilePage')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            username = CustomUser.objects.get(email = email).username
            user = authenticate(request,username = username,password = password)
            if user is not None:
                login(request,user)
                return redirect('indexPage')
            else:
                 return render(request,'login.html',{
                    'form':form
                })  
        else:
          return render(request,'login.html',{
            'form':form
        })  

    form = LoginForm()
    return render(request,'login.html',{
        'form':form
    })

def register_request(request):
    if request.user.is_authenticated:
        return redirect('profilePage')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('loginPage')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username = username,password = password)
            login(request,user)
            return redirect('indexPage')
        else:
            return render(request,'register.html',{
                'form':form
            })
    form = RegisterForm()
    return render(request,'register.html',{
        'form':form
    })

@login_required(login_url='/login/')
def profile(request):
    if request.method == 'POST':
        id = request.POST['idSil']
        silinecek = Profile.objects.get(pk = id)
        silinecek.delete()
        messages.success(request,'Basarıyla silindi')
        return redirect('profilePage')
    return render(request,'profile.html')

@login_required(login_url='/login/')
def profile_manage(request,slug):
    
    if request.method == 'POST':
        form = ProfileCreate(request.POST , request.FILES)
        if form.is_valid():
            if request.user.profilleri_say() < 5:
                profil = form.save(commit=False)
                profil.owner = request.user
                profil.save()
                messages.success(request,'Profil başarı ile olusturuldu')
                return redirect('profilePage')
            else:
                messages.error(request,'Acabileceğiniz en fazla 5 adet profildir')
                return redirect('profilePage')
        else:
            return render(request,'profile-manage.html',{
                'form':form
            })
    
    form = ProfileCreate()
    return render(request,'profile-manage.html',{
        'form':form
    })


def logout_request(request):
    logout(request)
    return redirect('indexPage')

def hesap(request,id):
    if request.method == 'POST':
        request.user.delete()
        return redirect('indexPage')


    profil = CustomUser.objects.get(id = id)
    profiller = request.user.profile_set.all()


    return render(request,'hesap.html',{
        'profil':profil,
        'profiller':profiller
    })

def changePass(request):
    form = ChangePass(request.user)
    return render(request,'changePass.html',{
        'form':form
    })