import pygame

import sys

from pygame.sprite import Group

from pygame.sprite import Sprite

class Settings():
	
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800

class Alien(Sprite):
	def __init__(self, ai_settings, screen):
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		self.image = pygame.image.load('images/star.bmp')
		self.rect = self.image.get_rect()
		
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		self.x = float(self.rect.x)
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)	
		
def get_number_rows(ai_settings, alien_height):
	
	number_rows = int(ai_settings.screen_height/ (2*alien_height))
	return number_rows					

def get_number_aliens_x(ai_settings, alien_width):
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x/(2*alien_width))
	
	return number_aliens_x			
	
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2*alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number
	aliens.add(alien)		
	
def create_fleet(ai_settings, screen, aliens):
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings,
									alien.rect.height)
	
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, 
							row_number)	
							
def update_screen(ai_settings, screen, aliens):
	aliens.draw(screen)
	pygame.display.flip()										
	

def run():
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption("Govnokod")
	ai_settings = Settings()
	stars = Group()
	
	create_fleet(ai_settings, screen, stars)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		
				
		update_screen(ai_settings, screen, stars)	

run()

