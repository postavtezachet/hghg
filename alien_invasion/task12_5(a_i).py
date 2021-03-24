import pygame
from pygame.sprite import Group

from settingsa import Settings
from shipa import Ship
import game_functionsa as gf
from block import Block
from stats import GameStats
from button import Button

def run_game():
	
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,
										ai_settings.screen_height))
													
	pygame.display.set_caption("Alien invasion")
	bg_color = (ai_settings.bg_color)
	ship = Ship(ai_settings, screen)	
	block = Block(ai_settings, screen)
	bullets = Group()	
	play_button = Button(ai_settings, screen, "Play")
	stats = GameStats(ai_settings)			
	
	
	while True:
		
		gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)
		
		if stats.game_active:
			ship.update()	
			gf.update_bullets(bullets)
			for bullet in bullets.copy():
				gf.training(ai_settings, screen, bullets, block, bullet)
			block.update(ai_settings)
		gf.update_screen(ai_settings,screen,ship, stats, 
					bullets, block, play_button)
		
		
		
run_game()	

