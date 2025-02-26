"""
Base code from: https://www.makeuseof.com/pygame-touch-inputs-working-with/
"""

import pygame as pg

pg.init()
# Set up the display
size = (400, 400)
screen = pg.display.set_mode(size)
clock = pg.time.Clock()

# Create a player object
player = pg.Surface((50, 50))
player.fill((255, 0, 0))

# Set the initial position of the player
player_pos = [175, 175]
# The game loop
running = True

while running:
    clock.tick(60)
    # Check for events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # Check for mouse inputs
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            player_pos[0] = mouse_x
            player_pos[1] = mouse_y
        elif event.type == pg.MOUSEBUTTONUP:
            pass
        # Check for finger inputs
        elif event.type == pg.FINGERDOWN:
            finger_x, finger_y = event.pos
            player_pos[0] = finger_x
            player_pos[1] = finger_y
        elif event.type == pg.FINGERUP:
            pass

    screen.fill((0, 0, 0))

    # Draw the player
    screen.blit(player, player_pos)

    # Update the display
    pg.display.update()
