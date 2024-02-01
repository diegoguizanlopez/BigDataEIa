import os
from turtle import color
import cv2 as cv
import numpy as np

#video = cv.VideoCapture(0)

def click_raton(event,x,y,flags,param):
    global color_punto
    if event == cv.EVENT_LBUTTONDBLCLK:
        # SACAMOS LA SATURACIÓN COLOR ...
        b,g,r = frame[y,x]
        # LE DECIMOS QUE NOS DE EL PUNTO DE COLOR COMO UN NP.INT
        color_punto = np.uint8([[[b,g,r]]])
        # SACAMOS EL COLOR DEL PUNTO 
        color_punto = cv.cvtColor(color_punto,cv.COLOR_BGR2HSV)
        # PRINTAMOS
        print(f"Cick en {x}, {y}, color:{color_punto}")

video = cv.VideoCapture(0)
color_punto=None
cv.namedWindow("Salida")
cv.setMouseCallback("Salida",click_raton)

while(True):
    ret, frame = video.read()
    if ret == True:
        frame = cv.flip(frame, 1)
        cv.imshow("Salida", frame)
        
        if color_punto is not None:
            # Creamos la máscara en el punto actual y en vez de pasar imagen pasamos el FRAME
            hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
            color_minimo = np.array([color_punto[0,0,0] - 10,10,10])
            color_maximo = np.array([color_punto[0,0,0] + 10,255,255])
            #color_minimo = np.array([color_punto[0,0,0] - ])
            mascara = cv.inRange(hsv, color_minimo, color_maximo)
            cv.namedWindow("Mascara")
            cv.imshow("Mascara", mascara)
            color_punto = None
    if cv.waitKey(10) & 0xFF == 27: break

video.release()
cv.destroyAllWindows()