# Generated by Django 3.1.3 on 2020-12-01 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20201201_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonspecie',
            name='pokemon_type',
            field=models.ManyToManyField(related_name='species', to='my_app.PokemonType'),
        ),
    ]
