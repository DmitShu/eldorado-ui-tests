"""

"Эльдорадо" page elements and additional functions

"""

import time
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements
from pages.helpers import *


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = URL_MAIN

        super().__init__(web_driver, url)


    #____________MAIN PAGE____________


    # "Выберите ваш город"
    header_city_popup_yes = WebElement(xpath = "//button[normalize-space(.)='Да, верно']")
    header_city_popup_no = WebElement(xpath = "//button[normalize-space(.)='Нет, другой']")
    header_city_select = WebElement(css_selector = "#__next div div header button")
    region_input = WebElement(css_selector = "input[name = 'region-search']")
    region_option = WebElement(css_selector = "div[role='listbox'] span")
    region_city_buttons = ManyWebElements(css_selector = "div[role='dialog'] span[role='button']")
    region_close_button = WebElement(css_selector = 'button[aria-label="Закрыть"]')

    region_list_1_select = WebElement(xpath = "//span[normalize-space(.)='"+REGION_LIST_1+"']")
    region_list_2_select = WebElement(xpath = "//span[normalize-space(.)='"+REGION_LIST_2+"']")
    region_list_3_select = WebElement(xpath = "//span[normalize-space(.)='"+REGION_LIST_3+"']")

    # "Эльдорадости"
    header_club = WebElement(xpath = "//a[@href='" + URL_CLUB + "']")

    # "Магазины"
    header_shops = WebElement(xpath = "//a[@href='" + URL_SHOPS + "']")

    # "Пункты выдачи"
    header_pvz = WebElement(xpath = "//a[@href='" + URL_PVZ + "']")

    # "Статус заказа"
    header_orders = WebElement(xpath = "//a[@href='" + URL_ORDERS + "']")

    # "Статус заказа" form elements
    orders_form_input_order = WebElement(css_selector = 'form input[name="name"]')
    orders_form_input_phone = WebElement(css_selector = 'form div:nth-child(3) input')
    orders_form_submit_button = WebElement(css_selector = 'form > button[type="submit"]')
    orders_form_messages = ManyWebElements(css_selector = 'div[role="dialog"] form div span')

    # "Эльдоблог"
    header_blog = WebElement(xpath = "//a[@href='" + URL_BLOG + "']")

    # "Для бизнеса"
    header_b2b = WebElement(xpath = "//a[@href='" + URL_B2B + "']")

    # "Открыть онлайн-консультант"
    header_chat_button = WebElement(css_selector = '#__next button[aria-label="Открыть онлайн-консультант"]')

    # "chat elements"
    chat_viber_button = WebElement(css_selector = '#__next a[href="viber://pa/?chatURI=eldorado_stores"]')
    chat_telegram_button = WebElement(css_selector = '#__next a[href="https://t.me/Eldorado_official_bot"]')

    # "Регистрация или вход"
    header_login_button = WebElement(xpath = "(//BUTTON[contains(text(), 'Вход')])[1]")

    # "login form"
    login_tel_input = WebElement(css_selector = 'input[inputmode="tel"]')
    login_submit_button = WebElement(xpath = "//button[normalize-space(.)='Получить код']")

    # Search-form
    header_search_input = WebElement(css_selector = 'input[name="search"]')
    header_search_button = WebElement(css_selector = 'form[id="search-form"] button[type="submit"]')

    header_search_item_1 = WebElement(xpath = "//a[normalize-space(.)='" + SEARCH_ITEM_1 + "']")
    header_search_item_2 = WebElement(xpath = "//a[normalize-space(.)='" + SEARCH_ITEM_2 + "']")

    # Search results
    search_result_products = ManyWebElements(css_selector = 'div[id="listing-container"] li[data-dy="product"]')
    search_result_prices = ManyWebElements(css_selector = 'span[data-pc="offer_price"]')
    search_result_prices_old = ManyWebElements(xpath = "//span[@data-pc='offer_price']/following-sibling::div/span")
    search_result_ratings = ManyWebElements(xpath = "//li[@data-dy='product']//div[contains(@aria-label,'Рейтинг')]//span")
    search_result_reviews = ManyWebElements(xpath = "//li[@data-dy='product']//a[@data-dy='review']")

    search_result_sort_price = WebElement(xpath = "//div[@id='listing-container']//button[normalize-space(.)='По цене']")
    search_result_sort_rating = WebElement(xpath = "//div[@id='listing-container']//button[normalize-space(.)='По рейтингу']")
    search_result_sort_review = WebElement(xpath = "//div[@id='listing-container']//button[normalize-space(.)='По отзывам']")
    search_result_sort_discount = WebElement(xpath = "//div[@id='listing-container']//button[normalize-space(.)='По размеру скидки']")
    search_result_sort_date = WebElement(xpath = "//div[@id='listing-container']//button[normalize-space(.)='По новизне']")

    search_result_sort_vendors_btn = WebElement(xpath = "(//*[contains(text(), 'Производители')]/ancestor-or-self::*/DIV[contains(text(), 'Показать')])")
    search_result_sort_vendor_1 = WebElement(css_selector = 'span[title="Bosch"]')

    # "Корзина"
    header_basket_button = WebElement(xpath = "//a[@href='" + URL_BASKET + "']")
    cart_counter = WebElement(xpath = "//span[@data-dy='header-cart-counter']")
    cart_total = WebElement(xpath = "//span[@data-dy='header-cart-counter']/..")

    add_to_cart_button_filter = WebElement(xpath = "//button[normalize-space(.)='Добавить в корзину']")
    add_to_cart_button_main = WebElement(xpath = "//div[@aria-labelledby]//button[normalize-space(.)='В корзину']")
    add_to_cart_price = WebElement(css_selector = 'span[data-pc="offer_price"]')

    basket_page_region = WebElement(css_selector = 'span.headerRegionName')

    # Main
    main_section = WebElement(css_selector = 'main')
    main_catalog_buttons = ManyWebElements(css_selector = 'ul[data-dy="catalog_menu"] li')
    main_hero_block = ManyWebElements(css_selector = 'div[data-dy="hero-block"] picture img')
    main_recommend_tabs = ManyWebElements(css_selector = 'div[role="tablist"] button')

    main_media_tube = WebElement(xpath = "//a[normalize-space(.)='ЭльдоTUBE']")
    main_media_play = WebElement(xpath = "//a[normalize-space(.)='ЭльдоPLAY']")
    main_media_blog = WebElement(xpath = "//a[normalize-space(.)='ЭльдоBLOG']")


    #____________Basket PAGE____________


    # Basket button elements
    bb_count = WebElement(css_selector = 'span[id="basketCount"]')
    bb_cost = WebElement(css_selector = 'span[id="basketCost"]')

    # basket container items
    basket_block_close_button = WebElement(css_selector = 'span.q-basketBlockClouser-button')
    basket_block_price_discount = WebElement(css_selector = 'div.price-all.w-discount')
    basket_block_spinner_right = WebElement(css_selector = 'div.qs-side-right')
    basket_block_spinner_left = WebElement(css_selector = 'div.qs-side-left')
    basket_block_spinner_input = WebElement(css_selector = 'div.qs-side-center input')
    basket_total_services_price = WebElement(css_selector = 'span[id="services_price_td"]')
    basket_services_radio = ManyWebElements(css_selector = 'label.checkboxlabel')
    basket_services_prices = ManyWebElements(css_selector = 'span.price_value')
    basket_toorders_button = WebElement(css_selector = 'div.cartTotalPart span.successBttnCP')
    basket_item_recovery_button = WebElement(xpath = "//a[normalize-space(.)='Восстановить в корзине']")
    basket_clear_button = WebElement(css_selector = 'span.q-basketBlockRowHeaderItem__clearBasketBtn')
    basket_empty_span = WebElement(css_selector = 'div.empty-basket')
    basket_retailrocket_button = WebElement(css_selector = 'div.retailrocket-item a.rr-item__actions-buy')
    basket_accessories_popup_button = WebElement(css_selector = 'button[data-popup-src="#accessories-popup"]')
    basket_services_popup_button = WebElement(css_selector = 'button[data-popup-src="#services-popup"]')
    basket_accessories_tocart_button = WebElement(css_selector = 'a.servicesItem.q-btn-to-cart')
    basket_services_tocart_button = WebElement(css_selector = 'a.servicesItem.add_services')


    #____________Order page____________


    order_total_price = WebElement(css_selector='div.rsc-price-all-value')
