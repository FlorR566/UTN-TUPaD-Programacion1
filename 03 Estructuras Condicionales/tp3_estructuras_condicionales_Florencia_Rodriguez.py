from statistics import mode, median, mean
import random
import math


# Ejercicio 1:
print("_____________________________________________________________________")
edad_usuario = int(input("Por favor introduzca su edad: "))

if edad_usuario >= 18:
  print("Es mayor de edad")


# Ejercicio 2:
print("_____________________________________________________________________")
nota_usuario = int(input("Por favor ingrese su nota para saber si aprobó o desaprobó: "))

if nota_usuario >= 6:
  print("Aprobado")
else: 
  print("Desaprobado")


# Ejercicio 3:
print("_____________________________________________________________________")
numero_ingresado = int(input("Por favor ingrese un número: "))

if numero_ingresado % 2 == 0:
  print("Ha ingresado un número par")
else:
  print("Por favor ingrese un número par")


# Ejercicio 4:
print("_____________________________________________________________________")
print("Ahora queremos saber a qué rango etario pertence: ")
edad_usuario = int(input("Por favor introduzca su edad: "))

if edad_usuario > 0 and edad_usuario < 12:
  print("El usuario pertenece a la categoría Niño/a")
elif edad_usuario >= 12 and edad_usuario < 18:
  print("El usuario pertenece a la categoría Adolescente")
elif edad_usuario >= 10 and edad_usuario < 30:
  print("El usuario pertenece a la categoría Adulto/a joven")  
elif edad_usuario >= 30:
  print("El usuario pertenece a la categoría Adulto/a")
else: 
  print("Por favor ingrese un valor mayor a 0")


# Ejercicio 5:
print("_____________________________________________________________________")
contraseña = input("Por favor introduzca una contraseña de entre 8 y 14 caracteres: ")
largo = len(contraseña)

if (largo >= 8 and largo <= 10 ):
  print("Ha ingresado una contraseña correcta")
else:
  print("ERROR: Por favor ingrese una contraseña de entre 8 y 14 caracteres")


# Ejercicio 6:
print("_____________________________________________________________________") 
numeros_aleatorios = [random.randint(1,100) for i in range(50)] # crea una lista con 50 números aleatorios del 1 al 100

print(f"NUMEROS ALEATORIOS: {numeros_aleatorios}")

moda = mode(numeros_aleatorios) # valor que aparece con mayor frecuencia en los datos
mediana = median(numeros_aleatorios) # valor que se encuentra justo en medio, ordenando los datos de menor a mayor
media = mean(numeros_aleatorios) # promedio de todos los valores 

print("La moda es: ", moda)
print("La mediana es: ", mediana)
print("La media es: ", media)

if (media > mediana and mediana > moda): 
  print("Hay sesgo positivo o a la derecha")
elif(media < mediana and mediana < moda):
  print("Hay sesgo negativo o a la izquierda")
elif(media == mediana == moda):
  print("Sin sesgo")


# Ejercicio 7:
print("_____________________________________________________________________")
dato_ingresado = input("Por favor ingrese una palabra o frase: ")

ultima_letra = dato_ingresado[-1].lower()

if ultima_letra == "a":
  print(f"{dato_ingresado} !")
elif ultima_letra == "e":
  print(f"{dato_ingresado} !")
elif  ultima_letra == "i":
  print(f"{dato_ingresado} !")
elif ultima_letra == "o":
  print(f"{dato_ingresado} !")
elif ultima_letra == "u":
  print(f"{dato_ingresado} !")
else:
  print(dato_ingresado)


# Ejercicio 8:
print("_____________________________________________________________________")
nombre_ingresado = input("""Por favor ingrese su nombre seguido de una de las siguientes opciones: 
    Escriba 1 si lo quiere todo en mayúsculas. Ejemplo: PEDRO
    Escriba 2 si lo prefiere en minúsculas. Ejemplo: pedro
    Escriba 3 si solo quiere la primer letra en mayúscula. Ejemplo: Pedro
    : """)

opcion_elegida = nombre_ingresado[-1].lower() # Obtenemos el último carácter

nombre_a_formatear = nombre_ingresado[:-1] # Elimina el último carácter

if opcion_elegida == "1":
  print(nombre_a_formatear.upper())
elif opcion_elegida == "2":
  print(nombre_a_formatear.lower())
elif opcion_elegida == "3":
  print(nombre_a_formatear.title()) # Ojo capitalize() solo deja en mayúscula la primera letra de toda la cadena de strings.
