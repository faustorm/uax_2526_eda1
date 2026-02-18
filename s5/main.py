from clases import Banco, Persona, CuentaBancaria, CuentaCredito

#crear un banco
santander = Banco("Santander",4.5)
revolut = Banco("Revolut",3.5)
#crear una persona
persona1 = Persona("Pepe", "García", "García", "2001-01-10", "12121212F")
#crear una cuenta
cuenta2 = CuentaBancaria(santander,persona1,"ES000000000001")

cuenta1 = CuentaCredito(santander,persona1,"ES000000000001", "USD", 900)

#simular movimientos
print(cuenta1.get_saldo())


#cuenta1.sacar_dinero(50)

while True:
    accion = int(input("1 para ingresar, 2 para ver saldo, 3 para sacar dinero, 4 para ver registro  de movimientos, cualquier otro para salir: "))
    if accion == 1:
        cuenta1.ingresar(float(input("¿Qué cantidad quieres ingresar? ")))
    elif accion == 2:
        print(cuenta1.get_saldo())
    elif accion == 3:
        cuenta1.sacar_dinero(float(input("¿Qué cantidad quieres sacar? ")))
    elif accion == 4:
        print(cuenta1.get_movimientos())
    else:
        break