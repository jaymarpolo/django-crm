# Generated by Django 3.1.2 on 2020-12-11 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20201211_2315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='firstname',
            new_name='first_name',
        ),
    ]
