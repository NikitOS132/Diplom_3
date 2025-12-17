import allure
from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators

class AccountPage(BasePage):
    @allure.step('Ввод логина и пароля')
    def data_entry_form(self, email: str, password: str):
        self.wait_visibility_of_element(AccountPageLocators.field_email)
        self.send_keys_to_input(AccountPageLocators.field_email, email)
        self.wait_visibility_of_element(AccountPageLocators.field_password)
        self.send_keys_to_input(AccountPageLocators.field_password, password)
        self.click_on_element(AccountPageLocators.button_entrance)