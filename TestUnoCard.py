import unittest
from AbstractCard import AbstractCard
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
            UnoCard('bones', 5)
        
    def test_constructor_pre_low_rank(self) -> None:
        with self.assertRaises(AssertionError):
            UnoCard('green', -1)

    def test_constructor_pre_low_wild_rank(self) -> None:
        with self.assertRaises(AssertionError):
            UnoCard('wild', 5)

    def test_constructor_pre_high_rank(self) -> None:
        with self.assertRaises(AssertionError):
            UnoCard('blue', 15)

    def test_constructor_pre_high_color_rank(self) -> None:
        with self.assertRaises(AssertionError):
            UnoCard('blue', 13)

    def test_rank(self) -> None:
        self.assertEqual(UnoCard('yellow', 5).rank(), 5)

    def test_suit(self) -> None:
        self.assertEqual(UnoCard('red', 5).suit(), 'Red')

    def test_str_skip(self) -> None:
        self.assertEqual(str(UnoCard('green', 10)), 'Green Skip')

    def test_str_reverse(self) -> None:
        self.assertEqual(str(UnoCard('Yellow', 11)), 'Yellow Reverse')

    def test_str_draw2(self) -> None:
        self.assertEqual(str(UnoCard('red', 12)), 'Red Draw Two')

    def test_str_wild(self) -> None:
        self.assertEqual(str(UnoCard('Wild', 13)), 'Wild')

    def test_str_draw4(self) -> None:
        self.assertEqual(str(UnoCard('wild', 14)), 'Wild Draw Four')

    def test_str_number(self) -> None:
        self.assertEqual(str(UnoCard('blue', 5)), 'Blue 5')

    def test_lt_diff_ranks(self) -> None:
        self.assertTrue(UnoCard('yellow', 5) < UnoCard('yellow', 6))
    
    def test_lt_ranks_equal(self) -> None:
        self.assertTrue(UnoCard('green', 5) < UnoCard('red', 5))

    def test_lt_ranks_reversed(self) -> None:
        self.assertTrue(UnoCard('red', 5) < UnoCard('green', 6))

    def test_nlt_diff_ranks(self) -> None:
        self.assertFalse(UnoCard('yellow', 5) < UnoCard('yellow', 5))
    
    def test_nlt_ranks_equal(self) -> None:
        self.assertFalse(UnoCard('red', 5) < UnoCard('green', 5))

    def test_nlt_ranks_reversed(self) -> None:
        self.assertFalse(UnoCard('green', 6) < UnoCard('red', 5))
    
    def test_eq_yes(self) -> None:
        self.assertTrue(UnoCard('yellow', 5) == UnoCard('yellow', 5))

    def test_eq_no_rank(self) -> None:
        self.assertFalse(UnoCard('yellow', 5) == UnoCard('yellow', 4))

    def test_eq_no_suit(self) -> None:
        self.assertFalse(UnoCard('yellow', 5) == UnoCard('blue', 5))

    def test_ne_yes(self) -> None:
        self.assertFalse(UnoCard('yellow', 5) != UnoCard('yellow', 5))

    def test_ne_no_rank(self) -> None:
        self.assertTrue(UnoCard('yellow', 5) != UnoCard('yellow', 4))

    def test_ne_no_suit(self) -> None:
        self.assertTrue(UnoCard('yellow', 5) != UnoCard('blue', 5))

    def test_ngt_diff_ranks(self) -> None:
        self.assertFalse(UnoCard('yellow', 5) > UnoCard('yellow', 5))
    
    def test_ngt_ranks_equal(self) -> None:
        self.assertFalse(UnoCard('green', 5) > UnoCard('red', 5))

    def test_ngt_ranks_reversed(self) -> None:
        self.assertFalse(UnoCard('red', 5) > UnoCard('green', 6))

    def test_gt_diff_ranks(self) -> None:
        self.assertTrue(UnoCard('yellow', 6) > UnoCard('yellow', 5))
    
    def test_gt_ranks_equal(self) -> None:
        self.assertTrue(UnoCard('red', 5) > UnoCard('green', 5))

    def test_gt_ranks_reversed(self) -> None:
        self.assertTrue(UnoCard('green', 6) > UnoCard('red', 5))
    
    def test_nge_diff_ranks(self) -> None:
        self.assertFalse(UnoCard('yellow', 5) >= UnoCard('yellow', 6)) # type: ignore # @total_ordering
    
    def test_nge_ranks_equal(self) -> None:
        self.assertFalse(UnoCard('green', 5) >= UnoCard('red', 5)) # type: ignore # @total_ordering

    def test_nge_ranks_reversed(self) -> None:
        self.assertFalse(UnoCard('red', 5) >= UnoCard('green', 6)) # type: ignore # @total_ordering

    def test_ge_diff_ranks(self) -> None:
        self.assertTrue(UnoCard('yellow', 5) >= UnoCard('yellow', 5)) # type: ignore # @total_ordering
    
    def test_ge_ranks_equal(self) -> None:
        self.assertTrue(UnoCard('red', 5) >= UnoCard('green', 5)) # type: ignore # @total_ordering

    def test_ge_ranks_reversed(self) -> None:
        self.assertTrue(UnoCard('green', 6) >= UnoCard('red', 5)) # type: ignore # @total_ordering

    def test_nle_diff_ranks(self) -> None:
        self.assertFalse(UnoCard('yellow', 6) <= UnoCard('yellow', 5)) # type: ignore # @total_ordering
    
    def test_nle_ranks_equal(self) -> None:
        self.assertFalse(UnoCard('red', 5) <= UnoCard('green', 5)) # type: ignore # @total_ordering

    def test_nle_ranks_reversed(self) -> None:
        self.assertFalse(UnoCard('green', 6) <= UnoCard('red', 5)) # type: ignore # @total_ordering

    def test_le_diff_ranks(self) -> None:
        self.assertTrue(UnoCard('yellow', 5) <= UnoCard('yellow', 5)) # type: ignore # @total_ordering
    
    def test_le_ranks_equal(self) -> None:
        self.assertTrue(UnoCard('green', 5) <= UnoCard('red', 5)) # type: ignore # @total_ordering

    def test_le_ranks_reversed(self) -> None:
        self.assertTrue(UnoCard('red', 5) <= UnoCard('green', 6)) # type: ignore # @total_ordering

    def test_makeDeck(self) -> None:
        deck:List[AbstractCard] = UnoCard.makeDeck()
        self.assertEqual(len(deck), 108)

        for suit in UnoCard._COLOR_SUITS:
            with self.subTest(suit=suit):
                self.assertEqual(deck.count(UnoCard(suit, 0)), 1)
            # Other color cards
            for rank in UnoCard._COLOR_RANKS[1:]:
                with self.subTest(suit=suit, rank=rank):
                    self.assertEqual(deck.count(UnoCard(suit, rank)), 2)
        # Wild cards
        for rank in UnoCard._WILD_RANKS:
            with self.subTest(rank=rank):
                self.assertEqual(deck.count(UnoCard('Wild', rank)), 4)
                    
        # for i in range(52):
        #     for j in range(52):
        #         with self.subTest(k = 52*i + j):
        #             # No two distinct cards in the deck are equal
        #             # AKA for all i != j, deck[i] != deck[j] 
        #             self.assertTrue(i == j or deck[i] != deck[j])

if __name__ == '__main__':
    unittest.main()