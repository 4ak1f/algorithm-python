print("To make a list for range r1 to r2.")
r1 = int(input("Enter the first number (r1): "))
r2 = int(input("Enter the second number (r2): "))

if r1 < r2:
    # Create a list using range (inclusive)
    result_list = list(range(r1, r2 + 1))
    print("The list with the given range is:", result_list)
else:
    print("Error: r1 should be less than r2.")
