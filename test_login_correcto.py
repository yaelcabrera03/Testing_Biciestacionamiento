from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import Keys
import time;
#A - Preparar
driver = webdriver.Chrome()
driver.get("https://yaelcabrera03.github.io/IS2026-2-Sistema-de-biciestacionamiento-/index.html")


#A - Ejecutar
campos = driver.find_elements(By.CLASS_NAME, "entradaTexto")

#campos[0].send_keys("")
#campos[1].send_keys("")
driver.find_element(By.ID,"btnIngresar").click();

time.sleep(10)

#A - verificar

assert "Login" in driver.title
print("El sistema cargó correctamente")
print("Titulo: ".driver.title)

# limpiar
driver.quit()
