from .base_page import BasePage


class YandexImagesPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.first_image_url = None
        self.current_image_url = None
        self.category_name = None

    def is_present_image_link(self):
        assert self.browser.is_element_present_by_css(".service_name_images .link"), \
            "Сслыка на страницу картинки отсутстует"

    def click_to_images_link(self):
        images_link = self.browser.find_by_css(".service_name_images .link")
        images_link.click()

    def open_first_category_images(self):
        first_category = self.browser.find_by_css(".PopularRequestList-Preview").first
        self.category_name = self.browser.find_by_css(".PopularRequestList-SearchText").first.value
        first_category.click()

    def check_name_of_category_in_input_value(self):
        self.browser.windows.current = self.browser.windows[1]
        input_search = self.browser.find_by_css(".input__box .input__control")
        assert input_search.value == self.category_name, "Отображается неверное название категории"

    def open_first_image(self):
        first_image = self.browser.find_by_css(".serp-item__link").first
        first_image.click()

    def is_opened_image(self):
        self.first_image_url = self.browser.find_by_css(".MMImage-Origin")["src"]
        assert self.browser.is_element_present_by_css(".MMImage-Preview"), "Картинка не открылась"

    def click_to_next_image(self):
        button_next = self.browser.find_by_css(".CircleButton_type_next")
        button_next.click()
        self.current_image_url = self.browser.find_by_css(".MMImage-Origin")["src"]

    def is_the_picture_changed(self):
        assert self.first_image_url != self.current_image_url, "Картинка не сменилась"

    def click_to_prev_image(self):
        button_prev = self.browser.find_by_css(".CircleButton_type_prev")
        button_prev.click()
        self.current_image_url = self.browser.find_by_css(".MMImage-Origin")["src"]

    def is_the_previous_picture(self):
        assert self.first_image_url == self.current_image_url, "Первая картинка не"

