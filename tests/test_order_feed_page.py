import pytest
import allure
from pages.login_page import AccountPage
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.order_feed_page import OrderFeedPage

class TestOrderFeedPage:
    @allure.title('При создании нового заказа счётчик «Выполнено за всё время» увеличивается')
    def test_check_all_time_meter(self, driver, test_credentials):
        page = MainPage(driver)
        page.wait_visibility_of_login_button()
        page.click_on_login_button()
        email = test_credentials["email"]
        password = test_credentials["password"]
        page = AccountPage(driver)
        page.data_entry_form(email, password)
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
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_visibility_of_all_time_meter()
        initial_value = order_feed_page.get_current_at_all_time_value()
        allure.attach(str(initial_value), name="Initial count")
        order_feed_page.click_on_constructor_button()
        page.click_on_make_order()
        page.wait_until_invisible_wall_hidden()
        page.wait_visibility_of_ready_order()
        page.wait_visibility_of_ready_order_info_exit_button()
        page.click_on_ready_order_info_exit_button()
        page.click_on_order_list_button()
        order_feed_page.wait_visibility_of_all_time_meter()
        new_value = order_feed_page.wait_for_at_all_time_update(OrderFeedPageLocators.at_all_time, timeout=10)
        allure.attach(str(new_value), name="Updated count")
        assert new_value > initial_value

    @allure.title('При создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_check_today_meter(self, driver, test_credentials):
        page = MainPage(driver)
        page.wait_visibility_of_login_button()
        page.click_on_login_button()
        email = test_credentials["email"]
        password = test_credentials["password"]
        page = AccountPage(driver)
        page.data_entry_form(email, password)
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
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_visibility_of_today_meter()
        initial_value = order_feed_page.get_current_at_today_value()
        allure.attach(str(initial_value), name="Initial count")
        order_feed_page.click_on_constructor_button()
        page.click_on_make_order()
        page.wait_until_invisible_wall_hidden()
        page.wait_visibility_of_ready_order()
        page.wait_visibility_of_ready_order_info_exit_button()
        page.click_on_ready_order_info_exit_button()
        page.click_on_order_list_button()
        order_feed_page.wait_visibility_of_today_meter()
        new_value = order_feed_page.wait_for_at_today_update(OrderFeedPageLocators.at_today, timeout=10)
        allure.attach(str(new_value), name="Updated count")
        assert new_value > initial_value

    @allure.title('После оформления заказа его номер появляется в разделе «В работе»')
    def test_check_order_in_work(self, driver, test_credentials):
        page = MainPage(driver)
        page.wait_visibility_of_login_button()
        page.click_on_login_button()
        email = test_credentials["email"]
        password = test_credentials["password"]
        page = AccountPage(driver)
        page.data_entry_form(email, password)
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