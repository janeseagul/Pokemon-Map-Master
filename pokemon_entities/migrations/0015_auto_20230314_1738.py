# Generated by Django 2.2.24 on 2023-03-14 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0014_auto_20230314_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='Lat',
            field=models.FloatField(blank=True, null=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Len',
            field=models.FloatField(blank=True, null=True, verbose_name='Долгота'),
        ),
    ]
