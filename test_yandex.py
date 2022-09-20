import time
from loguru import logger
from pages.yandex_search_page import YandexSearchPage
from pages.yandex_images_page import YandexImagesPage

logger.add("./logs/tests_yandex.log", format="{level} {time} {message}")


class TestYandex:
    def test_of_the_transition_to_the_tensor_page(self, browser):
        logger.info("Начало теста 'Поиск в Яндексе'")
        page = YandexSearchPage(browser)
        logger.debug("Открытие поисковой страницы Яндекса")
        page.go_to_url()
        logger.debug("Ввод текста в поле поиска")
        page.entering_text_in_input()
        logger.debug("Проверка появления результатов")
        page.is_present_results_after_pressing_enter()
        logger.debug("Клик по первой ссылке результатов")
        page.click_to_first_link()
        logger.debug("Проверка, что находимcя на сайте тензора")
        page.checking_the_transition_to_the_page("tensor.ru")
        logger.info("Конец теста 'Поиск в Яндексе'")

    def test_images(self, browser):
        logger.info("Начало теста 'Картинки на Яндексе'")
        page = YandexSearchPage(browser)
        logger.debug("Открытие поисковой страницы Яндекса")
        page.go_to_url()
        page_images = YandexImagesPage(browser, browser.url)
        logger.debug("Проверка наличия ссылки 'Картинки'")
        page_images.is_present_image_link()
        logger.debug("Клик по ссылке 'Картинки'")
        page_images.click_to_images_link()
        logger.debug("Проверка перехода на страницу www.yandex.ru/images")
        page_images.checking_the_transition_to_the_page("https://yandex.ru/images/")
        logger.debug("Открытие первой категории картинок")
        page_images.open_first_category_images()
        logger.debug("Проверка наличия в поисковой строке названия категории")
        page_images.check_name_of_category_in_input_value()
        logger.debug("Открытие первой картинки")
        page_images.open_first_image()
        time.sleep(0.3)
        logger.debug("Проверка, что картинка открылась")
        page_images.is_opened_image()
        logger.debug("Переход к следующей картинке")
        page_images.click_to_next_image()
        time.sleep(0.3)
        logger.debug("Проверка, что картинка изменилась")
        page_images.is_the_picture_changed()
        logger.debug("Переход к предыдущей картинке")
        page_images.click_to_prev_image()
        time.sleep(0.3)
        logger.debug("Проверка, что мы вернулись к исходной картинке")
        page_images.is_the_previous_picture()
        logger.info("Конец теста 'Картинки на Яндексе'")
