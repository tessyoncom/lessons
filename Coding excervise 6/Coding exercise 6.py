#this programme merges 3 different files and names the merged file by time
import datetime


filename = datetime.datetime.now()
print (filename)

with open(filename,'w') as file:
