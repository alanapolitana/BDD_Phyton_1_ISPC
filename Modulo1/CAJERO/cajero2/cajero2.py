"""
  Mostrar por pantalla el siguiente menú:

CAJERO AUTOMATICO

ISPC

Listado de opciones:

1)      Ingreso de dinero

2)      Extracción de dinero

3)      Consulta de salto

4)      Salir

Ingrese su selección: _

El programa deberá mostrar luego del ingreso de cada opción “Usted ha seleccionado la opción x”, por ejemplo, en el caso de ingresar un 1, deberá mostrar por pantalla “Usted ha seleccionado la opción 1” y así sucesivamente. Al seleccionar la opción 4 se debe terminar la ejecución del programa.

 """

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