########################Configuración########################

windowSize = 500
maxRandomExplosionRadius = 200
windowColor = [0, 0, 0]
maxRandomExplosions = 100

#############################################################


import math
import random
import pygame


#Función de explosión
def explotar(radius, xPos, yPos, screenRGB, particleRGB):
    for i in range(radius):
        screen.fill((screenRGB[0], screenRGB[1], screenRGB[2]))
        for speed, angle in particles:
            distance = i * speed
            x = xPos + distance * math.cos(angle)
            y = yPos + distance * math.sin(angle)
            screen.set_at((int(x), int(y)), (particleRGB[0], particleRGB[1], particleRGB[2]))
        pygame.display.flip()


#Preguntar cosas al usuario
randomExpTotalToggle = input("Lanzar un número de explosiones aleatorio? (y/n) ")
if randomExpTotalToggle == "y":
    expTotal = random.randint(0, maxRandomExplosions)
if randomExpTotalToggle == "n":
    expTotal = int(input("Cuántas explosiones debería generar? "))
randomToggle = input("Usar colores aleatorios? (y/n) ")
expColors = []
if randomToggle == "y":
    for i in range(0, expTotal):
        expColors.append([random.randint(0, 255), random.randint(0, 255), random.randint(0,255)])
if randomToggle == "n":
    for i in range(0, expTotal):
        red = int(input("De 0 a 255, cuánto rojo  uso para la explosión " + str(i+1) + "? "))
        grn = int(input("De 0 a 255, cuánto verde uso para la explosión " + str(i+1) + "? "))
        blu = int(input("De 0 a 255, cuánto azul  uso para la explosión " + str(i+1) + "? "))
        print("\n")
        expColors.append([red, grn, blu])
moveToggle = input("Mover las explosiones durante la animación? (y/n) ")
positionsX = []
positionsY = []
if moveToggle == "n":
    for i in range(0, expTotal):
        positionsX.append((windowSize/2))
        positionsY.append((windowSize/2))
if moveToggle == "y":
    motion = input("Uso movimiento aleatorio, lineal horizontal, leneal vertical, diagonal, o manual? (a/h/v/d/m) ")
    if motion == "a":
        for i in range(0, expTotal):
            positionsX.append(random.randint(0, windowSize))
            positionsY.append(random.randint(0, windowSize))
    if motion == "h":
        for i in range(0, expTotal):
            positionsX.append((windowSize/(expTotal+1))*(i+1))
            positionsY.append((windowSize/2))
    if motion == "v":
        for i in range(0, expTotal):
            positionsX.append((windowSize/2))
            positionsY.append((windowSize/(expTotal+1))*(i+1))
    if motion == "d":
        for i in range(0, expTotal):
            positionsX.append((windowSize/(expTotal+1))*(i+1))
            positionsY.append((windowSize/(expTotal+1))*(i+1))
    if motion == "m":
        positionsX.append(int(input("Cual debería ser la coordenada en X de la explosión " + str(i+1) + "? ")))
        positionsY.append(int(input("Cual debería ser la coordenada en Y de la explosión " + str(i+1) + "? ")))
        print("\n")
randomRadiusToggle = input("Usar radios de explosión aleatorios? (y/n) ")
explosionRadius = []
if randomRadiusToggle == "y":
    for i in range(0, expTotal):
        explosionRadius.append(random.randint(0,maxRandomExplosionRadius))
if randomRadiusToggle == "n":
    inverseFullManualToggle = input("Usar el mismo radio para todas las explosiones? (y/n) ")
    if inverseFullManualToggle == "y":
        radius = int(input("Cuál será ese radio?"))
        for i in range(0, expTotal):
            explosionRadius[i] = radius
    if inverseFullManualToggle == "n":
        for i in range(0, expTotal):
            explosionRadius.append(int(input("Cuál debería ser el radio de la explosión " + str(i+1) + "? ")))


print("\n\n\n")
for i in range(0, expTotal):
    print("-----------")
    print("Explosión " + str(i+1))
    print("Color: ", expColors[i])
    print("Radio: ", explosionRadius[i])
    print("X: ", positionsX[i])
    print("Y: ", positionsY[i])
    print("-----------")
    print("\n")


#Inicializar una ventana con la librería pygame
pygame.init()
screen = pygame.display.set_mode((windowSize, windowSize))
particles = [(random.gauss(0,.5), random.uniform(0,6.28318)) for i in range(2000)]


#Inicia código a ejecutar en la ventana
for i in range(0, expTotal):
    explotar(explosionRadius[i], positionsX[i], positionsY[i], windowColor, expColors[i])