"""Dada la lista [10, 20, 30, 40, 50], escribe un script que imprima el primer y el último elemento.​

Modifica el tercer elemento a 35 y muestra la lista modificada"""

lista = [10, 20, 30, 40, 50]

print(lista[0])
print(lista[len(lista)-1])
ultimo = lista.pop()
lista[2] = 35

print(lista, ultimo)