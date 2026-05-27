from selenium import webdriver
from selenium.webdriver.common.by import By

import time;
#A - Preparar
driver = webdriver.Chrome()
driver.get("https://yaelcabrera03.github.io/IS2026-2-Sistema-de-biciestacionamiento-/index.html")


#A - Ejecutar
campos = driver.find_elements(By.CLASS_NAME, "entradaTexto")
campos[0].send_keys("estudiante@gmail.com")
campos[1].send_keys("123456")
driver.find_element(By.ID,"btnIngresar").click();

time.sleep(10)

#A - verificar

assert "principal.html" in driver.current_url
print("El sistema cargó correctamente")


# limpiar
driver.quit()
