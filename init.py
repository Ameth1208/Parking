import keyboard
import cv2
import pytesseract
import numpy
import qrcode
from PIL import Image


#Captura de Foto
def capture_image(camara= cv2.VideoCapture(0)):

    while True:
        #Lee un frame de la camara
        ret, frame = camara.read();
        
        cv2.imshow('Capturar',frame)
        #Esperar hasta precionar una tecla
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
        
    cv2.imwrite('output\placa.png',frame)   
    
    camara.release()
    cv2.destroyAllWindows()     
    return frame

def process_image(imagen):
    
    #path_pytesseract = r'C:\Users\ameth.galarcio\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    #pytesseract.pytesseract.tesseract_cmd = path_pytesseract
    #image_path = r'output\placa.png'
    
    # Lee la imagen de la placa.
    #image = cv2.imread(image_path)
    # Convierte la imagen a escala de grises.
    
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    print("Texto extraído: ", text)
    return text

# Función para guardar la información de la placa en un QR code
def qr_creator(text):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    image = qr.make_image(fill_color="black", back_color="white")
    image.save("qrcode.png")
    return



def _init_():
    imagen = capture_image()
    process_image(imagen)
    ##print(text)
    
    
    
_init_()
capture_image()