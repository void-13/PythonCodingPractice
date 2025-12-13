def basic_calculator():
    firstInput = float(input("Enter first number: "))
    secondInput = float(input("Enter second number: "))

    operator = input("Enter any of the following operator (+, -, *, /): ")

    if operator == "+":
        result = firstInput + secondInput
    elif operator == "-":
        result = firstInput - secondInput
    elif operator == "*":
        result = firstInput * secondInput
    elif operator == "/":
        result = firstInput / secondInput
    else:
        print("Invalid operator")
        return
    print(f"Result: {result:.2f}")


basic_calculator()
