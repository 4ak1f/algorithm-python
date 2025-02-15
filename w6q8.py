mixed_list = input("Enter a list of elements (e.g., 10, 'a', 20, 'b') to find the sum of integers present in that list: ")
mixed_list = eval(mixed_list)

total_sum = 0

for item in mixed_list:
    if isinstance(item, (int, float)):
        total_sum += item

print("The sum of the numbers in the list is:", total_sum)
