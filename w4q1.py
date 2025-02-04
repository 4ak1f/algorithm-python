def avg(a,b,c,d,e):    
    print("Average of these 5 numbers :",(a+b+c+d+e)/5)
def cel_to_fahr(cel):
    print("Fahrenheit temp. :",cel*(9/5)+32)
def rec(len,br):
    print("Perimeter of rectangle: ",len*br)

i=int(input("Enter 1 for finding average of 5 numbers,\n2 for converting celsius to fahrenheit,\n3 to find the perimeter of rectangle: "))
if(i==1):
    a = int(input("Enter 1st number : "))
    b = int(input("Enter 2nd number : "))
    c = int(input("Enter 3rd number : "))
    d = int(input("Enter 4th number : "))
    e = int(input("Enter 5th number : "))
    avg(a,b,c,d,e)
elif(i==2):
    cel = float(input("Enter Celsius temp. : "))
    cel_to_fahr(cel)
elif(i==3):
    len = float(input("Enter length : "))
    br = float(input("Enter breadth : "))
    rec(len,br)
else:
    print("Invalid option! Choose option 1,2 or 3.")