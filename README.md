<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Тестирование автоматизации пользовательского интерфейса с помощью Playwright и Pytest</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1, h2, h3 {
            color: #333;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: monospace;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        a {
            color: #007BFF;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Тестирование автоматизации пользовательского интерфейса с помощью Playwright и Pytest</h1>
    <p>Этот проект демонстрирует автоматизацию тестирования пользовательского интерфейса с использованием Playwright и Pytest. Он включает тесты для навигации по главной странице веб-сайта <a href="https://effective-mobile.ru">https://effective-mobile.ru</a>.</p>

    <h2>Предварительные требования</h2>
    <ul>
        <li>Python 3.10</li>
        <li>Docker (опционально, для запуска тестов в контейнере)</li>
        <li>Allure (для генерации отчетов)</li>
    </ul>

    <h2>Установка</h2>
    <ol>
        <li>Клонируйте репозиторий:
            <pre><code>git clone https://github.com/Telipenko/effective-mobile</code></pre>
        </li>
        <li>Установите зависимости:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Установите браузеры для Playwright:
            <pre><code>playwright install</code></pre>
        </li>
    </ol>

    <h2>Запуск тестов локально</h2>
    <p>Запустите тесты с помощью Pytest:</p>
    <pre><code>pytest --alluredir=allure-results</code></pre>
    <p>Результаты тестов будут сохранены в папке <code>allure-results</code>.</p>
    <p>Для генерации отчета Allure выполните:</p>
    <pre><code>allure serve allure-results</code></pre>
    <p>Отчет будет автоматически открыт в вашем браузере.</p>

    <h2>Запуск тестов в Docker-контейнере</h2>
    <p>Убедитесь, что Docker установлен на вашем компьютере. Если нет, скачайте и установите его с <a href="https://www.docker.com/">официального сайта</a>.</p>
    <ol>
        <li>Соберите Docker-образ:
            <pre><code>docker build -t my-pytest-app .</code></pre>
        </li>
        <li>Запустите контейнер с тестами:
            <pre><code>docker run my-pytest-app</code></pre>
        </li>
        <li>Скопируйте результаты тестов из контейнера на ваш локальный компьютер:
            <pre><code>docker cp &lt;container_id&gt;:/app/allure-results ./allure-results</code></pre>
            <p>Замените <code>&lt;container_id&gt;</code> на ID вашего контейнера (можно узнать с помощью <code>docker ps -a</code>).</p>
        </li>
        <li>Сгенерируйте отчет Allure:
            <pre><code>allure serve allure-results</code></pre>
        </li>
    </ol>

    <h2>Генерация отчетов с помощью Allure</h2>
    <h3>Установка Allure</h3>
    <ul>
        <li><strong>macOS</strong> (с помощью Homebrew):
            <pre><code>brew install allure</code></pre>
        </li>
        <li><strong>Windows</strong> (с помощью Scoop):
            <pre><code>scoop install allure</code></pre>
        </li>
        <li><strong>Linux</strong> (с помощью Snap):
            <pre><code>sudo snap install allure</code></pre>
        </li>
    </ul>

    <h3>Генерация отчета</h3>
    <p>Убедитесь, что у вас есть папка <code>allure-results</code> с результатами тестов.</p>
    <p>Сгенерируйте отчет:</p>
    <pre><code>allure serve allure-results</code></pre>
    <p>Отчет будет автоматически открыт в вашем браузере.</p>

    <h2>Анализ отчета</h2>
    <p>Отчет Allure предоставляет:</p>
    <ul>
        <li><strong>Графики:</strong> Общая статистика по успешным, проваленным и пропущенным тестам.</li>
        <li><strong>Детали тестов:</strong> Шаги выполнения каждого теста и ошибки, если они возникли.</li>
        <li><strong>Логи и скриншоты:</strong> Если тест завершился неудачно, вы можете увидеть логи и скриншоты (если они были сделаны).</li>
    </ul>

    <h2>Структура проекта</h2>
    <ul>
        <li><code>Dockerfile</code>: Файл для создания Docker-образа.</li>
        <li><code>requirements.txt</code>: Список зависимостей Python.</li>
        <li><code>test_MOBILe.py</code>: Файл с тестами для навигации по главной странице.</li>
        <li><code>allure-results</code>: Папка с результатами тестов (создается после запуска тестов).</li>
    </ul>
</body>
</html>
