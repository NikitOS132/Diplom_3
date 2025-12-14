import pytest
import allure
from pages.login_page import AccountPage
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage

class TestOrderFeedPage:
    @allure.title('При создании нового заказа счётчик «Выполнено за всё время» увеличивается')
    def test_check_display_all_time_meter(self, driver):
        page = MainPage(driver)
        page.wait_visibility_of_login_button()
        page.click_on_login_button()
        page = AccountPage(driver)
        page.data_entry_form()
        page = MainPage(driver)
        page.wait_visibility_of_krator_bun()
        page.wait_visibility_of_order_basket()
        page.wait_visibility_of_krator_bun_clickable()
        page.wait_visibility_of_burger_basket_clickable()
        page.drag_and_drop_element(
        MainPageLocators.krator_bun,
        MainPageLocators.burger_basket
    )
        page.click_on_make_order()
        page.wait_until_invisible_wall_hidden()
        page.wait_visibility_of_ready_order()
        page.wait_visibility_of_ready_order_info_exit_button()
        page.click_on_ready_order_info_exit_button()
        page.click_on_order_list_button()
        page = OrderFeedPage(driver)
        page.wait_visibility_of_all_time_meter()
        assert page.check_displaying_of_all_time_meter()

    @allure.title('При создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_check_display_today_meter(self, driver):
        page = MainPage(driver)
        page.wait_visibility_of_login_button()
        page.click_on_login_button()
        page = AccountPage(driver)
        page.data_entry_form()
        page = MainPage(driver)
        page.wait_visibility_of_krator_bun()
        page.wait_visibility_of_order_basket()
        page.wait_visibility_of_krator_bun_clickable()
        page.wait_visibility_of_burger_basket_clickable()
        page.drag_and_drop_element(
        MainPageLocators.krator_bun,
        MainPageLocators.burger_basket
    )
        page.click_on_make_order()
        page.wait_until_invisible_wall_hidden()
        page.wait_visibility_of_ready_order()
        page.wait_visibility_of_ready_order_info_exit_button()
        page.click_on_ready_order_info_exit_button()
        page.click_on_order_list_button()
        page = OrderFeedPage(driver)
        page.wait_visibility_of_today_meter()
        assert page.check_displaying_of_today_meter()

    @allure.title('После оформления заказа его номер появляется в разделе «В работе»')
    def test_check_order_in_work(self, driver):
        page = MainPage(driver)
        page.wait_visibility_of_login_button()
        page.click_on_login_button()
        page = AccountPage(driver)
        page.data_entry_form()
        page = MainPage(driver)
        page.wait_visibility_of_krator_bun()
        page.wait_visibility_of_order_basket()
        page.wait_visibility_of_krator_bun_clickable()
        page.wait_visibility_of_burger_basket_clickable()
        page.drag_and_drop_element(
        MainPageLocators.krator_bun,
        MainPageLocators.burger_basket
    )
        page.click_on_make_order()
        page.wait_until_invisible_wall_hidden()
        page.wait_visibility_of_ready_order()
        page.wait_visibility_of_ready_order_info_exit_button()
        page.click_on_ready_order_info_exit_button()
        page.click_on_order_list_button()
        page = OrderFeedPage(driver)
        page.wait_visibility_of_order_in_work()
        assert page.check_displaying_of_order_in_work()