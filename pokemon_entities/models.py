from django.db import models

DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


class Pokemon(models.Model):
    title = models.CharField('Имя покемона', max_length=200, blank=True)
    title_en = models.CharField('Имя покемона на английском', max_length=200, blank=True, null=True)
    title_jp = models.CharField('Имя покемона на японском', max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField('Описание покемона', blank=True, null=True)
    previous_evolution = models.ForeignKey(
        "self",
        verbose_name='Предыдущая стадия',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='next_evolutions'
    )

    def get_image_url(self, request):
        image_url = DEFAULT_IMAGE_URL
        if self.image:
            image_url = request.build_absolute_uri(self.image.url)
        return image_url

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        verbose_name='Покемон',
        null=True,
        on_delete=models.PROTECT,
        related_name='entities'
    )

    lat = models.FloatField('Широта', null=True, blank=True)
    len = models.FloatField('Долгота', null=True, blank=True)
    appeared_at = models.DateTimeField('Когда появляется', null=True, blank=True)
    disappeared_at = models.DateTimeField('Когда исчезает', null=True, blank=True)
    level = models.IntegerField('Уровень', null=True, blank=True)
    health = models.IntegerField('Здоровье', null=True, blank=True)
    strength = models.IntegerField('Сила', null=True, blank=True)
    defence = models.IntegerField('Защита', null=True, blank=True)
    stamina = models.IntegerField('Выносливость', null=True, blank=True)
