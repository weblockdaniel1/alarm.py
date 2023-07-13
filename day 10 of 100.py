year = int(input("Enter the Year: "))
    #Check to see if it's a leap year or normal year
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    #Leap year has 366 days
    days = 366
    print("Leap Year")
    year_type = "Normal Year"
else:
    #Normal year has 365
    days = 365
    print("Normal Year")
    year_type = "Normal year"

secondsInMinute = 60
minutesInHour = 60
hoursInDay = 24
daysInmonth = 31
monthsInYear = 12


secondsInYear = days * hoursInDay * minutesInHour * secondsInMinute
print("Conversion Factors: ")
print("1 minute = ", secondsInMinute, "seconds")
print("1 hour = ", minutesInHour * secondsInMinute, "seconds")
print("1 day = ", hoursInDay * minutesInHour * secondsInMinute, "seconds")
print("1 year = ", days * hoursInDay * minutesInHour * secondsInMinute, "seconds")

print()
print("\nNumber of seconds in the year", year, "(" + year_type + "):", secondsInYear)
print("monthsInYear: 12")


