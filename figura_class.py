import pygame as pg
from utils import BLANCO

class Pelota:
    def __init__(self,pos_x,pos_y,radio=20,color = BLANCO,vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y =pos_y 
        self.radio = radio
        self.color = color
        self.vx = vx
        self.vy = vy
        self.font = pg.font.Font('fonts/PressStart2P.ttf', 15)
        self.sonido = pg.mixer.Sound('songs/pelota.mp3')
    
    def dibujar(self,pantalla):
        pg.draw.circle(pantalla,self.color,(self.pos_x,self.pos_y),self.radio)
        
    def mover(self, y_max=600, x_max=800):
        self.pos_x += self.vx
        self.pos_y += self.vy
        
        if self.pos_y >= y_max-self.radio or self.pos_y < 0+self.radio:#para que rebote arriba y abajo
            self.vy *= -1
        
        if self.pos_x >= (x_max+self.radio*10):
            self.pos_x = x_max//2
            self.pos_y = y_max//2
            self.vx *= -1
            self.vy *= -1

            return "right" 
            
            
        
        if self.pos_x < (0-self.radio*10):
            self.pos_x = x_max//2
            self.pos_y = y_max//2
            self.vx *= -1
            self.vy *= -1

            return "left"
            
            
    '''''       
    def marcador(self, pantalla_principal):
        marcadorIzquierda = self.font.render( str( self.contadorDerecha),0, (255,255,0))
        marcadorDerecha = self.font.render( str(self.contadorIzquierda),0, (255,255,0))
        jugador1 = self.font.render('Player 1', 0, (255,255,0))
        jugador2 = self.font.render('Player 2', 0, (255,255,0))
        pantalla_principal.blit(jugador1, (150,50))
        pantalla_principal.blit(jugador2, (550,50))
        pantalla_principal.blit(marcadorDerecha, (200, 100))
        pantalla_principal.blit(marcadorIzquierda, (600, 100 ))
    '''    
    @property
    def derecha(self):
        return self.pos_x + self.radio
    @property
    def izquierda(self):
        return self.pos_x - self.radio
    @property
    def arriba(self):
        return self.pos_y - self.radio
    @property
    def abajo(self):
        return self.pos_y + self.radio                

    def comprobar_choque(self,r1,r2):
        if self.derecha  >= r2.izquierda and \
            self.izquierda  <= r2.derecha and \
            self.abajo >= r2.arriba and\
            self.arriba <= r2.abajo:
            self.vx *= -1

        if self.derecha  >= r1.izquierda and \
            self.izquierda  <= r1.derecha and \
            self.abajo >= r1.arriba and\
            self.arriba <= r1.abajo:
            self.vx *= -1

    def comprobar_choqueV2(self,*raquetas):
        
        for r in raquetas:
            if self.derecha  >= r.izquierda and \
               self.izquierda  <= r.derecha and \
               self.abajo >= r.arriba and\
               self.arriba <= r.abajo:
                self.sonido.play()
                self.vx *= -1

                break
          
        
    
        

class Raqueta:
    def __init__(self,pos_x,pos_y,w=20,h=100,color = BLANCO,vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y =pos_y 
        self.w = w
        self.h = h
        self.color = color
        self.vx = vx
        self.vy = vy
        
        self.file_imagenes = {'izqda':['electric00_izqda.png','electric01_izqda.png','electric02_izqda.png'],
                         'drcha':['electric00_drcha.png','electric01_drcha.png','electric02_drcha.png']}
        
        self.imagenes = self.cargar_imagenes() #llamo al metodo que me devuelve la inicializacion de imagenes
        self._direccion = '' #variable para asignar direccion
        self.imagen_activa = 0 #variable para indicar repeticion
        
        #self._imagen = None
        
    def cargar_imagenes(self):
        imagenprueba={}
        for lado in self.file_imagenes:
            imagenprueba[lado]=[]
            for nombre_fichero in self.file_imagenes[lado]:
                fotos = pg.image.load( f"images/raquetas/{ nombre_fichero }" )
                imagenprueba[lado].append(fotos)
        
        return imagenprueba
        
        
        
    @property
    def direccion(self):
        return self._direccion
    
    @direccion.setter
    def direccion(self,valor):
        self._direccion = valor
    
    #@property
    #def imagen(self):
        #return self._imagen
    
    #@imagen.setter
    #def imagen(self, valor):
        #self._imagen = pg.image.load(f'images/raquetas/{self.imagenes[valor]}')
        
    #def cambiar_imagen(self,parametro):
        #self.raqueta = pg.image.load(f'images/raquetas/{self.imagenes[parametro]}')
        
    def dibujar(self,pantalla):
        #pg.draw.rect(pantalla,self.color,(self.pos_x-(self.w//2),self.pos_y-(self.h//2),self.w,self.h))   
        #pantalla.blit(self.imagen,(self.pos_x-(self.w//2),self.pos_y-(self.h//2),self.w,self.h) )
        pantalla.blit(self.imagenes[self.direccion][self.imagen_activa],( self.pos_x-(self.w//2),self.pos_y-(self.h//2) , self.w, self.h ) )
        self.imagen_activa += 1
        if self.imagen_activa >= len(self.imagenes[self.direccion]) :
            self.imagen_activa = 0
    
    def mover(self, tecla_arriba, tecla_abajo, y_max=600, y_min=0):
        estado_teclas = pg.key.get_pressed()

        if estado_teclas[tecla_arriba] == True and self.pos_y > (y_min+self.h//2):
            self.pos_y -= 1
        if estado_teclas[tecla_abajo] == True and self.pos_y < (y_max-self.h//2):
            self.pos_y += 1 
            
    @property
    def arriba(self):
        return self.pos_y - self.h//2

    @property
    def abajo(self):
        return self.pos_y + self.h//2
    
    @property
    def izquierda(self):
        return self.pos_x - self.w//2
    
    @property
    def derecha(self):
        return self.pos_x + self.w//2
      