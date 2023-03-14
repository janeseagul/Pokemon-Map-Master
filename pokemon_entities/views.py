import folium

from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime

from .models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]

DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    current_datetime = localtime()
    pokemon_entities = PokemonEntity.objects.filter(
        Appeared_at__lte=current_datetime,
        Disappeared_at__gte=current_datetime,
    )

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon_entity in pokemon_entities:
        image_url = pokemon_entity.pokemon.get_image_url(request)
        add_pokemon(
            folium_map, pokemon_entity.Lat,
            pokemon_entity.Len,
            image_url
        )

    pokemons_from_model = Pokemon.objects.all()
    pokemons_on_page = []

    for pokemon in pokemons_from_model:
        image_url = None
        if pokemon.image:
            image_url = pokemon.image.url
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': image_url,
            'title_ru': pokemon.title,

        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=int(pokemon_id))
    image_url = pokemon.get_image_url(request)
    previous_evolution = pokemon.previous_evolution
    if previous_evolution:
        previous_evolution = {
            "title_ru": previous_evolution.title,
            "pokemon_id": previous_evolution.id,
            "img_url": previous_evolution.get_image_url(request)
        }
    next_evolution = pokemon.next_evolution.first()
    if next_evolution:
        next_evolution = {
            "title_ru": next_evolution.title,
            "pokemon_id": next_evolution.id,
            "img_url": next_evolution.get_image_url(request)
        }

    serialized_pokemon = {
        "pokemon_id": pokemon.id,
        "title_ru": pokemon.title,
        "title_en": pokemon.title_en,
        "title_jp": pokemon.title_jp,
        "img_url": image_url,
        "description": pokemon.description,
        "previous_evolution": previous_evolution,
        "next_evolution": next_evolution
    }

    current_datetime = localtime()
    pokemon_entities = PokemonEntity.objects.filter(
        pokemon=pokemon,
        Appeared_at__lte=current_datetime,
        Disappeared_at__gte=current_datetime
    )
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.lat,
            pokemon_entity.len,
            image_url
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': serialized_pokemon
    })