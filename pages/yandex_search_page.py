from selenium.webdriver import Keys
from .base_page import BasePage


class YandexSearchPage(BasePage):
    url = "https://yandex.ru/search/"

    def __init__(self, browser):
        super().__init__(browser, self.url)

    def text_in_input(self):
        search_input = self.browser.find_by_css("input.input__control")
        search_input.fill("Тензор")
        self.is_present_suggest()
        search_input.type(Keys.ENTER)

    def is_present_suggest(self):
        assert self.browser.is_element_present_by_css(".mini-suggest__popup"), "Отстутствует таблица с подсказками"

    def is_present_results_after_pressing_enter(self):
        assert self.browser.is_element_present_by_css("ul.serp-list"), "Отстутсвует таблица с результатами поиска"

    def the_first_link_directs_to_tensor_ru(self):
        first_link = self.browser.find_by_css("[data-cid='0'] a.Link")
        first_link.click()

