from django.db import models
from django.utils.text import slugify
# Create your models here.

class Genre(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(blank=True,null=True,unique=True)

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='movie_pic')
    description = models.TextField(max_length=200)
    video = models.FileField(upload_to='movie_video')
    slug = models.SlugField(null=True,blank=True,unique=True)

    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)



