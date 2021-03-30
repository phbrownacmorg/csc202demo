# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
from palindrome import interesting, palindrome

class TestNothing(unittest.TestCase):
    def test_nothing(self) -> None:
        self.assertTrue(palindrome(''))
        
    def test_1letter(self) -> None:
        self.assertTrue(palindrome('a'))

    def test_2letters_yes(self) -> None:
        self.assertTrue(palindrome('aa'))

    def test_2letters_no(self) -> None:
        self.assertFalse(palindrome('ab'))

    def test_2letters_case(self) -> None:
        self.assertTrue(palindrome('Aa'))

    def test_2letters_space(self) -> None:
        self.assertTrue(palindrome(' Aa'))
    
    def test_tacocat(self) -> None:
        self.assertTrue(palindrome('tacocat'))

    def test_TR(self) -> None:
        self.assertTrue(palindrome('A man, a plan, a canal: Panama!'))

    def test_interesting_a(self) -> None:
        self.assertTrue(interesting('a'))

    def test_interesting_z(self) -> None:
        self.assertTrue(interesting('z'))

    def test_interesting_A(self) -> None:
        self.assertTrue(interesting('A'))

    def test_interesting_Z(self) -> None:
        self.assertTrue(interesting('Z'))

    def test_interesting_0(self) -> None:
        self.assertTrue(interesting('0'))

    def test_interesting_9(self) -> None:
        self.assertTrue(interesting('9'))

    def test_interesting_space(self) -> None:
        self.assertFalse(interesting(' '))

    def test_interesting_slash(self) -> None:
        self.assertFalse(interesting('/'))

    def test_interesting_lsqbr(self) -> None:
        self.assertFalse(interesting('['))

    def test_interesting_backquo(self) -> None:
        self.assertFalse(interesting('`'))

    def test_interesting_lsquig(self) -> None:
        self.assertFalse(interesting('{'))

    def test_interesting_tilde(self) -> None:
        self.assertFalse(interesting('~'))

if __name__ == '__main__':
    unittest.main()