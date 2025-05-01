import random

from settings import WIDTH


class Cloud:
    def __init__(self, assets):
        self.x_position = WIDTH + random.randint(800, 1000)  # Start off-screen to the right
        self.y_position = random.randint(50, 100)  # Random vertical position
        self.sprite = assets["CLOUD_SPRITE"]
        self.width = self.sprite.get_width()

    # Update cloud position
    def update(self, game_speed):
        self.x_position -= game_speed  # Move cloud to the left
        if self.x_position < -self.width:
            self.x_position = WIDTH + random.randint(2500, 3000)  # Reset to far right
            self.y_position = random.randint(50, 100)  # Randomise height

    # Draw the cloud
    def draw(self, window):
        window.blit(self.sprite, (self.x_position, self.y_position))
