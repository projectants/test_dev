from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Nome', unique=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Data de Cadastro')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Data de Atualização')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
