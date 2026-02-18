#datos de la persona
# nombre
# fecha de nacimiento
# dni
# nomina (dinero que entra con una cierta frecuencia)
from datetime import datetime

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
    def __init__(self,nombre, interes, credito_maximo = 2000):
        self.nombre = nombre
        self.interes = interes
        self.credito_maximo = credito_maximo
    
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
    def __init__(self, banco, dueño, iban = None, divisa = "EUR"):
        self.banco = banco
        self.dueño = dueño
        self.iban = iban
        self.fecha_apertura = datetime.now()
        self.saldo = 0
        self.divisa = divisa
        self.registro_movimientos = [{"fecha":  self.fecha_apertura, "concepto": "Apertura de cuenta", "valor": 0}]

    def get_saldo(self):
        return f"{self.saldo} {self.divisa}"
    
    def ingresar(self, cantidad = 0):
        #validamos que cantidad sea positiva
        if (cantidad > 0):
            self.saldo += cantidad
            concepto = f"Ingreso de {cantidad} {self.divisa}, saldo actual {self.saldo} {self.divisa}"
            self.registro_movimientos.append({"fecha":  datetime.now(), "concepto": concepto, "valor": cantidad})
            print(concepto)

    def validar_identidad(self,cantidad = 0):
        documento_declarado = input("Introduce tu DNI para saber que eres tú: ")
        if(documento_declarado != self.dueño.numero_documento):
            print("Lo siento, si no te sabes tu DNI no me fio de que seas tú")
            self.registro_movimientos.append({"fecha":  datetime.now(), "concepto": "Intento de sacar dinero sin DNI", "valor": cantidad})
            return False

    def sacar_dinero(self, cantidad):
        # validar que tengo saldo suficiente, validar identidad y restar saldo
        if not self.validar_identidad(cantidad):
            return False
        if(self.saldo >= cantidad):
            self.saldo -= cantidad
            concepto = f"Retirada de {cantidad} {self.divisa}, saldo actual {self.saldo} {self.divisa}"
            self.registro_movimientos.append({"fecha":  datetime.now(), "concepto": concepto, "valor": cantidad})
            print(concepto)
            return True
        else:
            print("No tienes un duro, macho")
            return False
        
    def get_movimientos(self):
        registro_movimientos_formateado = self.registro_movimientos
        return self.registro_movimientos

class CuentaCredito(CuentaBancaria):
    def __init__(self, banco, dueño, iban=None, divisa="EUR", credito_maximo = None):
        super().__init__(banco, dueño, iban, divisa)
        if credito_maximo == None:
            self.credito_maximo = banco.credito_maximo
        else:
            self.credito_maximo = credito_maximo

    def sacar_dinero(self, cantidad):
        print(cantidad,self.credito_maximo)
        """if not self.validar_identidad():
            return False"""
        if(cantidad <= self.credito_maximo):
            print("Entra")
            self.saldo -= cantidad
            concepto = f"Retirada de {cantidad} {self.divisa}, saldo actual {self.saldo} {self.divisa}"
            self.registro_movimientos.append({"fecha":  datetime.now(), "concepto": concepto, "valor": cantidad})
            print(concepto)
            return True
        else:
            print(f"{cantidad} es más de lo que te puedo prestar")
            return False