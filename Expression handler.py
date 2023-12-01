""""Example of shunting yard algorithm to evaluate
    simple math expressions of single digits and basic operators
    like +, -, *, /, ^, (, )

    Note: this improved version uses regex to enable use with decimals
          and multi digit numbers"""
import re

# checks if an input string matches an integer or decimal number
def is_integer_or_decimal(s):
    pattern = r"^[+-]?\d+(\.\d+)?$"
    return bool(re.match(pattern, s))

operators = {'(':1, ')':1, '^':1.5, '*':2, '/':2,
              '+':3, '-':3}

# Splits expression into its individual parts, operators and operands
def make_infix(expr):
    result = []
    cur = []
    for char in expr:
        if char in operators:
            if cur:
                result.append("".join(cur))
            cur = []
            result.append(char)
        else:
            cur.append(char)
    if cur:
        result.append("".join(cur))
    return result

def convert(expr):
    stack = []
    result = []
    for symbol in expr:
        # if it's a number just add to postfix result
        if is_integer_or_decimal(symbol):
            result.append(float(symbol))
        # if it's something we don't recognize then it's invalid
        elif symbol not in operators:
            print(f"{expr}: invalid expression - unknown symbol -> {symbol}")
            return
        # if we have symbols in our stack
        elif stack:
            # special case when the symbol is )
            if symbol == ')':
                # add everything on the stack onto the
                # result until matching ( is found
                while stack[-1] != '(':
                    result.append(stack.pop())
                    # if we get through all previous symbols and none were (
                    # then we have an invalid expression
                    if not stack:
                        print(f"{expr}: invalid expression - unmatched ')'")
                        return
                # we found matching ( and must now remove it
                stack.pop()
            # compare precedence
            # if current symbol is lower priority, we add pop top of stack to result
            # and push symbol onto stack, else just push symbol onto stack
            elif operators[symbol] > operators[stack[-1]] and stack[-1] != '(':
                result.append(stack.pop())
                stack.append(symbol)
            else:
                stack.append(symbol)
        else:
            # push onto stack if it's empty
            stack.append(symbol)
    while stack:
        # at the end just pop all remaining symbols onto result
        # if we encounter ( then it didn't have a match so
        # expression is invalid
        if stack[-1] == '(':
            print(f"{expr}: invalid expression - leftover '(")
            return
        result.append(stack.pop())

    return result

# Evaluator helper
def eval(num1, num2, operator):
    if operator == '+':
        return num1+num2
    elif operator == '-':
        return num1-num2
    elif operator == '*':
        return num1*num2
    elif operator == '/':
        return num1/num2
    elif operator == '^':
        return num1**num2

# Function to evaluate postfix expressions
def evaluator(expr):
    stack = []
    for symbol in expr:
        # if it's not a string then it's a number, we just add onto stack
        if type(symbol) != str:
            stack.append(symbol)
        else:
            # if it's an operator and there's less than 2 numbers
            # then it's an invalid expression
            if len(stack) < 2:
                print(f"Inavlid postfix expression: {expr}")
                return
            # else, pop the last 2 elements and evaluate
            num2 = stack.pop()
            num1 = stack.pop()
            result = eval(num1, num2, symbol)
            stack.append(result)
    # if we have more than 1 number on the stack it was an
    # invalid expression
    if len(stack) != 1:
        print(f"{expr}: invalid postfix expression")
        return
    return stack.pop()
# example use case
expr = "(2.5*4+3*2.0)^1.5"
print(f"After preprocessing, {expr} becomes:")
infix = make_infix(expr)
print(infix)
postfix = convert(infix)
print("Then in postfix: ", postfix)
print("which evaluates to: %.3f" % evaluator(postfix))





