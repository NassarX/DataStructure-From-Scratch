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
        """ Returns top item on the stack.

        :return:
        """
        if len(self.items) != 0:
            return self.items[len(self.items) - 1]
        else:
            return False

    def display(self):
        """ Returns stack contents

        :return:
        """
        return self.items

    def __str__(self):
        """ For printing the stack contents

        :return:
        """
        return ' '.join([str(i) for i in self.items])