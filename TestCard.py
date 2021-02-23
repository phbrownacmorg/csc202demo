# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import unittest
from PlayingCard import PlayingCard
from typing import List

class TestCard(unittest.TestCase):
    def test_construction(self) -> None:
        # Uses the postcondition in the constructor to test different suits and ranks.
        # The point is that the postcondition will trigger an error if the suit (or rank)
        #    doesn't work.
        card:PlayingCard = PlayingCard('hearts', 5)
        card = PlayingCard('spades', 1)
        card = PlayingCard('clubs', 13)
        self.assertTrue(card._invariant())

    def test_constructor_pre_bad_suit(self) -> None:
        with self.assertRaises(AssertionError):
            card:PlayingCard = PlayingCard('bones', 5)
        
    def test_constructor_pre_low_rank(self) -> None:
        with self.assertRaises(AssertionError):
            card:PlayingCard = PlayingCard('hearts', 0)

    def test_constructor_pre_high_rank(self) -> None:
        with self.assertRaises(AssertionError):
            card:PlayingCard = PlayingCard('hearts', 14)

    def test_rank(self) -> None:
        self.assertEqual(PlayingCard('diamonds', 5).rank(), 5)

    def test_suit(self) -> None:
        self.assertEqual(PlayingCard('Hearts', 5).suit(), 'Hearts')

    def test_str_ace(self) -> None:
        self.assertEqual(str(PlayingCard('spades', 1)), 'Ace of Spades')

    def test_str_jack(self) -> None:
        self.assertEqual(str(PlayingCard('diamonds', 11)), 'Jack of Diamonds')

    def test_str_queen(self) -> None:
        self.assertEqual(str(PlayingCard('hearts', 12)), 'Queen of Hearts')

    def test_str_king(self) -> None:
        self.assertEqual(str(PlayingCard('clubs', 13)), 'King of Clubs')

    def test_str_number(self) -> None:
        self.assertEqual(str(PlayingCard('hearts', 5)), '5 of Hearts')

    def test_lt_diff_ranks(self) -> None:
        self.assertTrue(PlayingCard('hearts', 5) < PlayingCard('hearts', 13))
    
    def test_lt_suits_equal(self) -> None:
        self.assertTrue(PlayingCard('hearts', 5) < PlayingCard('spades', 5))

    def test_lt_ranks_reversed(self) -> None:
        self.assertTrue(PlayingCard('hearts', 5) < PlayingCard('clubs', 6))

    def test_makeDeck(self) -> None:
        deck:List[PlayingCard] = PlayingCard.makeDeck()
        self.assertEqual(len(deck), 52)
        for i in range(52):
            for j in range(52):
                with self.subTest(k = 52*i + j):
                    # No two distinct cards in the deck are equal
                    # AKA for all i != j, deck[i] != deck[j] 
                    self.assertTrue(i == j or deck[i] != deck[j])

if __name__ == '__main__':
    unittest.main()