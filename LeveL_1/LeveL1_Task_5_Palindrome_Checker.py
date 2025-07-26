#Palindrome Checker
def is_palindrome(Str):
    Str = Str.lower().replace(" ", "")  # Normalize the string
    return Str == Str[::-1]

Str= input("Enter a string to check if it's a palindrome: ")
if is_palindrome(Str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


