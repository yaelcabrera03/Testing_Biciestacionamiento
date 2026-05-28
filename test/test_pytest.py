import pytest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
import os 

URL = "https://yaelcabrera03.github.io/IS2026-2-Sistema-de-biciestacionamiento-/index.html"

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    yield d
    d.quit
def test_carga_pagina(driver):
    driver.get(URL)
    assert driver.title == "SISTEMA DEL BIENESTAR"
def test_login_correcto(driver):
    driver.get(URL)
    campos = driver.find_elements(By.CLASS_NAME, "entradaTexto")
    campos[0].send_keys("estudiante@gmail.com")
    campos[1].send_keys("123456")
    driver.find_element(By.ID,"btnIngresar").click();
    
    mensaje = driver.find_element(By.ID,"msjLogin").text
    time.sleep(2)
    #A - verificar
    try:
        assert "principal.html" in driver.current_url
        print("El sistema cargó correctamente")
    except:
        driver.save_screenshot("../evidencias/test_login.png")
        raise
def test_login_incorrecto(driver):
    driver.get(URL)
    campos = driver.find_elements(By.CLASS_NAME, "entradaTexto")
    campos[0].send_keys("correNoValido.com")
    campos[1].send_keys("123456")
    driver.find_element(By.ID,"btnIngresar").click()
    time.sleep(4)
    mensaje = driver.find_element(By.ID,"msjLogin").text
    
    #A - verificar
    try:
        assert mensaje ==  "Datos incorrectos"
        print("")
    except:
        os.makedirs("../evidencias",exist_ok=True)
        driver.save_screenshot("../evidencias/test_login.png")
        raise
    
    