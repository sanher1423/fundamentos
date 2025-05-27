
def convertir_a_romano():
    valores = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    while True:
        n = int(input("Ingresa un número entero positivo (0 para salir): "))
        if n == 0:
            break
        romano = ''
        for val, simbolo in valores:
            while n >= val:
                romano += simbolo
                n -= val
        print("En números romanos:", romano)

convertir_a_romano()
