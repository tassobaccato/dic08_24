from selenium.webdriver.firefox.options import Options
import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    options = Options()
    options.add_argument('--headless')  # активировать не визуальный режим
    browser = webdriver.Firefox(options=options)  # Создаём объект браузера Firefox()
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.quit()
