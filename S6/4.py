"""
​

Crea un diccionario que represente un libro, incluyendo claves como titulo, autor y año.​

Agrega una nueva clave ISBN con un valor correspondiente.​

Crea una lista de 4 libros, una lista de diccionarios.​

Itera la lista e imprime una frase para cada libro usando interpolación de strings f"Texto {variable}"
"""

libro1 = {"titulo": "Manual de Resistencia", "año": 2019,"autor": "Pedro Sánchez"}
libro1["ISBN"] = "ES11111111111111111"

libros = [
    libro1,
    {"titulo": "Orden y libertad", "año": 2015, "autor": "Jose María Aznar", "ISBN": "ES3333333333"},
    {"titulo": "El Principito", "año": 1917, "autor": "", "ISBN": "ES265656"},
    {"titulo": "Política para adultos", "año": 2025, "autor": "M. Rajoy", "ISBN": "ES26565ssss6"},
    {"titulo": "El Quijote", "año": 1725, "autor": "Miguel de Cervantes", "ISBN": "ES3333333393"}
]

for libro in libros:
    valoracion = ""
    if libro["autor"] == "M. Rajoy":
        valoracion = " es un truño, no lo leas"
        
    print(f"{libro["autor"]} escribió {libro["titulo"]} en {libro["año"]}{valoracion}.")