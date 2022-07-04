"""

Realizar un programa en Python que le permita al equipo de trabajo conocer el
estado nutricional del paciente del hospital infantil-juvenil y la cantidad de días
que le tomará a este paciente alcanzar el peso objetivo o su peso máximo si es
un paciente que previamente tiene una condición de peso saludable.

"""


def solucion(edad, peso):
    edad = float(input("Indicar la edad del paciente:"))
    peso = float(input("Indicar el peso del paciente en kilogramos:"))
    dietaA = 0.001*((60.1*2) + (30.5*1) - (24.4*2))
    dietaB = 0.001*((60.1*0.6) + (30.5*1) - (24.4*4))
    dietaC = 0.001*((60.1*0.5) + (30.5*0.7) - (24.4*2))
    objetivo = 0
    tipo = "Sin definir"
    m = 0
    d = 1
    obj = 0
    dieta = 0
    if edad >= 5 and edad <= 10:
        if peso < 16:
            dieta = dietaA
            objetivo = 22
            tipo = "A"
        elif peso > 28:
            dieta = dietaB
            objetivo = 24
            tipo = "B"
        else:
            dieta = dietaC
            objetivo = 28
            tipo = "C"
    if edad > 10 and edad <= 13:
        if peso < 30:
            dieta = dietaA
            objetivo = 32
            tipo = "A"
        elif peso > 50:
            dieta = dietaB
            objetivo = 43
            tipo = "B"
        else:
            dieta = dietaC
            objetivo = 50
            tipo = "C"
    if edad > 13 and edad <= 17:
        if peso < 51:
            dieta = dietaA
            objetivo = 56
            tipo = "A"
        elif peso > 63:
            dieta = dietaB
            objetivo = 58
            tipo = "B"
        else:
            dieta = dietaC
            objetivo = 63
            tipo = "C"
    while m == 0:
        obj = peso + dieta*d
        print(obj, d)
        if obj >= objetivo and tipo == "C":
            print(
                f"El estado nutricional del paciente es {tipo} y se requieren {d} días de dieta para que alcance el peso máximo")
            m = 1
        if obj >= objetivo and tipo == "A" or tipo == "B":
            print(
                f"El estado nutricional del paciente es {tipo} y se requieren {d} días de dieta para que alcance el peso saludable")
            m = 1
        else:
            d += 1


solucion(15, 10)
