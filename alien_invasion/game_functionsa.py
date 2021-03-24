import sys

import pygame
from pygame.sprite import Group
from bulleta import Bullet
from pygame.sprite import Sprite


def update_bullets(bullets, i = []):
	bullets.update()	
	if not i:
		i.append(0)
		
	
	
	
	for bullet in bullets.copy():
			if bullet.rect.left >= 1200:
				i[0] = i[0]+1
				if i[0]>= 3:
					sys.exit()
				bullets.remove(bullet)	
				
			
def training(ai_settings, screen, bullets, block, bullet):

	if pygame.sprite.spritecollideany(block, bullets):
		ai_settings.increase_speed()
		bullets.remove(bullet)
			
	

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	if event.key == pygame.K_DOWN:
		ship.moving_right = True
	elif event.key == pygame.K_UP:
		ship.moving_left = True	
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
	if len(bullets) < ai_settings.bullet_allowed:
			new_bullet = Bullet(ai_settings,screen,ship)
			bullets.add(new_bullet)	
			
def check_keyup_events(event,ship):
	if event.key == pygame.K_DOWN:
		ship.moving_right = False	
	elif event.key == pygame.K_UP:
		ship.moving_left = False	
		
def check_play_button(ai_settings, screen, stats, play_button, ship, 
						 bullets, mouse_x, mouse_y):
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)						
							
	if button_clicked and not stats.game_active:
		start_game(ai_settings, screen, stats, ship, bullets)
			
			
def start_game(ai_settings, screen, stats, ship, bullets):
		ai_settings.initialize_dynamic_settings()
		pygame.mouse.set_visible(False)
		stats.game_active = True	
		
		bullets.empty()
		
		ship.center_ship()						
		

def check_events(ai_settings, screen, stats, play_button,
				ship, bullets):
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event, ai_settings, screen, ship,bullets)
			elif event.type == pygame.KEYUP:
				check_keyup_events(event,ship)	
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				check_play_button(ai_settings, screen, stats, play_button,
									ship,
									bullets, mouse_x, mouse_y)	

			
def update_screen(ai_settings,screen,ship, stats, 
					bullets, block, play_button):
	screen.fill(ai_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	block.draw_block()	
	ship.blitme()
	if not stats.game_active:
		play_button.draw_button()
	pygame.display.flip()				

