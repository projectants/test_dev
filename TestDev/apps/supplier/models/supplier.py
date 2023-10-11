from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nome', unique=True)
    social_reason = models.CharField(
        max_length=200, verbose_name='Razão Social', unique=True)
    state = models.CharField(
        max_length=200, verbose_name='Estado', unique=True)
    city = models.CharField(max_length=200, verbose_name='Cidade', unique=True)
    district = models.CharField(
        max_length=200, verbose_name='Bairro', unique=True)
    address = models.CharField(
        max_length=200, verbose_name='Endereço', unique=True)
    cnpj = models.CharField(max_length=14, verbose_name='CNPJ', unique=True)
    phone = models.CharField(
        max_length=200, verbose_name='Telefone', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
