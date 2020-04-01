import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
	"""Overall class managing game behaviour and assets"""


	def __init__(self):
		"""initalise thegame and resources"""
		pygame.init()
		self.settings = Settings()
		self._update_screen()
		
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()

	def run_game(self):
		"""start games main loop"""
		while True:
			"""watch for keyboard and mouse events"""
			self._check_events()
			self.ship.update()
			self.bullets.update()
			self._update_screen()

			#make the most recent draw screen visable
			pygame.display.flip()

	def _check_events(self):
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					self._check_keydown_events(event)
				elif event.type == pygame.KEYUP:
					self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""responses to keypresses"""
		if event.key == pygame.K_RIGHT:
			#move ship to the right
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			#move ship to the left
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):
		"""create a new bullet and add to bullets group"""
		new_bullet = Bullet(self)
		self.bullets.add(new_bullet)

	def _update_screen(self):
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		#redraw the screen each pass of the loop
		self.screen.fill(self.settings.bg_colour)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

if __name__ == '__main__':
	#make game instance and the game run
	ai = AlienInvasion()
	ai.run_game()
