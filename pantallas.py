import pygame as pg
from figura_class import Pelota, Raqueta

ANCHO = 800
ALTO = 600


BLANCO=(255,255,255)
AMARILLO=(255,255,0)
ROJO = (255,0,0)
NARANJA=(255, 128, 0)
VERDE=(0,128,94)
GRANATE=(192, 57, 43)

FPS = 280
PRIMER_AVISO = 10000
SEGUNDO_AVISO = 5000


class Partida:
    def __init__(self):
        pg.init()
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption('PONG')
        self.tasa_refresco = pg.time.Clock()
        
        self.pelota = Pelota(ANCHO//2,ALTO//2,vx=2,vy=2)
        self.raqueta1 = Raqueta(10, ALTO//2,vy=5)
        self.raqueta2 = Raqueta(ANCHO-10,ALTO//2,vy=5)
        self.marcador1 = 0
        self.marcador2 = 0
        self.font = pg.font.Font("fonts/pressStart2P.ttf", 15)
        self.fuenteTemp = pg.font.Font("fonts/pressStart2P.ttf",30)
        self.quienMarco = ""
        self.temporizador = 15000 #en milisegundos
        self.colorFondo = VERDE  
        self.contadorFotograma=0
        
    def bucle_pantalla(self):
        game_over = False

        while not game_over and (self.marcador1<10 or self.marcador2<10) and self.temporizador > 0:
            salto_tiempo = self.tasa_refresco.tick(FPS)#1000/280 = cantidad de fotograma por segundo pero en milisegundos
            self.temporizador -= salto_tiempo
            
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True
    
            self.raqueta1.mover(pg.K_w, pg.K_s)
            self.raqueta2.mover(pg.K_UP, pg.K_DOWN)
            self.quienMarco = self.pelota.mover()
     

            self.pantalla_principal.fill(self.fijar_fondo())
            self.pelota.comprobar_choqueV2(self.raqueta2,self.raqueta1)
            
            self.marcador()
            self.linea_disc()
          
            tiempo = self.font.render( str( int(self.temporizador/1000) ),0, ROJO)
            self.pantalla_principal.blit(tiempo, (400, 20 ))
            
            
            
            #pg.draw.line(pantalla_principal, (255,255,255), (400,0), (400,600), width=2)
            
            


            self.pelota.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)
            self.mostrar_jugador()
    
            pg.display.flip()
            
        pg.quit()
        
   
    def linea_disc(self):
        cont_linea1=0
        cont_linea2=50

        while cont_linea1 <= 560 and cont_linea2 <= 630:
            pg.draw.line(self.pantalla_principal, BLANCO, (400,cont_linea1), (400,cont_linea2), width=10)
            cont_linea1 += 70
            cont_linea2 += 70

    def mostrar_jugador(self):
        jugador1 = self.font.render("Jugador 1",0, AMARILLO)
        jugador2 = self.font.render( "Jugador 2",0, AMARILLO)
        self.pantalla_principal.blit(jugador1, (155, 30))
        self.pantalla_principal.blit(jugador2, (555, 30 ))

    def marcador(self):
        if self.quienMarco == "right":
            self.marcador1 += 1
        elif self.quienMarco == "left":
            self.marcador2 += 1  
        marcadorIzquierda = self.font.render(str( self.marcador2),0, AMARILLO)
        marcadorDerecha = self.font.render( str(self.marcador1),0, AMARILLO)
        self.pantalla_principal.blit(marcadorDerecha, (200, 50))
        self.pantalla_principal.blit(marcadorIzquierda, (600, 50 ))

    def fijar_fondo(self):
        self.contadorFotograma +=1

        if self.temporizador > PRIMER_AVISO:#no entra en ninguna condicion aun
          
            self.contadorFotograma=0

        elif self.temporizador > SEGUNDO_AVISO:#entra en la condicion que parpadee en naranja, 10 SEGUNDOS

            if self.contadorFotograma == 30:
                if self.colorFondo == VERDE:
                    self.colorFondo = NARANJA
                else:
                    self.colorFondo = VERDE
                self.contadorFotograma = 0
            
        else:# entra en la condicion que parpadee en rojo, 5 SEGUNDOS
            if self.contadorFotograma == 30:
                if self.colorFondo == VERDE:
                    self.colorFondo = ROJO
                else:
                    self.colorFondo = VERDE
                self.contadorFotograma = 0

        return self.colorFondo


class Menu:
    def __init__(self):
        pg.init()
        self.pantalla_principal = pg.display.set_mode( (ANCHO,ALTO) )
        pg.display.set_caption("Menu")
        self.tasa_refresco = pg.time.Clock()

        self.imagenFondo = pg.image.load("images/portada.jpg")
        self.fuenteMenu = pg.font.Font("fonts/pressStart2P.ttf", 20)

    def bucle_pantalla(self):
        game_over = False

        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True

            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_RETURN:
                    game_over = True
                    return "jugar"          

            self.pantalla_principal.blit(self.imagenFondo,(0,0))
            menu = self.fuenteMenu.render("Pulsa ENTER para jugar",0,GRANATE)
            self.pantalla_principal.blit(menu, (155,ALTO//2) )
            pg.display.flip()