import json
import os


def record_solution_json(solution, filename="solution.json"):
    """
    Write the solution to a JSON file.

    Parameters:
        solution (list): List of tuples (word, positions, score).
        filename (str): File name to store the JSON.
    """
    # Convert tuples to dicts for clarity.

    output_dir = "out"
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)

    sol_list = [
        {"word": word, "positions": positions, "score": score, "ranking": i}
        for word, positions, score, i in solution
    ]
    with open(file_path, "w") as f:
        json.dump(sol_list, f, indent=2)
