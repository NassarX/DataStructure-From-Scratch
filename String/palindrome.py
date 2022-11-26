import unittest


def is_palindrome(string, start, end) -> bool:
    if start > len(string) // 2:
        return True

    if string[start] != string[end]:
        return False

    return is_palindrome(string, start + 1, end - 1)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(is_palindrome("Was it a cat I saw".replace(" ", "").lower(), 0, -1), True)  # add assertion here


if __name__ == '__main__':
    unittest.main()