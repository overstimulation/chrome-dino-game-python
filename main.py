import os

import pygame

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

# --- Game Constants ---
WIDTH = 1100
HEIGHT = 600

# --- Game Assets ---
DINO_RUN_SPRITES = [
    pygame.image.load(os.path.join("assets/dino", "dino_run_1.png")),
    pygame.image.load(os.path.join("assets/dino", "dino_run_2.png")),
]
DINO_DUCK_SPRITES = [
    pygame.image.load(os.path.join("assets/dino", "dino_duck_1.png")),
    pygame.image.load(os.path.join("assets/dino", "dino_duck_2.png")),
]
DINO_JUMP_SPRITE = pygame.image.load(os.path.join("assets/dino", "dino_jump.png"))
DINO_START_SPRITE = pygame.image.load(os.path.join("assets/dino", "dino_start.png"))
DINO_DEAD_SPRITE = pygame.image.load(os.path.join("assets/dino", "dino_dead.png"))

BIRD_SPRITES = [
    pygame.image.load(os.path.join("assets/bird", "bird_1.png")),
    pygame.image.load(os.path.join("assets/bird", "bird_2.png")),
]

SMALL_CACTUS_SPRITES = [
    pygame.image.load(os.path.join("assets/cactus", "small_cactus_1.png")),
    pygame.image.load(os.path.join("assets/cactus", "small_cactus_2.png")),
    pygame.image.load(os.path.join("assets/cactus", "small_cactus_3.png")),
]
LARGE_CACTUS_SPRITES = [
    pygame.image.load(os.path.join("assets/cactus", "large_cactus_1.png")),
    pygame.image.load(os.path.join("assets/cactus", "large_cactus_2.png")),
    pygame.image.load(os.path.join("assets/cactus", "large_cactus_3.png")),
]

TRACK_SPRITE = pygame.image.load(os.path.join("assets/misc", "track.png"))
CLOUD_SPRITE = pygame.image.load(os.path.join("assets/misc", "cloud.png"))
GAME_OVER_TEXT_SPRITE = pygame.image.load(os.path.join("assets/misc", "game_over.png"))
RESET_BUTTON_SPRITE = pygame.image.load(os.path.join("assets/misc", "reset.png"))

JUMP_SOUND = pygame.mixer.Sound("assets/sounds/jump.wav")
SCORE_UP_SOUND = pygame.mixer.Sound("assets/sounds/score_up.wav")
DEATH_SOUND = pygame.mixer.Sound("assets/sounds/death.wav")

# --- Pygame Window Setup ---
GAME_WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game by @overstimulation on GitHub")


# --- Main Game Loop ---
def main():
    clock = pygame.time.Clock()
    game_running = True

    # Main loop
    while game_running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

    pygame.quit()


if __name__ == "__main__":
    main()
