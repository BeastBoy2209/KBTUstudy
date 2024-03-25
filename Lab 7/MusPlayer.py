import pygame
import os

pygame.mixer.init()

KEY_PLAY_PAUSE = pygame.K_SPACE
KEY_STOP = pygame.K_ESCAPE
KEY_NEXT = pygame.K_RIGHT
KEY_PREVIOUS = pygame.K_LEFT

def play_song(filepath):
    try:
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()
    except pygame.error:
        print(f"Error loading song: {filepath}")

def handle_events(event):
    if event.type == pygame.KEYDOWN:
        if event.key == KEY_PLAY_PAUSE:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()
        elif event.key == KEY_STOP:
            pygame.mixer.music.stop()
        elif event.key == KEY_NEXT:
            print("Next Song (not implemented yet)")
        elif event.key == KEY_PREVIOUS:
            print("Previous Song (not implemented yet)")

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

current_song = "path/to/your/song.mp3"
play_song(current_song)

play_button = pygame.Rect(50, 50, 50, 50)  # x, y, width, height
stop_button = pygame.Rect(150, 50, 50, 50)  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(event.pos):
                pygame.mixer.music.unpause()
            elif stop_button.collidepoint(event.pos):
                pygame.mixer.music.stop()
        handle_events(event)

    pygame.draw.rect(screen, (0, 255, 0), play_button)  #Play
    pygame.draw.rect(screen, (255, 0, 0), stop_button)  #Stop

    pygame.display.flip()

pygame.quit()
