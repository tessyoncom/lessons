
years = [2000,2012,2011,1996,1219,1900]

def leap_year(x):
    for year in x:
        if year % 4 != 0:
            print ("Common year")
        elif year % 100 != 0:
            print ("Leap year")
        elif year % 400 != 0:
            print ("Common year")
        else: print ("leap year")



print (leap_year(years))


