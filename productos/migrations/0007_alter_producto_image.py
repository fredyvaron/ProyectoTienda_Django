# Generated by Django 4.0 on 2021-12-21 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_alter_producto_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='image',
            field=models.ImageField(default='defaul.png', upload_to='products/'),
        ),
    ]
