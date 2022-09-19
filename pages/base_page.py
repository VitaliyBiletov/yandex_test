from splinter import Browser
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def go_to_url(self):
        self.browser.visit(self.url)

    def checking_the_transition_to_the_page(self, target_url):
        self.browser.windows.current = self.browser.windows[1]
        url = self.browser.url
        assert target_url in url, f"Не выполнен переход по адресу: {target_url}"
