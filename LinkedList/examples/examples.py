from LinkedList.Singly_Linked_List import SinglyLinkedList


class Example:
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

    def count_occurences_iterative(self):
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

    def sum_two_lists(self, list):
        p = self.singly_linked_list.head
        q = list.head

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