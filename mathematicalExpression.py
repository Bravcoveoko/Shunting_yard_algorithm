import re

def checkPrecedence(op1, op2):
    # u stands for unary minus and - sign stands for binary minus
    prece = {"+": 2, "-": 2, "/": 3, "*": 3, "u": 4}
    return prece[op1] >= prece[op2]

def evaluate(rpn):
    print(rpn)
    values = []
    for i in range(len(rpn)):
        token = rpn[i]
        print(values)
        if type(token) is int or type(token) is float:
            values.append(token)
        elif token == '+':
            right = values.pop()
            left = values.pop()
            res = left + right
            values.append(res)
        elif token == '*':
            right = values.pop()
            left = values.pop()
            res = left * right
            values.append(res)
        elif token == '/':
            right = values.pop()
            left = values.pop()
            res = left / right
            values.append(res)
        elif token == 'u':
            n = values.pop()
            values.append(-n)
        else:
            right = values.pop()
            left = values.pop()
            res = left - right
            values.append(res)
    return values.pop()

def shunting_yard(tokens):
    output, stack = [], []
    length = len(tokens)
    for i in range(length):
        token = tokens[i]
        if type(token) is int or type(token) is float:
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            peek = stack[-1] if stack else None
            while peek is not None and peek != '(':
                output.append(peek)
                stack.pop()
                peek = stack[-1] if stack else None
            stack.pop()  
        else:
            peek = stack[-1] if stack else None
            while peek is not None and peek not in "()" and checkPrecedence(peek, token):
                output.append(stack.pop())
                peek = stack[-1] if stack else None
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return output

def stringToInt(tokens):
    length = len(tokens)
    for i in range(length):
        try:
            intNum = int(tokens[i])
            tokens[i] = intNum
        except:
            try:
                floatNum = float(tokens[i])
                tokens[i] = floatNum
            except:
                continue

def calc(expression):
    print("EXP: ",expression)
    # Remove whitespaces
    tokens = ""
    for t in expression:
        if t != " ":
            tokens += t
    
    # Find unary minus sign
    length = len(tokens)
    newtokens = ""
    for i in range(length):
        tk = tokens[i]
        if tk == '-':
            # - is unary if previous character is left parenthesis or any operator OR it is a first character
            if i == 0:
                newtokens += 'u'
            elif i - 1 > -1 and newtokens[i - 1] in "+-*/(":
                newtokens += 'u'
            else:
                newtokens += tk
        else:
            newtokens += tk
    
    # Regex to take operators, integers number or flaot numbers
    newtokens = re.findall("[+/*()-]|u|\d+\.*\d*", newtokens)
    stringToInt(newtokens)
    # Make reverse polish notation with shunting yard algorithm
    rpn = shunting_yard(newtokens)
    print(rpn)
    # Finally evaluate the rpn form
    result = evaluate(rpn)
    return result