else: 
  print("Error: No especificó una de las tres opciones.")


# Ejercicio 9:
print("_____________________________________________________________________")
print("Ahora usamos la escala de Richter para saber qué impacto tiene un terremoto: ")

magnitud_terremoto = float(input("Por favor ingrese la magnitud del terremoto: "))

if magnitud_terremoto < 3 : 
  print(f' "Muy leve" (imperceptible)')
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4: 
  print(f' "Leve" (ligeramente perceptible)')
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5: 
  print(f' "Moderado" (sentido por personas, pero generalmente no causa daños)')
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
  print(f' "Fuerte" (puede causar daños en estructuras débiles)')
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7: 
  print(f' "Muy Fuerte" (puede causar daños significativos)')
elif magnitud_terremoto >= 7:
  print(f' "Extremo" (puede causar graves daños a gran escala)')


# Ejercicio 10:
print("_____________________________________________________________________")
print("AHORA QUEREMOS SABER EN QUE ESTACION DEL AÑO SE ENCUENTRA: ")
hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").lower()
mes = int(input("¿En qué mes se encuentra? Por favor escribirlo en números: "))
dia = int(input("¿Qué día es? Por favor escribirlo en números: "))

if hemisferio == "n":
  # Meses con cambio de estación
  if mes == 3 and (dia >= 1 and dia <= 20): 
    print("Es Invierno")
  elif mes == 3 and (dia >= 21 and dia <= 31): 
    print("Es Primavera")
  elif mes == 6 and (dia >= 1 and dia <= 20):
    print("Es Primavera")
  elif mes == 6 and (dia >= 21 and dia <= 30):
    print("Es Verano")
  elif mes == 9 and (dia >= 1 and dia <= 20): 
    print("Es Verano")
  elif mes == 9 and (dia >= 21 and dia <= 30):
     print("Es Otoño")
  elif mes == 12 and (dia >= 1 and dia <= 20):
    print("Es Otoño")
  elif mes == 12 and (dia >= 21 and dia <= 31):
    print("Es Invierno")
  # Meses completos
  if mes == 1 and (dia >= 1 and dia <= 30):
    print("Es Invierno")
  elif mes == 2 and (dia >= 1 and dia <= 28):
    print("Es Invierno")
  elif mes == 4 and (dia >= 1 and dia <= 30):
    print("Es Primavera")
  elif mes == 5 and (dia >= 1 and dia <= 31):
    print("Es Primavera")
  elif mes == 7 and (dia >= 1 and dia <= 31):
    print("Es Verano")
  elif mes == 8 and (dia >= 1 and dia <= 31):
    print("Es Verano")
  elif mes == 10 and (dia >= 1 and dia <= 31): 
    print("Es Otoño")
  elif mes == 11 and (dia >= 1 and dia <= 30):
    print("Es Otoño")
elif hemisferio == "s":
  # Meses con cambio de estación
  if mes == 3 and (dia >= 1 and dia <= 20): 
    print("Es Verano")
  elif mes == 3 and (dia >= 21 and dia <= 31): 
    print("Es Otoño")
  elif mes == 6 and (dia >= 1 and dia <= 20):
    print("Es Otoño")
  elif mes == 6 and (dia >= 21 and dia <= 30):
    print("Es Invierno")
  elif mes == 9 and (dia >= 1 and dia <= 20): 
    print("Es Invierno")
  elif mes == 9 and (dia >= 21 and dia <= 30):
     print("Es Primavera")
  elif mes == 12 and (dia >= 1 and dia <= 20):
    print("Es Primavera")
  elif mes == 12 and (dia >= 21 and dia <= 31):
    print("Es Verano")
  # Meses completos
  if mes == 1 and (dia >= 1 and dia <= 30):
    print("Es Verano")
  elif mes == 2 and (dia >= 1 and dia <= 28):
    print("Es Verano")
  elif mes == 4 and (dia >= 1 and dia <= 30):
    print("Es Otoño")
  elif mes == 5 and (dia >= 1 and dia <= 31):
    print("Es Otoño")
  elif mes == 7 and (dia >= 1 and dia <= 31):
    print("Es Invierno")
  elif mes == 8 and (dia >= 1 and dia <= 31):
    print("Es Invierno")
  elif mes == 10 and (dia >= 1 and dia <= 31): 
    print("Es Primavera")
  elif mes == 11 and (dia >= 1 and dia <= 30):
    print("Es Primavera")
else: 
    print("Error: Por favor revise el hemisferio ingresado.")
 
