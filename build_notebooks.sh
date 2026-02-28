#!/usr/bin/env bash

set -euo pipefail

# Optional: base directory (default = current directory)
BASE_DIR="${1:-.}"

echo "Searching for .ipynb files in: $BASE_DIR"
echo

# Find all .ipynb files recursively
find "$BASE_DIR" -type f -name "*.ipynb" | while read -r notebook; do
    echo "Building $notebook"
    jupyter-book build "$notebook"
    echo "Done: $notebook"
    echo
done

echo "All notebooks processed."