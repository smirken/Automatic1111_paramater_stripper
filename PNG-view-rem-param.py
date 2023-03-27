#!/bin/env python3
 
# add args
#current version, reads all png in this directory, and dumps in ParametersRemoved
from dis import show_code
import os
from pathlib import Path
from PIL import Image
import argparse

outputdirname="ParametersRemoved"

parser = argparse.ArgumentParser(description ='Basic PNG chunk remover',add_help=True)
parser.add_argument('--outputdir',default=outputdirname, help ='The output directory. Default is {outputdirname}')
parser.add_argument('--inputdir',default ='.', help = 'The input directory. Default is cwd')
parser.add_argument('--force', '-f',action ='store_true',help='Ignore warnings, used when input and output are the same directory')
parser.add_argument('--parameter',default ='parameters', help = 'The chunk parameter to modify default is "parameters"')
parser.add_argument('--remove','-r',action = 'store_true', help="remove the pameter specified by 'parameter'")
parser.add_argument('--add','-a', help = 'The text to add, default')
parser.add_argument('--show','--display','-s','-d',action ='store_true', help = 'Show/display all text chunks')


args =parser.parse_args()
print(args)
# print (len(args.add), args.add)
if args.show:
    MODE='show'
elif args.add:
    MODE='add'
elif args.remove:
    MODE='remove'
else:
    parser.print_help()
    print('No action specified, use one of -d -r or -a')
    quit()
print ('mode',MODE)


inputdir = Path(args.inputdir)
# Check if input directory exists, otherwise exit
if not inputdir.exists() or not inputdir.is_dir():
    print("Input directory does not exist")
    exit()


#we only need output directories for add and remove
if not MODE=='show':
    outputdir = Path(args.outputdir)
    if inputdir== outputdir:
        print('Input and output directory are the same')
        if args.force==False:
            print('use -f to force')
            quit()

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
