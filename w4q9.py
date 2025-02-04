print("Q9-Enter a string and calculate the number of upper case letters and lower-case letters")
def count_case_letters(s):
    upper_case = 0
    lower_case = 0
    for char in s:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1
    return upper_case, lower_case

string = input("Enter a string: ")
upper, lower = count_case_letters(string)
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
