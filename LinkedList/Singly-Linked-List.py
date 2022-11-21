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