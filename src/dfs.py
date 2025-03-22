def find_words_with_positions(grid, dictionary, max_length=16, min_length=4):
    """
    Perform DFS from every cell in the grid to find valid words along with their positions.

    Parameters:
        grid (list[list[str]]): A 2D list representing the 6x8 letter grid.
        dictionary (Dictionary): An instance of Dictionary (Trie-based) that provides
                                 is_word and has_prefix methods.
        max_length (int): Maximum allowed word length to prevent excessive recursion.
        min_length (int): Minimum word length required (default is 4).

    Returns:
        list: A list of tuples (word, path) where 'word' is a valid candidate word and
              'path' is a list of grid positions (tuples) that form the word.

    The DFS continues exploring even after finding a valid word to capture words that share
    common prefixes (e.g., "word" and "words").
    """
    rows = len(grid)
    cols = len(grid[0])
    found_words = []

    def dfs(r, c, current_word, visited, path):
        # Stop if current_word exceeds max_length.
        if len(current_word) > max_length:
            return

        # Prune search if no word in the dictionary starts with the current prefix.
        if not dictionary.has_prefix(current_word):
            return

        # Record the word if it meets the minimum length and is a valid word.
        if len(current_word) >= min_length and dictionary.is_word(current_word):
            found_words.append((current_word, path))

        # Explore all 8 adjacent cells.
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue  # Skip the current cell.
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    dfs(
                        nr,
                        nc,
                        current_word + grid[nr][nc],
                        visited | {(nr, nc)},
                        path + [(nr, nc)],
                    )

    # Start DFS from every cell in the grid.
    for r in range(rows):
        for c in range(cols):
            dfs(r, c, grid[r][c], {(r, c)}, [(r, c)])

    return found_words
