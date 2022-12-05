from django.contrib import admin
from .models import Products

@admin.register(Products)
class ProductsTable(admin.ModelAdmin):
    list_display = ['name', 'barcode']
    ordering = ['name']