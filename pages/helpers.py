"""

Contains common variables and methods, used in tests

"""

import time

#------------------------------------------------------------------------
# common variables, used in tests


# URL'S
URL_MAIN = 'https://www.eldorado.ru'
URL_CLUB = '/club/'
URL_SHOPS = '/info/shops/'
URL_PVZ = '/info/pvz/11324/'
URL_ORDERS = '/personal/orders/'
URL_BLOG = 'https://blog.eldorado.ru/'
URL_B2B = '/b2b/'
URL_BASKET = '/personal/basket.php'
URL_ORDER = '/personal/order_self_delivery.php'
# холодильники
URL_CATEGORY_1 = '/c/kholodilniki'
# утюги
URL_CATEGORY_2 = '/c/utyugi'


# Header city form
CITY_P_1 = 'Ярославль'
CITY_N_1 = '12345'
CITY_BAD_MESSAGE = 'Ничего не найдено'


# Header orders form
ORDER_TEL_P_1 = '9666666666'
ORDER_TEL_N_1 = '0000000000'
ORDER_P_1 = '1234567890'
ORDER_TEL_BAD_MESSAGE = 'Мобильный телефон указан некорректно'
ORDER_TEL_EMPTY = 'Мобильный телефон не указан'
ORDER_EMPTY_MSG = 'Введите номер заказа'


# Search
SEARCH_ITEM_1 = 'Холодильники'
SEARCH_ITEM_2 = 'Утюги'


# Basket item count (max 999 allowed)
COUNT_P_1 = '10'
COUNT_P_2 = '999'
COUNT_N_ZERO = '0'
COUNT_N_LARGE = '1000'
COUNT_N_VERYBIG = '1000000000'
COUNT_N_NEGATIVE = '-10'
COUNT_N_FLOAT = '1.5'
COUNT_N_TEXT = 'abc'
COUNT_N_SPECIAL = '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


#------------------------------------------------------------------------
# common functions, used in tests


def get_price(some_text):
    """ This functions attempts to convert price """

    price = 0
    try:
        price = float(some_text.split('р')[0].replace(' ', ''))
    except:
        # nothing to do, returning 0
        pass

    return price


def prepare_basket(page):
    """ Prepare basket for tests """
    # adding one item
    page.add_to_cart_button_main.scroll_to_element()
    time.sleep(3)
    page.add_to_cart_button_main.wait_to_be_clickable(3)
    page.add_to_cart_button_main.scroll_to_element()
    page.add_to_cart_button_main.click()
    time.sleep(1)
    # checking result in basket page
    page.get(URL_MAIN+URL_BASKET)
    bb_count = get_price(page.bb_count.get_text())

    assert bb_count == 1, f'Precondition error. {bb_count} in basket, but 1 expected'

    return page


def prec_basket_cook(page):
    """ for fast testing only / not reliable / cart stored on server """

    page.get(URL_MAIN + URL_BASKET)
    page.load_cookies()
    page.wait_page_loaded()

    return page