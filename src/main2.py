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


DIRECTIONS = [  # 8 possible directions (including diagonals)
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1),  (1, 0), (1, 1)
]

COLORS = [
    (255, 99, 71),     # Tomato
    (135, 206, 250),   # LightSkyBlue
    (144, 238, 144),   # LightGreen
    (255, 182, 193),   # LightPink
    (221, 160, 221),   # Plum
    (255, 215, 0),     # Gold
    (64, 224, 208),    # Turquoise
    (255, 165, 0),     # Orange
]

def find_word_positions(grid, word):
    rows, cols = len(grid), len(grid[0])
    word = word[0].upper()

    def dfs(r, c, index, path, visited):
        if index == len(word):
            return path

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < rows and 0 <= nc < cols
                and (nr, nc) not in visited
                and grid[nr][nc] == word[index]
            ):
                new_path = dfs(nr, nc, index + 1, path + [(nr, nc)], visited | {(nr, nc)})
                if new_path:
                    return new_path
        return None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == word[0]:
                path = dfs(r, c, 1, [(r, c)], {(r, c)})
                if path:
                    return path
    return []

# Solve using your agent
agent = StrandsAgent((spangram, grid, None), dictionary_file="words_dictionary.json", verbose=False)
words = agent.solve()
found_words = [(word, find_word_positions(grid, word)) for word in words]

def draw_grid(words_to_draw):
    coord_color_map = {}
    for idx, (word, coords) in enumerate(words_to_draw):
        color = COLORS[idx % len(COLORS)]
        for coord in coords:
            coord_color_map[coord] = color

    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            x = col * (CELL_SIZE + MARGIN) + 40
            y = row * (CELL_SIZE + MARGIN) + 40

            rect_color = coord_color_map.get((row, col), WHITE)
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
    clock = pygame.time.Clock()
    running = True
    current_word_index = 0
    current_char_index = 0
    animation_timer = 0
    animation_delay = 200  # milliseconds between each character

    while running:
        screen.fill(BG)

        # Compute how many characters should be shown for each word
        animated_found_words = []
        for idx, (word, coords) in enumerate(found_words):
            if idx < current_word_index:
                animated_found_words.append((word, coords))
            elif idx == current_word_index:
                animated_found_words.append((word, coords[:current_char_index]))
                break
            else:
                break

        draw_grid(animated_found_words)
        draw_info()
        pygame.display.flip()

        animation_timer += clock.get_time()
        if animation_timer >= animation_delay:
            animation_timer = 0
            if current_word_index < len(found_words):
                word, coords = found_words[current_word_index]
                if current_char_index < len(coords):
                    current_char_index += 1
                else:
                    current_word_index += 1
                    current_char_index = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(60)

    pygame.quit()



if __name__ == "__main__":
    main()