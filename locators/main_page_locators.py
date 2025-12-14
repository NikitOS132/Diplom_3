from selenium.webdriver.common.by import By

class MainPageLocators:
    krator_bun = (By.XPATH, "//p[text()='Краторная булка N-200i']/ancestor::a[contains(@class,'BurgerIngredient_ingredient')]")
    ingred_detail = (By.XPATH, "//div[contains(@class,'Modal_modal__contentBox') and contains(@class,'pt-10')]")
    exit_ingred_detail = (By.XPATH, ".//button[contains(@class,'Modal_modal__close_modified') and contains(@class,'Modal_modal__close')]")
    burger_basket = (By.XPATH, "//ul[contains(@class,'BurgerConstructor_basket')]")
    ingred_meter = (By.XPATH, "//p[text()='Краторная булка N-200i']/ancestor::a[contains(@class,'BurgerIngredient_ingredient')]//p[contains(@class,'counter_counter__num')]")
    make_order = (By.XPATH, ".//button[contains(text(),'Оформить заказ')]")
    order_list = (By.XPATH, "//*[contains(@class,'AppHeader_header__linkText') and contains(@class,'ml-2') and text()='Лента Заказов']")
    login_button = (By.XPATH, ".//button[contains(text(),'Войти в аккаунт')]")
    order_is_ready = (By.XPATH, "//div[contains(@class,'Modal_modal__contentBox') and contains(@class,'pt-30')]")
    invisible_order_wall = (By.XPATH, ".//div[contains(@class,'Modal_modal_opened') and contains(@class,'Modal_modal__P3')]")
    overlay = (By.XPATH, "//div[contains(@class,'Modal_modal_overlay')]")
    exit_ready_order_info = (By.XPATH, ".//button[contains(@class,'Modal_modal__close_modified') and contains(@class,'Modal_modal__close')]")