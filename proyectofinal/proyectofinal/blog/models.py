from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    fecha = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(verbose_name='Imagen', upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.titulo

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.png', upload_to='profile_images')
    descripcion = models.TextField()

    def __str__(self):
        return self.user.username