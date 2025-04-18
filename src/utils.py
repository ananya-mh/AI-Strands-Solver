#This file saves the solution as a json file.

import json
import os


def record_solution_json(solution, filename="solution.json"):


    output_dir = "out"
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)

    sol_list = [
        {"word": word, "positions": positions, "score": score, "ranking": i}
        for word, positions, score, i in solution
    ]
    with open(file_path, "w") as f:
        json.dump(sol_list, f, indent=2)
