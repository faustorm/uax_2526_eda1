from clases import Persona, Espacio

persona1 = Persona("Pepe",2007,["Ing. Matemática"])

espacio1 = Espacio("UAX BT502",(20,6))

for _ in range(20):
    #representamos el paso de tiempo con steps
    persona1.mover()
    print(persona1)