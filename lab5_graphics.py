import pygame
import math
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

PI = math.pi

pygame.display.set_caption("Nima's Game")
size = (700, 500)
screen = pygame.display.set_mode(size)
screen.fill(BLACK)
pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
pygame.draw.line(screen, GREEN, [100, 100], [0, 200], 5)
for y_offset in range(0, 500, 20):
    pygame.draw.line(screen,BLUE,[0,10+y_offset],[300,110+y_offset],5)
pygame.draw.rect(screen, WHITE, [500, 100, 150, 100], 2)
pygame.draw.ellipse(screen, RED, [500, 100, 150, 100], 2)

font = pygame.font.SysFont('Calibri', 25, True, False)
text = font.render("My text", True, BLACK)
screen.blit(text, [250, 250])

pygame.display.flip()
pygame.quit()
sys.exit()

"""
 Pygame base template for opening a window
"""
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
sys.exit()