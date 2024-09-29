from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step('Open a browser')
    def open_browser(self):
        self.driver.get(self.url)


    def login_user(self, locator):
        self.driver.get(self.url)
        username_field = self.driver.find_element(By.XPATH, '//input[@data-test="username"]')
        username_field.send_keys("standard_user")

        password_field = self.driver.find_element(By.XPATH, '//input[@data-test="password"]')
        password_field.send_keys("secret_sauce")

        login_button = self.driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
        login_button.click()




