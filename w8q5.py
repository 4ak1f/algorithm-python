print("Different operations on the string \"Python rules!\"")
data = "Python rules!"
words = data.split()
uppercase_data = data.upper()
position = data.find("rules")
char_position = data.find('o')
replaced_data = data.replace("!", "?")

print(words)
print(uppercase_data)
print(position)
print(char_position)
print(replaced_data)
