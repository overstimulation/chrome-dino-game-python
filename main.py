import os
import random

import pygame

# Initialise Pygame mixer and Pygame itself
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

# --- Game Constants ---
WIDTH = 1100  # Window width
HEIGHT = 600  # Window height
FPS = 30  # Frames per second

BACKGROUND_COLOUR = (255, 255, 255)  # The white colour

# --- Font Setup ---
FONT_SIZE = 30
FONT_COLOUR = (0, 0, 0)
try:
    FONT = pygame.font.SysFont(["Courier New", "Consolas", "Lucida Console", "monospace"], FONT_SIZE, bold=True)
except pygame.error:
    FONT = pygame.font.SysFont(None, FONT_SIZE, bold=True)

# --- Game Assets ---


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

# --- Pygame Window Setup ---
GAME_WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the game window
pygame.display.set_caption("Dino Game by @overstimulation on GitHub")  # Set window title


# --- Dinosaur Class ---
class Dinosaur:
    X_POSITION = 80
    Y_POSITION = 310
    Y_POSITION_WHILE_DUCKING = 340
    JUMP_VELOCITY = 8.5

    def __init__(self):
        # Assign sprites
        self.run_sprite = DINO_RUN_SPRITES
        self.duck_sprite = DINO_DUCK_SPRITES
        self.jump_sprite = DINO_JUMP_SPRITE

        # State flags
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False

        # Sprite and hitbox setup
        self.sprite = self.run_sprite[0]
        self.dino_hitbox = self.sprite.get_rect()
        self.dino_hitbox.x = self.X_POSITION
        self.dino_hitbox.y = self.Y_POSITION
        self.step_index = 0
        self.jump_velocity = self.JUMP_VELOCITY

    # Draw the dinosaur
    def draw(self, window):
        window.blit(self.sprite, (self.dino_hitbox.x, self.dino_hitbox.y))

    # Update dinosaur state based on input
    def update(self, player_input):
        if self.dino_run:
            self.run()
        if self.dino_duck:
            self.duck()
        if self.dino_jump:
            self.jump()

        # Loop animation step index
        if self.step_index >= 10:
            self.step_index = 0

        # Handle input for jumping, ducking, or running
        if player_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
        elif player_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif not (self.dino_jump or player_input[pygame.K_DOWN]):
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

    # Handle running animation and position
    def run(self):
        self.sprite = self.run_sprite[self.step_index // 5]
        self.dino_hitbox = self.sprite.get_rect()
        self.dino_hitbox.x = self.X_POSITION
        self.dino_hitbox.y = self.Y_POSITION
        self.step_index += 1

    # Handle ducking animation and position
    def duck(self):
        self.sprite = self.duck_sprite[self.step_index // 5]
        self.dino_hitbox = self.sprite.get_rect()
        self.dino_hitbox.x = self.X_POSITION
        self.dino_hitbox.y = self.Y_POSITION_WHILE_DUCKING
        self.step_index += 1

    # Handle jumping animation and movement
    def jump(self):
        self.sprite = self.jump_sprite
        if self.dino_jump:
            self.dino_hitbox.y -= self.jump_velocity * 4  # Move upwards by current velocity
            self.jump_velocity -= 0.8  # Apply gravity (reduce velocity)
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.dino_jump = False  # Stop jumping when peak is reached
            self.jump_velocity = self.JUMP_VELOCITY  # Reset velocity for next jump


# --- Cloud Class ---
class Cloud:
    def __init__(self):
        self.x_position = WIDTH + random.randint(800, 1000)  # Start off-screen to the right
        self.y_position = random.randint(50, 100)  # Random vertical position
        self.sprite = CLOUD_SPRITE
        self.width = self.sprite.get_width()

    # Update cloud position
    def update(self):
        self.x_position -= game_speed  # Move cloud to the left
        if self.x_position < -self.width:
            self.x_position = WIDTH + random.randint(2500, 3000)  # Reset to far right
            self.y_position = random.randint(50, 100)  # Randomise height

    # Draw the cloud
    def draw(self, window):
        window.blit(self.sprite, (self.x_position, self.y_position))


# Draw the moving ground background
def draw_background(window):
    global x_position_background, y_position_background
    background_width = TRACK_SPRITE.get_width()
    window.blit(TRACK_SPRITE, (x_position_background, y_position_background))
    window.blit(TRACK_SPRITE, (background_width + x_position_background, y_position_background))
    if x_position_background <= -background_width:
        window.blit(TRACK_SPRITE, (background_width + x_position_background, y_position_background))
        x_position_background = 0
    x_position_background -= game_speed


# Count and display the score
def count_score(window):
    global score, game_speed

    score += 1  # Increase score

    if score % 100 == 0:
        game_speed += 1  # Increase speed every 100 points

    score_str = f"{score:06d}"
    text = FONT.render(f"Score: {score_str}", True, FONT_COLOUR)
    text_rect = text.get_rect()
    text_rect.topright = (WIDTH - 40, 40)
    window.blit(text, text_rect)


# --- Main Game Loop ---
def main(window):
    global game_speed, x_position_background, y_position_background, score

    clock = pygame.time.Clock()  # Game clock
    game_running = True  # Main loop flag
    game_speed = 14  # Initial game speed
    score = 0  # Initial score

    x_position_background = 0  # Background X position
    y_position_background = 380  # Background Y position

    player = Dinosaur()  # Create the dinosaur
    cloud = Cloud()  # Create the cloud

    # Main loop
    while game_running:
        clock.tick(FPS)  # Maintain FPS
        window.fill(BACKGROUND_COLOUR)  # Fill background

        # Handle window close event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        player_input = pygame.key.get_pressed()  # Get keyboard input
        player.draw(window)  # Draw dinosaur
        player.update(player_input)  # Update dinosaur state

        draw_background(window)  # Draw ground

        cloud.draw(window)  # Draw cloud
        cloud.update()  # Update cloud position

        count_score(window)  # Update and display score

        pygame.display.update()  # Refresh display

    pygame.quit()  # Quit Pygame


# Run the game if this file is executed directly
if __name__ == "__main__":
    main(GAME_WINDOW)
