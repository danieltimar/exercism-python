def is_leap_year(year: int) -> bool:
    """
    The function takes a year as an integer and returns True if it is leap year and False if it is not.
    """
    if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
        return True
    else:
        return False

