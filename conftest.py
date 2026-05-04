import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options # Importación necesaria para el modo headless[cite: 10]
import pytest_html 

# Este es el hook que atrapa los resultados de las pruebas
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Captura de pantalla automática en caso de fallo"""
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extra", [])
    
    if report.when == "call" and report.failed:
        # Acceder al driver desde la fixture
        driver = item.funcargs['driver']
        
        # Convertir la captura a base64 para el reporte HTML
        screenshot = driver.get_screenshot_as_base64()
        html = f'<div><img src="data:image/png;base64,{screenshot}" alt="screenshot" style="width:304px;height:228px;" onclick="window.open(this.src)" align="right"/></div>'
        extras.append(pytest_html.extras.html(html))
        
    report.extra = extras

# Fixture del navegador
@pytest.fixture
def driver():
    """Fixture del navegador configurado para CI/CD"""
    options = Options()[cite: 10]
    options.add_argument("--headless") # Ejecución sin ventana visual[cite: 10]
    options.add_argument("--no-sandbox")[cite: 10]
    options.add_argument("--disable-dev-shm-usage")[cite: 10]
    
    driver = webdriver.Chrome(options=options)[cite: 10]
    driver.maximize_window()
    yield driver  # Aquí es donde se ejecutan las pruebas
    driver.quit() # Esto se ejecuta al terminar, pase lo que pase