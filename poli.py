import cv2
import numpy as np

imagen1 = cv2.imread('C:\\Users\\caco2\\Desktop\\pollito\\pollito.png')
imagen2 = cv2.imread('C:\\Users\\caco2\\Desktop\\pollito\\pollito1.png')
imagen1 = cv2.resize(imagen1, (300, 300))
imagen2 = cv2.resize(imagen2, (300, 300))

gris1 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2GRAY)
gris2 = cv2.cvtColor(imagen2, cv2.COLOR_BGR2GRAY)

diferencia = cv2.absdiff(gris1, gris2)

umbral = 30
_, umbralizado = cv2.threshold(diferencia, umbral, 255, cv2.THRESH_BINARY)

cv2.imshow('Imagen 1', imagen1)
cv2.imshow('Imagen 2', imagen2)
cv2.imshow('Diferencias resaltadas', umbralizado)

cv2.waitKey(0)
cv2.destroyAllWindows()
