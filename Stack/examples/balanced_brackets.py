"""
BalancedBrackets class.
"""

from Stack.stack import Stack


class BalancedBrackets:
    brackets_stack = Stack()

    opening_brackets = ['{', '(', '[']
    closing_brackets = ['}', ')', ']']

    def is_balanced(self):
        brackets_string = input("Please enter your brackets: ")
        brackets_list = [*brackets_string]
        is_balanced = True

        index = 0
        while index < len(brackets_list) and is_balanced:
            bracket = brackets_list[index]

            if bracket in self.opening_brackets + self.closing_brackets:
                if bracket in self.closing_brackets:
                    if self.brackets_stack.is_empty() \
                            or self.closing_brackets.index(bracket) \
                            != self.opening_brackets.index(self.brackets_stack.peek()):
                        is_balanced = False
                        break
                    else:
                        self.brackets_stack.pop()
                else:
                    self.brackets_stack.push(bracket)

            index += 1

        return "Balanced" if is_balanced else "In-Balanced"
