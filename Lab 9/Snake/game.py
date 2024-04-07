import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game with Food Weights and Timers')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Define food types with different weights and colors
food_types = {
    "apple": {"weight": 70, "color": (255, 0, 0)},  # Red apple (most common)
    "banana": {"weight": 20, "color": (255, 255, 0)},  # Yellow banana
    "berry": {"weight": 10, "color": (128, 0, 128)},  # Purple berry (rare)
}

def draw_score(score, level):
    value = score_font.render("Your Score: " + str(score) + "  Level: " + str(level), True, white)
    dis.blit(value, [0, 0])

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def check_collision(snake_head, snake_body):
    for x in snake_body[:-1]:
        if x == snake_head:
            return True
    if snake_head[0] >= dis_width or snake_head[0] < 0 or snake_head[1] >= dis_height or snake_head[1] < 0:
        return True
    return False

# Function to generate food with weights
def generate_food(snake_body):
    while True:
        x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        if (x, y) not in snake_body:
            food_type = random.choices(list(food_types.keys()), 
                                      weights=[v["weight"] for v in food_types.values()])[0]
            return (x, y), food_type

# Function to draw food with specific color
def draw_food(food_position, food_type):
    pygame.draw.rect(dis, food_types[food_type]["color"], 
                     [food_position[0], food_position[1], snake_block, snake_block])

# Function to draw the timer
def draw_timer(time_left):
    timer_text = font_style.render(f"Food Timer: {time_left}", True, white)
    dis.blit(timer_text, [dis_width - timer_text.get_width() - 10, 10])  # Position at top-right corner

def level_up(score):
    global level, snake_speed
    if score % 5 == 0 and score > 0:
        level += 1
        snake_speed += 2

def game_loop():
    global snake_speed, level
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    food_position, food_type = generate_food(snake_list)
    food_timer = 10  # Timer for food disappearance

    level = 1

    while not game_over:

        while game_close == True:
            dis.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            draw_score(snake_length - 1, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != snake_block:
                    x1_change = -snake_block
                    y1_change = 0 
                elif event.key == pygame.K_RIGHT and x1_change != -snake_block:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != snake_block:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change != -snake_block:
                    y1_change = snake_block
                    x1_change = 0

        if check_collision([x1, y1], snake_list):
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)

        # Update and draw food with timer
        food_timer -= 1
        if food_timer <= 0:
            food_position, food_type = generate_food(snake_list)
            food_timer = 100
        draw_food(food_position, food_type)

        # Draw the timer
        draw_timer(food_timer)

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        draw_snake(snake_block, snake_list)
        draw_score(snake_length - 1, level)

        pygame.display.update()

        if x1 == food_position[0] and y1 == food_position[1]:
            food_position, food_type = generate_food(snake_list)
            snake_length += 1
            level_up(snake_length - 1)

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()