import unittest


def look_and_say(next_number):
    new_str = ''
    i = 0
    while i < len(next_number):
        char_count = 1
        char = next_number[i]
        while i < len(next_number) - 1 and next_number[i + 1] == char:
            char_count += 1
            i += 1
        new_str += f'{char_count}' + char
        i += 1
    return new_str


def print_look_and_say(next_number, repeat_num):
    results = [int(next_number)]
    for i in range(repeat_num - 1):
        next_number = look_and_say(next_number)
        results.append(int(next_number))
    return results


class MyTestCase(unittest.TestCase):
    def test_look_and_say(self):
        self.assertEqual(print_look_and_say('1', 6), [1, 11, 21, 1211, 111221, 312211])
        self.assertEqual(print_look_and_say('1', 7), [1, 11, 21, 1211, 111221, 312211, 13112221])
        self.assertEqual(print_look_and_say('1', 8), [1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211])


if __name__ == '__main__':
    unittest.main()
