def is_leap_year(year):
    """Return True if the given year is a leap year, False otherwise.
    A leap year is- Divisible by 4 and not divisible by 100, OR Divisible by 400
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
