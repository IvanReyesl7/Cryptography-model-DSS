import tkinter as tk
from tkinter import filedialog, messagebox
import random
import hashlib

# Generar numeros primos 

x = random.getrandbits(16) | 1
y = random.getrandbits(16) | 1
semilla = random.getrandbits(32)

# Numero de llaves a crear

n = 10

# Scrambled Funcion

def fs(x,y):
    combinado = (str(x) + str(y)).encode()
    return int.from_bytes(hashlib.sha256(combinado).digest()[:8], byteorder='big')

# generation funcion 

def fg(x,y):
    return x ^ y
# mutation function

def fm(x,y):
    return (x * y) % (2**32)
    
#funcion que genera la tabla de claves

def generar_tabla_claves(X, Y, Semilla, num_llaves):
    tabla_llaves = []
    for _ in range(num_llaves):
        P0 = fs(X, Semilla)       
        clave = fg(P0, Y)   
        tabla_llaves.append(clave)
        Semilla = fm(Semilla, Y)
    return tabla_llaves

tabla_claves = generar_tabla_claves(x, y, semilla, n)
PSN = 4

print("=== Tabla de llaves ===")
for i, clave in enumerate(tabla_claves):
    print(f"={hex(clave)}=")
#Funcion para encriptar mensaje

def encriptar(mensaje: str, tabla_claves: list, PSN: int) -> bytes:
    clave = tabla_claves[PSN % len(tabla_claves)]
    clave_bytes = clave.to_bytes(8, byteorder='big')
    mensaje_bytes = mensaje.encode('utf-8')
    return bytes(mensaje_bytes[i] ^ clave_bytes[i % 8] for i in range(len(mensaje_bytes)))

#Funcion para desencriptar mensaje

def desencriptar(hex_str: str) -> str:
    clave = tabla_claves[PSN % len(tabla_claves)]
    clave_bytes = clave.to_bytes(8, 'big')
    bytes_encriptados = bytes.fromhex(hex_str)
    return ''.join([chr(b ^ clave_bytes[i % 8]) for i, b in enumerate(bytes_encriptados)])

# Funciones para guardar y abrir archivos

def guardar_texto():
    texto = entrada_texto.get("1.0", tk.END).strip()
    if not texto:
        messagebox.showwarning("Error", "No hay ningún mensaje para encriptar.")
        return

    # Encriptar y convertir a hexadecimal

    texto_encriptado = encriptar(texto, tabla_claves, PSN).hex()
    
    archivo_ruta = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt")],
        title="Guardar texto encriptado (hex)"
    )
    
    if archivo_ruta:
        with open(archivo_ruta, "w") as archivo:
            archivo.write(texto_encriptado)
        messagebox.showinfo("Éxito", f"¡Texto encriptado (hex) guardado en:\n{archivo_ruta}")

def abrir_encriptado():
    archivo_ruta = filedialog.askopenfilename(
        filetypes=[("Archivos de texto", "*.txt")],
        title="Abrir texto encriptado"
    )
    
    if archivo_ruta:
        with open(archivo_ruta, "r") as archivo:
            contenido = archivo.read()
        
        try:
            texto_desencriptado = desencriptar(contenido)
            messagebox.showinfo("Texto desencriptado", f"Texto desencriptado:\n{texto_desencriptado}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al desencriptar el texto:\n{str(e)}")


# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Encriptar y desencriptar texto")
ventana.geometry("400x300")

# tamaño de la ventana 
ventana.minsize(300, 200) 
ventana.maxsize(800, 600)  

# Área de texto
entrada_texto = tk.Text(ventana, height=10, width=40)
entrada_texto.pack(pady=10)

# Botón
boton_encriptar = tk.Button(text="Encriptar y Guardar", command=guardar_texto)
boton_encriptar.pack()

boton_desencriptar = tk.Button(text="Abrir y Descifrar", command=abrir_encriptado)
boton_desencriptar.pack()


ventana.mainloop()