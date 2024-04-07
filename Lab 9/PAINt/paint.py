import pygame
import math

colors = {
    "green": (0, 255, 0),
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "black": (0, 0, 0),
    "white": (255, 255, 255),
}

pygame.init()
width, height = 1000, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Paint")

# --- Button setup ---
button_width, button_height = 50, 50
button_margin = 10

# Color buttons
color_buttons = []
for i, color in enumerate(colors):
    x = button_margin + i * (button_width + button_margin)
    y = button_margin
    button = pygame.Rect(x, y, button_width, button_height)
    color_buttons.append((button, color))

# Shape buttons
shape_buttons = []
shapes = ["line", "square", "right triangle", "equilateral triangle", "rhombus"]
for i, shape in enumerate(shapes):
    x = button_margin + i * (button_width + button_margin)
    y = button_margin * 2 + button_height  # Below color buttons
    button = pygame.Rect(x, y, button_width, button_height)
    shape_buttons.append((button, shape))

clear_button = pygame.Rect(width - button_width - button_margin, button_margin, button_width, button_height)

# --- Drawing functions ---
def draw_square(screen, color, start_pos, end_pos):
    width = abs(end_pos[0] - start_pos[0])
    height = abs(end_pos[1] - start_pos[1])
    size = 40
    rect = pygame.Rect(start_pos[0], start_pos[1], size, size)
    pygame.draw.rect(screen, colors[color], rect)

def draw_right_triangle(screen, color, start_pos, end_pos):
    # Determine base and height based on mouse movement direction
    base = end_pos[0] - start_pos[0]
    height = end_pos[1] - start_pos[1]
    
    # Ensure right angle is always at the start_pos
    if abs(base) > abs(height):
        # Base is longer, so make it horizontal
        if base > 0:
            point1 = start_pos
            point2 = (start_pos[0] + base, start_pos[1])
            point3 = (start_pos[0], start_pos[1] + height)
        else:
            point1 = start_pos
            point2 = (start_pos[0] + base, start_pos[1])
            point3 = (start_pos[0] + base, start_pos[1] + height)
    else:
        # Height is longer (or equal), so make it vertical
        if height > 0:
            point1 = start_pos
            point2 = (start_pos[0], start_pos[1] + height)
            point3 = (start_pos[0] + base, start_pos[1])
        else:
            point1 = start_pos
            point2 = (start_pos[0], start_pos[1] + height)
            point3 = (start_pos[0] + base, start_pos[1] + height)

    pygame.draw.polygon(screen, colors[color], [point1, point2, point3], 20) 

def draw_equilateral_triangle(screen, color, start_pos, end_pos):
    side = abs(end_pos[0] - start_pos[0])
    height = side * math.sqrt(3) / 2
    point1 = start_pos
    point2 = (start_pos[0] + side, start_pos[1])
    point3 = (start_pos[0] + side / 2, start_pos[1] + height)
    pygame.draw.polygon(screen, colors[color], [point1, point2, point3], 20)

def draw_rhombus(screen, color, start_pos, end_pos):
    width = abs(end_pos[0] - start_pos[0])
    height = abs(end_pos[1] - start_pos[1])
    point1 = start_pos
    point2 = (start_pos[0] + width / 2, start_pos[1] + height)
    point3 = (start_pos[0] + width, start_pos[1])
    point4 = (start_pos[0] + width / 2, start_pos[1] - height)
    pygame.draw.polygon(screen, colors[color], [point1, point2, point3, point4], 20)

shape_functions = {
    "square": draw_square,
    "right triangle": draw_right_triangle,
    "equilateral triangle": draw_equilateral_triangle,
    "rhombus": draw_rhombus
}

current_color = "white"
current_shape = "line"
drawing = False
last_pos = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check for color button clicks
            for button, color in color_buttons:
                if button.collidepoint(event.pos):
                    current_color = color
                    break
            
            # Check for shape button clicks 
            for button, shape in shape_buttons:
                if button.collidepoint(event.pos):
                    current_shape = shape
                    break 

            if clear_button.collidepoint(event.pos):
                screen.fill(colors["white"])
            drawing = True
            last_pos = event.pos
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                if current_shape == "line":
                    pygame.draw.line(screen, colors[current_color], last_pos, event.pos, 15)
                else:
                    shape_functions[current_shape](screen, current_color, last_pos, event.pos)
                last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False

    # --- Drawing buttons --- 
    for button, color in color_buttons:
        pygame.draw.rect(screen, colors[color], button)

    for button, shape in shape_buttons:
        pygame.draw.rect(screen, colors["black"], button)
        # Add text to shape buttons 
        font = pygame.font.SysFont(None, 15)
        text = font.render(shape[0], True, colors["white"])  # First letter of shape name
        text_rect = text.get_rect(center=button.center)
        screen.blit(text, text_rect) 

    # Draw clear button
    pygame.draw.rect(screen, colors["black"], clear_button)
    font = pygame.font.SysFont(None, 20)
    text = font.render("clear", True, colors["white"])
    text_rect = text.get_rect(center=clear_button.center)
    screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()