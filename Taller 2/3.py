
import string

def cifrado_cesar_frase():
    def cifrar_palabra(palabra, salto):
        alfabeto = string.ascii_lowercase
        resultado = ''
        for letra in palabra:
            if letra.lower() in alfabeto:
                mayus = letra.isupper()
                indice = alfabeto.index(letra.lower())
                nueva_letra = alfabeto[(indice + salto) % 26]
                resultado += nueva_letra.upper() if mayus else nueva_letra
            else:
                resultado += letra
        return resultado

    frase = input("Ingresa la frase a cifrar/descifrar: ")
    palabras = frase.split()
    resultado = []

    for i, palabra in enumerate(palabras):
        salto = 3 if i % 2 == 1 else 4
        resultado.append(cifrar_palabra(palabra, salto))

    print("Frase cifrada:", ' '.join(resultado))

cifrado_cesar_frase()
