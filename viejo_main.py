from figura_class import Pelota,Raqueta
import pygame as pg

pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("Pong")


#definir la tasa de refresco de nuestro bucle de fotogramas fps
cronometro = pg.time.Clock()

pelota = Pelota(400,300)
raqueta1 = Raqueta(10,300)
raqueta2 = Raqueta(790,300)

#asignar velocidad
raqueta1.vy=6
raqueta2.vy=6
pelota.vx=2



game_over = False

while not game_over:
    #print('gol raqueta 1:', pelota.contadorIzquierda)
    #print('gol raqueta 2:', pelota.contadorDerecha)
    
    velocidad_tiempo = cronometro.tick(240)
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
    
    raqueta1.mover(pg.K_w, pg.K_s)
    raqueta2.mover(pg.K_UP, pg.K_DOWN)
    pelota.mover()
     

    pantalla_principal.fill((0,128,94))
    
    pelota.comprobar_choqueV2(raqueta2,raqueta1)
    
    pelota.marcador(pantalla_principal)
    
    pg.draw.line(pantalla_principal, (255,255,255), (400,0), (400,600), width=2)

    
    pelota.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)
    
    pg.display.flip()
    
pg.quit()