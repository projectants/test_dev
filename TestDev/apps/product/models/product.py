from django.db import models

from apps.category.models import Category
from apps.supplier.models import Supplier


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nome', unique=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Data de Cadastro')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Data de Atualização')
    description = models.TextField(
        verbose_name='Descrição', blank=True, null=True)
    category = models.ForeignKey(
        Category, verbose_name='Categoria', on_delete=models.CASCADE
    )

    supplier = models.ForeignKey(
        Supplier, verbose_name='Fornecedor', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
