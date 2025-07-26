#Temperature Conversion
def C_TO_F(C):
    return (C * 9/5) + 32

def F_TO_C(F):
    return (F - 32) * 5/9

temp = float(input("Enter the temperature value: "))
unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ").strip().upper()

if unit == "C":
    converted = C_TO_F(temp)
    print(f"{temp}°C is {converted:.2f}°F")
elif unit == "F":
    converted = F_TO_C(temp)
    print(f"{temp}°F is {converted:.2f}°C")
else:
    print("Invalid unit entered. Please enter 'C' or 'F'.")