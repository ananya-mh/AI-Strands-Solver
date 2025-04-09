from heapq import heappush, heappop
import time

def find_words_with_positions(grid, dictionary, max_length=16, min_length=4, beam_width=200):
    """
    Perform Beam Search from every cell to find valid words.
    
    Args:
        grid (list[list[str]]): 2D grid of letters.
        dictionary (Dictionary): Trie-based dictionary.
        max_length (int): Max word length.
        min_length (int): Min word length.
        beam_width (int): Number of top paths to keep at each step.
    
    Returns:
        list: [(word, path), ...] where path is list of (r, c) positions.
    """
    rows, cols = len(grid), len(grid[0])
    found_words = []

    def heuristic_score(word):
        """Optional: Prioritize prefixes more likely to lead to theme words."""
        # Example: Give higher scores to prefixes in bird-related terms.
        bird_prefixes = {"bir", "fla", "wad", "egr", "spo"}
        return 1.0 if any(word.startswith(p) for p in bird_prefixes) else 0.0
    start = time.time()
    for start_r in range(rows):
        for start_c in range(cols):
            # Priority queue: (-score, word, path, visited)
            # Using negative score for min-heap behavior.
            beam = [ (0.0, grid[start_r][start_c], [(start_r, start_c)], {(start_r, start_c)}) ]

            while beam:
                next_beam = []
                for _ in range(min(beam_width, len(beam))):
                    score, word, path, visited = heappop(beam)
                    score = -score  # Convert back to positive

                    # Check if current word is valid.
                    if len(word) >= min_length and dictionary.is_word(word):
                        found_words.append((word, path))

                    # Stop if word exceeds max length.
                    if len(word) >= max_length:
                        continue

                    # Explore neighbors.
                    r, c = path[-1]
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0:
                                continue  # Skip current cell.
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                                new_word = word + grid[nr][nc]
                                if dictionary.has_prefix(new_word):
                                    new_score = score + heuristic_score(new_word)
                                    new_path = path + [(nr, nc)]
                                    new_visited = visited | {(nr, nc)}
                                    heappush(next_beam, (-new_score, new_word, new_path, new_visited))

                beam = next_beam
    print((time.time() - start))
    return found_words