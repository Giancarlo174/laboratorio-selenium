from selenium.webdriver.common.by import By
from login_page import LoginPage
from inventory_page import InventoryPage
import time

def test_login_fallido(driver):
    driver.get("https://www.saucedemo.com/")
    
    pagina_login = LoginPage(driver)
    pagina_login.hacer_login("standard_user", "clave_equivocada_123")
    
    error_element = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert "Epic sadface" in error_element.text, "Error: El mensaje de bloqueo no apareció"

def test_flujo_completo_pom(driver):
    driver.get("https://www.saucedemo.com/")
    
    pagina_login = LoginPage(driver)
    pagina_login.hacer_login("standard_user", "secret_sauce")
    
    pagina_inventario = InventoryPage(driver)
    pagina_inventario.esperar_carga()
    pagina_inventario.agregar_mochila()
    
    cantidad_en_carrito = pagina_inventario.obtener_cantidad_carrito()
    
    # Le diremos que espere 5 productos en vez de 1 para que la prueba explote y tome foto.
    assert cantidad_en_carrito == "5", "Error intencional: El carrito no tiene 5 productos"