import random

import pygame

from settings import WIDTH


class Obstacle:
    def __init__(self, sprite_list, type_index):
        self.sprite_list = sprite_list
        self.type = type_index
        self.rect = self.sprite_list[self.type].get_rect()
        self.rect.x = WIDTH
        self.mask = pygame.mask.from_surface(self.sprite_list[self.type])

    # Update obstacle position
    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.remove(self)

    # Draw the obstacle
    def draw(self, window):
        window.blit(self.sprite_list[self.type], self.rect)


# Small cactus obstacle
class SmallCactus(Obstacle):
    def __init__(self, assets):
        self.sprite_list = assets["SMALL_CACTUS_SPRITES"]
        self.type = random.randint(0, 2)
        super().__init__(self.sprite_list, self.type)
        self.rect.y = 325


# Large cactus obstacle
class LargeCactus(Obstacle):
    def __init__(self, assets):
        self.sprite_list = assets["LARGE_CACTUS_SPRITES"]
        self.type = random.randint(0, 2)
        super().__init__(self.sprite_list, self.type)
        self.rect.y = 300


# Bird obstacle
class Bird(Obstacle):
    def __init__(self, assets):
        self.sprite_list = assets["BIRD_SPRITES"]
        self.type = 0
        super().__init__(self.sprite_list, self.type)
        self.rect.y = 250
        self.step_index = 0

    # Draw the bird with flapping animation
    def draw(self, window):
        if self.step_index >= 9:
            self.step_index = 0
        window.blit(self.sprite_list[self.step_index // 5], self.rect)
        self.step_index += 1
