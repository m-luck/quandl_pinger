import csv
import pandas as pd
import sys
import time
from typing import List

if len(sys.argv) < 2:
    print("Please include the file name as the first argument to this Python program")

file_name = sys.argv[1]

def filterDimensions(csvpath:str, newcsv:str, features:List):
    '''
    Take a set of features you want to keep and isolate those.
    '''
    chunksize = 20000
    i=0
    for chunk in pd.read_csv(csvpath, chunksize=chunksize, usecols=features):
        print("Chunk",i)
        i+=1
        chunk.to_csv(newcsv, mode='a', index=False)

timestr = time.strftime("%Y%m%d-%H%M%S")
new_file = f"rename_this_{timestr}.csv"
filterDimensions(file_name, new_file, ["ticker","stkPx", "spot_px"])
print("Prospero Team member, your file of interest is at", new_file)