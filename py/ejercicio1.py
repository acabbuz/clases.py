"""
Operadores
"""

# Operadores aritmetricos
print(f"Suma : 10 + 3 = {10 + 3}")
print(f"Resta : 10 - 3 = {10 - 3}")
print(f"Multiplicación : 10 * 3 = {10 * 3}")
print(f"División : 10 / 3 = {10 / 3}")
print(f"Modulo 10 % 3 = {10 % 3}")
print(f"Exponente 10 ** 3 = {10 ** 3}")
print(f"División entera 10 // 3 = {10 // 3}")

#Operadores de Comparación
print(f"Igualdad : 10 == 3 es {10 == 3} ")
print(f"Desigualdad : 10 != 3 es {10 != 3} ")
print(f"Mayor que: 10 > 3 es {10 > 3} ")
print(f"Mayor o igual  que: 10 >= 10 es {10 >= 10} ")
print(f"Menor que: 10 < 3 es {10 < 3} ")
print(f"Menor o igual que: 10 <= 3 es {10 <= 3} ")

# Operadores Lógicos
print(f"AND : 10 + 3 == 13 and 5 - 1 == 4 : {10 + 3 == 13 and 5 - 1 == 4}") #Los dos son True
print(f"OR : 10 + 3 == 13 or 5 - 1 == 4 : {10 + 3 == 13 or 5 - 1 == 4}")    #Uno de los dos es True
print(f"not : 10 + 3 == 14 es : {not 10 + 3 == 14}") 
#Combierte algo que es true en false y al contrario 10 + 3 tenemos que es 14 y como es False al negarlo lo volvemos True

#Operadores de Asignación 
my_number = 11  # Asignación 
print(my_number)
my_number += 1  # Suma y asignación 
print(my_number)
my_number -= 1  # Resta y Asignación 
print(my_number)
my_number *= 2  # Multiplicación y Asignación 
print(my_number)
my_number /= 2  # División y Asignación 
print(my_number)
my_number %= 2  # Módulo y Asignación 
print(my_number)
my_number **= 1 # Exponente y Asignación 
print(my_number)
my_number //= 1 # División entera y Asignación 
print(my_number)

#Operadores de identidad (Nos sirve para comparar el valor de la pposición de la memoria)
my_new_number = my_number
print(f"my_number is my_new_number = {my_number is my_new_number}")
print(f"my_number is not my_new_number = {my_number is not my_new_number}")

#Operadores de pertenenecia
print(f" 'u' in 'moure' : {'u' in 'moure'}")
print(f" 'b' in 'moure' : {'u' not in 'moure'}")

#OIperadores bit
a = 10 #
b = 3  #
c= 10 
print("hola")