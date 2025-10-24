FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app

# системные зависимости для Playwright
RUN apt-get update && apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libxss1 \
    libxcomposite1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpangocairo-1.0-0 \
    libgtk-3-0 \
    fonts-liberation \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# копируем код
COPY . .

# Установить браузеры Playwright
RUN python -m playwright install --with-deps

# удобная команда по умолчанию для запуска тестов (можно переопределить при docker run)
CMD ["pytest", "--alluredir=allure-results", "-q"]
