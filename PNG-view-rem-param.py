#!/bin/env python3
 
# add args
#current version, reads all png in this directory, and dumps in ParametersRemoved
import os
from pathlib import Path
from PIL import Image

inputdir = Path(".")
outputdir = Path("ParametersRemoved")

# Check if input directory exists, otherwise exit
if not inputdir.exists() or not inputdir.is_dir():
    print("Input directory does not exist")
    exit()

# Create output directory if it doesn't exist
if not outputdir.exists() or not outputdir.is_dir():
    outputdir.mkdir()

# Iterate over all PNG files in the input directory and process them
for file in inputdir.glob("*.png"):
    if not file.is_file():
        # Skip if it's not a file
        continue

    # Generate the output file path
    outfile = outputdir / file.name

    if outfile.exists():
        # Skip if output file already exists
        print(f"File already processed: {outfile}")
        continue

    try:
        with Image.open(file) as img:
            # Remove the "parameters" attribute from the PNG file
            try:
                img.info.pop("parameters")
            except Exception as e:
                print(f"Failed to pop parameters, was this already done? {e}")
            img.save(outfile)
            print(f"Processed file: {file} -> {outfile}")
    except Exception as e:
        print(f"Failed to process file: {file} -> {e}")
