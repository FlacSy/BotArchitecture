# Архитектура V3.1

* Примичание, архитектура сделана для ботов на aiogram 3.X.X

## Описание

Данный скрипт представляет собой основной файл для запуска бота, который использует фреймворк aiogram для работы с Telegram API. Он загружает настройки из файла конфигурации, создает бота, настраивает его параметры и запускает обработчики сообщений.

### Использование

Для запуска скрипта необходимо выполнить его в Python-интерпретаторе.

### Переменные

- `TOKEN`: Токен Telegram бота, полученный при создании бота в BotFather.

### Методы

- `register_routers()`: Асинхронная функция для регистрации маршрутов (обработчиков) бота.
- `load_modules(directories, ignore_files = ["__init__.py"])`: Асинхронная функция для динамической загрузки модулей из указанных директорий.

### Основной блок

- Создается экземпляр `Logger` для логирования.
- Выполняется основная асинхронная функция `main()`, которая запускает бота, регистрирует маршруты и загружает дополнительные модули из указанных директорий.


## Структура
```
├───bot
│   │   __init__.py
│   │
│   ├───admin
│   │   │   __init__.py
│   │   │
│   │   ├───handlers
│   │   │   │   __init__.py
│   │   │   │
│   │   │   ├───callbacks
│   │   │   │       __init__.py
│   │   │   │
│   │   │   └───commands
│   │   │           __init__.py
│   │   │
│   │   └───messages
│   │           __init__.py
│   │
│   └───user
│       │   __init__.py
│       │
│       └───handlers
│           │   __init__.py
│           │
│           ├───callbacks
│           │       __init__.py
│           │
│           ├───commands
│           │       help.py
│           │       start.py
│           │       __init__.py
│           │
│           ├───messages
│           │       __init__.py
│           │    
│           └───router
│                   user_router.py    
|           
│
├───config
│   │   config_manager.py
│   │   __init__.py
│   │
│   ├───development
│   │       config.ini
│   │
│   └───production
│           config.ini
│
├───database
│   │   database.py
│   │   __init__.py
│   │
│   ├───development
│   │       development.db
│   │
│   └───production
│           production.db
│
├───logs
│       log.log
│
└───tests
        __init__.py
```

