#!/usr/bin/env bash
# compare.sh
# A simple bash wrapper to execute the comparison script via uv easily.

echo "Starting Comparison Script..."
# Let uv run the actual python comparison logic natively in the managed virtualenv
python -m uv run compare_loras.py
