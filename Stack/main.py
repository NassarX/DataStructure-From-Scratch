from examples.balanced_brackets import BalancedBrackets
from examples.decimal_to_binary import DecimalToBinary


class Main:
    balanced_brackets = BalancedBrackets()
    print(balanced_brackets.is_balanced())

    dec_bin = DecimalToBinary()
    decimal_number = int(input("Please enter number to convert to Binary: "))
    print(dec_bin.convert_int_to_bin(int(decimal_number)))
