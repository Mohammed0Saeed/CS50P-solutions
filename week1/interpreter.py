#prompt the user to enter a mathematical expression
expression = input("Expression: ").split(" ")

match expression[1]:
    case "+":
        print(float(expression[0]) + float(expression[2]))
    case "-":
        print(float(expression[0]) - float(expression[2]))
    case "*":
        print(float(expression[0]) * float(expression[2]))
    case "/":
        print(float(expression[0]) / float(expression[2]))
    case _:
        print("invalid expression")
