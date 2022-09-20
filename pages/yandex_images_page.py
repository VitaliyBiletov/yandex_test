from loguru import logger
from .base_page import BasePage


class YandexImagesPage(BasePage):
    """Класс описывает методы работы со страницей картинок (yandex.ry/images)"""
    def __init__(self, browser, url):
        """
        Конструктор класса
        first_image_url - атрибут для хранения url первой картинки
        current_image_url - атрибут для хранения url текущей открытой картинки
        category_name - атрибут для хранения названия категории
        """
        super().__init__(browser, url)
        self.first_image_url = None
        self.current_image_url = None
        self.category_name = None

    def is_present_image_link(self):
        """Проверяет наличие ссылки на страницу с картинками"""
        assert self.browser.is_element_present_by_css(".service_name_images .link"), \
            logger.error("Сслыка на страницу картинки отсутстует")

    def click_to_images_link(self):
        """Получает элемент ссылки и кликает по нему"""
        images_link = self.browser.find_by_css(".service_name_images .link")
        images_link.click()

    def open_first_category_images(self):
        """
        Получает первый элемент среди категорий картинок
        Получает имя категории и заисывает его в атрибут category_name
        Кликает по первой категории
        """
        first_category = self.browser.find_by_css(".PopularRequestList-Preview").first
        self.category_name = self.browser.find_by_css(".PopularRequestList-SearchText").first.value
        first_category.click()

    def check_name_of_category_in_input_value(self):
        """
        Проверяет наличие названия категории в поисковой строке
        Проверяет что именно та категоря которую мы выбрали отображается в поисковой строке
        """
        self.browser.windows.current = self.browser.windows[1]
        input_search = self.browser.find_by_css(".input__box .input__control")
        assert input_search.value == self.category_name, \
            logger.error("Отображается неверное название категории")

    def open_first_image(self):
        """Получает первую картинку и кликает по ней"""
        first_image = self.browser.find_by_css(".serp-item__link").first
        first_image.click()

    def is_opened_image(self):
        """
        Проверяет открытие картинки
        Запоминает url прервой картинки в атрибуте first_image_url
        """
        self.first_image_url = self.browser.find_by_css(".MMImage-Origin")["src"]
        assert self.browser.is_element_present_by_css(".MMImage-Preview"), \
            logger.error("Ошибка открытия картинки")

    def click_to_next_image(self):
        """
        Получает элемент для переход к следующей картинке
        Кликает по нему
        Запоминает url картинки в атрибуте current_image_url
        """
        button_next = self.browser.find_by_css(".CircleButton_type_next")
        button_next.click()
        self.current_image_url = self.browser.find_by_css(".MMImage-Origin")["src"]

    def is_the_picture_changed(self):
        """Проверяет что картинка сменилась"""
        assert self.first_image_url != self.current_image_url, \
            logger.error("Картинка не сменилась")

    def click_to_prev_image(self):
        """
        Получает элемент для переход к предыдущей картинке
        Кликает по нему
        """
        button_prev = self.browser.find_by_css(".CircleButton_type_prev")
        button_prev.click()
        self.current_image_url = self.browser.find_by_css(".MMImage-Origin")["src"]

    def is_the_previous_picture(self):
        """Сраванивает url первой картинки и текущей"""
        assert self.first_image_url == self.current_image_url, \
            logger.error("Первая картинка не совпадает с исходной")

