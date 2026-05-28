from selenium import webdriver
from selenium.webdriver.common.by import By

import time;
#A - Preparar
driver = webdriver.Chrome()
driver.get("https://yaelcabrera03.github.io/IS2026-2-Sistema-de-biciestacionamiento-/index.html")


#A - Ejecutar
campos = driver.find_elements(By.CLASS_NAME, "entradaTexto")
campos[0].send_keys("correoInvalido@gmail.com")
campos[1].send_keys("nose")
driver.find_element(By.ID,"btnIngresar").click();

time.sleep(10)
mensaje = driver.find_element(By.ID,"msjLogin").text

#A - verificar

assert mensaje == "Datos incorrectos"
print("El sistema cargó correctamente")
driver.save_screenshot("../evidencias/test_login.png")

# limpiar
driver.quit()