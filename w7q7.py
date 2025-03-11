def second_largest(numbers):
    numbers = list(set(numbers))
    numbers.sort(reverse=True)
    # Check if the list has at least two elements
    if len(numbers) < 2:
        return "There is no second largest number"
    return numbers[1]

numbers = [int(x) for x in input("Enter numbers separated by space to find the second largest number out of all of them: ").split()]

result = second_largest(numbers)
print("The second largest number is:", result)
