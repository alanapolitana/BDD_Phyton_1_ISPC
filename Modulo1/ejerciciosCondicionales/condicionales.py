# CONDICIONAL SIMPLE

# 1)) Realice un programa que solicite dos letras ingresadas por el usuario y verifique si son iguales o no, mostrando un mensaje.
# 2)) Hacer un programa que permita decidir si dos palabras son iguales o diferentes. Mostrar por pantalla.
# 3)) Realizar un programa que permita ingresar "f" o "m" y determinar si vota en mesa femenina o masculina.
# 4)) Realice un programa que lea dos numeros y diga cual es mayor.
# 5)) Realice un programa que cambie pesos a dolares. Mejórelo, añadiendo el cambio de dolares a pesos y que sea el usuario quien decida que tipo de cambio quiere, si de dolares a pesos o viceversa.
# 6)) Realice un programa donde el usuario ingrese su edad. Si es mayor de 16 años, muestre un mensaje diciendo "puede votar", sino "no vota".


# CONDICIONAL COMPUESTO (IF ANIDADOS)
# 1)) Introducir los lados de un triangulo y visualizar por pantalla si dicho triangulo es equilátero, isoceles o escaleno.
# 2)) Realice un programa que le permita al usuario simular el pago ingresando importe y la forma de pago:
#    Contado (1) : se aplica un descuento 10% al importe.
#    Tarjeta (2) : se aplica un interes de 10%.
#    Débito  (3) : se aplica un descuento de 5%.
#                              Mostrar el importe, el descuento o interes y el importe total.
# 3)) Realize un programa que lea tres números, muestre cual es el mayor y determine si es par o impar.
# 4)) Confeccione un programa que pida un numero del 1 al 7 y diga el dia de la semana correspondiente.
# 5)) Realice un programa que pida un numero del 1 al 12 y diga el nombre del mes correspondiente.




# Ejercicio estructura condicional simple:
# 1. Realice un programa que solicite dos letras ingresadas por el usuario y
# verifique si son iguales o no, mostrando un mensaje.

letra_1 = input("Ingrese la primer letra: ")
letra_2 = input("Ingrese la segunda letra: ")

if letra_1 == letra_2:
    print("Las letras son iguales!")
else:
    print("Las letras NO son iguales!")

# 2. Hacer un programa que permita decidir si dos palabras son iguales o
 # diferentes. Mostrar mensaje por pantalla.

palabra_1 = input("Ingrese la primer palabra: ")
palabra_2 = input("Ingrese la segunda palabra: ")

if palabra_1 == palabra_2:
    print("Las palabras son iguales!")
else:
    print("Las palabras NO son iguales!")

# 3. Realizar un programa que permita ingresar “f” o “m” y determinar si vota
# en mesa femenina o masculina.

mesa = input("Ingrese si es mesa femenina (f) o mesa masculina (m): ")

if mesa == "m":
    print("Es mesa masculina!")
elif mesa == "f":
    print("Es mesa femenina!")
else:
    print("Error! Ingreso una letra invalida!, vuelva a ingresar...")
    mesa = input("Ingrese si es mesa femenina (f) o mesa masculina (m): ")

# 4. Realice un programa que lea dos números y diga cuál es el mayor.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 > num2:
    print("El numero", num1, "es el mayor!")
else:
    print("El numero", num2, "es el mayor!")

# 5. Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo
# el cambio de dólares a pesos y que sea el usuario quién decida qué tipo
# de cambio quiere, si de dólares a pesos o viceversa.

pesos = float(input("Ingrese la cantidad de pesos: "))

dolares = pesos * 300

print("La cantidad de dolares es: ", dolares)

# mejorado

cambio = float(input("Ingrese el cambio que quiere, pesos(1) dolares(2): "))

if cambio == 1:
    pesos = float(input("Ingrese la cantidad de pesos: "))
    dolares = pesos * 300
    print("La cantidad de dolares es: ", dolares)
