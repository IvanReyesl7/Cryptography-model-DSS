import tkinter as tk
from tkinter import filedialog, messagebox
import random
import hashlib

# Generar numeros primos 

x = random.getrandbits(16) | 1
y = random.getrandbits(16) | 1
semilla = random.getrandbits(32)

# Numero de llaves a crear

n = 5

# Scrambled Funcion

def fs(x,y):
    return hashlib.sha256((str(x) + str(semilla).encode()).hexdigest())

# generation funcion 

def fg(x,y):
    return

# mutation function

def fm(x,y):
    return

def generar_tabla_claves(X, Y, Semilla, num_llaves):
    tabla_llaves = []
    for _ in range(num_llaves):
        P0 = fs(X, S)       
        clave = fg(P0, Y)   
        tabla_llaves.append(clave)
        S = fm(Semilla, Y)
    return tabla_llaves

generar_tabla_claves(x, y, semilla, n)


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
ventana.title("Encriptar Texto")
ventana.geometry("400x300")

# tamaño de la ventana 
ventana.minsize(300, 200) 
ventana.maxsize(800, 600)  

# Área de texto
entrada_texto = tk.Text(ventana, height=10, width=40)
entrada_texto.pack(pady=10)

# Botón
boton_encriptar = tk.Button(ventana, text="encriptar", command=guardar_texto)
boton_encriptar.pack()

ventana.mainloop()