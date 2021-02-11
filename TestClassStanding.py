# Empty unit-testing class
# Peter Brown, 26 Jan 2017

from class_standing import *
import unittest

class TestNothing(unittest.TestCase):
    def test_negative(self) -> None:
        self.assertEqual(class_status(-1), 'NO status: invalid input')

    def test_min_freshman(self) -> None:
        self.assertEqual(class_status(0), 'freshman status')        

    def test_normal_freshman(self) -> None:
        self.assertEqual(class_status(10), 'freshman status')        

    def test_max_freshman(self) -> None:
        self.assertEqual(class_status(23.9999999999), 'freshman status')
    
    def test_min_sophomore(self) -> None:
        self.assertEqual(class_status(24), 'sophomore status')

    def test_normal_sophomore(self) -> None:
        self.assertEqual(class_status(40), 'sophomore status')
        
    def test_max_sophomore(self) -> None:
        self.assertEqual(class_status(55.99999999999), 'sophomore status')
    
    def test_min_junior(self) -> None:
        self.assertEqual(class_status(56), 'junior status')

    def test_normal_junior(self) -> None:
        self.assertEqual(class_status(70), 'junior status')

    def test_max_junior(self) -> None:
        self.assertEqual(class_status(86.999999999999), 'junior status')

    def test_min_senior(self) -> None:
        self.assertEqual(class_status(87), 'senior status')

    def test_normal_senior(self) -> None:
        self.assertEqual(class_status(120), 'senior status')

    def test_overachieving_senior(self) -> None:
        self.assertEqual(class_status(320), 'senior status')


if __name__ == '__main__':
    unittest.main()