print("This is a Calculator")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Select operation:") #performing only two operations .
print("1. Addition")
print("2. Subtraction")

choice = input("Enter choice (1 or 2): ")

if choice == '1':
    result = a + b
    print("Result:", a, "+", b, "=", result)
elif choice == '2':
    result = a - b
    print("Result:", a, "-", b, "=", result)
else:
    print("Invalid choice")
