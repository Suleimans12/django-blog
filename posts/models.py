from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    image = models.ImageField(height_field='height_field', width_field='width_field')
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    body = models.TextField()
    draft = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id })

    class Meta:
        db_table = 'posts'
