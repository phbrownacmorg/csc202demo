import unittest
from UnoCard import UnoCard
from typing import List

class TestUnoCard(unittest.TestCase):
    def test_construction(self) -> None:
        # Uses the postcondition in the constructor to test different suits and ranks.
        # The point is that the postcondition will trigger an error if the suit (or rank)
        #    doesn't work.
        card:UnoCard = UnoCard('green', 5)
        card = UnoCard('blue', 0)
        card = UnoCard('yellow', 12)
        self.assertTrue(card._invariant())

    def test_constructor_pre_bad_suit(self) -> None:
        with self.assertRaises(AssertionError):
            card:UnoCard = UnoCard('bones', 5)
        
    def test_constructor_pre_low_rank(self) -> None:
        with self.assertRaises(AssertionError):
            card:UnoCard = UnoCard('green', -1)

    def test_constructor_pre_low_wild_rank(self) -> None:
        with self.assertRaises(AssertionError):
            card:UnoCard = UnoCard('wild', 5)

    def test_constructor_pre_high_rank(self) -> None:
        with self.assertRaises(AssertionError):
            card:UnoCard = UnoCard('blue', 15)

    def test_constructor_pre_high_color_rank(self) -> None:
        with self.assertRaises(AssertionError):
            card:UnoCard = UnoCard('blue', 13)

    def test_rank(self) -> None:
        self.assertEqual(UnoCard('yellow', 5).rank(), 5)

    def test_suit(self) -> None:
        self.assertEqual(UnoCard('red', 5).suit(), 'Red')

    # def test_str_ace(self) -> None:
    #     self.assertEqual(str(UnoCard('spades', 1)), 'Ace of Spades')

    # def test_str_jack(self) -> None:
    #     self.assertEqual(str(UnoCard('diamonds', 11)), 'Jack of Diamonds')

    # def test_str_queen(self) -> None:
    #     self.assertEqual(str(UnoCard('hearts', 12)), 'Queen of Hearts')

    # def test_str_king(self) -> None:
    #     self.assertEqual(str(UnoCard('clubs', 13)), 'King of Clubs')

    # def test_str_number(self) -> None:
    #     self.assertEqual(str(UnoCard('hearts', 5)), '5 of Hearts')

    # def test_lt_diff_ranks(self) -> None:
    #     self.assertTrue(UnoCard('hearts', 5) < UnoCard('hearts', 13))
    
    # def test_lt_suits_equal(self) -> None:
    #     self.assertTrue(UnoCard('hearts', 5) < UnoCard('spades', 5))

    # def test_lt_ranks_reversed(self) -> None:
    #     self.assertTrue(UnoCard('hearts', 5) < UnoCard('clubs', 6))

    # def test_makeDeck(self) -> None:
    #     deck:List[UnoCard] = UnoCard.makeDeck()
    #     self.assertEqual(len(deck), 52)
    #     for i in range(52):
    #         for j in range(52):
    #             with self.subTest(k = 52*i + j):
    #                 # No two distinct cards in the deck are equal
    #                 # AKA for all i != j, deck[i] != deck[j] 
    #                 self.assertTrue(i == j or deck[i] != deck[j])

if __name__ == '__main__':
    unittest.main()