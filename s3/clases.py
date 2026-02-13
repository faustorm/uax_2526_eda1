import time

class Persona:
    def __init__(self,nombre,ano, estudios = [], documento = None, tipo_documento = None, posicion_inicial = [0,0], velocidad = 1):
        self.nombre = nombre
        self.ano_nacimiento = ano
        self.edad = 2026 - self.ano_nacimiento
        self.documento = documento
        self.tipo_documento = tipo_documento
        self.estudios = estudios
        self.posicion = posicion_inicial
        self.velocidad = velocidad

    def saludar(self):
        saludo = f"Hola, me llamo {self.nombre} y tengo {self.edad} años."
        print(saludo)

    def get_documento(self):
        if self.documento == None or self.tipo_documento == None:
            return False
        else:
            return { "documento": self.documento, "tipo_documento": self.tipo_documento}
    
    def print_documento(self):
        if self.documento == None or self.tipo_documento == None:
            print(f"No hay información sobre el documento de {self.nombre}")
        else:
            print(f"El {self.tipo_documento} de {self.nombre} es {self.documento}")
        
    def add_estudio(self, estudio):
        self.estudios.append(estudio)
        print(f"{estudio} añadido con éxito")
    
    def print_estudios(self):
        print(", ".join(self.estudios))

    def mover(self):
        desplazamiento_x = self.velocidad   # un random integer entre -velocidad y velocidad
        desplazamiento_y = self.velocidad
        self.posicion = [self.posicion[0] + desplazamiento_x, self.posicion[1] + desplazamiento_y]
    def __str__(self):
        return f"{self.nombre} está en la posición {self.posicion}"

class Alumno(Persona):
    def __init__(self):
        pass

class Espacio:
    def __init__(self, nombre, tamaño = (0,0)):
        self.name = nombre
        self.size_x = tamaño[0]
        self.size_y = tamaño[1]
        self.ocupantes = []
    def __str__(self):
        return f"{self.name} tiene tamaño {self.size_x} x {self.size_y}"
    
    def add_ocupante(self,ocupante):
        self.ocupantes.append(ocupante)
        print(f"{ocupante.name} ha entrado en {self.name}")
    
    def print_ocupantes(self):
        str_ocupantes = ", ".join(ocupante.name for ocupante in self.ocupantes)
        print(str_ocupantes)