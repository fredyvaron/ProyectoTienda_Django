# Generated by Django 4.0 on 2021-12-20 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuario',
            name='avatar',
            field=models.ImageField(default='images/default.png', upload_to='Media/perfiles/'),
        ),
    ]
