from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return f'{self.category_name}'
    
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True,upload_to='media/picture/%Y/%m/')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    
    
    def __str__(self) -> str:
        return f'Contato: {self.first_name} {self.last_name}'
    
