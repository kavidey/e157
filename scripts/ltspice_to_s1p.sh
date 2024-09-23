#!/bin/bash

# filename: ltspice_to_s1p.sh
# author: Diego Herrera Vicioso dherreravicioso@hmc.edu 9/25/2023
# This script converts exported LTspice text data to a Touchstone .s1p format usable
# in Python scikit-rf and MATLAB.
#
# Usage:
# ./ltspice_to_s1p.sh filename.txt
#
# To see the options and descriptions, use:
# ./ltspice_to_s1p.sh -h

show_help() {
    echo "Script to turn .txt files exported from LTspice into .s1p files that can be used in MATLAB or scikit-rf to plot Smith Charts."
    echo "This script is designed to work when the .txt file contains a column with the frequencies and two additional columns: Re(gamma) and Im(gamma)."
    echo "Usage: ./ltspice_to_s1p.sh filename.txt"
}

# Check for help option
if [ "$1" == "-h" ]; then
    show_help
    exit 0
fi

# Check if a filename is provided
if [ -z "$1" ]; then
    echo "Error: No filename provided"
    show_help
    exit 1
fi

# Extract the filename
filename="$PWD/$1"

# Check if the file has .txt extension
if [[ "$filename" != *.txt ]]; then
    echo "Error: Input file is not a .txt file"
    exit 1
fi

# Read the input file and process it
output_filename="${filename%.txt}.s1p"

{
    # Read and modify the first line
    IFS= read -r first_line
    echo "# Hz S RI R 50"

    # Process the rest of the file
    while IFS= read -r line
    do
        # Replace commas with spaces
        echo "$line" | tr ',' ' '
    done
} < "$filename" > "$output_filename"

echo "Conversion complete: $output_filename"
