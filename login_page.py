from selenium.webdriver.common.by import By

class LoginPage:
    # El constructor (__init__) recibe el driver para poder controlar el navegador
    def __init__(self, driver):
        self.driver = driver
        
        # 1. Definimos los Localizadores como tuplas
        self.username_locator = (By.ID, "user-name")
        self.password_locator = (By.ID, "password")
        self.login_button_locator = (By.ID, "login-button")

    # 2. Definimos las acciones que un usuario puede hacer aquí
    def hacer_login(self, usuario, contrasena):
        # El asterisco (*) sirve para desempaquetar la tupla y pasar los dos valores al find_element
        self.driver.find_element(*self.username_locator).send_keys(usuario)
        self.driver.find_element(*self.password_locator).send_keys(contrasena)
        self.driver.find_element(*self.login_button_locator).click()