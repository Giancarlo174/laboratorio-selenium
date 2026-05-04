from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        
        # 1. Localizadores de esta página
        self.inventario_container_locator = (By.ID, "inventory_container")
        self.btn_mochila_locator = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.carrito_badge_locator = (By.CLASS_NAME, "shopping_cart_badge")

    # 2. Acción: Esperar a que cargue la página
    def esperar_carga(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.inventario_container_locator))

    # 3. Acción: Hacer clic en el botón de la mochila
    def agregar_mochila(self):
        self.driver.find_element(*self.btn_mochila_locator).click()

    # 4. Acción: Leer el número que tiene el carrito y devolverlo
    def obtener_cantidad_carrito(self):
        badge = self.driver.find_element(*self.carrito_badge_locator)
        return badge.text