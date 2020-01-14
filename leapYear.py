def is_leap(year):
    leap = False
    max=10**5
    if year in range(1900, max+1):
        if year%100==0 and year%400==0:
            if year%4==0:
                leap = True
        else:
            if year%4==0 and year%100!=0:
                leap = True
    return leap

year = int(2000)
print(is_leap(year))