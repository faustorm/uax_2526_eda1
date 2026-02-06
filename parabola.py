"""
La ecuación de una parábola es    y = ax**2 + bx + c​
Queremos graficar esta función cuadrática en un rango de valores de x (usa np.linspace para ello)
"""
import numpy as np
import matplotlib.pyplot as plt

def parabola(a,b,c,x):
    y = a*x**2 + b * x + c
    return y

a = int(input("valor de a: "))
b = int(input("valor de b: "))
c = int(input("valor de c: "))

x = np.linspace(1,200,200)
y = np.linspace(1,200,200)

plt.plot(x,y)
plt.show()

