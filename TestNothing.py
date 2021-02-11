# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
class TestNothing(unittest.TestCase):
    def test_nothing(self) -> None:
        self.assertTrue(True)
        
if __name__ == '__main__':
    unittest.main()