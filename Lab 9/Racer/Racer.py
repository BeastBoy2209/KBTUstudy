import pygame
import random
import json

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Racer Game")
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 250, 0)
grey = (128, 128, 128)

car_img = pygame.image.load(r"C:\Users\timur\Desktop\GitHUB\KBTUstudy\Lab 9\Racer\Car.png").convert_alpha()
coin1_img = pygame.image.load(r"C:\Users\timur\Desktop\GitHUB\KBTUstudy\Lab 9\Racer\coin1.png").convert_alpha()
coin2_img = pygame.image.load(r"C:\Users\timur\Desktop\GitHUB\KBTUstudy\Lab 9\Racer\coin2.png").convert_alpha()
enemy_img = pygame.image.load(r"C:\Users\timur\Desktop\GitHUB\KBTUstudy\Lab 9\Racer\enemy_car.png").convert_alpha()
background_img = pygame.image.load(r"C:\Users\timur\Desktop\GitHUB\KBTUstudy\Lab 9\Racer\asphalt.png").convert()

lane_width = screen_width // 6
lane_1_left = 0

class Coin:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.img = random.choice([coin1_img, coin2_img])
        self.rect = self.img.get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.img, self.rect)

    def update(self):
        self.y += coin_speed
        self.rect.top = self.y

class EnemyCar:
    def __init__(self, x, y, lane, speed):
        self.x = x
        self.y = y
        self.lane = lane
        self.speed = speed
        self.img = enemy_img

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def update(self):
        self.y += self.speed
        if self.y > screen_height:
            self.y = -self.img.get_height()
            self.lane = random.randint(0, 5) 
            self.x = lane_1_left + self.lane * lane_width + lane_width // 2 - self.img.get_width() // 2

    def check_collision(self, player_rect):
        enemy_rect = self.img.get_rect(topleft=(self.x, self.y))
        return enemy_rect.colliderect(player_rect)

class PlayerCar:
    def __init__(self):
        self.x = screen_width // 2 - car_img.get_width() // 2 - lane_width // 2
        self.y = screen_height - 100
        self.lane = 3 
        self.speed = 3  
        self.score = 0
        self.img = car_img

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def update(self):
        global move_left, move_right, last_lane_change_time
        current_time = pygame.time.get_ticks()
        if current_time - last_lane_change_time >= lane_change_delay:
            if move_left and self.lane > 1:
                self.lane -= 1
                self.x = lane_1_left + (self.lane - 1) * lane_width + lane_width // 2 - car_img.get_width() // 2
                last_lane_change_time = current_time
            elif move_right and self.lane < 6:
                self.lane += 1
                self.x = lane_1_left + (self.lane - 1) * lane_width + lane_width // 2 - car_img.get_width() // 2  
                last_lane_change_time = current_time

    def check_collision(self, enemies):
        player_rect = self.img.get_rect(topleft=(self.x, self.y))
        for enemy in enemies:
            enemy_rect = enemy.img.get_rect(topleft=(enemy.x, enemy.y))
            if player_rect.colliderect(enemy_rect):
                return True
        return False

    def collect_coins(self, coins):
        collected_coins = []
        player_rect = self.img.get_rect(topleft=(self.x, self.y))
        for coin in coins:
            coin_rect = coin.img.get_rect(topleft=(coin.x, coin.y))
            if player_rect.colliderect(coin_rect):
                self.score += coin.value
                collected_coins.append(coin)
        return collected_coins 

def draw_road_markings(screen):
    dashed_line_width = 5
    first_line_left = lane_width // 2 
    for lane in range(6):
        lane_left = first_line_left + lane_width * lane 
        for y in range(-road_marking_offset, screen_height, dashed_line_length + gap_between_dashes): 
            start_pos = (lane_left, y)
            end_pos = (lane_left, y + dashed_line_length) 
            pygame.draw.line(screen, white, start_pos, end_pos, dashed_line_width) 

menu_font = pygame.font.SysFont(None, 48)
button_width = 200
button_height = 50
button_color = (0, 128, 255)
button_text_color = white

def create_button(text, x, y):
    button_rect = pygame.Rect(x, y, button_width, button_height)
    pygame.draw.rect(screen, button_color, button_rect)
    text_surface = menu_font.render(text, True, button_text_color)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)
    return button_rect

def create_slider(x, y, width, min_value, max_value, current_value):
    slider_rect = pygame.Rect(x, y, width, 5)
    pygame.draw.rect(screen, white, slider_rect)

    handle_radius = 10
    handle_x = x + (width - 2 * handle_radius) * ((current_value - min_value) / (max_value - min_value))
    handle_rect = pygame.Rect(handle_x, y - handle_radius + 2, 2 * handle_radius, 2 * handle_radius)
    pygame.draw.circle(screen, button_color, handle_rect.center, handle_radius)
    
    return slider_rect, handle_rect

def load_settings():
    try:
        with open("settings.json", "r") as f:
            settings = json.load(f)
            return settings
    except FileNotFoundError:
        return {}

def save_settings(settings):
    with open("settings.json", "w") as f:
        json.dump(settings, f)

