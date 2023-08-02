# BlackMantra


![Logo](bf4625564d16420f97c64d1b12e77067.webp)
![Logo](b61aa079-db46-4743-8c4b-afcf4ecda3c1.jpg)








Deploy ransomware making by IA 
Encriptador con Menú
Este es un programa en Python que ofrece funcionalidades para encriptar archivos con extensiones específicas y enviar la clave de encriptación a través del correo electrónico. Además, proporciona una interfaz gráfica simple con dos botones para realizar las acciones deseadas.

Funcionalidades
El programa proporciona las siguientes funcionalidades:

Encriptar archivos: Permite encriptar archivos con extensiones específicas. Al ejecutar la función "Test 1", se abrirá un cuadro de diálogo para que el usuario seleccione una carpeta de destino. A continuación, el programa buscará los archivos con las extensiones especificadas (por defecto, .txt y .docx) en la carpeta seleccionada y en sus subcarpetas, y procederá a encriptarlos utilizando el algoritmo Fernet de la librería cryptography. Los archivos encriptados se guardarán en la misma ubicación con una extensión ".encrypted" agregada a sus nombres.

Listar archivos encriptados: Al ejecutar la función "Test 2", el programa buscará en el directorio actual todos los archivos que tengan la extensión ".encrypted" y mostrará una ventana emergente con los nombres de dichos archivos encriptados.

Enviar clave de encriptación por correo electrónico: Antes de encriptar los archivos, el programa generará una clave de encriptación aleatoria. Luego, se enviará esta clave al correo electrónico especificado por el usuario. La función "send_key_by_email" es la responsable de enviar el correo electrónico con la clave.

Requisitos
Para ejecutar el programa, es necesario tener instaladas las siguientes librerías de Python:

tkinter: Para la creación de la interfaz gráfica.
cryptography: Para el cifrado y descifrado de archivos utilizando el algoritmo Fernet.
smtplib: Para enviar correos electrónicos.
email: Para crear el mensaje de correo electrónico.
os: Para acceder a la estructura de directorios del sistema.
Instrucciones de Uso
Ejecuta el programa utilizando Python. Al abrirse la ventana, verás dos botones: "Test 1" y "Test 2".

Test 1 - Encriptar archivos: Al hacer clic en este botón, se abrirá un cuadro de diálogo para seleccionar una carpeta. Asegúrate de elegir una carpeta que contenga los archivos que deseas encriptar. El programa buscará todos los archivos con extensiones especificadas en la lista extensions_to_encrypt (por defecto, .txt y .docx) dentro de la carpeta seleccionada y sus subcarpetas. Luego, los encriptará y los guardará en la misma ubicación con la extensión ".encrypted" agregada a sus nombres.

Test 2 - Listar archivos encriptados: Al hacer clic en este botón, el programa buscará en el directorio actual todos los archivos que tengan la extensión ".encrypted". Si encuentra archivos encriptados, mostrará una ventana emergente con los nombres de dichos archivos.

Enviar clave por correo electrónico: Antes de encriptar los archivos, el programa generará una clave de encriptación aleatoria. Esta clave se enviará al correo electrónico que especifiques. Para ello, debes modificar la función send_key_by_email(sender_email, sender_password, receiver_email, key) para que utilice tus credenciales de correo electrónico y las del destinatario.

Advertencia
La encriptación y seguridad de archivos es un tema delicado. Este programa solo tiene fines educativos y no debe usarse para actividades ilegales o maliciosas. No se garantiza la seguridad total de los archivos encriptados. Siempre es recomendable utilizar soluciones de encriptación profesionales y seguras para proteger datos sensibles.

Contribución
Si deseas contribuir a este proyecto, puedes hacerlo mediante la apertura de un "Issue" o enviando un "Pull Request". Se aprecian todas las contribuciones y sugerencias para mejorar el código y las funcionalidades.

Licencia
Este proyecto se distribuye bajo la Licencia MIT. Puedes consultar el archivo LICENSE para obtener más información sobre los términos y condiciones de la licencia.