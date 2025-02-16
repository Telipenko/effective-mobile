# Используем официальный образ Python 3.10
FROM python:3.10-slim

# Устанавливаем системные зависимости, которые могут понадобиться Playwright
RUN apt-get update && apt-get install -y \
    wget \
    libnss3 \
    libatk1.0-0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxfixes3 \
    libxi6 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libasound2 \
    libatk-bridge2.0-0\            
    libcups2\                                  
    libdbus-1-3\                                 
    libxkbcommon0\                               
    libatspi2.0-0\                               
    libcairo2\                  
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем все файлы из текущей директории в контейнер
COPY . /app

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем только Chromium (игнорируем Firefox)
RUN python -m playwright install chromium

# Запускаем тесты с помощью pytest
CMD ["pytest", "--alluredir=allure-results"]