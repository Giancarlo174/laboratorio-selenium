from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # Volvemos a importar time para nuestra pausa visual

driver = webdriver.Chrome()

try:
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "inventory_container")))
    
    btn_agregar = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    btn_agregar.click()
    
    carrito_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    
    if carrito_badge.text == "1":
        print(" ✔️ Prueba exitosa: Producto agregado y el carrito muestra 1.")
    else:
        print(" ❌ Prueba fallida: El carrito no muestra la cantidad correcta.")

    # Congelamos la pantalla 4 segundos para poder verlo
    time.sleep(4)

finally:
    driver.quit()