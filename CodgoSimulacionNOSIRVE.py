import tkinter as tk
import time
import math

#Definicion de constantes

ancho_fisico = 2400
alto_fisico = 1200
ancho_canvas = 1200
alto_canvas = 600 
escala_x = ancho_fisico / ancho_canvas
fuerza = 0
carga1 = 0.01
carga2 = 0.30
constante_vacio = 8.9*pow(10,9)
distancia = 0
tiempo_paso = 1000

#Definicion de clases
class Particula:
    def __init__(self, carga, x, y, masa, vx, vy, ax, ay, color):
        self.circulo = canvas.create_oval(
            x - masa, y - masa, x + masa, y + masa, fill=color
        )
        self.carga = carga
        self.masa = masa
        self.vx = vx
        self.vy = vy
        self.x = x
        self.y = y

    def mover(self, x, y):
        canvas.move(self.circulo, x, y)
        self.x = x
        self.y = y


if __name__ == '__main__':
    root = tk.Tk()

    # create canvas
    canvas = tk.Canvas(root, width=ancho_canvas, height=alto_canvas)
    canvas.pack()

    # create objects
    p = Particula(1, 100, 400, 50, 0, 0, 0, 0, 'blue')
    p2 = Particula(3, 100, 400, 100, 0, 0, 0, 0, 'red')
    #line = canvas.create_line(50, 50, 300,50, fill="black")

   
    def calcular_fuerza():
        fuerza = constante_vacio * ((p.carga*p2.carga)/(p.x-p2.x)**2)
        return fuerza

    #Bucle principal
    while True:
        time.sleep(0.025)
        fuerza = calcular_fuerza()
        print(fuerza)
        #p.mover(p.carga,0)
        #p2.mover(p2.carga,0)
        canvas.update()

