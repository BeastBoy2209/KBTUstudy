import pygame
import time
import math
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

image_path = image_path = r"C:\Users\timur\Desktop\GitHUB\KBTUstudy\Lab 7\mickeyclock.png"
image = pygame.image.load(image_path)

center = (350, 250)

length_seconds = 100
length_minutes = 80

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    # Get the current time
    current_time = time.localtime()

    # Calculate the angle of the hands
    angle_seconds = math.radians(current_time.tm_sec * 6 - 90)
    angle_minutes = math.radians(current_time.tm_min * 6 - 90)

    # Calculate the end point of the hands
    end_seconds = (center[0] + length_seconds * math.cos(angle_seconds), center[1] + length_seconds * math.sin(angle_seconds))
    end_minutes = (center[0] + length_minutes * math.cos(angle_minutes), center[1] + length_minutes * math.sin(angle_minutes))

    # --- Drawing code should go here
    # First, clear the screen to white
    screen.fill((255, 255, 255))

    # Draw the image
    screen.blit(pygame.transform.scale(image, (700, 500)), (0, 0))

    # Draw the hands
    pygame.draw.line(screen, (255, 0, 0), center, end_seconds, 2)
    pygame.draw.line(screen, (0, 0, 255), center, end_minutes, 4)

    # --- Go ahead and update the screen with what we've drawn
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit
pygame.quit()
