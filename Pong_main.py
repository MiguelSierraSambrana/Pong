import os, pygame, sys, time, random
from pygame.locals import *
from interfaz_pong import Ui_VentanaPrincipal
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
#Import para la clase del teclado
from teclado import Keyboard
#Import para la clase del juego
from pong import *
#import para base de datos
import sqlite3
#import para sacar la lista de puntuaciones a una ventana
from tkinter import *

#Directorio de trabajo (necesario para cosas como el sonido)
directorio_principal = os.path.dirname(os.path.realpath(sys.argv[0]))

class Ventana(QMainWindow, Ui_VentanaPrincipal):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.conexionSenalesRanuras()
        
    def conexionSenalesRanuras(self):
        
        self.infoButton.clicked.connect(self.acercaDe)
        self.startButton.clicked.connect(self.game)
        self.exitButton.clicked.connect(self.exit)
        self.scoreButton.clicked.connect(self.mostrar_puntuaciones)
        
    def mostrar_puntuaciones(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #hago esto porque si no me saca la BD a /home/user en vez del directorio del juego
        db_path = os.path.join(BASE_DIR, "scores.db")
        with sqlite3.connect(db_path) as db:
            cur = db.cursor()
            cur.execute("SELECT * FROM SCORE")
            datos = cur.fetchall()
            #me volví loco pero no conseguí pasar la información creando un QTableWidget 
            #así que decidí utlizar las librerias tkinter, queda menos cutre que un print(datos)
            os.chdir(directorio_principal)
            puntua = Tk()
            puntua.title("Puntuaciones")
            canvas = Canvas(width = 300, height = 200, bg = 'black')
            canvas.pack(expand = YES, fill = BOTH)
            gif1 = PhotoImage(file = './ui/images/puntua.gif')
            canvas.create_image(50, 10, image = gif1, anchor = NW)

            for item in datos:
                 w = Label(puntua, text=item)
                 w.pack()
            puntua.mainloop()
            
    def acercaDe(self):
        mensajeInf= QMessageBox()
        mensajeInf.setText("<p>Pong 0.1alfa construido con:</p><p>- PyQt</p><p>- Qt Designer</p><p>- Python</p><p>Para jugar utiliza las teclas AWSD</p><p>Tienes 5 vidas.. suerte!!</p>")
        mensajeInf.setWindowTitle("PONG 0.1alpha")
        mensajeInf.exec_()
    
    def game(self):
        #copio el contenido del QtextEdit a una variable para mostrar el nombre en el juego
        jugador = self.editNombre.toPlainText()

        #inicializo la base de datos
        BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #hago esto porque si no me saca la BD a /home/user en vez del directorio del juego
        db_path = os.path.join(BASE_DIR, "scores.db")
        with sqlite3.connect(db_path) as db:
            cur = db.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS SCORE(Jugador TEXT, Puntuacion INT)")
            db.commit()
        
            
        #Inicializa el sonido y el juego
        pygame.mixer.pre_init(44100,-16,1, 1024) 
        pygame.init()

        #Incializa el teclado
        teclado = Keyboard(pygame.event)

        #prepara la pantalla
        width = 800
        height = 600
        screen = pygame.display.set_mode((width, height))

        #inicia el juego con velocidad aleatoria para la bola
        def rand_vel_bola(bola):
            rand = int(random.random()*100)
            bola.vel_x = int(bola.max_speed/5 if rand%2 else -bola.max_speed/5)
            bola.vel_y = int(rand%(bola.max_speed) - bola.max_speed/2)

        #pinta el fondo de negro
        screen.fill((0, 0, 0))

        #visualización de las puntuaciones
        score_izquierda = 0
        score_derecha = 0
        vidas_restantes = 5
        font_score = pygame.font.SysFont(pygame.font.get_default_font(), 30, True,False)

        #crea la bola
        bola = Bola(screen, (255, 255, 255), screen.get_rect().center, 8)
        rand_vel_bola(bola)

        #crea la barra izquierda
        barra_izquierda = Barra(screen,(255, 255, 255), Rect(30, height/2-75, 25, 150))

        #controla la barra izquierda
        teclado.while_key_pressed(pygame.K_w, barra_izquierda.mover_arriba)
        teclado.on_key_released(pygame.K_w, barra_izquierda.parar)

        teclado.while_key_pressed(pygame.K_s, barra_izquierda.mover_abajo)
        teclado.on_key_released(pygame.K_s, barra_izquierda.parar)

        #crea la barra derecha
        barra_derecha = Barra(screen,(255, 255, 255), Rect(width-25-30, height/2-75, 25, 150))
    
        ia = IA(barra_derecha, bola)
    
        # sonidos del juego.hay que establecer el directorio operativo del juego para poder reproducir los sonidos
        os.chdir(directorio_principal)
        sonido_rebote= pygame.mixer.Sound("rebote.ogg")
        sonido_punto = pygame.mixer.Sound("punto.ogg")
        
        #al presionar la tecla Q se sale del juego
        teclado.on_key_pressed(pygame.K_q, pygame.quit)

        #loop principal para mantener el programa en ejecución
        while True:
            #borra la pantalla y crea la linea central de la pista
            screen.fill((0, 0, 0))
            pygame.draw.aaline(screen,(160,160,160),(width/2,40), (width/2,height-40))

            #muestra vidas restantes, nombres y puntuación
            score = font_score.render(str(jugador)+" "+str(score_izquierda)+"    -    "+str("Ordenador")+" "+str(score_derecha),True,(0,204,0))
            vida = font_score.render(str(vidas_restantes),True,(204,0,0))

            #posición en la pantalla de la puntuación y vidas restantes
            screen.blit(score, (width/3, 10))
            screen.blit(vida, (0, 10))
        
            if (bola.rect.left <= 0 or bola.rect.right >= width):
                #si uno de los jugadores anota punto reproduce el sonido 
                pygame.mixer.Sound.play(sonido_punto)
                if(bola.rect.left <= 0):
                    score_derecha +=1
                    vidas_restantes -=1
                    if vidas_restantes<=0:
                        #suelto mensaje de final de juego y sale del juego
                        mensaje= QMessageBox()
                        mensaje.setText("GAME  OVER!!")
                        mensaje.setWindowTitle("PONG 0.1alpha")
                        mensaje.exec_()
                        #añado la puntuación del jugador a la BD
                        BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #hago esto porque si no me saca la BD a /home/user en vez del directorio del juego
                        db_path = os.path.join(BASE_DIR, "scores.db")
                        with sqlite3.connect(db_path) as db:
                            cur = db.cursor()
                            cur.execute("INSERT INTO SCORE(Jugador, Puntuacion) VALUES ('{}', {});".format(jugador, score_izquierda))
                            db.commit()
                            pygame.quit()
                        
                else:
                    score_izquierda +=1
                    
                #resetea la posición de las barras
                barra_izquierda.rect.y = height/2-75
                barra_derecha.rect.y = height/2-75

                #resetea la posición de la bola
                bola.center_x,bola.center_y= screen.get_rect().center
                rand_vel_bola(bola)

            #rebote de la pelota en los lados
            if (bola.rect.bottom >= height or bola.rect.top <= 0):
                bola.vel_y *= -1

            #rebote de la pelota en las barras, cuanto mas lejos del centro mas accelera la pelota
            if(bola.rect.colliderect(barra_izquierda.rect)):
                #si la pelota rebota reproduce el sonido
                pygame.mixer.Sound.play(sonido_rebote)
                if bola.vel_x > 0:
                    bola.vel_x = -bola.max_speed
                else: 
                    bola.vel_x = bola.max_speed

                delta = barra_izquierda.rect.centery -  bola.center_y
                diff = delta//(barra_izquierda.rect.height/8)
                bola.vel_y -= int(diff)

            if(bola.rect.colliderect(barra_derecha.rect)):
                #si la pelota rebota reproduce el sonido
                pygame.mixer.Sound.play(sonido_rebote)
                if bola.vel_x > 0:
                    bola.vel_x = -bola.max_speed
                else: 
                    bola.vel_x = bola.max_speed
                delta = barra_derecha.rect.centery -  bola.center_y
                diff = delta//(barra_derecha.rect.height/8)
                bola.vel_y -= int(diff)


            #registrar movimientos
            bola.mover()
            barra_izquierda.mover()
            barra_derecha.mover()
            

            #refesca la pantalla y ralentiza el juego (es necesario o iría demasiado rápido)
            pygame.display.update()
            time.sleep(0.01)


    def exit(self):
        sys.exit(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Ventana()
    gui.show()
    sys.exit(app.exec())



