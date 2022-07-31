"""
These test cases check the search and filtering on the site.

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
import pytest
from pages.eldorado_page import *
from pages.helpers import *


def test_search_positive(web_browser):
    """ Check the search for a real product. """

    page = MainPage(web_browser)
    # Removing city select popup
    select_city(page)

    # Searching item
    page.header_search_input.click()
    page.header_search_input.wait_to_be_clickable(5)
    page.header_search_input = SEARCH_ITEM_3
    page.header_search_button.wait_to_be_clickable(5)
    page.header_search_button.click()
    page.wait_page_loaded()

    # Verify that user can see the list of products:
    assert page.search_result_products.count() > 0, 'Search results are empty'

    # Make sure user found the relevant products
    for item in page.search_result_products.get_text():
        msg = 'Wrong product in search "{}"'.format(item)
        assert SEARCH_ITEM_3 in item.lower(), msg





