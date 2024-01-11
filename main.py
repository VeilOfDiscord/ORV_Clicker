# Welcome to the beginning of what will be the amazing code for [REDACTED], enjoy !

# Main game idea? ORV CLICKEWR GMAE RAHHHHHHHH

#  1. Find out how to blit sprite and GUI
#  2. Find out controls (Mouse and Keyboard)
#  3. Find out different Menus too!
#  4. Fuck around to get a nice gameplay loop
#  5. Find out how collisions work
#  6. Fuck around with collision physics

import pygame as pg
import game as g

# screen size
HEIGHT = 700
WIDTH = 500

# create game window
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Omniscient Clicker's Viewpoint")

# set game constants
GM = g.game(0.0, 50.0, 2.0, 0, 2.5)

# framerate
clock = pg.time.Clock()
FPS = 60

# define shop area
SHOP_HEIGHT = 300
area = pg.Rect(0, HEIGHT-SHOP_HEIGHT, WIDTH, SHOP_HEIGHT)

class Square(pg.sprite.Sprite):
    def __init__(self, col, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

# create sprites
square = Square("crimson", WIDTH/2, 100)   
mc = Square("green", WIDTH/2, 230)
squares = pg.sprite.Group()
squares.add(square)
squares.add(mc)

# companion sprite section
# 07/01/2024 - https://stackoverflow.com/questions/22361249/how-can-i-just-draw-a-specific-sprite-in-a-group-with-pygame-draw
# cont'd - https://stackoverflow.com/questions/62210803/questions-with-creating-sprites-in-pygame
# Notes: Move lower creation to be cleaner, 
        # buy companion system and increment that value to add sprite to group (so that it can be drawn)
        # make position values cleaner too, make it move with aspect ratio

party = pg.sprite.Group()

# combat force
empress = Square("orange", (WIDTH/2)+140, (HEIGHT/4)+95) # Yoo Sang-Ah
insect = Square("tan", (WIDTH/2)+120, (HEIGHT/4)+165)   # Lee Gil Young
soldier = Square("silver", (WIDTH/2)-120, (HEIGHT/4)+ 85) # Lee Hyunsung
judge = Square("maroon", (WIDTH/2)-200, (HEIGHT/4)+90) # Jung Heewon
tamer = Square("gold", (WIDTH/2)+175, (HEIGHT/4)+155) # Shin Yoosung
admiral = Square("navy", (WIDTH/2)-180, (HEIGHT/4)+165) # Lee Jihye
beauty = Square("yellow",(WIDTH/2)-80, (HEIGHT/4)+165)  # Hang Hayoung

# support force
# doctor = Square("orange", (WIDTH/2)+80, (HEIGHT/4)+155) # Lee Seolhwa
# landlord = Square("orange", (WIDTH/2)+80, (HEIGHT/4)+155) # Gong Pildu
# lizard = Square("orange", (WIDTH/2)+80, (HEIGHT/4)+155) # Han Myugoh

party_mem = [empress, insect, soldier, judge, tamer, admiral, beauty]
# party.add(party_mem[0])
# party.add(party_mem[1])
# party.add(party_mem[2])
# party.add(party_mem[3])
# party.add(party_mem[4])
# party.add(party_mem[5])
# party.add(party_mem[6])






# Our main loop that actually runs the game.
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button.
                # Check if the rect collides with the mouse pos.
                if area.collidepoint(event.pos):
                    print('Area clicked.')
                else:
                    print("Left Clicked!")
                    GM.dealDamage()
            if event.button == 3: # Right mouse button.
                print('Right Clicked!')

    # check if enemy has been defeated or not
    if(GM.enemy_health <= 0.0):
        GM.respawnEnemy()

    clock.tick(FPS)

    # fill screen
    screen.fill("dimgrey")

    # update sprite group
    squares.update()
    
    # draw sprite group
    squares.draw(screen)
    party.draw(screen)
    # shop
    pg.draw.rect(screen, "grey", area)

    pg.display.flip()