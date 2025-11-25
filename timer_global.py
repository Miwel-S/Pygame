import time
import threading

tiempo_restante = 300   # 5 minutos
_timer_activo = False
_thread = None

def _run_timer():
    global tiempo_restante, _timer_activo
    while _timer_activo and tiempo_restante > 0:
        time.sleep(1)
        tiempo_restante -= 1

    # Cuando llega a 0 se detiene solo
    _timer_activo = False

def iniciar_temporizador():
    global _timer_activo, _thread
    if _timer_activo:
        return

    _timer_activo = True
    _thread = threading.Thread(target=_run_timer)
    _thread.daemon = True
    _thread.start()

def obtener_tiempo():
    minutos = tiempo_restante // 60
    segundos = tiempo_restante % 60
    return f"{minutos:02}:{segundos:02}"

def tiempo_terminado():
    return tiempo_restante <= 0
