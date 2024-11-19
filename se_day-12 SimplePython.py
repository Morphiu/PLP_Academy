def calculate(num_1, num_2, operation):
    if operation == "+":
        return num_1 + num_2
    elif operation == "-":
        return num_1 - num_2
    elif operation == "*":
        return num_1 * num_2
    elif operation == "/":
        if num_2 == 0:
            print("Cannot divide by zero.")
            exit()
        else:
            return num_1/num_2
    else:
        print("Invalid operator")
        exit()


name = input("What is your name?")
print("Hello "+name)
num_1 = input("Enter the first number: ")
num_2 = input("Enter the second number: ")
operation = input("Which operation would you like to do? e.g., +,-,*,/")

num_1 = int(num_1)
num_2 = int(num_2)

result = calculate(num_1, num_2, operation)
print(num_1, operation, num_2, "=", result)
