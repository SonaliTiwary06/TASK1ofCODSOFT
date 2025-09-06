def calculate(user_input):
    parts = user_input.split()  # Split input into number, operator, number
    if len(parts) != 3:
        print("Invalid input, Use format: number operator number (e.g. 3 + 7)")
        return
    
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    # Perform calculation based on operator
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Use only + - * /")
        return

    # If result is a whole number, convert to int
    if int(result) == result:
        result = int(result)

    print("Result:", result)

def main():
    print("--------- Simple Calculator (type exit to quit) ---------")
    while True:
        user_input = input("Enter calculation (+ - * /) or 'exit': ")
        if user_input == "exit":
            print("Good bye")
            break
        else:
            calculate(user_input)

main()
