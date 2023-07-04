# 1)      Escribir un programa que permita validar el ingreso a un sistema. Se deberá solicitar el ingreso por teclado de nombre de usuario y contraseña. Será valido como nombre de usuario “admin” y como contraseña “1234”. Si el ingreso es correcto deberá mostrar por pantalla el mensaje “Ingreso exitoso”.

# Opcional 1: permitir como usuario valido también su propio nombre y su propia contraseña.

# Opcional 2: solamente permitir el ingreso incorrecto de los datos 3 veces, luego de ello, no permitir más ingresos y mostrar por pantalla “Cuenta bloqueada”.

 

# 2)      Mostrar por pantalla el siguiente menú:

# CAJERO AUTOMATICO

# ISPC

# Listado de opciones:

# 1)      Ingreso de dinero

# 2)      Extracción de dinero

# 3)      Consulta de salto

# 4)      Salir

# Ingrese su selección: _

# El programa deberá mostrar luego del ingreso de cada opción “Usted ha seleccionado la opción x”, por ejemplo, en el caso de ingresar un 1, deberá mostrar por pantalla “Usted ha seleccionado la opción 1” y así sucesivamente. Al seleccionar la opción 4 se debe terminar la ejecución del programa.

# 3)      Deberá continuar con el ejercicio 2 y escribir la lógica del cajero automático de la siguiente manera.

# a.       Su saldo inicial será de $10000.

# b.       Al seleccionar la opción 1 se pedirá al usuario que ingrese un importe por teclado el cual se sumará a su saldo inicial.

# c.       De la misma manera al seleccionar la opción 2, se solicitará un importe por teclado el cual se restará al saldo inicial.

# d.       Con la opción 3 se consultará su saldo actual.

# e.       En todo momento se deberá contralar que no se pueda extraer dinero, si no se cuentan con fondos suficientes.

# 4)      Deberá en un solo programa unir el logueo del sistema con los ejercicios 2 y 3. Esto quiere decir que, si el ingreso al sistema es exitoso, se mostrará el menú del cajero automático y el usuario podrá comenzar a operar.

# Opcional 3: Puede incluir parte de la lógica del programa en una o más funciones.


intentos = 0  # Variable para contar los intentos de ingreso

while intentos < 3:  # Permitir hasta 3 intentos
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if (usuario == "admin" and contraseña == "1234") or (usuario == input("Ingrese su propio nombre de usuario: ") and contraseña == input("Ingrese su propia contraseña: ")):
        print("Ingreso exitoso")
        break  # Salir del bucle si el ingreso es exitoso
    else:
        intentos += 1  # Incrementar el contador de intentos
        print("Nombre de usuario o contraseña incorrectos")

if intentos == 3:
    print("Cuenta bloqueada")

while True:
    print("CAJERO AUTOMATICO\n")
    print("ISPC\n")
    print("Listado de opciones:\n")
    print("1) Ingreso de dinero")
    print("2) Extracción de dinero")
    print("3) Consulta de saldo")
    print("4) Salir\n")

    opcion = input("Ingrese su selección: ")

    if opcion == "1":
        print("Usted ha seleccionado la opción 1")
        # Código para ingreso de dinero
    elif opcion == "2":
        print("Usted ha seleccionado la opción 2")
        # Código para extracción de dinero
    elif opcion == "3":
        print("Usted ha seleccionado la opción 3")
        # Código para consulta de saldo
    elif opcion == "4":
        print("Usted ha seleccionado la opción 4. ¡Hasta luego!")
        break  # Terminar la ejecución del programa
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.\n")