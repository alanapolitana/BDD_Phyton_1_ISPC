# ejercicios listas diccionarios y tuplas

# 1. Diseña un algoritmo que introduzca por teclado el nombre de 3 países,
# se almacenen en una lista y los muestre por pantalla.
lista = []
for pais in range(3):
    paises = input("Ingres el pais: ")
    lista += [paises]

print(lista)

# 2. Diseña un algoritmo que almacene los precios de 4 productos que compré en una lista
# y luego me muestre el total en pantalla.

precios = []
for i in range(4):
    precio = float(input("Ingrese el precio del producto: "))
    precios.append(precio)

total = sum(precios)
print("El total de la compra es: ", total)

# 3. Diseña un algoritmo que almacene las letra de tu nombre en una lista
# y luego muestre el nombre.

nombre = []

nombre_completo = input("Ingresa tu nombre completo: ")
for letra in nombre_completo:
    if letra != " ":
        nombre.append(letra)

print("Tu nombre es: ")
for letra in nombre:
    print(letra, end="")
   
# 4. Diseña un algoritmo que introduzca por teclado el nombre, materia,
# profesor y nota. Se almacene en una tupla y luego muestre
# los datos en pantalla.

print(" ")
print("-" * 60)
cantidad = int(input("Inbrese la cantidad de alumnos a cargar: "))
tupla = ()
datos_alumno = []

for datos in range(cantidad):
    nombre_alumno = input("Ingrese su nombre: ")
    materia = input("Ingrese la materia: ")
    profesor = input("Ingrese el profesor: ")
    nota = float(input("Ingrese la nota: "))

    # creamos una lista temporal con los datos de cada alumno
    datos_alumno = [nombre_alumno, materia, profesor, nota]

    # agregamos a la lista emporal a la tupla

    tupla = tupla + (datos_alumno,)


    print("-" * 60)


print("Datos de los alumnos: ")

for alumno in tupla:
    print("Nombre: ", alumno[0])
    print("Materia: ", alumno[1])
    print("Profesor: ", alumno[2])
    print("Nota: ", alumno[3])
    print("-" * 60)

# 5. Diseña un algoritmo que introduzca por teclado el nombre de 3 materias y sus notas correspondientes.
#  Deben almacenarse las materias en una tupla y las notas en otra. Luego muestre en pantalla la materia con su nota correspondiente.

tupla_materias = ()
lista_notas = []

for i in range(3):
    materias = input("Ingrese el nombre de la materia: ")
    nota = float(input("Ingrese la nota de la materia:  "))
    tupla_materias += (materias,)
    lista_notas.append(nota)



print("-" * 40)

print("Materia\t\tNota")

print("-" * 60)

for i in range(3):
    print(tupla_materias[i],":",lista_notas[i])

# 6. Diseña un algoritmo con un diccionario que contenga como clave 3
#  materias que estás cursando y como valores uses tuplas para almacenar
#  2 notas por materia. Luego por pantalla muestres las notas de cada
# materia.


materas_y_notas = {"Introduccion a la programacion": (8, 6),
                   "Ingles": (9, 5),
                    "Base de datos": (7, 10)}

for materia, notas in materas_y_notas.items():
    nota1, nota2 = notas
    print("Notas de", materia,": ", nota1,"y", nota2)
    print("-" * 30)

# 7. Diseña un algoritmo creando una tupla que almacene 3 categorías
# de música y luego crea un diccionario donde utilices como clave la
#  tupla y almacenes 2 músicos por categoría de música.
# Luego mostrar en pantalla los artistas.

# Crear una tupla con 3 categorías de música
categorias = ("Rock", "Jazz", "Electrónica")

# Crear un diccionario para almacenar los músicos por categoría
musicos = {}

# Agregar los músicos por categoría utilizando la tupla como clave
for categoria in categorias:
    # Pedir al usuario que ingrese los músicos para esta categoría
    print(f"Ingrese dos músicos de la categoría {categoria}:")
    musico1 = input("Músico 1: ")
    musico2 = input("Músico 2: ")
    # Almacenar los músicos en una lista
    lista_musicos = [musico1, musico2]
    # Agregar la lista de músicos al diccionario, utilizando la tupla de categoría como clave
    musicos[categoria] = lista_musicos

# Mostrar los músicos por categoría en pantalla
for categoria, lista_musicos in musicos.items():
    print(f"Categoría: {categoria}")
    print("Músicos:")
    for musico in lista_musicos:
        print(f"- {musico}")
    print("-" * 20)