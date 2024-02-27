# Архитектура V3.0

* Примичание, архитектура сделана для ботов на aiogram 3.X.X

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

> Я устал писать README, допишите остальное 👉✪ ω ✪👈  