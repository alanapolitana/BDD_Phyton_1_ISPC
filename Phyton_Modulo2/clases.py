# Ejercicios sobre clases
# Resolver utilizando clases, método constructor y métodos.
# 1. Clase Rectángulo: Crea una clase Rectangulo que tenga atributos base y
# altura. Luego, define métodos para calcular el área y el perímetro del
# rectángulo.

class Rectangulo:
    def _init_(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

# Ejemplo de uso de la clase Rectangulo
rectangulo = Rectangulo(4, 5)
area = rectangulo.calcular_area()
perimetro = rectangulo.calcular_perimetro()

print(f"El área del rectángulo es: {area}")
print(f"El perímetro del rectángulo es: {perimetro}")


# En este ejemplo, la clase Rectangulo tiene un método constructor _init_ que recibe los valores de la base y la altura y los asigna a los atributos correspondientes self.base y self.altura.

# La clase también tiene dos métodos adicionales: calcular_area y calcular_perimetro. El método calcular_area multiplica la base por la altura y devuelve el resultado, mientras que el método calcular_perimetro calcula el perímetro sumando dos veces la base y dos veces la altura.

# Después de definir la clase, puedes crear un objeto rectangulo de la clase Rectangulo pasando los valores de la base y la altura. Luego, puedes llamar a los métodos calcular_area y calcular_perimetro en el objeto rectangulo para obtener el área y el perímetro respectivamente. Finalmente, puedes imprimir los resultados. En el ejemplo se utiliza f-string para formatear los mensajes de salida.

# 2. Clase Estudiante: Crea una clase Estudiante que tenga atributos nombre y
# edad. Luego, define un método para imprimir la información del
# estudiante. Realiza 3 instancias de esta clase.
class Estudiante:
    def _init_(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

# Ejemplo de uso de la clase Estudiante
estudiante1 = Estudiante("Juan", 20)
estudiante2 = Estudiante("María", 22)
estudiante3 = Estudiante("Pedro", 19)

estudiante1.imprimir_informacion()
print()  # Imprimir una línea en blanco para separar la información de los estudiantes
estudiante2.imprimir_informacion()
print()
estudiante3.imprimir_informacion()


# En este ejemplo, la clase Estudiante tiene un método constructor _init_ que recibe los valores del nombre y la edad y los asigna a los atributos correspondientes self.nombre y self.edad.

# La clase también tiene un método imprimir_informacion que imprime en pantalla la información del estudiante, incluyendo su nombre y edad.

# Después de definir la clase, se crean tres objetos estudiante1, estudiante2 y estudiante3 de la clase Estudiante pasando los valores del nombre y la edad. Luego, se llama al método imprimir_informacion en cada uno de los objetos para imprimir su información respectiva.

# Al ejecutar el código, se mostrará la información de los tres estudiantes en la consola.



# 3. Clase Libro: Crea una clase Libro que tenga atributos titulo, autor y anio.
# Luego, define un método para imprimir la información completa del libro.

class Libro:
    def _init_(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def imprimir_informacion(self):
        print("Información del libro:")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.anio}")

# Ejemplo de uso de la clase Libro
libro1 = Libro("1984", "George Orwell", 1949)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
libro3 = Libro("El principito", "Antoine de Saint-Exupéry", 1943)

libro1.imprimir_informacion()
print()  # Imprimir una línea en blanco para separar la información de los libros
libro2.imprimir_informacion()
print()
libro3.imprimir_informacion()

# En este ejemplo, la clase Libro tiene un método constructor _init_ que recibe los valores del título, autor y año, y los asigna a los atributos correspondientes self.titulo, self.autor y self.anio.

# La clase también tiene un método imprimir_informacion que imprime en pantalla la información completa del libro, incluyendo el título, autor y año.

# Después de definir la clase, se crean tres objetos libro1, libro2 y libro3 de la clase Libro pasando los valores del título, autor y año. Luego, se llama al método imprimir_informacion en cada uno de los objetos para imprimir su información completa.

# Al ejecutar el código, se mostrará la información de los tres libros en la consola




# 4. Clase Calculadora: Crea una clase Calculadora que tenga métodos para
# realizar operaciones matemáticas básicas, como suma, resta, multiplicación
# y división. También puedes agregar métodos adicionales según tus
# necesidades.

class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        if b != 0:
            return a / b
        else:
            print("Error: división por cero")
            return None

# Ejemplo de uso de la clase Calculadora
calculadora = Calculadora()

resultado_suma = calculadora.suma(5, 3)
print("Suma:", resultado_suma)

resultado_resta = calculadora.resta(10, 4)
print("Resta:", resultado_resta)

resultado_multiplicacion = calculadora.multiplicacion(6, 2)
print("Multiplicación:", resultado_multiplicacion)

resultado_division = calculadora.division(8, 2)
print("División:", resultado_division)

resultado_division_por_cero = calculadora.division(10, 0)
print("División por cero:", resultado_division_por_cero)



# En este ejemplo, la clase Calculadora tiene cuatro métodos: suma, resta, multiplicacion y division, cada uno de los cuales realiza una operación matemática básica y devuelve el resultado.

# En el método division, se verifica si el divisor b es diferente de cero antes de realizar la operación para evitar una división por cero. Si el divisor es cero, se imprime un mensaje de error y se devuelve None.

# Después de definir la clase, se crea un objeto calculadora de la clase Calculadora. Luego, se llaman a los métodos de la calculadora pasando los valores necesarios para realizar las operaciones matemáticas.

# Al ejecutar el código, se mostrarán los resultados de las operaciones en la consola.




# 5. Clase Círculo: Crea una clase Circulo que tenga un atributo radio. Luego,
# define métodos para calcular el área y la circunferencia del círculo.

import math

class Circulo:
    def _init_(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2

    def calcular_circunferencia(self):
        return 2 * math.pi * self.radio

# Ejemplo de uso de la clase Circulo
circulo = Circulo(5)

area = circulo.calcular_area()
print("Área del círculo:", area)

circunferencia = circulo.calcular_circunferencia()
print("Circunferencia del círculo:", circunferencia)


# En este ejemplo, la clase Circulo tiene un atributo radio que se inicializa en el método constructor _init_. Luego, se definen dos métodos: calcular_area y calcular_circunferencia.

# El método calcular_area utiliza la fórmula del área del círculo (π * radio^2) para calcular y devolver el área del círculo.

# El método calcular_circunferencia utiliza la fórmula de la circunferencia del círculo (2 * π * radio) para calcular y devolver la circunferencia del círculo.

# Después de definir la clase, se crea un objeto circulo de la clase Circulo con un radio de 5. Luego, se llaman a los métodos calcular_area y calcular_circunferencia del objeto circulo para obtener y mostrar el área y la circunferencia del círculo respectivamente.

# Al ejecutar el código, se mostrarán los resultados en la consola.