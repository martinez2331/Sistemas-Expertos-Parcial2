# -*- coding: utf-8 -*-
"""
Created on Mon May  6 13:08:54 2024

@author: JOC
"""

import json
import random
respuestas_correctas = 0


def cargar_base_de_datos(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data


def elegir_testimonio(buscar, tipo):
    global respuestas_correctas
    equivocado = "El no es el responsable"
    correcto = "El si es el responsable "
    if tipo == 0:
        if buscar == 1:
            return testimonio1
        if buscar == 2:
            return testimonio2
        if buscar == 3:
            return testimonio3
        if buscar == 4:
            return testimonio4
        if buscar == 5:
            return sospechoso
        if buscar == 6:
            return lugar
        if buscar == 7:
            return arma
    else:
        if buscar in (1, 2, 3, 4):
            return equivocado
        if buscar in (5, 6, 7):
            respuestas_correctas = respuestas_correctas+1
            return correcto


def buscar(sospechosos, revisar, tipo):
    revisar = int(revisar)-1
    if 0 <= revisar < len(sospechosos):
        objetivo = sospechosos[revisar]
        if objetivo in testimonios:
            print(elegir_testimonio(testimonios[objetivo], tipo))
        y = 1
        return y
    else:
        print("\nInsertar el número de la opcion\n")
        y = 0
        return y


def investigar_personaje():
    y = 0
    sospechosos = list(personajes.keys())

    while y == 0:
        revisar = input(
            "Sospechosos : \n1) Fernando_Gutiérrez_Barrios\n2) Manuel_Tello_Macías\n3) Antonio_Riviello_Bazán\n4) Genaro_Garcia_Luna\n5) salinas_de_gortari \n")
        y = buscar(sospechosos, revisar, 0)


def investigar_locacion():
    y = 0
    sospechosos = list(locaciones.keys())

    while y == 0:
        revisar = input(
            "Locaciones visitadas : \n1) LOS_PINOS\n2) TIJUANA\n3) PALACIO_DE_BELLAS_2ARTES\n4) MUNICIPIO_DE_CHALCO\n5) ZOCALO\n")
        y = buscar(sospechosos, revisar, 0)


def investigar_arma():
    y = 0
    sospechosos = list(armas.keys())

    while y == 0:
        revisar = input(
            "Posibles Armas: \n1) CUCHILLO\n2) PISTOLA\n3) TIJERAS\n4) CABLE\n5) VENENO\n")
        y = buscar(sospechosos, revisar, 0)

def alazar_borrar_personaje(numero):
    borrar=random.choice(list(personajes2.keys()))
    del informacion2["evidencia"][0]["personajes"][borrar]
    testimonios[borrar]=numero
    return borrar

def alazar_borrar_locacion(numero):
    borrar=random.choice(list(locaciones2.keys()))
    del informacion2["evidencia"][1]["locaciones"][borrar]
    testimonios[borrar]=numero
    return borrar

def alazar_borrar_arma(numero):
    borrar=random.choice(list(armas2.keys()))
    del informacion2["evidencia"][2]["armas"][borrar]
    testimonios[borrar]=numero
    return borrar


informacion: dict = cargar_base_de_datos('base_de_datos.json')


informacion2: dict = cargar_base_de_datos('base_de_datos.json')


# SE ELIGE   PARA CREAR LA HISTORIA

personajes = informacion['evidencia'][0]['personajes']
asesino = random.choice(list(personajes.keys()))
informacion["evidencia"][0]["personajes"][asesino] = True

locaciones = informacion['evidencia'][1]['locaciones']
escena_crimen = random.choice(list(locaciones.keys()))
informacion["evidencia"][1]["locaciones"][escena_crimen] = True

armas = informacion['evidencia'][2]['armas']
arma_homicida = random.choice(list(armas.keys()))
informacion["evidencia"][2]["armas"][arma_homicida] = True


# Historia
testimonios = {}

personajes2 = informacion2['evidencia'][0]['personajes']
locaciones2 = informacion2['evidencia'][1]['locaciones']
armas2 = informacion2['evidencia'][2]['armas']

sospechoso = asesino+"No se encontro rastro de el"
testimonios[asesino] = 5
lugar = "No se vio que laguen entrara "+escena_crimen
testimonios[escena_crimen] = 6
arma = "Nadie tenia esa arma "+arma_homicida
testimonios[arma_homicida] = 7
final_resultado = asesino+" mato a Luis_Donaldo_Colosio usando " + \
    arma_homicida+" en la/el "+escena_crimen

del informacion2["evidencia"][0]["personajes"][asesino]
del informacion2["evidencia"][1]["locaciones"][escena_crimen]
del informacion2["evidencia"][2]["armas"][arma_homicida]

testimonio1= alazar_borrar_personaje(1)+" estaba en "+alazar_borrar_locacion(1)+" usando "+alazar_borrar_arma(1)
testimonio2= alazar_borrar_personaje(2)+" estaba en "+alazar_borrar_locacion(2)+" usando "+alazar_borrar_arma(2)
testimonio3= alazar_borrar_personaje(3)+" estaba en "+alazar_borrar_locacion(3)+" usando "+alazar_borrar_arma(3)
testimonio4= alazar_borrar_personaje(4)+" estaba en "+alazar_borrar_locacion(4)+" usando "+alazar_borrar_arma(4)
##


print("Han matado a Luis_Donaldo_Colosio\n")
print("¿QUIEN LO MATO?\n")

x = 5

while x != 0:
    a_investigar = input(
        "Quedan "+str(x)+" intentos\nSelecciona que quieres investigar\n 1. Personaje\n 2. Ubicacion\n 3. Arma\n")

    switch = {
        '1': investigar_personaje,
        '2': investigar_locacion,
        '3': investigar_arma
    }

    if a_investigar in switch:
        switch[a_investigar]()
        x = x-1
    else:
        print("No Existe")

print("\nSe acabaron los intentos para buscar las evidencias, ya tienes en mente quien lo hizo? , su arma y el lugar del asesinto ?\n")

y = 0

while y == 0:
    final_culpable = input(
        "Culpable: \n1) Fernando_Gutierrez_Barrios \n2) Manuel_Tello_Macías \n3) Antonio_Riviello_Bazán \n4) Genaro_Garcia_Luna \n5) salinas_de_gortari  \n")
    y = buscar(list(personajes.keys()), final_culpable, 1)

y = 0
while y == 0:
    final_lugar = input(
        "Lugar: \n1) LOS_PINOS\n2) TIJUANA\n3) PALACIO_DE_BELLAS_ARTES\n4) MUNICIPIO_DE_CHALCO\n5) ZOCALO\n")
    y = buscar(list(locaciones.keys()), final_lugar, 1)

y = 0
while y == 0:
    final_arma = input(
        "Arma: \n1) CUCHILLO\n2) PISTOLA\n3) TIJERAS\n4) CABLE\n5) VENENO\n")
    y = buscar(list(armas.keys()), final_arma, 1)

print("\n"+final_resultado+"\n")
print("Deduciste "+str(respuestas_correctas)+" parte(s) del asesinato")
if respuestas_correctas == 3:
    print("\nFelicidades, has contestado todo correctamente")
else:
    print("\nPerdiste.")
