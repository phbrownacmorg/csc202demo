# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
from BST import BST
from typing import cast

class TestBST(unittest.TestCase):
    def setUp(self) -> None:
        self._1node:BST[int] = BST[int](34)     #  34

        self._3nodes:BST[int] = BST[int](34)    #     34
        self._3nodes.add(47)                    #    /  \
        self._3nodes.add(31)                    #  31    47

        self._6nodes:BST[int] = BST[int](34)    #       34
        self._6nodes.add(47)                    #      /  \
        self._6nodes.add(31)                    #    31    47
        self._6nodes.add(6)                     #   /        \
        self._6nodes.add(15)                    #  6          70
        self._6nodes.add(70)                    #   \
                                                #    15

    def test_contains1(self) -> None:
        self.assertTrue(34 in self._1node)
        self.assertFalse(31 in self._1node)

    def test_contains3(self) -> None:
        self.assertTrue(34 in self._3nodes)
        self.assertTrue(31 in self._3nodes)
        self.assertTrue(47 in self._3nodes)
        self.assertFalse(6 in self._3nodes)

    def test_contains6(self) -> None:
        self.assertTrue(34 in self._6nodes)
        self.assertTrue(31 in self._6nodes)
        self.assertTrue(47 in self._6nodes)
        self.assertTrue(6 in self._6nodes)
        self.assertTrue(15 in self._6nodes)
        self.assertTrue(70 in self._6nodes)
        self.assertFalse(57 in self._6nodes)

    def testSuccessor(self) -> None:
        self.assertEqual(self._1node.findSuccessor(), None)


if __name__ == '__main__':
    unittest.main()