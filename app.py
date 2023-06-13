import keyboard
import cv2
import pytesseract
import flet
from flet import *


#Modules
from modules.interfaces.nav_bar import *
from modules.interfaces.dashboard import *




        
        
def main(page:Page):
    
   
    #Remove title bar and buttons from windows frame
    
    page.fonts = {
        "Poppins":"fonts/Poppins/Poppins-Medium.ttf",
    }
    
    #page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True
    page.theme = Theme(font_family="Poppins")
    
    #Contenedor
    _main_container = Container(
        expand=True,
        margin=-10,
        
        # gradient=RadialGradient(
        #     center=Alignment(0,-1.25),
        #     radius =1.4,
        #     colors=[
        #         '#42445f',
        #         '#393b52',
        #         '#33354a',
        #         '#2f3143',
        #         '#292b3c',
        #         '#222331',
        #         '#1a1a25',
        #         '#1a1b26',
        #         '#21222f',
        #         '#1d1e2a',
        #         ],
        # ), 
        bgcolor='#f5f6f7',
        padding=0,
        content=Row(            
            [
            
              ModernNavBar(),  
              Dashboard(),

              
            ],
            
            expand=True,
        ),
        
        
    )
    
    
    page.add(_main_container)
    page.update()
    



if __name__ == '__main__':
    flet.app(
        target=main,
        port=8484,
        view=WEB_BROWSER,
        assets_dir="assets"
        
    )