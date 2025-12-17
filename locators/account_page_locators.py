from selenium.webdriver.common.by import By

class AccountPageLocators:
    button_entrance = (By.XPATH, ".//button[contains(text(),'Войти')]")
    field_email = (By.XPATH, "//div[label[contains(text(),'Email')]]//input")
    field_password = (By.XPATH, "//div[label[contains(text(),'Пароль')]]//input")