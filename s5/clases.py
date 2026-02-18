#datos de la persona
# nombre
# fecha de nacimiento
# dni
# nomina (dinero que entra con una cierta frecuencia)
import datetime

class Persona:
    def __init__(self,nombre, apellido1, apellido2, fecha_de_nacimiento, numero_documento):
        self.nombre = nombre
        self.apellidos = f"{apellido1} {apellido2}"
        self.fecha_de_nacimiento = datetime.strptime(fecha_de_nacimiento, "%Y-%m-%d")
        self.numero_documento = numero_documento


# entidad (banco)
# código IBAN
# saldo
# registro de movimientos

class Banco:
    def __init__(self,nombre, interes):
        self.nombre = nombre
        self.interes = interes
    
    def get_nombre(self):
        return self.nombre
    
    def get_interes(self):
        return self.interes

# préstamo
# transferir (a otra cuenta)
# ingresar
# sacar dinero
# ver saldo
# ver registro movimientos

class CuentaBancaria:
    def __init__(self, banco, iban = None, divisa = "EUR"):
        self.banco = banco
        self.iban = iban
        self.fecha_apertura = datetime.now()
        self.saldo = 0
        self.divisa = divisa
        self.registro_movimientos = [{"fecha":  self.fecha_apertura, "concepto": "Apertura de cuenta", "valor": 0}]

    def get_saldo(self):
        return self.saldo
    
    def ingresar(self, cantidad = 0):
        #validamos que cantidad sea positiva
        if (cantidad > 0):
            self.saldo += cantidad
            concepto = f"Ingreso de {cantidad} {self.divisa}, saldo actual {self.saldo} {self.divisa}"
            self.registro_movimientos.append({"fecha":  datetime.now(), "concepto": concepto, "valor": cantidad})
            print(concepto)

    def sacar_dinero(self, cantidad, numero_documento):
        # validar que tengo saldo suficiente, validar identidad y restar saldo
        pass


