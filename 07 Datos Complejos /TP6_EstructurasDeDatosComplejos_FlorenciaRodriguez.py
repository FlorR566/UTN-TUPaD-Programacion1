from collections import Counter


def saltar_renglon_Ejercicio(i): # saltamos de renglón entre un ejercicio y otro: 
  print(f"\n________________________________ Ejercicio {i} ________________________________\n") 



saltar_renglon_Ejercicio(1) 
# Dado el siguiente diccionario, añadir las frutas con sus respectivos precios.
precios_frutas = {"Banana" : 1200, "Ananá" : 2500, "Melón": 3000, "Uva":1450} 
print(precios_frutas)

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(f"Añadimos frutas y precios: \n{precios_frutas}\n")



saltar_renglon_Ejercicio(2)
# Siguiendo con el mismo diccionario que resulta en el punto anterior, actualizar los precios de las siguientes frutas: 
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800
print(f"Actualizamos precios: \n{precios_frutas}\n")



saltar_renglon_Ejercicio(3)
# Siguiendo con el mismo diccionario que resulta en el punto anterior, crear una lista que contenga únicamente las frutas son los precios. 
solo_frutas = list(precios_frutas.keys())
print(f"Listado de frutas: \n{solo_frutas}\n")


saltar_renglon_Ejercicio(4)
# Escribir un programa que permita almacenar y consultar números de teléfono.
    # Permitir al usuario cargar 5 contactos con su nombre como clave y número como valor.
    # Luego, pedir un nombre y mostrarle el número asociado, si existe. 

contactos = {}

def buscar_telefono(nombre):
  if nombre in contactos:
    print(f"\nEl número de {nombre.title()} es: {contactos[nombre]}\n")
  else: 
    print(f"Error - El nombre no está dentro de los contactos. ")

# Programa principal
print("Programa para agendar a 5 contactos: \n")
for n in range(5):
  # Validar nombre
  while True:
    nombre = input(f"Ingrese el {n + 1}º NOMBRE: ").strip().lower()
    if nombre.isalpha() and not nombre in contactos:  # Solo letras y no debe estar en contactos
      break
    elif nombre in contactos:
      print("⚠️ Este nombre ya existe, ingrese otro.")
      continue
    else:
      print("⚠️ El nombre solo debe contener letras. Intente de nuevo.")
      continue

  # Validar teléfono
  while True:
    telefono = input("Ingrese el TELEFONO (solo números): ").strip()
    if telefono.isdigit():
      break
    print("⚠️ El teléfono debe contener solo número.")

  contactos[nombre] = telefono

print(f"\n📞 Contactos guardados: {contactos}\n")

while True:
  opcion = input("\nIngrese un contacto a buscar, o escriba 'Salir': ").lower()
  if opcion == "salir":
    print("Saliendo...\n")
    break
  else:
    buscar_telefono(opcion)


saltar_renglon_Ejercicio(5)
# Solicitar al usuario una frase e imprimir:
    # Las palabras únicas usando set().
    # Y un diccionario con la cantidad de veces que aparece cada palabra. 

# Entrada -->>  EstrEllas sol planetas sol LUna sol luna estrellas Sol Luna sol 
lista_palabras = input("Por favor ingrese una frase: ").lower().split()
print(f"\nFrase ingresada: \n {lista_palabras} \n")

# Salida: 
palabras_unicas = set(lista_palabras)
frecuencia = Counter(lista_palabras) # usando "Counter" obtengo la frecuencia en la que aparece cada palabra 
diccionario_frecuencias = dict(frecuencia) # convertimos a diccionario
print(f"\nPalabras únicas: \n {palabras_unicas} \n")
print(f"Frecuencias de cada palabra:\n {diccionario_frecuencias} \n")



saltar_renglon_Ejercicio(6)
# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
alumnos = {}

