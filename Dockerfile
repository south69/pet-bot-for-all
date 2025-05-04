# Базовый образ с Python
FROM python:3.11-slim

# Установка зависимостей для pip (wheel, и т.п.)
RUN apt-get update && apt-get install -y gcc libpq-dev

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Указываем команду запуска
CMD ["python", "main.py"]