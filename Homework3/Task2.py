from datetime import date
import datetime


year = int(input("Enter the year you were born: "))
month = int(input("Enter the number of the month you were born: "))
_date = int(input("Enter the date you were born: "))

if year > 0 and year <= 2024:
    validYear = True
else:
    validYear = False

if month > 0 and month <= 12:
    validMonth = True
else:
    validMonth = False

if _date > 0 and _date <=31:
    validDate = True
else:
    validDate = False

if validYear and validMonth and validDate:
    birthDate = datetime.date(year, month, _date)
    weekDay = birthDate.weekday()
    if weekDay == 0:
        print("You were born on Monday")
    elif weekDay == 1:
        print("You were born on Tuesday")
    elif weekDay == 2:
        print("You were born on Wednesday")
    elif weekDay == 3:
        print("You were born on Thursday")
    elif weekDay == 4:
        print("You were born on Friday")
    elif weekDay == 5:
        print("You were born on Saturday")
    else:
        print("You were born on Sunday")

    