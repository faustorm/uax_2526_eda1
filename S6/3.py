"""
Crea una tupla con tres elementos numéricos y uno textual.​

Intenta modificar el segundo elemento de la tupla (esto debería resultar en un error).​

Escribe un código para extraer e imprimir cada elemento de la tupla utilizando un bucle.​

Utiliza desempaquetado de tuplas para asignar estos valores a las variables a, b, y c y luego imprime sus valores.
"""
tupla = ( 1, 9, "hola")
#tupla[1] = 99

for el in tupla:
    print(el)

x, y, z = tupla
print(x, y, z)

diccionario = { "nombre": "Fausto"}
print(diccionario["nombre"])