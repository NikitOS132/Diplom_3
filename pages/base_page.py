import allure
from selenium.webdriver.support.ui import WebDriverWait
from seletools.actions import drag_and_drop
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Подождать прогрузки элемента')
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located(locator))
    
    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Ввести значение в поле ввода')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Получение начального значения счётчика')
    def get_ingredient_counter_value(self, locator):
        element = self.driver.find_element(*locator)
        text = element.text.strip()
        import re
        numbers = re.findall(r'\d+', text)
        return int(numbers[0])
    
    @allure.step('Дождаться скрытия всплывающего окна')
    def wait_until_element_hidden(self, locator, timeout=5):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.invisibility_of_element_located(locator))
    
    @allure.step('Дождаться кликабельности элемента')
    def wait_for_element_to_be_clickable(self, locator, timeout=15):
       wait = WebDriverWait(self.driver, timeout)
       return wait.until(EC.element_to_be_clickable(locator))
    
    @allure.step('Перетащить элемент в корзину')
    def drag_and_drop_with_js(self, source_locator, target_locator):
        source = self.driver.find_element(*source_locator)
        target = self.driver.find_element(*target_locator)

        self.driver.execute_script("""
        const source = arguments[0];
        const target = arguments[1];

        // Создаём событие dragstart
        const dragStartEvent = new DragEvent('dragstart', {
            bubbles: true,
            cancelable: true
        });
        source.dispatchEvent(dragStartEvent);

        // Перемещаем в целевую зону
        const dragEnterEvent = new DragEvent('dragenter', {
            bubbles: true,
            cancelable: true
        });
        target.dispatchEvent(dragEnterEvent);

        // Завершаем drag-and-drop
        const dropEvent = new DragEvent('drop', {
            bubbles: true,
            cancelable: true
        });
        target.dispatchEvent(dropEvent);

        const dragEndEvent = new DragEvent('dragend', {
            bubbles: true,
            cancelable: true
        });
        source.dispatchEvent(dragEndEvent);
    """, source, target)

    @allure.step('Кликнуть на элемент JS')  
    def click_via_js(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Подождать прогрузки сайта')
    def wait_url_to_be(self, expected_url: str, timeout: int = 6):
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))

    @allure.step('Получение первого значения счётчика "За все время"')
    def get_at_all_time_value(self, locator):
        element = self.driver.find_element(*locator)
        text = element.text.strip()
        import re
        numbers = re.findall(r'\d+', text)
        return int(numbers[0])
    
    @allure.step('Получение первого значения счётчика "За сегодня"')
    def get_at_today_value(self, locator):
        element = self.driver.find_element(*locator)
        text = element.text.strip()
        import re
        numbers = re.findall(r'\d+', text)
        return int(numbers[0])