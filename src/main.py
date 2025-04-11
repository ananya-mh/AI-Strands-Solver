import sys
sys.setrecursionlimit(10000)

from agent import StrandsAgent
from utils import record_solution_json
from visualize_solver import draw_grid_with_words




def main():
    # Example 6x8 grid. Each inner list represents a row in the grid.
    theme = "grrr"
    spangram = "CROSSWORD"
    count = 7
    test = [
        ["Y", "K", "U", "R", "L", "Y"],
        ["N", "S", "D", "P", "E", "D"],
        ["A", "C", "X", "R", "E", "V"],
        ["R", "E", "O", "E", "O", "E"],
        ["D", "R", "I", "S", "V", "W"],
        ["C", "D", "E", "R", "S", "O"],
        ["Y", "M", "U", "K", "T", "U"],
        ["P", "R", "G", "Y", "H", "C"],
    ]
    g1 = spangram, test

    wp = "Wetland Patrol"
    spangram2 = "Wading Bird"
    test2 = [
        ["N", "E", "I", "B", "I", "L"],
        ["R", "T", "B", "R", "N", "L"],
        ["T", "B", "G", "S", "D", "O"],
        ["I", "O", "N", "O", "P", "O"],
        ["G", "I", "T", "K", "R", "T"],
        ["N", "F", "D", "S", "E", "E"],
        ["I", "L", "A", "B", "G", "R"],
        ["M", "A", "W", "I", "I", "S"],
    ]
    count2 = 8  # 7
    ans = ["WADINGBIRD", "BITTERN", "SPOONBILL", "FLAMINGO", "EGRET", "STORK", "IBIS"]
    g2 = spangram, test, None

    wp3 = "What's the buzz?"
    spangram3 = "Bumblebee"
    test_today = [
    ["A", "N", "T", "N", "A", "E"],
    ["R", "O", "E", "N", "W", "I"],
    ["A", "H", "T", "B", "G", "N"],
    ["X", "O", "D", "A", "S", "U"],
    ["E", "R", "M", "E", "E", "G"],
    ["N", "G", "N", "T", "O", "N"],
    ["I", "T", "S", "E", "M", "U"],
    ["E", "E", "B", "L", "B", "B"],
    ]
    g3 = spangram3, test_today, None


    # Initialize the Strands agent.
    # You can optionally pass a path to a dictionary file; otherwise, a default list is used.
    agent = StrandsAgent(g3, dictionary_file="words_dictionary.json", verbose=True)

    # Solve the grid and print the found words.
    found_words = agent.solve()
    print("Found words:")
    for word in sorted(found_words):
        print(word)

    if found_words:
        record_solution_json(found_words, f"{g1[0]}.json")

        # Visualize the result
        from ranking import rank_candidates
        from visualize_solver import draw_grid_with_words

        candidates = agent.find_words_with_positions()
        ranked = rank_candidates(
            candidates,
            agent.theme,
            weight_sim=0.5,
            weight_lm=0.5,
            weight_freq=0,
            verbose=False,
        )

        # Format found_words for visualization (strip index)
        found_word_viz = [(word, positions) for word, positions, _, _ in found_words]
        draw_grid_with_words(test_today, found_word_viz, ranked[:10])



if __name__ == "__main__":
    main()