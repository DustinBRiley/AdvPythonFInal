# Generated by Django 4.2.7 on 2023-12-12 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcc', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemoncard',
            old_name='Type1',
            new_name='Type',
        ),
    ]
