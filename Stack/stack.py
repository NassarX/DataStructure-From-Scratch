"""
Stack Data Structure.
"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """ Check if stack empty

        :return: boolean
        """
        if not self.items:
            return True
        else:
            return False

    def push(self, item):
        """ Push item onto the stack.

        :param item: Item to be pushed onto stack.
        """
        self.items.append(item)

    def pop(self):
        """ Pop last inserted item onto stack.

        :return: pop-ed item
        """
        if len(self.items) != 0:
            return self.items.pop()
        else:
            print("Stack is empty")

    def remove_by_val(self, item):
        """ Removes first occurrence of the item from the stack.

        :param item:
        :return:
        """

        if len(self.items) != 0:
            try:
                self.items.remove(item)
            except:
                print(f"Item {item} not in the stack")
        else:
            print("Stack is empty")

    def remove_by_index(self, index):
        """ Remove items by index.

        :param index:
        :return:
        """

        if len(self.items) != 0:
            try:
                del self.items[int(index)]
            except:
                print(f"Item  at index : {index} not in the stack")
        else:
            print("Stack is empty")

    def clear(self):
        """ Removes all items from the stack.

        :return:
        """
        self.items.clear()

    def peek(self):
        """ Returns top iem on the stack.

        :return:
        """
        if len(self.items) != 0:
            return self.items[len(self.items) - 1]
        else:
            print("Stack is empty")

    def display(self):
        return self.items


# __main__
s = Stack()
c = 0
while c != 7:
    print('\tSTACK OPERATIONS')
    print('1.Push  2.Pop  3.Remove By Value  4.Remove By Index  5.Peek  6.Display Stack  7.Exit')
    c = int(input('Enter your choice(1-6): '))
    if c == 1:
        x = input("Enter the item: ")
        s.push(x)
    elif c == 2:
        print(s.pop())
    elif c == 3:
        x = input("Enter the item value: ")
        s.remove_by_val(x)
    elif c == 4:
        x = input("Enter the item index: ")
        s.remove_by_index(x)
    elif c == 5:
        print(s.peek())
    elif c == 6:
        print(s.display())
    elif c == 7:
        print('Bye')
    else:
        print('Wrong Choice! Choose from 1 to 6 only')
