"""
Gameplay:
Collect as many coins as you can.
Dodge the red falling cubes.
The more you survive, your score increases.
The more your score increases, the harder it gets.
"""

# Libraries
import pygame, random

# Declarations
screen_size = (1200, 900)
BACKGROUND = (102, 179, 255)
player_size = 70
player_poz = [screen_size[0] / 2, screen_size[1] - 2 * player_size]
cube_size = 40
cube_poz = [random.randint (0, screen_size[0] - cube_size), 0]
enemies = [cube_poz]
FPS = 60
speed = 5
running = True
Score = 0
clock = pygame.time.Clock ()
coin_size = 25
coin_poz = [random.randint (50, screen_size[1] - 50), screen_size[1] - 70]
Coins = 0


# Functions
def display_enemies (enemies):
    for cube_poz in enemies:
        pygame.draw.rect (screen, (255, 0, 0), (cube_poz[0], cube_poz[1], cube_size, cube_size))


def respawn_enemies (enemies):
    delay = random.random ()
    if len (enemies) < 12 and delay < 0.3:
        t = random.randint (0, screen_size[0] - cube_size)
        inamic_x = t
        enemies.append ([inamic_x, 0])


def stages (Score, speed):
    if Score < 35:
        speed = 5
    elif Score > 35 and Score < 71:
        speed = 8
    elif 71 < Score < 107:
        speed = 11
    elif Score > 107 and Score < 140:
        speed = 14
    elif Score > 140 and Score < 170:
        speed = 17
    else:
        speed = 20
    return speed


def positions (enemies, Score):
    for i, cube_poz in enumerate (enemies):
        if cube_poz[1] >= 0 and cube_poz[1] < screen_size[1]:
            cube_poz[1] = cube_poz[1] + speed
            # Vertical falling
        else:
            enemies.pop (i)
            Score = Score + 1
    return Score


def quit_if_collision (player_poz, cube_poz):
    if ((cube_poz[0] >= player_poz[0] and cube_poz[0] < player_poz[0] + player_size) or (
            player_poz[0] >= cube_poz[0] and player_poz[0] < cube_poz[0] + cube_size)):
        if ((cube_poz[1] >= player_poz[1] and cube_poz[1] < player_poz[1] + player_size) or (
                player_poz[1] >= cube_poz[1] and player_poz[1] < cube_poz[1] + cube_size)):
            return True
    return False


def get_coin (player_poz, cube_poz):
    if ((cube_poz[0] >= player_poz[0] and cube_poz[0] < player_poz[0] + player_size) or (
            player_poz[0] >= cube_poz[0] and player_poz[0] < cube_poz[0] + cube_size)):
        if ((cube_poz[1] >= player_poz[1] and cube_poz[1] < player_poz[1] + player_size) or (
                player_poz[1] >= cube_poz[1] and player_poz[1] < cube_poz[1] + cube_size)):
            return True
    return False


def collected (player_poz, coin_poz):
    if (coin_poz[0] >= player_poz[0] and coin_poz[0] <= (player_poz[0] + player_size)):
        return True
    return False


def bool_collision (enemies, player_poz):
    for cube_poz in enemies:
        if quit_if_collision (cube_poz, player_poz):
            return True

    return False


def collect_coin (coin, player_poz):
    if collected (coin, player_poz):
        return True
    return False


def spawn_coin ():
    pygame.draw.rect (screen, (255, 255, 0), (coin_poz[0], coin_poz[1], coin_size, coin_size))


while running:
    pygame.init ()
    pygame.display.set_caption ("DODGE IT!")
    screen = pygame.display.set_mode ((screen_size[0], screen_size[1]))
    Word_font = pygame.font.SysFont ("arial", 25)
    Word_font2 = pygame.font.SysFont ("arial", 25)
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN:
            # Movement & prevent from leaving screen
            if event.key == pygame.K_LEFT:
                player_poz[0] = player_poz[0] - 50
                if (player_poz[0] < 0): player_poz[0] += 50
            elif event.key == pygame.K_RIGHT:
                if (player_poz[0] <= screen_size[0] - 50):
                    player_poz[0] = player_poz[0] + 50
            player_poz = [player_poz[0], player_poz[1]]

    # Display
    screen.fill (BACKGROUND)
    respawn_enemies (enemies)
    Score = positions (enemies, Score)
    speed = stages (Score, speed)
    text = "S c o r e: " + str (Score)
    label = Word_font.render (text, 1, (255, 255, 255))
    screen.blit (label, (screen_size[0] - 150, screen_size[1] - 50))
    text = "C o i n s : " + str (Coins)
    label = Word_font2.render (text, 1, (255, 255, 255))
    screen.blit (label, (screen_size[0] - 300, screen_size[1] - 50))

    if bool_collision (enemies, player_poz):
        running = False
    display_enemies (enemies)
    pygame.draw.rect (screen, (0, 255, 0),
                      (player_poz[0] - (player_size / 2), player_poz[1] + 40, player_size, player_size))
    clock.tick (FPS)
    spawn_coin ()
    if collect_coin (coin_poz, player_poz):
        Coins = Coins + 1
        coin_poz[0] = random.randint (50, screen_size[0] - 50)
        spawn_coin ()
    pygame.display.update ()
    pygame.display.flip ()
