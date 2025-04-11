import random

def generar_numeros_aleatorios(rango_min, rango_max, cantidad = 9):
    num_inicio = random.randint(rango_min, rango_max)
    num_max = num_inicio + cantidad - 1
    numeros_aleatorios =[]
    while True:
        num_ale = random.randint(num_inicio, num_max)
        if num_ale not in numeros_aleatorios:
            numeros_aleatorios.append(num_ale)
            if len(numeros_aleatorios) == cantidad:
                break
    return numeros_aleatorios