"""
3)      Deberá continuar con el ejercicio 2 y escribir la lógica del cajero automático de la siguiente manera.

a.       Su saldo inicial será de $10000.

b.       Al seleccionar la opción 1 se pedirá al usuario que ingrese un importe por teclado el cual se sumará a su saldo inicial.

c.       De la misma manera al seleccionar la opción 2, se solicitará un importe por teclado el cual se restará al saldo inicial.

d.       Con la opción 3 se consultará su saldo actual.

e.       En todo momento se deberá contralar que no se pueda extraer dinero, si no se cuentan con fondos suficientes.
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


saldo = 10000

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
        print("Usted ha seleccionado la opción 1\n")
        monto = float(input("Ingrese el monto a depositar: "))
        saldo += monto
        print("¡Depósito realizado exitosamente!\n")
    elif opcion == "2":
        print("Usted ha seleccionado la opción 2\n")
        monto = float(input("Ingrese el monto a retirar: "))
        if monto <= saldo:
            saldo -= monto
            print("¡Retiro realizado exitosamente!\n")
        else:
            print("¡Fondos insuficientes! No se puede realizar el retiro.\n")
    elif opcion == "3":
        print("Usted ha seleccionado la opción 3\n")
        print("Saldo actual: $", saldo, "\n")
    elif opcion == "4":
        print("Usted ha seleccionado la opción 4. ¡Hasta luego!")
        break  # Terminar la ejecución del programa
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.\n")