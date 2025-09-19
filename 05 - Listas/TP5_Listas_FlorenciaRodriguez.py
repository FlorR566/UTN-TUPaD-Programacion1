import random

print("\n ----------------- Ejercicio 1 ----------------- \n")
# Crear una lista con las notas de 10 estudiantes. 
# Mostrar la lista completa.
# Calcular y mostrar el promedio.
# Indicar la nota más alta y la más baja. 

lista_notas = [6,4,8,9,7,6,8,9,7,3]
suma_notas = 0
mayor_nota = 0
menor_nota = lista_notas[0]

print(lista_notas, "\n")

for nota in lista_notas:
  suma_notas += nota 

  if nota >= mayor_nota:
    mayor_nota = nota
  
  if nota <= menor_nota:
    menor_nota = nota

promedio_notas = suma_notas / (len(lista_notas))
print("El promedio de las notas es: ",promedio_notas, "\n")
print(f"La nota más alta es: {mayor_nota} y la más baja: {menor_nota} \n")



print("\n ----------------- Ejercicio 2 ----------------- \n")
# Pedir al usuario que cargue 5 productos en una lista.
# Mostrar la lista ordenada alfabéticamente. (Usar sorted())
# Preguntar al usuario qué producto desea eliminar y actualizar la lista. 

lista_productos = []

print("Por favor ingrese 5 productos \n")
for i in range(0,5):
  lista_productos.append(input(f"Por favor ingrese el {i+1} producto: ").lower())
  print( )

print(f"Lista ingresada: \n", lista_productos, "\n")
lista_ordenada = sorted(lista_productos)
print(f"Lista ordenada: \n", lista_ordenada, "\n")

prod_eliminado = input("Qué producto desea eliminar?: ").lower()

if prod_eliminado in lista_ordenada: 
  lista_ordenada.remove(prod_eliminado)
  print("\nEl listado queda así: \n", lista_ordenada, "\n")
else: 
  print("El producto no está en la lista.")



print("\n ----------------- Ejercicio 3 ----------------- \n")
# Genera una lista con 15 números enteros al azar entre 1 y 100.
# Crea una lista con los pares y otra con los impares.
# Muestra cuántos números tiene cada lista. 

lista_aleatoria = [random.randint(1,100) for i in range(15)] # crea una lista con 15 números aleatorios del 1 al 100
lista_pares = []
lista_impares = []

print("Lista original: \n", lista_aleatoria, "\n")

for i in lista_aleatoria:
  if i % 2 == 0:
    lista_pares.append(i)
  else: 
    lista_impares.append(i)

print(f"\nLa lista tiene {len(lista_pares)} números PARES: \n {lista_pares}\n")
print(f"\nLa lista tiene {len(lista_impares)} números IMPARES: \n {lista_impares}\n")


print("\n ----------------- Ejercicio 4 ----------------- \n")
# Dada una lista con valores repetidos.
# Crear una nueva lista sin elementos repetidos.
# Mostrar el resultado. 

datos = [1,3,5,3,7,1,9,5,3]
nueva_lista = []
print("Listado original:", datos, "\n")

for elem in datos:
  if elem in datos and not elem in nueva_lista:
    nueva_lista.append(elem)
  
print("Lista depurada:", nueva_lista, "\n")


print("\n ----------------- Ejercicio 5 ----------------- \n")
# Crear una lista con los 8 estudiantes presentes en clase.
# Preguntar al usuario si quiere agregar a un estudiante o eliminar uno existente. 
# Mostrar la lista final actualizada. 

listado_estudiantes = []

print ("\n Por favor ingresar los nombres de los 8 estudiantes: \n")

for i in range(1,9):
  listado_estudiantes.append(input(f"Ingrese al {i}º estudiante: ").title())

agregar = input("Quiere AGREGAR otro alumno? Escriba S (si) y N (no): \n")

if agregar == "s":
  listado_estudiantes.append(input("Ingrese el nuevo alumno: \n").title())
else: 
  print("No se agregaron alumnos.\n")
  print(f"\n Lista: {listado_estudiantes} \n")

