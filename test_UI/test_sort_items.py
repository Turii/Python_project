import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from data.url import Urls

driver = webdriver.Chrome()


@pytest.fixture
def login_user():
    return Urls.login_url


expexted_items = [
    {"item_name": "Sauce Labs Onesie", "item_price": 7.99},
    {"item_name": "Test.allTheThings() T-Shirt (Red)", "item_price": 15.99},
    {"item_name": "Sauce Labs Fleece Jacket", "item_price": 49.99},
    {"item_name": "Sauce Labs Bolt T-Shirt", "item_price": 15.99},
    {"item_name": "Sauce Labs Bike Light", "item_price": 9.99},
    {"item_name": "Sauce Labs Backpack", "item_price": 29.99},
]


# Авторизация
#
# Авторизация используя корректные данные (standard_user, secret_sauce)
# Авторизация используя некорректные данные (user, user)
# Корзина
#
# Добавление товара в корзину через каталог
# Удаление товара из корзины через корзину
# Добавление товара в корзину из карточки товара
# Удаление товара из корзины через карточку товара
# Карточка товара
#
# Успешный переход к карточке товара после клика на картинку товара
# Успешный переход к карточке товара после клика на название товара
# Оформление заказа
#
# Оформление заказа используя корректные данные
# Фильтр
#
# Проверка работоспособности фильтра (A to Z)
# Проверка работоспособности фильтра (Z to A)
# Проверка работоспособности фильтра (low to high)
# Проверка работоспособности фильтра (high to low)
# Бургер меню
#
# Выход из системы
# Проверка работоспособности кнопки "About" в меню
# Проверка работоспособности кнопки "Reset App State"


def test_sortAZ(login_user):
    driver.get(login_user)

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    current_selection = driver.find_element(By.CSS_SELECTOR, ".active_option").text
    if (current_selection == "Name (A to Z)"):
        products_items_main_page = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item_name']")
        products_items_name_main_page = [item_name.text for item_name in products_items_main_page]
        time.sleep(5)
        print("Currrrrrrentt list")
        print(products_items_name_main_page)
        sorted_expexted_items = sorted(expexted_items, key=lambda x: x["item_name"])
        print("sssssssorted")
        print(sorted_expexted_items)
        expected_names = [item["item_name"] for item in sorted_expexted_items]
        assert products_items_name_main_page == expected_names, f"Expected names: {expected_names}, but got: {products_items_name_main_page}"
    else:
        dropdown = Select(driver.find_element(By.CSS_SELECTOR, ".product_sort_container"))
        dropdown.select_by_visible_text("Name (A to Z)")
        products_items_main_page = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item_name']")
        products_items_name_main_page = [item_name.text for item_name in products_items_main_page]
        time.sleep(5)
        print("Currrrrrrentt list")
        print(products_items_name_main_page)
        sorted_expexted_items = sorted(expexted_items, key=lambda x: x["item_name"])
        print("sssssssorted")
        print(sorted_expexted_items)
        expected_names = [item["item_name"] for item in sorted_expexted_items]

        assert products_items_name_main_page == expected_names, f"Expected names: {expected_names}, but got: {products_items_name_main_page}"

    driver.quit()


def test_sort_low_high(login_user):
    driver.get(login_user)

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    current_selection = driver.find_element(By.CSS_SELECTOR, ".active_option").text
    if (current_selection == "Price (low to high)"):
        products_prices_main_page = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item_price']")
        # products_prices_value_main_page = [item_price.text for item_price in products_prices_main_page]
        products_prices_value_main_page = [float(item_price.text[1:]) for item_price in products_prices_main_page]
        time.sleep(5)
        print("Currrrrrrentt list")
        print(products_prices_main_page)
        sorted_expexted_prices = sorted(expexted_items, key=lambda x: x["item_price"])
        print("sssssssorted")
        print(sorted_expexted_prices)
        expected_prices = [item["item_price"] for item in sorted_expexted_prices]
        assert products_prices_value_main_page == expected_prices, f"Expected names: {expected_prices}, but got: {products_prices_value_main_page}"
    else:
        dropdown = Select(driver.find_element(By.CSS_SELECTOR, ".product_sort_container"))
        dropdown.select_by_visible_text("Price (low to high)")
        products_prices_main_page = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item_price']")
        # products_prices_value_main_page = [item_price.text for item_price in products_prices_main_page]
        products_prices_value_main_page = [float(item_price.text[1:]) for item_price in products_prices_main_page]
        time.sleep(5)
        print("Currrrrrrentt list")
        print(products_prices_main_page)
        sorted_expexted_prices = sorted(expexted_items, key=lambda x: x["item_price"])
        print("sssssssorted")
        print(sorted_expexted_prices)
        expected_prices = [item["item_price"] for item in sorted_expexted_prices]
        assert products_prices_value_main_page == expected_prices, f"Expected names: {expected_prices}, but got: {products_prices_value_main_page}"

    driver.quit()
