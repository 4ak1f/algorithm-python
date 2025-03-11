def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def generate_fibonacci(n):
    fib_sequence = []
    for i in range(n):
        fib_sequence.append(fibonacci(i))
    return fib_sequence

n = int(input("Enter the number of Fibonacci terms to generate: "))
fib_terms = generate_fibonacci(n)
print(f"The first {n} Fibonacci terms are: {fib_terms}")
