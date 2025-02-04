import math

n = int(input("Enter a number: "))

if (math.isqrt(5 * n * n + 4) ** 2 == 5 * n * n + 4) or (math.isqrt(5 * n * n - 4) ** 2 == 5 * n * n - 4):
    print(f"{n} is a Fibonacci number.")
else:
    print(f"{n} is not a Fibonacci number.")
