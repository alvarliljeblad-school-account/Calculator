NUMBERS = [str(n) for n in range(10)]+['.']


def find_chunk(expr:str,index:str):
    left_index=index-1
    a = True
    while a:
        if left_index == 0:
            a = False
        elif not (expr[left_index-1] in NUMBERS):
            a = False
        else:
            left_index-=1
    right_index=index+1
    a = True
    while a:
        if right_index == len(expr)-1:
            a = False
        elif not (expr[right_index+1] in NUMBERS):
            a = False
        else:
            right_index+=1
    return (left_index,right_index)

def evaluate_chunk(left,right,operator):
        left = float(left)
        right = float(right)
        match operator:
            case '+':
                return left+right
            case '-':
                return left-right
            case '*':
                return left*right
            case '/':
                return left/right
            case '^':
                return left**right
        


def evaluate_expression(expression:str):
    print(expression)
    if sum(map(expression.count, ['+','-','*','/','^'])) == 0:
        return float(expression.strip())
    else:
        #Find the index of the operation to evaluate
        if expression.count('^') > 0:
            index = expression.find('^')
        if sum(map(expression.count, ['*','/'])) > 0:
            mult_index = expression.find('*')
            if mult_index == -1: mult_index=len(expression)
            div_index = expression.find('/')
            if div_index == -1: div_index=len(expression)
            index = min(mult_index,div_index)
        elif sum(map(expression.count, ['+','-'])) > 0:
            add_index = expression.find('+')
            if add_index == -1: add_index=len(expression)
            sub_index = expression.find('-')
            if sub_index == -1: sub_index=len(expression)
            index = min(add_index,sub_index)

        #Find the chunk around the operator
        left_index,right_index = find_chunk(expression,index)
        #Get the values in the chunk
        left = expression[left_index:index]
        right = expression[index+1:right_index+1]
        #Evaluate chunk
        value = evaluate_chunk(left,right,expression[index])

        #Construct new string
        new_expression=expression[:left_index]+str(value)+expression[right_index+1:]
        evaluate_expression(new_expression)


def main():
    print('Please enter an expression')
    expression = input('->')
    return_value = evaluate_expression(expression)
    print(return_value)

if __name__ == '__main__':
    main()