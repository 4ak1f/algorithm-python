year=int(input("Enter a year to check if it's leap year or not: "))
if((year%4==0 and year%100!=0) or (year%400==0)):
    print(year, "is leap year.")
else:
    print(year,"is not leap year.")    