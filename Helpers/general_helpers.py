from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException


class Helper():
    def __init__(self, driver, test_logger):
        self.driver = driver
        self.test_logger = test_logger

    def go_to_page(self, url):
        self.driver.get(url)
        self.test_logger.info(f"{url} is opened.")

    # def find_and_click(self, loc, sec=60):
    #     WebDriverWait(self.driver, sec).until(EC.element_to_be_clickable(loc)).click()

    def find_and_click(self, loc, sec=60):
        try:
            WebDriverWait(self.driver, sec).until(EC.presence_of_element_located(loc))
            WebDriverWait(self.driver, sec).until(EC.element_to_be_clickable(loc)).click()
        except StaleElementReferenceException:
            # Re-fetch the element and try again
            WebDriverWait(self.driver, sec).until(EC.presence_of_element_located(loc))
            WebDriverWait(self.driver, sec).until(EC.element_to_be_clickable(loc)).click()

    def find_and_send_keys(self, loc, inp_text, sec=60):
        elem = self.find_elem_ui(loc, sec)
        elem.send_keys(inp_text)

    def move_to_element(self, loc, sec=60):
        element = self.find_elem_ui(loc, sec)
        ActionChains(self.driver).move_to_element(element).perform()
        self.test_logger.info(f"Moved to element: {loc}")

    def hover_element(self, loc):
        actions = ActionChains(self.driver)
        hover = actions.move_to_element(self.find_elem_ui(loc)).pause(0.5)
        hover.perform()
