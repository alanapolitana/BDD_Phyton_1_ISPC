# Ejercicios estructuras repetitivas y estructuras condicionales.


# 1. Realice un programa que lea 4 números y diga cuántos son pares y
# cuantos impares y devuelva la sumatoria de los pares.

numeros = []
cantidad_pares = 0
suma_pares = 0

for i in range(4):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)
    
    if numero % 2 == 0:
        cantidad_pares += 1
        suma_pares += numero

cantidad_impares = 4 - cantidad_pares

print("Cantidad de números pares:", cantidad_pares)
print("Cantidad de números impares:", cantidad_impares)
print("Suma de los números pares:", suma_pares)


# En este código, se utiliza un bucle for para iterar 4 veces y leer los 4 números ingresados por el usuario. Los números se almacenan en la lista numeros mediante la función append().

# Dentro del bucle, se utiliza una estructura condicional if para verificar si cada número es par. Esto se hace comprobando si el residuo de la división del número entre 2 es igual a cero (numero % 2 == 0). Si el número es par, se incrementa la variable cantidad_pares en 1 y se agrega el número a la variable suma_pares.

# Después de salir del bucle, se calcula la cantidad de números impares restando la cantidad de números pares de 4.

# Finalmente, se imprime la cantidad de números pares, la cantidad de números impares y la suma de los números pares utilizando la función print().



# 2. Leer 10 números y obtener la cantidad de mayores y la cantidad de
# menores a 100, cuál es el número máximo y cuál es el número mínimo.

cantidad_mayores_100 = 0
cantidad_menores_100 = 0
numero_maximo = float('-inf')
numero_minimo = float('inf')

for i in range(10):
    numero = int(input("Ingrese un número: "))
    
    if numero > 100:
        cantidad_mayores_100 += 1
    else:
        cantidad_menores_100 += 1
        
    if numero > numero_maximo:
        numero_maximo = numero
        
    if numero < numero_minimo:
        numero_minimo = numero

print("Cantidad de números mayores a 100:", cantidad_mayores_100)
print("Cantidad de números menores a 100:", cantidad_menores_100)
print("Número máximo:", numero_maximo)
print("Número mínimo:", numero_minimo)



# 3. Ingresar las edades y el sexo de 15 personas y determinar cuántas son
# mujeres, cuántos varones, cuántos mayores de edad y cuántos
# menores de edad.
cantidad_mujeres = 0
cantidad_varones = 0
cantidad_mayores_edad = 0
cantidad_menores_edad = 0

for i in range(15):
    edad = int(input("Ingrese la edad de la persona: "))
    sexo = input("Ingrese el sexo de la persona (M/F): ").upper()
    
    if sexo == "M":
        cantidad_varones += 1
    elif sexo == "F":
        cantidad_mujeres += 1
    
    if edad >= 18:
        cantidad_mayores_edad += 1
    else:
        cantidad_menores_edad += 1

print("Cantidad de mujeres:", cantidad_mujeres)
print("Cantidad de varones:", cantidad_varones)
print("Cantidad de mayores de edad:", cantidad_mayores_edad)
print("Cantidad de menores de edad:", cantidad_menores_edad)


# 4. Leer 10 números y mostrar solamente los números positivos, y su
# sumatoria.

sumatoria_positivos = 0

for i in range(10):
    numero = float(input("Ingrese un número: "))
    
    if numero > 0:
        sumatoria_positivos += numero

print("La sumatoria de los números positivos es:", sumatoria_positivos)

# 5. Leer 15 números negativos y convertirlos a positivos e imprimir dichos
# números
numeros_convertidos = []

for i in range(15):
    numero = float(input("Ingrese un número negativo: "))
    numero_convertido = abs(numero)  # Utilizamos la función abs() para obtener el valor absoluto
    
    numeros_convertidos.append(numero_convertido)

print("Números convertidos a positivos:")
for numero in numeros_convertidos:
    print(numero)