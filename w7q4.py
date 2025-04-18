def factorial(n):
    if n == 0 or n == 1:  # Base case: 0! = 1 and 1! = 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive step

# Input from the user
n = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {n} is: {factorial(n)}")
