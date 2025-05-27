
def evaluar_polinomio(coeficientes, x):
    return sum(c * (x ** i) for i, c in enumerate(reversed(coeficientes)))

def herencia():
    while True:
        try:
            grado = int(input())
            if grado == 20:
                break
            coeficientes = list(map(int, input().split()))
            n = int(input())

            area_cain = 0.0
            for i in range(n):
                x = i / n
                y = evaluar_polinomio(coeficientes, x)

                if y < 0:
                    y = 0
                elif y > 1:
                    y = 1

                area_cain += (1 / n) * y

            area_abel = 1 - area_cain
            diferencia = abs(area_cain - area_abel)

            if diferencia <= 0.001:
                print("JUSTO")
            elif area_cain > area_abel:
                print("CAIN")
            else:
                print("ABEL")
        except EOFError:
            break

if __name__ == "__main__":
    herencia()
