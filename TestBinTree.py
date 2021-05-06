# Unit tests for BinTree
# Peter Brown, 4 May 2021

import unittest
from typing import cast
from BinTree import BinTree

class TestBinTree(unittest.TestCase):

    def setUp(self) -> None:
        self._1node:BinTree[str] = BinTree[str]('a')                   #      a

        self._3nodes:BinTree[str] = BinTree[str]('a')                  #      a      
        self._3nodes.addLeft('b')                    #     /  \
        self._3nodes.addRight('c')                   #    b    c

        self._6nodes:BinTree[str] = BinTree[str]('a')                                 #
        self._6nodes.addLeft('b')                                   #          a
        self._6nodes.addRight('c')                                  #       /      \
        cast(BinTree[str], self._6nodes.leftChild()).addRight('d')       #    b          c
        cast(BinTree[str], self._6nodes.rightChild()).addLeft('e')       #     \        / \
        cast(BinTree[str], self._6nodes.rightChild()).addRight('f')      #      d      e   f

    def test_hasLeft(self) -> None:
        self.assertFalse(self._1node.hasLeftChild())
        self.assertTrue(self._3nodes.hasLeftChild())

    def test_hasRight(self) -> None:
        self.assertFalse(self._1node.hasRightChild())
        self.assertTrue(self._3nodes.hasRightChild())

    def test_getData(self) -> None:
        self.assertEqual(self._1node.data(), 'a')

        self.assertEqual(self._3nodes.data(), 'a')
        leftChild:BinTree[str] = cast(BinTree[str], self._3nodes.leftChild())
        rightChild:BinTree[str] = cast(BinTree[str], self._3nodes.rightChild())
        self.assertEqual(leftChild.data(), 'b')
        self.assertEqual(rightChild.data(), 'c')

        self.assertEqual(self._6nodes.data(), 'a')
        leftChild = cast(BinTree[str], self._6nodes.leftChild())
        rightChild = cast(BinTree[str], self._6nodes.rightChild())
        self.assertEqual(leftChild.data(), 'b')
        self.assertEqual(rightChild.data(), 'c')
        left_rightChild:BinTree[str] = cast(BinTree[str], leftChild.rightChild())
        right_leftChild:BinTree[str] = cast(BinTree[str], rightChild.leftChild())
        right_rightChild:BinTree[str] = cast(BinTree[str], rightChild.rightChild())
        self.assertEqual(left_rightChild.data(), 'd')
        self.assertEqual(right_leftChild.data(), 'e')
        self.assertEqual(right_rightChild.data(), 'f')

    def test_addLeft_noChild(self) -> None:
        self.assertFalse(self._1node.hasLeftChild())
        self._1node.addLeft('z')
        self.assertTrue(self._1node.hasLeftChild())
        leftChild:BinTree[str] = cast(BinTree[str], self._1node.leftChild())
        self.assertEqual(leftChild.data(), 'z')

    def test_addLeft_Child(self) -> None:
        self.assertTrue(self._3nodes.hasLeftChild())
        leftChild:BinTree[str] = cast(BinTree[str], self._3nodes.leftChild())
        self.assertEqual(leftChild.data(), 'b')
        self.assertFalse(leftChild.hasLeftChild())

        self._3nodes.addLeft('x')
        self.assertTrue(self._3nodes.hasLeftChild())
        leftChild = cast(BinTree[str], self._3nodes.leftChild())
        self.assertEqual(leftChild.data(), 'x')
        self.assertTrue(leftChild.hasLeftChild())
        left_leftChild:BinTree[str] = cast(BinTree[str], leftChild.leftChild())
        self.assertEqual(left_leftChild.data(), 'b')

    def test_addRight_noChild(self) -> None:
        self.assertFalse(self._1node.hasRightChild())
        self._1node.addRight('y')
        self.assertTrue(self._1node.hasRightChild())
        rightChild:BinTree[str] = cast(BinTree[str], self._1node.rightChild())
        self.assertEqual(rightChild.data(), 'y')

    def test_addRight_Child(self) -> None:
        self.assertTrue(self._3nodes.hasRightChild())
        rightChild:BinTree[str] = cast(BinTree[str], self._3nodes.rightChild())
        self.assertEqual(rightChild.data(), 'c')
        self.assertFalse(rightChild.hasRightChild())

        self._3nodes.addRight('w')
        self.assertTrue(self._3nodes.hasRightChild())
        rightChild = cast(BinTree[str], self._3nodes.rightChild())
        self.assertEqual(rightChild.data(), 'w')
        self.assertTrue(rightChild.hasRightChild())
        right_rightChild:BinTree[str] = cast(BinTree[str], rightChild.rightChild())
        self.assertEqual(right_rightChild.data(), 'c')

    def test_len(self) -> None:
        self.assertEqual(len(self._1node), 1)  
        self.assertEqual(len(self._3nodes), 3)  
        self.assertEqual(len(self._6nodes), 6) 

if __name__ == '__main__':
    unittest.main()