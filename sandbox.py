import datetime

samplefile = datetime.datetime.now()

#to create a file with date as filename

def create_file():
    with open(samplefile.strftime("%Y-%H")+".txt",'w') as file:
        file.write("")


create_file()



import time
lst=[]

for i in range (2):
    lst.append(datetime.datetime.now())
    time.sleep(1)

    for i in lst:
        print (lst)