def show_settings_menu():
    global coin_speed, coin_spawn_rate, enemy_spawn_rate, max_enemies
    
    settings = load_settings()
    
    coin_speed = settings.get("coin_speed", 1)
    coin_spawn_rate = settings.get("coin_spawn_rate", 1000)
    enemy_spawn_rate = settings.get("enemy_spawn_rate", 1000)
    max_enemies = settings.get("max_enemies", 5)

    coin_speed_slider, coin_speed_handle = create_slider(150, 100, 500, 1, 10, coin_speed)
    coin_spawn_rate_slider, coin_spawn_rate_handle = create_slider(150, 150, 500, 200, 2000, coin_spawn_rate)
    enemy_spawn_rate_slider, enemy_spawn_rate_handle = create_slider(150, 200, 500, 200, 2000, enemy_spawn_rate)
    max_enemies_slider, max_enemies_handle = create_slider(150, 250, 500, 1, 10, max_enemies)

    dragging_coin_speed = False
    dragging_coin_spawn_rate = False
    dragging_enemy_spawn_rate = False
    dragging_max_enemies = False
    
    exit_settings_menu = False 

    while not exit_settings_menu:
        screen.fill(grey)
        
        coin_speed_text = menu_font.render(f"Coin Speed: {coin_speed}", True, white)
        screen.blit(coin_speed_text, (50, 70))
        coin_spawn_rate_text = menu_font.render(f"Coin Spawn Rate: {coin_spawn_rate}", True, white)
        screen.blit(coin_spawn_rate_text, (50, 120))
        enemy_spawn_rate_text = menu_font.render(f"Enemy Spawn Rate: {enemy_spawn_rate}", True, white)
        screen.blit(enemy_spawn_rate_text, (50, 170))
        max_enemies_text = menu_font.render(f"Max Enemies: {max_enemies}", True, white)
        screen.blit(max_enemies_text, (50, 220))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if coin_speed_handle.collidepoint(event.pos):
                    dragging_coin_speed = True
                elif coin_spawn_rate_handle.collidepoint(event.pos):
                    dragging_coin_spawn_rate = True
                elif enemy_spawn_rate_handle.collidepoint(event.pos):
                    dragging_enemy_spawn_rate = True 
                elif max_enemies_handle.collidepoint(event.pos):
                    dragging_max_enemies = True
                elif back_button.collidepoint(event.pos):
                    exit_settings_menu = True 
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging_coin_speed = False
                dragging_coin_spawn_rate = False 
                dragging_enemy_spawn_rate = False
                dragging_max_enemies = False
            elif event.type == pygame.MOUSEMOTION:
                if dragging_coin_speed:
                    handle_x = event.pos[0]
                    handle_x = max(coin_speed_slider.left, min(handle_x, coin_speed_slider.right - 20)) 
                    coin_speed = round(1 + (handle_x - coin_speed_slider.left) / (coin_speed_slider.width - 20) * 9)
                elif dragging_coin_spawn_rate:
                    handle_x = event.pos[0]
                    handle_x = max(coin_spawn_rate_slider.left, min(handle_x, coin_spawn_rate_slider.right - 20))
                    coin_spawn_rate = round(200 + (handle_x - coin_spawn_rate_slider.left) / (coin_spawn_rate_slider.width - 20) * 1800)
                elif dragging_enemy_spawn_rate:
                    handle_x = event.pos[0] 
                    handle_x = max(enemy_spawn_rate_slider.left, min(handle_x, enemy_spawn_rate_slider.right - 20))
                    enemy_spawn_rate = round(200 + (handle_x - enemy_spawn_rate_slider.left) / (enemy_spawn_rate_slider.width - 20) * 1800)
                elif dragging_max_enemies: 
                    handle_x = event.pos[0]
                    handle_x = max(max_enemies_slider.left, min(handle_x, max_enemies_slider.right - 20)) 
                    max_enemies = round(1 + (handle_x - max_enemies_slider.left) / (max_enemies_slider.width - 20) * 9)

        coin_speed_slider, coin_speed_handle = create_slider(150, 100, 500, 1, 10, coin_speed)
        coin_spawn_rate_slider, coin_spawn_rate_handle = create_slider(150, 150, 500, 200, 2000, coin_spawn_rate)
        enemy_spawn_rate_slider, enemy_spawn_rate_handle = create_slider(150, 200, 500, 200, 2000, enemy_spawn_rate)
        max_enemies_slider, max_enemies_handle = create_slider(150, 250, 500, 1, 10, max_enemies)

        back_button = create_button("Back", screen_width // 2 - button_width // 2, 450)

        pygame.display.flip()
        clock.tick(60)

    save_settings({
        "coin_speed": coin_speed,
        "coin_spawn_rate": coin_spawn_rate,
        "enemy_spawn_rate": enemy_spawn_rate,
        "max_enemies": max_enemies,
    })

def init_game():
    global game_over, enemies, coins, last_enemy_spawn, last_coin_spawn, player_car, last_lane_change_time 
    game_over = False
    enemies = []
    coins = []
    last_enemy_spawn = pygame.time.get_ticks()
    last_coin_spawn = 0
    player_car = PlayerCar() 
    last_lane_change_time = 0 

game_over = False
enemies = []
coins = []
last_enemy_spawn = pygame.time.get_ticks()
last_coin_spawn = 0
enemy_spawn_rate = 1000 
coin_spawn_rate = 1000
coin_speed = 1
max_coins = 2
move_left = False 
move_right = False 
max_enemies = 5
lane_change_delay = 200 
last_lane_change_time = 0 
road_marking_offset = 0 
road_marking_speed = 2
dashed_line_length = 20 
gap_between_dashes = 10 
background_y = 0 
background_speed = 2 

font = pygame.font.SysFont(None, 32) 

player_car = PlayerCar() 

settings = load_settings()
coin_speed = settings.get("coin_speed", 1)
coin_spawn_rate = settings.get("coin_spawn_rate", 1000)
enemy_spawn_rate = settings.get("enemy_spawn_rate", 1000)
max_enemies = settings.get("max_enemies", 5)

# Game loop 
running = True
in_menu = False  # Начинаем игру сразу, без меню
init_game()  # Инициализация новой игры
mouse_pressed = False 
while running:
    current_time = pygame.time.get_ticks() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True 
            elif event.key == pygame.K_RIGHT:
                move_right = True 
            elif event.key == pygame.K_ESCAPE and not game_over:
                in_menu = True  
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False 
            elif event.key == pygame.K_RIGHT:
                move_right = False 
        elif event.type == pygame.ACTIVEEVENT:
            if event.state == pygame.APPACTIVE:
                if event.gain == 1:
                    move_left = False 
                    move_right = False 
        elif event.type == pygame.MOUSEBUTTONDOWN and in_menu:  
            if resume_button.collidepoint(event.pos):
                in_menu = False
            elif settings_button.collidepoint(event.pos):
                show_settings_menu() 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over: 
                init_game()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True 

    if in_menu:
        screen.fill(grey)

        resume_button = create_button("Resume", screen_width // 2 - button_width // 2, 200)
        settings_button = create_button("Settings", screen_width // 2 - button_width // 2, 300)

    else:
        background_y += background_speed 
        if background_y >= background_img.get_height(): 
            background_y = 0 
        screen.blit(background_img, (0, background_y - background_img.get_height())) 
        screen.blit(background_img, (0, background_y))

        draw_road_markings(screen) 

        for coin in coins:
            coin.draw(screen)  

        player_car.draw(screen)
        for enemy in enemies:
            enemy.draw(screen) 

        collected_coins = player_car.collect_coins(coins)
        for coin in collected_coins:
            coins.remove(coin)

        score_text = font.render(f"Score: {player_car.score}", True, white)
        screen.blit(score_text, (10, 10)) 

        if game_over:
            screen.fill(grey) 

            game_over_text = menu_font.render("GAME OVER", True, red)
            text_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
            screen.blit(game_over_text, text_rect)

            restart_button = create_button("Restart", screen_width // 2 - button_width // 2, screen_height // 2 + 50)
            quit_button = create_button("Quit", screen_width // 2 - button_width // 2, screen_height // 2 + 120)

    if game_over and mouse_pressed:
        if restart_button.collidepoint(pygame.mouse.get_pos()):
            init_game() 
        elif quit_button.collidepoint(pygame.mouse.get_pos()):
            running = False 
    mouse_pressed = False 

    if not in_menu:  
        if not game_over and pygame.time.get_ticks() - last_coin_spawn >= coin_spawn_rate:
            coin_lane = random.randint(0, 5)
            coin_x = lane_1_left + coin_lane * lane_width + lane_width // 2 - coin1_img.get_width() // 2
            coin_y = -coin1_img.get_height()
            coin_value = random.choice([10, 30])
            coins.append(Coin(coin_x, coin_y, coin_value))
            last_coin_spawn = pygame.time.get_ticks()

        if not game_over:
            if current_time - last_enemy_spawn >= enemy_spawn_rate and len(enemies) < max_enemies:
                enemy_lane = random.randint(0, 5) 
                enemy_speed = random.randint(3, 6)
                enemy_x = lane_1_left + enemy_lane * lane_width + lane_width // 2 - enemy_img.get_width() // 2 
                enemies.append(EnemyCar(enemy_x, -enemy_img.get_height(), enemy_lane, enemy_speed))
                last_enemy_spawn = current_time 

        if not game_over:
            coins_to_remove = [] 
            for coin in coins:
                coin.update()
                if coin.y > screen_height:
                    coins_to_remove.append(coin)
            for coin in coins_to_remove:
                coins.remove(coin)
            for enemy in enemies:
                enemy.update()
            if player_car.check_collision(enemies):
                game_over = True 

        if not game_over and not in_menu:
            player_car.update() 

        if not in_menu:
            road_marking_offset -= road_marking_speed 
            if road_marking_offset <= - (dashed_line_length + gap_between_dashes):
                road_marking_offset = 0 

    pygame.display.flip()
    clock.tick(60)

pygame.quit()