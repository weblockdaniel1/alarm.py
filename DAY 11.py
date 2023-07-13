year = int(input("Enter the Year to compute the year: "))
#To calculate the number of seonds you 1st need to consider factors
if year % 4 == 0 and (year % 100 != 0 or year % 400 ==0):
        days = 366
        #if days is equalto 366 then its a leap year
        year_type = "Leap Year"
else:
        days = 365
        # it means is a normal year
        year_type = "Normal year"
print()
secondsMinute = 60
minutesHour = 60
hoursDay = 24
daysMonth = 31
monthsYear = 12
print()

secondsYear = days * hoursDay * minutesHour * secondsMinute
print('Conversion Factors')
print("\nThere are", secondsYear, "seconds in the year you \nhave entered which is", year)
