#problema 1
def get_fuel_porcentaje():
    while True:
        try:
            n=int(input("Ingrese el primer numero: "))
            m=int(input("Ingrese el segundo numero: "))
            print("{}/{} = {}".format(n,m,n/m))
            
            if m == 0 or n > m:
                print("Por favor, ingrese numeros validos")
                continue
            
            porcentaje = (n/m)*100
            
            if porcentaje < 1:
                return "E"
            elif porcentaje > 99: 
                return "F"
            else:
                return f"{round(porcentaje)}%"
            
        except ValueError:
            print("Por favor, ingrese un numero entero")
        
        except ZeroDivisionError:
            print("El denominador no puede ser cero")
            
fuel_porcentaje = get_fuel_porcentaje()
print("Cantidad de combustible en el tanque:", fuel_porcentaje)



#problema 2
while True:
        try:
            calificaciones = input("Por favor, ingrese sus calificaciones, separadas por comas: ")
            calificaciones_lista = calificaciones.split(',')
            calificaciones_enteros = []

            for calificaciones in calificaciones_lista:
                try:
                    calificaciones_entero = int(calificaciones)
                    calificaciones_enteros.append(calificaciones_entero)
                except ValueError:
                    print(f"Error: '{calificaciones}' no es una calificación válida")
                    
                if calificaciones_enteros:
                        print("Calificaciones convertidas a enteros:", calificaciones_enteros)
                    
                else:
                    print("No se ingresaron calificaciones válidas")
                    break  

        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")


#problema 3
import math
class CIRCULO:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2

radio_circulo = float(input("Ingrese el radio del círculo: "))
circulo = CIRCULO(radio_circulo)

area = circulo.calcular_area()
print(f"El área del círculo con un radio de {radio_circulo} es: {area:.2f}")



#problema 4
import math
class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho  
    
    def calcular_area(self):
        return self.largo * self.ancho 

largo_rectangulo = float(input("Ingrese el largo del rectangulo: "))
ancho_rectangulo = float(input("Ingrese el ancho del rectangulo: "))
rectangulo = RECTANGULO(largo_rectangulo, ancho_rectangulo)

area = rectangulo.calcular_area()
print(f"El área del rectangulo con un largo de {largo_rectangulo} y un ancho de {ancho_rectangulo} es: {area:.2f}")


#problema 5
class Alumno:
    def __init__(self,nombre,registro):
        
        self.nombre = nombre
        self.registro = registro
        
    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.notas:
            print("Notas:")
            for i, nota in enumerate(self.notas, start=1):
                print(f"Nota {i}: {nota}")
        
    def setAge(self,age):
        self.age = age
        
    def setNota(self,nota):
        self.nota = nota 


#problema 6
class punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y 

    def __str__(self):
        return f"({self.x},{self.y})"

punto1 = punto(2, 5)
punto2 = punto()    

print("Punto 1:", punto1)
print("Punto 2:", punto2)

def cuadrante (self):
    if (self.x > 0 and self.y > 0):
        print("primer cuadrante") 

    elif (self.x < 0 and self.y > 0):
        print("segundo cuadrante")

    elif (self.x < 0 and self.y < 0):
        print("tercer cuadrante")

    elif (self.x > 0 and self.y < 0):
        print("cuarto cuadrante")

    elif (self.x == 0 and self.y!= 0 ):
        print("Se encuentra en el eje Y")

    elif (self.x != 0 and self.y == 0 ):
        print("Se encuentra en el eje X")

    elif (self.x == 0 and self.y == 0 ):
        print("Se encuentra en el Origen")
    pass


def vector(self, otro_punto):
        dx = otro_punto.x - self.x
        dy = otro_punto.y - self.y
        return Punto(dx, dy)
def distancia(self, otro_punto):
        dx = otro_punto.x - self.x
        dy = otro_punto.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return distancia

class RECTANGULO:
    def __init__(self, p1=punto(0,0), p2=punto(2,5)):
        self.p1 = p1 
        self.p2 = p2
        pass

def __init__(self, largo, ancho):
        self.largo = largo
        punto = self.pi.vector(self.p1)
        return abs(p1.y)

        self.ancho = ancho 
        punto = self.pi.vector(self.p2)
        return abs(p2.x) 

def area(self):
        A = self.pi.vector(self.pf)
        return p1.x * p2.y 


#problema 7
import random
def numeros_aleatorios():
    numeros_aleatorios = [random.randint(0, 100) for i in range(20)]
    return numeros_aleatorios

def mostrar_lista(lista):
    print("Lista obtenida:")
    for numero in lista:
        print(numero, end=" ")

def ordenar_y_mostrar(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:")
    for numero in lista_ordenada:
        print(numero, end=" ")

numeros = numeros_aleatorios()
mostrar_lista(numeros)
ordenar_y_mostrar(numeros)


#problema 8
def suma(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido"

def resta(a, b):
    try:
        resultado = a - b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido"

def producto(a, b):
    try:
        resultado = a * b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido"

def division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Error: No es posible dividir entre cero")
        resultado = a / b
        return resultado
    except (TypeError, ZeroDivisionError) as i:
        return f"Error: {i}"
    
            


