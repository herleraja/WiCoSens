import glob
import shutil
import os

# set to the file extension of "to-be-merged" files
ext = '.csv'

# set to your working directory
dir_path = 'C:\\Users\\NUCER\\Documents\\git\\WiCoSens\\MLDataLabeler\\datarecording\\'

# set to the name of your output file
outfilename = dir_path + 'final.csv'

'''
with open(outfilename, 'w') as outfile:
    for filename in glob.glob(dir_path + '*.csv'):
        if filename == outfilename:
            # don't want to copy the output into the output
            continue
        with open(filename, 'r') as readfile:
            shutil.copyfileobj(readfile, outfile)

#OR 

with open(dir_path + outfilename, 'w') as outfile:
    for filename in glob.glob(dir_path + '*.csv'):
        with open(filename) as infile:
            for line in infile:
                outfile.write(line)
'''

with open(outfilename, 'a') as singleFile:
    for csv in glob.glob(dir_path +'*.csv'):
        if csv == outfilename:
            pass
        else:
            for line in open(csv, 'r'):
                singleFile.write(line)
            singleFile.write('\n')
