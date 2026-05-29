# Sistema de biciestacionamiento 
* Software para gestionar un estacionamiento de bicicletas y de motos.
- Existen tres tipos de usuarios. Administradores, estudiantes y empleados.
- Los administradores podran gestionar el acceso y lugares disponibles, y los estudiantes y empleados tendran que registrarse para tener acceso al estacionamiento. 
---
## Tecnologías utilizadas
### Sistema Biciestacionamiento 
- HTML, CSS y JavaScript para el desarrollo de la interfaz del sistema.
- Supabase para la gestión de registros y datos.
### Testing 
- Selenium con Python para pruebas automatizadas en navegador.
- Uso de librerías pytest, selenium.webdriver y selenium.webdriver.common.by.
---
## Instalación
### Sistema Biciestacionamiento 
* No se requiere instalación.
- Para utilizar el sistema, únicamente es necesario acceder a la siguiente URL:
https://yaelcabrera03.github.io/IS2026-2-Sistema-de-biciestacionamiento-/index.html
### Testing 
- Instalar Phyton -> Importante que esté seleccionado el “pip”
- Instalar Selenium 
- Instalar Pytest
---
## Ejecutar sistema
### Sistema Biciestacionamiento 
1. Paso 1: Abrir el enlace del sistema en cualquier navegador web.
2. Paso 2: Iniciar sesión o registrarse para acceder a las funcionalidades del sistema.
3. Paso 3: Utilizar las opciones disponibles dentro de la plataforma. 
### Testing 
1. Para "test_carga.py", "test_login_correcto.py" y "test_login_incorrecto.py" es suficente con correr el codigo desde el boton run.<br>
2. Para "test_pytest.py" Es necesario desde la terminal<br>
&nbsp;&nbsp;&nbsp;&nbsp;2.1. Paso 1: Colocarnos en la carpta en la que se encuentra el archivo
-     cd test
  
&nbsp;&nbsp;&nbsp;&nbsp; 2.2. Paso 2: Ejecutamos con:
-     pytest test_pytest.py
  
## Uso del sistema
Para ingresar al sistema, necesitas registrarte o iniciar sesión. Los administradores podrán gestionar todo lo relacionado con el estacionamiento; esto incluye visualizar la información de los usuarios y manipular su estado en el sistema. Los estudiantes y empleados podrán darse de alta y cambiar su información personal. También contarán con una ventana de ayuda para que puedan familiarizarse con el sistema. Cualquier tipo de usuario podrá ver los lugares disponibles y ocupados en el estacionamiento.

---
## Funcionalidades principales
### Sistema Biciestacionamiento 
- Login: Registro y inicio de seción en el sistema.
- Gestionar: Para administradores.
- Mi cuenta: Editar información personal, vehiculo y preferencias.
- Ayuda: Preguntas frecuentes o contactar al equipo de apoyo.
- Cerrar seción: Salir del sistema
### Testing 
- Probar que el sistema abra correctamente.
- Probar que se inicie secion con login correcto.
- Probar que no se inicie secion con login incorrecto.
- Tomar captura de pantalla al loguear para ver resultado.
---
## Evidencias
### Sistema Biciestacionamiento 
- Los logs se guardan en supbase
  
### Testing 
- Capturas de pantalla generadas por "test_pytest.py" se almacenan en la carpeta 'evidencias'

---
## Estructura del proyecto
### Sistema Biciestacionamiento 
Sistema-de-biciestacionamiento/<br>
│<br>
├── assets/<br>
├── css/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├──STYLE.CSS<br>
├──js/<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├──script.js<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├──script_registro.js<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├──scritp_cuenta.js<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├──supabase.js<br>
├── pages/<br>
├── README.md<br>
└── index.html<br>

---
## Notas adicionales
Todavia no acabamos el proyecto :P
