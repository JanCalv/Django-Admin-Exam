# Generated by Django 3.1.3 on 2020-12-02 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_auto_20201202_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='pokemon_trainer',
            field=models.CharField(max_length=200),
        ),
    ]
