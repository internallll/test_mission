# Базовый образ с Python
FROM python:3.12-slim

# Устанавливаем uv
RUN pip install --no-cache-dir uv

# Задаём рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей (pyproject.toml и uv.lock, если есть)
COPY pyproject.toml uv.lock* ./
#Устанавливаем нужные библиотеки для Постгры
RUN apt-get update && apt-get install -y libpq-dev gcc python3-dev
# Устанавливаем зависимости
RUN uv sync

# Копируем всё приложение
COPY . .

# Открываем порт для Django
EXPOSE 8000

# Запуск Django-сервера разработки
CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
