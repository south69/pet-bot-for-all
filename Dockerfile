# Базовый образ
FROM python:3.11-slim

# Установка необходимых системных пакетов
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    libffi-dev \
    libssl-dev \
    curl \
    build-essential \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Рабочая директория
WORKDIR /app

# Копируем файлы проекта
COPY . .

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Запуск
CMD ["python", "main.py"]