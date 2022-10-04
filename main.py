import pygame
from sys import exit


def display_score():
    current_time = int((pygame.time.get_ticks() - start_time) / 1000)
    score_surf = test_font.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

# Font for Title
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

game_name = test_font.render("Pixel Runner", False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))

instructions_surf = test_font.render("Press SPACE to start", False, (111, 196, 169))
instructions_rect = instructions_surf.get_rect(center=(400, 340))

start_time = 0
game_active = False
score = 0

# Background Surfaces
sky_surf = pygame.image.load("graphics/Sky.png").convert()
ground_surf = pygame.image.load("graphics/ground.png").convert()

score_surf = test_font.render("My game", False, (64, 64, 64))
score_rect = score_surf.get_rect(center=(400, 50))

# Snail Surface and Rectangle
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600, 300))

# Player Surface and Rectangle
player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0

# Intro Screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if player_rect.bottom == 300 and event.key == pygame.K_SPACE:
                    player_gravity = -20

            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = pygame.time.get_ticks()

    if game_active:
        # Displaying Background Images to the Display Surface
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))

        score = display_score()
        # pygame.draw.rect(screen, "#c0e8ec", score_rect)
        # pygame.draw.rect(screen, "#c0e8ec", score_rect, 10)
        # screen.blit(score_surf, score_rect)

        snail_rect.x -= 5
        if snail_rect.right < 0:
            snail_rect.left = 800
        screen.blit(snail_surf, snail_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)

        score_message = test_font.render(f"Your Score: {score}", False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 330))

        screen.blit(game_name, game_name_rect)
        if score == 0:
            screen.blit(instructions_surf, instructions_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)
