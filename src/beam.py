#This file was used for beam search based comparison

from heapq import heappush, heappop
import time

def find_words_with_positions(grid, dictionary, max_length=16, min_length=4, beam_width=200):
    rows, cols = len(grid), len(grid[0])
    found_words = []

    def heuristic_score(word):
        bird_prefixes = {"bir", "fla", "wad", "egr", "spo"}
        return 1.0 if any(word.startswith(p) for p in bird_prefixes) else 0.0
    start = time.time()
    for start_r in range(rows):
        for start_c in range(cols):
            beam = [ (0.0, grid[start_r][start_c], [(start_r, start_c)], {(start_r, start_c)}) ]

            while beam:
                next_beam = []
                for _ in range(min(beam_width, len(beam))):
                    score, word, path, visited = heappop(beam)
                    score = -score  

                    if len(word) >= min_length and dictionary.is_word(word):
                        found_words.append((word, path))

                    if len(word) >= max_length:
                        continue

                    r, c = path[-1]
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0:
                                continue  
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