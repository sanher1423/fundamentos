
def es_triangular(matriz):
    n = len(matriz)
    superior = True
    inferior = True

    for i in range(n):
        for j in range(n):
            if i > j and matriz[i][j] != 0:
                inferior = False
            if i < j and matriz[i][j] != 0:
                superior = False

    return superior or inferior

def matrices_triangulares():
    while True:
        n = int(input())
        if n == 0:
            break
        matriz = []
        for _ in range(n):
            fila = list(map(int, input().split()))
            matriz.append(fila)

        print("SI" if es_triangular(matriz) else "NO")

if __name__ == "__main__":
    matrices_triangulares()
