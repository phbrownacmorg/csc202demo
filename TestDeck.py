# Empty unit-testing class
# Peter Brown, 26 Jan 2017

import random
import unittest
from Deck import Deck
from AbstractCard import AbstractCard
from PlayingCard import PlayingCard
from UnoCard import UnoCard
from typing import List

class TestDeck(unittest.TestCase):

    # setUp runs before each test
    def setUp(self) -> None:
        self.emptyDeck:Deck = Deck([])
        self.deck:Deck = Deck(PlayingCard.makeDeck())

    def test_init(self) -> None:
        self.assertTrue(self.deck._invariant())
        self.assertTrue(self.emptyDeck._invariant())

    def test_len(self) -> None:
        self.assertEqual(len(self.deck), 52)

    def test_deal_one(self) -> None:
        # Should deal the King of Spades
        self.assertEqual(self.deck.deal(), PlayingCard('spades', 13))
        self.assertEqual(len(self.deck), 51)

    def test_deal_all(self) -> None:
        numCards:int = len(self.deck)
        self.assertEqual(numCards, 52)
        for i in range(numCards, 0, -1): # type: int
            with self.subTest(i=i):
                self.assertEqual(i, len(self.deck))
                card:AbstractCard = self.deck.deal()
                self.assertEqual(card.rank() % 13, i % 13)
                self.assertEqual(card.suit(), card._SUITS[(i-1) // 13])
                self.assertEqual(i-1, len(self.deck))

    def test_empty(self) -> None:
        self.assertEqual(len(self.emptyDeck), 0)
        self.assertTrue(self.emptyDeck.isEmpty())
        self.assertFalse(self.deck.isEmpty())

    def test_deal_from_empty(self) -> None:
        with self.assertRaises(AssertionError):
            self.emptyDeck.deal()

    def test_shuffle(self) -> None:
        # Ensure predictability.  Providing any object as a seed works here.
        random.seed("Listening in class is generally a good idea.")
        self.deck.shuffle()
        for i in range(52, 0, -1): # type: int
            with self.subTest(i=i):
                self.assertEqual(i, len(self.deck))
                card:AbstractCard = self.deck.deal()

                # Assert that the cards aren't where they started.  On average, 51 of
                # the 52 will have been moved.  This seed gives exactly that result.
                if i != 3:  # The one exception out of 52 cards
                    self.assertTrue((card.rank() % 13 != i % 13)
                                    or (card.suit() != card._SUITS[(i-1) // 13]))
                else:
                    self.assertTrue((card.rank() % 13 == i % 13)
                                    and (card.suit() == card._SUITS[(i-1) // 13]))
        self.assertTrue(self.deck.isEmpty())

    def test_str(self) -> None:
        expected:str = 'Deck:\n'
        for i in range(52):
            expected += '\t' + PlayingCard._RANK_NAMES[i % 13 + 1] + ' of '
            expected += PlayingCard._SUITS[i // 13] + '\n'
        self.assertEqual(str(self.deck), expected)

    def test_str_empty(self) -> None:
        self.assertEqual(str(self.emptyDeck), 'Deck:\n')

    def test_polymorphism_demo(self) -> None:
        setOfCards:List[AbstractCard] = PlayingCard.makeDeck()[:5]
        for i in range(4):
            setOfCards.append(UnoCard(UnoCard._SUITS[i], i))
        setOfCards.append(UnoCard('Wild', 13))
        mixedDeck:Deck = Deck(setOfCards)
        mixedDeck.shuffle()
        print(str(mixedDeck))
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()