# ----------------------------------
# Clase Particula
# ----------------------------------

import numpy as np
from math import sqrt
from parametros import *


class Particula():
    def __init__(self, nombre, carga, masa, x0, y0):
        self.nombre = nombre # Identificador unico de la carga
        self.carga = carga # Carga en C
        self.masa = masa # Masa en Kg
        self.pos = np.array([x0, y0]) # Vector posicion de la particula
        self.vel = np.zeros(2)
        self.acel = np.zeros(2)
        self.fuerza = np.zeros(2) # Vector Fuerza en N
        self.fuerza_total = np.zeros(2)
        self.circulo = None # circulo que representa a la particula (se crea al cargar el programa)
        self.radio = radio * self.masa # radio del circulo que representa la particula, afectado en forma dir proporcional a su masa
        self.aplicar_color() # metodo que aplica color a la particula dependiendo su carga        

    
    #####################
    #### Cosmeticas #####
    #####################

    # Metodo que toma la posicion x e y de la particula, crea un circulo usando 
    # su atributo del radio y lo rellena con su color
    def crear_circulo(self, canvas):        
        x0 = self.set_circulo()[0]
        y0 = self.set_circulo()[1]
        x1 = self.set_circulo()[2]
        y1 = self.set_circulo()[3]
        self.circulo = canvas.create_oval(x0, y0, x1, y1, fill = self.color)
    
    def mover_circulo(self, canvas):        
        x0 = self.set_circulo()[0]
        y0 = self.set_circulo()[1]
        x1 = self.set_circulo()[2]
        y1 = self.set_circulo()[3]
        canvas.coords(self.circulo, x0, y0, x1, y1)
    
    def set_circulo(self):
        x0 = np.round((self.pos[0] * escala[0]) - self.radio)
        y0 = np.round((self.pos[1] * escala[1]) - self.radio)
        x1 = np.round((self.pos[0] * escala[0]) + self.radio)
        y1 = np.round((self.pos[1] * escala[1]) + self.radio)
        return (x0, y0, x1, y1)
                
    # Metodo para colorear el circulo que representa a la particula
    # Si la carga es mayor a 0 aplica el color para cargas positivas
    # Si la carga es menor a 0 aplica el color para cargas negativas
    # Si la carga es 0 aplica el color para cargas neutras
    def aplicar_color(self):
        if self.carga > 0:
            self.color = color_positiva
        elif self.carga < 0:
            self.color = color_negativa
        else:
            self.color = color_neutro
    
    #####################
    ###### Fisicas ######
    #####################
    
    # metodo para calcular la fuerza ejercida por otra particula
    def calcular_fuerza(self, lista_particulas):
        # F = K * ((q1*q2) / (r**2))
        self.fuerza_total = np.zeros(2)        
        for p in lista_particulas:
            if p.nombre is not self.nombre:
                # si hay colision entre particulas las detengo
                # si no hay calculo la fuerza y la sumarizo 
                if self.calcular_colisiones_particulas(p):
                    self.stop()
                    p.stop()
                else:
                    # F = K * q1*q2 * (pos1 - pos2) / | pos2 - pos1| * 3
                    self.fuerza = K * (p.carga * self.carga) * (p.pos - self.pos)/ (np.linalg.norm(p.pos - self.pos) ** 3)

                # como el vector resultante que obtengo de la formula F es en realidad la fuerza de la particula
                # sobre la restante, multiplico por -1 para cambiar el sentido y obtener la fuerza de la otra
                self.fuerza_total += self.fuerza * -1


    def calcular_aceleracion(self):
        # A = F/M        
        self.acel = self.fuerza_total / self.masa
    
    def calcular_velocidad(self):
        # V = v0 + A * t        
        self.vel = self.vel + self.acel * delta_tiempo
    
    def calcular_posicion(self):
        # d = d0 + V*t + 1/2 (a*(t**2))        
        self.pos = self.pos + self.vel * delta_tiempo + ((self.acel * delta_tiempo**2) / 2)

    ######################
    ##### Colisiones #####
    ######################

    # funcion para calcular si hay colision entre las particulas               
    def calcular_colisiones_particulas(self, p):
        distancia_centros = (np.linalg.norm(self.pos - p.pos)) * escala[0]
        suma_radios = self.radio + p.radio
        distancia = distancia_centros - suma_radios
        # si a la distancia euclidea entre los centros de particula le resto sus respectivos radios obtengo
        # la distancia de borde a borde
        if abs(distancia) < limite_colision:
            # hay colision
            return True 
        else:
            # no hay colision
            return False

    def calcular_colisiones_bordes(self):
        # Colisiones contra los bordes de la pantalla
        lado_der = self.pos[0] * escala[0] + self.radio
        lado_izq = self.pos[0] * escala[0] - self.radio
        techo = (self.pos[1] * escala[1] - self.radio)
        piso = self.pos[1] * escala[1] + self.radio

        if lado_der >= tamanio_pixeles[1]:
            # colision contra borde derecho pantalla 
            self.stop_x()                
        elif lado_izq <= 0:
            # colision contra borde izquierdo pantalla
            self.stop_x()

        if techo <= 0:
            # colision contra borde superior pantalla
            self.stop_y()
        elif piso >= tamanio_pixeles[0]:
            # colision contra borde inferior pantalla
            self.stop_y()             
                
    
    def stop_x(self):
        self.fuerza[0] = 0
        self.acel[0] = 0
        self.vel[0] = 0
    
    def stop_y(self):
        self.fuerza[1] = 0
        self.acel[1] = 0
        self.vel[1] = 0
    
    def stop(self):
        self.stop_x()
        self.stop_y()
    
    ###################
    ###### Datos ######
    ###################

    # Metodo que muestra datos importantes de la particula
    # Como su nombre, componentes del vector en X e Y y su sumatoria
    # Por ultimo la aceleracion, velocida y posicion de la particula
    def mostrar_datos(self):
        print(f"Particula {self.nombre}")
        print(f"F:{self.fuerza}[N]")
        print(f"Acel:{self.acel}[mm/sg2] -- Vel:{self.vel}[mm*sg] -- Pos:{self.pos}[mm]")
        print("-----------------------------------------------------------------------------------------------------")
        