import pytest
from selene import browser


@pytest.fixture
def browser_size():
    browser.config.window_height = 600
    browser.config.window_width = 600

    yield
    browser.quit()

