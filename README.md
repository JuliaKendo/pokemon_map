# Карта покемонов

![screenshot](https://dvmn.org/filer/canonical/1563275070/172/)

### Предметная область

Сайт для помощи по игре [Pokemon GO](https://www.pokemongo.com/en-us/). Это игра про ловлю [покемонов](https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%BA%D0%B5%D0%BC%D0%BE%D0%BD).

Суть игры в том, что на карте появляются покемоны. Может быть сразу несколько особей одного и того же покемона: например, 3 Бульбазавра. Каждую особь могут поймать сразу несколько игроков.

В игре есть механика эволюции. Покемон одного вида может "эволюционировать" в другого. Так, например, Бульбазавр превращается в Ивизавра, а тот превращается в Венузавра.

![bulba evolution](https://dvmn.org/filer/canonical/1562265973/167/)

### Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 2 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта

### Как запустить

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Затем установите зависимости:

```sh
pip install -r requirements.txt
```

Выполните миграцию:

```sh
python3 manage.py migrate
```

Запустите сервер

```sh
python3 manage.py runserver
```

Перейдите по ссылке: [127.0.0.1:8000](http://127.0.0.1:8000)

### Как попасть в админку

Создайте `superuser`

```sh
python3 manage.py createsuperuser
```

Запустите сервер

```sh
python3 manage.py runserver
```
Перейдите по ссылке: [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin/)

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
