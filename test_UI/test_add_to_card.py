import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from data.url import Urls

driver = webdriver.Chrome()


@pytest.fixture
def login_user():
    return Urls.login_url


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

def test_corect_login(login_user):
    driver.get(login_user)

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(5)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    driver.quit()


def test_incorect_login(login_user):
    driver.get(login_user)

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("user")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(5)
    error_message_element = driver.find_element(By.XPATH, '//h3[@data-test="error"]').text

    assert driver.current_url == "https://www.saucedemo.com/"
    assert error_message_element == "Epic sadface: Username and password do not match any user in this service"

    driver.quit()


def test_add_product(login_user):
    driver.get(login_user)

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item = driver.find_element(By.CSS_SELECTOR, 'a[id = "item_4_title_link"]').text

    assert item == "Sauce Labs Backpack"

    add_item = driver.find_element(By.XPATH, "//button[@class = 'btn btn_primary btn_small btn_inventory']")
    add_item.click()
    time.sleep(5)
    added_element = driver.find_element(By.XPATH,
                                        '//div[@class = "inventory_item_description"]//button[@class = "btn btn_secondary btn_small btn_inventory"]').text

    assert added_element == "Remove"

    shoping_cart = driver.find_element(By.XPATH,
                                       "//a[@class = 'shopping_cart_link']/span[@class = 'shopping_cart_badge']")

    assert shoping_cart.text == "1"

    shoping_cart.click()
    item_name_elements = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item_name']")
    cart_items_name = [cart_item.text for cart_item in item_name_elements]
    assert item in cart_items_name
    assert cart_items_name[0] == item, f"Expected item: {item}, but found: {cart_items_name[0]}"

    assert len(cart_items_name) == 1, f"Expected 1 item in the cart, but found {len(cart_items_name)}"
    time.sleep(5)

    remove_button = driver.find_element(By.XPATH, "//button[@class = 'btn btn_secondary btn_small cart_button']")
    remove_button.click()
    item_name_elements = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item_name']")
    cart_items_name = [cart_item.text for cart_item in item_name_elements]

    assert item not in cart_items_name, f"Item '{item}' should nott be in the cart but it is"

    time.sleep(5)
    driver.quit()
