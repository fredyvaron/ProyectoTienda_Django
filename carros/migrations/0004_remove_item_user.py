# Generated by Django 4.0 on 2021-12-23 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0003_alter_item_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='user',
        ),
    ]