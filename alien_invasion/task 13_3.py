import pygame

import sys

from pygame.sprite import Group

from pygame.sprite import Sprite

class Settings():
	
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		
		self.kapl_drop_speed = 1

class Kapl(Sprite):
	def __init__(self, ai_settings, screen):
		super(Kapl, self).__init__()
		
		self.ai_settings = ai_settings
		self.screen = screen
		
		self.image = pygame.image.load('images/kapl.bmp')
		self.rect = self.image.get_rect()
		
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		self.x = float(self.rect.x)
		
				
	def blitme(self):
		self.screen.blit(self.image, self.rect)	
		
	

def get_number_kapls_x(ai_settings, kapl_width):
	available_space_x = ai_settings.screen_width - 2 * kapl_width
	number_kapls_x = int(available_space_x/(2*kapl_width))
	
	return number_kapls_x			
	
def create_kapl(ai_settings, screen, kapls, kapl_number, row_number):
	kapl = Kapl(ai_settings, screen)
	kapl_width = kapl.rect.width
	kapl.x = kapl_width + 2*kapl_width *kapl_number
	kapl.rect.x = kapl.x
	kapl.rect.y = kapl.rect.height + 2*kapl.rect.height * row_number
	kapls.add(kapl)		
	
def create_fleet(ai_settings, screen, kapls):
	kapl = Kapl(ai_settings, screen)
	number_kapls_x = get_number_kapls_x(ai_settings, kapl.rect.width)
	
	for row_number in range(0,2):
		for kapl_number in range(number_kapls_x):
			create_kapl(ai_settings, screen, kapls, kapl_number, 
							row_number)	
	

def update(ai_settings, screen, kapls):
	
	
	for kapl in kapls.sprites():
		kapl.rect.y += ai_settings.kapl_drop_speed
		
		
	for kapl in kapls.copy():
			if kapl.rect.bottom >= ai_settings.screen_height :
				kapls.remove()
				
	
	

def update_screen(ai_settings, screen, kapls):
	screen.fill((0,0,0))
	kapls.draw(screen)
	pygame.display.flip()		


def run():
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption("Govnokod")
	
	ai_settings = Settings()
	kapls = Group()
	
	create_fleet(ai_settings, screen, kapls)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
		update(ai_settings, screen, kapls)		
		update_screen(ai_settings, screen, kapls)		

run()

