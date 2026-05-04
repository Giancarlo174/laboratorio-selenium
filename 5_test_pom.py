from selenium import webdriver
import time

# Importamos nuestras Páginas/Clases
from login_page import LoginPage
from inventory_page import InventoryPage

driver = webdriver.Chrome()

try:
    # 1. Abrimos el navegador en la URL base
    driver.get("https://www.saucedemo.com/")
    
    # 2. Usamos la página de Login
    pagina_login = LoginPage(driver)
    pagina_login.hacer_login("standard_user", "secret_sauce")
    
    # 3. Usamos la página de Inventario
    pagina_inventario = InventoryPage(driver)
    pagina_inventario.esperar_carga()
    pagina_inventario.agregar_mochila()
    
    # 4. Validamos el resultado
    cantidad_en_carrito = pagina_inventario.obtener_cantidad_carrito()
    
    if cantidad_en_carrito == "1":
        print(" ✔️ Prueba POM exitosa: El código está completamente modularizado y funcionando.")
    else:
        print(" ❌ Prueba fallida: El carrito no muestra la cantidad correcta.")

    # Pausa para ver
    time.sleep(4)

finally:
    driver.quit()