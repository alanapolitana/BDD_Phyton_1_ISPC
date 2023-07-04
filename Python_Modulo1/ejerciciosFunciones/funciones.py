# Resolver los siguientes ejercicios usando funciones

# 1. Realice una función para calcular el costo total recaudado
# en entradas de un recital.

def calcular_costo_total_entradas(cantidad_entradas, precio_entrada):
    costo_total = cantidad_entradas * precio_entrada
    return costo_total

# Ejemplo de uso de la función
cantidad = int(input("Ingrese la cantidad de entradas vendidas: "))
precio = float(input("Ingrese el precio de cada entrada: "))

total_recaudado = calcular_costo_total_entradas(cantidad, precio)
print("El costo total recaudado es:", total_recaudado)




# 2. Función para comprobar si una canción está en la lista de
# reproducción de un recital.
def comprobar_cancion_en_lista(cancion, lista_reproduccion):
    if cancion in lista_reproduccion:
        return True
    else:
        return False

# Ejemplo de uso de la función
lista = ["Canción 1", "Canción 2", "Canción 3", "Canción 4"]

cancion_buscar = input("Ingrese el nombre de la canción a buscar: ")

if comprobar_cancion_en_lista(cancion_buscar, lista):
    print("La canción está en la lista de reproducción.")
else:
    print("La canción no está en la lista de reproducción.")




# 3. Función para calcular el tiempo total de duración de un
# recital, considerando la duración de x cantidad de
# canciones.
def calcular_duracion_total(canciones):
    duracion_total = sum(canciones)
    return duracion_total

# Ejemplo de uso de la función
canciones = [3.5, 4.2, 2.8, 5.1, 3.9]

duracion_total = calcular_duracion_total(canciones)

print(f"La duración total del recital es de {duracion_total} minutos.")




# 4. Crear una función que calcule la velocidad promedio de un
# auto, dada la distancia recorrida y el tiempo empleado.
def calcular_velocidad_promedio(distancia, tiempo):
    velocidad_promedio = distancia / tiempo
    return velocidad_promedio

# Ejemplo de uso de la función
distancia_recorrida = 250  # en kilómetros
tiempo_empleado = 4.5  # en horas

velocidad = calcular_velocidad_promedio(distancia_recorrida, tiempo_empleado)

print(f"La velocidad promedio del auto es de {velocidad} km/h.")


# 5. Crear una función que determine si un auto está en
# marcha o detenido, dada su velocidad.
def determinar_estado_auto(velocidad):
    if velocidad > 0:
        return "El auto está en marcha."
    else:
        return "El auto está detenido."

# Ejemplo de uso de la función
velocidad_actual = 60  # en km/h

estado = determinar_estado_auto(velocidad_actual)

print(estado)


# 6. Crear una función que convierta kilómetros por hora a
# millas por hora.
def convertir_kmh_a_mph(kmh):
    mph = kmh * 0.621371  # Fórmula de conversión
    return mph

# Ejemplo de uso de la función
velocidad_kmh = 100

velocidad_mph = convertir_kmh_a_mph(velocidad_kmh)

print(f"{velocidad_kmh} km/h equivale a {velocidad_mph} mph.")


# 7. Crear una función que calcule el consumo de combustible
# de un auto por kilómetro, dada la distancia recorrida y la
# cantidad de combustible utilizada.

def calcular_consumo_combustible(distancia, combustible):
    consumo = combustible / distancia  # Cálculo del consumo por kilómetro
    return consumo

# Ejemplo de uso de la función
distancia_recorrida = 250  # en kilómetros
cantidad_combustible = 40  # en litros

consumo_por_kilometro = calcular_consumo_combustible(distancia_recorrida, cantidad_combustible)

print(f"El consumo de combustible es de {consumo_por_kilometro} litros por kilómetro.")
# 8. Crear una función que determine el costo de un viaje en
# auto, dada la distancia recorrida, el consumo de
# combustible y el precio del combustible
def calcular_costo_viaje(distancia, consumo_combustible, precio_combustible):
    costo_combustible = consumo_combustible * precio_combustible
    costo_total = costo_combustible * distancia
    return costo_total

# Ejemplo de uso de la función
distancia_recorrida = 200  # en kilómetros
consumo_combustible = 8  # en litros por kilómetro
precio_combustible = 1.5  # en dólares por litro

costo_viaje = calcular_costo_viaje(distancia_recorrida, consumo_combustible, precio_combustible)

print(f"El costo del viaje es de ${costo_viaje}.")