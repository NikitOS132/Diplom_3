import allure
from pages.base_page import BasePage
from seletools.actions import drag_and_drop
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    @allure.step('Подождать прогрузки "Краторной булки N-200i" на основной странице')
    def wait_visibility_of_krator_bun(self):
        self.wait_visibility_of_element(MainPageLocators.krator_bun)

    @allure.step('Кликнуть по "Краторной булке N-200i" на основной странице')
    def click_on_krator_bun(self):
        self.click_on_element(MainPageLocators.krator_bun)

    @allure.step('Подождать кликабельности "Краторной булки N-200i" на основной странице')
    def wait_visibility_of_krator_bun_clickable(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.krator_bun)

    @allure.step('Подождать кликабельности корзины заказа на основной странице')
    def wait_visibility_of_burger_basket_clickable(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.burger_basket)

    @allure.step('Подождать прогрузки "Краторной булки N-200i" на основной странице')
    def wait_visibility_of_krator_bun(self):
        self.wait_visibility_of_element(MainPageLocators.krator_bun)

    @allure.step('Подождать отображения информации об ингредиенте "Краторная булка N-200i" на основной странице')
    def wait_visibility_of_krator_bun_ingred_info(self):
        return self.wait_visibility_of_element(MainPageLocators.ingred_detail)

    @allure.step('Проверить отображение информации об ингредиенте "Краторная булка N-200i" на основной странице')
    def check_displaying_of_krator_bun_ingred_info(self):
        return self.check_displaying_of_element(MainPageLocators.ingred_detail)

    @allure.step('Подождать прогрузки кнопки закрытия информации об ингредиенте "Краторная булка N-200i" на основной странице')
    def wait_visibility_of_krator_bun_ingred_info_exit_button(self):
        self.wait_visibility_of_element(MainPageLocators.exit_ingred_detail)

    @allure.step('Кликнуть по кнопке закрытия информации об ингредиенте "Краторная булка N-200i" на основной странице')
    def click_on_krator_bun_ingred_info_exit_button(self):
        self.click_on_element(MainPageLocators.exit_ingred_detail)

    @allure.step('Подождать прогрузки кнопки "Лента Заказов" в хедере')
    def wait_visibility_of_order_list_button(self):
        self.wait_visibility_of_element(MainPageLocators.order_list)

    @allure.step('Кликнуть по кнопке "Лента Заказов" в хедере')
    def click_on_order_list_button(self):
        self.click_via_js(MainPageLocators.order_list)

    @allure.step('Подождать прогрузки корзины заказа на основной странице')
    def wait_visibility_of_order_basket(self):
        self.wait_visibility_of_element(MainPageLocators.burger_basket)

    @allure.step('Проверить отображение счетчика ингредиента "Краторная булка N-200i" на основной странице')
    def check_displaying_of_krator_bun_meter(self):
        self.check_displaying_of_element(MainPageLocators.ingred_meter)

    @allure.step('Подождать прогрузки кнопки "Оформить заказ" на основной странице')
    def wait_visibility_of_make_order(self):
        self.wait_visibility_of_element(MainPageLocators.make_order)

    @allure.step('Кликнуть по кнопке "Оформить заказ" на основной странице')
    def click_on_make_order(self):
        self.click_on_element(MainPageLocators.make_order)
    
    @allure.step('Ожидание обновления счётчика')
    def wait_for_counter_update(self, locator, timeout=30):
        initial_value = self.get_ingredient_counter_value(locator)
        current_value = self.get_ingredient_counter_value(locator)
        return current_value
    
    @allure.step('Дождаться скрытия всплывающего окна')
    def wait_until_ingred_info_hidden(self):
        self.wait_visibility_of_element(MainPageLocators.ingred_detail)
        self.wait_until_element_hidden(MainPageLocators.ingred_detail)

    @allure.step('Подождать прогрузки кнопки "Войти в аккаунт" на основной странице')
    def wait_visibility_of_login_button(self):
        self.wait_visibility_of_element(MainPageLocators.login_button)

    @allure.step('Кликнуть по кнопке "Войти в аккаунт" на основной странице')
    def click_on_login_button(self):
        self.click_on_element(MainPageLocators.login_button)

    @allure.step('Подождать прогрузки отображения информации об готовом заказе')
    def wait_visibility_of_ready_order(self):
        return self.wait_visibility_of_element(MainPageLocators.order_is_ready)
    
    @allure.step('Проверить отображение информации об готовом заказе')
    def check_displaying_of_ready_order(self):
        return self.check_displaying_of_element(MainPageLocators.order_is_ready)
    
    @allure.step('Дождаться скрытия всплывающей стены')
    def wait_until_invisible_wall_hidden(self):
        self.wait_visibility_of_element(MainPageLocators.invisible_order_wall)
        self.wait_until_element_hidden(MainPageLocators.invisible_order_wall)

    @allure.step('Получение текущего значения счётчика ингредиентов на главной странице')
    def get_current_ingredient_count(self):
        return self.get_ingredient_counter_value(MainPageLocators.ingred_meter)
    
    @allure.step('Перетащить элемент в корзину')
    def drag_and_drop_element(self, element_from, element_to):
        super().drag_and_drop_with_js(element_from, element_to)

    @allure.step('Дождаться скрытия overlay')
    def wait_until_overlay_hidden(self):
        self.wait_visibility_of_element(MainPageLocators.overlay)
        self.wait_until_element_hidden(MainPageLocators.overlay)

    @allure.step('Подождать прогрузки кнопки закрытия информации о готовом заказе на основной странице')
    def wait_visibility_of_ready_order_info_exit_button(self):
        self.wait_visibility_of_element(MainPageLocators.exit_ready_order_info)

    @allure.step('Кликнуть по кнопке закрытия информации о готовом заказе на основной странице')
    def click_on_ready_order_info_exit_button(self):
        self.click_via_js(MainPageLocators.exit_ready_order_info)