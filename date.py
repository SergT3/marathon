def date(day, month, year):
    if day <= 0 or month <= 0 or year < 0:
        return False
    thirty_ones = [1, 3, 5, 7, 8, 10, 12]
    thirties = [4, 6, 9, 11]
    if month in thirty_ones and day <= 31:
        return True
    if month in thirties and day <= 30:
        return True
    leap = False
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        leap = True
    if leap and month == 2 and day <= 29:
        return True
    if not leap and month == 2 and day <= 28:
        return True
    return False
