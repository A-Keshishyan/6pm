from selenium.webdriver.common.by import By
from Helpers.general_helpers import Helper
from Testdatas.data import brand_filter_value, filter_price_value, filter_color


class Home(Helper):
    # Locators
    search_input_locator = (By.XPATH, "//input[@id='searchAll']")
    search_button_locator = (By.XPATH, "//button[text()='Submit Search']")
    search_result_header_locator = (By.XPATH, "//h1[text()='classic sunglasses']") #TODO

    brand_filter_section_locator = (By.XPATH, "//h3[@id='brandNameFacet']/button")
    brand_checkbox_locator = (By.XPATH, f"//a[span[text()='{brand_filter_value}']]")

    price_filter_section_locator = (By.XPATH, "//h3[@id='priceFacet']/button")
    price_checkbox_locator = (By.XPATH, f"//a[.//span[contains(text(), '{filter_price_value}') and contains(text(), 'and Under')]]")

    color_filter_section_locator = (By.XPATH, "//h3[@id='colorFacet']/button")
    color_checkbox_locator = (By.XPATH, f"//a[contains(@class, 'Ss-z')]/span[text()='{filter_color}']")

    product_card_locator = (By.XPATH, "//div[contains(@class, 'cQ-z')]")
    brand_text_locator = (By.XPATH, ".//dd[contains(@class, 'eQ-z')]/span")
    price_text_locator = (By.XPATH, ".//dd[contains(@class, 'M9-z')]//span[contains(@class, 'L9-z')]")

    def search_product(self, keyword):
        self.find_and_send_keys(self.search_input_locator, keyword)
        self.find_and_click(self.search_button_locator)

    def apply_filters(self):
        self.find_and_click(self.brand_filter_section_locator)
        self.find_and_click(self.brand_checkbox_locator)
        self.find_and_click(self.price_filter_section_locator)
        self.find_and_click(self.price_checkbox_locator)
        self.find_and_click(self.color_filter_section_locator)
        self.find_and_click(self.color_checkbox_locator)

    def extracted_brand_and_price(self, product_card):
        brand_elem = product_card.find_element(*self.brand_text_locator)
        price_elem = product_card.find_element(*self.price_text_locator)

        brand_text = brand_elem.text.strip()
        price_text = price_elem.text.strip().replace('$', '')
        price_value = float(price_text)

        return brand_text, price_value
