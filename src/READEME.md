# Strands Word Puzzle Solver

An intelligent solver for the NYT Strands puzzle. The game is a word puzzle where the objective is to fill a grid with words from a predefined list, ensuring no overlaps and fitting the theme of the puzzle. 

## Background: The NYT Strands Game

The **Strands** game, featured in *The New York Times*, is a word puzzle that challenges players to find valid words within a grid of letters. The puzzle is designed with a unique set of rules and requires both linguistic intuition and spatial awareness to solve.

### Puzzle Layout
The grid is typically composed of letters arranged in rows and columns, and the goal is to form valid words by selecting adjacent letters. The words can be formed by connecting letters in any direction: horizontally, vertically, or diagonally. Each letter in the grid can only be used once per word, and the words must be a minimum of three letters long.

### Thematic Coherence
In Strands, there is also an emphasis on the thematic relevance of the words formed. Words that are thematically related or follow a specific pattern contribute more to the puzzle’s solution. This aspect of the game makes it more challenging and engaging, as it requires players to consider the context and meaning behind the words formed, beyond just letter arrangement.

### Objective
The objective of the game is to find all the possible valid words that can be constructed from the grid, while adhering to the spatial and thematic rules. Once the player identifies all valid words, they must ensure these words fit the constraints of the puzzle, covering the grid efficiently without overlap or leaving any empty spaces.

The challenge in solving Strands lies in finding the correct set of words that not only fit within the grid but also match a thematic pattern. This makes it an interesting problem for computational approaches, as both word generation and optimization are involved.

### Technical Approach

In this project, we leveraged advanced techniques such as **depth-first search (DFS)**, **Sentence Transformers (SBERT)**, and **constraint solvers** to tackle this problem. By incorporating these methods, our solver aims to replicate the process of solving the Strands puzzle, automatically finding the best word combinations to fit the grid while considering both word validity and thematic relevance.


1. **Trie + DFS Approach**: This stage extracts all possible valid words from the given word grid using a trie-based depth-first search (DFS).
2. **Sentence Transformer (SBERT)**: The extracted words are ranked by thematic coherence using SBERT, a model for generating sentence embeddings that capture the meaning of words in context.
3. **Constraint Satisfaction Problem (CSP) Solver**: Finally, a CSP solver selects the optimal subset of words that satisfy the spatial arrangement constraints of the grid.

In addition to the primary approach, alternative methods such as **Dancing Links (DLX)** and **Genetic Algorithms** were explored to handle different trade-offs in efficiency and constraint enforcement. Each method contributes to finding solutions that balance computational performance and constraint satisfaction.



## Requirements

- Python 3.x
- Required Python Libraries:
  - `numpy`
  - `pandas`
  - `torch` (for transformer models)
  - `matplotlib`
  - `scikit-learn`
  - `transformers`
  - `torchvision`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/strands-word-puzzle-solver.git
    ```

2. Navigate to the project directory:
    ```bash
    cd strands-word-puzzle-solver
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Solver

1. Open the command line in the project directory.
2. Run the main solver script to solve the puzzle:
    ```bash
    python main.py
    ```