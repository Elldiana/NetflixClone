from django.contrib import admin
from .models import *
# Register your models here.



class AdminGenre(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

class AdminMovie(admin.ModelAdmin):
    list_display = ('title','description')
    # admin paneline filtreleme ekranı
    list_filter = ('genre',)
    search_fields = ('title','description')
    list_display_links = ('title','description')

    

admin.site.register(Movie,AdminMovie)
admin.site.register(Genre,AdminGenre)