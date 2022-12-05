from django.db import models
from django.core.files import File
from io import BytesIO

# importing barcode module
from barcode.writer import ImageWriter
import barcode


class Products(models.Model):
    id = models.CharField(max_length=12, primary_key=True, unique=True, editable=False)
    product_id = models.CharField(max_length=6, blank=False)
    country_id = models.CharField(max_length=1, null=False)
    manufacturer_id = models.CharField(max_length=7, blank=False)

    name = models.CharField(max_length=50, blank=False)
    barcode = models.ImageField(upload_to='barcodes/', blank=True)

    class Meta:
        verbose_name_plural = 'Products'
    
    
    def __str__(self):
        return f'{self.name}'


    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(f'', writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save('barcode.png', File(buffer), save=False)
        return super(Products, self).save(*args, **kwargs)
        