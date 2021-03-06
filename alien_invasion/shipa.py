import pygame

class Ship():
	def __init__(self,ai_settings, screen):
		self.screen = screen
		self.ai_settings = ai_settings
		
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		#Каждый корабль появляется в нижнем краю экрана
		self.rect.bottom = self.screen_rect.centery
		
		self.center = float(self.rect.centery)
		
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		if self.moving_right and self.rect.bottom < self.screen_rect.bottom:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.top > 0:
			self.center -= self.ai_settings.ship_speed_factor
		self.rect.centery = self.center
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)	

	def center_ship(self):
		self.center = self.screen_rect.centery
