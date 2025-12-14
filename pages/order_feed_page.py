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