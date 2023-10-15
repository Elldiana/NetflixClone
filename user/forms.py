from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.forms import widgets

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not CustomUser.objects.filter(email = email).exists():
            self.add_error('email','Bu email adresi mecvut değil')
        
        return email
    

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','username','email','birth_date','phone')

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget = widgets.TextInput(attrs={'class':'form-control'})
        self.fields['last_name'].widget = widgets.TextInput(attrs={'class':'form-control'})
        self.fields['username'].widget = widgets.TextInput(attrs={'class':'form-control'})
        self.fields['email'].widget = widgets.EmailInput(attrs={'class':'form-control'})
        self.fields['birth_date'].widget = widgets.DateInput(attrs={'class':'form-control','type':'date'})
        self.fields['phone'].widget = widgets.TextInput(attrs={'class':'form-control'})
        self.fields['password1'].widget = widgets.PasswordInput(attrs={'class':'form-control'})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'class':'form-control'})

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if CustomUser.objects.filter(email = email).exists():
            self.add_error('email','Bu email adresi sisteme kayıtlı')
        
        return email
    


class ProfileCreate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name','image')
        labels = {
            'name':'İsim',
            'image':'Resim'
        }

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget = widgets.TextInput(attrs={'class':'form-control'})
        self.fields['image'].widget = widgets.FileInput(attrs={'class':'form-control'})


class ChangePass(PasswordChangeForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget = widgets.PasswordInput(attrs={'class':'form-control'})
        self.fields['new_password1'].widget = widgets.PasswordInput(attrs={'class':'form-control'})
        self.fields['new_password2'].widget = widgets.PasswordInput(attrs={'class':'form-control'})