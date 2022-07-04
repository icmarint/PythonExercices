"""

Usted y un grupo de amigos ha decidido realizar una rifa de 1’000.000 de pesos
para recaudar fondos en pro de los habitantes de calle del municipio en el que
usted habita.

"""


def solucion(b, n):
    a = 0
    intentos = 0
    m = 0
    while m == 0:
        a = input(f"Ingrese un número: ")
        a = int(a)
        if a > b or a < 0:
            print(f"¡Te saliste del intervalo!")
            intentos -= 1
        if a > n and a <= b and a > 0:
            print(f"¡Ups! Te pasaste")
        if a < n and a < b and a >= 0:
            print(f"¡Ups! Estás por debajo")
        intentos += 1
        if a == n:
            print(f"¡LO LOGRASTE! Usaste {intentos} intentos")
            m = 1


solucion(15, 10)
