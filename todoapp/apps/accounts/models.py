from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserProfile(models.Model):
    photo = models.ImageField('Foto', upload_to='photos')
    secondary_email = models.EmailField('Email', blank=True, null=True)
    cell_phone = models.CharField('Celular', max_length=16)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    class Meta:
        verbose_name = 'Perfil do usuário'
        verbose_name_plural = 'Perfis dos usuários'

    def __str__(self):
        return self.user.first_name

    def clean(self):
        model = self.__class__
        if model.objects.count() > 0 and self.id != model.objects.get().id:
            raise ValidationError("Você já tem um perfil cadastrado!")
