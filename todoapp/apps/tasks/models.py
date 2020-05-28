from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField('Nome', max_length=150)
    description = models.TextField('Descrição', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

    def __str__(self):
        return self.name