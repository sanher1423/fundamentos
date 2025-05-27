
import numpy as np
import matplotlib.pyplot as plt

def proyeccion_vectores():
    while True:
        entrada = input("Ingresa las componentes x e y del vector separadas por espacio (o escribe 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            break
        x, y = map(float, entrada.split())
        v = np.array([x, y])
        u1 = np.random.rand(2)
        u1 /= np.linalg.norm(u1)
        u2 = np.random.rand(2)
        u2 /= np.linalg.norm(u2)

        p1 = np.dot(v, u1) * u1
        p2 = np.dot(v, u2) * u2

        plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector original')
        plt.quiver(0, 0, p1[0], p1[1], angles='xy', scale_units='xy', scale=1, color='r', label='Proyección 1')
        plt.quiver(0, 0, p2[0], p2[1], angles='xy', scale_units='xy', scale=1, color='g', label='Proyección 2')
        plt.legend()
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        plt.grid()
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()

proyeccion_vectores()
