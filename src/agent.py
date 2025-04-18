#Main agent file that is used to solve the Strands Puzzle
import json
from dictionary import Dictionary
from dfs import find_words_with_positions
from csp import ExactCoverSolver
from ranking import rank_candidates


class StrandsAgent:
    def __init__(self, game, dictionary_file=None, verbose=False):
        """
        Initialize the Strands agent with a given grid and dictionary.

        Parameters:
            grid (list[list[str]]): A 2D list representing the 6x8 letter grid.
            dictionary_file (str, optional): Path to a file containing dictionary words.
                                             Supports JSON files (e.g., words_dictionary.json)
                                             or plain text files (one word per line).
        """
        self.theme, self.grid, self.word_count = game
        self.verbose = verbose
        self.dictionary = self.load_dictionary(dictionary_file)

    def load_dictionary(self, dictionary_file):
        """
        Load dictionary words from a file.

        - For a JSON file (e.g., words_dictionary.json), the file is expected to be a dictionary
          where each key is a word and the value is 1.
        - For a plain text file, it expects one word per line.

        Returns:
            Dictionary: An instance of Dictionary (Trie-based) populated with words.
        """
        if self.verbose:
            print("Loading Dictionary...")
        words = []
        if dictionary_file:
            try:
                if dictionary_file.endswith(".json"):
                    with open(dictionary_file, "r") as f:
                        json_dict = json.load(f)
                        # Use the keys of the JSON dictionary as the word list.
                        words = list(json_dict.keys())
                else:
                    with open(dictionary_file, "r") as f:
                        words = [line.strip().lower() for line in f if line.strip()]
            except Exception as e:
                print(f"Error loading dictionary from file: {e}")
        else:
            # Default list for testing purposes.
            words = ["word", "words", "sword", "ward", "rod", "wordy", "world"]
        return Dictionary(words)

    def find_words_with_positions(self):
        """
        Generate candidate words from the grid along with their positions.

        Returns:
            list: A list of tuples (word, positions) generated by the DFS algorithm.
        """
        if self.verbose:
            print("Finding Words and Positions...")
        return find_words_with_positions(self.grid, self.dictionary)

    def solve(self):
        """
        Generate candidate words with positions and then use the CSP solver to select a valid
        combination that covers the grid exactly (i.e., every cell is used once without overlap).

        Returns:
            list or None: A list of tuples (word, positions) that form a valid Strands solution,
                          or None if no solution is found.
        """
        # Generate candidate words with positions.

        candidates = self.find_words_with_positions()

        if self.verbose:
            print(f"\tNumber of candidates found: {len(candidates)}")
            print("Ranking...")
        ranked = rank_candidates(
            candidates,
            self.theme,
            weight_sim=0.5,
            weight_lm=0.5,
            weight_freq=0,
            verbose=True,
        )
        print(ranked[:100])

        # Create the CSP solver instance for a 6x8 grid.
        solver = ExactCoverSolver(
            ranked,
            grid_rows=len(self.grid),
            grid_cols=len(self.grid[0]),
            target_word_count=self.word_count,
        )
        if self.verbose:
            print("Solving...")
        solution = solver.solve()
        return solution
