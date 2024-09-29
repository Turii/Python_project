from pages.base_page import BasePage
from selenium.webdriver.common.by import By
# from data.ui_urls import UiUrls
import time


# driver = webdriver.Chrome()

class TestLogout(BasePage):

    def test_login_form(self, driver):
        driver.get("https://www.saucedemo.com/")

        username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
        username_field.send_keys("standard_user")

        password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
        password_field.send_keys("secret_sauce")

        login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
        login_button.click()

    time.sleep(5)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


def test_add_product(driver):
    driver.get("https://www.saucedemo.com/")
    urlbefore = driver.current_url

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    burger_menu = driver.find_element((By.ID, "react-burger-menu-btn"))
    burger_menu.click()
    logout = driver.find_element(By.ID, "logout_sidebar_link")
    logout.click()

    urlafter = driver.current_url

    assert urlbefore == urlafter
