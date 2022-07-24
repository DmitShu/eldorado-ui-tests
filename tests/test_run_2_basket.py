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

from pages.eldorado_pages import *
from pages.variables import *
import random as r
import pytest
import time

preconditions = True


def test_basket_add_several_items(web_browser):
    """ Check base functionality. Add several items to basket """

    page = MainPage(web_browser)
    if page.header_city_popup.is_clickable():
        page.header_city_popup.click()

    # searching first item
    page.header_search_input.click()
    page.header_search_input.wait_to_be_clickable()
    page.header_search_input = search_item_1
    page.header_search_item_1.wait_to_be_clickable()
    page.header_search_item_1.click()
    page.wait_page_loaded()
    # adding first item to cart
    page.add_to_cart_button.click()
    page.wait_page_loaded()
    # checking result
    price_total = float(page.add_to_cart_price.get_text().replace(' ', ''))
    cart_counter = float(page.cart_counter.get_text())
    cart_total = float((page.cart_total.get_text().split(' р.')[0].replace(' ', '')))

    assert cart_counter == 1, f'{cart_counter} in basket, but 1 expected'
    assert cart_total == price_total, f'{cart_total} in basket, but {price_total} expected'

    # searching second item
    page.header_search_input.click()
    page.header_search_input.wait_to_be_clickable()
    page.header_search_input = search_item_2
    page.header_search_item_2.wait_to_be_clickable()
    page.header_search_item_2.click()
    page.wait_page_loaded()
    # adding second item to cart
    page.add_to_cart_button.click()
    page.wait_page_loaded()
    # checking result
    price_total += float(page.add_to_cart_price.get_text().replace(' ', ''))
    cart_counter = float(page.cart_counter.get_text())
    cart_total = float((page.cart_total.get_text().split(' р.')[0].replace(' ', '')))

    assert cart_counter == 2, f'{cart_counter} in basket, but 2 expected'
    assert cart_total == price_total, f'{cart_total} in basket, but {price_total} expected'

    page.header_basket_button.click()
    page.wait_page_loaded()

    assert cart_counter == 2, f'{cart_counter} in basket, but 2 expected'
    assert cart_total == price_total, f'{cart_total} in basket, but {price_total} expected'

    # checking result in basket page
    page.header_basket_button.click()
    page.wait_page_loaded()
    bb_count = (float(page.bb_count.get_text()))
    bb_cost = (float(page.bb_cost.get_text().split('р')[0].replace(' ', '')))

    assert bb_count == 2, f'{bb_count} in basket, but 2 expected'
    assert price_total == bb_cost, f'{bb_cost} in basket, but {price_total} expected'

    # saving cookies for next test cases if pass
    page.save_cookies()
    # If this test fails, we block the execution of the rest.
    # (The following require an item in the cart)
    global preconditions
    preconditions = True


@pytest.fixture()
def prec_met():
    assert preconditions, "Precondition not met"


def test_basket_items_count_change(prec_met, web_browser):
    """ Changing item count in basket """

    page = BasketPage(web_browser)
    page.load_cookies()
    # initial prices and count
    price_1 = (float(page.basket_block_price_discount.get_text().replace(' ', '').replace('р', '')))
    bb_cost_1 = (float(page.bb_cost.get_text().split('р')[0].replace(' ', '')))
    # increasing item count with "+" button
    page.basket_block_spinner_right.click()
    page.wait_page_loaded()
    # getting new values
    bb_count = (float(page.bb_count.get_text()))
    price_2 = (float(page.basket_block_price_discount.get_text().replace(' ', '').replace('р', '')))
    bb_cost_2 = (float(page.bb_cost.get_text().split('р')[0].replace(' ', '')))

    assert bb_count == 3, f'{bb_count} in basket, but 3 expected'
    assert price_2/price_1 == 2, 'Quantity has not changed'
    assert bb_cost_2-bb_cost_1 == price_1, 'The new price is incorrect'

    # decreasing item count with "-" button
    page.basket_block_spinner_left.click()
    page.wait_page_loaded()
    # getting new values
    bb_count = (float(page.bb_count.get_text()))
    price_2 = (float(page.basket_block_price_discount.get_text().replace(' ', '').replace('р', '')))
    bb_cost_2 = (float(page.bb_cost.get_text().split('р')[0].replace(' ', '')))

    assert bb_count == 2, f'{bb_count} in basket, but 2 expected'
    assert price_2 == price_1, 'Quantity has not changed'
    assert bb_cost_2 == bb_cost_1, 'The new price is incorrect'


def test_basket_service_price_apply_remove(prec_met, web_browser):
    """ Adding and removing services """

    page = BasketPage(web_browser)
    page.load_cookies()
    # initial prices
    bb_cost_1 = (float(page.bb_cost.get_text().split('р')[0].replace(' ', '')))
    service_prices = page.basket_services_prices.get_text()
    service_prices = [float(p.replace(' ', '').replace('р.', '')) for p in service_prices]
    # applying service
    page.basket_services_radio.find()[1].click()
    page.wait_page_loaded()
    bb_cost_2 = (float(page.bb_cost.get_text().split('р')[0].replace(' ', '')))

    assert bb_cost_2-bb_cost_1 == service_prices[0], "Service price not applied"

    # removing service
    page.basket_services_radio.find()[0].click()
    page.wait_page_loaded()
    bb_cost_2 = (float(page.bb_cost.get_text().split('р')[0].replace(' ', '')))

    assert bb_cost_2 == bb_cost_1, "Service price not removed"


# def test_basket_delete_items(prec_met, web_browser):
#     """ Removing items from basket """
#
#     page = BasketPage(web_browser)
#     page.load_cookies()
#     # removing first item
#     page.basket_block_close_button.click()
#     page.wait_page_loaded()
#     # checking remaining items number and price
#     bb_count = (float(page.bb_count.get_text()))
#     bb_cost = (float(page.bb_cost.get_text().split('р')[0].replace(' ', '')))
#     item_cost = (float(page.basket_block_price_discount.get_text().replace(' ', '').replace('р', '')))
#
#     assert bb_count == 1, f'{bb_count} in basket, but 1 expected'
#     assert item_cost == bb_cost, f'{bb_cost} in basket, but {item_cost} expected'
#
#     # removing last item
#     page.basket_block_close_button.click()

