def separate_even_odd(numbers):
    even_list = []
    odd_list = []

    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)

    return even_list, odd_list

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
even, odd = separate_even_odd(numbers)

print("Even numbers:", even)
print("Odd numbers:", odd)
