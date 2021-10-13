# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 23:21:02 2021

@author: AmairaniG
"""

# importando la libreria para el manejo de archivos csv
import csv

# creando una lista para guardar los registros de BD
lista_datos = []

# Leyendo el archivo y guardando en una lista los registros
with open('synergy_logistics_database.csv', 'r') as archivo_csv:
    lector = csv.reader(archivo_csv)
    skip = 0
    for linea in lector:
        if skip == 0:
            skip += 1
        else:
            lista_datos.append(linea)

# Consigna 1

# Registro de las rutas
# Generando variable de busqueda de sentido


def rutas_demanda(direccion):  # Definiendo una función que genere las listas para consigna 1
    rutas_conteo = []  # Lista para guardar la ruta y cuantas veces se repite
    contador = 0  # Variable para contar el número de veces que una ruta se presenta
    valor = 0  # Variable para sumar el valor de la exportacion
    rutas_contadas = []  # Lista para guardar las listas que ya han sido registradas

    for ruta in lista_datos:
        ruta_actual = [ruta[2], ruta[3]]
        if ruta[1] == direccion and ruta_actual not in rutas_contadas:
            for movimiento in lista_datos:
                if ruta_actual == [movimiento[2], movimiento[3]] and movimiento[1] == direccion:
                    contador += 1
                    valor += int(movimiento[9])
                    rutas_contadas.append(ruta_actual)
            formato = [ruta[2], ruta[3], contador, valor]
            rutas_conteo.append(formato)
            contador = 0
            valor = 0

    # Ordenando las rutas por su conteo
    sorted(rutas_conteo, reverse=True, key=lambda x: x[2])
    count = 0
    for i in rutas_conteo:
        if count < 10:
            print(i[0], i[1])
            count += 1
    print('')

# Consigna 2

# Definiendo una función que genere las listas para consigna 2

def transportes_demanda(direccion):
    transporte_valor = []  # Lista para guardar la ruta y su valor total por sentido logistico
    valor = 0  # Variable para contar el número de veces que una ruta se presenta
    transporte_valuado = []  # Lista para guardar las listas que ya han sido registradas

    for transporte in lista_datos:  # creando a lista de los transportes y su valor
        transporte_actual = [transporte[7]]
        if transporte[1] == direccion and transporte_actual not in transporte_valuado:
            for movimiento in lista_datos:
                if transporte_actual == [movimiento[7]] and movimiento[1] == direccion:
                    valor += int(movimiento[9])
                    transporte_valuado.append(transporte_actual)
            formato = [transporte[7], valor]
            transporte_valor.append(formato)
            valor = 0

    # Ordenando las rutas por su conteo
    sorted(transporte_valor, reverse=True, key=lambda x: x[1])

    print(f'Los tres medios de transportes más importantes de {direccion}')
    count = 0
    for i in transporte_valor:
        if count < 3:
            print(i[0], i[1])
            count += 1
    print('')

# Consigna 3

# Definiendo una función que genere las listas para consigna 3

def paises_demanda(direccion):
    pais_valor = []  # Lista para guardar el pais y su valor total por sentido logistico
    pais_porcentaje = []
    valor = 0  # Variable para contar el número de veces que una ruta se presenta
    pais_valuado = []  # Lista para guardar las listas que ya han sido registradas
    suma_total = 0
    if direccion == 'Exports':
        indice = 2
    elif direccion == 'Imports':
        indice = 3
    for pais in lista_datos:
        pais_actual = pais[indice]
        if pais[1] == direccion and pais_actual not in pais_valuado:
            for movimiento in lista_datos:
                if pais_actual == movimiento[indice] and movimiento[1] == direccion:
                    valor += int(movimiento[9])
                    suma_total += int(movimiento[9])
                    pais_valuado.append(pais_actual)
            formato = [pais_actual, valor]
            pais_valor.append(formato)
            valor = 0
    suma_total
    # Ordenando las rutas por su conteo
    pais_valor.sort(reverse=True, key=lambda x: x[1])
    porcentaje = 0
    for pais in pais_valor:  # creando una lista ordenada solo con los paises que suman el 80%
        if porcentaje < 80:
            porc = (pais[1]/suma_total)*100
            pais_porcentaje.append([pais[0], porc])
            porcentaje += porc
    print(f'Los países con el 80% del valor de {direccion}')
    for i in pais_porcentaje:
        print(i[0], f'{i[1]}%')
    print("")
    return pais_porcentaje


selec = input('Seleccione la opcion que requiera analizar2 \n 1.Rutas de importación y exportación \n 2.Medio de transporte utilizado \n 3.Valor total de importaciones y exportaciones\n\n')
valid = 0
while valid == 0:
    if selec == '1':
        # invocando funcion para registrar rutas de exportaciones
        rutas_demanda('Exports')
        # invocando funcion para registrar rutas de importaciones
        rutas_demanda('Imports')
        valid = 1
    elif selec == '2':
        # invocando funcion para registrar rutas de exportaciones
        transportes_demanda('Exports')
        # invocando funcion para registrar rutas de importaciones
        transportes_demanda('Imports')
        valid = 1
    elif selec == '3':
        # invocando funcion para registrar rutas de exportaciones
        paises_demanda('Exports')
        # invocando funcion para registrar rutas de importaciones
        paises_demanda('Imports')
        valid = 1
    else:
        selec = input('Selecciona una consigna válida')
