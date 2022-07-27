"""
These test cases check the basket functionality.

How To Run Tests
----------------

1) Install all requirements:

    ```bash
    pip3 install -r requirements.txt
    ```

2) Download and unpack Selenium WebDriver (choose version which is compatible with your browser).

3) Open [conftest.py](conftest.py) and specify the driver type and path to the executable file.

4) Run tests:

    ```bash
    python -m pytest -v tests/
    ```

"""

import time
import random as r
import pytest
from pages.eldorado_page import *
from pages.variables import *


def test_basket_base_functions(web_browser):
    """ Check base functionality. Add two items to basket and check total price"""

    page = MainPage(web_browser)
    # closing choose region popups
    page.header_city_select.click()
    page.region_input.wait_to_be_clickable(5)
    page.region_city_buttons.find()[0].click()
    time.sleep(1)
    page.wait_page_loaded()

    # searching first item
    page.header_search_input.click()
    page.header_search_input.wait_to_be_clickable()
    page.header_search_input = SEARCH_ITEM_1
    page.header_search_item_1.wait_to_be_clickable()
    page.header_search_item_1.click()
    page.wait_page_loaded()
    # adding first item to cart
    page.add_to_cart_button_filter.click()
    page.wait_page_loaded()
    # checking result
    price_total = get_price(page.add_to_cart_price.get_text())
    cart_counter = get_price(page.cart_counter.get_text())
    cart_total = get_price(page.cart_total.get_text())

    assert cart_counter == 1, f'{cart_counter} in basket, but 1 expected'
    assert cart_total == price_total, f'{cart_total} in basket, but {price_total} expected'

    # searching second item
    page.header_search_input.click()
    page.header_search_input.wait_to_be_clickable()
    page.header_search_input = SEARCH_ITEM_2
    page.header_search_item_2.wait_to_be_clickable()
    page.header_search_item_2.click()
    page.wait_page_loaded()
    # adding second item to cart
    page.add_to_cart_button_filter.click()
    page.wait_page_loaded()
    # checking result
    price_total += get_price(page.add_to_cart_price.get_text())
    cart_counter = get_price(page.cart_counter.get_text())
    cart_total = get_price(page.cart_total.get_text())

    assert cart_counter == 2, f'{cart_counter} in basket, but 2 expected'
    assert cart_total == price_total, f'{cart_total} in basket, but {price_total} expected'

    # checking result in basket page
    page.header_basket_button.click()
    time.sleep(1)
    page.wait_page_loaded()
    bb_count = get_price(page.bb_count.get_text())
    bb_cost = get_price(page.bb_cost.get_text())

    assert bb_count == 2, f'{bb_count} in basket, but 2 expected'
    assert price_total == bb_cost, f'{bb_cost} in basket, but {price_total} expected'


def test_basket_price_in_orders(web_browser):
    """ Price in orders page = price in basket page """

    # Prepare basket for tests
    page = prepare_basket(MainPage(web_browser))

    # Total price on basket page
    bb_cost = get_price(page.bb_cost.get_text())
    # Clicking "Продолжить" button
    page.scroll_down()
    page.basket_toorders_button.wait_to_be_clickable()
    page.basket_toorders_button.click()
    time.sleep(1)
    page.wait_page_loaded()

    assert URL_ORDER in page.get_current_url(), "Wrong URL"

    # Total price on order page
    order_cost = get_price(page.order_total_price.get_text())

    assert bb_cost == order_cost != 0, 'Price in orders page != price in basket page'


def test_basket_service_price_apply_remove(web_browser):
    """ Adding and removing services """

    # Prepare basket for tests
    page = prepare_basket(MainPage(web_browser))

    # initial prices
    bb_cost_1 = get_price(page.bb_cost.get_text())
    service_prices = page.basket_services_prices.get_text()
    service_prices = [get_price(p) for p in service_prices]
    # applying service
    page.basket_services_radio.find()[1].click()
    page.wait_page_loaded()
    bb_cost_2 = get_price(page.bb_cost.get_text())

    assert bb_cost_2-bb_cost_1 == service_prices[0], "Service price not applied"

    # removing service
    page.basket_services_radio.find()[0].click()
    page.wait_page_loaded()
    bb_cost_2 = get_price(page.bb_cost.get_text())

    assert bb_cost_2 == bb_cost_1, "Service price not removed"


