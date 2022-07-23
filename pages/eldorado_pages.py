"""
main page
"Эльдорадо"
"""
import os, pickle
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements
from pages.variables import *


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = main_url

        super().__init__(web_driver, url)

    def save_cookies(self):
        with open('test_cookies.tmp', 'wb') as cookies:
            pickle.dump(self._web_driver.get_cookies(), cookies)


    # Header elements:

    # "Выберите ваш город"
    header_city_popup = WebElement(xpath = "//button[normalize-space(.)='Да, верно']")
    header_city_select = WebElement(css_selector = "#__next div div header button")
    region_input = WebElement(css_selector = "input[name = 'region-search']")
    region_option = WebElement(css_selector = "div[role='listbox'] span")
    region_city_buttons = ManyWebElements(css_selector = "div[role='dialog'] span[role='button']")

    # "Эльдорадости"
    header_club = WebElement(xpath = "//a[@href='"+club_url+"']")

    # "Магазины"
    header_shops = WebElement(xpath = "//a[@href='"+shops_url+"']")

    # "Пункты выдачи"
    header_pvz = WebElement(xpath = "//a[@href='"+pvz_url+"']")

    # "Статус заказа"
    header_orders = WebElement(xpath = "//a[@href='"+orders_url+"']")

    # "Статус заказа" form elements
    orders_form_input_order = WebElement(css_selector = 'form input[name="name"]')
    orders_form_input_phone = WebElement(css_selector = 'form div:nth-child(3) input')
    orders_form_submit_button = WebElement(css_selector = 'form > button[type="submit"]')
    orders_form_messages = ManyWebElements(css_selector = 'div[role="dialog"] form div span')

    # "Эльдоблог"
    header_blog = WebElement(xpath = "//a[@href='"+blog_url+"']")

    # "Для бизнеса"
    header_b2b = WebElement(xpath = "//a[@href='"+b2b_url+"']")

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
    header_search_item_1 = WebElement(xpath = "//a[normalize-space(.)='"+search_item_1+"']")
    header_search_item_2 = WebElement(xpath = "//a[normalize-space(.)='"+search_item_2+"']")


    # "Корзина"
    header_basket_button = WebElement(xpath = "//a[@href='"+basket_url+"']")
    cart_counter = WebElement(xpath = "//span[@data-dy='header-cart-counter']")
    cart_total = WebElement(xpath = "//span[@data-dy='header-cart-counter']/..")

    add_to_cart_button = WebElement(xpath = "//button[normalize-space(.)='Добавить в корзину']")
    add_to_cart_price = WebElement(css_selector = 'span[data-pc="offer_price"]')


class BasketPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = main_url+basket_url

        super().__init__(web_driver, url)

        # load cookies, if possible
        try:
            with open('test_cookies.tmp', 'rb') as cookiesfile:
                cookies = pickle.load(cookiesfile)
                for cookie in cookies:
                    web_driver.add_cookie(cookie)
                web_driver.refresh();

        except:
            pass


    # Header elements: