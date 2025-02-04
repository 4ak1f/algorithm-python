print("Q4-Calculate the factorial of a number ")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

print("Calculate the factorial of a number")
number = int(input("Enter a non-negative integer: "))
if number >= 0:
    print(f"Factorial of {number}: {factorial(number)}")
else:
    print("Please enter a non-negative integer.")