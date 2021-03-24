import pygame

import sys


class Dog():
	def __init__(self,screen):
		self.screen = screen
		self.image = pygame.image.load('images\dog.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.centery+170
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)	
	
def run():
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption("Govnokod")
	bg_color = (30,144,255)
	
	a = Dog(screen)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
		screen.fill(bg_color)
		a.blitme()		
		pygame.display.flip()		

run()

