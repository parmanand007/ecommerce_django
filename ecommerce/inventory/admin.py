from django.contrib import admin

# Register your models here.
from ecommerce.inventory.models import Category

admin.site.register(Category)