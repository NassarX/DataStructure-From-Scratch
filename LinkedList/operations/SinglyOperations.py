from LinkedList.Singly_Linked_List import SinglyLinkedList
from LinkedList.Singly_Linked_List import Node


class SinglyOperations:
    def __init__(self):
        self.singly_linked_list = SinglyLinkedList()

    def find_nth_from_last(self, n):
        length = self.singly_linked_list.length()
        curr = self.singly_linked_list.head
        node = None
        while curr:
            if length == n:
                node = curr
            length -= 1
            curr = curr.next
        return node

    def count_occurrences_iterative(self):
        curr = self.singly_linked_list.head
        occur_dic = dict()
        while curr:
            occur_dic[curr.data] = occur_dic.get(curr.data, 0) + 1
            curr = curr.next
        print(occur_dic)

    def rotate(self, k):
        prev = None
        p = self.singly_linked_list.head
        q = self.singly_linked_list.head
        count = 0
        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count += 1
        p = prev  # on the pivot node
        while q:
            prev = q
            q = q.next
        q = prev  # last node

        q.next = self.singly_linked_list.head
        self.singly_linked_list.head = p.next
        p.next = None

    def is_palindrome(self):
        # Solution 2:
        p = self.singly_linked_list.head
        s = []
        while p:
            s.append(p.data)
            p = p.next
        p = self.singly_linked_list.head
        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True

    def move_tail_to_head(self):
        prev = None
        q = self.singly_linked_list.head
        while q.next:
            prev = q
            q = q.next

        q.next = self.singly_linked_list.head
        self.singly_linked_list.head = q
        prev.next = None

    def move_tail_to_head_2(self):
        prev = self.find_nth_from_last(2)
        last = self.find_nth_from_last(1)

        last.next = self.singly_linked_list.head
        self.singly_linked_list.head = last
        prev.next = None

    def sum_two_lists(self, llist):
        p = self.singly_linked_list.head
        q = llist.head

        i = 1
        total_sum = 0
        while p or q:
            digit_1 = 0 if not p else int(p.data)
            digit_2 = 0 if not q else int(q.data)
            sum_ = i * (digit_1 + digit_2)
            total_sum += sum_
            i *= 10
            p = p if not p else p.next
            q = q if not q else q.next

        new_list = SinglyLinkedList()
        sum_digits = [int(d) for d in str(total_sum)]
        sum_digits.reverse()
        for digit in sum_digits:
            new_list.append(digit)

        return new_list.display()

    def swap_nodes(self, data_1, data_2):
        if not self.singly_linked_list.head:
            return False

        if data_1 == data_2:
            return

        left_node_parent = None
        left_node = self.singly_linked_list.head
        while left_node and left_node.data != data_1:
            left_node_parent = left_node
            left_node = left_node.next

        right_node_parent = None
        right_node = self.singly_linked_list.head
        while right_node and right_node.data != data_2:
            right_node_parent = right_node
            right_node = right_node.next

        left_node_parent.next, right_node_parent.next = right_node, left_node
        left_node.next, right_node.next = right_node.next, left_node.next

    def reverse_iterative(self):

        # initialize variables
        prev = None  # `previous` initially points to None
        cur = self.singly_linked_list.head  # `current` points at the first element
        next_node = cur.next  # `following` points at the second element

        # go till the last element of the list
        while cur:
            cur.next = prev  # reverse the link
            prev = cur  # move `previous` one step ahead
            cur = next_node  # move `current` one step ahead
            if next_node:  # if this was not the last element
                next_node = next_node.next  # move `following` one step ahead

        self.singly_linked_list.head = prev

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

        self.singly_linked_list.head = _reverse_recursive(cur=self.singly_linked_list.head, prev=None)

    def merge(self, list_2):
        list_1 = self.singly_linked_list.head
        list_2 = list_2.head
        # Node for output LinkedList
        head_ptr = temp_ptr = Node()  # head_ptr will be the head node of the output list
        # temp_ptr will be used to insert nodes in the output list

        # Loop for merging two lists
        # Loop terminates when both lists reaches to its end
        while list_1 or list_2:
            # list_1 has not reached its end
            # and list_2 has either reached its end or its current node has data
            # greater than or equal to the data of list_1 node
            # than insert list_1 node in the output list
            if list_1 and (not list_2 or list_1.data <= list_2.data):
                temp_ptr.next = Node(list_1.data)
                list_1 = list_1.next
            # otherwise insert list_2 node in the output list
            else:
                temp_ptr.next = Node(list_2.data)
                list_2 = list_2.next
            # move temp_pointer to next position
            temp_ptr = temp_ptr.next
        # return output list
        return head_ptr.next

    def remove_duplicates(self):
        cur = self.singly_linked_list.head
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

    def delete_at_head(self):
        cur = self.singly_linked_list.head
        if not self.singly_linked_list.head:
            return False

        self.singly_linked_list.head = cur.next
        return

    def delete_node_by_vale(self, data):
        cur = self.singly_linked_list.head

        if self.singly_linked_list.head is None:
            return False

        while cur is not None:
            next_node = cur.next
            if next_node.data == data:
                cur.next = next_node.next
                break
            cur = cur.next

    def delete_node_at_pos(self, pos):
        cur = self.singly_linked_list.head
        if self.singly_linked_list.head is None:
            return False

        if pos == 0:
            self.singly_linked_list.head = cur.next
            return

        index = 0
        while cur is not None:
            next_node = cur.next
            if (index + 1) == pos:
                cur.next = next_node.next
                break
            cur = cur.next
            index += 1
