
import datetime
import glob2

my_files = glob2.glob("*.txt")

with open("mergedfile.txt",'w') as file:
    for files in my_files:
        with open (files,'r') as f:
            file.write(f.read()+"\n")


