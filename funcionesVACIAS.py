from operator import truediv
from principal import *
from configuracion import *
import random
import math



def lectura(archivo, salida):
    datos = archivo.readlines()
    for i in range(len(datos)):
        salida.append(datos[i])
    

def nuevaPalabra(lista):
    i = random.randint(1,len(lista))
    for palabra in lista:
        return lista[i]

def silabasTOpalabra(silaba):
    pal = ""
    for char in silaba:
        if char == "-" or char == " ":
            pass
        else: pal += char
    return pal


def palabraTOsilaba(palabra):
    pass

def esCorrecta(palabraEnSilabasEnPantalla, palabra):
    return True

def puntaje(palabra):
    return 5

