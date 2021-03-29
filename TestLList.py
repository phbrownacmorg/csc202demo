# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
from LList import LList

class TestLList(unittest.TestCase):
    def setUp(self) -> None:
        self._empty = LList[str]()

        self._one = LList[str]()
        self._one.add('foo')

        self._two = LList[str]()
        self._two.add('bar')
        self._two.add('foo')

    def test_empty(self) -> None:
        self.assertTrue(self._empty.isEmpty())

    def test_empty_not(self) -> None:
        self.assertFalse(self._one.isEmpty())

    def test_str_empty(self) -> None:
        self.assertEqual('∅', str(self._empty))

    def test_str_one(self) -> None:
        self.assertEqual(str(self._one), '❬foo❭➞∅')

    def test_str_two(self) -> None:
        self.assertEqual(str(self._two), '❬bar❭➞❬foo❭➞∅')

    def test_size_0(self) -> None:
        self.assertEqual(self._empty.size(), 0)

    def test_size_0(self) -> None:
        self.assertEqual(self._empty.size(), 0)

    def test_size_1(self) -> None:
        self.assertEqual(self._one.size(), 1)

    def test_size_2(self) -> None:
        self.assertEqual(self._two.size(), 2)

    def test_search_empty(self) -> None:
        self.assertFalse(self._empty.search('foo'))

    def test_search_one_yes(self) -> None:
        self.assertTrue(self._one.search('foo'))

    def test_search_one_no(self) -> None:
        self.assertFalse(self._one.search('bar'))

    def test_search_two_foo(self) -> None:
        self.assertTrue(self._two.search('foo'))

    def test_search_two_bar(self) -> None:
        self.assertTrue(self._two.search('bar'))

    def test_search_two_other(self) -> None:
        self.assertFalse(self._two.search('other'))

    def test_pop_empty(self) -> None:
        with self.assertRaises(AssertionError):
            self._empty.pop()

    def test_pop_one(self) -> None:
        self.assertEqual(self._one.pop(), 'foo')
        self.assertTrue(self._one.isEmpty())

    def test_pop_two(self) -> None:
        self.assertEqual(self._two.pop(), 'foo')
        self.assertEqual(str(self._two), '❬bar❭➞∅')
        self.assertEqual(self._two.pop(), 'bar')
        self.assertTrue(self._two.isEmpty())

    def test_popn_two_n2(self) -> None:
        with self.assertRaises(AssertionError):
            self._two.pop(-2)

    def test_popn_two_2(self) -> None:
        with self.assertRaises(AssertionError):
            self._two.pop(2)

    def test_popn_two_0(self) -> None:
        self.assertEqual(self._two.pop(0), 'bar')
        self.assertEqual(str(self._two), '❬foo❭➞∅')

if __name__ == '__main__':
    unittest.main()