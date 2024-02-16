import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def chrome_browser_instance(request):
    '''
    Provide a selenium webdriver instance.
    '''
    options = Options()
    options.headless= False  # it runs in window rather than background
    browser= webdriver.Chrome(options=options)
    yield browser
    browser.close()