#Fibonacci sequence generator
def Fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibo(n-1) + Fibo(n-2)
# Main function to run the Fibonacci sequence generator
def main():
    try:
        n = int(input("Enter the number of terms in the Fibonacci sequence: "))
        if n < 0:
            print("Please enter a non-negative integer.")
            return
        print("Fibonacci sequence:")
        for i in range(n):
            print(Fibo(i), end=" ")
        print()  # For a new line after the sequence
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
main()
