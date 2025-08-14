# **Тестовое задание: Веб-сервис для управления движением денежных средств (ДДС)**
## Требования
Для работы с проектом вам понадобятся:

- Python 3.11
- Docker и Docker Compose v2
- [uv](https://docs.astral.sh/uv/#project-management) (для управления зависимостями)

  ## Установка и настройка

### 1. Перед началом работы: 
- Создайте виртуальное окружение
- Установите зависимости из `pyproject.toml`
- Активируйте его с помощью `uv`
```bash
  uv sync
  source .venv/bin/activate
```

### 2. Настройка переменных окружения
Создайте файл `.env` в корневой директории проекта. Скопируйте содержимое из `.env.example`:
```bash
  cp .env.example .env
```

### 3. Миграции
```bash
  python manage.py migrate
```
### 4. Фикстуры
Для нормального работы приложения следует добавить первоначальные данные
```bash
  python manage.py loaddata db.json
```
### 4. Линтер
```bash
  ruff format && ruff check --fix
```
### 5. Создание суперпользователя
```bash
    python manage.py createsuperuser
```

## Запуск проекта через Makefile

Проект можно запускать с помощью команд из `Makefile`. Вот описание основных команд:

### Быстрый старт
- **Запуск всех сервисов в контейнере (Django, RabbitMQ, Celery, PostgreSQL)**
```bash
  sudo make start
```
- **Остановка контейнеров**
```bash
  sudo make stop
```

---

<details>
<summary>Полный список команд</summary>

### 1. Запуск сервисов
- **Запуск всех сервисов (Django, RabbitMQ, Celery, PostgreSQL):**
```bash
  sudo make start
```
- **Запуск всех сервисов с динамическим редактирование:**
```bash
  sudo make watch
```

### 2. Остановка сервисов
- **Остановка контейнеров:**
```bash
  sudo make stop
```
- **Остановка контейнеров с их удалением:**
```bash
  sudo make down
```
- **Остановка контейнеров с удалением volumes (полная очистка):**
```bash
  sudo make down-total## Запуск проекта через Makefile

Проект можно запускать с помощью команд из `Makefile`. Вот описание основных команд:

### Быстрый старт
- **Запуск всех сервисов в контейнере (Django, RabbitMQ, Celery, PostgreSQL)**
```bash
  sudo make start
```
- **Остановка контейнеров**
```bash
  sudo make stop
```

---

<details>
<summary>Полный список команд</summary>

### 1. Запуск сервисов
- **Запуск всех сервисов (Django, RabbitMQ, Celery, PostgreSQL):**
```bash
  sudo make start
```
- **Запуск всех сервисов с динамическим редактирование:**
```bash
  sudo make watch
```

### 2. Остановка сервисов
- **Остановка контейнеров:**
```bash
  sudo make stop
```
- **Остановка контейнеров с их удалением:**
```bash
  sudo make down
```
```

### 3. Просмотр логов
- **Логи Django приложения:**
```bash
  sudo make webserver-logs
```
- **Логи RabbitMQ приложения:**
```bash
  sudo make rabbitmq-logs
```
- **Логи PostgreSQL приложения:**
```bash
  sudo make postgres-logs
```
</details>

---

