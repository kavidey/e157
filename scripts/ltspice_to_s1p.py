"""
filename: ltspice_to_s1p.py
author: Diego Herrera Vicioso dherreravicioso@hmc.edu 9/25/2023

This script converts exported LTspice text data to a Touchstone .s1p format usable
in Python scikit-rf and MATLAB. 

Usage: 
python ltspice_to_s1p.py filename.txt

To see the options and descriptions, use
python ltspice_to_s1p.py -h

"""

import argparse

def main():
    # take command line input for a filename
    parser = argparse.ArgumentParser(description="Script to turn .txt files exported from LTspice into .s1p files that can be used in \
                                     MATLAB or scikit-rf to plot Smith Charts. This script is designed to work when the .txt file contains \
                                     a column with the frequencies and two additional columns: Re(gamma) and Im(gamma).")
    
    parser.add_argument('filename', help="Name of the .txt file containing S11/gamma data in complex cartesian form")
    args = parser.parse_args()

    # check for .txt file input
    if ('.txt' != args.filename[-4:]):
        raise Exception("Input file is not a .txt file")

    with open(args.filename, 'r') as input_file:
        line_array = input_file.readlines()

        # Change first line to s1p format
        line_array[0] = "# Hz S RI R 50\n"

        # LTspice exports with commas, change to spaces
        for idx, line in enumerate(line_array):
            line_array[idx] = line.replace(",", " ")

    s1p_filename = args.filename.replace(".txt", ".s1p")

    # write to s1p file
    with open(s1p_filename, 'w') as output_file: 
        output_file.writelines(line_array)


if __name__ == "__main__":
    main()