eliminar = input("Quiere ELIMINAR un alumno existente? Ingrese S (si) o N (no): \n").lower()

if eliminar == "s":
  alumno_eliminado = (input("Ingrese el nombre del alumno a eliminar: ").title())
  
  if alumno_eliminado in listado_estudiantes:
    listado_estudiantes.remove(alumno_eliminado)
    print(f"\n Lista final actualizada: {listado_estudiantes}")
  else:
    print("El alumno no está en la lista.")
else: 
  print("No se eliminaron alumnos. \n")
  print(f"\n Lista: {listado_estudiantes} \n")



print("\n ----------------- Ejercicio 6 ----------------- \n")
# Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha.
# El último pasa a ser el primero.

lista = [1,2,3,4,5,6,7]
ultimo_elem = lista[-1]
lista_corrida = []
lista_corrida.append(ultimo_elem)

for elem in lista:
  lista_corrida.append(elem)
  if elem == lista[-2]:
    break

print(" Lista original: \n" , lista)
print("\n Lista con los números corridos hacia la derecha: \n" , lista_corrida)


####  Resolución Clase:  #### 
# numeros = [1,2,3,4,5,6,7]
# ultimo_numero = numeros[-1] # --> 7
# resto = numeros[:len(numeros)-1] # --> [1,2,3,4,5,6]
# nueva_lista = [ultimo_numero] + resto  # --> [7] + [1,2,3,4,5,6] =>[7,1,2,3,4,5,6]

# print(nueva_lista) # --> [7,1,2,3,4,5,6]


print("\n ----------------- Ejercicio 7 ----------------- \n")
# Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# Calcular el promedio de las mínimas y el de las máximas. 
# Mostrar en qué día se registró la mayor amplitud térmica. 

# OJO si me piden que sea de 7x2 son 7 filas y 2 columnas.

# NOTA: La matriz de abajo es de 2x7, tiene 2 filas y 7 columnas.

temperaturas = [
  [8,7,4,6,5,8,11],          # Temperaturas mínimas
  [20,21,20,25,23,21,25]     # Temperaturas máximas
]

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo" ]
suma_minimas = 0
suma_maximas = 0
lista_amplitudes = []
index = 0
i = 0
mayor_amplitud = [temperaturas[0][0]]                     # Asignamos como primer valor la temperatura mínima del día 1

# Cálculo de temperaturas promedio y amplitud:
for temp in temperaturas[0]:                              # Solo iteramos en fila 1
  suma_minimas += temp                                    # Sumatoria temperaturas en fila 1
  amplitud = temperaturas[1][index] - temp                # Guardamos en valor el resultado de máximo - mínimo por día
  lista_amplitudes.append(amplitud)                       # Agregamos la amplitud del día al listado de amplitudes
  if mayor_amplitud[0] < lista_amplitudes[index]:
    mayor_amplitud[0] = lista_amplitudes[index]            # Actualizamos mayor_amplitud si en la lista de amplitudes se guarda una amplitud más grande a la actual
    index += 1

for temp in temperaturas[1]:
  suma_maximas += temp

# Cálculo de los promedios: 
promedio_minimas = round(suma_minimas / len(temperaturas[0]), 2)
promedio_maximas = round(suma_maximas / len(temperaturas[1]), 2)

print(f"Promedio temperaturas Mínimas: {promedio_minimas} \n")
print(f"Promedio temperaturas Máximas: {promedio_maximas} \n")

# Obtenemos el día com mayor amplitud térmica: 
for temp in lista_amplitudes: 
  if temp != mayor_amplitud[0]:
    #print(i, temp)
    i += 1
  else: 
    # print(i, temp, "TEMPERATURA MAXIMA")
    break

print(f"El día de más amplitud térmica es el {(dias_semana[i]).upper()} con {mayor_amplitud[0]}º \n")


print("\n ----------------- Ejercicio 8 ----------------- \n")
# Crear una matriz con las notas de 5 estudiantes en 3 materias.
# Mostrar el promedio de cada estudiante.
# Mostrar el promedio de cada materia. 


