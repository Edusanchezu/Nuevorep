import tkinter as tk
from tkinter import messagebox

# Función para agregar números y operadores
def agregar(valor):
    pantalla.insert(tk.END, valor)

# Función para limpiar la pantalla
def limpiar():
    pantalla.delete(0, tk.END)

# Función para calcular resultado
def calcular():
    try:
        operacion = pantalla.get()
        resultado = eval(operacion)

        historial.insert(tk.END, f"{operacion} = {resultado}")

        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))

    except:
        messagebox.showerror("Error", "Operación no válida")
        limpiar()

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora con Historial")
ventana.geometry("400x500")
ventana.resizable(False, False)

# Pantalla
pantalla = tk.Entry(ventana, font=("Arial", 18), justify="right")
pantalla.pack(fill="x", padx=10, pady=10)

# Frame de botones
frame_botones = tk.Frame(ventana)
frame_botones.pack()

botones = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

fila = 0
columna = 0

for boton in botones:
    if boton == "=":
        comando = calcular
    else:
        comando = lambda x=boton: agregar(x)

    tk.Button(
        frame_botones,
        text=boton,
        width=8,
        height=3,
        command=comando
    ).grid(row=fila, column=columna)

    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Botón limpiar
tk.Button(
    ventana,
    text="Limpiar",
    width=35,
    height=2,
    bg="lightcoral",
    command=limpiar
).pack(pady=10)

# Historial
tk.Label(
    ventana,
    text="Historial de operaciones",
    font=("Arial", 12, "bold")
).pack()

historial = tk.Listbox(ventana, height=10)
historial.pack(fill="both", expand=True, padx=10, pady=10)

ventana.mainloop()