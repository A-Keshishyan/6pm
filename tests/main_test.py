import config
import time
from Testdatas.data import search_keyword, brand_filter_value, filter_price_value
from Pages.page_search import Home
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search_and_filter_products(test_driver, test_logger):
    home_page = Home(test_driver, test_logger)

    home_page.go_to_page(config.url)
    home_page.search_product(search_keyword)

    # Verify correct results page
    assert home_page.find_elem_ui(home_page.search_result_header_locator), \
        test_logger.error("Search result page did not load as expected.")
    test_logger.info("Search result page loaded successfully.")

    time.sleep(20)
    home_page.apply_filters()

    result_count_locator = (By.CLASS_NAME, "ft-z")
    filtered_result_elem = WebDriverWait(test_driver, 10).until(
        EC.visibility_of_element_located(result_count_locator)
    )
    filtered_result_text = filtered_result_elem.text
    test_logger.info(f"Filtered result count: {filtered_result_text}")

    product_card = WebDriverWait(test_driver, 15).until(
        EC.presence_of_element_located(Home.product_card_locator)
    )

    returned_brand, returned_price = home_page.extracted_brand_and_price(product_card)

    assert returned_brand == brand_filter_value, f"Filtered brand '{brand_filter_value}' does not match returned product brand '{returned_brand}'"
    # assert returned_price <= float(filter_price_value.replace('$', '')), \
    #     f" price ≤ {filter_price_value}, got ${returned_price }"
    assert returned_price <= float(filter_price_value.replace('$', '')), \
        f" Filtered returned price ${returned_price} is not less than or equal to the selected filter price {filter_price_value}"

    test_logger.info(f"Verified brand: {returned_brand}")
    test_logger.info(f"Verified price: ${returned_price} within limit {filter_price_value}")