notas = [
  [7,9,8],
  [4,7,7],
  [8,7,9], 
  [5,6,5],
  [8,8,9], 
]

promedio = []
i = 0
n = 0
suma = 0

print("PROMEDIO POR ESTUDIANTE: \n")
for alumno in notas:
  for nota in alumno:
    promedio_estudiante = round((sum(alumno) / len(notas[0])),2)
  print(f"El promedio del estudiante {i+1} es: {promedio_estudiante}\n")
  i += 1

print("PROMEDIO POR MATERIA: \n")
for materia in notas[n]:
  for j in notas:
     nota = j[n]
     suma += nota
  print(f"El promedio de la materia {n+1} es: {round((suma / len(notas)),2)}\n")
  suma = 0
  n += 1


print("\n ----------------- Ejercicio 9 ----------------- \n")
# Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# Inicializarlo con guiones "-" representando casillas vacías.
# Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# Mostrar el tablero después de cada jugada.

### TA-TE-TI

matriz = []

# Variables de control:
jugador_1 = "X"
jugador_2 = "O"

# Cración del tablero:
for i in range(3):           # filas
    fila = []
    for j in range(3):       # columnas
        fila.append("-")
    matriz.append(fila)

turno = jugador_1

print("Juguemos al TA-TE-TI 😎 \n")
print("Turno: Jugador 'X' \nMarcá la ubicación, ingresando 1,2 o 3 en [fila][columna] \n")

## NOTA: este juego toma valores (1,2,3):

for fila in matriz:
  for col in fila:
    print(col, end=" ")
  print( )

# Inicio del juego:
for i in range(1,10):
  fila = int(input("\nIngresá la fila: "))
  columna = int(input("Ingresá la columna: "))
  # Validación de datos: 
  if fila < 1 or fila > 3 and columna < 1 or columna > 3:
    print("⚠️ Error! valor inválido, ingresá otras coordenadas.")
    continue
  elif matriz[fila -1][columna - 1] != "-":
    print("⚠️ Casillero ocupado, elegí otro")
    continue
  # Se muestra el tablero:
  else:
    matriz[fila -1][columna -1] = turno
    print( ) 
    for fila in matriz:
      for col in fila:
        print(col, end=" ")
      print( )
  # Cambio de jugador:
  if turno == jugador_1:
     turno = jugador_2
  else:
     turno = jugador_1

  print(f"\nSiguiente turno jugador: '{turno}' \n")



print("\n ----------------- Ejercicio 10 ----------------- \n")
# Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# Mostrar el total vendido por cada producto.
# Mostrar el día con mayores ventas totales.
# Indicar cuál fue el producto más vendido en la semana.

ventas = [
  [18,15,20,12,18,25,14],  # Producto 1
  [3,8,12,10,15,9,7],      # Producto 2
  [20,18,15,22,19,17,21],  # Producto 3
  [12,14,11,18,20,13,15],  # Producto 4
]

# ---- Mostrar el total vendido por cada producto:
# primero tengo que recorrer cada fila e ir sumando 
max = 0
pmax = 0

# for i, producto in enumerate(ventas):  # en i nos devuelve el número de producto y como segundo parámetro devuelve la lista
#   total = 0
#   for dia in producto:
#     total += dia
#   print(f"ventas: #{i+1} {total}")

### Esta es otra forma más acotada de hacer lo mismo de arriba
for i, producto in enumerate(ventas):
  total = sum(producto)                          # Sum devuelve la suma de una lista 
  print(f"ventas del producto # {i+1}: {total} \n")
  if total > max:
    max = total
    pmax = i + 1


# ---- Mostrar el día con mayores ventas totales: 
max = 0
dmax = 0

for dia in range(7): # va de 0 a 6
  total = 0
  for prod in range(4):
    total += ventas[prod][dia]
  #El total de lo que se vendió durante ese día.
  if total > max:
    max = total
    dmax = dia + 1
print(f"El día con mayor cant. de ventas fué el {dmax}º \n")

# ---- Indicar cuál fue el producto más vendido en la semana: 
print(f"El producto más vendido fué el {pmax}. \n")