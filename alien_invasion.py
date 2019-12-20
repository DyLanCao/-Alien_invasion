import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats

def run_game():
    #初始化游戏并创建一个对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    stats = GameStats(ai_settings)

    bg_color = (230,230,230)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    gf.create_fleet(ai_settings, screen,ship, aliens)

    #alien = Alien(ai_settings, screen)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        bullets.update()
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings,stats, screen, ship, aliens,bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
        #screen.fill(ai_settings.bg_color)
        #ship.blitme()

        #pygame.display.flip()

run_game()
