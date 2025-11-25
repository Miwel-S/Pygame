import pygame
import sys
from timer_global import obtener_tiempo, tiempo_terminado

# Dimensiones de la ventana
ANCHO, ALTO = 800, 800

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 100, 255)
AMARILLO = (255, 255, 0)
VERDE= (0, 255, 0)
ROJO = (255, 0, 0)

TAM =40  # tamaño de cada casilla
# -------------------------------------------------------------------------
# 🧱 MAPA DEL LABERINTO
# 0 = vacío / pasillo
# 1 = pared
# 2 = llave
# 3 = puerta
# 4 = meta
# -------------------------------------------------------------------------

MAPA = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,2,0,0,0,1], 
[1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,1,1,0,1],
[1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,1],  
[1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,0,1,0,1],
[1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1],
[1,1,1,0,1,1,1,0,1,1,1,1,1,1,0,1,0,1,0,1],   
[1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1],
[1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,1,0,1,0,1],
[1,0,1,2,0,0,1,0,0,0,1,0,0,0,2,0,0,1,0,1],  
[1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
[1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],   
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1],
[1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
[1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
[1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1],
[1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1],   
[1,0,0,0,3,0,0,1,1,1,1,1,1,1,4,1,0,3,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

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

# -------------------------------------------------------------------------
# BUCLE PRINCIPAL DEL NIVEL 3
# -------------------------------------------------------------------------
def nivel_3():
    global jugador_x, jugador_y
    jugador_x, jugador_y = 1, 1  # reiniciar

    pygame.init() #Inicializar pygame
    global PANTALLA, RELOJ, FUENTE
    PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Laberinto - Nivel 3")
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

        # ✔️ Si llega a la meta (valor 4) → pasar al siguiente nivel
        if MAPA[jugador_y][jugador_x] == 4:
            return "completado"

        PANTALLA.fill(BLANCO)
        dibujar_mapa()

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