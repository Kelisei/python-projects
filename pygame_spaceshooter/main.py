from random import randint
import pygame
from sys import exit


def enemy_movement(enemy_list):
    if enemy_list:
        for enemy in enemy_list:
            enemy.top += 10
            screen.blit(enemy_surface, enemy)
        enemy_list = [enemy for enemy in enemy_list if enemy.top < 500]
        return enemy_list
    else:
        return []


def laser_movement(lasers):
    if lasers:
        for laser in lasers:
            laser.top -= 10
            screen.blit(laser_surface, laser)
        lasers = [laser for laser in lasers if laser.top > 0]
        return lasers
    else:
        return []


def collision_player(player, enemies):
    if enemies:
        for enemy in enemies:
            if player.colliderect(enemy):
                enemies.clear()
                return True
    return False


def collision_lasers(score, lasers, enemies):
    if lasers and enemies:
        for laser in lasers:
            for enemy in enemies:
                if laser.colliderect(enemy):
                    lasers.remove(laser)
                    enemies.remove(enemy)
                    return score + 1
    return score


def display_score(score):
    score_surface = main_font.render(f'{score}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 100))
    screen.blit(score_surface, score_rect)


pygame.init()
# Game-mode
gameover = False

# Score
score = 0

# We create the window
size = (800, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Space Shooter')

# We create a clock to limit the frames per second
clock = pygame.time.Clock()

# We load an enemy graphics and use a rect to give positioning
enemy_surface = pygame.image.load('graphics/Enemy.png').convert_alpha()
# enemy_rect = enemy_surface.get_rect(center=(600, 0))

enemy_rect_list = []

# We load the player graphics and use a rect to give positioning
player_surface = pygame.image.load('graphics/Player.png').convert_alpha()
player_rect = player_surface.get_rect(center=(400, 450))

# We load the background
bg_surface = pygame.image.load('graphics/Bg.png').convert()
bg_overlay = pygame.image.load('graphics/Game Over.png').convert_alpha()

# We load the ray texture
laser_surface = pygame.image.load('graphics/Ray.png').convert_alpha()
lasers = []

# We load the font
main_font = pygame.font.Font('graphics/fonts/unispace bd.ttf', 50)

# Timer
enemy_timer = pygame.USEREVENT + 1
time_passed = 0
miliseconds = 1000
pygame.time.set_timer(enemy_timer, miliseconds)

# Main game loop
while True:
    for event in pygame.event.get():
        # If the game is closed we want to break out the while and end all
        if event.type == pygame.QUIT:
            # .quit() is the inverse of init()
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and gameover:
                gameover = False
                player_rect.center = (400, 450)
                score = 0
            if event.key == pygame.K_SPACE and not gameover:
                lasers.append(laser_surface.get_rect(center=(player_rect.center)))


        if event.type == enemy_timer and not gameover:
            enemy_rect_list.append(enemy_surface.get_rect(center=(randint(0, 800), 0)))
    if not gameover:
        time_passed += 1
        if miliseconds > 100 and time_passed % 180 == 0:
            miliseconds = int(miliseconds // 1.1)
            pygame.time.set_timer(enemy_timer, miliseconds)

        display_score(score)

        # We draw the background
        screen.blit(bg_surface, (0, 0))

        # We draw the player
        screen.blit(player_surface, player_rect)

        # Move stuff
        enemy_rect_list = enemy_movement(enemy_rect_list)
        lasers = laser_movement(lasers)
        # Collision
        gameover = collision_player(player_rect, enemy_rect_list)
        score = collision_lasers(score, lasers, enemy_rect_list)

        # Controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and player_rect.left < 750:
            player_rect.left += 8

        if keys[pygame.K_a] and player_rect.left > 50:
            player_rect.left -= 8

        display_score(score)
    else:
        screen.blit(bg_overlay, (0, 0))
        miliseconds = 1000
    # Updates all elements.
    pygame.display.update()
    clock.tick(60)
