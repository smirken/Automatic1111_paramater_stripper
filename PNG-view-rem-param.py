#!/bin/env python3
 
# add args
#current version, reads all png in this directory, and dumps in ParametersRemoved

import PIL
from PIL import Image 
import os

inputdir='.'
outputdir='ParametersRemoved'

#make sure inpuyt exists
if not os.path.isdir(inputdir):
    print ('Input does not exist')
    quit()

#if it doesn't exist create output dir
if not os.path.isdir(outputdir):
    os.mkdir(outputdir)

#Get a list of all file in inputdir which is "currentDir"
#check if that file exitss in outputdir 'ParametersRemoved'
#if it does not exist load and save

for eachfile in os.listdir(inputdir):
    # print ('eachfile',eachfile)
    infilename=os.path.join(inputdir,eachfile)
    infileext=os.path.splitext(eachfile)[1].lower()
    # print (eachfile,infileext)
    if (os.path.isfile(infilename) and infileext == ".png"):
        # print ('valid PNG', infilename)
        #if it is a file continue
        outputfilename=os.path.join(outputdir,eachfile)
        if not (os.path.exists(outputfilename)):
            # print("It doesn't exist",outputfilename)
            with PIL.Image.open(infilename) as img:
                img.load()
                img.info.pop("parameters")
                img.save(outputfilename)
        else:
            print('File already processed',outputfilename)
    else:
        print ('invalid PNG',infilename)
