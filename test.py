import keyboard
import cv2
import pytesseract
import flet
from flet import *


class ModernNavBar(UserControl):
    def __init__(self):
        super().__init__()
    
    
    def USerData(self, initials: str):
        #first row has has user info, diffent from the icon rows, so we create a separate function for it
        return Container(
            content=Row(
                controls=[
                    Container(
                        width=42,
                        height=42,
                        bgcolor='#1b1a31',
                        alignment=alignment.center,
                        border_radius=10,
                        content=Text(
                            value=initials,
                            size=20,
                            weight='bold',
                            color="#1df2fe",
                        ),   
                    ),
                    Column(
                        
                        controls=[
                            Text('Silver',
                                 size=15,
                                 color='#212121',
                            ),
                            Text('Parking',),
                        ],
                    ),
                    
                ]
            )
        )
        

    
    def build(self):
        return Container(
            #Define las dimenciones y caracteristicas del container             
            width=200,
            height=flet.Page.height,
            padding=padding.all(10),
            animate=animation.Animation(500,"decelerate"),
            bgcolor='#fdfbf9',
            content=Column(
                controls=[
                    self.USerData('SP')
                    #add the SiderBar icons in here....
                ]
            )
                         
                         
                         
        )






def main(page:Page):
    #Remove title bar and buttons from windows frame
    #page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True
    
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
        bgcolor='#e6e9ea',
        padding=0,
        content=Row(            
            [
              ModernNavBar(),  

              
            ],
            
            expand=True,
        ),
        
        
    )
    
    
    page.add(_main_container)
    page.update()
    pass 



if __name__ == '__main__':
    flet.app(target=main)