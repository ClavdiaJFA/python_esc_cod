#nums = [ 2, 5, 15, 21, 16, 18, 7, 18, 37, 33, 78, 82, 28, 25, 12, 40, 3, 20, 45, 55, 20, 21 ]
#1) Con la lista de números, cada uno de ellos calcular su Cuadrado
#2) Usando una lista de números, imprimir si es par o impar
#3) Imprimir sólo los números donde su cubo sea mayor a 5000

# 1 Calcular el cuadrado de cada número en la lista
cuadrados = [num ** 2 for num in nums]
print("Cuadrados de los números:", cuadrados)

# 2 Imprimir si cada número en la lista es par o impar
for num in nums:
    if num % 2 == 0:
        print(f"{num} es par")
    else:
        print(f"{num} es impar")

# 2 Imprimir si cada número en la lista es par o impar
cubos_mayor_5000 = [num for num in nums if num**3 > 5000]
print("Números cuyo cubo es mayor a 5000:", cubos_mayor_5000)
