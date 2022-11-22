from LinkedList.Singly_Linked_List import SinglyLinkedList
from LinkedList.doubly_Linked_List import DoublyLinkedList
from LinkedList.Singly_Linked_List import Node as SinglyNode


class DoublyOperations:
    def __init__(self):
        self.doubly_linked_list = DoublyLinkedList()

    def find_nth_from_last(self, n):
        length = self.doubly_linked_list.length()
        curr = self.doubly_linked_list.head
        node = None
        while curr:
            if length == n:
                node = curr
            length -= 1
            curr = curr.next
        return node

    def count_occurrences_iterative(self):
        curr = self.doubly_linked_list.head
        occur_dic = dict()
        while curr:
            occur_dic[curr.data] = occur_dic.get(curr.data, 0) + 1
            curr = curr.next
        print(occur_dic)

    def rotate(self, k):
        prev = None
        p = self.doubly_linked_list.head
        q = self.doubly_linked_list.head
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

        q.next = self.doubly_linked_list.head
        self.doubly_linked_list.head = p.next
        p.next.prev = None
        p.next = None

    def is_palindrome(self):
        # Solution 2:
        p = self.doubly_linked_list.head
        s = []
        while p:
            s.append(p.data)
            p = p.next
        p = self.doubly_linked_list.head
        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True

    def move_tail_to_head(self):
        prev = None
        q = self.doubly_linked_list.head
        while q.next:
            prev = q
            q = q.next

        q.next = self.doubly_linked_list.head
        q.prev = None
        self.doubly_linked_list.head = q
        prev.next = None

    def move_tail_to_head_2(self):
        prev = self.find_nth_from_last(2)
        last = self.find_nth_from_last(1)

        last.next = self.doubly_linked_list.head
        last.prev = None
        self.doubly_linked_list.head = last
        prev.next = None

    def sum_two_lists(self, llist):
        p = self.doubly_linked_list.head
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
        if not self.doubly_linked_list.head:
            return False

        if data_1 == data_2:
            return

        left_node_parent = None
        left_node = self.doubly_linked_list.head
        while left_node and left_node.data != data_1:
            left_node_parent = left_node
            left_node = left_node.next

        right_node_parent = None
        right_node = self.doubly_linked_list.head
        while right_node and right_node.data != data_2:
            right_node_parent = right_node
            right_node = right_node.next

        left_node_parent.next, right_node_parent.next = right_node, left_node
        left_node.next, right_node.next = right_node.next, left_node.next
        left_node.prev, right_node.prev = right_node.prev, left_node.prev

    def reverse_iterative(self):

        # initialize variables
        prev = None  # `previous` initially points to None
        cur = self.doubly_linked_list.head  # `current` points at the first element
        next_node = cur.next  # `following` points at the second element

        # go till the last element of the list
        while cur:
            cur.next = prev  # reverse the link
            cur.prev = cur.next
            prev = cur  # move `previous` one step ahead
            cur = next_node  # move `current` one step ahead
            if next_node:  # if this was not the last element
                next_node = next_node.next  # move `following` one step ahead

        self.doubly_linked_list.head = prev

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            next_node = cur.next  # `following` points at the second element
            cur.next = prev  # reverse the link
            cur.prev = cur.next  # reverse the link
            prev = cur  # move `previous` one step ahead
            cur = next_node  # move `current` one step ahead
            if next_node:  # if this was not the last element
                next_node = next_node.next  # move `following` one step ahead
            return _reverse_recursive(cur, prev)

        self.doubly_linked_list.head = _reverse_recursive(cur=self.doubly_linked_list.head, prev=None)

    def merge(self, list_2):
        list_1 = self.doubly_linked_list.head
        list_2 = list_2.head
        # Node for output LinkedList
        head_ptr = temp_ptr = SinglyNode()  # head_ptr will be the head node of the output list
        # temp_ptr will be used to insert nodes in the output list

        # Loop for merging two lists
        # Loop terminates when both lists reaches to its end
        while list_1 or list_2:
            # list_1 has not reached its end
            # and list_2 has either reached its end or its current node has data
            # greater than or equal to the data of list_1 node
            # than insert list_1 node in the output list
            if list_1 and (not list_2 or list_1.data <= list_2.data):
                temp_ptr.next = SinglyNode(list_1.data)
                list_1 = list_1.next
            # otherwise insert list_2 node in the output list
            else:
                temp_ptr.next = SinglyNode(list_2.data)
                list_2 = list_2.next
            # move temp_pointer to next position
            temp_ptr = temp_ptr.next
        # return output list
        return head_ptr.next

    def remove_duplicates(self):
        cur = self.doubly_linked_list.head
        prev = None
        dup_values = dict()

        while cur:
            if cur.data in dup_values:
                # Remove node:
                cur.prev.next = cur.next
                cur = None
            else:
                # Have not encountered element before.
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next

    def delete_at_head(self):
        cur = self.doubly_linked_list.head
        if not self.doubly_linked_list.head:
            return False

        cur.prev = None
        self.doubly_linked_list.head = cur.next
        return

    def delete_node_at_pos(self, pos):
        cur = self.doubly_linked_list.head
        if self.doubly_linked_list.head is None:
            return False

        if pos == 0:
            self.doubly_linked_list.head = cur.next
            return

        index = 0
        while cur:
            if pos == index:
                nxt = cur.next
                prev = cur.prev
                nxt.prev = prev
                prev.next = nxt
                return
            index += 1
            cur = cur.next

    def pairs_with_sum(self, sum_val):
        p = self.doubly_linked_list.head
        q = p.next

        if not p:
            return False

        results = []
        while p and q:
            while q:
                if p.data + q.data == sum_val:
                    r = (p.data, q.data)
                    results.append(r)
                q = q.next
            p = p.next
            q = p.next
        return results
