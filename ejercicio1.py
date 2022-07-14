import numpy as np
import random

def escribir_archivo():

    nombre_fichero = "./numeros_prueba.txt"
    with open(nombre_fichero, "w", enconding="utf-8") as file:
        for i in range(1, 21):
            numero_aleatorio = random.randint(100, 1000)
            linea = str(numero_aleatorio)

            file.write(linea)
            file.write("/n")

def leer():
    numeros = []
    with open("./numeros_prueba.txt", "r")
        for linea in file:
            numeros.append(int(linea))
    numero_impar = []
    for n in numeros:
        if n % 2 != 0:
            numero_impar.append(n)
    return numero_impar

def main():
    escribir_archivo()
    numero_impar = leer()

    print(numero_impar)
    arreglo = np.array(numero_impar)
    print(arreglo.ndim)

if __name__ == "__main__":
    main()

