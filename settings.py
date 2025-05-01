import pygame

# --- Game Constants ---
WIDTH = 1100  # Window width
HEIGHT = 600  # Window height
FPS = 60  # Frames per second

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BACKGROUND_COLOUR = WHITE

# --- Font Setup ---
FONT_SIZE = 30
FONT_COLOUR = BLACK
FONT = None


def init_font():
    global FONT

    try:
        FONT = pygame.font.SysFont(["Courier New", "Consolas", "Lucida Console", "monospace"], FONT_SIZE, bold=True)
    except pygame.error:
        FONT = pygame.font.SysFont(None, FONT_SIZE, bold=True)
