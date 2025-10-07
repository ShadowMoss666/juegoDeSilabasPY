#! /usr/bin/env python
import os
import random
import sys
import math
import pygame

from pygame.locals import *
from configuracion import *
from extras import *
from funcionesSeparador import *
from funcionesVACIAS import *

# Funcion principal


def main():
    # Centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    # pygame.mixer.init()

    # Preparar la ventana
    pygame.display.set_caption("El juego del Mago Goma...")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    # tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    fps = FPS_inicial

    puntos = 0
    palabra_usuario = ""
    lemario_en_silabas = []
    lista_palabras_diccionario = []  # array con todas las palabras del diccionario

    lemario = open("src/lemario.txt", "r")

    # lectura del diccionario
    lectura_lemario(lemario, lista_palabras_diccionario)

    # elige una al azar
    palabra_en_pantalla = nueva_palabra(lista_palabras_diccionario)
##
    palabra_en_pantalla_anterior = ""
    dibujar_en_pantalla(screen, palabra_usuario,
                        palabra_en_pantalla, puntos, segundos)

    while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        fps = 3

        # Buscar la tecla apretada del modulo de eventos de pygame
        for e in pygame.event.get():

            # QUIT es apretar la X en la ventana
            if e.type == QUIT:
                pygame.quit()
                return ()

        # Ver si fue apretada alguna tecla
            if e.type == KEYDOWN:
                letra = dame_letra_apretada(e.key)
                palabra_usuario += letra  # es la palabra que escribe el usuario
                if e.key == K_BACKSPACE:
                    palabra_usuario = palabra_usuario[0:len(palabra_usuario)-1]
                if e.key == K_RETURN:
                    # pasa la palabra a silabas
                    palabra_en_pantalla_en_silabas = palabra_to_silabas(
                        palabra_en_pantalla)
                    if es_correcta(palabra_en_pantalla_en_silabas, palabra_usuario):
                        puntos += puntaje(palabra_en_pantalla)
                    else:
                        puntos -= int(puntaje(palabra_en_pantalla)/2)

                    # elige una al azar
                    palabra_en_pantalla = nueva_palabra(
                        lista_palabras_diccionario)
                    palabra_usuario = ""

        segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

        # Limpiar pantalla anterior
        screen.fill(COLOR_FONDO)

        # Dibujar de nuevo todo
        dibujar_en_pantalla(screen, palabra_usuario,
                            palabra_en_pantalla, puntos, segundos)

        pygame.display.flip()

    while 1:
        # Esperar el QUIT del usuario
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return

    lemario.close()


# Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
