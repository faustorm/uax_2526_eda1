from clases import Persona
import time

personas = [
    Persona("pepe","garcia","martin", "1987-06-04", "222222D"),
    Persona("Ana","garcia","martin", "1989-05-08", "222222D")
]

while True:
    time.sleep(1)
    for persona in personas:
        persona.saludar()
        persona.mover()