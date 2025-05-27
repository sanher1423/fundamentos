
from itertools import permutations

def permutaciones_cadena():
    cadena = input("Ingresa una cadena de caracteres: ")
    unica = ''.join(sorted(set(cadena)))
    print(f"Caracteres únicos considerados: {unica}")

    perms = permutations(unica)
    for p in perms:
        print(''.join(p))

permutaciones_cadena()
