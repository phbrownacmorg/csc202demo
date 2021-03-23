# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
from stack_apps import balancedDelims, baseConvert

class TestStackApps(unittest.TestCase):
    # ------------------ Balanced delimiters ----------------------------------

    def test_balanced1(self) -> None:
        self.assertTrue(balancedDelims('{ { ( [ ] [ ] ) } ( ) }'))

    def test_balanced2(self) -> None:
        self.assertTrue(balancedDelims('[ [ { { ( ( ) ) } } ] ]'))

    def test_balanced3(self) -> None:
        self.assertTrue(balancedDelims('[ ] [ ] [ ] ( ) { }'))

    def test_imbalancedType(self) -> None:
        self.assertFalse(balancedDelims('( [ ) ]'))
    
    def test_imbalanced2(self) -> None:
        self.assertFalse(balancedDelims('( ( ( ) ] ) )'))

    def test_imbalanced3(self) -> None:
        self.assertFalse(balancedDelims('[ { ( ) ]'))

    def test_imbalancedFewRight(self) -> None:
        self.assertFalse(balancedDelims('( ( )'))

    def test_imbalancedFewLeft(self) -> None:
        self.assertFalse(balancedDelims('( ) )'))

    def test_imbalancedOrder(self) -> None:
        self.assertFalse(balancedDelims(') ('))

    def test_balanced_empty(self) -> None:
        self.assertTrue(balancedDelims(''))

    # ------------------------- Base conversions ------------------------------

    def test_233_2(self) -> None:
        self.assertEqual(baseConvert(233, 2), '11101001')

    def test_233_8(self) -> None:
        self.assertEqual(baseConvert(233, 8), '351')

    def test_233_16(self) -> None:
        self.assertEqual(baseConvert(233, 16), 'e9')

    def test_233_26(self) -> None:
        self.assertEqual(baseConvert(233, 26), '8p')

    def test_25_2(self) -> None:
        self.assertEqual(baseConvert(25, 2), '11001')

    def test_25_8(self) -> None:
        self.assertEqual(baseConvert(25, 8), '31')

    def test_25_16(self) -> None:
        self.assertEqual(baseConvert(25, 16), '19')

    def test_25_26(self) -> None:
        self.assertEqual(baseConvert(25, 26), 'p')

    def test_256_2(self) -> None:
        self.assertEqual(baseConvert(256, 2), '100000000')
    
    def test_256_8(self) -> None:
        self.assertEqual(baseConvert(256, 8), '400')

    def test_256_16(self) -> None:
        self.assertEqual(baseConvert(256, 16), '100')
    
    def test_256_26(self) -> None:
        self.assertEqual(baseConvert(256, 26), '9m')

    def test_26_2(self) -> None:
        self.assertEqual(baseConvert(26, 2), '11010')

    def test_26_8(self) -> None:
        self.assertEqual(baseConvert(26, 8), '32')

    def test_26_16(self) -> None:
        self.assertEqual(baseConvert(26, 16), '1a')

    def test_26_26(self) -> None:
        self.assertEqual(baseConvert(26, 26), '10')

    def test_0_10(self) -> None:
        self.assertEqual(baseConvert(0, 10), '0')

    def test_big_base(self) -> None:
        with self.assertRaises(AssertionError):
            baseConvert(233, 37)

    def test_small_base(self) -> None:
        with self.assertRaises(AssertionError):
            baseConvert(233, 1)

    def test_neg_num(self) -> None:
        with self.assertRaises(AssertionError):
            baseConvert(-1, 16)


if __name__ == '__main__':
    unittest.main()