def test_basket_items_count_change(web_browser):
    """ Changing item count in basket + and - buttons"""

    # Prepare basket for tests
    page = prepare_basket(MainPage(web_browser))

    # initial prices and count
    price_1 = get_price(page.basket_block_price_discount.get_text())
    bb_cost_1 = get_price(page.bb_cost.get_text())
    # increasing item count with "+" button
    page.basket_block_spinner_right.click()
    page.wait_page_loaded()
    # getting new values
    bb_count = get_price(page.bb_count.get_text())
    price_2 = get_price(page.basket_block_price_discount.get_text())
    bb_cost_2 = get_price(page.bb_cost.get_text())

    assert bb_count == 2, f'{bb_count} in basket, but 2 expected'
    assert price_2/price_1 == 2, 'Quantity has not changed'
    assert bb_cost_2-bb_cost_1 == price_1, 'The new price is incorrect'

    # decreasing item count with "-" button
    page.basket_block_spinner_left.click()
    page.wait_page_loaded()
    # getting new values
    bb_count = get_price(page.bb_count.get_text())
    price_2 = get_price(page.basket_block_price_discount.get_text())
    bb_cost_2 = get_price(page.bb_cost.get_text())

    assert bb_count == 1, f'{bb_count} in basket, but 1 expected'
    assert price_2 == price_1, 'Quantity has not changed'
    assert bb_cost_2 == bb_cost_1, 'The new price is incorrect'


def test_basket_decreasing_below_1(web_browser):
    """ Decrease button not working if item count is 1 """

    # Prepare basket for tests
    page = prepare_basket(MainPage(web_browser))

    # initial prices and count
    price_1 = get_price(page.basket_block_price_discount.get_text())
    bb_cost_1 = get_price(page.bb_cost.get_text())
    # increasing item count with "+" button
    page.basket_block_spinner_left.click()
    page.wait_page_loaded()
    # getting new values
    bb_count = get_price(page.bb_count.get_text())
    price_2 = get_price(page.basket_block_price_discount.get_text())
    bb_cost_2 = get_price(page.bb_cost.get_text())

    assert bb_count == 1, f'{bb_count} in basket, but 1 expected'
    assert price_2/price_1 == 1, 'The quantity has changed'
    assert bb_cost_2 == bb_cost_1, 'The price has changed.'


def test_basket_manual_count_input_positive(web_browser):
    """ Changing item count in basket manually with valid count (999 max)"""

    # Prepare basket for tests
    page = prepare_basket(MainPage(web_browser))

    # initial prices
    price_1 = get_price(page.basket_block_price_discount.get_text())
    # setting new count
    page.basket_block_spinner_input.send_keys(COUNT_P_2)
    page.wait_page_loaded()
    # new prices
    price_2 = get_price(page.basket_block_price_discount.get_text())

    assert price_2/price_1 == float(COUNT_P_2), "The price has not changed"


def test_basket_increasing_above_999(web_browser):
    """ Increase button not working if item count is 999 """

    # Prepare basket for tests
    page = prepare_basket(MainPage(web_browser))

    # setting item count (999)
    page.basket_block_spinner_input.send_keys(COUNT_P_2)
    time.sleep(1)
    page.wait_page_loaded()
    # checking item count
    bb_count = get_price(page.bb_count.get_text())

    assert bb_count == float(COUNT_P_2), "Precondition fail. Count has not changed"

    page.refresh()
    # increasing item count with "+" button
    page.basket_block_spinner_right.click()
    page.wait_page_loaded()
    # getting new values
    bb_count = get_price(page.bb_count.get_text())

    assert bb_count == float(COUNT_P_2), "Count has changed"


@pytest.mark.parametrize("value", [COUNT_N_ZERO,
                                   COUNT_N_LARGE,
                                   COUNT_N_VERYBIG,
                                   COUNT_N_NEGATIVE,
                                   COUNT_N_FLOAT,
                                   COUNT_N_TEXT,
                                   COUNT_N_SPECIAL,],
                         ids= [COUNT_N_ZERO,
                                   COUNT_N_LARGE,
                                   COUNT_N_VERYBIG,
                                   COUNT_N_NEGATIVE,
                                   COUNT_N_FLOAT,
                                   COUNT_N_TEXT,
                                   COUNT_N_SPECIAL,],)
