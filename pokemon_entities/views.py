import folium

from django.http import HttpResponseNotFound
from django.shortcuts import render

from .models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # tooltip=name,  # disable tooltip because of folium encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons_on_page = []
    pokemons = Pokemon.objects.all()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        pokemon_image = request.build_absolute_uri(pokemon.image.url) if pokemon.image else DEFAULT_IMAGE_URL
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon_image,
            'title_ru': pokemon.title,
        })

        pokemon_entities = PokemonEntity.objects.filter(pokemon=pokemon)
        for pokemon_entity in pokemon_entities:
            add_pokemon(
                folium_map, pokemon_entity.lat, pokemon_entity.lon, pokemon_image)

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    if not pokemon:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')
    pokemon_image = request.build_absolute_uri(pokemon.image.url) if pokemon.image else DEFAULT_IMAGE_URL
    requested_pokemon = {
        'pokemon_id': pokemon.id,
        'img_url': pokemon_image,
        'title_ru': pokemon.title,
        'description': pokemon.description,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
    }
    add_previous_pokemon(request, requested_pokemon, pokemon)
    add_next_pokemon(request, requested_pokemon, pokemon)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemon_entities = PokemonEntity.objects.filter(pokemon=pokemon)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.lat, pokemon_entity.lon, pokemon_image)

    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': requested_pokemon})


def add_previous_pokemon(request, requested_pokemon, pokemon_parent):
    pokemon = pokemon_parent.previous_evolution
    if not pokemon:
        return
    pokemon_image = request.build_absolute_uri(pokemon.image.url) if pokemon.image else DEFAULT_IMAGE_URL
    requested_pokemon['previous_evolution'] = {
        'pokemon_id': pokemon.id,
        'img_url': pokemon_image,
        'title_ru': pokemon.title,
    }


def add_next_pokemon(request, requested_pokemon, pokemon_inheritor):
    pokemons = pokemon_inheritor.pokemon_set.all()
    if not pokemons:
        return
    pokemon_image = request.build_absolute_uri(pokemons[0].image.url) if pokemons[0].image else DEFAULT_IMAGE_URL
    requested_pokemon['next_evolution'] = {
        'pokemon_id': pokemons[0].id,
        'img_url': pokemon_image,
        'title_ru': pokemons[0].title,
    }
