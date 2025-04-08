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
        if not dictionary.has_prefix(current_word.lower()):
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

# def find_words_with_positions(grid, dictionary, max_length=16, min_length=4):
#     """
#     Perform DFS from every cell in the grid to find valid words along with their positions.

#     Parameters:
#         grid (list[list[str]]): A 2D list representing the 6x8 letter grid.
#         dictionary (Dictionary): A Trie-based dictionary with `is_word` and `has_prefix`.
#         max_length (int): Maximum allowed word length to prevent excessive recursion.
#         min_length (int): Minimum word length required.

#     Returns:
#         list: A list of tuples (word, path), where 'word' is valid, and 'path' contains grid positions.
#     """
#     rows, cols = len(grid), len(grid[0])
#     found_words = []
#     visited = [[False] * cols for _ in range(rows)]  # Faster than a set

#     def dfs(r, c, node, path, word):
#         """
#         Depth-first search exploring valid words in the Trie.

#         Parameters:
#             r, c: Current grid position.
#             node: Current TrieNode.
#             path: List of visited positions.
#             word: The accumulated word.
#         """
#         if node.is_word and len(word) >= min_length:
#             found_words.append((word, path))
#             node.is_word = False  # Prevent duplicate words

#         # Stop if word is too long
#         if len(word) > max_length:
#             return

#         # Mark as visited
#         visited[r][c] = True

#         # Explore all 8 directions
#         for dr, dc in [(-1, -1), (-1, 0), (-1, 1),
#                        (0, -1),         (0, 1),
#                        (1, -1), (1, 0), (1, 1)]:
#             nr, nc = r + dr, c + dc
#             if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
#                 next_char = grid[nr][nc].lower()
#                 if next_char in node.children:
#                     dfs(nr, nc, node.children[next_char], path + [(nr, nc)], word + next_char)

#         # Unmark visited for backtracking
#         visited[r][c] = False

#     # Start DFS from each grid cell if it exists in the Trie root
#     for r in range(rows):
#         for c in range(cols):
#             char = grid[r][c].lower()
#             if char in dictionary.root.children:
#                 dfs(r, c, dictionary.root.children[char], [(r, c)], char)

#     return found_words
