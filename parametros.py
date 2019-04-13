# ----------------------------------
# Archivo parametros (constantes)
# ----------------------------------

import numpy as np

K = 8.988E9 # Constante de Coulomb = 8.988 x 10**9 [(N * m**2)/C**2]
tamanio_fisico = np.array([24E-3, 48E-3]) # altoZ y anchoX del canvas fisico (10 mm)
tamanio_pixeles = np.array([600, 1200]) # altoZ y anchoX de la pantalla (pixeles)
escala = tamanio_pixeles / tamanio_fisico # pixeles por mm de simulacion real
delta_tiempo = 1E-6 # tiempo de actualizacion de la simulacion (1 micro segundo)
radio = 40E5 # valor estandar de radio para generar circulo a traves de la masa
limite_colision = 1 # valor para detectar colisiones entre particulas
timer = 0 # valor de timer para mostrar datos periodicamente
color_neutro = "green" # color default particula
color_positiva = "blue" # color particulas carga tipo positiva
color_negativa = "red" # color particulas carga tipo negativa
color_fondo = "white" # color fondo pantalla
color_letra_label = "white"
color_bg_label = "black"


## Deprecated ##

#tiempo = 0.001 # milisegundos
#ancho_pantalla = 1200 # pixeles
#alto_pantalla = 600 # pixeles
#ancho_fisico = 2400 # metros
#alto_fisico = 1200 # metros
#escala_x = ancho_fisico / ancho_pantalla # 1 pixel = 2 metros
#escala_y = alto_fisico / alto_pantalla # 1 pixel = 2 metros
