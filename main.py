from pantallas import Partida, Menu #importar la clase Partida

menu = Menu()
mensaje = menu.bucle_pantalla()

if mensaje == 'jugar':
    juego = Partida() #creamos objeto de la clase Partida
    juego.bucle_pantalla() #llamamos al bucle de fotograma

print(mensaje)