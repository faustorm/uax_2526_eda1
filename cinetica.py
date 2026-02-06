#Ec = ½ * m * v²
def energia_cinetica(masa, velocidad):
    energia_cinetica = 0.5 * masa * velocidad**2
    return energia_cinetica


masa = float(input("Introduce la masa: "))
velocidad = float(input("Y ahora la velocidad: "))

print(f"La energía cinética es de {energia_cinetica(masa,velocidad)} Julios")