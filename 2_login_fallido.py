from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    # 1. Abrir página
    driver.get("https://www.saucedemo.com/")
    
    # 2. Ingresar usuario válido pero contraseña INVÁLIDA
    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user")
    
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("clave_equivocada_123") # Contraseña incorrecta para simular el error de login
    
    # 3. Hacer clic en login
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    
    # Pausa breve para ver el error
    time.sleep(2)
    
    # 4. Encontrar el mensaje de error usando un selector CSS, esto es equivalente a hacer document.querySelector("[data-test='error']")
    error_element = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    
    # 5. Validación: Comprobar si el texto del error es el esperado
    # error_element.text extrae el texto visible dentro de la etiqueta HTML
    if "Epic sadface" in error_element.text:
        print(" ✔️ Prueba exitosa: El sistema bloqueó el acceso y mostró el error.")
    else:
        print(" ❌ Prueba fallida: El error no apareció o es diferente.")

finally:
    # Cerrar navegador
    driver.quit()