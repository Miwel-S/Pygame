# 🎮 Laberinto con Pygame, Tkinter y Sistema de Niveles

Este proyecto es un juego de laberintos creado en **Python**, utilizando:

- **Pygame** → para la lógica del juego, movimiento, enemigos y HUD  
- **Tkinter** → para el menú principal (inicio, créditos, instrucciones)  
- **Threading** → para el temporizador global  
- **Arquitectura modular** separando cada nivel en su archivo  

Incluye un temporizador global, varios niveles, puertas, llaves, enemigos y pantallas de victoria/derrota.

---

## 🧩 Características principales

### ✔ Sistema de niveles
El juego avanza automáticamente entre niveles:
- Nivel 1 → Laberinto básico  
- Nivel 2 → Puertas y llaves  
- Nivel 3 → Mapa grande con múltiples llaves y puertas  
- Nivel 4 → Dos enemigos perseguidores, penalización de tiempo, meta protegida  

### ✔ Jugabilidad
- Movimiento con flechas del teclado  
- Llaves para abrir puertas  
- Temporizador global de 5 minutos compartido entre todos los niveles  
- HUD que muestra tiempo restante y si el jugador tiene una llave  

### ✔ Enemigos Inteligentes
- Enemigos **patrulladores** y **perseguidores**  
- El perseguidor utiliza un algoritmo básico de seguimiento (distancia Manhattan)  
- Si toca al jugador → resta 10 segundos y lo devuelve al inicio  
- Los enemigos **no se superponen** entre sí  

### ✔ Pantallas especiales
- **Pantalla de victoria**
- **Pantalla de Game Over**
- **Menú de inicio** con Tkinter

---

## 📂 Estructura del Proyecto
.
├── main.py # Menú principal y controlador de niveles
├── laberinto1.py # Nivel 1
├── laberinto2.py # Nivel 2
├── laberinto3.py # Nivel 3
├── laberinto4.py # Nivel 4 con enemigos perseguidores
├── timer_global.py # Temporizador global usando threading
├── assets/ # (Opcional) imágenes, sonidos, fuentes
└── README.md # Este archivo

---

## 🚀 Instalación

### Requisitos
- Python 3.10 o superior
- Pygame  
- Tkinter (viene por defecto en la mayoría de instalaciones de Python)

### Instalación de dependencias

```bash
pip install pygame
```
---

## ▶ Ejecución del juego

### Simplemente corre:
```bash
python main.py
```

### Aparecerá la ventana de menú en Tkinter.
Desde allí puedes:
- Iniciar el juego
- Ver créditos
- Ver instrucciones
- Cerrar la aplicación

---

## 🧠 Lógica de Enemigos (resumen técnico)
El enemigo perseguidor:
- Se mueve cada N frames (movimiento lento)
- Sigue al jugador en el eje con mayor diferencia
- Verifica paredes antes de moverse
- No se superpone con otros enemigos (detección entre ellos)
- Penaliza al jugador con tiempo y respawn

---
## 🎯 Imagenes del juego
### Pantalla principal
<img width="598" height="430" alt="image" src="https://github.com/user-attachments/assets/8963e85e-e399-4b38-905e-68bda67ee342" />

### Instrucciones
<img width="594" height="429" alt="image" src="https://github.com/user-attachments/assets/cfdc6d44-fc7f-4884-b228-edc497f7b713" />

### Creditos
<img width="595" height="403" alt="image" src="https://github.com/user-attachments/assets/550820e2-d51a-4c61-8df3-5cdaccc9aec0" />

### Nivel 1
<img width="498" height="528" alt="image" src="https://github.com/user-attachments/assets/60829738-09e6-40a6-8582-701227b43928" />

### Nivel 2
<img width="796" height="572" alt="image" src="https://github.com/user-attachments/assets/9e643370-58c9-439d-8b2b-8cb394b783c5" />

### Nivel 3
<img width="993" height="1028" alt="image" src="https://github.com/user-attachments/assets/8232a4bb-6b45-4cf4-b473-98f3d1e6080f" />

### Nivel 4
<img width="1249" height="1031" alt="image" src="https://github.com/user-attachments/assets/80165aa1-3fa2-4ba4-99f9-ec16a0e341ba" />

---

## 👨‍💻 Autor
Proyecto desarrollado por Miguel
