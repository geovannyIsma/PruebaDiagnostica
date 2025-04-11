from utils import generar_numeros_aleatorios
from ArbolBInarioAVL import ArbolBinarioAVL

nums = sorted(generar_numeros_aleatorios(1, 50, 9))
print("Numeros: ", nums)

CONSTATE_MAGICA = sum(nums) // 3
print("Constante magica: ", CONSTATE_MAGICA)

centro = nums[4]

cuadro = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
cuadro[1][1] = centro

impares = [num for num in nums if num % 2 != 0]
pares = [num for num in nums if num % 2 == 0]

if (centro % 2 == 0):  # Centro es par
    cuadro[0][0] = impares.pop(0)
    cuadro[0][2] = impares.pop(0)

    if (cuadro[0][0] + centro + impares[0] == CONSTATE_MAGICA):
        cuadro[2][2] = impares.pop(0)
    else:
        cuadro[2][2] = impares.pop(1)

    if (cuadro[0][2] + centro + impares[0] == CONSTATE_MAGICA):
        cuadro[2][0] = impares.pop(0)
    else:
        cuadro[2][0] = impares.pop(1)

else:  # Centro es impar
    cuadro[0][0] = pares.pop(0)
    cuadro[0][2] = pares.pop(0)

    if (cuadro[0][0] + centro + pares[0] == CONSTATE_MAGICA):
        cuadro[2][2] = pares.pop(0)
    else:
        cuadro[2][2] = pares.pop(1)

    if (cuadro[0][2] + centro + pares[0] == CONSTATE_MAGICA):
        cuadro[2][0] = pares.pop(0)
    else:
        cuadro[2][0] = pares.pop(1)

faltantes = [
        (0, 1, CONSTATE_MAGICA - (cuadro[0][0] + cuadro[0][2])),
        (2, 1, CONSTATE_MAGICA - (cuadro[2][0] + cuadro[2][2])),
        (1, 0, CONSTATE_MAGICA - (cuadro[0][0] + cuadro[2][0])),
        (1, 2, CONSTATE_MAGICA - (cuadro[0][2] + cuadro[2][2]))
    ]
for fila, col, valor in faltantes:
    if valor in nums:
        cuadro[fila][col] = valor

for fila in cuadro:
    print(fila)

def verificar_cuadro(cuadro, constante):
    for fila in cuadro:
        suma_fila = sum(fila)
        if suma_fila != constante:
            return False

    for col in range(3):
        suma_columna = 0
        for fila in range(3):
            suma_columna += cuadro[fila][col]
        if suma_columna != constante:
            return False

    suma_diagonal_principal = 0
    for i in range(3):
        suma_diagonal_principal += cuadro[i][i]
    if suma_diagonal_principal != constante:
        return False

    suma_diagonal_secundaria = 0
    for i in range(3):
        suma_diagonal_secundaria += cuadro[i][2 - i]
    if suma_diagonal_secundaria != constante:
        return False
    return True

if verificar_cuadro(cuadro, CONSTATE_MAGICA):
    print("Cuadro mágico completado correctamente:")
else:
    print("Error al completar el cuadro mágico:")

arbol = ArbolBinarioAVL(cuadro[1][1])
for fila in cuadro:
    for num in fila:
        if num != cuadro[1][1]:
            arbol.insertar(num)

print("\nÁrbol binario generado a partir del cuadro mágico:")
arbol.imprimir_arbol()

print("\nRecorrido inorden del árbol binario:")
print(arbol.recorrido_inorden())