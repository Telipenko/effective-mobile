# TESTMOBILe.py

# Импорт библиотек
import pytest
from playwright.sync_api import sync_playwright
import allure

# Фикстуры для pytest
def pytest_addoption(parser):
    parser.addoption("--base-url", action="store", default="https://effective-mobile.ru", help="Base URL for tests")

@pytest.fixture(scope="session")
def playwright_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])  
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(playwright_browser):
    context = playwright_browser.new_context()
    page = context.new_page()
    yield page
    page.close()

# Базовый класс для страниц
class BasePage:
    def __init__(self, page):
        self.page = page

    def go_to(self, url):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()

# Класс для главной страницы
class MainPage(BasePage):
    ABOUT_US = "a[href='#about']"  # Локатор для "О нас"
    SERVICES = "a[href='#moreinfo']"  # Локатор для "Услуги"
    PROJECTS = "a[href='#cases']"  # Локатор для "Проекты"
    REVIEWS = "a[href='#Reviews']"  # Локатор для "Отзывы"
    CONTACTS = "a[href='#contacts']"  # Локатор для "Контакты"

    def click_about_us(self):
        self.page.wait_for_selector(self.ABOUT_US, state="visible", timeout=120000)  # Увеличено до 120 секунд
        self.page.click(self.ABOUT_US)

    def click_services(self):
        self.page.wait_for_selector(self.SERVICES, state="visible", timeout=120000)  # Увеличено до 120 секунд
        self.page.click(self.SERVICES)

    def click_projects(self):
        self.page.wait_for_selector(self.PROJECTS, state="visible", timeout=120000)  # Увеличено до 120 секунд
        self.page.click(self.PROJECTS)

    def click_reviews(self):
        self.page.wait_for_selector(self.REVIEWS, state="visible", timeout=120000)  # Увеличено до 120 секунд
        self.page.click(self.REVIEWS)

    def click_contacts(self):
        self.page.wait_for_selector(self.CONTACTS, state="visible", timeout=120000)  # Увеличено до 120 секунд
        self.page.click(self.CONTACTS)

# Тесты для главной страницы
@allure.feature("Main Page Navigation")
@pytest.mark.parametrize("link, expected_url", [
    ("ABOUT_US", "https://effective-mobile.ru/#about"),
    ("SERVICES", "https://effective-mobile.ru/#moreinfo"),
    ("PROJECTS", "https://effective-mobile.ru/#cases"),
    ("REVIEWS", "https://effective-mobile.ru/#Reviews"),
    ("CONTACTS", "https://effective-mobile.ru/#contacts"),
])
def test_navigation(page, link, expected_url):
    page.on("console", lambda msg: print(msg.text))  # Логирование консольных ошибок
    main_page = MainPage(page)
    main_page.go_to("https://effective-mobile.ru")

    # Клик по элементу и проверка URL
    getattr(main_page, f"click_{link.lower()}")()
    page.wait_for_url(expected_url, timeout=120000, wait_until="networkidle")  # Ожидание завершения сетевых запросов
    assert page.url == expected_url, f"Expected {expected_url}, got {page.url}"

    print(f"Current URL: {page.url}")

# Точка входа для запуска тестов
if __name__ == "__main__":
    pytest.main(["--alluredir=allure-results"])

