<<<<<<< HEAD
# Архитектура V3.0

* Примичание, архитектура сделана для ботов на aiogram 3.X.X

=======
# Архитектура V2.1

* Примичание, архитектура сделана для ботов на aiogram 2.x 
 
>>>>>>> df708176cbb16e4c3be30a059e5d5556f152c6d0
## Структура

```
├───bot
│   │   __init__.py
│   │
<<<<<<< HEAD
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
│       ├───handlers
│       │   │   __init__.py
│       │   │
│       │   ├───callbacks
│       │   │       __init__.py
│       │   │
│       │   └───commands
│       │           help.py
│       │           start.py
│       │           __init__.py
│       │
│       └───messages
│               __init__.py
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



> Я устал, README допишу позже..
=======
│   └───handlers
│       │   help.py
│       │   start.py
│       │   __init__.py
│
├───config
│   │   secrets.ini
│   │   secrets.py
│   │   settings.ini
│   │   settings.py
│   │   __init__.py
│
├───database
│   │   bot.db
│   │   database.py
│   │   __init__.py
│
├───logs
│
├───tests
│   │   __init__.py
│
└───utils
    │   helpers.py
    │   __init__.py
.gitignore
main.py
```

### Описание структуры

- **.gitignore**: Файл, определяющий игнорируемые файлы и папки при работе с системой контроля версий Git.

- **main.py**: Основной файл для запуска бота.

- **bot**: Основной модуль бота.

    - **__init__.py**: Индикатор, что каталог `bot` является пакетом Python.
    
    - **handlers**: Каталог, содержащий обработчики команд бота.

        - **help.py**: Модуль для обработки команды "help".
        
        - **start.py**: Модуль для обработки команды "start".
        
        - **__init__.py**: Индикатор, что каталог `handlers` является пакетом Python.

- **config**: Каталог, содержащий файлы конфигурации.

    - **secrets.ini**: Файл для хранения секретных данных.
    
    - **secrets.py**: Модуль для доступа к секретным данным.
    
    - **settings.ini**: Файл с настройками.
    
    - **settings.py**: Модуль для доступа к настройкам.
    
    - **__init__.py**: Индикатор, что каталог `config` является пакетом Python.

- **database**: Каталог для хранения базы данных и модуля для работы с ней.

    - **bot.db**: Файл базы данных.
    
    - **database.py**: Модуль для взаимодействия с базой данных.
    
    - **__init__.py**: Индикатор, что каталог `database` является пакетом Python.

- **logs**: Папка, предназначенная для хранения логов.

- **tests**: Каталог, содержащий модули для тестирования.

    - **__init__.py**: Индикатор, что каталог `tests` является пакетом Python.

- **utils**: Каталог, содержащий утилитарные модули.

    - **helpers.py**: Модуль с вспомогательными функциями.
    
    - **__init__.py**: Индикатор, что каталог `utils` является пакетом Python.
>>>>>>> df708176cbb16e4c3be30a059e5d5556f152c6d0
