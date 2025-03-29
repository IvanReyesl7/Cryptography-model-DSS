import tkinter as tk
from tkinter import filedialog, messagebox
import random
import hashlib

# Generar y comprobrar numeros primos 

def if_primo(n):
    
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        if n % p == 0:
            return n == p
    return True

def generar_primo(bits):
    
    while True:
        num = random.getrandbits(bits)
        if if_primo(num):
            return num


def guardar_texto():
    texto = entrada_texto.get("1.0", tk.END).strip()  # Obtiene el texto
    if not texto:
        messagebox.showwarning("Error", "No hay ningun mensaje para encriptar.")
        return

    # donde se guardara el archivo
    archivo_ruta = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")],
        title="Guardar como"
    )
    
    if archivo_ruta:  
        with open(archivo_ruta, "w", encoding="utf-8") as archivo:
            archivo.write(texto)
        messagebox.showinfo("Éxito", f"¡Archivo guardado en:\n{archivo_ruta}")




# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Guardar Texto")
ventana.geometry("400x300")

# tamaño de la ventana 
ventana.minsize(300, 200) 
ventana.maxsize(800, 600)  

# Área de texto
entrada_texto = tk.Text(ventana, height=10, width=40)
entrada_texto.pack(pady=10)

# Botón
boton_texto = tk.Button(ventana, text="Selecionar texto", command=guardar_texto)
boton_texto.pack()

boton_llave = tk.Button(ventana, text="Seleccionar llave", command=guardar_texto)
boton_llave.pack()

boton_desencriptar = tk.Button(ventana, text="Desencriptar", command=guardar_texto)
boton_desencriptar.pack()

ventana.mainloop()