elif cambio == 2:
    dolares = float(input("Ingrese la cantidad de dolares: "))
    pesos = dolares * 212
    print("La cantidad de pesos es: ", pesos)
else:
    print("ERROR INGRESO UN NUMERO ERRONEO!")

# 6. Realice un programa donde el usuario ingrese su edad. Si es mayor de
# 16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”.

edad = int(input("Ingrese su edad: "))

if edad >= 16:
    print("Puede votar")
else:
    print("No puede votar")


# CONDICIONALES

# Ejercicios estructura condicional compuesto (IF anidados)
# 1. Introducir los lados de un triángulo y visualizar por pantalla si dicho
# triángulo es equilátero, isósceles o escaleno.

lado_a = int(input("Ingrese el valor del lado: "))
lado_b = int(input("Ingrese el valor del lado: "))
lado_c = int(input("Ingrese el valor del lado: "))

if lado_a == lado_b and lado_b == lado_c:
    print("Es equilatero")
elif lado_a != lado_b and lado_a != lado_c:
    print("Es escaleno")
else:
    print("Es isoceles")

# 2. Realice un programa que le permita al usuario simular el pago
# ingresando el importe y la forma de pago:
# • Contado (1): se aplica un descuento del 10% al importe
# • Tarjeta (2): se aplica un interés de 10%
# • Débito (3): se aplica un descuento del 5%
# Mostrar el importe, el descuento o interés y el importe total.

importe = float(input("Ingrese el importe: "))
forma_pago = int(input("Ingrese la forma de pago, contado(1), tarjeta(2), debito(3): "))

if forma_pago == 1:
    importe_final = importe - (importe * 0.10)
    descuento_o_interes = "descuento del 10%"
elif forma_pago == 2:
    importe_final = importe + (importe * 0.10)
    descuento_o_interes = "interés del 10%"
elif forma_pago == 3:
    descuento_o_interes = "descuento del 5%"
    importe_final = importe - (importe * 0.05)
else:
    print("ELIGIO UNA FORMA DE PAGO ERRONEA!")

if forma_pago == 1 or forma_pago == 2 or forma_pago == 3:
    print("El importe final es de: ", importe_final, "el importe es de: ", importe, "y el descuento es de: ", descuento_o_interes)



# 3. Realice un programa que lea tres números, muestre cuál es el mayor y
# determine si es par o impar.

a = int(input("Ingrese el numero: "))
b = int(input("Ingrese el numero: "))
c = int(input("Ingrese el numero: "))

if a > b and a > c:
    print("El mayor es: ", a)
    if a % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
elif b > a and b > c:
    print("El mayot es: ", b)
    if b % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
else:
    print("El mayor es: ", c)
    if c % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

# 4. Confeccione un programa que pida un número del 1 al 7 y diga el día de
# la semana correspondiente.

dia = int(input("Ingrese el dia de semana del 1 al 7 (1 lunes hasta domingo 7)"))

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
elif dia == 6:
    print("Es sabado")
elif dia == 7:
    print("Es domingo")
else:
    print("ERROR! Ingreso un numero erroneo!")

# 5. Realice un programa que pida un número del 1 al 12 y diga el nombre
# del mes correspondiente.

mes = int(input("Ingrese el mes (empezando por 1-enero hasta el 12-diciembre: )"))

if mes == 1:
    print("Es enero")
elif mes == 2:
    print("Es febrero")
elif mes == 3:
    print("Es marzo")
elif mes == 4:
    print("Es abril")
elif mes == 5:
    print("Es mayo")
elif mes == 6:
    print("Es junio")
elif mes == 7:
    print("Es julio")
elif mes == 8:
    print("Es agosto")
elif mes == 9:
    print("Es septiembre")
elif mes == 10:
    print("Es octubre")
elif mes == 11:
    print("Es noviembre")
elif mes == 12:
    print("Es diciembre")
else:
    print("ERROR! Ingreso un numero erroneo")