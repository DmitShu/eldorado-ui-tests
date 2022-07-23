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
import pickle
import random as r
import pytest
import time

preconditions = True


def test_basket_add_several_items(web_browser):
    """ Add several items to basket """

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

    # saving cookies for next test cases if pass
    # with open('test_cookies.tmp', 'wb') as cookies:
    #     pickle.dump(web_browser.get_cookies(), cookies)
    page.save_cookies()
    # If this test fails, we block the execution of the rest.
    # (The following require an item in the cart)
    global preconditions
    preconditions = True


@pytest.fixture()
def prec_met():
    assert preconditions, "Precondition not met"


def test_basket_count_items(prec_met, web_browser):
    """ Add several basket """

    page = BasketPage(web_browser)
    page.scroll_up()