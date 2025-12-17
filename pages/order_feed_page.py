import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators

class OrderFeedPage(BasePage):
    @allure.step('Подождать прогрузки кнопки "Конструктор" в хедере')
    def wait_visibility_of_constructor_button(self):
        self.wait_visibility_of_element(OrderFeedPageLocators.constructor)

    @allure.step('Кликнуть по кнопке "Конструктор" в хедере')
    def click_on_constructor_button(self):
        self.click_on_element(OrderFeedPageLocators.constructor)

    @allure.step('Проверить отображение счетчика "Выполнено за все время"')
    def check_displaying_of_all_time_meter(self):
        return self.check_displaying_of_element(OrderFeedPageLocators.at_all_time)

    @allure.step('Проверить отображение счетчика "Выполнено за сегодня"')
    def check_displaying_of_today_meter(self):
        return self.check_displaying_of_element(OrderFeedPageLocators.at_today)

    @allure.step('Подождать прогрузки отображения заказа в работе')
    def wait_visibility_of_order_in_work(self):
        self.wait_visibility_of_element(OrderFeedPageLocators.order_in_work)

    @allure.step('Проверить отображение заказа в работе')
    def check_displaying_of_order_in_work(self):
        return self.check_displaying_of_element(OrderFeedPageLocators.order_in_work)

    @allure.step('Подождать прогрузки отображения счетчика "Выполнено за все время"')
    def wait_visibility_of_all_time_meter(self):
        self.wait_visibility_of_element(OrderFeedPageLocators.order_in_work)

    @allure.step('Подождать прогрузки отображения счетчика "Выполнено за сегодня"')
    def wait_visibility_of_today_meter(self):
        self.wait_visibility_of_element(OrderFeedPageLocators.at_today)

    @allure.step('Открыть главную страницу')
    def open_constructor_feed(self, main_url: str):
        self.wait_visibility_of_constructor_button()
        self.click_on_constructor_button()
        self.wait_url_to_be(main_url)

    @allure.step('Получение текущего значения счётчика "За все время" в ленте заказов')
    def get_current_at_all_time_value(self):
        return self.get_at_all_time_value(OrderFeedPageLocators.at_all_time)
    
    @allure.step('Получение текущего значения счётчика "За сегодня" в ленте заказов')
    def get_current_at_today_value(self):
        return self.get_at_today_value(OrderFeedPageLocators.at_today)

    @allure.step('Ожидание обновления счётчика "За все время"')
    def wait_for_at_all_time_update(self, locator, timeout=30):
        initial_value = self.get_at_all_time_value(locator)
        current_value = self.get_at_all_time_value(locator)
        return current_value
    
    @allure.step('Ожидание обновления счётчика "За сегодня"')
    def wait_for_at_today_update(self, locator, timeout=30):
        initial_value = self.get_at_today_value(locator)
        current_value = self.get_at_today_value(locator)
        return current_value