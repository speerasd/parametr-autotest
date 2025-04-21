import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, fr, es, etc.")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print(f"\nЗапускаем браузер с языком: {user_language}")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nЗакрываем браузер")
    browser.quit()