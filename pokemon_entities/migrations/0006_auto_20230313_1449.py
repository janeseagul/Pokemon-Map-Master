# Generated by Django 2.2.24 on 2023-03-13 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_auto_20230313_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='Defence',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='Health',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='Level',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='Stamina',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='Strength',
            field=models.TextField(null=True),
        ),
    ]
