# Используем базовый образ Python
FROM python:3.8

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости проекта (requirements.txt) в контейнер
COPY requirements.txt requirements.txt

# Устанавливаем зависимости приложения
RUN pip install -r requirements.txt

# Копируем все файлы текущего каталога в /app в контейнере
COPY . .

# Копируем файл .env внутрь контейнера
COPY .env

# Открываем порт, на котором будет работать приложение
EXPOSE 8000

# Команда для запуска приложения через uvicorn
CMD ["python", "app.py"]
