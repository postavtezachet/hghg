class Settings():
	
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
	
		#Пули
	
		self.bullet_width = 15
		self.bullet_height = 3
		self.bullet_color = (60,60,60)
		self.bullet_allowed = 3
	
		
		self.block_width = 100
		self.block_height = 200
		self.block_color = (60,60,60)
		
		self.speedup_scale = 1.5
		
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		self.bullet_speed_factor = 2
		self.ship_speed_factor = 1
		self.block_speed_factor = 1
			
	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.block_speed_factor *= 	self.speedup_scale	
		
