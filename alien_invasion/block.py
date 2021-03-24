import pygame

class Block():
	def __init__(self,ai_settings,screen):
		
		self.screen = screen
		
		self.rect = pygame.Rect(0,0,ai_settings.block_width,
									ai_settings.block_height)
		self.screen_rect = screen.get_rect()							
		self.rect.centerx = self.screen_rect.right - 50
		
		
		self.y= float(self.rect.y)
		
		
		self.color = ai_settings.block_color
		self.speed_factor = ai_settings.block_speed_factor
		
									
	def update(self, ai_settings):
		if self.rect.bottom >= self.screen_rect.bottom:
			ai_settings.block_speed_factor *= -1
		if self.rect.top < 0:			
			ai_settings.block_speed_factor *= -1
				
			
		self.y += ai_settings.block_speed_factor
		self.rect.y = self.y	
		
	def draw_block(self):
		pygame.draw.rect(self.screen, self.color, self.rect)									


