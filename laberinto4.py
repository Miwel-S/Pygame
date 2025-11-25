import pygame
import sys
from timer_global import obtener_tiempo, tiempo_terminado, tiempo_restante
import timer_global

# Dimensiones de la ventana
ANCHO, ALTO = 1250, 1000

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 100, 255)
AMARILLO = (255, 255, 0)
VERDE= (0, 255, 0)
ROJO = (255, 0, 0)

TAM = 50  # tamaño de cada casilla
# -------------------------------------------------------------------------
# 🧱 MAPA DEL LABERINTO
# 0 = vacío / pasillo
# 1 = pared
# 2 = llave
# 3 = puerta
# 4 = meta
# -------------------------------------------------------------------------
MAPA = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,2,0,0,1],
[1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1],
[1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1,0,1],
[1,0,1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,1,0,1],
[1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,1],
[1,1,1,0,1,0,1,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1,0,1],
[1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,0,1,0,1],
[1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,1,0,1],
[1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1],
[1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,0,1],
[1,0,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,0,1,0,1,1,1],
[1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1],
[1,0,1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1],
[1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,1],
[1,1,1,0,1,0,1,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1],
[1,2,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,3,3,0,1,1,1],
[1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,4,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

# Enemigos perseguidores
enemigo1 = {
    "x": 5,
    "y": 10,
    "velocidad": 2,  # frames para moverse
    "contador": 0
}

enemigo2 = {
    "x": 15,
    "y": 10,
    "velocidad": 2,  # frames para moverse
    "contador": 0
}

# Posición inicial del jugador
jugador_x, jugador_y = 1, 1

tiene_llave = False

# -------------------------------------------------------------------------
# FUNCIONES
# -------------------------------------------------------------------------
def dibujar_mapa():
    for y, fila in enumerate(MAPA):
        for x, valor in enumerate(fila):
            rect = pygame.Rect(x*TAM, y*TAM, TAM, TAM)

            if valor == 1:  # pared
                pygame.draw.rect(PANTALLA, AZUL, rect)

            elif valor == 2:  # llave
                pygame.draw.rect(PANTALLA, AMARILLO, rect)

            elif valor == 3:  # puerta
                pygame.draw.rect(PANTALLA, ROJO, rect)

            elif valor == 4:  # meta
                pygame.draw.rect(PANTALLA, VERDE, rect)

            # bordes finos
            pygame.draw.rect(PANTALLA, NEGRO, rect, 1)


def mover_jugador(dx, dy):
    global jugador_x, jugador_y, tiene_llave

    nuevo_x = jugador_x + dx
    nuevo_y = jugador_y + dy

    if MAPA[nuevo_y][nuevo_x] == 1:
        return  # pared → no se mueve

    # llave
    if MAPA[nuevo_y][nuevo_x] == 2:
        if tiene_llave ==True:
            return # no lo deja tomar otra llave para evitar soflockeo
        tiene_llave = True
        MAPA[nuevo_y][nuevo_x] = 0

    # puerta cerrada
    if MAPA[nuevo_y][nuevo_x] == 3:
        if tiene_llave:
            MAPA[nuevo_y][nuevo_x] = 0  # abrir puerta
            tiene_llave=False
        else:
            return  # no puede pasar

    jugador_x = nuevo_x
    jugador_y = nuevo_y


def mostrar_hud_tiempo():
    # obtiene el tiempo formateado desde timer_global
    tiempo = obtener_tiempo()

    # superficie semitransparente para el HUD
    ancho_hud, alto_hud = 220, 50
    hud = pygame.Surface((ancho_hud, alto_hud))
    hud.set_alpha(170)
    hud.fill((0, 0, 0))

    # texto
    texto = FUENTE.render(f"Tiempo: {tiempo}", True, (255, 255, 255))
    # opcional: mostrar si tiene llave
    llave_text = FUENTE.render(f"Llave: {'Sí' if tiene_llave else 'No'}", True, (255,255,255))

    # dibujar hud y textos
    PANTALLA.blit(hud, (10, 10))
    PANTALLA.blit(texto, (20, 18))
    PANTALLA.blit(llave_text, (20, 36))


def mostrar_game_over_overlay():
    overlay = pygame.Surface((ANCHO, ALTO))
    overlay.set_alpha(220)
    overlay.fill((0, 0, 0))
    PANTALLA.blit(overlay, (0, 0))

    big = pygame.font.SysFont("Consolas", 64, bold=True)
    texto = big.render("GAME OVER", True, (255, 50, 50))
    rect = texto.get_rect(center=(ANCHO//2, ALTO//2))
    PANTALLA.blit(texto, rect)
    pygame.display.flip()


def dibujar_enemigo(enemigo):
    pygame.draw.circle(
        PANTALLA,
        (200, 20, 20),  # rojo oscuro
        (enemigo["x"]*TAM + TAM//2, enemigo["y"]*TAM + TAM//2),
        TAM//3
    )


def mover_enemigo_persiguiendo(enemigo, otros_enemigos):
    enemigo["contador"] += 1
    if enemigo["contador"] < enemigo["velocidad"]:
        return
    enemigo["contador"] = 0

    ex, ey = enemigo["x"], enemigo["y"]
    dx = jugador_x - ex
    dy = jugador_y - ey

    # Función interna para validar si la casilla está libre
    def casilla_libre(nx, ny):
        # no es pared
        if MAPA[ny][nx] == 1:
            return False
        # no está ocupada por otro enemigo
        for otro in otros_enemigos:
            if otro["x"] == nx and otro["y"] == ny:
                return False
        return True

    # 1. Intentar eje prioritario
    if abs(dx) > abs(dy):
        paso_x = 1 if dx > 0 else -1
        nx, ny = ex + paso_x, ey
        if casilla_libre(nx, ny):
            enemigo["x"] = nx
            return

    paso_y = 1 if dy > 0 else -1
    nx, ny = ex, ey + paso_y
    if casilla_libre(nx, ny):
        enemigo["y"] = ny
        return

    # 2. Última alternativa (eje secundario)
    paso_x = 1 if dx > 0 else -1
    nx, ny = ex + paso_x, ey
    if casilla_libre(nx, ny):
        enemigo["x"] = nx


def penalizar_jugador():
    global jugador_x, jugador_y
    timer_global.tiempo_restante = max(0, timer_global.tiempo_restante - 10)
    jugador_x, jugador_y = inicio_jugador


def mostrar_victoria_overlay(mensaje="¡Nivel Completado!"):
    overlay = pygame.Surface((ANCHO, ALTO))
    overlay.set_alpha(200)
    overlay.fill((0, 0, 0))
    PANTALLA.blit(overlay, (0, 0))

    big = pygame.font.SysFont("Consolas", 64, bold=True)
    small = pygame.font.SysFont("Consolas", 36)

    texto = big.render("¡Victoria!", True, (50, 255, 50))
    subtitulo = small.render(mensaje, True, (255, 255, 255))

    rect1 = texto.get_rect(center=(ANCHO//2, ALTO//2 - 50))
    rect2 = subtitulo.get_rect(center=(ANCHO//2, ALTO//2 + 20))

    PANTALLA.blit(texto, rect1)
    PANTALLA.blit(subtitulo, rect2)

    pygame.display.flip()
    pygame.time.delay(2500)  # Pausa 2.5 segundos antes de avanzar

# -------------------------------------------------------------------------
# BUCLE PRINCIPAL DEL NIVEL 4
# -------------------------------------------------------------------------
def nivel_4():
    global inicio_jugador, jugador_x, jugador_y
    inicio_jugador = (1, 1)
    jugador_x, jugador_y = inicio_jugador  # reiniciar

    pygame.init() #Inicializar pygame
    global PANTALLA, RELOJ, FUENTE
    PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Laberinto - Nivel 4")
    RELOJ = pygame.time.Clock()
    FUENTE = pygame.font.SysFont("Arial", 24)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    mover_jugador(0, -1)
                elif event.key == pygame.K_DOWN:
                    mover_jugador(0, 1)
                elif event.key == pygame.K_LEFT:
                    mover_jugador(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    mover_jugador(1, 0)

        # Si se acabó el tiempo → mostrar Game Over
        if tiempo_terminado():
            mostrar_game_over_overlay()
            pygame.time.delay(2000)
            return "tiempo_agotado"

        if MAPA[jugador_y][jugador_x] == 4:
            mostrar_victoria_overlay("Has escapado del laberinto")
            return "completado"

        PANTALLA.fill(BLANCO)
        dibujar_mapa()
        dibujar_enemigo(enemigo1)
        dibujar_enemigo(enemigo2)
        mover_enemigo_persiguiendo(enemigo1, [enemigo2])
        mover_enemigo_persiguiendo(enemigo2, [enemigo1])

        # Colisión con enemigo perseguidor
        if enemigo1["x"] == jugador_x and enemigo1["y"] == jugador_y:
           penalizar_jugador()
        if enemigo2["x"] == jugador_x and enemigo2["y"] == jugador_y:
           penalizar_jugador()

        # Dibujar jugador
        pygame.draw.circle(
            PANTALLA,
            (0,0,0),
            (jugador_x*TAM + TAM//2, jugador_y*TAM + TAM//2),
            TAM//3
        )

        mostrar_hud_tiempo()

        pygame.display.flip()
        RELOJ.tick(10)