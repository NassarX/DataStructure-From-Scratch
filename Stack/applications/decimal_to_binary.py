"""
DecimalToBinary class.
"""

from Stack.stack import Stack


class DecimalToBinary:
    stack = Stack()

    def convert_int_to_bin(self, dec_num):
        if dec_num / 2 != 0:
            r = dec_num % 2
            self.stack.push(r)
            dec_num = int(dec_num / 2)
            self.convert_int_to_bin(dec_num)

        binary_list = self.stack.display()
        binary_list.reverse()
        return ''.join(str(x) for x in binary_list)
