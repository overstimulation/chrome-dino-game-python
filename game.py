import random

import pygame

from cloud import Cloud
from dino import Dinosaur
from obstacles import Bird, LargeCactus, SmallCactus
from settings import BACKGROUND_COLOUR, FPS
from ui import count_score, draw_background


# --- Main Game Loop ---
def main(window, assets):
    clock = pygame.time.Clock()  # Game clock
    game_running = True  # Main loop flag
    game_speed = 14  # Initial game speed
    score = 0  # Initial score
    death_count = 0  # Initial death count

    x_position_background = 0  # Background X position
    y_position_background = 380  # Background Y position

    obstacles = []  # List to hold obstacles
    player = Dinosaur(assets)  # Create the dinosaur
    cloud = Cloud(assets)  # Create the cloud

    # Main loop
    while game_running:
        clock.tick(FPS)  # Maintain FPS
        window.fill(BACKGROUND_COLOUR)  # Fill background

        x_position_background = draw_background(
            window, x_position_background, y_position_background, game_speed, assets
        )  # Draw background

        # Handle window close event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        player_input = pygame.key.get_pressed()  # Get keyboard input
        player.draw(window)  # Draw dinosaur
        player.update(player_input, assets)  # Update dinosaur state

        # Spawn obstacles if none exist
        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(assets))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(assets))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(assets))

        # Draw and update all obstacles
        for obstacle in obstacles:
            obstacle.draw(window)
            obstacle.update(game_speed, obstacles)
            # Pixel-perfect collision check using masks
            offset = (obstacle.rect.x - player.dino_hitbox.x, obstacle.rect.y - player.dino_hitbox.y)
            if player.mask.overlap(obstacle.mask, offset):
                if assets["DEATH_SOUND"]:
                    assets["DEATH_SOUND"].play()  # Play the death sound
                pygame.time.delay(500)  # Pause briefly
                death_count += 1  # Increment deaths
                game_running = False
                break

        cloud.draw(window)  # Draw cloud
        cloud.update(game_speed)  # Update cloud position

        score, game_speed = count_score(window, score, game_speed, assets)  # Update and display score

        pygame.display.update()  # Refresh display

    return score, death_count  # Return score and death_count to main.py


pygame.quit()  # Quit Pygame
