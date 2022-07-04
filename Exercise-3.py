# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN.
# NO ELIMINAR LAS IMPORTACIONES A CONTINUACIÓN. SU SOLUCIÓN
# DEBE BASARSE EN EL USO DE ELLAS. CREE DOS FUNCIONES, UNA
# PARA EL ENCRIPTADO Y OTRA PARA EL DESENCRIPTADO

import numpy as np
import random


def encriptado(texto):

    # ESCRIBA EN ESTA REGIÓN SU PROPUESTA DE SOLUCIÓN PARA EL ENCRIPTADO
    # USANDO EL MÉTODO EXPUESTO EN EL ENUNCIADO. ATÉNGASE AL USO DE LOS
    # RETORNOS PUESTOS AL FINAL DE ESTA FUNCIÓN

    # Contar los caracteres del vector: n

    n = len(texto)
    print(n)

    # Calcular raiz cuadrada de n
    raiz = n**(0.5)
    print(raiz)
    # Verificar si raiz cuadrada de n es entero -> raiz % 1 == 0 (sea una potencia de un número entero)
    if raiz % 1 == 0:
        print('es cuadrado perfecto')
    else:
        print('no es cuadrado perfecto')

    # Definir cuál es la potencia más cercana

    m = 0
    i = 0
    print(n)
    while m == 0:
        n = n + 1
        raizmas = n**(0.5)
        if raizmas % 1 == 0:
            print(f'el cuadrado perfecto más cercano es {n}')
            m = 1
        else:
            i = i + 1
            print(i)

    # Añadir _ al texto un número de veces
    # hasta que el texto tenga un número de caracteres igual a la potencia más cercana
    objetivo = n
    n = len(texto)
    print(n)

    m = objetivo - n
    print(m)

    if m > 0:
        nuevo = texto + ('_'*m)
        print(nuevo)

    # Convertir texto en array y array en list con np

    l = []
    m = list(nuevo)
    l = np.array(m)
    l = list(l)
    print(l)

    rows = len(l)
    clave = []

    # Crear vector con ceros:

    for row_index in range(rows):
        row = "0000"
        clave.append(row)

    print(clave)

    # Reemplazar vector de ceros por numeros en orden
    for i in range(rows):
        clave[i] = i

    print(clave)

    # Desordenar vector aleatoriamente:
    mylist = clave
    random.shuffle(mylist)
    clave = mylist

    print(clave)

    # Asignar string en el orden que indica la matriz clave

    n = np.array(l)
    clave = np.array(clave)

    sorted_n = n[clave]

    print(sorted_n)

    # Convertir cada caracter en su respectivo código unicode

    rows2 = len(sorted_n)

    codigo_unicode = []

    # Crear vector con ceros:

    for row_index in range(rows2):
        row = "0000"
        codigo_unicode.append(row)

    print(codigo_unicode)

    # Asignar a cada valor de cero, un código unicode

    for i in range(rows2):
        s = sorted_n[i]
        codigo_unicode[i] = ord(s)

    print(codigo_unicode)

    # Convertir vector con valores unicode en matriz cuadrada:

    array = np.asarray(codigo_unicode)
    print(array)
    print(rows2)
    raiz2 = rows2**(0.5)
    filas = int(raiz2)
    array_final = array.reshape(filas, filas)

    print(array_final)
    print(clave)

    return array_final, clave


def desencriptado(array_encriptado, clave):

    print(array_encriptado)
    print(clave)

    # Transformar matriz encriptada en vector:
    array = np.array(array_encriptado)

    flat = array.flatten()
    print(flat)

    # Cambiar vecto con valores unicode por texto

    rows3 = len(flat)
    print(rows3)

    chr_unicode = []

    # Crear vector con ceros:

    for row_index in range(rows3):
        row = "0000"
        chr_unicode.append(row)

    print(chr_unicode)

    # Traducir valores unicode del vector flat a caracteres:

    for i in range(rows3):
        s = flat[i]
        chr_unicode[i] = chr(s)

    print(chr_unicode)

    # Asignar lista de caracteres desordenados en el orden que indica el vector clave

    clave = np.array(clave)
    chr_unicode = np.array(chr_unicode)

    result_list = [i for _, i in sorted(zip(clave, chr_unicode))]
    print(result_list)

    # Convertir vector a texto
    G = ''.join(result_list)
    print(G)

    # Remover "_" del texto:

    texto = G
    characters = "_"

    texto = texto.replace(characters, "")

    print(texto)

    # ESCRIBA EN ESTA REGIÓN SU PROPUESTA DE SOLUCIÓN PARA EL DESENCRIPTADO
    # USANDO EL MÉTODO EXPUESTO EN EL ENUNCIADO. ATÉNGASE AL USO DEL
    # RETORNO PUESTO AL FINAL DE ESTA FUNCIÓN

    return texto


encriptado('Today is Caturday!')


desencriptado(([[95, 105,  95,  32,  32], [95, 115, 121, 100, 114], [97, 116,  95,  97,  95], [95,  97,  95,  67, 117], [
    33, 100, 111, 121,  84]]), ([23,  6, 18,  5,  8, 19,  7, 16,  2, 13, 15, 11, 22, 10, 21, 20,  3, 24,  9, 12, 17, 14, 1, 4, 0]))
