data = input("Enter a string to make another string consisting of the first and last two letters of the first string-")
result = data[:2] + data[-2:] if len(data) >= 2 else ''
print(result)
