print("Enter three numbers to find the smallest of the three.")
n1=int(input("First number: "))
n2=int(input("Second number: "))
n3=int(input("Third number: "))
if(n1<n2 and n1<n3):
    print(n1,"is the smallest of the three.")
    if(n2<n1 and n2<n3):
        print(n2,"is the smallest number of the three.")
else:
    print(n3,"is the smallest number of the three.")