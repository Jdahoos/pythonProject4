import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
PURPLE = (128, 0, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
ORANGE = (255, 128, 0)
display_surface.fill(CYAN)

CENTER = (200, 500)
RADIUS = 100
pygame.draw.circle(display_surface, WHITE, CENTER, RADIUS)

START = (100, 100)
END = (500, 500)
pygame.draw.line(display_surface, BLUE, START, END)

X = 310
Y = 300
WIDTH = 100
HEIGHT = 300
rect = pygame. Rect(X, Y, WIDTH, HEIGHT)
pygame.draw.rect(display_surface, CYAN, rect)

CENTER = (200, 350)
RADIUS = 75
pygame.draw.circle(display_surface, WHITE, CENTER, RADIUS)

CENTER = (200, 250)
RADIUS = 50
pygame.draw.circle(display_surface, WHITE, CENTER, RADIUS)
CENTER = (175, 240)
RADIUS = 10
pygame.draw.circle(display_surface, BLACK, CENTER, RADIUS)

CENTER = (225, 240)
RADIUS = 10
pygame.draw.circle(display_surface, BLACK, CENTER, RADIUS)








running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()
