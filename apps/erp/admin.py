from django.contrib import admin

# Register your models here.
from apps.erp.models import *

admin.site.register(Category)
admin.site.register(Sale)
admin.site.register(SaleDetail)
admin.site.register(Product)
