# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
from typing import List
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

    def test_slowexp(self) -> None:
        self.assertAlmostEqual(slowexp(1, 0), 1)
        self.assertAlmostEqual(slowexp(2, 0), 1)
        self.assertAlmostEqual(slowexp(-2.5, 0), 1)
        self.assertAlmostEqual(slowexp(1, 1), 1)
        self.assertAlmostEqual(slowexp(2, 1), 2)
        self.assertAlmostEqual(slowexp(-2.5, 1), -2.5)
        self.assertAlmostEqual(slowexp(1, 2), 1)
        self.assertAlmostEqual(slowexp(2, 2), 4)
        self.assertAlmostEqual(slowexp(-2.5, 2), 6.25)
        self.assertAlmostEqual(slowexp(1, 5), 1)
        self.assertAlmostEqual(slowexp(2, 5), 32)
        self.assertAlmostEqual(slowexp(-2.5, 5), -97.65625)

    def test_fastexp(self) -> None:
        self.assertAlmostEqual(fastexp(1, 0), 1)
        self.assertAlmostEqual(fastexp(2, 0), 1)
        self.assertAlmostEqual(fastexp(-2.5, 0), 1)
        self.assertAlmostEqual(fastexp(1, 1), 1)
        self.assertAlmostEqual(fastexp(2, 1), 2)
        self.assertAlmostEqual(fastexp(-2.5, 1), -2.5)
        self.assertAlmostEqual(fastexp(1, 2), 1)
        self.assertAlmostEqual(fastexp(2, 2), 4)
        self.assertAlmostEqual(fastexp(-2.5, 2), 6.25)
        self.assertAlmostEqual(fastexp(1, 5), 1)
        self.assertAlmostEqual(fastexp(2, 5), 32)
        self.assertAlmostEqual(fastexp(-2.5, 5), -97.65625)

     # ------------------------- Base conversions ------------------------------

    def test_233_2(self) -> None:
        self.assertEqual(baseconv(233, 2), '11101001')

    def test_233_8(self) -> None:
        self.assertEqual(baseconv(233, 8), '351')

    def test_233_16(self) -> None:
        self.assertEqual(baseconv(233, 16), 'e9')

    def test_233_26(self) -> None:
        self.assertEqual(baseconv(233, 26), '8p')

    def test_25_2(self) -> None:
        self.assertEqual(baseconv(25, 2), '11001')

    def test_25_8(self) -> None:
        self.assertEqual(baseconv(25, 8), '31')

    def test_25_16(self) -> None:
        self.assertEqual(baseconv(25, 16), '19')

    def test_25_26(self) -> None:
        self.assertEqual(baseconv(25, 26), 'p')

    def test_256_2(self) -> None:
        self.assertEqual(baseconv(256, 2), '100000000')
    
    def test_256_8(self) -> None:
        self.assertEqual(baseconv(256, 8), '400')

    def test_256_16(self) -> None:
        self.assertEqual(baseconv(256, 16), '100')
    
    def test_256_26(self) -> None:
        self.assertEqual(baseconv(256, 26), '9m')

    def test_26_2(self) -> None:
        self.assertEqual(baseconv(26, 2), '11010')

    def test_26_8(self) -> None:
        self.assertEqual(baseconv(26, 8), '32')

    def test_26_16(self) -> None:
        self.assertEqual(baseconv(26, 16), '1a')

    def test_26_26(self) -> None:
        self.assertEqual(baseconv(26, 26), '10')

    def test_0_10(self) -> None:
        self.assertEqual(baseconv(0, 10), '0')

    def test_big_base(self) -> None:
        with self.assertRaises(AssertionError):
            baseconv(233, 37)

    def test_small_base(self) -> None:
        with self.assertRaises(AssertionError):
            baseconv(233, 1)

    def test_neg_num(self) -> None:
        with self.assertRaises(AssertionError):
            baseconv(-1, 16)


    #------------ Fibonacci ------------------------------
    def test_fib_neg(self) -> None:
        with self.assertRaises(AssertionError):
            fibonacci(-1)

    def test_fib_n(self) -> None:
        expected:List[int] = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233,377, 610, 987, 1597, 2584, 4181, 6765,
        10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040,
        1346269, 2178309, 3524578, 5702887, 9227465]
        for i in range(len(expected)):
            with self.subTest(i=i):
                self.assertEqual(fibonacci(i), expected[i])

    def test_fib_50(self) -> None:
        self.assertEqual(fibonacci(50), 12586269025)

if __name__ == '__main__':
    unittest.main()