
import math

def minimo_multiplicador_para_cuadrado_perfecto():
    casos = int(input("Ingresa la cantidad de casos de prueba: "))
    for _ in range(casos):
        n = int(input("Ingresa un número mayor que 0 y menor que 2^31: "))
        i = 1
        while True:
            if math.isqrt(n * i)**2 == n * i:
                print(i)
                break
            i += 1

minimo_multiplicador_para_cuadrado_perfecto()