def test_basket_manual_count_input_negative(web_browser, value):
    """ Changing item count in basket manually with invalid values"""

    # Prepare basket for tests
    page = prepare_basket(MainPage(web_browser))

    # setting new count
    page.basket_block_spinner_input.send_keys(value)
    page.wait_page_loaded()
    # new prices
    bb_count = get_price(page.bb_count.get_text())

    assert 0<bb_count<1000, "item count out of range"


def test_basket_remove_item(web_browser):
    """ Removing item from basket with individual X button """

    # Prepare basket for test
    page = prepare_basket(MainPage(web_browser))

    # removing item
    page.basket_block_close_button.click()
    page.wait_page_loaded()
    # checking remaining items number and price
    bb_count = get_price(page.bb_count.get_text())
    bb_cost = get_price(page.bb_cost.get_text())

    assert bb_count == 0, 'Item was not removed'
    assert bb_cost == 0, 'Item was not removed'


def test_basket_restore_removed_item(web_browser):
    """ Test item recovery in basket page """

    # Prepare basket for test
    page = prepare_basket(MainPage(web_browser))

    # removing item
    page.basket_block_close_button.click()
    time.sleep(1)
    page.basket_item_recovery_button.wait_to_be_clickable(5)

    # Checking item removed
    bb_count = get_price(page.bb_count.get_text())
    assert bb_count == 0, 'Item was not removed'

    # Checking recovery button
    assert page.basket_item_recovery_button.is_clickable(), 'Restore button is not clickable'

    # Restoring item
    page.basket_item_recovery_button.click()
    page.wait_page_loaded()

    # Checking item restored
    bb_count = get_price(page.bb_count.get_text())
    assert bb_count == 1, 'Item was not restored'


def test_basket_clear_basket_button(web_browser):
    """ Test clear basket button functionality """

    # Prepare basket for test
    page = prepare_basket(MainPage(web_browser))

    # removing by button
    page.basket_clear_button.click()
    time.sleep(1)
    page.wait_page_loaded()

    # checking remaining items number and price
    bb_count = get_price(page.bb_count.get_text())
    bb_cost = get_price(page.bb_cost.get_text())

    assert bb_count == 0, 'Item was not removed'
    assert bb_cost == 0, 'Item was not removed'


def test_basket_item_could_restore_after_clean(web_browser):
    """ Test items can be restored after cleaning the basket. """

    # Prepare basket for test
    page = prepare_basket(MainPage(web_browser))

    # removing by button
    page.basket_clear_button.click()
    time.sleep(1)
    page.wait_page_loaded()

    # checking remaining items number and price
    bb_count = get_price(page.bb_count.get_text())
    bb_cost = get_price(page.bb_cost.get_text())

    assert bb_count == 0, 'Item was not removed'
    assert bb_cost == 0, 'Item was not removed'

    # Checking recovery button
    assert page.basket_item_recovery_button.is_clickable(), 'Restore button is not clickable'

    # Restoring item
    page.basket_item_recovery_button.click()
    page.wait_page_loaded()

    # Checking item restored
    bb_count = get_price(page.bb_count.get_text())
    assert bb_count == 1, 'Item was not restored'


def test_basket_empty_after_page_refresh(web_browser):
    """ Checking that the basket is empty after cleaning and reloading the page. """

    # Prepare basket for test
    page = prepare_basket(MainPage(web_browser))

    # removing by button
    page.basket_clear_button.click()
    time.sleep(1)
    page.wait_page_loaded()

    # checking remaining items number and price
    bb_count = get_price(page.bb_count.get_text())
    bb_cost = get_price(page.bb_cost.get_text())

    assert bb_count == 0, 'Item was not removed'
    assert bb_cost == 0, 'Item was not removed'

    # refreshing page.
    page.refresh()

    assert page.basket_empty_span.is_visible(), 'Basket is not empty.'




def test_basket_test(web_browser):
    """ testing test """

    page=MainPage(web_browser)

    page.get(URL_MAIN)
    page.refresh()
    page.basket_empty_span.is_visible()

