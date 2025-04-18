#DFS file

def find_words_with_positions(grid, dictionary, max_length=16, min_length=4):
    rows = len(grid)
    cols = len(grid[0])
    found_words = []

    def dfs(r, c, current_word, visited, path):
        if len(current_word) > max_length:
            return

        if not dictionary.has_prefix(current_word):
            return

        if len(current_word) >= min_length and dictionary.is_word(current_word):
            found_words.append((current_word, path))

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue  
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    dfs(
                        nr,
                        nc,
                        current_word + grid[nr][nc],
                        visited | {(nr, nc)},
                        path + [(nr, nc)],
                    )

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, grid[r][c], {(r, c)}, [(r, c)])

    return found_words
