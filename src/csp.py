import sys
sys.setrecursionlimit(1000000)

class ExactCoverSolver:

    def __init__(self, candidates, grid_rows, grid_cols, target_word_count=None):
        self.candidates = candidates
        self.grid_rows = grid_rows
        self.grid_cols = grid_cols
        self.grid_size = grid_rows * grid_cols
        self.solution = []
        self.covered = set()
        self.target_word_count = target_word_count

    def solve(self):
        if self._backtrack(0):
            return self.solution
        else:
            return None

    def _backtrack(self, index):
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

        if index >= len(self.candidates):
            return False

        word, positions, score = self.candidates[index]

        if any(pos in self.covered for pos in positions):
            return self._backtrack(index + 1)

        self.solution.append((word, positions, score, index))
        for pos in positions:
            self.covered.add(pos)

        if self._backtrack(index + 1):
            return True

        self.solution.pop()
        for pos in positions:
            self.covered.remove(pos)

        return self._backtrack(index + 1)
