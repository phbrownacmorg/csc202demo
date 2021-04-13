# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
from recursion_demo import *
from LList import LList

class TestRecursion(unittest.TestCase):
    def test_sum_python_list_empty(self) -> None:
        self.assertEqual(sum_python_list([]), 0)
        
    def test_sum_python_list_1_item(self) -> None:
        self.assertEqual(sum_python_list([53]), 53)

    def test_sum_python_list_2_items(self) -> None:
        self.assertEqual(sum_python_list([53, 21]), 74)

    def test_sum_python_list_neg(self) -> None:
        self.assertEqual(sum_python_list([53, -21]), 32)

    def test_sum_python_list_neg_2(self) -> None:
        self.assertEqual(sum_python_list([-53, -21]), -74)

    def test_sum_LList_empty(self) -> None:
        self.assertEqual(sum_LList(LList[int]()), 0)

    def test_sum_LList_1_item(self) -> None:
        numlist:LList[int] = LList[int]()
        numlist.add(53)
        self.assertEqual(sum_LList(numlist), 53)

    def test_sum_LList_2_item(self) -> None:
        numlist:LList[int] = LList[int]()
        numlist.add(53)
        numlist.add(21)
        self.assertEqual(sum_LList(numlist), 74)

    def test_sum_LList_neg(self) -> None:
        numlist:LList[int] = LList[int]()
        numlist.add(53)
        numlist.add(-21)
        self.assertEqual(sum_LList(numlist), 32)

    def test_sum_LList_neg_2(self) -> None:
        numlist:LList[int] = LList[int]()
        numlist.add(-53)
        numlist.add(-21)
        self.assertEqual(sum_LList(numlist), -74)

    def test_strrev(self) -> None:
        self.assertEqual(strrev(""), "")
        self.assertEqual(strrev("a"), "a")
        self.assertEqual(strrev("ab"), "ba")
        self.assertEqual(strrev("ab"), "ba")
        self.assertEqual(strrev('ABBA'), 'ABBA')
        self.assertEqual(strrev('Wassamassaw'), 'wassamassaW')
        self.assertEqual(strrev('Spartanburg'), 'grubnatrapS')

    def test_gcd(self) -> None:
        self.assertEqual(gcd(1, 0), 1)
        self.assertEqual(gcd(0, 1), 1)
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(15, 12), 3)
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(15, 12), 3)
        self.assertEqual(gcd(4, 3), 1)
        self.assertEqual(gcd(3, 4), 1)
        self.assertEqual(gcd(3, 0), 3)
        self.assertEqual(gcd(0, 3), 3)
        self.assertEqual(gcd(-12, 15), 3)
        self.assertEqual(gcd(-12, -15), 3)
        self.assertEqual(gcd(12, -15), 3)


if __name__ == '__main__':
    unittest.main()