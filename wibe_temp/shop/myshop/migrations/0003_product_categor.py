# Generated by Django 4.0.2 on 2023-04-19 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0002_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categor',
            field=models.CharField(db_index=True, default='SOME STRING', max_length=150),
        ),
    ]
