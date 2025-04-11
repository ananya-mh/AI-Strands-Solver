import pygame
from agent import StrandsAgent

# Initialize Pygame
pygame.init()

# Constants
CELL_SIZE = 50
MARGIN = 5
GRID_ROWS = 8
GRID_COLS = 6
WIDTH = GRID_COLS * (CELL_SIZE + MARGIN) + 300
HEIGHT = GRID_ROWS * (CELL_SIZE + MARGIN) + 100

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG = (30, 30, 30)
HIGHLIGHT = (255, 223, 88)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Strands Puzzle Viewer")
FONT = pygame.font.SysFont("arial", 28)
SMALL_FONT = pygame.font.SysFont("arial", 22)

# Puzzle data
theme = "Wetland Patrol"
spangram = "WADINGBIRD"
grid = [
    ["N", "E", "I", "B", "I", "L"],
    ["R", "T", "B", "R", "N", "L"],
    ["T", "B", "G", "S", "D", "O"],
    ["I", "O", "N", "O", "P", "O"],
    ["G", "I", "T", "K", "R", "T"],
    ["N", "F", "D", "S", "E", "E"],
    ["I", "L", "A", "B", "G", "R"],
    ["M", "A", "W", "I", "I", "S"],
]

# Solve using your agent
agent = StrandsAgent((spangram, grid, None), dictionary_file="words_dictionary.json", verbose=False)
found_words = agent.solve()


def draw_grid():
    highlight_coords = set()
    for item in found_words:
        if isinstance(item, tuple) and len(item) == 2:
            _, coords = item
            highlight_coords.update(coords)

    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            x = col * (CELL_SIZE + MARGIN) + 40
            y = row * (CELL_SIZE + MARGIN) + 40

            rect_color = HIGHLIGHT if (row, col) in highlight_coords else WHITE
            pygame.draw.rect(screen, rect_color, (x, y, CELL_SIZE, CELL_SIZE))

            letter = grid[row][col]
            text = FONT.render(letter, True, BLACK)
            text_rect = text.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
            screen.blit(text, text_rect)



def draw_info():
    theme_text = SMALL_FONT.render(f"Theme: {theme}", True, WHITE)
    spangram_text = SMALL_FONT.render(f"Spangram: {spangram}", True, WHITE)
    found_text = SMALL_FONT.render("Found Words:", True, HIGHLIGHT)

    screen.blit(theme_text, (420, 30))
    screen.blit(spangram_text, (420, 60))
    screen.blit(found_text, (420, 100))

    y = 130
    for item in sorted(found_words):
        word = item if isinstance(item, str) else item[0]
        word_text = SMALL_FONT.render(str(word), True, WHITE)

        screen.blit(word_text, (420, y))
        y += 30


def main():
    running = True
    while running:
        screen.fill(BG)
        draw_grid()
        draw_info()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == "__main__":
    main()
