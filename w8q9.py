def reverse_words():
    sentence = input("Enter a string to get the reverse version of the string: ")
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    print(reversed_sentence)

def check_palindrome():
    string = input("Enter a string to check if it's a palindrome: ")
    if string == string[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

reverse_words()
check_palindrome()
