"""
These tests check the presence of elements on the main page and the correctness of the links.

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
import time


def test_click_city_select(web_browser):
    """ Check header element "Выберите ваш город" opens city select form """

    page = MainPage(web_browser)
    page.scroll_up()
    page.header_city_select.click()
    page.wait_page_loaded()

    assert page.region_input.is_visible(), "No city select form"


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
    """ Check header element "Статус заказа" opens new form """

    page = MainPage(web_browser)
    page.scroll_up()
    page.header_orders.click()
    page.wait_page_loaded()

    assert page.orders_form_submit_button.is_clickable(), 'No "Статус заказа" form'


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


# @pytest.mark.parametrize("filter", [255,
#                                     1001,
#                                     123,
#                                     ],
#                          ids= ['255',
#                                '1001',
#                                 '123'
#                                ])
# def test_load_page(web_browser, filter):
#     """ Make sure main search works fine. """
#
#     page = MainPage(web_browser)
#     page.scroll_down()
#     page.wait_page_loaded()
#
#     assert page.get_current_url() == main_url
#     assert filter == 255



# # @pytest.mark.skip(reason="testing")
# def test_check_main_search(web_browser):
#     """ Make sure main search works fine. """
#
#     page = MainPage(web_browser)
#
#     page.search = 'iPhone 12'
#     page.search_run_button.click()
#
#     # Verify that user can see the list of products:
#     assert page.products_titles.count() > 0
#
#     # Make sure user found the relevant products
#     for title in page.products_titles.get_text():
#         msg = 'Wrong product in search "{}"'.format(title)
#         assert 'iphone' in title.lower(), msg

# # @pytest.mark.skip(reason="testing")
# def test_check_wrong_input_in_search(web_browser):
#     """ Make sure that wrong keyboard layout input works fine. """
#
#     page = MainPage(web_browser)
#
#     # Try to enter "смартфон" with English keyboard:
#     page.search = 'cvfhnajy'
#     page.search_run_button.click()
#
#     # Verify that user can see the list of products:
#     assert page.products_titles.count() > 0
#
#     # Make sure user found the relevant products
#     for title in page.products_titles.get_text():
#         msg = 'Wrong product in search "{}"'.format(title)
#         assert 'смартфон' in title.lower(), msg
#
#
# # @pytest.mark.xfail(reason="Filter by price doesn't work")
# # @pytest.mark.skip(reason="testing")
# def test_check_sort_by_price(web_browser):
#     """ Make sure that sort by price works fine.
#     """
#
#     page = MainPage(web_browser)
#
#     page.search = 'чайник'
#     page.search_run_button.click()
#
#     # Scroll to element before click on it to make sure
#     # user will see this element in real browser
#     page.sort_products_by_price.scroll_to_element()
#     page.sort_products_by_price.click()
#     page.wait_page_loaded()
#     page.scroll_down()
#
#     # Get prices of the products in Search results
#     all_prices = page.products_prices.get_text()
#
#     # Convert all prices from strings to numbers
#     all_prices = [float(p.replace(' ', '')) for p in all_prices]
#
#     print()
#     print(all_prices)
#     print(sorted(all_prices))
#
#     # Make sure products are sorted by price correctly:
#     assert all_prices == sorted(all_prices), "Sort by price doesn't work!"
