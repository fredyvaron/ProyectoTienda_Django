# Generated by Django 4.0 on 2021-12-21 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_alter_producto_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='image',
            field=models.ImageField(default='images/default.png', upload_to='categorias/'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='image',
            field=models.ImageField(default='images/default.png', upload_to='products/'),
        ),
    ]
