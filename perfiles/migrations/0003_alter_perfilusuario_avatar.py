# Generated by Django 4.0 on 2021-12-21 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0002_alter_perfilusuario_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuario',
            name='avatar',
            field=models.ImageField(default='images/default.png', upload_to='Media/perfiles_usuario/'),
        ),
    ]
