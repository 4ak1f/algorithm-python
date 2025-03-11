def factorial(n):
    fact = 1
    for i in range(1, n + 1): 
        fact *= i  
    return fact

num = int(input("Enter a number to find its factorial: "))

if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}.")
