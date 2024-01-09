# ВЕСЬ FASTAPI ЗА 30 МИН
https://www.youtube.com/watch?v=1ZlOEoCWkQU

# Зависимости
## Чтобы получить список пакетов в проекте выполняем команду
pip freeze

## Для записи вывода в requirements.txt дополняем следующим образом:
pip freeze > requirements.txt

# Установка пакетов
pip install -r requirements.txt

# Работа с GIT
git init
git add *
git commit -m "first commit"
git remote add origin git@github.com:vxv-cod/backend_FastApi_30_minut.git
git push -u origin maste

# Установка FastApi
pip install "fastapi[all]" alembic

# Миграции
## Инициализируем alembic
`alembic init migrations`
## Корректируем migrations/env.py
### Импортируем в (migrations/env.py) модели вместе с Base (Base = declarative_base())
`from models.user import *`
### и прописываем метаданные в переменную target_metadata
`target_metadata = Base.metadata`
## Создаем ревизию миграции 
`alembic revision --autogenerate -m "Создаем таблицы"`
## Обновляем базу данных по номеру последней миграции
`alembic upgrade e07bd21282bb`