# CATEDRA DE FISICA - VIDEOJUEGOS
# UNIVERSIDAD DE LA CUENCA DEL PLATA
# PROF. GUSTAVO MANUEL DELUCA
#
# PROYECTO: SIMULACION DE ELECTROSTATICA Y MOVIMIENTO DE CARGAS
# VERSION: 1.0 
#
# CON EL CODIGO DE OMAR BAZZI VERSION CAMBIADA PARA MOSTRAR DATOS POR PANTALLA
# ACTUALIZACION: 13-04-2019

# ----------------------------------
# Archivo Main -- Clase simulacion
# ----------------------------------

# Librerias necesarias

import os
import tkinter as tk
import time
from particulas import *
from parametros import *


class Simulacion():
    def __init__(self, root):
        self.running = False
        self.salir = False
        self.root = root
        self.root.bind("<Escape>", self.apagar)
        self.root.bind("<space>", self.pausar)

        canvas.pack()

        # Creo particulas (nombre, carga, masa, x0, y0)
        p1 = Particula("q1", -20E-9, 2E-6, 40E-3, 12E-3)
        p2 = Particula("q2", 25E-9, 3E-6, 5E-3, 15E-3)

        particulas = [p1, p2]
        for p in particulas:
            p.crear_circulo(canvas)
            
        
        timer = 0 # timer local igualado al timer parametrizado
        
        # ---------------------------------------------
        # BUCLE PRINCIPAL - controla la ventana abierta
        # ---------------------------------------------
        while not self.salir:
            self.root.update()

            # ----------------------------------------------------------------------
            # Bucle secundario del programa, controla el estado de pausa o corriendo
            # ----------------------------------------------------------------------
            if self.running:

                # sistema corriendo
                
                time.sleep(delta_tiempo)
                timer += delta_tiempo*1E6

                # --------------------
                # Calculo de colisiones
                # Calculo de fisicas
                # Renderizado
                # --------------------
                
                for p in particulas:
                    p.calcular_colisiones_bordes()
                    ###
                    p.calcular_fuerza(particulas)
                    p.calcular_aceleracion()
                    p.calcular_velocidad()
                    p.calcular_posicion()
                    ###
                    p.mover_circulo(canvas)
                    
                    if (timer % 50) == 0:
                    # cada medio segundo muestro datos en consola
                        #Mostrando datos por pantalla              
                        frame=tk.Frame(root,width=100,height=100,relief='solid',bd=1)
                        frame.place(x=(tamanio_pixeles[1]/2)-100,y=(tamanio_pixeles[0])-10)
                        text=tk.Label(frame,text=f"Carga particula 1: {p1.carga}" + '\n' + f"Posicion particula 1 {p1.pos}"+ '\n' + f"Fuerza particula 1:{p1.fuerza}[N]", font=("Helvetica", 12))
                        text.pack()

                        text2=tk.Label(frame,text=f"Carga particula 2: {p2.carga}" + '\n' +f"Posicion particula 2 {p2.pos}"+ '\n' + f"Fuerza particula 2 {p2.fuerza}[N]", font=("Helvetica", 12))
                        text2.pack()

                # Actualizo la pantalla                
                canvas.update()
            else:
                # sistema pausado
                time.sleep(0)

    # evento bindeado para salir de la simulacion
    def apagar(self, event):
        self.salir = True
        self.root.destroy()

    # evento bindeado para pausar la simulacion
    def pausar(self, event):
        self.running = not(self.running)
    


if __name__ == "__main__":
    root = tk.Tk()
    root.overrideredirect(True)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    canvas = tk.Canvas(root, bg = color_fondo, height = tamanio_pixeles[0], width = tamanio_pixeles[1])
    
    label1 = tk.Label(root, text="Simulacion Ley de Coulomb 2D / Martin Matias", font=("Helvetica", 15),
     fg = color_letra_label, bg = "green")
    label2 = tk.Label(root, text="Presione la tecla ESPACIO para comenzar o pausar la simulacion", font=("Helvetica", 15),
     fg = color_letra_label, bg = "grey") 
    
    label1.pack()
    label2.pack()
    Simulacion(root)