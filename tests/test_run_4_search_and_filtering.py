"""
These test cases check the search and filtering on the site.

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

import time
import pytest
from pages.eldorado_page import *
from pages.helpers import *


# Search input tests

def test_search_positive(web_browser):
    """ Check the search for a real product. """

    page = MainPage(web_browser)
    # Removing city select popup
    select_city(page)

    # Searching item
    page.header_search_input.click()
    page.header_search_input.wait_to_be_clickable(5)
    page.header_search_input = SEARCH_ITEM_3
    page.header_search_button.wait_to_be_clickable(5)
    page.header_search_button.click()
    page.wait_page_loaded()

    # Verify that user can see the list of products:
    assert page.search_result_products.count() > 0, 'Search results are empty'

    # Make sure user found the relevant products
    for item in page.search_result_products.get_text():
        msg = 'Wrong product in search "{}"'.format(item)
        assert SEARCH_ITEM_3 in item.lower(), msg


def test_search_wrong_key_layout(web_browser):
    """ Check the search for a product taped with wrong key layout. """

    page = MainPage(web_browser)
    # Removing city select popup
    select_city(page)

    # Searching item
    page.header_search_input.click()
    page.header_search_input.wait_to_be_clickable(5)
    page.header_search_input = SEARCH_ITEM_4_eng
    page.header_search_button.wait_to_be_clickable(5)
    page.header_search_button.click()
    page.wait_page_loaded()

    # Verify that user can see the list of products:
    assert page.search_result_products.count() > 0, 'Search results are empty'

    # Make sure user found the relevant products and request fixed
    for item in page.search_result_products.get_text():
        msg = 'Wrong product in search "{}"'.format(item)
        assert SEARCH_ITEM_4 in item.lower(), msg


def test_search_suggestion(web_browser):
    """ Check the search suggestion functionality. """

    page = MainPage(web_browser)
    # Removing city select popup
    select_city(page)


    # searching first item
    page.header_search_input.click()
    page.header_search_input.wait_to_be_clickable()
    page.header_search_input = SEARCH_ITEM_1_SUG

    # Suggested item showing and clickable
    page.header_search_item_1.wait_to_be_clickable()
    page.header_search_item_1.click()
    page.wait_page_loaded()

    # Verify that user can see the list of products:
    assert page.search_result_products.count() > 0, 'Search results are empty'

    # Make sure user found the relevant products and request fixed
    for item in page.search_result_products.get_text():
        msg = 'Wrong product in search "{}"'.format(item)
        assert SEARCH_ITEM_1_SUG.lower() in item.lower(), msg


@pytest.mark.parametrize("search", [DATA_N_1,
                                    DATA_N_2,
                                    DATA_N_3],
                         ids=      [DATA_N_1,
                                    DATA_N_2,
                                    DATA_N_3])
def test_search_input_invalid_data(web_browser, search):
    """ Check the search reaction to invalid data. """

    page = MainPage(web_browser)
    # Removing city select popup
    select_city(page)

    # Searching item
    page.header_search_input.click()
    page.header_search_input.wait_to_be_clickable(5)
    page.header_search_input = search
    page.header_search_button.wait_to_be_clickable(5)
    page.header_search_button.click()
    page.wait_page_loaded()

    # Verify that page loaded and search results are empty:
    msg = 'No "'+SEARCH_EMPTY_MESSAGE+'" message on page'
    assert SEARCH_EMPTY_MESSAGE in page.main_section.get_text(), msg


# Search result sorting tests


def test_sorting_by_price(web_browser):
    """ Check sorting by price button min to max. """

    page = MainPage(web_browser)
    # preparing page for testing
    filter_preconditions(page)

    # sorting by price (from min to max)
    page.search_result_sort_price.click()
    page.wait_page_loaded()

    # checking sorted prices
    all_prices = page.search_result_prices.get_text()
    all_prices = [get_price(i) for i in all_prices]

    # Make sure products are sorted by price correctly:
    assert all_prices == sorted(all_prices), "Sort by price (min to max) doesn't work!"


def test_sorting_by_price_reverse(web_browser):
    """ Check sorting by price button max to min. """

    page = MainPage(web_browser)
    # preparing page for testing
    filter_preconditions(page)

    # sorting by price (from min to max)
    page.search_result_sort_price.click()
    time.sleep(1)
    page.search_result_sort_price.click()
    page.wait_page_loaded()

    # checking sorted prices
    all_prices = page.search_result_prices.get_text()
    all_prices = [get_price(i) for i in all_prices]

    # Make sure products are sorted by price correctly:
    assert all_prices == sorted(all_prices, reverse=True), "Sort by price (max to min) doesn't work!"


def test_sorting_by_rating(web_browser):
    """ Check sorting by rating button. """

    page = MainPage(web_browser)
    # preparing page for testing
    filter_preconditions(page)

    # sorting by rating (from max to min)
    page.search_result_sort_rating.click()
    page.wait_page_loaded()

    # checking sorted
    all_ratings = page.search_result_ratings.get_text()
    all_ratings = [get_price(i) for i in all_ratings]

    # Make sure products are sorted by rating correctly:
    assert all_ratings == sorted(all_ratings, reverse=True), "Sort by rating doesn't work!"


def test_sorting_by_review(web_browser):
    """ Check sorting by review button. """

    page = MainPage(web_browser)
    # preparing page for testing
    filter_preconditions(page)

    # sorting by review count (from max to min)
    page.search_result_sort_review.click()
    page.wait_page_loaded()

    # checking sorted
    all_reviews = page.search_result_reviews.get_text()
    all_reviews = [int(i.split()[0]) for i in all_reviews]

    # Make sure products are sorted by rating correctly:
    assert all_reviews == sorted(all_reviews, reverse=True), "Sort by review doesn't work!"


def test_sorting_by_discount(web_browser):
    """ Check sorting by discount button. """

    page = MainPage(web_browser)
    # preparing page for testing
    filter_preconditions(page)

    # sorting by discount (from max to min)
    page.search_result_sort_discount.click()
    page.wait_page_loaded()

    # checking sorted data
    all_prices_old = page.search_result_prices_old.get_text()
    all_prices_old = [get_price(i) for i in all_prices_old]

    all_prices_new = page.search_result_prices.get_text()
    all_prices_new = [get_price(i) for i in all_prices_new]

    # discount
    discount = []
    for i in range(len(all_prices_new)):
        discount.append(all_prices_old[i]-all_prices_new[i])

    # Make sure products are sorted by discount correctly:
    assert discount == sorted(discount, reverse=True), "Sort by discount doesn't work correctly!"


def test_sorting_by_date(web_browser):
    """ Check sorting by date button. """

    page = MainPage(web_browser)
    # preparing page for testing
    filter_preconditions(page)

    # sorting by date
    all_prices_1 = page.search_result_prices.get_text()
    page.search_result_sort_date.click()
    page.wait_page_loaded()

    # checking sorted (Site doesn't have such information)
    all_prices_2 = page.search_result_prices.get_text()

    assert 'sort=-date_create' in page.get_current_url(), 'Wrong URL'

    assert all_prices_1 != all_prices_2, 'Sort by date not working!'


def test_sorting_by_min_price(web_browser):
    """ Check sorting by minimum price available. """

    page = MainPage(web_browser)
    # preparing page for testing
    filter_preconditions(page)

    # finding minimum price
    price_min = page.search_result_input_min_price.get_attribute('placeholder')

    # transferring min price to max price input
    page.search_result_input_max_price.click()
    time.sleep(1)
    page.search_result_input_max_price=price_min
    time.sleep(1)
    page.search_result_input_apply_button.click()
    page.wait_page_loaded()

    # checking result
    all_prices = page.search_result_prices.get_text()

    assert len(all_prices) > 0, 'No items found'

    # Make sure products are sorted by price correctly:
    price_min = get_price(price_min)
    price = get_price(all_prices[0])

    assert price == price_min, "Sort by min price doesn't work!"


def test_sorting_by_max_price(web_browser):
    """ Check sorting by maximum price available. """

    page = MainPage(web_browser)
    # preparing page for testing
    filter_preconditions(page)

    # finding maximum price
    price_max = page.search_result_input_max_price.get_attribute('placeholder')

    # transferring max price to min price input
    page.search_result_input_min_price.click()
    time.sleep(1)
    page.search_result_input_min_price=price_max
    time.sleep(1)
    page.search_result_input_apply_button.click()
    page.wait_page_loaded()

    # checking result
    all_prices = page.search_result_prices.get_text()

    assert len(all_prices) > 0, 'No items found'

    # Make sure products are sorted by price correctly:
    price_max = get_price(price_max)
    price = get_price(all_prices[0])

    assert price == price_max, "Sort by max price doesn't work!"


def test_sorting_by_min_price_out_of_range(web_browser):
    """ Check sorting by minimum price if input is out of range. """

    page = MainPage(web_browser)
    # preparing page for testing
    filter_preconditions(page)

    # finding minimum and maximum prices
    price_min = get_price(page.search_result_input_min_price.get_attribute('placeholder'))

    # testing input with price < price_min
    price = str(price_min - 1)
    page.search_result_input_min_price.click()
    time.sleep(1)
    page.search_result_input_min_price=price
    time.sleep(1)
    page.search_result_input_apply_button.click()
    page.wait_page_loaded()

    # checking result
    price_min_new = get_price(page.search_result_input_min_price.get_attribute('placeholder'))

    assert price_min_new == price_min, 'Min price was not reset to default'


def test_sorting_by_max_price_out_of_range(web_browser):
    """ Check sorting by minimum price if input is out of range. """

    page = MainPage(web_browser)
    # preparing page for testing
    filter_preconditions(page)

    # finding minimum and maximum prices
    price_max = get_price(page.search_result_input_max_price.get_attribute('placeholder'))

    # testing input with price < price_min
    price = str(price_max + 1)
    page.search_result_input_max_price.click()
    time.sleep(1)
    page.search_result_input_max_price=price
    time.sleep(1)
    page.search_result_input_apply_button.click()
    page.wait_page_loaded()

    # checking result
    price_max_new = get_price(page.search_result_input_max_price.get_attribute('placeholder'))

    assert price_max_new == price_max, 'Max price was not reset to default'


# Search result filtering tests


def test_filtering_by_vendor(web_browser):
    """ Check sorting results by checkbox. """

    page = MainPage(web_browser)
    # preparing page for testing
    filter_preconditions(page)

    # applying filter by vendor
    page.search_result_sort_vendors_btn.scroll_to_element()
    page.search_result_sort_vendors_btn.click()
    time.sleep(1)
    page.search_result_sort_vendor_1.click()
    page.wait_page_loaded()

    # checking filtered results
    assert page.search_result_products.count() > 0, 'Search results are empty'

    # Make sure user found the relevant products
    for item in page.search_result_products.get_text():
        msg = 'Wrong product in search "{}"'.format(item)
        assert SEARCH_ITEM_1_VENDOR.lower() in item.lower(), msg
