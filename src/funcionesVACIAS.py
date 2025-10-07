from operator import truediv
from principal import *
from configuracion import *
from funcionesSeparador import *
import random
import math


def lectura_lemario(archivo, salida):
    linea = archivo.readlines()
    for i in range(len(linea)):
        salida.append(linea[i].strip())


def nueva_palabra(lista_palabras_diccionario):
    i = random.randint(1, len(lista_palabras_diccionario))
    for palabra in lista_palabras_diccionario:
        return lista_palabras_diccionario[i]


def silabas_to_palabra(palabra_en_silabas):
    ret = ""
    for char in palabra_en_silabas:
        if char == "-" or char == " ":
            pass
        else:
            ret += char
    return ret


def palabra_to_silabas(palabra):
    return separador(palabra)


def es_correcta(palabra_en_pantalla_en_silabas, palabra):
    return palabra_en_pantalla_en_silabas == palabra


def puntaje(palabra):
    return len(palabra)