# Programa principal
print("Ingrese tres alumnos y tres notas de cada uno: \n")
for n in range(3):
  # Validar alumno
  while True:
    nombre = input(f"Ingrese el nombre del {n + 1}º alumno: ").strip().lower()
    if nombre.isalpha() and not nombre in alumnos: 
      break
    elif nombre in alumnos:
      print("⚠️ Este nombre de alumno ya existe, ingrese otro.")
      continue
    else:
      print("⚠️ El nombre solo debe contener letras. Intente de nuevo.")
      continue

  # Validar notas
  notas = []
  suma_notas_alumno = []
  for n in range(3):
    while True:
      nota = input(f"{n+1}º nota: ").strip()
      if nota.isdigit():
        break
      print("⚠️ Error - la nota debe contener solo número.")
    notas.append(int(nota))
  
  alumnos[nombre] = tuple(notas)

print(f"\nAlumnos y notas ingresados correctamente: {alumnos}\n")

for alumno, notas in alumnos.items():
  promedio = sum(notas) / len(notas)
  print(f"{alumno.title()} tiene un promedio de {promedio:.2f}" )



saltar_renglon_Ejercicio(7)
#  Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
    # • Mostrá los que aprobaron ambos parciales.
    # • Mostrá los que aprobaron solo uno de los dos.
    # • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).


aprob_parcial_uno = {"Pedro", "Rocío", "Gerónimo", "Daniela", "Magalí", "Clara"}
aprob_parcial_dos = {"Pedro", "Daniela", "Rocío", "Gerónimo", "Julián"}

ambos_parciales = aprob_parcial_uno & aprob_parcial_dos    # Intersección

print(f"\n\nAprobaron ambos parciales: {ambos_parciales}\n")

solo_un_parcial = aprob_parcial_uno ^ aprob_parcial_dos     # Diferencia Simétrica 

print(f"\nAprobaron solo el 1er parcial: {solo_un_parcial}\n") 

# "Al menos 1 parcial" --> aquellos que aprobaron 1 o más parciales. 

al_menos_un_parcial = aprob_parcial_uno | aprob_parcial_dos   # Union
  
print(f"\nEstudiantes que aprobaron al menos 1 parcial: {al_menos_un_parcial}\n") 



saltar_renglon_Ejercicio(8)
# Armar un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permitir al usuario:
    # • Consultar el stock de un producto ingresado.
    # • Agregar unidades al stock si el producto ya existe.
    # • Agregar un nuevo producto si no existe.

inventario = {'plato': 10, 'cuchillo': 5, 'tenedor': 5, 'vaso': 10, 'botella': 1} 

def mostrar_menu():
  print("\n** MENU DE OPCIONES: **") 
  print("1 - Consultar Stock del producto.")
  print("2 - Agregar unidades al stock existente.")
  print("3 - Agregar un nuevo producto.")
  print("4 - Mostrar todos los productos.")
  print("5- Salir.")

def mostrar_inventario():
  print("\nInventario de productos: ",inventario)

def salto_linea():
  print("_________________ .. _________________")

def validar_entero(valor):
  while True:
    if valor.isdigit():
      numero = int(valor)
      if numero > 0:
        return numero
      else:
        valor = input("Ingrese un número positivo: ").strip()
    else:
      valor = input("Ingrese un número válido (solo digitos): ").strip()


def consultar_stock(inventario):
  print("** Consulta de Stock: **")
  producto = input("\nEscriba un producto para saber su stock: ").strip().lower()
  if producto in inventario:
    print(f"\n{producto.title()} cantidad: {inventario[producto]}\n")
  else: 
    print("\nError, el producto no se encuentra en el inventario. Utilice la opción 3 para agregarlo.\n")
  salto_linea()

def agregar_stock(inventario):
  print("** Agregar Stock a producto existente: **")
  producto = input("\nEscriba el producto: ").strip().lower()
  if producto in inventario:
    agregar_unidades = input("¿Cuás unidades se agregan?:  ").strip()
    inventario[producto] += validar_entero(agregar_unidades)
    print(f"\n{producto.title()} cantidad: {inventario[producto]}\n")
  else: 
    print("\nError, el producto no pertenece al inventario. Utilice la opción 3 para agregarlo.")
  salto_linea()

