# Generated by Django 4.2.7 on 2023-12-12 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcc', '0002_rename_type1_pokemoncard_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemoncard',
            old_name='Type',
            new_name='Type1',
        ),
    ]