import pygame

import sys

def run():
	pygame.init()
	screen = pygame.display.set_mode((1200,600))
	pygame.display.set_caption("Govnokod")
	bg_color = (30,144,255)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				print(event.key)	
				
		screen.fill(bg_color)		
		pygame.display.flip()		
run()

