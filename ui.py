import pygame

import settings


# Display the menu before starting or after dying
def menu(window, death_count, score, assets):
    WIDTH = settings.WIDTH
    HEIGHT = settings.HEIGHT
    BLACK = settings.BLACK
    BACKGROUND_COLOUR = settings.BACKGROUND_COLOUR
    FONT = settings.FONT

    menu_running = True

    while menu_running:
        window.fill(BACKGROUND_COLOUR)

        if death_count == 0:
            text = FONT.render("Press any key to Start", True, BLACK)
        elif death_count > 0:
            text = FONT.render("Press any key to Restart", True, BLACK)
            score_str = FONT.render("Your Score: " + str(score), True, BLACK)
            score_rect = score_str.get_rect()
            score_rect.center = (WIDTH // 2, HEIGHT // 2 + 50)
            window.blit(score_str, score_rect)

        text_rect = text.get_rect()
        text_rect.center = (WIDTH // 2, HEIGHT // 2)
        window.blit(text, text_rect)
        window.blit(assets["DINO_RUN_SPRITES"][0], (WIDTH // 2 - 20, HEIGHT // 2 - 140))
        pygame.display.update()

        # Listen for quit or key press events to exit or restart game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_running = False
                pygame.quit()  # Quit Pygame
            if event.type == pygame.KEYDOWN:
                menu_running = False


# Draw the moving ground background
def draw_background(window, x_position_background, y_position_background, game_speed, assets):
    background_width = assets["TRACK_SPRITE"].get_width()
    window.blit(assets["TRACK_SPRITE"], (x_position_background, y_position_background))
    window.blit(assets["TRACK_SPRITE"], (background_width + x_position_background, y_position_background))
    if x_position_background <= -background_width:
        x_position_background = 0
    x_position_background -= game_speed
    return x_position_background


# Count and display the score
def count_score(window, score, game_speed, assets):
    WIDTH = settings.WIDTH
    FONT_COLOUR = settings.FONT_COLOUR
    FONT = settings.FONT

    score += 1  # Increase score

    if score % 100 == 0:
        game_speed += 1  # Increase speed every 100 points
        if assets["SCORE_UP_SOUND"]:
            assets["SCORE_UP_SOUND"].play()  # Play the score up sound every 100 points

    score_str = f"{score:06d}"
    text = FONT.render(f"Score: {score_str}", True, FONT_COLOUR)
    text_rect = text.get_rect()
    text_rect.topright = (WIDTH - 40, 40)
    window.blit(text, text_rect)
    return score, game_speed
