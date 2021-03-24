import pygame

import sys
from pygame.sprite import Group
from random import randint
from pygame.sprite import Sprite

class Settings():
	
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		
		self.kapl_drop_speed = 1


class Dog():
	def __init__(self,screen):
		self.screen = screen
		self.image = pygame.image.load('images\dog1.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		self.m_l=False
		self.m_r=False
		
		
	def update(self):
		if self.m_r and self.rect.right < self.screen_rect.right:
			self.rect.centerx += 2
		if self.m_l and self.rect.left > 0: 
			self.rect.centerx -=2
	
	def blitme(self):
		self.screen.blit(self.image,self.rect)	

class Bit(Sprite):
	def __init__(self, ai_settings, screen):
		super(Bit, self).__init__()
		
		self.ai_settings = ai_settings
		self.screen = screen
		
		self.image = pygame.image.load('images/bit.bmp')
		self.rect = self.image.get_rect()
		
		self.rect.x = randint(0, (ai_settings.screen_width - 
								self.rect.width))
		self.rect.y = self.rect.height
		
		self.x = float(self.rect.x)
		
				
	def blitme(self):
		self.screen.blit(self.image, self.rect)	
		
		
def lov(ai_settings,screen ,bit,a):
	for b in bit.sprites():
		b.rect.y += ai_settings.kapl_drop_speed
		
	if pygame.sprite.spritecollideany(a, bit):
		bit.empty()
		b = Bit(ai_settings, screen)
		bit.add(b)
	
	

		
def check_keydown_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.m_r = True
	elif event.key == pygame.K_LEFT:
		ship.m_l= True	

		
def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.m_r = False	
	elif event.key == pygame.K_LEFT:
		ship.m_l = False
			
		
		

	
def run():
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption("Govnokod")
	bg_color = (30,144,255)
	ai_settings = Settings()
	bit =Group()
	b = Bit(ai_settings, screen)
	bit.add(b)
	a = Dog(screen)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event,a)
			elif event.type == pygame.KEYUP:
				check_keyup_events(event,a)
		for b in bit.sprites():		
			if b.rect.bottom >= ai_settings.screen_height:
				sys.exit()	
		a.update()		
		screen.fill(bg_color)
		lov(ai_settings,screen , bit, a)
		bit.draw(screen)
		a.blitme()		
		pygame.display.flip()		

run()
