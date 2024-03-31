import pygame
import random

pygame.init()

# Set display dimensions
display_width = 1820
display_height = 1000
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('RacerExtend - Coin Collection')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (128, 128, 128)

# Car and coin images
car_img = pygame.image.load(r'C:\Users\timur\Desktop\GitHUB\KBTUstudy\Lab 8\Racer\carsRGB.png')
coin_img = pygame.image.load(r'C:\Users\timur\Desktop\GitHUB\KBTUstudy\Lab 8\Racer\coinsRGB.png')


def draw_highway(num_lanes):
    lane_width = display_width // num_lanes
    for i in range(num_lanes):
        pygame.draw.rect(gameDisplay, gray, (i * lane_width, 0, lane_width, display_height))
        if i < num_lanes - 1:  # Draw lane markings except for the last lane
            pygame.draw.line(gameDisplay, white, (i * lane_width + lane_width - 5, 0),
                             (i * lane_width + lane_width - 5, display_height), 5)


def car(x, y):
    gameDisplay.blit(car_img, (x, y - car_img.get_height()))


def draw_coin(x, y):
    gameDisplay.blit(coin_img, (x, y))


# Function to display text
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


# Function to display the coin count
def display_coin_count(count):
    font = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRect = text_objects("Coins: " + str(count), font)
    textRect.topright = (display_width - 20, 20)
    gameDisplay.blit(textSurf, textRect)


# Game loop
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0

    # Coin variables
    num_lanes = 10  # You can adjust the number of lanes here
    lane_width = display_width // num_lanes
    coin_x = random.randrange(lane_width // 2, display_width - lane_width // 2, lane_width)
    coin_y = -64  # Start off-screen
    coin_speed = 5
    coin_collected = False
    coin_collected_this_frame = False
    coin_initially_collected = False  # Flag for initial collection
    coin_count = 0

    gameExit = False

    while True:  # Keep the game running until the user quits
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Car movement controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        # Update car position
        x += x_change

        # Keep car within bounds
        x = max(0, min(x, display_width - car_img.get_width()))

        # Update coin position
        coin_y += coin_speed

        # Reset coin position if it goes off-screen
        if coin_y > display_height:
            coin_y = -64
            coin_x = random.randrange(lane_width // 2, display_width - lane_width // 2, lane_width)
            coin_collected = False
            coin_initially_collected = False  # Clear the initial collection flag

        # Check for coin collision
        car_rect = car_img.get_rect(topleft=(x, y))
        coin_rect = coin_img.get_rect(topleft=(coin_x, coin_y))
        collection_zone = pygame.Rect(x + car_img.get_width() // 4, y, car_img.get_width() // 2, car_img.get_height())

        if collection_zone.colliderect(coin_rect) and not coin_collected_this_frame:
            coin_collected = True
            coin_count += 1
            coin_collected_this_frame = True
            coin_initially_collected = True
        # Check if the coin is no longer colliding
        if not collection_zone.colliderect(coin_rect):
            coin_collected_this_frame = False  # Allow collection again
            coin_initially_collected = False    # Clear the initial collection flag

        # Draw everything
        gameDisplay.fill(white)
        draw_highway(num_lanes)
        car(x, y)  # Ensure y positions the car fully within the display
        if not coin_collected:
            draw_coin(coin_x, coin_y)
        display_coin_count(coin_count)

        pygame.display.update()  # Update the display to reflect changes


game_loop()
pygame.quit()
quit()