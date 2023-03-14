from django.db import models


DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)

class Pokemon(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(default='Description not added yet')

    def get_image_url(self, request):
        image_url = DEFAULT_IMAGE_URL
        if self.image:
            image_url = request.build_absolute_uri(self.image.url)
        return image_url

    def __str__(self):
        return f'{self.title}'

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        null=True,
        on_delete=models.CASCADE)
    Lat = models.FloatField(blank=True)
    Len = models.FloatField(blank=True)
    Appeared_at = models.DateTimeField(null=True)
    Disappeared_at = models.DateTimeField(null=True)
    Level = models.CharField(max_length=20, null=True)
    Health = models.CharField(max_length=20, null=True)
    Strength = models.CharField(max_length=20, null=True)
    Defence = models.CharField(max_length=20, null=True)
    Stamina = models.CharField(max_length=20, null=True)
    def __str__(self):
        return f'{self.pokemon} Level {self.level}'
