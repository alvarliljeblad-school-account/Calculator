# A list of symbols that represent numbers
NUMBERS = [str(n) for n in range(10)] + ["."]


def find_chunk(expr: str, index: int):
    """
    Finds the chunk of numbers surrounding an operator at index index in expression expr
    Returns the indexes of the ends of the chunk
    """
    #Find left index by starting one to the left of the oprator
    left_index = index - 1
    a = True
    # Move left until the next one is not a number, then the endpoint is found
    while a:
        if left_index == 0:
            a = False
        elif expr[left_index - 1] not in NUMBERS:
            a = False
        else:
            left_index -= 1
    # Find right index by starting one to the right of the operator
    right_index = index + 1
    a = True
    # move right until the next one is not a number, then the endpoint is found
    while a:
        if right_index == len(expr) - 1:
            a = False
        elif expr[right_index + 1] not in NUMBERS:
            a = False
        else:
            right_index += 1
    # return the indexes of the endpoints
    return (left_index, right_index)


def evaluate_chunk(left, right, operator):
    """
    Takes a left value, a right vaue and an operator and evaluates the operater on the vaues
    Returns the result
    """
    # Convert the values to floats
    left = float(left)
    right = float(right)
    # Check operator and return result
    match operator:
        case "+":
            return left + right
        case "-":
            return left - right
        case "*":
            return left * right
        case "/":
            # If division by 0 return an error
            if right == 0:
                return "ERROR: Division by 0 not allowed"
            return left / right
        case "^":
            return left**right


def find_corresponding_parenthesis(expr, index):
    """
    Finds the corresponding closing parenthesis to the open parenthesis at index in expr
    returns the index of the corresponding parenthesis
    """
    # checks how many parentheis deep it is when another parentesis is found at the same depth return its index
    depth = 0
    i = index
    while not (expr[i] == ")" and depth == 0):
        i += 1
    return i


def evaluate_expression(expression: str):
    """
    Recursively evaluates an expression containing numbers, parenthesis and the operators (+,-,*,/,^)
    Returns the resulting value
    """
    #Remove all spaces in the string
    expression = expression.replace(" ", "")
    # If the expression has no operators, return the number value
    if sum(map(expression.count, ["+", "-", "*", "/", "^", "(", ")"])) == 0:
        return float(expression)
    else:
        # Parenthesis handlig
        if expression.count("(") > 0:
            #Find the first open parenthesis pair
            left_index = expression.find("(")
            right_index = find_corresponding_parenthesis(expression, left_index)
            # Evaluate the expression inside the parenthesis
            value = evaluate_expression(expression[left_index + 1 : right_index])

        else:
            # Find the index of the operation to evaluate
            # find the operators in the correct order following PEMDAS
            if expression.count("^") > 0:
                index = expression.find("^")
            elif sum(map(expression.count, ["*", "/"])) > 0:
                mult_index = expression.find("*")
                if mult_index == -1:
                    mult_index = len(expression)
                div_index = expression.find("/")
                if div_index == -1:
                    div_index = len(expression)
                index = min(mult_index, div_index)
            elif sum(map(expression.count, ["+", "-"])) > 0:
                add_index = expression.find("+")
                if add_index == -1:
                    add_index = len(expression)
                sub_index = expression.find("-")
                if sub_index == -1:
                    sub_index = len(expression)
                index = min(add_index, sub_index)

            # Find the chunk around the operator
            left_index, right_index = find_chunk(expression, index)
            # Get the values in the chunk
            left = expression[left_index:index]
            right = expression[index + 1 : right_index + 1]
            # Evaluate chunk
            value = evaluate_chunk(left, right, expression[index])
        
        # If the vaule is an error pass it up
        if type(value) == str:
            return value
        # Construct new string
        new_expression = (
            expression[:left_index] + str(value) + expression[right_index + 1 :]
        )
        # recursively evaluate until there is only a number left
        return evaluate_expression(new_expression)


def main():
    # Loop until program is closed
    running = True
    while running:
        # Take input
        print('Please enter an expression(q to quit)')
        expression = input('->')
        #Check to close program
        if expression == 'q':
            running = False
        else:
            # Evaluate the expression
            return_value = evaluate_expression(expression)
            print(return_value)


if __name__ == "__main__":
    main()