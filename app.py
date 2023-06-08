import cv2
import numpy as np
import pytesseract
from PIL import Image

#Realizar la captura de la imagen
#video = "Placa.mp4"
captura = cv2.VideoCapture(0)
captura_text='PRU-EBA'
#captura_text=''

while True:
    #Realiamos la captura de la imagen
    ret, frame = captura.read()

    
    
    if ret ==False: 
        break
    
    

    #Ancho y el Alto de los fotogramas
    al, an, c = frame.shape

    #Capturar el centro de la imagen

    #En x:
    
    x1 = int(an/3) #Toma el 1/3 de la imagen
    x2 = int(x1*2) #Hasta el inicio de 3/3 de la imagen
    
    #En y:
    y1 = int(al/3) #Toma el 1/3 de la imagen
    y2 = int(y1*2) #Hasta el inicio de 3/3 de la imagen
    
    #texto
    # cv2.rectangle(frame, (x1+160, y1+500),(1120,940),(0,0,0),cv2.FILLED)
    # cv2.putText(frame,"Procesando placa",(x1+180,y1+550),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255, 0),2)
    cv2.rectangle(frame, (x1+210, y1+230),(x1,350),(0,0,0),cv2.FILLED)
    cv2.putText(frame,"Procesando placa",(x1+30,375),cv2.FONT_HERSHEY_PLAIN,1,(0,255, 0),1)

    #Ubicamos el rectangulo en la zonas extraidas
    cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
    
    
    #Zona de captura de la imagen
    # cv2.rectangle(frame,(870,750),(1070,850),(0,0,0),cv2.FILLED)
    # cv2.putText(frame,captura_text[0:7],(900,810),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,255,0),2)
    cv2.rectangle(frame, (x1+210, y1+270),(x1,400),(0,0,0),cv2.FILLED)
    cv2.putText(frame,captura_text[0:7],(x1+60,420),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),)
    
    
    

    #Realizamos un recorte a nuestra zona de interes
    recorte = frame[y1:y2,x1:x2]
    
    


    nB=  np.matrix(recorte[:,:,0])
    nG = np.matrix(recorte[:,:,1])
    nR = np.matrix(recorte[:,:,2])

    
    #Color
    Color = cv2.absdiff(nG,nB)

    #Binarizamos la imagen
    _, umbral = cv2.threshold(Color,40,255,cv2.THRESH_BINARY)

    #Extraemos los contornos de la zona seleccionada
    contornos,_ = cv2.findContours(umbral,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    #Primero ordenamos del mas grande al mas pequeño
    contornos = sorted(contornos,key=lambda x : cv2.contourArea(x), reverse=True)
    
    
    
    
    
    #Dibujamos los contornos extaidos
    for contorno in contornos:
        area = cv2.contourArea(contorno)
        x,y,ancho,alto = cv2.boundingRect(contorno)
        epsilon = 0.09*cv2.arcLength(contorno,True)
        approx = cv2.approxPolyDP(contorno,epsilon,True)
        
        if len(approx)==4 and area>300:
            #Detecta la placa
            #x,y , ancho, alto = cv2.boundingRect(contorno)
            
            aspect_ratio = float(ancho)/alto
            
            #Extraemos las cordenadas
            xpi =  x-x1   #Conocemos la cordenada de la placa en X inicial
            ypi =  y-y1 #Conocemos la cordenada de la placa en Y inicial

            xpf = x + ancho +x1 #Conocemos la cordenada de la placa en X final
            ypf = y + alto + y1 #Conocemos la cordenada de la placa en Y final

            
            #Dibujamos el rectangulo
            #cv2.rectangle(frame, (xpi, ypi),(xpf,ypf),(0,0,255),2)
            cv2.rectangle(frame, (x-xpi,y-ypi),(xpf,ypf),(255,255,0),2)

            #Extraemos los pixeles
            placa = frame[ypi:ypf,xpi:xpf]

            #Extraemos el ancho y el alto de los fotogramas
            alp, anp, cp, =placa.shape

            #Procesamos los pixeles para extraer los valores de las placas
            Mva = np.zeros((alp,alp ))


            #Normalizamos las matrices

            mBp=np.matrix(placa[:,:,0])
            mGp=np.matrix(placa[:,:,1])
            mRp=np.matrix(placa[:,:,2])

            #Creamos una mascara

            for col in range(0,alp):
                for fil in range(0,anp):
                    Max = max(mRp[col,fil],mGp[col,fil],mBp[col,fil])
                    Mva[col,fil]= 255-Max

            #Binarizamos la imagen
            _, bin = cv2.threshold(Mva, 155, 255, cv2.THRESH_BINARY)

            if bin is None:
                continue

            #Convertimos la matriz en imagen
            bin = bin.reshape(alp,anp)
            bin = Image.fromarray(bin)
            bin = bin.convert("L")

            
            
            #Declaramos la dirección de Pytesseract
            pytesseract = pytesseract.pytesseract.tesseract_cmd = r'C:\Users\ameth.galarcio\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

            #extraemos el texto 
            text = pytesseract.image_to_string(bin,config='--psm 11')
            print('PLACA: ',text)
            #if para no mostrar basura log
            if len(text)>=7:
                captura_text = text
                print(captura_text)

            #Nos aseguramos de tener un buen tamañana para la placa
            # if alp >=36 and anp >=50:

            #     #Declaramos la dirección de Pytesseract
            #     pytesseract = pytesseract.pytesseract.tesseract_cmd = r'C:\Users\ameth.galarcio\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

            #     #extraemos el texto 
            #     config = '--psm 1'
            #     texto = pytesseract.image_to_string(bin,config=config)
            #     print(texto)
            #     #if para no mostrar basura log
            #     if len(texto)<=7:
            #         captura_text = texto
            #         print(texto)
            # break
            
            #Mostramos el recorte
            cv2.imshow("Detectado",bin)

        #Mostramos el recorte en gris
        cv2.imshow("Detectar",frame)    

        #leemos una tecla

        t = cv2.waitKey(0)

        if t == 27:
            break
    

captura.release()

cv2.destroyAllWindows()


    



