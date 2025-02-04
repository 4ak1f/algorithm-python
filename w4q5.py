print("Q5-Calculate the sum of digits of given decimal integer.")
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

number = int(input("Enter a decimal integer: "))
print("Sum of digits:", sum_of_digits(number))
