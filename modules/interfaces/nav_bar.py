import flet
from flet import *


##Navbar
class ModernNavBar(UserControl):
    def __init__(self):
        super().__init__()
    
    
    def UserData(self, initials: str):
        #first row has has user info, diffent from the icon rows, so we create a separate function for it
        return Container(
            content=Row(
                controls=[
                    Container(
                        width=80,
                        height=42,
                        #bgcolor="#c1c1c1",
                        alignment=alignment.center,
                        border_radius=10,
                        content=Text(
                            value=initials,
                            size=20,
                            font_family="Nunito",
                            weight=FontWeight.W_800,
                            color="#507b63",
                        ),   
                    ),
                    
                    
                ]
            )
        )
        
    def container_click(self,e: ContainerTapEvent):
        value = f"local_x: {e.local_x}\nlocal_y: {e.local_y}\nglobal_x: {e.global_x}\nglobal_y: {e.global_y}"
        print(value) 
        self.update()
        

    
        
    def ContainedIcon(self, icon_name: str, text:str):
        return Container(
            width=80,
            height=80,
            on_click=self.container_click,
            ink=True,
            alignment=alignment.center,
            content=Column(
                alignment=alignment.center,
                controls=[
                    Container(
                    width=80,
                    alignment=alignment.center,
                    content=Icon(     
                            name=icon_name,              
                            color="#404331",
                            
                        ),      
                    ),
                    Container(
                        width=80,
                        alignment=alignment.center,
                        content=Text(
                            value=text,
                            color="#404331",
                            size=12,
                            text_align=TextAlign.CENTER, 
                            font_family="Nunito",
                        ),
                    ),
                    
                ]
            )
        )
    
    def build(self):
        return Container(
            #Define las dimenciones y caracteristicas del container             
            width=100,
            height=flet.Page.height,
            padding=padding.all(10),
            animate=animation.Animation(500,"decelerate"),
            bgcolor='#fcfbfa',
            shadow=BoxShadow(
            offset=Offset(1,1),
            blur_radius=10,
            color="#08212121",
            
            spread_radius=1,
            ),
            content=Column(            
                controls=[                    
                    #Logo                          
                    self.UserData('AISP'),
                    #add the SiderBar icons in here....
                    Container(
                        width=80,
                        height=42,
                    ),
                    self.ContainedIcon(
                        text='Dasboard',
                        icon_name=icons.DASHBOARD_ROUNDED,                        
                    ),
                    
                    self.ContainedIcon(
                        text='Registro',
                        icon_name=icons.DATA_USAGE_ROUNDED,                        
                    ),
                    self.ContainedIcon(
                        text='Buscar',
                        icon_name=icons.SEARCH_ROUNDED,                        
                    ),
                ]
            )                         
                                         
        )
        



