import math

# Funcion para saltar el renglón entre un ejercicio y otro: 
def saltar_renglon(i):
  print(f"\n________________________________ Ejercicio {i} ________________________________") 



saltar_renglon(1) # Ejercicio 1
# Función para imprimir un mensaje:
def imprimir_hola_mundo(mensaje):
  print(f"\n{mensaje}")

# Programa principal:
imprimir_hola_mundo("Hola Mundo!")



saltar_renglon(2) # Ejercicio 2 
# Función para imprimir un mensaje:
def saludar_usuario(nom):
  print(f"\nHola {nom}!")

# Programa principal:
print("\n *** SALUDO PERSONALIZADO *** \n")
nombre = input("\nPor favor ingrese su nombre: ")
saludar_usuario(nombre.title())



saltar_renglon(3) # Ejercicio 3
# Función que recibe 4 parámetros e imprime un mensaje:
def informacion_personal(nombre, apellido, edad, residencia):
  print(f"\nSoy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Programa principal:
print("\n *** INFORMACION PERSONAL *** \n")
nombre = input("\nSu nombre: ").title()
apellido = input("Su apellido: ").title()
edad = input("su edad: ")
residencia = input("Su residencia: ").title()

informacion_personal(nombre, apellido, edad, residencia)



saltar_renglon(4) # Ejercicio 4
# Función que recibe el radio e imprime el área de un círculo:
def calcular_area_circulo(radio):
  area = math.pi * (radio ** 2)
  print(f"\n El área del círculo es: {area:.2f}")     # ':.2f' sirve para mostrar una cantidad de decimales específicos sin cambiar el valor original.

# Función que recibe el radio e imprime el perímetro de un círculo:
def calcular_perimetro_circulo(radio):
  perimetro = math.pi * (radio * 2)
  print(f"\n El perímetro del círculo es: {perimetro:.2f}")     # ':.2f' sirve para mostrar una cantidad de decimales específicos sin cambiar el valor original.

# Programa principal:
print("\n *** CALCULADORA DE AREA Y PERIMETRO DE UN CIRCULO *** \n")
radio = float(input("\nPor favor ingrese el radio (en enteros): "))

calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)



saltar_renglon(5) # Ejercicio 5
# Función que recibe una cantidad de segundos y devuelve la cantidad en horas correspondientes:
def segundos_a_horas(seg):
   return round(seg / 3600, 2)

# Programa principal:
print("\n *** CONVERSOR DE SEGUNDOS A HORAS *** \n")
segundos = float(input("\nIngrese la cantidad de segundos a convertir (entero): "))

print(f"\nLos segundos ingresados equivalen a {segundos_a_horas(segundos)} horas.\n")


saltar_renglon(6) # Ejercicio 6
# Función que devuelve la tabla de multiplicar 
def tabla_multiplicar(numero):
  print(f"\n *** TABLA DE MULTIPLICAR DEL: {numero} *** \n")
  for i in range(1,11):
    print(f" {i} * {numero} = {i * numero}")

# Programa principal:
numero = int(input("\nPor favor ingrese un número del 1 al 10: "))

tabla_multiplicar(numero)



saltar_renglon(7) # Ejercicio 7
# Función que devuelve una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
def operaciones_basicas(a, b):
  tupla = ( a + b, a - b, a * b, a / b)
  print(f"\nLa suma de {a} y {b} = {tupla[0]:.2f}")
  print(f"\nLa resta de {a} y {b} = {tupla[1]:.2f}")
  print(f"\nLa multiplicación de {a} y {b} = {tupla[2]:.2f}")
  print(f"\nLa división de {a} y {b} = {tupla[3]:.2f}")

# Programa principal:
print("\n *** CALCULADORA DE SUMA - RESTA - MULTIPLICACION - DIVISION *** \n")
numero_1 = float(input("\nIngrese el primer número: "))
numero_2 = float(input("\nIngrese el segundo número: "))

operaciones_basicas(numero_1, numero_2)



saltar_renglon(8) # Ejercicio 8

# Función que calcula el IMC:
def calcular_imc(peso, altura):
 return peso / (altura ** 2)

# Programa principal:
print("\n *** CALCULADORA DE IMC *** \n")
peso = float(input("\nIngrese el peso en kilogramos: "))
altura = float(input("\nIngrese la altura en metros: "))

print(f"\nSegún su peso: {peso} y altura: {altura}, su IMC es: {calcular_imc(peso, altura):.2f}.")



saltar_renglon(9) # Ejercicio 9
# Función que convierte de Celsius a Fahrenheit:
def celsius_a_fahrenheit(celsius):
  return (celsius * 1.8) + 32

# Programa principal: 
print("\n *** CALCULADORA DE CELSIUS A FAHRENHEIT *** \n")
celsius = float(input("\nIngrese los grados Celsius: "))

print(f"\nResultado: {celsius}º Celsius equivalen a {celsius_a_fahrenheit(celsius)}º Fahrenheit.")



saltar_renglon(10) # Ejercicio 10
# Función que calcula el promedio:
def calcular_promedio(a,b,c):
  return (a+b+c)/3 

# Programa principal:
print("\n *** CALCULADORA DE PROMEDIOS *** \n")
num1 = float(input("\nIngrese el primer número: "))
num2 = float(input("\nIngrese el segundo número: "))
num3 = float(input("\nIngrese el tercer número: "))

print(f"\nEl promedio de {num1}, {num2} y {num3} es: {calcular_promedio(num1, num2, num3):.2f}")



