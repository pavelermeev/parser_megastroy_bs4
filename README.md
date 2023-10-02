# Проект телеграм-бот-парсер для сайта Мегастрой.

### Описание проекта
Телеграм бот способен парсить страницы сайта Мегастрой и присылать с csv файл с данными, полученными с сайта.

### Запуск проекта
Создаём виртуальную среду для проекта
```
python -m venv venv
```

Устанавливаем необходимые компоненты из файла requirements.txt
```
pip install -r requirements.txt
```

Создаём файл .env c токеном телеграм-бота, формата:
```
BOT_TOKEN = ваш_токен
```

Запускаем бота
```
python3 bot.py
```

Автор: Ермеев Павел https://github.com/bytplokhim