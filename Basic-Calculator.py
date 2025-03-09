def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

def calculator():
    operations = {
        '1': ('Addition', add),
        '2': ('Subtraction', subtract),
        '3': ('Multiplication', multiply),
        '4': ('Division', divide)
    }
    
    print("Select an operation:")
    for key, value in operations.items():
        print(f"{key}. {value[0]}")
    
    choice = input("Enter choice among these (1/2/3/4): ")
    
    if choice in operations:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = operations[choice][1](num1, num2)
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input! Please enter numerical values.")
    else:
        print("Invalid choice! Please select a valid operation.")

calculator()
