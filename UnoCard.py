from AbstractCard import AbstractCard
from functools import total_ordering
from typing import List, Tuple

@total_ordering
class UnoCard(AbstractCard):
    """Class to represent an Uno card."""

    # Inherits AbstractCard._MIN_RANK
    _COLOR_RANKS:List[int] = list(range(13))
    _WILD_RANKS:List[int] = [13, 14]
    _RANKS = _COLOR_RANKS + _WILD_RANKS # Overriddes 
    _MAX_RANK = len(_RANKS)             # Overrides
    _COLOR_SUITS:List[str] = ['Red', 'Yellow', 'Green', 'Blue']
    _WILD_SUITS:List[str] = ['Wild']
    _SUITS:List[str] = _COLOR_SUITS + _WILD_SUITS # Overrides
    _RANK_NAMES:List[str] = list(map(str, range(10))) + \
        ['Skip', 'Reverse', 'Draw Two', '', 'Draw Four']   # Overrides

    # Overriddes
    def _invariant(self) -> bool:
        """Class invariant."""
        return (self.suit() in self._WILD_SUITS and self.rank() in self._WILD_RANKS) or \
            (self.suit() in self._COLOR_SUITS and self.rank() in self._COLOR_RANKS)

    # Overrides
    def __init__(self, suit:str, rank:int) -> None:
        """Constructor for an UnoCard."""
        # Pre:
        assert (suit.title() == 'Wild' and rank in UnoCard._WILD_RANKS) or \
            (suit.title() in UnoCard._COLOR_SUITS and rank in UnoCard._COLOR_RANKS)
        super().__init__(suit, rank)
        # Post:
        assert self._invariant()

    # Inherits rank(), suit(), __str__(), __eq__(), __lt__()

    # Overrides (sort of)
    @staticmethod
    def makeDeck() -> List[AbstractCard]:
        """Make and return a list with all the cards in a standard Uno deck."""
        return []