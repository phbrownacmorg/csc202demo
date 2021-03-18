# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
from Stack import Stack

class TestStack(unittest.TestCase):

    def setUp(self) -> None:
        self.emptyStack:Stack[str] = Stack[str]()

        self.oneItem:Stack[str] = Stack[str]()
        self.oneItem.push('foo')

        self.twoItems:Stack[str] = Stack[str]()
        self.twoItems.push('foo')
        self.twoItems.push('bar')

    def test_isEmptyTrue(self) -> None:
        self.assertTrue(self.emptyStack.isEmpty())

    def testIsEmptyFalse(self) -> None:
        self.assertFalse(self.oneItem.isEmpty())
        self.assertFalse(self.twoItems.isEmpty())

    def testPopTwo(self) -> None:
        self.assertEqual(self.twoItems.pop(), 'bar')
        self.assertFalse(self.twoItems.isEmpty())
        self.assertEqual(self.twoItems.pop(), 'foo')
        self.assertTrue(self.twoItems.isEmpty())

    def testPopEmpty(self) -> None:
        with self.assertRaises(AssertionError):
            self.emptyStack.pop()

    def testPushTwo(self) -> None:
        self.assertTrue(self.emptyStack.isEmpty())
        self.emptyStack.push('bar')
        self.assertFalse(self.emptyStack.isEmpty())
        self.emptyStack.push('foo')
        self.assertFalse(self.emptyStack.isEmpty())
        self.assertEqual(self.emptyStack.pop(), 'foo')
        self.assertFalse(self.emptyStack.isEmpty())
        self.assertEqual(self.emptyStack.pop(), 'bar')
        self.assertTrue(self.emptyStack.isEmpty())

if __name__ == '__main__':
    unittest.main()