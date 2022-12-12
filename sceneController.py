from pantallas import *
from utils import ANCHO, ALTO

class Controller:
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption('PONG')
        self.tasa_refresco = pg.time.Clock()
        '''''
        self.menu = Menu(self.pantalla_principal, self.tasa_refresco)
        self.partida = Partida(self.pantalla_principal, self.tasa_refresco)
        self.resultado = Resultado(self.pantalla_principal, self.tasa_refresco)
        self.records = Records(self.pantalla_principal, self.tasa_refresco)
        self.valor_resultado = ''
        '''
        self.pantallas = [ Menu(self.pantalla_principal,self.tasa_refresco),Partida(self.pantalla_principal,self.tasa_refresco),Resultado(self.pantalla_principal,self.tasa_refresco),Records(self.pantalla_principal,self.tasa_refresco) ]
        
        self.valor_resultado = ""
        
        
    def start(self):
        seguir = True    

        indice = 0
        while seguir:
           if indice == 1: 
                cerrar = self.valor_resultado = self.pantallas[indice].bucle_pantalla()
               
                if cerrar == True:
                    break
                indice +=1

           elif indice == 2:
                self.pantallas[indice].recibir_resultado(self.valor_resultado)
                cerrar = self.pantallas[indice].bucle_pantalla()
                if cerrar == True:
                    break
               
                indice = 0 
                
           elif indice == 0:
                cerrar = self.pantallas[indice].bucle_pantalla()
               
                if cerrar == 'records':
                    self.pantallas[3].bucle_pantalla()
                if cerrar == True:
                    break
                
                indice +=1
        
    
       
        
        