# comentario
import pygame
from Bola import Bola
from listaBolas import ListaBolas
from colisionDetector import Colision

listaBolas = ListaBolas()
colision = Colision()


# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
BLANCOPALIDO = (75, 75, 75)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

pygame.init()

# Establecemos las dimensiones de la pantalla [largo,altura]
dimensiones = [700, 500]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Azucar")

done = False

# Se usa para establecer cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()
# -------- Bucle principal del Programa -----------
while not done:
    # --- Bucle principal de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            done = True
        if evento.type == pygame.MOUSEBUTTONDOWN:
            bola = Bola(pantalla)
            listaBolas.add(bola)

    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ
    colision.comprobar(listaBolas.getLista())
    colision.suelo(listaBolas.getLista(), dimensiones[1] - 50)
    colision.pared(listaBolas.getLista(), 0, dimensiones[0])

    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ

    # Primero, limpia la pantalla con blanco. No vayas a poner otros comandos de dibujo encima
    # de esto, de otra forma serán borrados por este comando:
    pantalla.fill(NEGRO)


    # print(reloj.get_time())
    listaBolas.actualiza(reloj.get_time())
    listaBolas.dibuja(BLANCOPALIDO)

    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    # print("iteracion")
    reloj.tick(90)

# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
pygame.quit()