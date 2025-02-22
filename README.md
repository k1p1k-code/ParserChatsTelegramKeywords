# Запуск 

|[Скачать python](https://www.python.org/ftp/python/3.13.2/python-3.13.2-amd64.exe)



|Установить зависимости
```
pip install -r requments.txt
```


|Получить API_HASH, API_ID - [здесь](https://my.telegram.org/auth)

|Создать Telegram бота - [здесь](https://t.me/BotFather)

|Настройить config.py

```
token: токен бота
```

```
chat_send: чат куда будут приходить уведомление
```

```
chats: откуда парситься информация
```

```
words: ключевые слова
```

```
TELEGRAM_API_ID=полученый api_id
TELEGRAM_API_HASH=полученый api_hash
```


|Запуск
```
python main.py
```

| При первом запуске у вам нужно будет создать сессию можно использовать готовые желательно pyrogram не проверял совместимость с telebot


