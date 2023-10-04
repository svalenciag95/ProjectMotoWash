import cv2
import numpy as np 
import pytesseract
from PIL import Image

Ctexto = ''

ruta_video = 0

##realizar la captura del video

cap = cv2.VideoCapture(ruta_video)

while True:
    ##realiar la lectura de la videocamara
    ret, frame = cap.read()

    if ret == False:
        break

    #dibujamso un rectangulo
    cv2.rectangle(frame,(850, 750), (1070, 850), (0, 0, 0), cv2.FILLED)
    cv2.putText(frame, Ctexto[0:7], (900, 810), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    #extraer el ancho y el alto de los fotogramas
    al, an, c = frame.shape

    #tomar el centro de la imagen
    #en x:
    x1 = int(an /3)  # se toma el 1/3 de la imagen
    x2 = int(x1 * 2) # hasta el iniicio del 3/3 de la imagen

    #en y:
    y1 = int(al /3)  # se toma el 1/3 de la imagen
    y2 = int(x1 * 2) # hasta el iniicio del 3/3 de la imagen

    # texto
    cv2.rectangle(frame, (x1 + 160, y1 +500), (1120, 940), (0, 0, 0), cv2.FILLED)
    cv2.putText(frame, "Procesando Placa", (x1 + 180, y1 +550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    #ubicamos el rectangulo en las zonas extraidas
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    #realizamos un recorte de nuestra zona de interes
    recorte = frame[y1:y2, x1:x2]

    nB = recorte[:, :, 0]
    nG = recorte[:, :, 1]
    nR = recorte[:, :, 2]

    # Color
    Color = cv2.absdiff(nG, nB)

    # Binarizamos la imagen
    _, umbral = cv2.threshold(Color, 40, 255, cv2.THRESH_BINARY)

    # Extraer los contornos de la zona seleccionada
    contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contornos = sorted(contornos, key=lambda x: cv2.contourArea(x), reverse=True)

    #preprocesamiento de la zona de interes
    # nB = np.matrix(recorte [:, :, 0])
    # nG = np.matrix(recorte [:, :, 1])
    # nR = np.matrix(recorte [:, :, 2])

    # #color
    # Color = cv2.absdiff(nG, nB)

    # #binarizamos la imagen
    # _, umbral = cv2.threshold(Color, 40, 255, cv2.THRESH_BINARY)

    # #extraer los contornos de la zona seleccionada
    # contornos = sorted(contornos, key=lambda x: cv2.contourArea(x), reverse=True)

    #dibujar los contornos extraidos 

    for contorno in contornos:
        area = cv2.contourArea(contorno)
        if area > 500 and area < 5000:
            # detectar la placa
            x, y, ancho, alto = cv2.boundingRect(contorno)

            #extraer las coordenadas
            xpi = x + x1
            ypi = y + y1

            xpf = x + ancho + x1
            ypf = y + alto + y1

            #dibujar el rectangulo
            cv2.rectangle(frame, (xpi, ypi), (xpf, ypf), (255, 255, 0), 2)

            #extraer los pixeles
            placa = frame[ypi:ypf, xpi:xpf]

            #extraer el ancho y el alto de los fotogramas
            alp, anp, cp = placa.shape
            #print(alp, anp)

            #procesar los pixeles para extraer los valores de las placas
            Mva = np.zeros((alp, anp))

            #normalizar las matrices
            nBp = np.matrix(placa[:, :, 0])
            nGp = np.matrix(placa[:, :, 1])
            nRp = np.matrix(placa[:, :, 2])

            #crear una mascara
            for col in range(0, alp):
                for fil in range(0, anp):
                    max = max(nRp[col, fil], nGp[col, fil], nBp[col, fil])
                    Mva[col, fil] = 255 - max

            #binarizar la imagen
            _, bin = cv2.threshold(Mva, 150, 255, cv2.THRESH_BINARY)

            #convertir la matrix en imagen
            bin = bin.reshape(alp, anp)
            bin = Image.fromarray(bin)
            bin = bin.convert("L")

            #asegurar tener un buen tamaño de la placa
            if alp >= 36 and anp > 82:
                
                #declarar la direccion de Pytesseract
                pytesseract.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR'

                #extraer el texto
                config = "--psn 1"
                texto = pytesseract.image_to_string(bin, config=config)

                #if para no mostrar basura
                if len(texto) >= 7:
                    #print(texto[0:7])

                    Ctexto = texto

                    #mostrar los valores que nos interesan
                    #cv2.putText(frame, Ctexto[0:7], (910, 810), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            break

            #mostrar el recortte 
            #cv2.imshow("recorte", bin)
    
    #mostrar el recorte en gris
    cv2.imshow("vehiculos", frame)

    #leemos una tecla
    t = cv2.waitKey(1)

    if t == 27:
        break

cap.release()
cv2.destroyAllWindows()









