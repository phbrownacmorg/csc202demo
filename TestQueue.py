# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
from CircQ import Queue

class TestQueue(unittest.TestCase):

    def setUp(self) -> None:
        self.emptyQ:Queue[str] = Queue[str]()

        self.oneItem:Queue[str] = Queue[str]()
        self.oneItem.enqueue('foo')

        self.twoItems:Queue[str] = Queue[str]()
        self.twoItems.enqueue('foo')
        self.twoItems.enqueue('bar')

    def test_isEmptyTrue(self) -> None:
        self.assertTrue(self.emptyQ.isEmpty())

    def testIsEmptyFalse(self) -> None:
        self.assertFalse(self.oneItem.isEmpty())
        self.assertFalse(self.twoItems.isEmpty())

    def testdequeueTwo(self) -> None:
        self.assertEqual(self.twoItems.dequeue(), 'foo')
        self.assertFalse(self.twoItems.isEmpty())
        self.assertEqual(self.twoItems.dequeue(), 'bar')
        self.assertTrue(self.twoItems.isEmpty())

    def testPopEmpty(self) -> None:
        with self.assertRaises(AssertionError):
            self.emptyQ.dequeue()

    def testEnqueueTwo(self) -> None:
        self.assertTrue(self.emptyQ.isEmpty())
        self.emptyQ.enqueue('bar')
        self.assertFalse(self.emptyQ.isEmpty())
        self.emptyQ.enqueue('foo')
        self.assertFalse(self.emptyQ.isEmpty())
        self.assertEqual(self.emptyQ.dequeue(), 'bar')
        self.assertFalse(self.emptyQ.isEmpty())
        self.assertEqual(self.emptyQ.dequeue(), 'foo')
        self.assertTrue(self.emptyQ.isEmpty())

if __name__ == '__main__':
    unittest.main()