# Тестирование автоматизации пользовательского интерфейса с помощью Playwright и Pytest

Этот проект демонстрирует автоматизацию тестирования пользовательского интерфейса с использованием Playwright и Pytest. Он включает тесты для навигации по главной странице веб-сайта https://effective-mobile.ru.

## Предварительные требования

- Python 3.10
- Docker (опционально, для запуска тестов в контейнере)
- Allure (для генерации отчетов)

## Установка

  Клонируйте репозиторий:
  git clone https://github.com/Telipenko/effective-mobile

Установите зависимости:
pip install -r requirements.txt

Установите браузеры для Playwright:
playwright install

Запуск тестов локально
Запустите тесты с помощью Pytest:

pytest --alluredir=allure-results
Результаты тестов будут сохранены в папке allure-results.

Для генерации отчета Allure выполните:

allure serve allure-results
Отчет будет автоматически открыт в вашем браузере.

Запуск тестов в Docker-контейнере
Убедитесь, что Docker установлен на вашем компьютере. Если нет, скачайте и установите его с официального сайта.

Соберите Docker-образ:
docker build -t my-pytest-app .

Запустите контейнер с тестами:
docker run my-pytest-app

Скопируйте результаты тестов из контейнера на ваш локальный компьютер:
docker cp <container_id>:/app/allure-results ./allure-results

Замените <container_id> на ID вашего контейнера (можно узнать с помощью docker ps -a).

Сгенерируйте отчет Allure:
allure serve allure-results

Генерация отчетов с помощью Allure
Установка Allure

macOS (с помощью Homebrew):
brew install allure

Windows (с помощью Scoop):
scoop install allure

Linux (с помощью Snap):
sudo snap install allure

Генерация отчета
Убедитесь, что у вас есть папка allure-results с результатами тестов.

Сгенерируйте отчет:

allure serve allure-results
Отчет будет автоматически открыт в вашем браузере.

Анализ отчета
Отчет Allure предоставляет:

Графики: Общая статистика по успешным, проваленным и пропущенным тестам.

Детали тестов: Шаги выполнения каждого теста и ошибки, если они возникли.

Логи и скриншоты: Если тест завершился неудачно, вы можете увидеть логи и скриншоты (если они были сделаны).

Структура проекта
Dockerfile: Файл для создания Docker-образа.

requirements.txt: Список зависимостей Python.

test_MOBILe.py: Файл с тестами для навигации по главной странице.

allure-results: Папка с результатами тестов (создается после запуска тестов).

