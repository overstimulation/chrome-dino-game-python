import os

import pygame


# Load an image, return blank if not found
def load_image(path):
    try:
        return pygame.image.load(path)
    except pygame.error as e:
        print(f"Error loading image: {path} - {e}")
        return pygame.Surface((1, 1))


# Load a sound, return None if not found
def load_sound(path):
    try:
        return pygame.mixer.Sound(path)
    except pygame.error as e:
        print(f"Error loading sound: {path} - {e}")
        return None


def load_assets():
    # Dinosaur running sprites
    DINO_RUN_SPRITES = [
        load_image(os.path.join("assets/dino", "dino_run_1.png")),
        load_image(os.path.join("assets/dino", "dino_run_2.png")),
    ]
    # Dinosaur ducking sprites
    DINO_DUCK_SPRITES = [
        load_image(os.path.join("assets/dino", "dino_duck_1.png")),
        load_image(os.path.join("assets/dino", "dino_duck_2.png")),
    ]
    # Dinosaur jump, start, and dead sprites
    DINO_JUMP_SPRITE = load_image(os.path.join("assets/dino", "dino_jump.png"))
    DINO_START_SPRITE = load_image(os.path.join("assets/dino", "dino_start.png"))
    DINO_DEAD_SPRITE = load_image(os.path.join("assets/dino", "dino_dead.png"))

    # Bird sprites
    BIRD_SPRITES = [
        load_image(os.path.join("assets/bird", "bird_1.png")),
        load_image(os.path.join("assets/bird", "bird_2.png")),
    ]

    # Cactus sprites
    SMALL_CACTUS_SPRITES = [
        load_image(os.path.join("assets/cactus", "small_cactus_1.png")),
        load_image(os.path.join("assets/cactus", "small_cactus_2.png")),
        load_image(os.path.join("assets/cactus", "small_cactus_3.png")),
    ]
    LARGE_CACTUS_SPRITES = [
        load_image(os.path.join("assets/cactus", "large_cactus_1.png")),
        load_image(os.path.join("assets/cactus", "large_cactus_2.png")),
        load_image(os.path.join("assets/cactus", "large_cactus_3.png")),
    ]

    # Miscellaneous sprites
    TRACK_SPRITE = load_image(os.path.join("assets/misc", "track.png"))
    CLOUD_SPRITE = load_image(os.path.join("assets/misc", "cloud.png"))
    GAME_OVER_TEXT_SPRITE = load_image(os.path.join("assets/misc", "game_over.png"))
    RESET_BUTTON_SPRITE = load_image(os.path.join("assets/misc", "reset.png"))

    # Sounds
    JUMP_SOUND = load_sound("assets/sounds/jump.wav")
    SCORE_UP_SOUND = load_sound("assets/sounds/score_up.wav")
    DEATH_SOUND = load_sound("assets/sounds/death.wav")

    return {
        "DINO_RUN_SPRITES": DINO_RUN_SPRITES,
        "DINO_DUCK_SPRITES": DINO_DUCK_SPRITES,
        "DINO_JUMP_SPRITE": DINO_JUMP_SPRITE,
        "DINO_START_SPRITE": DINO_START_SPRITE,
        "DINO_DEAD_SPRITE": DINO_DEAD_SPRITE,
        "BIRD_SPRITES": BIRD_SPRITES,
        "SMALL_CACTUS_SPRITES": SMALL_CACTUS_SPRITES,
        "LARGE_CACTUS_SPRITES": LARGE_CACTUS_SPRITES,
        "TRACK_SPRITE": TRACK_SPRITE,
        "CLOUD_SPRITE": CLOUD_SPRITE,
        "GAME_OVER_TEXT_SPRITE": GAME_OVER_TEXT_SPRITE,
        "RESET_BUTTON_SPRITE": RESET_BUTTON_SPRITE,
        "JUMP_SOUND": JUMP_SOUND,
        "SCORE_UP_SOUND": SCORE_UP_SOUND,
        "DEATH_SOUND": DEATH_SOUND,
    }
