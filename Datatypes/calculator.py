
print("Hii, guys! This is a Python-based calculator.")

n = float(input("Enter the first number: ").strip())
m = float(input("Enter the second number: ").strip())

method = input("Enter the method (+, -, *, /): ").strip()

if method == "+":
    print("Addition:", n + m)

elif method == "-":
    print("Subtraction:", n - m)

elif method == "*":
    print("Multiplication:", n * m)

elif method == "/":
    if m == 0:
        print("Cannot divide by zero!")
    else:
        print("Division:", n / m)

else:
    print("Choose a correct method!")

print("Thank you for using this calculator!")
