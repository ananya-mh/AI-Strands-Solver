#The visualizer file that gives us the pygame output without animations.

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw_grid_with_words(grid, found_words, top_words, save_path=None):
    rows, cols = len(grid), len(grid[0])
    fig, ax = plt.subplots(figsize=(cols, rows))

    for r in range(rows):
        for c in range(cols):
            ax.add_patch(patches.Rectangle((c, rows - r - 1), 1, 1, fill=False, edgecolor='black'))
            ax.text(c + 0.5, rows - r - 0.5, grid[r][c], va='center', ha='center', fontsize=14)

    seen_words = set()
    unique_words = []
    for word, positions, *_ in found_words:
        if word not in seen_words:
            seen_words.add(word)
            unique_words.append((word, positions))

    color_map = plt.cm.get_cmap("tab10", len(unique_words))
    for i, (word, positions) in enumerate(unique_words):
        for r, c in positions:
            ax.add_patch(
                patches.Rectangle(
                    (c, rows - r - 1), 1, 1,
                    fill=True, color=color_map(i), alpha=0.3
                )
            )
        if len(positions) > 1:
            coords = [(c + 0.5, rows - r - 0.5) for r, c in positions]
            xs, ys = zip(*coords)
            ax.plot(xs, ys, color=color_map(i), linewidth=2)

    fig.subplots_adjust(right=0.65) 

    side_ax = fig.add_axes([0.67, 0.1, 0.3, 0.8])  

    side_ax.axis('off')
    side_ax.set_title("Top Ranked Words", fontsize=12)
    seen_top = set()
    display_top = []
    for word, _, score in top_words:
        if word not in seen_top:
            seen_top.add(word)
            display_top.append((word, score))
        if len(display_top) >= 10:
            break
    for i, (word, score) in enumerate(display_top):
        side_ax.text(0, 1 - 0.08 * i, f"{word} ({score:.2f})", fontsize=10)

    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect("equal")

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    else:
        plt.show()
