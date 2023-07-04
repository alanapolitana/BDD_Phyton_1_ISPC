import time

print('\n*************************** SISTEMA DE VALIDACIÓN DE DATOS CAJERO ISPC ***************************\n')

intentos = 0
user = 'admin'
password = 123


while intentos < 3:
    nombre_de_usuario = input(
        '   ► Ingrese su nombre de usuario, por favor: \n').lower()
    print()
    contrasenia = int(
        input('   ► Ingrese los 3 dígitos de su contraseña, por favor: \n'))
    time.sleep(1)
    if nombre_de_usuario == user and contrasenia == password:
        print('        Ingreso exitoso.')
        time.sleep(1)
        print(f'\nQue tenga una buena jornada ☺ !\n')
        print('\n*************************** FIN PROCESO DE VALIDACIÓN DE DATOS ***************************\n')

        print('\n*************************** M E N Ú ***************************\n')
# ************************************* M E N U ***********************************************************

        while True:  # loop infinito hasta break
         # Solicitar la opción elegida al usuario
            opción_elegida = int(input('''\n Ingrese el número de la opción elegida :\n
            ♦ opción 1 → Ingreso de dinero\n
            ♦ opción 2 → Extracción de dinero\n
            ♦ opción 3 → Consulta de saldo\n
            ♦ opción 4 → Salir\n
            \n'''))
# OPCION 4- sale del programa

            if opción_elegida == 4:
                print(f'\nQue tenga una buena jornada ☺ !\n')
                print(
                    '\n*************************** FIN PROCESO DE VALIDACIÓN DE DATOS ***************************\n')
                exit()
# OPCION 1- ingreso DE DINERO
            elif opción_elegida == 1:
                while True:
                    cantidad_a_depositar = int(input(
                        '\nIngrese la cantidad de dinero, en número enteros, que desea depositar:\n $'))
                    check = int(input(
                        f'\nUsted desea depositar ${cantidad_a_depositar},\n► si es correcto ingrese 1 de lo contrario\n ► digite 2 para ingresar un nuevo monto\n ► para volver al menú principal digite 3\n'))
                    saldo_actual = 10000 + cantidad_a_depositar
                    if check == 3:
                        print(
                            f' \n Usted ha depositado ${cantidad_a_depositar}.')
                        print(f'Su saldo actual es de ${saldo_actual}')
                        print('\n Dirigiendo al menú principal \n')
                        time.sleep(1)
                        break
                    elif check == 2:
                        continue
                    elif check == 1:
                        print(
                            f' \n Usted ha depositado ${cantidad_a_depositar}.')
                        print(f'Su saldo actual es de ${saldo_actual}')
                        print(f'\nQue tenga una buena jornada ☺ !\n')
                        print('FIN DEL PROCESO \n')
                        exit()
# OPCION 2- EXTRACCION DE DINERO
            elif opción_elegida == 2:
                while True:
                    cantidad_a_extraer = int(input(
                        '\nIngrese la cantidad de dinero, en número enteros, que desea extraer:\n $'))
                    check = int(input(
                        f'\nUsted desea extraer ${cantidad_a_extraer},\n► si es correcto ingrese 1 de lo contrario\n ► digite 2 para ingresar un nuevo monto\n ► para volver al menú principal digite 3\n'))
                    saldo_actual = 10000 - cantidad_a_extraer
                    if check == 3:
                        print(f' \n Usted ha extraído ${cantidad_a_extraer}.')
                        print(f'Su saldo actual es de ${saldo_actual}')
                        print('\n Dirigiendo al menú principal \n')
                        time.sleep(1)
                        break
                    elif check == 2:
                        continue
                    elif check == 1:
                        print(f' \n Usted ha extraído ${cantidad_a_extraer}.')
                        print(f'Su saldo actual es de ${saldo_actual}')
                        print(f'\nQue tenga una buena jornada ☺ !\n')
                        print('FIN DEL PROCESO \n')
                        exit()

# OPCION 3- CONSULTAR SALDO
            elif opción_elegida == 3:
                saldo = 10000
                print(f'Su saldo inicial es de ${saldo}')
                while True:
                    check = int(input(
                        f'\n► para finalizar digite 1\n ► para volver al menú principal digite 2\n '))
                    if check == 1:
                        print(f'\nQue tenga una buena jornada ☺ !\n')
                        print(f' \n FIN DEL PROCESO \n')
                        exit()
                    elif check == 2:
                        break

# corroborar datos
    else:
        intentos += 1
# EXCESO INTENTOS DE  INGRESO- SE CIERRA
        if intentos == 3:
            time.sleep(2)
            print("\n Ha excedido el número máximo de intentos. Cuenta bloqueada.\n")
            print(f'\nQue tenga una buena jornada ☺ !\n')
            print(
                '\n*************************** FIN PROCESO DE VALIDACIÓN DE DATOS ***************************\n')
            exit()
        else:
            print("\nCredenciales incorrectas.\n")