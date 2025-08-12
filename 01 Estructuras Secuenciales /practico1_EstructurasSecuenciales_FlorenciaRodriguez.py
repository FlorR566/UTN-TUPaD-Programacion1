###########################################################################################
# Ejercicio 1) Programa que imprime en pantalla el mensaje: "Hola Mundo!"
print( "Hola Mundo!")

###########################################################################################
# Ejercicio 2) Programa que pide al usuario su nombre y lo imprime en pantalla usando un saludo con su nombre ingresado. 
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

###########################################################################################
# Ejercicio 3) Programa quee pide al usuario nombre, apellido, edad y dirección e imprime un string con los datos. 
nombre = input ("Ingrse su nombre: ")
apellido = input ("Ingrse su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre}, tengo {edad} años y vivo en {residencia}.")

###########################################################################################
# Ejercicio 4) Programa que pide al usuario el radio de un círculo e imprime en pantalla su área y su perímetro.

radio = int(input("Ingrese el radio del círculo: "))
import math # Importamos el modulo de matemáticas
area = round(math.pi * (radio**2) , 2)
print(f"El área del círculo es: {area}")

perimetro = round(2 * math.pi * radio , 2)
print(f"El perímetro del círculo es: {perimetro}")


###########################################################################################
# Ejercicio 5) Programa que solicita al usuario que ingrese una cantidad de segundos y muestra en pantalla a cuantas hs equivale.

segundos = int(input("Por favor ingrese la cantidad de segundos: "))
print(segundos)
segundos_por_hora = 3600

horas = float(segundos / segundos_por_hora)

print(f"Los {segundos} segundos ingresados equivalen a {horas} horas")


###########################################################################################
# Ejercicio 6) Programa que pide al usuario un número e imprime en pantalla la tabla de multiplicar de dicho número.

numero = int(input ("Ingrese un número: "))

print (f"{numero} * 1 es igual a: ", numero * 1)
print (f"{numero} * 2 es igual a: ", numero * 2)
print (f"{numero} * 3 es igual a: ", numero * 3)
print (f"{numero} * 4 es igual a: ", numero * 4)
print (f"{numero} * 5 es igual a: ", numero * 5)
print (f"{numero} * 6 es igual a: ", numero * 6)
print (f"{numero} * 7 es igual a: ", numero * 7)
print (f"{numero} * 8 es igual a: ", numero * 8)
print (f"{numero} * 9 es igual a: ", numero * 9)
print (f"{numero} * 10 es igual a: ", numero * 10)


###########################################################################################
# Ejercicio 7) Programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 

num1 = int(input("Ingrese un número, distinto de cero: "))
num2 = int(input("Ingrese un segundo número, distinto de cero: "))

suma = num1 + num2 

resta = num1 - num2

multiplicacion = num1 * num2

division = num1 / num2 

print(f"""
  La suma entre {num1} y {num2} es: {suma}
  La resta entre {num1} y {num2} es: {resta}
  La multiplicacion entre {num1} y {num2} es: {multiplicacion}
  La division entre {num1} y {num2} es: {division}
    """)

###########################################################################################
# Ejercicio 8) Programa que pide al usuario su altura, su peso e imprime por pantalla su índice de masa corporal. 

peso = int(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / altura **2 

print("El índice de masa corporal es: ", imc)

###########################################################################################
# Ejercicio 9) Programa que pide al usuario una temperatura en grados Celsius e imprime por pantalla su equivalente en grados Fahrenheit.

celsius = int(input ("Ingrese la temperatura en Celsius: "))

fahrenheit = (9/5) * celsius + 32

print (f"{celsius} grados Celsius equivalen a {fahrenheit} grados Farenheit")

###########################################################################################
# Ejercicio 10) Programa que pide al usuario 3 números e imprime por pantalla el promedio de dichos números. 

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = (num1 + num2 + num3 ) / 3

print(f"El promedio de {num1} + {num2} + {num3} es igual a: ", promedio)

