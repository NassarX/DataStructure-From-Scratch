"""
InfixToPostfix class.
"""

from Stack.stack import Stack


def is_operand(char):
    return (ord('a') <= ord(char) <= ord('z')) or (ord('A') <= ord(char) <= ord('Z'))


def precedence(char):
    if char == '+' or char == '-':
        return 1
    elif char == '*' or char == '/':
        return 2
    elif char == '^':
        return 3
    else:
        return -1


def infix_to_postfix(expression):
    tmp_stack = Stack()
    postfix = []

    for i in range(len(expression)):
        char = expression[i]
        if is_operand(char):
            postfix.append(char)
        elif char == "(":
            tmp_stack.push(char)
        elif char == ")":
            while not tmp_stack.is_empty() and tmp_stack.peek() != "(":
                postfix.append(tmp_stack.pop())
            tmp_stack.pop()
        else:
            while not tmp_stack.is_empty() and precedence(tmp_stack.peek()) >= precedence(char):
                postfix.append(tmp_stack.pop())
            tmp_stack.push(char)

    while not tmp_stack.is_empty():
        postfix.append(tmp_stack.pop())
    return ''.join(postfix)


infix = "a+b*(c^d-e)^(f+g*h)-i"
print("infix: " + infix)
postfix = infix_to_postfix(infix)
print("postfix: " + postfix)
