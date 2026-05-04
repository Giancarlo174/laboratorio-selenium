from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # Nueva importación para la espera
from selenium.webdriver.support import expected_conditions as EC # Condiciones esperadas

driver = webdriver.Chrome()

try:
    driver.get("https://www.saucedemo.com/")
    
    # Login normal
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Espera explícita
    # Configuramos una espera máxima de 10 segundos
    wait = WebDriverWait(driver, 10)
    
    # Le decimos que espere HASTA que el contenedor del inventario esté presente en el DOM
    wait.until(EC.presence_of_element_located((By.ID, "inventory_container")))
    
    # Si pasa de la línea anterior sin dar error, significa que logramos entrar
    print(" ⬛   Login validado correctamente con espera explícita")

finally:
    driver.quit()