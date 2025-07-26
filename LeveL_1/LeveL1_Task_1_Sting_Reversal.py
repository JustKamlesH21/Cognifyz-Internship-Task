#String Reversal
def reverse_string(input_string):
    return input_string[::-1]


a=input("Enter a string to reverse: ")
reversed_string = reverse_string(a)
print("Reversed string:", reversed_string)