# Foodgram

Описание проекта
    
    Проект 'Продуктовый помощник' реализует сайт кулинарных рецептов,
    в котором вы можете создавать рецепты, подписываться на понравившихся
    авторов, подобрать себе коллекцию любимых рецептов и другой функционал.
    
    Проект запускается в 4 контейнерах:
        nginx
        backend
        frontend
        db

    Авторизация по токену.
    Все запросы от имени пользователя должны выполняться с 
    заголовком "Authorization: Token TOKENVALUE"
    
    Все запросы начинаются с /api/

Необходимые инструменты для запуска

    docker
    docker-compose

Запуск приложения

    Все действия выполняются из директории /infra/
    Перед запуском необходимо создать файл .env с переменными:
        DB_ENGINE
        DB_NAME
        POSTGRES_USER
        POSTGRES_PASSWORD
        DB_HOST
        DB_PORT
    
    Запуск контейнеров

        docker-compose up -d --build

    
    Заполнение бд
        
        docker exec -it backend bash
        python3 manage.py fill_db

    Для нормального функционирования приложения (создания рецептов, использования фильтров),
    через админку необходимо добавить Tags

Стек используемых технологий

    Python
    Django, DRF
    Docker
    PostgreSQL
    CI
    nginx
    simplejwt
    djoser

Доступные эндпоинты
    
    docs/                               # Документация проекта

    admin/                              # Панель администратора
    
    POST auth/token/login/              # Получить токен авторизации
    POST auth/token/logout/             # Удаление токена
    
    GET recipes/                        # Получить список рецептов
    POST recipes/                       # Создание рецепта
    GET recipes/{id}/                   # Получение рецепта по id
    PATCH recipes/{id}                  # Изменение рецепта
    DELETE recipes/{id}/                # Удаление рецепта
    GET recipes/download_shopping_cart/ # Скачать список покупок
    POST recipes/{id}/shopping_cart     # Добавить рецепт в список покупок
    DELETE recipes/{id}/shopping_cart   # Удаление рецепта из списка покупок
    POST recipes/{id}/favorite/         # Добавить рецепт в избранное
    DELETE recipes/{id}/favorite/       # Удаление рецепта из избранного
    
    POST users/                         # Регистрация пользователя
    GET  users/                         # Получение списка пользователей
    GET users/{id}/                     # Получение пользователя по id
    GET users/me/                       # Получение текущего пользователя
    POST users/set_password/            # Изменение пароля текущего пользователя
    GET users/subscriptions/            # Мои подписки
    POST users/{id}/subscribe/          # Подписаться на пользователя
    DELETE users/{id}/subscribe/        # Отписаться от пользователя
    
    GET ingredients/                    # Получить список ингредиентов
    GET ingredients/{id}/               # Получить ингредиент по id
    
    GET tags/                           # Получить список ингредиентов
    GET tags/{id}/                      # Получение тега по id