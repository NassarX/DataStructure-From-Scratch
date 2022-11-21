"""
------------------------ Singly Linked List -------------------------
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        The append method will insert an element at the end of the linked list.

        :param data:
        :return:
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node_data, data):
        cur = self.head

        if self.head is None:
            return False

        new_node = Node(data)
        while cur is not None:
            if cur.data == prev_node_data:
                new_node.next = cur.next
                cur.next = new_node
            cur = cur.next

    def insert_before_node(self, next_node_data, data):
        cur = self.head

        if self.head is None:
            return False

        new_node = Node(data)
        while cur is not None:
            next_node = cur.next
            if next_node.data == next_node_data:
                new_node.next = next_node
                cur.next = new_node
                break
            cur = cur.next

    def length(self):
        """
        Returns length of the linkedlist

        :return:
        """
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def display(self):
        nodes_data = []
        cur = self.head
        while cur is not None:
            nodes_data.append(cur.data)
            cur = cur.next
        return nodes_data

    def get(self, index):
        if index >= self.length():
            return "ERROR : index out of range!"
        idx = 0
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            if idx == index:
                return cur.data
            idx += 1

    def delete_node_by_vale(self, data):
        cur = self.head

        if self.head is None:
            return False

        while cur is not None:
            next_node = cur.next
            if next_node.data == data:
                cur.next = next_node.next
                break
            cur = cur.next

    def delete_node_at_pos(self, pos):
        cur = self.head
        if self.head is None:
            return False

        if pos == 0:
            self.head = cur.next
            return

        index = 0
        while cur is not None:
            next_node = cur.next
            if (index + 1) == pos:
                cur.next = next_node.next
                break
            cur = cur.next
            index += 1

    def swap_nodes(self, data_1, data_2):
        if self.head is None:
            return False

        if data_1 == data_2:
            return

        left_node_parent = None
        left_node = self.head
        while left_node and left_node.data != data_1:
            left_node_parent = left_node
            left_node = left_node.next

        right_node_parent = None
        right_node = self.head
        while right_node and right_node.data != data_2:
            right_node_parent = right_node
            right_node = right_node.next

        left_node_parent.next, right_node_parent.next = right_node, left_node
        left_node.next, right_node.next = right_node.next, left_node.next

    def reverse_iterative(self):

        # initialize variables
        prev = None  # `previous` initially points to None
        cur = self.head  # `current` points at the first element
        next_node = cur.next  # `following` points at the second element

        # go till the last element of the list
        while cur:
            cur.next = prev  # reverse the link
            prev = cur  # move `previous` one step ahead
            cur = next_node  # move `current` one step ahead
            if next_node:  # if this was not the last element
                next_node = next_node.next  # move `following` one step ahead

        self.head = prev

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            next_node = cur.next  # `following` points at the second element
            cur.next = prev  # reverse the link
            prev = cur  # move `previous` one step ahead
            cur = next_node  # move `current` one step ahead
            if next_node:  # if this was not the last element
                next_node = next_node.next  # move `following` one step ahead
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    def merge(self, List_2):
        List_1 = self.head
        List_2 = List_2.head
        # Node for output LinkedList
        head_ptr = temp_ptr = Node()  # head_ptr will be the head node of the output list
        # temp_ptr will be used to insert nodes in the output list

        # Loop for merging two lists
        # Loop terminates when both lists reaches to its end
        while List_1 or List_2:
            # List_1 has not reached its end
            # and List_2 has either reached its end or its current node has data
            # greater than or equal to the data of List_1 node
            # than insert List_1 node in the ouput list
            if List_1 and (not List_2 or List_1.data <= List_2.data):
                temp_ptr.next = Node(List_1.data)
                List_1 = List_1.next
            # otherwise insert List_2 node in the ouput list
            else:
                temp_ptr.next = Node(List_2.data)
                List_2 = List_2.next
            # move temp_pointer to next position
            temp_ptr = temp_ptr.next
        # return output list
        return head_ptr.next

    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = dict()

        while cur:
            if cur.data in dup_values:
                # Remove node:
                prev.next = cur.next
                cur = None
            else:
                # Have not encountered element before.
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next