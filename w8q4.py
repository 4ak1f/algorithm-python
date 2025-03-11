n = int(input("Enter the range for creating tuple with integers and their respected sqaures next to them: "))
result = [(i, i**2) for i in range(1, n+1)]
print(result)
