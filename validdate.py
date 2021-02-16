# Reads a date in M/D/YYYY format from the keyboard, and determines whether the date is a valid
# Gregorian date.
# Peter Brown <peter.brown@converse.edu>, 2021-02-16

from typing import cast, List, Optional, Tuple

def isLeapYear(year:int) -> bool:
    """Takes a year and returns a bool telling whether the year is a leap year."""
    isLeap:bool = (year % 4 == 0 and year % 100 != 0) \
                    or (year % 400 == 0)
    return isLeap
    
def parseDateString(dateStr:str) -> Tuple[int, int, int]:
    # Pre: dateStr is a string (mypy check)
    month:int = -1
    day:int = -1
    year:int = -1
    dateparts:List[str] = dateStr.split('/')
    #print(dateparts)
    try:
        if len(dateparts) == 3: # Can't be greater!
            month = int(dateparts[0].strip())
            day = int(dateparts[1].strip())
            year = int(dateparts[2].strip())
    except ValueError: # One of the parts wasn't an integer
        month = -1
        day = -1
        year = -1
    # Post: (validity criteria aren't quite strong enough: e.g., "/2162021/" passes)
    assert (dateStr.count('/') == 2 and dateStr.replace('/','').isdigit()) or \
        (month == day == year == -1)
    return month, day, year

def validYear(year:int) -> bool:
    return year >= 1582   # Future years are OK

def validMonth(month:int) -> bool:
    return 1 <= month <= 12

def validDay(month:int, day:int, year:int) -> bool:
    valid:bool = True
    if day < 1 or day > 31:
        valid = False
    # 30-day months
    elif month in (9, 4, 6, 11) and day == 31: 
        valid = False
    # February
    elif month == 2 and day > 29:
        valid = False
    elif month == 2 and day == 29 and not isLeapYear(year):
        valid = False
    return valid

def validDate(dateStr:str) -> bool:
    # Pre: dateStr is a string.  (mypy should catch it if not.)
    valid:bool = True
    month, day, year = parseDateString(dateStr) # type: Tuple[int, int, int]
    if not validYear(year):
        valid = False
    elif not validMonth(month):
        valid = False
    elif not validDay(month, day, year):
        valid = False
    # Post: valid == True iff dateStr contains a valid Gregorian date in m/d/yyyy format
    return valid    

def main(args:List[str]) -> int:
    # No precondition
    # Read a date from the keyboard
    dateStr:str = input('Please enter a date (m/d/yyyy, 4-digit year): ')

    print('{} is '.format(dateStr), end='')
    if not validDate(dateStr):
        print ('NOT', end=' ')
    print('a valid Gregorian date.')

    # No real postcondition
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)