import pygame
import sys
import os
import subprocess

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("PyPong Menu")
font = pygame.font.SysFont("Arial", 30)
small_font = pygame.font.SysFont("Arial", 20)

WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
RED = (255, 100, 100)
DARK = (20, 20, 20)

def file_exists_or_error(filepath):
    return os.path.isfile(filepath)

def draw_text_centered(text, y, font, color=WHITE):
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=(screen.get_width() // 2, y))
    screen.blit(surface, rect)
    return rect

def launch_script(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    if file_exists_or_error(filepath):
        pygame.quit()
        subprocess.run([sys.executable, filepath])
    else:
        print(f"Error: {filename} not found.")

running = True
while running:
    screen.fill(DARK)
    draw_text_centered("Welcome to PyPong!", 60, font, WHITE)
    single_rect = draw_text_centered("Single Player (AI)", 140, small_font, CYAN)
    two_rect = draw_text_centered("2 Player", 190, small_font, RED)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if single_rect.collidepoint(event.pos):
                launch_script("PyPong1Player.py")
            elif two_rect.collidepoint(event.pos):
                launch_script("PyPong2Player.py")
    pygame.draw.rect(screen, WHITE, single_rect.inflate(10, 10), 2)
    pygame.draw.rect(screen, WHITE, two_rect.inflate(10, 10), 2)
    pygame.draw.rect(screen, CYAN, single_rect.inflate(10, 10), 2)
    pygame.draw.rect(screen, RED, two_rect.inflate(10, 10), 2)
    pygame.time.Clock().tick(60)  
    pygame.display.flip()

pygame.quit()