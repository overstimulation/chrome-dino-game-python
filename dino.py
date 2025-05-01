import pygame


class Dinosaur:
    X_POSITION = 80
    Y_POSITION = 310
    Y_POSITION_WHILE_DUCKING = 340
    JUMP_VELOCITY = 8.5

    def __init__(self, assets):
        # Assign sprites
        self.run_sprite = assets["DINO_RUN_SPRITES"]
        self.duck_sprite = assets["DINO_DUCK_SPRITES"]
        self.jump_sprite = assets["DINO_JUMP_SPRITE"]

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
        self.mask = pygame.mask.from_surface(self.sprite)

    # Draw the dinosaur
    def draw(self, window):
        window.blit(self.sprite, (self.dino_hitbox.x, self.dino_hitbox.y))

    # Update dinosaur state based on input
    def update(self, player_input, assets):
        if self.dino_run:
            self.run()
        if self.dino_duck:
            self.duck()
        if self.dino_jump:
            self.jump()

        # Loop animation step index
        if self.step_index >= 20:
            self.step_index = 0

        # Handle input for jumping, ducking, or running
        if player_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
            if assets["JUMP_SOUND"]:
                assets["JUMP_SOUND"].play()  # Play the jump sound
        elif player_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif not (self.dino_jump or player_input[pygame.K_DOWN]):
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

        # Update mask after sprite changes
        self.mask = pygame.mask.from_surface(self.sprite)

    # Handle running animation and position
    def run(self):
        self.sprite = self.run_sprite[self.step_index // 10]
        self.dino_hitbox = self.sprite.get_rect()
        self.dino_hitbox.x = self.X_POSITION
        self.dino_hitbox.y = self.Y_POSITION
        self.step_index += 1

    # Handle ducking animation and position
    def duck(self):
        self.sprite = self.duck_sprite[self.step_index // 10]
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
