"""
These tests check the presence and functions of elements on the main page header.

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

from pages.eldorado_main_page import MainPage
from pages.variables import *
import random as r
import time


def test_city_select_input_positive(web_browser):
    """ Check header element "Выберите ваш город", input real city """

    page = MainPage(web_browser)
    page.scroll_up()
    page.header_city_select.click()
    page.region_input.wait_to_be_clickable(5)

    assert page.region_input.is_visible(), "City select form not visible"

    page.region_input.send_keys(city_p_1, 0.5)
    page.region_option.click()
    page.wait_page_loaded()

    assert city_p_1 in page.header_city_select.get_text(), "City was not selected"


def test_city_select_input_negative(web_browser):
    """ Check header element "Выберите ваш город", input bad data """

    page = MainPage(web_browser)
    page.scroll_up()
    page.header_city_select.click()
    page.region_input.wait_to_be_clickable(5)

    assert page.region_input.is_visible(), "City select form not visible"

    page.region_input.send_keys(city_n_1, 0.5)
    page.region_option.click()
    page.wait_page_loaded()

    assert city_bad_message in page.region_option.get_text(), "Now invalid input message"


def test_city_select_by_button(web_browser):
    """ Check header element "Выберите ваш город", select city button """

    page = MainPage(web_browser)
    page.scroll_up()
    page.header_city_select.click()
    page.region_input.wait_to_be_clickable(5)

    assert page.region_input.is_visible(), "City select form not visible"

    # Select and click random button
    cty_tst_btn = r.choice(page.region_city_buttons.find())
    cty_tst_btn_txt = cty_tst_btn.text
    cty_tst_btn.click()
    page.wait_page_loaded()

    assert cty_tst_btn_txt in page.header_city_select.get_text(), "City was not selected"


def test_click_header_club(web_browser):
    """ Check header element "Эльдорадости" opens in new tab """

    page = MainPage(web_browser)
    page.header_club.click()
    page.wait_page_loaded()

    assert MainPage.header_club_url not in page.get_current_url(), "Same tab"

    page.switch_tab()
    page.wait_page_loaded()

    assert MainPage.header_club_url in page.get_current_url(), "Wrong URL"


def test_click_header_shops(web_browser):
    """ Check header element "Магазины" opens in new tab """

    page = MainPage(web_browser)
    page.header_shops.click()
    page.wait_page_loaded()

    assert MainPage.header_shops_url not in page.get_current_url(), "Same tab"

    page.switch_tab()
    page.wait_page_loaded()

    assert MainPage.header_shops_url in page.get_current_url(), "Wrong URL"


def test_click_header_pvz(web_browser):
    """ Check header element "Пункты выдачи" opens in new tab """

    page = MainPage(web_browser)
    page.header_pvz.click()
    page.wait_page_loaded()

    assert MainPage.header_pvz_url not in page.get_current_url(), "Same tab"

    page.switch_tab()
    page.wait_page_loaded()

    assert MainPage.header_pvz_url in page.get_current_url(), "Wrong URL"


def test_click_header_orders(web_browser):
    """ Check header element "Статус заказа", click, empty fields """

    page = MainPage(web_browser)
    page.scroll_up()
    page.header_orders.click()
    page.orders_form_submit_button.wait_to_be_clickable()

    assert page.orders_form_submit_button.is_clickable(), 'No "Статус заказа" form'

    page.orders_form_submit_button.click()
    messages = page.orders_form_messages.get_text()

    assert order_tel_empty in messages, 'No "'+order_tel_empty+'" on form'
    assert order_empty_msg in messages, 'No "'+order_empty_msg+'" on form'




def test_click_header_blog(web_browser):
    """ Check header element "Эльдоблог" opens in new tab """

    page = MainPage(web_browser)
    page.header_blog.click()
    page.wait_page_loaded()

    assert MainPage.header_blog_url not in page.get_current_url(), "Same tab"

    page.switch_tab()
    page.wait_page_loaded()

    assert MainPage.header_blog_url in page.get_current_url(), "Wrong URL"


def test_click_header_b2b(web_browser):
    """ Check header element "Для бизнеса" opens in new tab """

    page = MainPage(web_browser)
    page.header_b2b.click()
    page.wait_page_loaded()

    assert MainPage.header_b2b_url not in page.get_current_url(), "Same tab"

    page.switch_tab()
    page.wait_page_loaded()

    assert MainPage.header_b2b_url in page.get_current_url(), "Wrong URL"


def test_click_header_chat(web_browser):
    """ Check header element "Открыть онлайн-консультант" shows links to social """

    page = MainPage(web_browser)
    page.scroll_up()
    page.header_chat_button.click()

    assert page.chat_viber_button.wait_to_be_clickable(1), "No viber link"
    assert page.chat_telegram_button.wait_to_be_clickable(1), "No telegram link"


def test_click_header_login(web_browser):
    """ Check header element "Регистрация или вход" shows login form """

    page = MainPage(web_browser)
    page.scroll_up()
    page.header_login_button.click()

    assert page.login_tel_input.wait_to_be_clickable(1), "No tel field"
    assert page.login_submit_button.wait_to_be_clickable(1), "No submit button"


def test_click_header_basket(web_browser):
    """ Check header element "Корзина" opens basket page """

    page = MainPage(web_browser)
    page.header_basket_button.click()
    page.wait_page_loaded()

    assert MainPage.header_basket_url in page.get_current_url(), "Not a basket page"