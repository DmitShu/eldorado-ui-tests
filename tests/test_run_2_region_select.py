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


def test_city_select_popup_yes(web_browser):
    """ Checking the "Yes" button of the city selection popup. """

    page = MainPage(web_browser)

    # checking button availability
    page.header_city_popup_yes.wait_to_be_clickable(3)

    assert page.header_city_popup_yes.is_clickable(), "Button is not clickable"

    # clicking button
    page.header_city_popup_yes.click()
    time.sleep(1)

    # Popup is no longer visible on page
    page.refresh()

    assert page.header_city_popup_yes.wait_until_not_visible(5) == None, "Popup visible"


def test_city_select_popup_no(web_browser):
    """ Checking the "No" button of the city selection popup. """

    page = MainPage(web_browser)

    # checking button availability
    page.header_city_popup_no.wait_to_be_clickable(3)

    assert page.header_city_popup_no.is_clickable(), "Button is not clickable"

    # clicking button
    page.header_city_popup_no.click()
    time.sleep(1)
    page.wait_page_loaded()

    # City select form is visible
    assert page.region_input.is_visible(), "City select form not visible"


def test_city_select_popup_not_showing_again(web_browser):
    """ Checking that popup does not appear after the selection form is closed. """

    page = MainPage(web_browser)

    # checking button availability
    page.header_city_popup_no.wait_to_be_clickable(3)

    assert page.header_city_popup_no.is_clickable(), "Button is not clickable"

    # clicking button
    page.header_city_popup_no.click()
    time.sleep(1)
    page.wait_page_loaded()

    # City select form is visible
    assert page.region_input.is_visible(), "City select form not visible"

    # Closing city select form
    page.region_close_button.click()
    time.sleep(1)
    page.refresh()

    assert page.header_city_popup_no.wait_until_not_visible(5) == None, "Popup visible"


def test_city_select_input_positive(web_browser):
    """ Check "Выберите ваш город", input real city """

    page = MainPage(web_browser)

    # clicking city selection input
    page.header_city_select.click()
    page.region_input.wait_to_be_clickable(5)

    assert page.region_input.is_visible(), "City select form not visible"

    page.region_input.send_keys(CITY_P_1, 1)
    page.region_option.click()
    page.wait_page_loaded()

    assert CITY_P_1 in page.header_city_select.get_text(), "City was not selected"


def test_city_select_input_suggest(web_browser):
    """ Check "Выберите ваш город", input suggester """

    page = MainPage(web_browser)

    # clicking city selection input
    page.header_city_select.click()
    page.region_input.wait_to_be_clickable(5)

    assert page.region_input.is_visible(), "City select form not visible"

    page.region_input.send_keys(CITY_P_1_SUGGEST, 5)

    assert CITY_P_1 in page.region_option.get_text(), "City suggestion not working"


def test_city_select_input_eng_layout(web_browser):
    """ Check "Выберите ваш город", input wrong layout """

    page = MainPage(web_browser)

    # clicking city selection input
    page.header_city_select.click()
    page.region_input.wait_to_be_clickable(5)

    assert page.region_input.is_visible(), "City select form not visible"

    page.region_input.send_keys(CITY_P_1_ENG, 5)

    assert CITY_P_1 in page.region_option.get_text(), "Wrong keyboard layout suggestion not working"


@pytest.mark.parametrize("city",  [CITY_N_1,
                                   CITY_N_2,
                                   CITY_N_3,],
                            ids=  [CITY_N_1,
                                   CITY_N_2,
                                   CITY_N_3],)
def test_city_select_input_negative(web_browser, city):
    """ Check "Выберите ваш город", input bad data """

    page = MainPage(web_browser)
    page.header_city_select.click()
    page.region_input.wait_to_be_clickable(5)

    assert page.region_input.is_visible(), "City select form not visible"

    page.region_input.send_keys(city, 1)
    page.region_option.click()
    page.wait_page_loaded()

    assert CITY_BAD_MESSAGE in page.region_option.get_text(), "No invalid input message"


def test_city_select_by_button(web_browser):
    """ Check "Выберите ваш город", select city by button """

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


def test_city_select_from_list(web_browser):
    """ Check "Выберите ваш город", from list """

    page = MainPage(web_browser)

    page.header_city_select.click()
    page.region_input.wait_to_be_clickable(5)

    assert page.region_input.is_visible(), "City select form not visible"

    # Select and click regions from list
    page.region_list_1_select.wait_to_be_clickable(2)
    page.region_list_1_select.click()
    page.region_list_2_select.wait_to_be_clickable(2)
    page.region_list_2_select.click()
    page.region_list_3_select.wait_to_be_clickable(2)
    page.region_list_3_select.click()
    time.sleep(1)
    page.wait_page_loaded()

    # checking resoult
    assert REGION_LIST_3 in page.header_city_select.get_text(), "City was not selected"


def test_city_selection_saved(web_browser):
    """ Check selected city on different pages """

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

    # checking result in basket page
    page.get(URL_MAIN+URL_BASKET)
    page.basket_page_region.wait_to_be_clickable(3)

    assert cty_tst_btn_txt in page.basket_page_region.get_text(), "Selected city was not saved"
