from datetime import datetime

class Persona:
    def __init__(self,nombre, apellido1, apellido2, fecha_de_nacimiento, numero_documento):
        self.nombre = nombre
        self.apellidos = f"{apellido1} {apellido2}"
        self.fecha_de_nacimiento = datetime.strptime(fecha_de_nacimiento, "%Y-%m-%d")
        self.numero_documento = numero_documento
    def saludar(self):
        print(f"Hola, soy {self.nombre}")

    def mover(self):
        pass