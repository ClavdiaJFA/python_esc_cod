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


#Resultados:
#Cuadrados de los números: [4, 25, 225, 441, 256, 324, 49, 324, 1369, 1089, 6084, 6724, 784, 625, 144, 1600, 9, 
#400, 2025, 3025, 400, 441]
#2 es par
#5 es impar
#15 es impar
#21 es impar
#16 es par
#18 es par
#7 es impar
#18 es par
#37 es impar
#33 es impar
#78 es par
#82 es par
#28 es par
#25 es impar
#40 es par
#3 es impar
#20 es par
#45 es impar
#55 es impar
#20 es par
#21 es impar
#Números cuyo cubo es mayor a 5000: [21, 18, 18, 37, 33, 78, 82, 28, 25, 40, 20, 45, 55, 20, 21]
