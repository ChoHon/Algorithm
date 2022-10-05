year = int(input())

def leap_year(year):
    if (year % 400) == 0:
        return 1

    elif (year % 100) == 0:
        return 0

    elif (year % 4) == 0:
        return 1

    else:
        return 0

print(leap_year(year))