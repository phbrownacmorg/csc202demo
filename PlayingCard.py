# Class to represent a playing card
# Peter Brown <peter.brown@converse.edu>, 2021-02-23

from AbstractCard import AbstractCard
from functools import total_ordering
from typing import List, Tuple

@total_ordering
class PlayingCard(AbstractCard):
    """Class to represent a playing card.  Objects of this type are immutable.  
    Assume aces are low."""

    _MIN_RANK:int = 1  # Ace (overridden)
    _MAX_RANK:int = 13 # King (overridden)
    _RANK_NAMES:List[str] = list(map(str, range(_MAX_RANK+1))) # overridden
    _RANK_NAMES[0] = ''
    _RANK_NAMES[1] = 'Ace'
    _RANK_NAMES[11] = 'Jack'
    _RANK_NAMES[12] = 'Queen'
    _RANK_NAMES[13] = 'King'

    _SUITS:List[str] = ['Clubs', 'Diamonds', 'Hearts', 'Spades'] # overridden

    # Class invariant is inherited from AbstractCard (except PlayingCard has 
    # overridden the values for the class constants so the invariant can be
    # true)

    # Overrides AbstractCard.__init__().  (Subclasses almost always override the
    # superclass constructor.)
    def __init__(self, suit:str, rank:int) -> None:
        """Constructs a playing card."""
        super().__init__(suit, rank)
        assert self._invariant()

    # ------ QUERY METHODS -----------------------------------

    # Inherits AbstractCard.rank() and AbstractCard.suit()

    # Overrides AbstractCard.__str__()
    def __str__(self) -> str:
        """Return a string representation of a Card."""
        return str(self._RANK_NAMES[self.rank()] + ' of ' + self.suit())

    # Inherits AbstractCard.__eq__() and AbstractCard.__lt__()
    
    # Overrides AbstractCard.makeDeck() (sort of--it's a static method)
    @staticmethod
    def makeDeck() -> List[AbstractCard]:
        """Return a List of all possible PlayingCards (in fact, the cards that would be found
        in a normal deck, apart from the jokers)."""
        deck:List[AbstractCard] = []
        for suit in PlayingCard._SUITS:
            for rank in range(PlayingCard._MIN_RANK, PlayingCard._MAX_RANK+1):
                deck.append(PlayingCard(suit, rank))
        # Post:
        assert len(deck) == 52 # and no two cards in the deck are equal to each other
        return deck