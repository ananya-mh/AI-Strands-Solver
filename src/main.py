from .agent import StrandsAgent
from .utils import record_solution_json


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
    g2 = spangram2, test2, None

    # Initialize the Strands agent.
    # You can optionally pass a path to a dictionary file; otherwise, a default list is used.
    agent = StrandsAgent(g2, dictionary_file="words_dictionary.json", verbose=True)

    # Solve the grid and print the found words.
    found_words = agent.solve()
    print("Found words:")
    for word in sorted(found_words):
        print(word)
    if found_words:
        record_solution_json(found_words, f"{g1[0]}.json")


if __name__ == "__main__":
    main()
