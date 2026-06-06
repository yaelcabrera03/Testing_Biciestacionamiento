from selenium import webdriver
import time;
#A - Preparar
driver = webdriver.Chrome()


#A - Ejecutar
driver.get("https://yaelcabrera03.github.io/IS2026-2-Sistema-de-biciestacionamiento-/index.html")
time.sleep(10)

#A - verificar

assert "PIMAC" in driver.title
print("El sistema cargó correctamente")
print("Titulo: ".driver.title)

# limpiar
driver.quit()

