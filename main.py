import tkinter as tk
import threading
from laberinto1 import nivel_1
from timer_global import iniciar_temporizador

# -------------------- PYGAME --------------------
juego_abierto=False
def iniciar_juego():
    global juego_abierto
    iniciar_temporizador()

    # Si ya está abierto, no permitir abrir otra ventana
    if juego_abierto:
        print("El juego ya está en ejecución.")
        return

    juego_abierto = True  # Bloquea nuevas aperturas

    def ejecutar():
        global juego_abierto

        # Nivel 1
        resultado = nivel_1()
        print("Resultado Nivel 1:", resultado)

        # Nivel 2
        if resultado == "completado":
            print("Iniciando Nivel 2...")
            from laberinto2 import nivel_2
            resultado = nivel_2()
            print("Resultado Nivel 2:", resultado)

        # Nivel 3
        if resultado == "completado":
            print("Iniciando Nivel 3...")
            from laberinto3 import nivel_3
            resultado = nivel_3()
            print("Resultado Nivel 3:", resultado)

        # Nivel 4
        if resultado == "completado":
            print("Iniciando Nivel 4...")
            from laberinto4 import nivel_4
            resultado = nivel_4()
            print("Resultado Nivel 4:", resultado)

        juego_abierto = False

    # Hilo para que Pygame no bloquee Tkinter
    hilo = threading.Thread(target=ejecutar)
    hilo.daemon = True
    hilo.start()


# -------------------- TKINTER --------------------
root = tk.Tk()
root.title("Menú Principal - Juego de Laberintos")
root.geometry("600x400")
root.resizable(False,False)

# Crear frames
menu_frame = tk.Frame(root)
menu_frame.place(relwidth=1, relheight=1)

instrucciones_frame = tk.Frame(root)
instrucciones_frame.place(relwidth=1, relheight=1)

creditos_frame = tk.Frame(root)
creditos_frame.place(relwidth=1, relheight=1)


# -------------------- MENU PRINCIPAL --------------------
tk.Label(menu_frame, text="🧠 JUEGO DE LABERINTOS 🧠", font=("Arial", 24, "bold")).pack(pady=40)

tk.Button(menu_frame, text="Iniciar Juego", command=iniciar_juego).pack(pady=10)
tk.Button(menu_frame, text="Instrucciones", command=lambda: instrucciones_frame.tkraise()).pack(pady=10)
tk.Button(menu_frame, text="Créditos", command=lambda: creditos_frame.tkraise()).pack(pady=10)
tk.Button(menu_frame, text="Salir", command=root.destroy).pack(pady=10)

# -------------------- INSTRUCCIONES --------------------
tk.Label(instrucciones_frame, text="📘 INSTRUCCIONES", font=("Arial", 20, "bold")).pack(pady=20)

texto_instr = (
    "1. Presiona 'Iniciar Juego' para comenzar.\n"
    "2. Soluciona los laberintos antes de que se acabe el tiempo,\nllegando a la casilla verde\n"
    "3. Algunos niveles tendran puertas (casillas rojas)\nque unicamente se abriran con llaves (casillas amarillas)\n"
    "4. El nivel final tendra unos enemigos que te persiguen,\nsi llegan a tocarte te devolveran al inicio del nivel\ny perderas 10 segundos.\n"
    "5. Espero disfrutes el juego :D"
)

tk.Label(instrucciones_frame, text=texto_instr, font=("Arial", 12)).pack(pady=20)

tk.Button(instrucciones_frame, text="Volver al Menú", command=lambda: menu_frame.tkraise()).pack(pady=20)

# -------------------- CREDITOS --------------------
tk.Label(creditos_frame, text="👑 CRÉDITOS", font=("Arial", 20, "bold")).pack(pady=20)

tk.Label(creditos_frame, text="Juego creado por Miguel Silva\n2025", font=("Arial", 14)).pack(pady=20)

tk.Button(creditos_frame, text="Volver al Menú", command=lambda: menu_frame.tkraise()).pack(pady=20)

# Mostrar pantalla inicial
menu_frame.tkraise()

# Iniciar Tkinter
root.mainloop()