from adt import ArrayStack


print("一、中辍表达式转后辍表达式")


def infix_to_postfix(infix_expr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = ArrayStack()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            topToken = op_stack.pop()
            while topToken != "(":
                postfix_list.append(topToken)
                topToken = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)


print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infix_to_postfix("( A + B ) * ( C + D )"))
print()

print("二、后辍表达式求值")


def postfix_eval(postfix_expr):
    op_stack = ArrayStack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token in "0123456789":
            op_stack.push(int(token))
        else:
            operand2 = op_stack.pop()
            operand1 = op_stack.pop()
            result = do_math(token, operand1, operand2)
            op_stack.push(result)
    return op_stack.pop()


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


print(postfix_eval("7 8 + 3 2 + /"))
