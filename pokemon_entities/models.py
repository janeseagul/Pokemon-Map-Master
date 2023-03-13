from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(null=True)
    def __str__(self):
        return f'{self.title}'

class PokemonEntity(models.Model):
    Pokemon = models.ForeignKey(
        Pokemon,
        null=True,
        on_delete=models.CASCADE)
    Lat = models.FloatField(blank=True)
    Len = models.FloatField(blank=True)
    Appeared_at = models.DateTimeField(null=True)
    Disappeared_at = models.DateTimeField(null=True)
