# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
from searching import sequential, binsearch
from typing import List

class TestSearch(unittest.TestCase):

    def setUp(self) -> None:
        self.array:List[int] = list(range(0, 100, 2)) # Even numbers from 0 to 100

    def test_sequential_found(self) -> None:
        for i in range(0, 100, 2):
            with self.subTest(i=i):
                self.assertEqual(sequential(self.array, i), i / 2)

    def test_sequential_not_found(self) -> None:
        for i in range(-1, 102, 2):  # Odd numbers from -1 up through 101
            with self.subTest(i=i):
                self.assertEqual(sequential(self.array, i), None)

    def test_binsearch_found(self) -> None:
        for i in range(0, 100, 2):
            with self.subTest(i=i):
                self.assertEqual(binsearch(self.array, i), i / 2)

    def test_binsearch_not_found(self) -> None:
        for i in range(-1, 102, 2):  # Odd numbers from -1 up through 101
            with self.subTest(i=i):
                self.assertEqual(binsearch(self.array, i), None)



if __name__ == '__main__':
    unittest.main()