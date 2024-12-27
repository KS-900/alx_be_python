num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":  
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*": 
        result = num1 * num2
    case "/": 
        result = num1 / num2
        if num2 == 0:
            print("Cannot divide by zero.")
            exit()
    case _:
        print("Invalid operation")
        exit()
print(f"The result is {result}")