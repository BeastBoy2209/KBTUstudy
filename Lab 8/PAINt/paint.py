import pygame

colors = {
    "green": (0, 255, 0),
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "black": (0, 0, 0),
    "white": (255, 255, 255),
}

pygame.init()

width, height = 500, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Paint")

button_width, button_height = 50, 50
button_margin = 10
buttons = []
for i, color in enumerate(colors):
    x = button_margin + i * (button_width + button_margin)
    y = button_margin
    button = pygame.Rect(x, y, button_width, button_height)
    buttons.append((button, color))

clear_button = pygame.Rect(width - button_width - button_margin, button_margin, button_width, button_height)

current_color = "white"
drawing = False
last_pos = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button, color in buttons:
                if button.collidepoint(event.pos):
                    current_color = color
                    break
            if clear_button.collidepoint(event.pos):
                screen.fill(colors["white"])

            drawing = True
            last_pos = event.pos
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                pygame.draw.line(screen, colors[current_color], last_pos, event.pos, 3)
                last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False

    for button, color in buttons:
        pygame.draw.rect(screen, colors[color], button)

    pygame.draw.rect(screen, colors["black"], clear_button)
    font = pygame.font.SysFont(None, 20)
    text = font.render("clear", True, colors["white"])
    text_rect = text.get_rect(center=clear_button.center)
    screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()