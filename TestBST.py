# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
from BST import BST
from typing import cast, List

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

        self.assertEqual(self._3nodes.leftChild().findSuccessor().data(), 34)   # type: ignore
        self.assertEqual(self._3nodes.findSuccessor().data(), 47)               # type: ignore
        self.assertEqual(self._3nodes.rightChild().findSuccessor(), None)       # type: ignore

        self.assertEqual(self._6nodes.leftChild().leftChild().findSuccessor().data(), 15)               # type: ignore
        self.assertEqual(self._6nodes.leftChild().leftChild().rightChild().findSuccessor().data(), 31)  # type: ignore
        self.assertEqual(self._6nodes.leftChild().findSuccessor().data(), 34)                           # type: ignore
        self.assertEqual(self._6nodes.findSuccessor().data(), 47)                                       # type: ignore
        self.assertEqual(self._6nodes.rightChild().findSuccessor().data(), 70)                          # type: ignore
        self.assertEqual(self._6nodes.rightChild().rightChild().findSuccessor(), None)                  # type: ignore

    def testRemove_1node(self) -> None:
        self.assertFalse(self._1node.isEmpty())
        self._1node.remove(31) # Nothing happens
        self.assertFalse(self._1node.isEmpty())
        self._1node.remove(34) # Deletes the root, leaving an empty tree
        self.assertTrue(self._1node.isEmpty())

    def test_remove_3nodes_left(self) -> None:
        self._3nodes.remove(31)
        self.assertFalse(31 in self._3nodes)                    # 31 is no longer in the tree
        self.assertEqual(self._3nodes.data(), 34)               # Root should be 34
        self.assertEqual(self._3nodes.rightChild().data(), 47)  # Right child should be 47
        self.assertEqual(len(self._3nodes), 2)                  # That should be the whole tree

    def test_remove_3nodes_right(self) -> None:
        self._3nodes.remove(47)
        self.assertFalse(47 in self._3nodes)                    # 47 is no longer in the tree
        self.assertEqual(self._3nodes.data(), 34)               # Root should be 34
        self.assertEqual(self._3nodes.leftChild().data(), 31)   # Left child should be 31
        self.assertEqual(len(self._3nodes), 2)                  # That should be the whole tree

    def test_remove_3nodes_root(self) -> None:
        self._3nodes.remove(34)
        self.assertFalse(34 in self._3nodes)                    # 34 is no longer in the tree
        self.assertEqual(self._3nodes.data(), 47)               # Root should be 47
        self.assertEqual(self._3nodes.leftChild().data(), 31)   # Left child should be 31
        self.assertEqual(len(self._3nodes), 2)                  # That should be the whole tree

    def test_remove_6nodes_left(self) -> None:
        self._6nodes.remove(31)
        self.assertFalse(31 in self._6nodes)
        self.assertEqual(self._6nodes.data(), 34)               # Root should be 34
        self.assertEqual(self._6nodes.leftChild().data(), 6)    # Left child should be 31
        self.assertEqual(self._6nodes.inorder(), cast(List[int], [6, 15, 34, 47, 70]))                  # That should be the whole tree

    def test_remove_6nodes_right(self) -> None:
        self._6nodes.remove(47)
        self.assertFalse(47 in self._6nodes)
        self.assertEqual(self._6nodes.data(), 34)               # Root should be 34
        self.assertEqual(self._6nodes.rightChild().data(), 70)  # Right child should be 70
        self.assertEqual(self._6nodes.inorder(), cast(List[int], [6, 15, 31, 34, 70]))                  # That should be the whole tree

    def test_remove_6nodes_root(self) -> None:
        self._6nodes.remove(34)
        self.assertFalse(34 in self._6nodes)
        self.assertEqual(self._6nodes.data(), 47)               # Root should be 47
        self.assertEqual(self._6nodes.rightChild().data(), 70)  # Right child should be 70
        self.assertEqual(self._6nodes.inorder(), cast(List[int], [6, 15, 31, 47, 70]))                  # That should be the whole tree


if __name__ == '__main__':
    unittest.main()