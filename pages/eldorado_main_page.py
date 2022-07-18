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

    # "Эльдорадости"
    header_club_url = '/club/'
    header_club = WebElement(xpath="//a[@href='"+header_club_url+"']")

    # "Магазины"
    header_shops_url = '/info/shops/'
    header_shops = WebElement(xpath="//a[@href='"+header_shops_url+"']")

    # "Пункты выдачи"
    header_pvz_url = '/info/pvz/11324/'
    header_pvz = WebElement(xpath="//a[@href='"+header_pvz_url+"']")








    # Search button
    search_run_button = WebElement(xpath='//button[@type="submit"]')

    # Titles of the products in search results
    products_titles = ManyWebElements(xpath='//a[contains(@href, "/product-") and @title!=""]')

    # Button to sort products by price
    sort_products_by_price = WebElement(css_selector='button[data-autotest-id="dprice"]')

    # Prices of the products in search results
    products_prices = ManyWebElements(xpath='//div[@class="_3NaXx _33ZFz _2m5MZ"]//span/*[1]')
#     (xpath='//div[@data-zone-name="price"]//span/*[1]')
