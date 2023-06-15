
import cv2
import base64
#Librerias UI
import flet

from flet import *

camara=cv2.VideoCapture(0)
#Dasboard
class VideoCamera(UserControl):
    
    def __init__(self):
        super().__init__()

    
    
    def did_mount(self):
        self.CameraView()
    
    
    def CameraView(self):
        while True:
            #Lee un frame de la camara
            _, frame = camara.read();
            _, im_arr = cv2.imencode('.png', frame)
            #cv2.imshow('Capturar',frame)
            im_b64 = base64.b64encode(im_arr)
            self.img.src_base64 = im_b64.decode("utf-8")
            self.update()
            #Esperar hasta precionar una tecla
            # if cv2.waitKey(1) & 0xFF ==ord('q'):
            #     break
        
            #cv2.imwrite('..\output\placa.png',frame)   
    
        #camara.release()
        #cv2.destroyAllWindows()     
        #return frame
        
    def canvas_resize(self):
        wd = Page.window_width
        #print(f"Ancho: {int(e.width)}")
        #print(f"Altura: {int(e.height)}")
        pass
        
    
    def build(self):
        
        
        self.img = Image(
            width=600,
            height=300,
            border_radius=border_radius.all(10),
            fit=ImageFit.FIT_WIDTH,
        )
        
        
        
        return Container(            
                
                
                
                content=self.img,
             
            )
        
    