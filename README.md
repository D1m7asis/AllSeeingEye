## 1. Установить библиотеки из [requirements](requirements.txt)

## 2. Запустить main.py

#### У вас будет запущен локальный веб-сервис на [localhost:5000](http://localhost:5000)

`(http://127.0.0.1:5000 к примеру)`

## 3. Работа с веб-сервисом - путем POST и GET запросов на

`http://localhost:5000/visited_links`

## Формат POST-запроса:

## `POST /visited_links`

```
{
    "links": "[
        "https://ya.ru/",
        "https://ya.ru/search/?text=мемы+с+котиками",
        "https://sber.ru",
        "https://stackoverflow.com/questions/65724760/how-it-is"
    
    ]"
}
```

## `RESPONSE:`

`HTTP 200`

```
{
    "status": "ok"
}
```

## Формат GET-запроса:

## `GET /visited_domains?from=###&to=###`

### Параметры:

`"from" - integer. С какого времени (секунд с начала эпохи)`

`"to" - integer. По какое время (секунд с начала эпохи)`

## `RESPONSE:`

`HTTP 200`

```
{
    "domains": "[
        "ya.ru",
        "sber.ru",
        "stackoverflow.com"
    ]",
    
    "status": "ok"
}
```