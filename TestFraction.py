# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
from Fraction import Fraction

class TestFraction(unittest.TestCase):
    def test_GCD(self) -> None:
        self.assertEqual(Fraction._gcd(12, 15), 3)
        self.assertEqual(Fraction._gcd(15, 12), 3)
        self.assertEqual(Fraction._gcd(4, 3), 1)
        self.assertEqual(Fraction._gcd(3, 4), 1)
        self.assertEqual(Fraction._gcd(3, 0), 3)
        self.assertEqual(Fraction._gcd(0, 3), 3)
        self.assertEqual(Fraction._gcd(-12, 15), 3)
        self.assertEqual(Fraction._gcd(-12, -15), 3)
        self.assertEqual(Fraction._gcd(12, -15), 3)

    def test_constructor(self) -> None:
        frac:Fraction = Fraction(1, 2)
        self.assertTrue(frac.numerator() == 1 and frac.denominator() == 2)
        frac = Fraction(9, 18)
        self.assertTrue(frac.numerator() == 1 and frac.denominator() == 2)
        frac = Fraction(1, -2)
        self.assertTrue(frac.numerator() == -1 and frac.denominator() == 2)
        frac = Fraction(-1, -2)
        self.assertTrue(frac.numerator() == 1 and frac.denominator() == 2)

    def test_str_(self) -> None:
        self.assertEqual(str(Fraction(1, 2)), "1/2")
        self.assertEqual(str(Fraction(3, 2)), "3/2")

    def test_eq(self) -> None:
        self.assertTrue(Fraction(1,2) == Fraction(1,2)) # Uses __eq__ for ==
        self.assertTrue(Fraction(1,2) == Fraction(9,18))  
        self.assertEqual(Fraction(-12, -15), Fraction(4, 5)) # Uses __eq__ for assertEqual

    def test_add(self) -> None:
        # self._denom == other._denom
        self.assertEqual(Fraction(1,5) + Fraction(2,5), Fraction(3,5)) 
        # self._denom != other._denom and result._denom == self._denom * other._denom
        self.assertEqual(Fraction(1,2) + Fraction(1,3), Fraction(5, 6))  
        # self._denom != other._denom and result._denom != self._denom * other._denom
        self.assertEqual(Fraction(1,6) + Fraction(1,3), Fraction(1,2))

if __name__ == '__main__':
    unittest.main()