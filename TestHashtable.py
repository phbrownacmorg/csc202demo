# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
from typing import List
from Hashtable import Hashtable

class TestHashtable(unittest.TestCase):

    def setUp(self) -> None:
        self._empty:Hashtable[str] = Hashtable[str](3)

        self._4items = Hashtable[str]()
        self._4items.put('foo')
        self._4items.put('bar')
        self._4items.put('oogba')
        self._4items.put('ignatz')

    def test_contains_empty(self) -> None:
        self.assertFalse('foo' in self._empty)
        
    def test_contains_foo(self) -> None:
        self.assertTrue('foo' in self._4items)

    def test_contains_bar(self) -> None:
        self.assertTrue('bar' in self._4items)

    def test_contains_oogba(self) -> None:
        self.assertTrue('oogba' in self._4items)

    def test_contains_iggy(self) -> None:
        self.assertTrue('ignatz' in self._4items)

    def test_contains_baz(self) -> None:
        self.assertFalse('baz' in self._4items)

    def test_get_present(self) -> None:
        items:List[str] = ['foo', 'bar', 'oogba', 'ignatz']
        for item in items:
            with self.subTest(item=item):
                self.assertEqual(self._4items.get(item), item)

    def test_get_absent(self) -> None:
        self.assertEqual(self._empty.get('baz'), None)
        self.assertEqual(self._4items.get('baz'), None)
    
if __name__ == '__main__':
    unittest.main()