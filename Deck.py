from AbstractCard import AbstractCard
from typing import Iterable, List
import random

class Deck(object):
    """Class to represent a deck of cards."""

    def _invariant(self) -> bool:
        """Class invariant."""
        valid:bool = True
        for c in self._cards:
            if not isinstance(c, AbstractCard):
                valid = False
        return valid

    def __init__(self, cards:Iterable[AbstractCard]):
        """Initialize the Deck with the given cards."""
        # Pre: cards is a list of AbstractCard
        self._cards:List[AbstractCard] = list(cards)
        # Post:
        assert self._invariant()

    # QUERY METHODS

    def __len__(self) -> int:
        """How many cards are in the deck?"""
        return len(self._cards)

    def isEmpty(self) -> bool:
        """Is the deck empty?"""
        return len(self) == 0

    def __str__(self) -> str:
        result:str = "Deck:\n"
        for c in self._cards:
            result += '\t' + str(c) + '\n'
        return result

    # MUTATOR METHODS
    def deal(self) -> AbstractCard:
        """ Deal a card off the top of the deck."""
        # Pre:
        assert (not self.isEmpty())
        return self._cards.pop()

    def shuffle(self) -> None:
        """Shuffle the deck in place."""
        for i in range(len(self._cards)-1, 0, -1):
            swapIndex = random.randint(0, i)
            self._cards[i], self._cards[swapIndex] = self._cards[swapIndex], self._cards[i]
    
    def deal_random(self) -> AbstractCard:
        """Deal off a card from a random position in the deck."""
        return self.deal()