"""
main page
"Эльдорадо"
"""
import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements
from pages.variables import *


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = main_url

        super().__init__(web_driver, url)

    # Header elements:

    # Выберите ваш город
    header_city_select = WebElement(css_selector = "#__next div div header button")
    region_input = WebElement(css_selector = "input[name = 'region-search']")
    region_option = WebElement(css_selector = "div[role='listbox'] span")
    region_city_buttons = ManyWebElements(css_selector = "div[role='dialog'] span[role='button']")

    # "Эльдорадости"
    header_club_url = '/club/'
    header_club = WebElement(xpath = "//a[@href='"+header_club_url+"']")


    # "Магазины"
    header_shops_url = '/info/shops/'
    header_shops = WebElement(xpath = "//a[@href='"+header_shops_url+"']")


    # "Пункты выдачи"
    header_pvz_url = '/info/pvz/11324/'
    header_pvz = WebElement(xpath = "//a[@href='"+header_pvz_url+"']")


    # "Статус заказа"
    header_orders_url = '/personal/orders/'
    header_orders = WebElement(xpath = "//a[@href='"+header_orders_url+"']")
    # "Статус заказа" form elements
    orders_form_submit_button = WebElement(css_selector = 'form > button[type="submit"]')


    # "Эльдоблог"
    header_blog_url = 'https://blog.eldorado.ru/'
    header_blog = WebElement(xpath = "//a[@href='"+header_blog_url+"']")


    # "Для бизнеса"
    header_b2b_url = '/b2b/'
    header_b2b = WebElement(xpath = "//a[@href='"+header_b2b_url+"']")


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


    # "Корзина
    header_basket_url = '/personal/basket.php'
    header_basket_button = WebElement(xpath = "//a[@href='"+header_basket_url+"']")





    # Search button
    search_run_button = WebElement(xpath='//button[@type="submit"]')

    # Titles of the products in search results
    products_titles = ManyWebElements(xpath='//a[contains(@href, "/product-") and @title!=""]')

    # Button to sort products by price
    sort_products_by_price = WebElement(css_selector='button[data-autotest-id="dprice"]')

    # Prices of the products in search results
    products_prices = ManyWebElements(xpath='//div[@class="_3NaXx _33ZFz _2m5MZ"]//span/*[1]')
#     (xpath='//div[@data-zone-name="price"]//span/*[1]')
