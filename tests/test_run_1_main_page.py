"""
These test cases check the presence and functions of elements on the main page.

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


# Header elements testing


def test_click_header_club(web_browser):
    """ Check header element "Эльдорадости" opens in new tab """

    page = MainPage(web_browser)
    page.header_club.click()
    page.wait_page_loaded()

    assert URL_CLUB not in page.get_current_url(), "Same tab"

    page.switch_tab()
    page.wait_page_loaded()

    assert URL_CLUB in page.get_current_url(), "Wrong URL"


def test_click_header_shops(web_browser):
    """ Check header element "Магазины" opens in new tab """

    page = MainPage(web_browser)
    page.header_shops.click()
    page.wait_page_loaded()

    assert URL_SHOPS not in page.get_current_url(), "Same tab"

    page.switch_tab()
    page.wait_page_loaded()

    assert URL_SHOPS in page.get_current_url(), "Wrong URL"


def test_click_header_pvz(web_browser):
    """ Check header element "Пункты выдачи" opens in new tab """

    page = MainPage(web_browser)
    page.header_pvz.click()
    page.wait_page_loaded()

    assert URL_PVZ not in page.get_current_url(), "Same tab"

    page.switch_tab()
    page.wait_page_loaded()

    assert URL_PVZ in page.get_current_url(), "Wrong URL"

@pytest.mark.xfail(reason="Valid order num + phone needed")
def test_click_header_orders_valid_data(web_browser):
    """ Check header element "Статус заказа", click, valid data """

    page = MainPage(web_browser)
    page.header_orders.click()
    page.orders_form_submit_button.wait_to_be_clickable()

    assert page.orders_form_submit_button.is_clickable(), 'No "Статус заказа" form'

    page.orders_form_input_order = ORDER_P_1
    page.orders_form_input_phone = ORDER_TEL_P_1
    page.orders_form_submit_button.click()
    page.wait_page_loaded()

    # checking redirection to personal orders
    messages = page.orders_form_messages.get_text()

    assert URL_ORDERS in page.get_current_url(), "Orders pages not opened"


def test_click_header_orders_empty_fields(web_browser):
    """ Check header element "Статус заказа", click, empty fields """

    page = MainPage(web_browser)
    page.header_orders.click()
    page.orders_form_submit_button.wait_to_be_clickable()

    assert page.orders_form_submit_button.is_clickable(), 'No "Статус заказа" form'

    page.orders_form_submit_button.click()
    time.sleep(1)
    messages = page.orders_form_messages.get_text()

    assert ORDER_TEL_EMPTY in messages, 'No "' + ORDER_TEL_EMPTY + '" on form'
    assert ORDER_EMPTY_MSG in messages, 'No "' + ORDER_EMPTY_MSG + '" on form'


def test_click_header_orders_invalid_phone(web_browser):
    """ Check header element "Статус заказа", click, invalid phone """

    page = MainPage(web_browser)
    page.header_orders.click()
    page.orders_form_submit_button.wait_to_be_clickable()

    assert page.orders_form_submit_button.is_clickable(), 'No "Статус заказа" form'

    page.orders_form_input_order = ORDER_P_1
    page.orders_form_input_phone = ORDER_TEL_N_1
    page.orders_form_submit_button.click()
    time.sleep(1)
    messages = page.orders_form_messages.get_text()

    assert ORDER_TEL_BAD_MESSAGE in messages, 'No "' + ORDER_TEL_BAD_MESSAGE + '" on form'


def test_click_header_blog(web_browser):
    """ Check header element "Эльдоблог" opens in new tab """

    page = MainPage(web_browser)
    page.header_blog.click()
    page.wait_page_loaded()

    assert URL_BLOG not in page.get_current_url(), "Same tab"

    page.switch_tab()
    page.wait_page_loaded()

    assert URL_BLOG in page.get_current_url(), "Wrong URL"


def test_click_header_b2b(web_browser):
    """ Check header element "Для бизнеса" opens in new tab """

    page = MainPage(web_browser)
    page.header_b2b.click()
    page.wait_page_loaded()

    assert URL_B2B not in page.get_current_url(), "Same tab"

    page.switch_tab()
    page.wait_page_loaded()

    assert URL_B2B in page.get_current_url(), "Wrong URL"


def test_click_header_chat(web_browser):
    """ Check header element "Открыть онлайн-консультант" shows links to social """

    page = MainPage(web_browser)
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

    assert URL_BASKET in page.get_current_url(), "Not a basket page"


# Main section testing


def test_main_catalog_menu_available(web_browser):
    """ Check main menu catalog shown and not empty """

    page = MainPage(web_browser)

    # locating main menu catalog items
    assert page.main_catalog_buttons.count() > 0, 'Menu not found'
    # At least one element visible
    assert page.main_catalog_buttons.find()[0].is_displayed, 'Menu not visible'


def test_main_hero_block_available(web_browser):
    """ Check main page hero block shown """

    page = MainPage(web_browser)

    # locating main menu catalog items
    assert page.main_hero_block.count() > 0, 'Menu not found'
    # All items have unique pictures
    img = page.main_hero_block.get_attribute('src')
    img_s = set(img)

    assert len(img) == len(img_s), 'Some items missing or duplicated'


def test_main_recommend_tabs_available(web_browser):
    """ Check main page contains recommendation tabs """

    page = MainPage(web_browser)

    # at least 3 tabs shown
    rec_tabs_cnt = page.main_recommend_tabs.count()
    rec_tabs = page.main_recommend_tabs.find()

    assert  rec_tabs_cnt >= 3, 'Recommendation tabs not found'

    # checking individual tabs
    for i in range(rec_tabs_cnt):
        page.add_to_cart_button_main.scroll_to_element()
        rec_tabs[i].click()
        page.add_to_cart_button_main.scroll_to_element()
        page.add_to_cart_button_main.wait_to_be_clickable(3)
        time.sleep(1)

        assert page.add_to_cart_button_main.is_clickable(), 'There are no items in the recommendation tab'


def test_main_media_block_tube_available(web_browser):
    """ Check main page "ЭльдоTUBE" element """

    # finding and clicking button
    page = MainPage(web_browser)
    page.main_media_tube.scroll_to_element()
    page.main_media_tube.click()
    page.wait_page_loaded()

    # Link should open in a new tab
    assert URL_TUBE not in page.get_current_url(), "Same tab"

    page.switch_tab()
    page.wait_page_loaded()

    # checking current page URL
    assert URL_TUBE in page.get_current_url(), "Wrong URL"


def test_main_media_block_play_available(web_browser):
    """ Check main page "ЭльдоPLAY" element """

    # finding and clicking button
    page = MainPage(web_browser)
    page.main_media_play.scroll_to_element()
    page.main_media_play.click()
    page.wait_page_loaded()

    # Link should open in a new tab
    assert URL_PLAY not in page.get_current_url(), "Same tab"

    page.switch_tab()
    page.wait_page_loaded()

    # checking current page URL
    assert URL_PLAY in page.get_current_url(), "Wrong URL"


def test_main_media_block_blog_available(web_browser):
    """ Check main page "ЭльдоBLOG" element """

    # finding and clicking button
    page = MainPage(web_browser)
    page.main_media_blog.scroll_to_element()
    page.main_media_blog.click()
    page.wait_page_loaded()

    # Link should open in a new tab
    assert URL_BLOG not in page.get_current_url(), "Same tab"

    page.switch_tab()
    page.wait_page_loaded()

    # checking current page URL
    assert URL_BLOG in page.get_current_url(), "Wrong URL"
