"""One Line, One Laugh - make.fun entry.

Writes a single self-contained joke to entry.txt (1-140 chars).
The grader runs this read-only at /bot and sets MAKEFUN_OUTPUT_DIR,
so output goes there when set, falling back to the script directory.
"""

import os

JOKE = "My Roomba unionized. Now it only cleans the rooms it believes in."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
