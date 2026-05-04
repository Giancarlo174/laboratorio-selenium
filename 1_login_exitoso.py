from selenium import webdriver
from selenium.webdriver.common.by import By  # Nueva librería para buscar en el DOM
import time

driver = webdriver.Chrome()

try:
    # 1. Abrir página
    driver.get("https://www.saucedemo.com/")
    
    # 2. Encontrar el campo de usuario e ingresar el texto
    # Usamos By.ID para buscar el id="user-name" en el HTML
    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user")
    
    # 3. Encontrar el campo de contraseña e ingresar el texto
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")
    
    # 4. Encontrar el botón de login y hacer clic
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    
    # Pausa breve para dejar que la página cargue el inventario y lo veas
    time.sleep(2)
    
    # 5. Validación: Comprobar si entramos a la página correcta
    # current_url nos devuelve la URL en la que estamos parados actualmente
    if "inventory" in driver.current_url:
        print(" ⬛   Prueba exitosa: Login correcto")
    else:
        print(" +  Prueba fallida")

finally:
    # Cerrar navegador
    driver.quit()