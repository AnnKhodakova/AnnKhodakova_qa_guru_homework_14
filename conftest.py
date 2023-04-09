import pytest
from selene.support.shared import browser


@pytest.fixture
def desktop_window_open():
    browser.config.window_width = 1366
    browser.config.window_height = 768
    browser.open('https://github.com/')


@pytest.fixture
def mobile_window_open():
    browser.config.window_width = 390
    browser.config.window_height = 844
    browser.open('https://github.com/')


@pytest.fixture(params=['desktop', 'mobile'])
def browser_open(request):
    if request.param == 'desktop':
        browser.config.window_width = 1366
        browser.config.window_height = 768
        browser.open('https://github.com/')
    else:
        browser.config.window_width = 390
        browser.config.window_height = 844
        browser.open('https://github.com/')
