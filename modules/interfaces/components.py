
#Librerias UI
import flet
from flet import *

    
    
##Card View    
class CardCount(UserControl):
    
    def __init__(self):
        super().__init__()

    def CardDecoration(self, colors :list[str],title: str,value:str,image:str):
        return Container(
            
            width=230,
            height=120,
            border_radius=10,
            alignment=alignment.center,
            gradient=LinearGradient(
                begin=alignment.top_left,
                end=alignment.bottom_right,                
                colors=colors,                              
            ), 
            content=Stack(
                expand=True,                
                #alignment= MainAxisAlignment.SPACE_BETWEEN,
                #alignment=CrossAxisAlignment.CENTER,      
                width=230,                
                controls=[                    
                    
                    Container(                        
                        content=Text(
                                value=title,
                                color='#FFFFFF',
                                size=12,
                                font_family="Nunito",                                                                                            
                            ),
                            top=30,
                            left=15,
                        ),
                    
                    Container(                        
                        content=Text(
                                value=value,
                                color='#FFFFFF',
                                size=30,
                                font_family="Nunito",                                                                                            
                                weight=FontWeight.W_500,
                            ),
                        top=45,
                        left=15,
                    ),
                    
                                              
                    Container(       
                                                                       
                        content=Image(
                            width=100,
                            height=120,
                            fit=ImageFit.CONTAIN,
                            repeat=ImageRepeat.NO_REPEAT,
                            src=image,
                            
                        ),
                        bottom=0,
                        right=-10,
                        
                    ),                             
                ]
                
            ),
        )
        

    def build(self):
        
        
        return Container(
            margin=30,
            height=320,
            content=Column(
                controls=[
                    Row(
                        controls=[
                            Container(
                                width=40,
                                height=40,
                                border_radius=10,
                                alignment=alignment.center,
                                bgcolor='#517b63',
                                content=Icon(
                                    color='#FFFFFF',
                                    name=icons.DASHBOARD_ROUNDED,
                                )
                            ),
                            Text(
                                value='Dasboard',
                                color='#272324',
                                size=15,
                                font_family="Poppins",
                                
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            Column(
                                controls=[
                            
                                    self.CardDecoration(
                                        colors=[
                                            
                                            '#199A8E',
                                            '#1BAF8A',
                                            
                                        ],
                                        title='Total del dia',
                                        value='123',
                                        image=f'/dashboard/camera.png',
                                        
                                    ),                    
                                    self.CardDecoration(
                                        colors=[
                                            '#FF7F50',  # Naranja coral
                                            '#FF6347'   # Naranja rojizo
                                            
                                        ],
                                        
                                        title='Sitios disponibles',
                                        value='512',
                                        image=f'/dashboard/building.png',
                                        
                                    ),                    
                                ],                                
                            ),
                            Column(
                                controls=[
                            
                                    self.CardDecoration(
                                      colors = [
                                            '#8A1BAF',
                                            '#8E199A'
                                        ],

                                        title='Total de la semana',
                                        value='45',
                                          image=f'/dashboard/car.png',
                                        
                                    ),                    
                                    self.CardDecoration(
                                        colors=[
                                            '#9599E2',
                                            '#8BC6EC',
                                            
                                        ],
                                        title='Dinero recogido',
                                        value='$ '+'124.0',
                                          image=f'/dashboard/money.png',
                                        
                                    ),                    
                                ],                                                    
                            ),                            
                        ]        
                    )  
                ]
            ),
            
        )
        


    


        
    
