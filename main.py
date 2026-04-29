def calculate_expression(expression:str):
    ... #TODO function that evaluates an expression string recursively

def main():
    print('Please enter an expression')
    expression = input('->')
    return_value = calculate_expression(expression)

if __name__ == '__main__':
    main()