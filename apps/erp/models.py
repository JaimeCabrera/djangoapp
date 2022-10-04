from datetime import datetime

from django.db import models
from apps.erp.choices import gender_choices


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre', unique=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%y/%m/%d', null=True, blank=True)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['id']


class Client(models.Model):
    names = models.CharField(max_length=255, verbose_name='Nombres')
    surnames = models.CharField(max_length=255, verbose_name='Apellidos')
    cedula = models.CharField(max_length=10, unique=True, verbose_name='Cedula')
    date_of_birthday = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='Direccion ')
    sexo = models.CharField(max_length=155, choices=gender_choices, default='male', verbose_name='Sexo')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['id']


class Sale(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.client_id.names

    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'
        ordering = ['id']


class SaleDetail(models.Model):
    sale_id = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    amount = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.product_id.name

    class Meta:
        verbose_name = 'Sale detail'
        verbose_name_plural = 'Sales details'
        ordering = ['id']
