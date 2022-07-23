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

preconditions = False


def test_basket_add_several_items(web_browser):
    """ Add several items to basket """

    page = MainPage(web_browser)
    page.scroll_up()
    page.header_search_input

    # with open('test_cookies.tmp', 'wb') as cookies:
    #     pickle.dump(web_browser.get_cookies(), cookies)
    #
    # assert page.region_input.is_visible(), "City select form not visible"

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