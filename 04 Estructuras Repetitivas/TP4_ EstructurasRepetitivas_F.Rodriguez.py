from statistics import mode, median, mean
import random


print("Punto 1 -----------")
# Crea un programa que imprima en pantalla todos los números entero desde 0 hasta 100 (incluyendo ambos extramos), en orden creciente, mostrando un número por línea. 

for n in range (0,100 +1):
  print(n)



print("Punto 2 -----------")
# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene. 

num = input("Por favor ingrese un número: ")

largo = len(num)
print(f"El largo del número es: {largo}")



print("Punto 3 -----------")
# Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores. 

valor_inicial = int(input("Por favor ingrese un valor inicial: "))
valor_final = int(input("Por favor ingrese un valor final: "))
acumulador = 0

for n in range (valor_inicial+1, valor_final):
  acumulador += n # acumulador = acumulador + n
  
print(f"La suma entre de los números comprendidos entre {valor_inicial} y {valor_final} es: {acumulador}")


    
print("Punto 4 -----------")
# Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0. 

num = int(input("Por favor ingrese un número: "))
count = 0

while num != 0:
  count = count + num
  num = int(input("Por favor ingrese otro número, o escriba 0 para salir:"))

print (f"La sumatoria de números ingresados es: {count}")



print("Punto 5 -----------")
# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

numero_aleatorio = random.randint(0,9) 
acum = 1
print("Juego: adivina un número aleatorio entre 0 y 9")
num = int(input("Por favor ingresa un número: "))

while num != numero_aleatorio and acum < 10:
   num = int(input(f"😞 No es el número, intento nº{acum+1}: "))
   acum = acum + 1

if num == numero_aleatorio:
   print(f"🎉 😎 🎉 ADIVINASTE!! EL NUMERO ES {numero_aleatorio}🎉 😎 🎉")
   print(f"Intentos: {acum}")
else:
   print("Perdiste, fueron muchos intentos 😞 😞 😞 😞 ")
   


print("Punto 6 -----------")
# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente. 

for n in range (100,0,-2):
  print(n)



print("Punto 7 -----------")
# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario. 

num = int(input("Por favor ingrese un número mayor a 0: "))
suma = 0

if num >= 0:
  for i in range (0,num+1):
    print(f"vuelta número {i + 1}")  
    suma = suma + i 

    print(f"Suma acumulada igual a {suma}")
else:
  print("Error: ingrese un número positivo")
  


print("Punto 8 -----------")
# Escribe un programa que permita al usuario ingresar 100 números enteros. 
# Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos positivos. 
# (Nota: para probar el programa pudes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un sólo cambio).

pares = 0
negativos = 0
positivos = 0 

for i in range(1, 100+1):
  num = int(input(f"Por favor ingrese el {i}º número: "))
  if num < 0: 
    if num % 2 == 0:
      pares += 1
      negativos += 1
    else:
      negativos += 1
  else:
    if num % 2 == 0:
      pares += 1
      positivos += 1
    else:
      positivos += 1

print(f"El total de números pares es: {pares}, el total de negativos es: {negativos} y el total de positivos es: {positivos}")




print("Punto 9 -----------")
# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. 
# (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor). 

count = 0
num = 0
total_numeros = 100

for i in range (0,total_numeros):
  num = int(input(f"Por favor ingrese el {i+1}º número entero: "))
  count += num  # count = count + num

print(f"La media es: {count/total_numeros}")



print("Punto 10 -----------")
# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

num = int(input("Por favor ingrese un número: "))
valor_inverso = 0
resto = num

while resto > 0:
	valor_inverso = valor_inverso * 10 + resto % 10
	resto = (resto - resto % 10) // 10 # Aplico división entera (floor division) "//" devuelve el cociente entero sin decimales. 

print(f"El valor inverso del número {num} es {valor_inverso} ")