def agregar_producto(inventario):
  print("** Agregar producto: **")
  producto = input("\nIndique el producto a agregar: ").strip().lower()
  if producto in inventario:
    print("Error - El producto ya existe en inventario, ingrese otro nombre.")
    salto_linea()
  else:
    unidades = input("¿Cuántas unidades se agregan?:  ").strip()
    inventario[producto] = validar_entero(unidades)
    print(f"\n{producto.title()} cantidad: {inventario[producto]}\n")
   

#Programa Principal

while True: 
  mostrar_menu()
  opcion = input(f"\nQué opción desea realizar?: ").strip()
  match opcion:
    case "1":
      consultar_stock(inventario)
    case "2":
      agregar_stock(inventario)
    case "3": 
       agregar_producto(inventario)
       continue
    case "4":
      print("** Mostrar inventario: **")
      mostrar_inventario()
      salto_linea()
    case "5": 
      print("Saliendo...")
      salto_linea()
      break
    case _:
      print("\nError - solo debe ingresar números del 1 al 4.")
      salto_linea()



saltar_renglon_Ejercicio(9)
# Crear una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Ejemplo:
# agenda = {("lunes","10:00"): "Reunión",
#          ("martes","15:00"): "Clase Inglés"
#          }
# Permití consultar qué actividad hay en cierto día y hora.

agenda = {}

def validar_entero(valor):
  while True:
    if valor.isdigit():
      numero = int(valor)
      if numero > 0:
        return numero
      else:
        valor = input("Ingrese un número positivo: ").strip()
    else:
      valor = input("Ingrese un número válido (solo digitos): ").strip()


def validar_dia(valor):
  dias_validos = ["lunes", "martes", "miércoles", "miercoles", "jueves", "viernes", "sábado", "sabado", "domingo"]
  while True:
    if valor in dias_validos:
      return valor
    else:
      valor = input("Ingrese un día válido (solo letras): ").strip()


def agendar(valor):
  for evento in range(valor):
    dia = input("Ingrese el día: ").lower().strip()
    dia = validar_dia(dia)
    hora = input("Ingrese una hora formato (HH:MM): ")
    evento = input("Ingrese un evento: ")
    agenda[(dia,hora)] = evento
  print("\nSe ingresaron los siguientes eventos: ",agenda)


def ver_evento(dia, hora):
  if (dia, hora) in agenda:
    print(f"\nTiene el evento: {agenda[(dia,hora)]}")
  else:
    print(f"\nNo tiene eventos el {dia} a las {hora}")


# Programa principal
while True: 
  print("\n ======== MENU ========\n 1. Agregar evento \n 2. Consultar actividad \n 3. Salir del menú ")
  opcion = input("Ingrese una opción del menú: ")
  match opcion:
    case "1":
      print("===== AGREGAR EVENTO =====")
      largo = input("Cuántas eventos quiere agendar? ")
      agendar(validar_entero(largo))

    case "2":
      print("===== CONSULTAR ACTIVIDAD =====")
      # Consulta de agenda
      dia = input("Indique el día a consultar: ")
      hora =  input("Indique la hora a consultar (formato HH:MM): ")
      ver_evento(validar_dia(dia), hora)

    case "3":
      print("Saliendo...")
      break

    case _:
      print("Error - indique una opción válida del menú (1, 2 o 3).")



saltar_renglon_Ejercicio(10)
# Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
    # Las capitales sean las claves.
    # Los países sean los valores.

original = {"Argentina": "Buenos Aires","Chile": "Santiago"}
invertido = {}

#············ FORMA MAS RAPIDA ············ 
for key in original:                                
  invertido[original[key]] = key                        # Asignamos como valor, la clave "país". Y nueva clave, dejamos la "capital" --> original[key]

print("\nOriginal: ", original)
print(f"\nInvertido: {invertido}\n")



# ············ OTRA FORMA DE HACER LO MISMO: ············ 
# for clave, valor in original.items():                 # items() es un método del diccionario para recorrerse a si mismo y así obtener en este caso su clave - valor
#   invertido[valor] = clave



# ············ IDEM ARRIBA: ············
# for valor in original.values():
#   for key in original.keys():
#     invertido[valor] = key