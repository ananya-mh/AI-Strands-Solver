from agent import StrandsAgent
from utils import record_solution_json
from visualizer import visualize_grid


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

    wp = "Sign Language"
    spangram3 = "ASTROLOGY"
    test3 =   [['R', 'G', 'I', 'Y', 'B', 'U'],
               ['I', 'S', 'N', 'G', 'L', 'L'],
               ['V', 'A', 'C', 'O', 'A', 'C'],
               ['L', 'E', 'S', 'L', 'R', 'H'],
               ['P', 'I', 'R', 'O', 'T', 'E'],
               ['R', 'O', 'T', 'I', 'W', 'R'],
               ['O', 'N', 'S', 'G', 'N', 'S'],
               ['C', 'S', 'A', 'O', 'A', 'T']]
    
    count3 = 8
    ans3 = [ "ASTROLOGY","ARCHER",
    "BULL",
    "GOAT",
    "SCALES",
    "SCORPION",
    "TWINS",
    "VIRGIN"
     ]
    g3 = spangram3, test3, None


    # Initialize the Strands agent.
    # You can optionally pass a path to a dictionary file; otherwise, a default list is used.
    agent = StrandsAgent(g2, dictionary_file="words_dictionary.json", verbose=True)
    # found_words = agent.solve()
    
#     print("Found words:")
#     for word in sorted(found_words):
#         print(word)
    
#     if found_words:
#         record_solution_json(found_words, f"{g2[0]}.json")
        
#         # Add these 2 lines for visualization (with dummy paths)
#         dummy_paths = [([(0,0)] * len(w)) for w in found_words]  # Replace with real paths if available
#         visualize_grid(test3, list(zip(found_words, dummy_paths)), title=g2[0])

# if __name__ == "__main__":
#     main()
    
    # Solve the grid and print the found words.
    found_words = agent.solve()
    print("Found words:")
    for word in sorted(found_words):
        print(word)
    # if found_words:
    #     record_solution_json(found_words, f"{g2[0]}.json")


if __name__ == "__main__":
    main()
