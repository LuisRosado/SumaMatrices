import os
def crear_matriz(Tamaño):
    os.system("cls")
    matriz = []

    for i in range(Tamaño):
        matriz.append([])
        for j in range(Tamaño):
            valor = int(input("Fila{}, Columna{} : ".format(i+1, j+1)))
            matriz[i].append(valor)

    print()
    for fila in matriz:
        print("[",end=" ")
        for elemento in fila:
            print("{}".format(elemento), end=" ")
        print("]")
    print("Esta es la matriz creada.")
    input('presiona enter para continuar...')
    return matriz

def sumar_matriz(m1,m2):
    m3 = []
    for i in range(len(m1)):
        m3.append([])
        for j in range(len(m1[0])):
            m3[i].append(m1[i][j] + m2[i][j])
    return m3




'''---Funcion Principal---'''
Tamaño = int(input('Ingrese el tamaño de las matrices: '))
print("Matriz 1: ")
a = crear_matriz(Tamaño)
print("Matriz 2: ")
b = crear_matriz(Tamaño)
c = sumar_matriz(a,b)
os.system("cls")
print("\nResultado de la suma: \n")

for fila in c:
    print("[",end=" ")
    for elemento in fila:
        print(elemento, end=" ")
    print("]")
