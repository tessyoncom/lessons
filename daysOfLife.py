daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeapYear(year):
    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##
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


def daysInYearOfBirth(y1, m1, d1):
    if isLeapYear(y1):
        if m1 > 1:
            actualMonthDays = daysOfMonths[m1] - d1 + 1
            days = 0
            while m1 <= 11:
                if m1 == 11:
                    return actualMonthDays + days
                else:
                    for days in range(m1 + 1, 11):
                        days += days
                m1 += 1

    else:
        actualMonthDays = daysOfMonths[m1] - d1 + 1
        days = 0
        while m1 <= 11:
            if m1 == 11:
                return actualMonthDays + days + 1
            else:
                for days in range(m1 + 1, 11):
                    days += days
            m1 += 1


def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    ##
    # Your code here.
    ##
    days = yearDaysCount(y1, y2) + daysInYearOfBirth(y1, m1, d1)

    return days


print (daysBetweenDates(2018, 0, 1, 2018, 0, 1))

