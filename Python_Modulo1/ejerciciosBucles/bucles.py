# EJERCICIOS BUCLES


# 1. Mostrar la lista de países de América del Sur y su población en millones de
# habitantes usando un bucle y el siguiente diccionario:
# poblaciones = {"Argentina": 45, "Bolivia": 11, "Brasil": 211, "Chile": 19, "Colombia": 50,
# "Ecuador": 17, "Guyana": 0.8, "Paraguay": 7, "Perú": 32, "Suriname": 0.6, "Uruguay":
# 3.5, "Venezuela": 28}

poblaciones = {"Argentina": 45, "Bolivia": 11, "Brasil": 211, "Chile": 19, "Colombia": 50,
               "Ecuador": 17, "Guyana": 0.8, "Paraguay": 7, "Perú": 32, "Suriname": 0.6, "Uruguay": 3.5, "Venezuela": 28}

print("Lista de países de América del Sur y su población en millones de habitantes:")

for pais, poblacion in poblaciones.items():
    print(f"{pais}: {poblacion} millones")

    # Este código recorre el diccionario poblaciones utilizando un bucle for y la función items(), que devuelve pares de clave-valor. Luego, se imprime cada país y su población correspondiente utilizando una f-string para formatear la salida.



# 2. Mostrar los nombres de los países que tienen una superficie mayor a 2
# millones de km², usando una lista de tuplas y un bucle while:
# paises = [("Rusia", 17.1), ("Canadá", 9.9), ("Paraguay", 1.6), ("EE.UU.", 9.5), ("Brasil", 8.5),
# ("Australia", 7.7), ("India", 3.3), ("Argentina", 2.8), ("Kazajistán", 2.7), ("Argelia", 2.4)]

paises = [("Rusia", 17.1), ("Canadá", 9.9), ("Paraguay", 1.6), ("EE.UU.", 9.5),
          ("Brasil", 8.5), ("Australia", 7.7), ("India", 3.3), ("Argentina", 2.8),
          ("Kazajistán", 2.7), ("Argelia", 2.4)]

print("Países con una superficie mayor a 2 millones de km²:")

i = 0
while i < len(paises):
    pais, superficie = paises[i]
    if superficie > 2:
        print(pais)
    i += 1
# Este código utiliza un bucle while para recorrer la lista de tuplas paises. En cada iteración, se verifica si la superficie del país actual es mayor a 2 millones de km². Si es así, se imprime el nombre del país. Luego, se incrementa el valor de i para pasar al siguiente elemento de la lista.

# En el código proporcionado, len() es una función incorporada en Python que se utiliza para obtener la longitud de un objeto iterable, como una lista, una cadena de texto o una tupla. La función len() devuelve el número de elementos en el objeto iterable.

# En el caso del código mencionado, se utiliza len(paises) para obtener la longitud de la lista paises. Esto proporciona el número total de elementos en la lista, que se utiliza en el bucle while para determinar la condición de terminación del bucle.

# La variable i es un contador que se utiliza en el bucle while para realizar un seguimiento de la posición actual mientras se recorre la lista. Inicialmente, se establece en 0 para apuntar al primer elemento de la lista. En cada iteración del bucle, se accede al elemento en la posición i y se realiza la comprobación correspondiente. Luego, el valor de i se incrementa en 1 para pasar al siguiente elemento en la siguiente iteración del bucle.

# En resumen, len() se utiliza para obtener la longitud de un objeto iterable, mientras que i es un contador utilizado para iterar a través de los elementos de una lista y realizar operaciones en cada elemento.





# 3. Mostrar los nombres de los países que empiezan con "M" o "N"
# paises = ["Sudáfrica", "Malawi", "Malí", "Costa de Marfil", "Mauricio", "Argelia",
# "Mozambique", "Namibia", "Níger", "Nigeria"]

paises = ["Sudáfrica", "Malawi", "Malí", "Costa de Marfil", "Mauricio", "Argelia", "Mozambique", "Namibia", "Níger", "Nigeria"]

for pais in paises:
    if pais.startswith("M") or pais.startswith("N"):
        print(pais)

# 4. Mostrar los nombres de los animales en una lista, pero omitiendo los
# animales que tienen más de 7 letras, utilizando un bucle while:
# animales = ["tigre", "oso", "cocodrilo", "mono", "jirafa", "puma", "pingüino", "elefante",
# "cebra", "ornitorrinco"]

animales = ["tigre", "oso", "cocodrilo", "mono", "jirafa", "puma", "pingüino", "elefante", "cebra", "ornitorrinco"]

indice = 0
while indice < len(animales):
    animal = animales[indice]
    if len(animal) <= 7:
        print(animal)
    indice += 1




# 5. Mostrar los nombres de los animales y su cantidad en una lista, utilizando
# un diccionario y un bucle for:
# animales = ["león", "jirafa", "elefante", "cebra", "hipopótamo", "rinoceronte"]
# cantidades = {"león": 3, "jirafa": 5, "elefante": 2, "cebra": 7, "hipopótamo": 1,
# "rinoceronte": 4
animales = ["león", "jirafa", "elefante", "cebra", "hipopótamo", "rinoceronte"]
cantidades = {"león": 3, "jirafa": 5, "elefante": 2, "cebra": 7, "hipopótamo": 1, "rinoceronte": 4}

for animal in animales:
    cantidad = cantidades[animal]
    print(f"{animal}: {cantidad}")


    # Para mostrar los nombres de los animales y su cantidad en una lista utilizando un diccionario y un bucle for, puedes combinar el diccionario cantidades con la lista animales y recorrerlos utilizando el bucle for.

    # En este código, el bu ra cada animal, se obtiene su cantidad correspondiente del diccionario cantidades utilizando cantidades[animal]. Luego, se imprime el nombre del animal junto con su cantidad utilizando la función print().