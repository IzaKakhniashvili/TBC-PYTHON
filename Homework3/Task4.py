from forex_python.bitcoin import BtcConverter

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the date: "))
price = int(input("Enter the price of bitcoin: "))


if year > 0 and year <= 2024:
    validYear = True
else:
    validYear = False

if month > 0 and month <= 12:
    validMonth = True
else:
    validMonth = False

if day > 0 and day <=31:
    validDate = True
else:
    validDate = False

if price > 0  and validDate and validMonth and validYear:
    b = BtcConverter()
    latest_price = b.get_latest_price('USD')
    difference =  price - latest_price
    if difference > 0:
        print(f"Your profit is: {difference} ")
    elif difference == 0:
        print(f"You have no profit")
    else:
        print(f"Your loss is {difference}")
else:
    print("Invalid date.")
