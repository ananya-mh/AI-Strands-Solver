class DLXNode:
    def __init__(self):
        self.left = self.right = self.up = self.down = self
        self.column = None
        self.row_id = -1
        self.row_count = 0  # Added row_count for column headers

class DLXSolver:
    def __init__(self, candidates, grid_rows, grid_cols, target_word_count=None):
        self.candidates = sorted(candidates, key=lambda x: -x[2])
        self.grid_rows = grid_rows
        self.grid_cols = grid_cols
        self.grid_size = grid_rows * grid_cols
        self.target_word_count = target_word_count
        # self.candidates = candidates  # Store candidates for solution mapping
        self.header = self.create_matrix()
        self.solution = []
        self.solution_nodes = []  # Sort by score descending

    def create_matrix(self):
        # Create header node
        header = DLXNode()
        columns = [header]
        
        # Create column headers for each grid cell
        for i in range(self.grid_size):
            col = DLXNode()
            col.row_id = i  # Column ID corresponds to grid cell
            columns.append(col)
            col.left = columns[-2]
            col.right = header
            columns[-2].right = col
            header.left = col
            col.column = col  # Column header points to itself
            col.row_count = 0  # Initialize row count for column
        
        # Add rows for each candidate word
        for idx, (word, positions, _) in enumerate(self.candidates):
            first_node = None
            for pos in positions:
                r, c = pos
                cell_num = r * self.grid_cols + c
                col = columns[cell_num + 1]  # +1 to skip header
                
                node = DLXNode()
                node.column = col
                node.row_id = idx  # Store candidate index
                
                # Link to other nodes in the same row
                if first_node:
                    node.left = first_node.left
                    node.right = first_node
                    first_node.left.right = node
                    first_node.left = node
                else:
                    first_node = node
                
                # Link to column
                node.up = col.up
                node.down = col
                col.up.down = node
                col.up = node
                col.row_count += 1  # Increment column row count
        
        return header

    def cover(self, col):
        # Remove column from header list
        col.right.left = col.left
        col.left.right = col.right
        
        # Remove all rows in this column from other columns they appear in
        row_node = col.down
        while row_node != col:
            right_node = row_node.right
            while right_node != row_node:
                right_node.down.up = right_node.up
                right_node.up.down = right_node.down
                right_node.column.row_count -= 1
                right_node = right_node.right
            row_node = row_node.down

    def uncover(self, col):
        # Reconnect all rows in this column to other columns
        row_node = col.up
        while row_node != col:
            left_node = row_node.left
            while left_node != row_node:
                left_node.column.row_count += 1
                left_node.down.up = left_node
                left_node.up.down = left_node
                left_node = left_node.left
            row_node = row_node.up
        
        # Reconnect column to header list
        col.right.left = col
        col.left.right = col

    def select_min_column(self):
        min_col = self.header.right
        current = min_col.right
        while current != self.header:
            if current.row_count < min_col.row_count:
                min_col = current
            current = current.right
        return min_col

    def search(self, k):
        if self.header.right == self.header:
            return True if (self.target_word_count is None or 
                          len(self.solution_nodes) == self.target_word_count) else False
        
        col = self.select_min_column()
        self.cover(col)
        
        row_node = col.down
        while row_node != col:
            self.solution_nodes.append(row_node)
            
            # Cover all columns this row intersects with
            right_node = row_node.right
            while right_node != row_node:
                self.cover(right_node.column)
                right_node = right_node.right
                
            if self.search(k + 1):
                return True
                
            # Backtrack
            self.solution_nodes.pop()
            left_node = row_node.left
            while left_node != row_node:
                self.uncover(left_node.column)
                left_node = left_node.left
                
            row_node = row_node.down
        
        self.uncover(col)
        return False

    def solve(self):
        print("dlx searching..")
        if self.search(0):
            # Convert node pointers back to original candidates
            solution_indices = {node.row_id for node in self.solution_nodes}
            return [self.candidates[i] for i in solution_indices]
        return None
