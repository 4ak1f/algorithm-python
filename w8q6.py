data = input("Enter a string to count the frequency of characters-")
frequency = {char: data.count(char) for char in data}
print(frequency)
