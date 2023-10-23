#Librerias UI
import flet
from flet import *

from modules.interfaces.camera import VideoCamera
from modules.interfaces.components import CardCount



class Dashboard(UserControl):
    
    def __init__(self):
       super().__init__()
           
    def build(self):
        #Dasboard
                
        return Row(
            controls=[
                
                CardCount(),
                VideoCamera(),
            ]
        )
    
    
       
    