import os
from turtle import color
import cv2 as cv
import numpy as np

def click_raton(event,x,y,flags,param):
    global color_punto,lower_color,upper_color,objeto_capa
    if event == cv.EVENT_LBUTTONDBLCLK:
        b,g,r = frame[y,x]
        color_punto = np.uint8([[[b,g,r]]])
        color_punto = cv.cvtColor(color_punto,cv.COLOR_BGR2HSV)

        lower_color = np.array([np.array(color_punto[0,0,0])-10,10,10])
        upper_color = np.array([np.array(color_punto[0,0,0])+10,255,255])
        objeto_capa = frame
        print(f"{lower_color} - {upper_color} - {color_punto}")

video = cv.VideoCapture(0)
color_punto=None
cv.namedWindow("Salida")
cv.setMouseCallback("Salida",click_raton)
frameObjeto=None
frame_inicial=None
objeto_capa = None

while(True):
    ret, frame = video.read()
    if ret == True:
        frame = cv.flip(frame, 1)
        cv.imshow("Salida", frame)
    if cv.waitKey(10) & 0xFF == 27: break
    if cv.waitKey(10) & 0xFF == 32: 
        if frame_inicial is None:
            cv.namedWindow("Mascara")
            cv.imshow("Mascara", frame)
            frame_inicial = frame

    if objeto_capa is not None:
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV) 
        cv.namedWindow("Mascara")
        white=cv.inRange(hsv,lower_color,upper_color)
        frame_inicial_gray = cv.cvtColor(frame_inicial, cv.COLOR_BGR2GRAY)
        mask_negra = cv.inRange(white, 0, 128)  # Máscara para la región negra
        mask_blanca = cv.inRange(white, 129, 255)  # Máscara para la región blanca
        img1 = cv.bitwise_and(frame, frame, mask=mask_negra)
        img2 = cv.bitwise_and(frame_inicial, frame_inicial, mask=mask_blanca)
        img_final = cv.add(img1, img2)
        cv.imshow("AND",img_final)

video.release()
cv.destroyAllWindows()
