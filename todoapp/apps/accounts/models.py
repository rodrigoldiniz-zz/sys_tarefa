from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    photo = models.ImageField('Foto', upload_to='photos')
    secondary_email = models.EmailField('Email', blank=True, null=True)
    cell_phone = models.CharField('Celular', max_length=16)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Perfil do usuário'
        verbose_name_plural = 'Perfis dos usuários'

    def __str__(self):
        return self.user.name
