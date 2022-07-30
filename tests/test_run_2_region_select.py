"""
These test cases check the region selection functionality.

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

from pages.eldorado_page import MainPage
from pages.helpers import *
import random as r
import pytest
import time


def test_city_select_input_positive(web_browser):
    """ Check header element "Выберите ваш город", input real city """

    page = MainPage(web_browser)
    page.header_city_select.click()
    page.region_input.wait_to_be_clickable(5)

    assert page.region_input.is_visible(), "City select form not visible"

    page.region_input.send_keys(CITY_P_1, 0.5)
    page.region_option.click()
    page.wait_page_loaded()

    assert CITY_P_1 in page.header_city_select.get_text(), "City was not selected"


def test_city_select_input_negative(web_browser):
    """ Check header element "Выберите ваш город", input bad data """

    page = MainPage(web_browser)
    page.header_city_select.click()
    page.region_input.wait_to_be_clickable(5)

    assert page.region_input.is_visible(), "City select form not visible"

    page.region_input.send_keys(CITY_N_1, 0.5)
    page.region_option.click()
    page.wait_page_loaded()

    assert CITY_BAD_MESSAGE in page.region_option.get_text(), "Now invalid input message"


def test_city_select_by_button(web_browser):
    """ Check header element "Выберите ваш город", select city button """

    page = MainPage(web_browser)
    page.header_city_select.click()
    page.region_input.wait_to_be_clickable(5)

    assert page.region_input.is_visible(), "City select form not visible"

    # Select and click random button
    cty_tst_btn = r.choice(page.region_city_buttons.find())
    cty_tst_btn_txt = cty_tst_btn.text
    cty_tst_btn.click()
    page.wait_page_loaded()
    page.header_city_select.wait_to_be_clickable()

    assert cty_tst_btn_txt in page.header_city_select.get_text(), "City was not selected"