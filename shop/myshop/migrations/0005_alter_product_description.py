# Generated by Django 4.0.2 on 2023-05-04 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0004_remove_product_categor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=130),
        ),
    ]