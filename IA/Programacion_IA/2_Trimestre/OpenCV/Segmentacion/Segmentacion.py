import csv
import os
import pathlib
from turtle import color
from click import Path
import cv2 as cv
from matplotlib.pyplot import hsv
import numpy as np
from sklearn.preprocessing import maxabs_scale

def click_raton(event,x,y,flags,param):
    # AL HACER DOBLE CLICK
    global color_punto
    if event == cv.EVENT_LBUTTONDBLCLK:
        # SACAMOS LA SATURACIÓN COLOR ...
        b,g,r = img1[y,x]
        # LE DECIMOS QUE NOS DE EL PUNTO DE COLOR COMO UN NP.INT
        color_punto = np.uint8([[[b,g,r]]])
        # SACAMOS EL COLOR DEL PUNTO 
        color_punto = cv.cvtColor(color_punto,cv.COLOR_BGR2HSV)
        # PRINTAMOS
        print(f"Cick en {x}, {y}, color:{color_punto}")


data_dir = os.path.dirname(__file__)
path = os.path.abspath(os.path.join(data_dir, os.pardir))+"/imagenes/"

# LE DECIMOS QUE LEA LA RUTA ANTERIOR EN IMAGENES Y LA IMAGEN DE NEMO
scr1 = cv.imread(path+"nemo.jpg")
# NOMBRAMOS LA VENTANA IMAGEN
cv.namedWindow("Imagen")
img1 = scr1

# LE DECIMOS QUE POR O DE AHORA NO SE DIO CLICK EN EL PUNTO Y NO TIENE COLOR
color_punto=None
hsv = cv.cvtColor(img1,cv.COLOR_BGR2HSV)
# LE DECIMOS QUE LA VENTANA IMAGEN TENGA CLICK RATÓN FUNCIÓN YA DEFINIDA
cv.setMouseCallback("Imagen",click_raton)
# LE DECIMOS QUE LO MUESTRE
cv.imshow("Imagen", img1)


while True:
    # EN EL MOMENTO QUE LA FUNCIÓN LEA EL DOBLE CLICK, SE HACE LO QUE SE QUIERE Y LUEGO VUELVE A NONE
    if color_punto is not None:
        color_minimo = np.array([color_punto[0,0,0] - 10,10,10])
        color_maximo = np.array([color_punto[0,0,0] + 10,255,255])
        mascara = cv.inRange(hsv, color_minimo, color_maximo)
        cv.namedWindow("Mascara")
        cv.imshow("Mascara", mascara)
        color_punto = None
    # Y LE DECIMOS QUE ESPERE HASTA DARLE ESCAPE
    if cv.waitKey(10) & 0xFF == 27 : break