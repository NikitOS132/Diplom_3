import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from curl import *
import allure
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage

class TestMainPage:
    @allure.title('Переход по клику на «Ленту заказов»')
    def test_click_order_list(self, driver):
        page = MainPage(driver)
        page.wait_visibility_of_order_list_button()
        page.click_on_order_list_button()
        WebDriverWait(driver, 6).until(EC.url_to_be(feed_order_site))
        assert driver.current_url == feed_order_site

    @allure.title('Переход по клику на «Конструктор»')
    def test_click_constructor(self, driver):
        page = MainPage(driver)
        page.wait_visibility_of_order_list_button()
        page.click_on_order_list_button()
        WebDriverWait(driver, 6).until(EC.url_to_be(feed_order_site))
        page = OrderFeedPage(driver)
        page.wait_visibility_of_constructor_button()
        page.click_on_constructor_button()
        WebDriverWait(driver, 6).until(EC.url_to_be(main_site))
        assert driver.current_url == main_site

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_display_ingred_info(self, driver):
        page = MainPage(driver)
        page.wait_visibility_of_krator_bun()
        page.click_on_krator_bun()
        page.wait_visibility_of_krator_bun_ingred_info()
        assert page.check_displaying_of_krator_bun_ingred_info()

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_ingred_info(self, driver):
        page = MainPage(driver)
        page.wait_visibility_of_krator_bun()
        page.click_on_krator_bun()
        page.wait_visibility_of_krator_bun_ingred_info()
        page.wait_visibility_of_krator_bun_ingred_info_exit_button()
        page.click_on_krator_bun_ingred_info_exit_button()
        page.wait_until_ingred_info_hidden()
        assert not page.check_displaying_of_krator_bun_ingred_info()

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается.')
    def test_check_ingred_meter(self, driver):
        page = MainPage(driver)
        page.wait_visibility_of_krator_bun()
        page.wait_visibility_of_order_basket()
        initial_count = page.get_current_ingredient_count()
        page.drag_and_drop_element(
        MainPageLocators.krator_bun,
        MainPageLocators.burger_basket
    )
        updated_count = page.wait_for_counter_update(MainPageLocators.ingred_meter, timeout=10)
        allure.attach(str(updated_count), name="Updated count", attachment_type=allure.attachment_type.TEXT)
        assert isinstance(updated_count, int)