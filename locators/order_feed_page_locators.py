from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    order_in_work = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderListReady') and contains(@class,'OrderFeed_orderList')]/li[contains(@class,'text_type_digits-default') and contains(@class,'mb-2')]")
    at_all_time = (By.XPATH, "//div[contains(@class,'undefined mb-15')]//p[contains(@class,'text text_type_main-medium') and text()='Выполнено за все время:']/following-sibling::p[contains(@class,'OrderFeed_number')]")
    at_today = (By.XPATH, "//div//p[contains(@class,'text text_type_main-medium') and text()='Выполнено за сегодня:']/following-sibling::p[contains(@class,'OrderFeed_number')]")
    constructor = (By.XPATH, "//*[contains(@class,'AppHeader_header__linkText') and contains(@class,'ml-2') and text()='Конструктор']")