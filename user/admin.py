from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (('Eklenen Bilgi', {'fields':['birth_date','phone']}),)


admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Profile)