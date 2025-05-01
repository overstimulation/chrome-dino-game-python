import pygame

from assets import load_assets
from game import main
from settings import HEIGHT, WIDTH, init_font
from ui import menu

# Initialise Pygame mixer and Pygame itself
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()
init_font()

ASSETS = load_assets()

# --- Pygame Window Setup ---
GAME_WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the game window
pygame.display.set_caption("Dino Game by @overstimulation on GitHub")  # Set window title


# Run the game if this file is executed directly
if __name__ == "__main__":
    death_count = 0
    score = 0
    while True:
        menu(GAME_WINDOW, death_count=death_count, score=score, assets=ASSETS)
        score, death_count = main(GAME_WINDOW, assets=ASSETS)
