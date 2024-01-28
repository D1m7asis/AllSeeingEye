0. По необходимости установить библиотеки:

pip install requests

pip install flask

pip install requests

1. Скачать репозиторий

2. Запустить main.py

У вас будет запущен локальный веб-сервис на адресе localhost:5000 (http://127.0.0.1:5000/ к примеру)

3. Вы можете работать с сервисом путём POST и GET запросов на адрес http://127.0.0.1:5000/visited_links
   
3.1 Пример POST-запроса

   POST /visited_links

   {

"links": [

"https://ya.ru/",

"https://ya.ru/search/?text=мемы+с+котиками",

"https://sber.ru",

"https://stackoverflow.com/questions/65724760/how-it-is"

]

}

ОТВЕТ /visited_links

{
"status": "ok"
}
HTTP 200

3.2 Пример GET-запроса

GET /visited_domains?from=1545221231&to1545217638

QUERPARAMS:

"from" - integer. С какого времени в формате (число секунд с начала эпохи)

"to" - integer. По какое время в формате (число секунд с начала эпохи)

ОТВЕТ /visited_links

{

"domains": [

"ya.ru",

"sber.ru",

"stackoverflow.com"

],

"status": "ok"

}

HTTP 200

