def is_armstrong_number(num):
    n = num
    sum = 0
    num_of_digits = len(str(num))
    
    while n > 0:
        digit = n % 10 
        sum += digit ** num_of_digits 
        n //= 10  
    
    return sum == num

num = int(input("Enter a number to check if it's Armstrong: "))

if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
