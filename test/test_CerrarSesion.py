import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

URL = "https://yaelcabrera03.github.io/IS2026-2-Sistema-de-biciestacionamiento-/index.html"

@pytest.fixture
def driver():
    d = webdriver.Edge()
    yield d
    time.sleep(3)
    d.quit()

def test_cerrar_sesion(driver):
    # A - Preparar
    driver.get(URL)
    # A - Ejecutar login
    campos = driver.find_elements(By.CLASS_NAME, "entradaTexto")
    campos[0].send_keys("estudiante@gmail.com")
    campos[1].send_keys("123456")

    driver.find_element(By.ID, "btnIngresar").click()

    time.sleep(3)

    # A - Ejecutar cerrar sesión
    driver.find_element(By.ID, "cerrarSesion").click()
    time.sleep(3)

    # Crear carpeta de evidencias
    os.makedirs("../evidencias", exist_ok=True)

    # Tomar captura
    driver.save_screenshot("../evidencias/cerrar_sesion.png")

    # Verificar
    assert "index.html" in driver.current_url
    print("Sesión cerrada correctamente")
    
