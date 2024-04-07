import pygame
import random
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

    def check_click(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

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
        self.x = screen_width // 2 - car_img.get_width() // 2
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

def draw_road_markings(screen):
    dashed_line_width = 5
    first_line_left = lane_width // 2 
    for lane in range(6):
        lane_left = first_line_left + lane_width * lane 
        for y in range(-road_marking_offset, screen_height, dashed_line_length + gap_between_dashes): 
            start_pos = (lane_left, y)
            end_pos = (lane_left, y + dashed_line_length) 
            pygame.draw.line(screen, white, start_pos, end_pos, dashed_line_width) 

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

# Game loop 
running = True
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

        coins_to_remove = [] 
        for coin in coins:
            coin.update()
            coin.draw(screen)  
            if coin.y > screen_height:
                coins_to_remove.append(coin)
            else:
                coin.draw(screen)  

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for coin in coins:
                    if coin.check_click(mouse_pos):
                        player_car.score += coin.value
                        coins_to_remove.append(coin)
                        print("Coin collected!")
                        break 

        for coin in coins_to_remove:
            coins.remove(coin)

        for enemy in enemies:
            enemy.update()

        if player_car.check_collision(enemies):
            game_over = True 

    background_y += background_speed 
    if background_y >= background_img.get_height(): 
        background_y = 0 

    screen.blit(background_img, (0, background_y - background_img.get_height())) 
    screen.blit(background_img, (0, background_y))

    draw_road_markings(screen) 

    player_car.draw(screen)
    for enemy in enemies:
        enemy.draw(screen) 

    score_text = font.render(f"Score: {player_car.score}", True, white)
    screen.blit(score_text, (10, 10)) 

    if game_over:
        game_over_text = font.render("Game Over!", True, red)
        screen_center_x = screen_width // 2 
        screen_center_y = screen_height // 2 
        text_rect = game_over_text.get_rect(center=(screen_center_x, screen_center_y))
        screen.blit(game_over_text, text_rect) 
 
    pygame.display.flip()

    if not game_over:
        player_car.update() 

    road_marking_offset += road_marking_speed 
    if road_marking_offset >= dashed_line_length + gap_between_dashes:
        road_marking_offset = 0 

    clock.tick(60) 

pygame.quit() 