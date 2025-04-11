# import sys
# sys.setrecursionlimit(1000000)

# class ExactCoverSolver:
#     """
#     A simple backtracking CSP solver for the exact cover problem.
#     Given a list of candidate words (each as a tuple: (word, positions))
#     and a grid (specified by its number of rows and columns), this solver
#     finds a subset of candidates such that every cell is covered exactly once.
#     """

#     def __init__(self, candidates, grid_rows, grid_cols, target_word_count=None):
#         self.candidates = candidates
#         # self.candidates = sorted(candidates, key=lambda x: -x[2])
#         self.grid_rows = grid_rows
#         self.grid_cols = grid_cols
#         self.grid_size = grid_rows * grid_cols
#         self.solution = []
#         self.covered = set() 
#         self.target_word_count = target_word_count

#     def solve(self):
#         # Optionally, sort candidates (e.g., by length or by number of positions) to improve performance.
#         # For now, we use the list in its current order.
#         if self._backtrack(0):
#             return self.solution
#         else:
#             return None

#     def _backtrack(self, index):
#         # If all grid cells are covered, we've found a solution.
#         if len(self.covered) == self.grid_size:
#             if (
#                 self.target_word_count is None
#                 or len(self.solution) == self.target_word_count
#             ):
#                 return True
#             else:
#                 return False

#         if (
#             self.target_word_count is not None
#             and len(self.solution) >= self.target_word_count
#         ):
#             return False

#         # If we've tried all candidates, fail this branch.
#         if index >= len(self.candidates):
#             return False

#         # Get the current candidate.
#         word, positions, score = self.candidates[index]

#         # Check if any position in this candidate is already covered.
#         if any(pos in self.covered for pos in positions):
#             # Skip this candidate and move to the next.
#             return self._backtrack(index + 1)

#         # Choose this candidate.
#         self.solution.append((word, positions, score, index))
#         for pos in positions:
#             self.covered.add(pos)

#         # Continue searching with the next candidate.
#         if self._backtrack(index + 1):
#             return True

#         # Backtrack: remove this candidate and try skipping it.
#         self.solution.pop()
#         for pos in positions:
#             self.covered.remove(pos)

#         return self._backtrack(index + 1)

import sys
sys.setrecursionlimit(1000000)

class ExactCoverSolver:
    """
    A simple backtracking CSP solver for the exact cover problem.
    Given a list of candidate words (each as a tuple: (word, positions))
    and a grid (specified by its number of rows and columns), this solver
    finds a subset of candidates such that every cell is covered exactly once.
    """

    def __init__(self, candidates, grid_rows, grid_cols, target_word_count=None):
        self.candidates = candidates
        self.grid_rows = grid_rows
        self.grid_cols = grid_cols
        self.grid_size = grid_rows * grid_cols
        self.solution = []
        self.covered = set()
        self.target_word_count = target_word_count

    def solve(self):
        # Optionally, sort candidates (e.g., by length or by number of positions) to improve performance.
        # For now, we use the list in its current order.
        if self._backtrack(0):
            return self.solution
        else:
            return None

    def _backtrack(self, index):
        # If all grid cells are covered, we've found a solution.
        if len(self.covered) == self.grid_size:
            if (
                self.target_word_count is None
                or len(self.solution) == self.target_word_count
            ):
                return True
            else:
                return False

        if (
            self.target_word_count is not None
            and len(self.solution) >= self.target_word_count
        ):
            return False

        # If we've tried all candidates, fail this branch.
        if index >= len(self.candidates):
            return False

        # Get the current candidate.
        word, positions, score = self.candidates[index]

        # Check if any position in this candidate is already covered.
        if any(pos in self.covered for pos in positions):
            # Skip this candidate and move to the next.
            return self._backtrack(index + 1)

        # Choose this candidate.
        self.solution.append((word, positions, score, index))
        for pos in positions:
            self.covered.add(pos)

        # Continue searching with the next candidate.
        if self._backtrack(index + 1):
            return True

        # Backtrack: remove this candidate and try skipping it.
        self.solution.pop()
        for pos in positions:
            self.covered.remove(pos)

        return self._backtrack(index + 1)