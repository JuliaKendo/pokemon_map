from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Наименование')
    title_en = models.CharField(
        max_length=200, blank=True,
        verbose_name='по английски'
    )
    title_jp = models.CharField(
        max_length=200, blank=True,
        verbose_name='по японски'
    )
    image = models.ImageField(
        upload_to='', null=True,
        blank=True, verbose_name='Изображение'
    )
    description = models.TextField(blank=True, verbose_name='Описание')
    previous_evolution = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name='Из кого эвалюционировал')

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, verbose_name='Покемон'
    )
    lat = models.FloatField(verbose_name='Широта', default=0.0, blank=True)
    lon = models.FloatField(verbose_name='Долгота', default=0.0, blank=True)
    appeared_at = models.DateTimeField(
        null=True, blank=True, verbose_name='Время появления'
    )
    disappeared_at = models.DateTimeField(
        null=True, blank=True, verbose_name='Время исчезновения'
    )
    level = models.IntegerField(default=0, blank=True, verbose_name='Уровень')
    health = models.IntegerField(
        default=0, blank=True, verbose_name='Здоровье'
    )
    strength = models.IntegerField(default=0, blank=True, verbose_name='Сила')
    defence = models.IntegerField(
        default=0, blank=True, verbose_name='Защита'
    )
    stamina = models.IntegerField(
        default=0, blank=True, verbose_name='Выносливость'
    )

    def __str__(self):
        return f'{self.pokemon.title} {self.level} level'
