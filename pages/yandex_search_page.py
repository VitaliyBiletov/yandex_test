from loguru import logger
from selenium.webdriver import Keys
from .base_page import BasePage


class YandexSearchPage(BasePage):
    """Класс описывает методы работы со поисковой страницей (yandex.ry/search)"""

    url = "https://yandex.ru/search/"

    def __init__(self, browser):
        """Конструктор класса"""
        super().__init__(browser, self.url)

    def should_be_input_field(self):
        """Проверяет наличие поля поиска"""
        assert self.browser.is_element_present_by_css("input.input__control"), \
            logger.error("Отстутствует поле поиска")

    def entering_text_in_input(self):
        """
        Получает поле поиска
        Вводит в него слово 'Тензор'
        Проверяет наличие таблицы с подсказками
        Нажимает Enter
        """
        search_input = self.browser.find_by_css("input.input__control")
        search_input.fill("Тензор")
        self.is_present_suggest()
        search_input.type(Keys.ENTER)

    def is_present_suggest(self):
        """Проверяет наличие таблицы с подсказками"""
        assert self.browser.is_element_present_by_css(".mini-suggest__popup"), \
            logger.error("Отстутствует таблица с подсказками")

    def is_present_results_after_pressing_enter(self):
        """Проверяет наличие результатов поиска"""
        assert self.browser.is_element_present_by_css("ul.serp-list"), \
            logger.error("Отстутсвует таблица с результатами поиска")

    def click_to_first_link(self):
        """Получает первую ссылку и кликает по ней"""
        first_link = self.browser.find_by_css("[data-cid='0'] a.Link")
        first_link.click()

