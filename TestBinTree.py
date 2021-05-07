# Unit tests for BinTree
# Peter Brown, 4 May 2021

import unittest
from typing import cast, List
from BinTree import BinTree

class TestBinTree(unittest.TestCase):

    def setUp(self) -> None:
        self._1node:BinTree[str] = BinTree[str]('a')     #      a

        self._3nodes:BinTree[str] = BinTree[str]('a')    #      a      
        self._3nodes.addLeft('b')                        #     /  \
        self._3nodes.addRight('c')                       #    b    c

        self._6nodes:BinTree[str] = BinTree[str]('a')    #
        self._6nodes.addLeft('b')                        #          a
        self._6nodes.addRight('c')                       #       /      \
        self._6nodes.leftChild().addRight('d')           #    b          c
        self._6nodes.rightChild().addLeft('e')           #     \        / \
        self._6nodes.rightChild().addRight('f')          #      d      e   f

    def test_hasLeft(self) -> None:
        self.assertFalse(self._1node.hasLeftChild())
        self.assertTrue(self._3nodes.hasLeftChild())

    def test_hasRight(self) -> None:
        self.assertFalse(self._1node.hasRightChild())
        self.assertTrue(self._3nodes.hasRightChild())

    def test_getData(self) -> None:
        self.assertEqual(self._1node.data(), 'a')

        self.assertEqual(self._3nodes.data(), 'a')
        self.assertEqual(self._3nodes.leftChild().data(), 'b')
        self.assertEqual(self._3nodes.rightChild().data(), 'c')

        self.assertEqual(self._6nodes.data(), 'a')
        self.assertEqual(self._6nodes.leftChild().data(), 'b')
        self.assertEqual(self._6nodes.rightChild().data(), 'c')
        self.assertEqual(self._6nodes.leftChild().rightChild().data(), 'd')
        self.assertEqual(self._6nodes.rightChild().leftChild().data(), 'e')
        self.assertEqual(self._6nodes.rightChild().rightChild().data(), 'f')

    def test_addLeft_noChild(self) -> None:
        self.assertFalse(self._1node.hasLeftChild())
        self._1node.addLeft('z')
        self.assertTrue(self._1node.hasLeftChild())
        self.assertEqual(self._1node.leftChild().data(), 'z')

    def test_addLeft_Child(self) -> None:
        self.assertTrue(self._3nodes.hasLeftChild())
        self.assertEqual(self._3nodes.leftChild().data(), 'b')
        self.assertFalse(self._3nodes.leftChild().hasLeftChild())

        self._3nodes.addLeft('x')
        self.assertTrue(self._3nodes.hasLeftChild())
        self.assertEqual(self._3nodes.leftChild().data(), 'x')
        self.assertTrue(self._3nodes.leftChild().hasLeftChild())
        self.assertEqual(self._3nodes.leftChild().leftChild().data(), 'b')

    def test_addRight_noChild(self) -> None:
        self.assertFalse(self._1node.hasRightChild())
        self._1node.addRight('y')
        self.assertTrue(self._1node.hasRightChild())
        self.assertEqual(self._1node.rightChild().data(), 'y')

    def test_addRight_Child(self) -> None:
        self.assertTrue(self._3nodes.hasRightChild())
        self.assertEqual(self._3nodes.rightChild().data(), 'c')
        self.assertFalse(self._3nodes.rightChild().hasRightChild())

        self._3nodes.addRight('w')
        self.assertTrue(self._3nodes.hasRightChild())
        self.assertEqual(self._3nodes.rightChild().data(), 'w')
        self.assertTrue(self._3nodes.rightChild().hasRightChild())
        self.assertEqual(self._3nodes.rightChild().rightChild().data(), 'c')

    def test_len(self) -> None:
        self.assertEqual(len(self._1node), 1)  
        self.assertEqual(len(self._3nodes), 3)  
        self.assertEqual(len(self._6nodes), 6)

    def test_preorder(self) -> None:
        self.assertEqual(self._1node.preorder(), cast(List[str], ['a']))
        self.assertEqual(self._3nodes.preorder(), cast(List[str], ['a', 'b', 'c']))
        self.assertEqual(self._6nodes.preorder(), cast(List[str], ['a', 'b', 'd', 'c', 'e', 'f']))

    def test_inorder(self) -> None:
        self.assertEqual(self._1node.inorder(), cast(List[str], ['a']))
        self.assertEqual(self._3nodes.inorder(), cast(List[str], ['b', 'a', 'c']))
        self.assertEqual(self._6nodes.inorder(), cast(List[str], ['b', 'd', 'a', 'e', 'c', 'f']))

    def test_postorder(self) -> None:
        self.assertEqual(self._1node.postorder(), cast(List[str], ['a']))
        self.assertEqual(self._3nodes.postorder(), cast(List[str], ['b', 'c', 'a']))
        self.assertEqual(self._6nodes.postorder(), cast(List[str], ['d', 'b', 'e', 'f', 'c', 'a']))

if __name__ == '__main__':
    unittest.main()