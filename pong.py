import pygame
import _thread, time

class Bola:
	#Constructor
	def __init__(self, surface, color, center, radius):
		self.surface = surface
		self.color = color
		self.center_x, self.center_y = center
		self.radius = radius 
		self.rect = pygame.draw.circle(surface, color, (self.center_x, self.center_y), radius)

		self.vel_x = 0
		self.vel_y = 0
		self.max_speed = 6
	#Función para mover la bola
	def mover(self):
		if self.vel_x > self.max_speed:
			self.vel_x = self.max_speed
		if self.vel_y > self.max_speed:
			self.vel_y = self.max_speed

		self.center_x += self.vel_x
		self.center_y += self.vel_y
		self.rect = pygame.draw.circle(self.surface, self.color, (self.center_x, self.center_y), self.radius)

class Barra:
	#Constructor
	def __init__(self, surface, color, rect):
		self.surface = surface
		self.color = color
		self.rect = rect
		pygame.draw.rect(self.surface, self.color, rect)

		self.speed = 4
		self.vel = 0
	#Funciones de movimiento de la barra
	def mover_arriba(self):
		self.vel = -self.speed
	
	def mover_abajo(self):
		self.vel = self.speed
	
	def parar(self):
		self.vel = 0
	
	def mover(self):
		self.rect.y += self.vel
		if (self.surface.get_rect().contains(self.rect)):
			pygame.draw.rect(self.surface, self.color, self.rect)
		else:
			self.rect.y -= self.vel			
			pygame.draw.rect(self.surface, self.color, self.rect)

class IA:
	#Constructor
	def __init__(self, barra, bola):
		self.barra = barra
		self.bola = bola

		_thread.start_new_thread(self.play,())
	#Inteligencia artificial
	def play(self):
		sens = 20
		while True:
			#se centra en el medio
			barra_pos = self.barra.rect.centery
			bola_pos = self.bola.center_y
			#la posición cambia según la pelota
			pos = barra_pos-bola_pos

			if pos - sens < 0:

				self.barra.mover_abajo()
			elif pos + sens > 0:

				self.barra.mover_arriba()
			else:

				self.barra.parar()
			time.sleep(0.01)
