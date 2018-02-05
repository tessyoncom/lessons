def isLeapYear(year):

    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def yearDaysCount(y1, y2):
    leapYearCount = 0
    normalYearCount = 0
    yearAfter = y1 + 1
    while yearAfter <= y2:
        if isLeapYear(yearAfter):
            leapYearCount += 1


        else:
            normalYearCount += 1

        yearAfter += 1


    return leapYearCount * 366 + normalYearCount * 365


print (yearDaysCount(2012, 2018))