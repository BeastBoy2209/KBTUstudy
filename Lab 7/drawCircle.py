import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
RADIUS = 25
SPEED = 0.1

screen = pygame.display.set_mode((WIDTH, HEIGHT))

x, y = WIDTH // 2, HEIGHT // 2

running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), RADIUS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y - SPEED - RADIUS > 0:
        y -= SPEED
    if keys[pygame.K_DOWN] and y + SPEED + RADIUS < HEIGHT:
        y += SPEED
    if keys[pygame.K_LEFT] and x - SPEED - RADIUS > 0:
        x -= SPEED
    if keys[pygame.K_RIGHT] and x + SPEED + RADIUS < WIDTH:
        x += SPEED

    pygame.display.flip()

pygame.quit()
