def generate_fibonacci(n):
    fib_sequence = []
    a, b = 0, 1  

    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b 
    
    return fib_sequence

num = int(input("Number of \"Fibonacci numbers\" that you would you like to generate: "))

fibonacci_numbers = generate_fibonacci(num)
print(f"The first {num} Fibonacci numbers are: {fibonacci_numbers}")
