"""

Contains common constants and methods, used in tests

"""

import time

#------------------------------------------------------------------------
# common constants, used in tests


#Main URL'S
URL_MAIN = 'https://www.eldorado.ru'
URL_CLUB = '/club/'
URL_SHOPS = '/info/shops/'
URL_PVZ = '/info/pvz/11324/'
URL_ORDERS = '/personal/orders/'
URL_BLOG = 'https://blog.eldorado.ru/'
URL_B2B = '/b2b/'
URL_BASKET = '/personal/basket.php'
URL_ORDER = '/personal/order_self_delivery.php'
# ЭльдоTUBE
URL_TUBE = 'https://www.youtube.com/c/eldoradovideo/videos'
# ЭльдоPLAY
URL_PLAY = 'https://blog.eldorado.ru/publications/category/eldoplay'

# холодильники
URL_CATEGORY_1 = '/c/kholodilniki'
# утюги
URL_CATEGORY_2 = '/c/utyugi'


# Region select form
CITY_P_1 = 'Ярославль'
CITY_P_1_SUGGEST = 'Яросл'
CITY_P_1_ENG = 'Zhjckfdkm'

DATA_N_1 = '123459'
DATA_N_2 = 257 * 'A'
DATA_N_3 = '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'

CITY_BAD_MESSAGE = 'Ничего не найдено'

REGION_LIST_1 = 'Сибирский ФО'
REGION_LIST_2 = 'Иркутская область'
REGION_LIST_3 = 'Иркутск'

# Header orders form
ORDER_TEL_P_1 = '9666666666'
ORDER_TEL_N_1 = '0000000000'
ORDER_P_1 = '1234567890'
ORDER_TEL_BAD_MESSAGE = 'Мобильный телефон указан некорректно'
ORDER_TEL_EMPTY = 'Мобильный телефон не указан'
ORDER_EMPTY_MSG = 'Введите номер заказа'


# Search & filters
SEARCH_ITEM_1 = 'Холодильники'
SEARCH_ITEM_1_SUG = 'холод'
SEARCH_ITEM_1_VENDOR = 'Bosch'
SEARCH_ITEM_2 = 'Утюги'
SEARCH_ITEM_3 = 'realme'
SEARCH_ITEM_4 = 'унитаз'
SEARCH_ITEM_4_eng = 'eybnfp'
SEARCH_EMPTY_MESSAGE = 'ничего не найдено'


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
# common methods, used in tests


def get_price(some_text):
    """ This functions attempts to convert price """

    price = 0
    try:
        price = int(some_text.split('р')[0].replace(' ', ''))
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


def select_city(page):
    """ Selecting city prevents popup on different pages """

    page.header_city_select.click()
    page.region_input.wait_to_be_clickable(5)
    page.region_city_buttons.find()[0].click()
    time.sleep(1)


def filter_preconditions(page):
    """ This method prepares page for filtering. """

    select_city(page)
    page.header_search_input.wait_to_be_clickable()
    page.header_search_input.click()
    page.header_search_input.wait_to_be_clickable()
    page.header_search_input = SEARCH_ITEM_1
    page.header_search_item_1.wait_to_be_clickable()
    page.header_search_item_1.click()
    page.wait_page_loaded()

    assert page.search_result_products.count() > 0, 'Preconditions fail. Nothing to filter'
