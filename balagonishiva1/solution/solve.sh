#!/bin/bash
# Move to the directory where solve.sh is located, then go up to project root
cd "$(dirname "$0")/.."

# Ensure output.json is cleared from previous failed runs
rm -f output.json

# Execute script with explicit python3 call
python3 solution/fix_script.py || python solution/fix_script.py