
def pares_suma_objetivo():
    lista = list(map(int, input("Ingresa la lista de enteros separados por coma: ").split(',')))
    objetivo = int(input("Ingresa la suma objetivo: "))
    vistos = set()
    pares = set()

    for num in lista:
        complemento = objetivo - num
        if complemento in vistos:
            par = tuple(sorted((num, complemento)))
            pares.add(par)
        vistos.add(num)

    for a, b in sorted(pares):
        print(f"{a}, {b}")

pares_suma_objetivo()
