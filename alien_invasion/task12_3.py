import pygame

import sys


class Dog():
	def __init__(self,screen):
		self.screen = screen
		self.image = pygame.image.load('images\dog.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom/2+170
		
		self.m_l=False
		self.m_u=False
		self.m_r=False
		self.m_d=False
		
	def update(self):
		if self.m_r and self.rect.right < self.screen_rect.right:
			self.rect.centerx += 1
		if self.m_l and self.rect.left > 0: 
			self.rect.centerx -=1
		if self.m_u and self.rect.top >0:
			self.rect.bottom -= 1
		if self.m_d and self.rect.bottom < self.screen_rect.bottom:
			self.rect.bottom += 1		
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)	
		
def check_keydown_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.m_r = True
	elif event.key == pygame.K_LEFT:
		ship.m_l= True	
	elif event.key == pygame.K_UP:
		ship.m_u = True
	elif event.key == pygame.K_DOWN:
		ship.m_d = True	
		
		
def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.m_r = False	
	elif event.key == pygame.K_LEFT:
		ship.m_l = False
	elif event.key == pygame.K_UP:
		ship.m_u = False
	elif event.key == pygame.K_DOWN:
		ship.m_d = False	
			
			
		
		
		
	
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
			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event,a)
			elif event.type == pygame.KEYUP:
				check_keyup_events(event,a)
				
		a.update()		
		screen.fill(bg_color)
		a.blitme()		
		pygame.display.flip()		

run()
