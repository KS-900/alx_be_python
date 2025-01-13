#defining a def
def perform_operation(num1,num2,operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2 
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Divided by zero" # 0 exception
        else:
            return num1 / num2
    else:
        return "Invalid operation" # wrong operation inputed