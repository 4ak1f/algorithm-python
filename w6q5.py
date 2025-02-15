month_input = input("Enter the month name or number to find the number of days in that month: ")

month_dict = {
    'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
    'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12
}

if (month_input.isdigit()):
    mnth = int(month_input)
else:
    month_input = month_input.lower() 
    if (month_input in month_dict):
        mnth = month_dict[month_input]
    else:
        print("Invalid month name!")
        exit()

if (1 <= mnth <= 12):
    if (mnth == 1 or mnth == 3 or mnth == 5 or mnth == 7 or mnth == 8 or mnth == 10 or mnth == 12):
        print("Number of days = 31")
    elif (mnth == 2):
        print("Number of days = 28 (non-leap year)")
    else:
        print("Number of days = 30")
else:
    print("Only 12 months in a year!")
