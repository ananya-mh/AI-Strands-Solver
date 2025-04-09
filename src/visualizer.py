# visualizer.py
import pygame
from typing import List, Tuple

def visualize_grid(
    grid: List[List[str]],
    word_paths: List[Tuple[str, List[Tuple[int, int]]]],  # (word, path)
    title: str = "Strands Solver"
):
    """Minimal PyGame visualization for Strands solutions."""
    pygame.init()
    cell_size = 80
    rows, cols = len(grid), len(grid[0])
    
    # Set up display
    screen = pygame.display.set_mode((cols * cell_size, rows * cell_size + 50))
    pygame.display.set_caption(title)
    font = pygame.font.SysFont('Arial', 24)
    
    # Colors
    COLORS = {
        'bg': (240, 240, 240),
        'text': (0, 0, 0),
        'highlight': (100, 200, 100),
        'grid': (200, 200, 200)
    }
    
    current_word = 0
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    current_word = (current_word + 1) % len(word_paths)
                elif event.key == pygame.K_LEFT:
                    current_word = (current_word - 1) % len(word_paths)
        
        # Draw grid
        screen.fill(COLORS['bg'])
        for r in range(rows):
            for c in range(cols):
                pygame.draw.rect(screen, COLORS['grid'], (c*cell_size, r*cell_size, cell_size, cell_size), 1)
                text = font.render(grid[r][c], True, COLORS['text'])
                screen.blit(text, (c*cell_size + 30, r*cell_size + 30))
        
        # Highlight current word path
        if word_paths:
            word, path = word_paths[current_word]
            for (r, c) in path:
                pygame.draw.rect(screen, COLORS['highlight'], (c*cell_size, r*cell_size, cell_size, cell_size), 4)
            
            # Display current word
            status = font.render(f"{current_word+1}/{len(word_paths)}: {word}", True, (0, 0, 0))
            screen.blit(status, (10, rows * cell_size + 10))
        
        pygame.display.flip()
    
    pygame.quit()