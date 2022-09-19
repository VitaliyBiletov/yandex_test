from splinter import Browser
import pytest


@pytest.fixture(scope="function")
def browser():
    browser = Browser("chrome")
    browser.wait_time = 5
    yield browser
    browser.quit()

