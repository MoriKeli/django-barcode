# Generated by Django 4.1.3 on 2022-12-05 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.CharField(editable=False, max_length=12, primary_key=True, serialize=False, unique=True)),
                ('product_id', models.CharField(max_length=6)),
                ('country_id', models.CharField(max_length=1)),
                ('manufacturer_id', models.CharField(max_length=7)),
                ('name', models.CharField(max_length=50)),
                ('barcode', models.ImageField(blank=True, upload_to='barcodes/')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
    ]